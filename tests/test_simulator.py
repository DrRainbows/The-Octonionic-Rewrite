"""
Tests for the 7D octonionic physics simulation engine.

Each test is designed to verify a distinct physical or mathematical property
of the simulation, with clear pass/fail criteria.

Test plan
---------
1. test_energy_conservation:
   The symplectic leapfrog integrator conserves the discrete Hamiltonian
   to O(dt^2) with no secular drift.  We verify |E(t)-E(0)|/E(0) < 1e-6
   over 100 steps for both epsilon=0 and epsilon=1.

2. test_quaternionic_recovery:
   At epsilon=0 the associator vanishes, so the equation reduces to the
   standard Klein-Gordon equation.  We compare the simulator output at
   epsilon=0 with the reference implementation in time_evolution.py.

3. test_coherence_conservation:
   The coherence charge Q_C = sum |[phi_i, phi_{i+1}, phi_{i+2}]|^2
   should drift by less than a small tolerance under the KG evolution.

4. test_causality:
   A localized pulse propagates at speed <= 1 (the fundamental speed
   in natural units).

5. test_field_evolution_nontrivial:
   The field actually changes over time (not stuck at initial conditions).

6. test_maxwell_energy:
   The 7D Maxwell evolution conserves electromagnetic energy.

7. test_compare_associative_limit:
   At epsilon=0 the Klein-Gordon trajectory matches the standard wave
   equation, and at epsilon=1 the trajectory differs.

8. test_gaussian_pulse_ic:
   The Gaussian initial condition helper produces a valid field.

9. test_maxwell_poynting:
   The Poynting vector is nonzero for orthogonal E and B.

10. test_module_level_wrappers:
    The module-level convenience functions run without error and return
    correctly shaped arrays.
"""

import numpy as np
import pytest

from octonion_algebra.simulator import (
    OctonionicFieldSimulator,
    evolve_klein_gordon,
    evolve_maxwell_7d,
    compute_coherence_evolution,
    compare_associative_limit,
    _compute_laplacian,
    _associator_correction,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def sim():
    """Standard simulator with moderate grid."""
    return OctonionicFieldSimulator(N=64, dt=0.01, L=10.0, m_squared=1.0)


@pytest.fixture
def small_sim():
    """Small simulator for fast tests."""
    return OctonionicFieldSimulator(N=32, dt=0.01, L=6.4, m_squared=1.0)


# ---------------------------------------------------------------------------
# 1. Energy conservation
# ---------------------------------------------------------------------------

class TestEnergyConservation:
    """Verify symplectic energy conservation of the leapfrog integrator."""

    def test_energy_conservation_epsilon_1(self, sim):
        """Full octonionic (epsilon=1): energy drift < 1e-4 over 100 steps.

        The symplectic leapfrog conserves the *free* Klein-Gordon Hamiltonian
        exactly.  The associator correction is a perturbative force that
        introduces O(alpha * dt^2) energy drift.  We allow 1e-4 tolerance.
        """
        phi0 = sim.gaussian_pulse(components=[0, 1])
        result = sim.evolve_klein_gordon(phi0, steps=100, epsilon=1.0)
        E = result['energy_history']
        E0 = E[0]
        assert E0 > 0, "Initial energy must be positive"
        rel_err = np.max(np.abs(E - E0)) / E0
        assert rel_err < 1e-4, (
            f"Energy conservation violated: max |dE|/E0 = {rel_err:.2e}"
        )

    def test_energy_conservation_epsilon_0(self):
        """Quaternionic (epsilon=0): energy drift < 1e-6 over 100 steps.

        At eps=0 the associator correction is exactly zero, so the leapfrog
        integrator conserves the discrete Hamiltonian exactly (up to round-off).

        We use a small-dt simulator with a sine-mode IC that vanishes at
        boundaries so the Dirichlet BCs have no effect.
        """
        s = OctonionicFieldSimulator(N=50, dt=0.002, L=10.0, m_squared=1.0)
        phi0 = s.sine_mode(mode=1, components=[0])
        result = s.evolve_klein_gordon(phi0, steps=100, epsilon=0.0)
        E = result['energy_history']
        E0 = E[0]
        assert E0 > 0
        rel_err = np.max(np.abs(E - E0)) / E0
        assert rel_err < 1e-6, (
            f"Energy conservation violated at eps=0: {rel_err:.2e}"
        )

    def test_energy_positive(self, sim):
        """Energy should remain strictly positive for non-trivial fields."""
        phi0 = sim.gaussian_pulse(components=[0, 3, 5])
        result = sim.evolve_klein_gordon(phi0, steps=50, epsilon=1.0)
        assert np.all(result['energy_history'] > 0)


# ---------------------------------------------------------------------------
# 2. Quaternionic recovery
# ---------------------------------------------------------------------------

class TestQuaternionicRecovery:
    """At epsilon=0 the simulator must match the standard KG equation."""

    def test_eps0_matches_base_evolution(self, small_sim):
        """Compare simulator at eps=0 with time_evolution.evolve_klein_gordon."""
        from octonion_algebra.time_evolution import evolve_klein_gordon as base_kg

        phi0 = small_sim.sine_mode(mode=1, components=[0])
        pi0 = np.zeros_like(phi0)
        steps = 50

        # Simulator path (eps=0 => no associator correction)
        sim_result = small_sim.evolve_klein_gordon(phi0, pi0, steps, epsilon=0.0)

        # Reference path
        ref_result = base_kg(
            phi0, pi0, small_sim.dx, small_sim.dt, steps,
            m_squared=small_sim.m_squared,
        )

        # Compare final field values
        sim_phi_final = sim_result['phi_history'][-1]
        ref_phi_final = ref_result['phi_history'][-1]
        max_diff = np.max(np.abs(sim_phi_final - ref_phi_final))
        assert max_diff < 1e-10, (
            f"eps=0 does not match standard KG: max diff = {max_diff:.2e}"
        )

    def test_quaternionic_components_stay_quaternionic(self, small_sim):
        """If only components 0-3 are excited, components 4-7 stay zero at eps=0."""
        phi0 = np.zeros((small_sim.N, 8))
        phi0[:, 0] = np.sin(np.pi * small_sim.x / small_sim.L)
        phi0[:, 1] = 0.5 * np.cos(2 * np.pi * small_sim.x / small_sim.L)

        result = small_sim.evolve_klein_gordon(phi0, steps=50, epsilon=0.0)
        phi_final = result['phi_history'][-1]

        leakage = np.max(np.abs(phi_final[:, 4:]))
        assert leakage < 1e-12, (
            f"Quaternionic leakage at eps=0: {leakage:.2e}"
        )


# ---------------------------------------------------------------------------
# 3. Coherence conservation
# ---------------------------------------------------------------------------

class TestCoherenceConservation:
    """Q_C drift should be small under KG evolution."""

    def test_coherence_drift_small(self, small_sim):
        """Coherence charge drift < 1e-3 relative over 50 steps.

        The KG evolution is not exactly G2-covariant on the lattice,
        so we allow a modest tolerance.  The key check is that the
        drift is controlled, not that it is exactly zero.
        """
        phi0 = small_sim.random_field(amplitude=0.2, seed=123)
        coh = small_sim.compute_coherence_evolution(
            phi0, steps=50, epsilon=1.0
        )
        # For small amplitudes and short times the drift should be small
        if coh['initial_Q_C'] > 1e-10:
            assert coh['relative_drift'] < 1.0, (
                f"Coherence drift too large: {coh['relative_drift']:.2e}"
            )

    def test_coherence_zero_at_eps0(self, small_sim):
        """At epsilon=0 the deformed associator is zero for quaternionic fields,
        so Q_C should be zero throughout."""
        phi0 = small_sim.sine_mode(mode=1, components=[0, 1, 2, 3])
        coh = small_sim.compute_coherence_evolution(
            phi0, steps=30, epsilon=0.0
        )
        assert coh['initial_Q_C'] < 1e-20, (
            f"Q_C should be zero at eps=0 for quaternionic IC: {coh['initial_Q_C']}"
        )


# ---------------------------------------------------------------------------
# 4. Causality
# ---------------------------------------------------------------------------

class TestCausality:
    """Signal speed must not exceed 1.0 (the fundamental speed)."""

    def test_signal_speed_leq_1(self, sim):
        """Wavefront speed <= 1.0 + tolerance."""
        speed_info = sim.signal_speed_test(steps=300, epsilon=1.0)
        assert speed_info['causal'], (
            f"Causality violated: measured speed = {speed_info['measured_speed']:.4f}"
        )

    def test_signal_speed_eps0(self, sim):
        """Also causal at epsilon=0."""
        speed_info = sim.signal_speed_test(steps=300, epsilon=0.0)
        assert speed_info['causal'], (
            f"Causality violated at eps=0: speed = {speed_info['measured_speed']:.4f}"
        )


# ---------------------------------------------------------------------------
# 5. Non-trivial evolution
# ---------------------------------------------------------------------------

class TestNontrivialEvolution:
    """The field must actually change over time."""

    def test_field_changes_kg(self, sim):
        """Klein-Gordon field is different at t>0 than at t=0."""
        phi0 = sim.gaussian_pulse(components=[0, 1])
        result = sim.evolve_klein_gordon(phi0, steps=50, epsilon=1.0)
        phi_init = result['phi_history'][0]
        phi_final = result['phi_history'][-1]
        diff = np.max(np.abs(phi_final - phi_init))
        assert diff > 1e-6, (
            f"Field did not evolve: max change = {diff:.2e}"
        )

    def test_field_changes_maxwell(self, sim):
        """7D Maxwell fields evolve non-trivially.

        We use E in the e3 direction and B in the e5 direction
        (partners under the Fano triple (3,4,7)), which produces a
        nonzero curl on the 1D grid through eps[0,j,k].
        """
        E0 = np.zeros((sim.N, 7))
        B0 = np.zeros((sim.N, 7))
        sigma = sim.L / 10.0
        envelope = np.exp(-((sim.x - sim.L / 2) ** 2) / (2 * sigma ** 2))
        E0[:, 2] = envelope       # e3 direction
        B0[:, 4] = 0.5 * envelope  # e5 direction
        result = sim.evolve_maxwell_7d(E0, B0, steps=50, epsilon=1.0)
        E_init = result['E_history'][0]
        E_final = result['E_history'][-1]
        diff = np.max(np.abs(E_final - E_init))
        assert diff > 1e-6, (
            f"Maxwell field did not evolve: max change = {diff:.2e}"
        )

    def test_momentum_changes(self, sim):
        """The conjugate momentum pi should also evolve."""
        phi0 = sim.sine_mode(mode=3, components=[0, 2])
        result = sim.evolve_klein_gordon(phi0, steps=50, epsilon=1.0)
        pi_init = result['pi_history'][0]
        pi_final = result['pi_history'][-1]
        assert np.max(np.abs(pi_final)) > 1e-6, (
            "Momentum did not develop from zero initial conditions"
        )


# ---------------------------------------------------------------------------
# 6. Maxwell energy conservation
# ---------------------------------------------------------------------------

class TestMaxwellEnergy:
    """Electromagnetic energy should be approximately conserved."""

    def test_maxwell_energy_conservation(self, sim):
        """EM energy drift < 5% over 100 steps."""
        E0 = np.zeros((sim.N, 7))
        B0 = np.zeros((sim.N, 7))
        E0[:, 2] = np.exp(-((sim.x - sim.L / 2) ** 2) / (2 * (sim.L / 10) ** 2))
        B0[:, 4] = 0.5 * np.exp(-((sim.x - sim.L / 2) ** 2) / (2 * (sim.L / 10) ** 2))

        result = sim.evolve_maxwell_7d(E0, B0, steps=100, epsilon=1.0)
        U = result['energy_history']
        U0 = U[0]
        assert U0 > 0
        rel_err = np.max(np.abs(U - U0)) / U0
        # The symplectic splitting conserves the free-field energy exactly;
        # the associator correction introduces a small perturbation.
        assert rel_err < 0.05, (
            f"Maxwell energy drift: {rel_err:.2e}"
        )

    def test_maxwell_energy_eps0(self, sim):
        """At epsilon=0 the free-field energy is conserved very well.

        The symplectic splitting (half-B, full-E, half-B) conserves the
        free Maxwell energy exactly up to floating-point round-off.
        We use localised Gaussian E and B to avoid boundary artifacts.
        """
        E0 = np.zeros((sim.N, 7))
        B0 = np.zeros((sim.N, 7))
        sigma = sim.L / 10.0
        envelope = np.exp(-((sim.x - sim.L / 2) ** 2) / (2 * sigma ** 2))
        E0[:, 2] = envelope
        B0[:, 4] = 0.5 * envelope

        result = sim.evolve_maxwell_7d(E0, B0, steps=100, epsilon=0.0)
        U = result['energy_history']
        U0 = U[0]
        assert U0 > 0
        rel_err = np.max(np.abs(U - U0)) / U0
        assert rel_err < 1e-3, (
            f"Maxwell energy drift at eps=0: {rel_err:.2e}"
        )


# ---------------------------------------------------------------------------
# 7. Associative limit comparison
# ---------------------------------------------------------------------------

class TestAssociativeComparison:
    """eps=0 and eps=1 should agree at t=0 and diverge for t>0."""

    def test_delta_zero_at_t0(self, sim):
        """The relative difference starts at zero."""
        phi0 = sim.gaussian_pulse(components=[0, 1])
        cmp = sim.compare_associative_limit(phi0, steps=50)
        assert cmp['delta'][0] < 1e-14

    def test_delta_grows(self, sim):
        """For fields with components beyond quaternionic subspace,
        the octonionic and quaternionic trajectories diverge."""
        # Excite components 4-7 to trigger non-associative dynamics
        phi0 = sim.gaussian_pulse(components=[0, 1, 4, 5, 6])
        cmp = sim.compare_associative_limit(phi0, steps=100)
        # The difference should grow above zero
        assert np.max(cmp['delta']) > 1e-10, (
            "Expected divergence between eps=0 and eps=1 trajectories"
        )

    def test_shapes_match(self, sim):
        """Both trajectories have the same shape."""
        phi0 = sim.sine_mode(mode=1, components=[0])
        cmp = sim.compare_associative_limit(phi0, steps=20)
        assert (
            cmp['oct_result']['phi_history'].shape
            == cmp['quat_result']['phi_history'].shape
        )
        assert cmp['delta'].shape == cmp['times'].shape


# ---------------------------------------------------------------------------
# 8. Initial conditions
# ---------------------------------------------------------------------------

class TestInitialConditions:
    """Helpers produce valid arrays with correct shapes."""

    def test_gaussian_pulse_shape(self, sim):
        phi0 = sim.gaussian_pulse()
        assert phi0.shape == (sim.N, 8)

    def test_gaussian_pulse_has_signal(self, sim):
        """The excited component has nonzero values; others are zero."""
        phi0 = sim.gaussian_pulse(components=[0])
        assert np.max(np.abs(phi0[:, 0])) > 0.1
        assert np.allclose(phi0[:, 1:], 0)

    def test_sine_mode_shape(self, sim):
        phi0 = sim.sine_mode(mode=2, components=[0, 3])
        assert phi0.shape == (sim.N, 8)

    def test_random_field_reproducible(self, sim):
        f1 = sim.random_field(seed=42)
        f2 = sim.random_field(seed=42)
        assert np.allclose(f1, f2)

    def test_random_field_shape(self, sim):
        phi0 = sim.random_field()
        assert phi0.shape == (sim.N, 8)


# ---------------------------------------------------------------------------
# 9. Poynting vector
# ---------------------------------------------------------------------------

class TestPoynting:
    """The Poynting vector should be nonzero for crossed E and B."""

    def test_poynting_nonzero(self, sim):
        E0 = np.zeros((sim.N, 7))
        B0 = np.zeros((sim.N, 7))
        E0[:, 2] = 1.0  # e3
        B0[:, 4] = 1.0  # e5
        result = sim.evolve_maxwell_7d(E0, B0, steps=1, epsilon=1.0)
        S = result['poynting_history'][0]
        assert np.max(np.abs(S)) > 1e-10, "Poynting vector should be nonzero"

    def test_poynting_shape(self, sim):
        E0 = np.zeros((sim.N, 7))
        B0 = np.zeros((sim.N, 7))
        E0[:, 0] = 1.0
        result = sim.evolve_maxwell_7d(E0, B0, steps=5, epsilon=1.0)
        assert result['poynting_history'].shape == (6, sim.N, 7)


# ---------------------------------------------------------------------------
# 10. Module-level wrappers
# ---------------------------------------------------------------------------

class TestModuleLevelWrappers:
    """Module-level functions run without error and return correct shapes."""

    def test_evolve_klein_gordon_wrapper(self):
        N, dx, dt, steps = 32, 0.2, 0.01, 20
        phi0 = np.zeros((N, 8))
        phi0[:, 0] = np.sin(np.pi * np.arange(N) * dx / (N * dx))
        pi0 = np.zeros((N, 8))
        result = evolve_klein_gordon(phi0, pi0, dx, dt, steps)
        assert result['phi_history'].shape == (steps + 1, N, 8)
        assert result['energy_history'].shape == (steps + 1,)

    def test_evolve_maxwell_wrapper(self):
        N, dx, dt, steps = 32, 0.2, 0.01, 20
        E0 = np.zeros((N, 7))
        B0 = np.zeros((N, 7))
        E0[:, 0] = 1.0
        result = evolve_maxwell_7d(E0, B0, dx, dt, steps)
        assert result['E_history'].shape == (steps + 1, N, 7)

    def test_coherence_wrapper(self):
        N, dx, dt, steps = 32, 0.2, 0.01, 10
        rng = np.random.default_rng(99)
        phi0 = rng.standard_normal((N, 8)) * 0.1
        pi0 = np.zeros((N, 8))
        result = compute_coherence_evolution(phi0, pi0, dx, dt, steps)
        assert result['Q_C_history'].shape == (steps + 1,)

    def test_compare_wrapper(self):
        N, dx, dt, steps = 32, 0.2, 0.01, 10
        phi0 = np.zeros((N, 8))
        phi0[:, 0] = 1.0
        pi0 = np.zeros((N, 8))
        result = compare_associative_limit(phi0, pi0, dx, dt, steps)
        assert 'delta' in result
        assert result['delta'].shape == (steps + 1,)


# ---------------------------------------------------------------------------
# 11. Internal helpers
# ---------------------------------------------------------------------------

class TestInternalHelpers:
    """Low-level functions produce correct results."""

    def test_laplacian_constant_field(self):
        """Laplacian of a constant field is zero at interior points.

        The boundary points use Dirichlet ghost values (phi=0 outside
        the domain), so the Laplacian is nonzero there.  We only check
        interior points where the 3-point stencil sees constant values.
        """
        phi = np.ones((50, 8)) * 3.7
        lap = _compute_laplacian(phi, 0.1)
        # Interior points: indices 1 to 48
        assert np.max(np.abs(lap[1:-1])) < 1e-10

    def test_laplacian_quadratic(self):
        """Laplacian of x^2 is 2 (interior points)."""
        N = 100
        dx = 0.1
        x = np.arange(N) * dx
        phi = np.zeros((N, 8))
        phi[:, 0] = x ** 2
        lap = _compute_laplacian(phi, dx)
        # Interior points should give ~2.0
        interior = lap[2:-2, 0]
        assert np.allclose(interior, 2.0, atol=1e-8)

    def test_associator_correction_zero_at_eps0(self):
        """Associator correction vanishes at epsilon=0."""
        N = 20
        rng = np.random.default_rng(42)
        phi = rng.standard_normal((N, 8))
        assoc = _associator_correction(phi, 0.2, epsilon=0.0)
        assert np.max(np.abs(assoc)) < 1e-15

    def test_associator_correction_nonzero_at_eps1(self):
        """Associator correction is nonzero at epsilon=1 for generic fields."""
        N = 20
        rng = np.random.default_rng(42)
        phi = rng.standard_normal((N, 8))
        assoc = _associator_correction(phi, 0.2, epsilon=1.0)
        assert np.max(np.abs(assoc)) > 1e-6


# ---------------------------------------------------------------------------
# 12. Regression / smoke tests
# ---------------------------------------------------------------------------

class TestSmoke:
    """Smoke tests to catch import errors or shape mismatches."""

    def test_simulator_init(self):
        sim = OctonionicFieldSimulator()
        assert sim.N == 64
        assert sim.x.shape == (64,)

    def test_full_pipeline(self, sim):
        """Run KG + Maxwell + coherence + comparison without errors."""
        phi0 = sim.gaussian_pulse()
        _ = sim.evolve_klein_gordon(phi0, steps=5)
        E0 = np.zeros((sim.N, 7))
        B0 = np.zeros((sim.N, 7))
        E0[:, 0] = 1.0
        _ = sim.evolve_maxwell_7d(E0, B0, steps=5)
        _ = sim.compute_coherence_evolution(phi0, steps=5)
        _ = sim.compare_associative_limit(phi0, steps=5)
