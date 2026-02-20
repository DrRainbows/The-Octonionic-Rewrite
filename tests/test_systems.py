"""
Tests for octonion_algebra.systems — the octonionic dynamical system modeler.

Covers:
  - epsilon=0 recovery of associative (standard) dynamics
  - monotonic growth of associator magnitude with epsilon
  - norm conservation under Hamiltonian-like dynamics
  - symmetry preservation in symmetric networks
  - determinism of the coalition model
  - smoothness of deformation sweeps
"""

import numpy as np
import pytest

from octonion_algebra.systems import (
    OctonionicDynamicalSystem,
    NetworkDynamics,
    CoalitionModel,
    DeformationSweep,
    _states_to_array,
    _array_to_deformed,
)
from octonion_algebra.core import Octonion
from octonion_algebra.deformation import DeformedOctonion


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def quaternionic_states_8():
    """8 unit-norm quaternionic states (only components 0-3 nonzero).

    These live in the associative subalgebra, so all associators vanish
    at any epsilon whose deformed multiplication reduces to the quaternionic
    product on the (1, e1, e2, e3) subalgebra — in particular at epsilon=0.
    """
    rng = np.random.default_rng(123)
    arr = np.zeros((8, 8))
    arr[:, :4] = rng.standard_normal((8, 4))
    norms = np.linalg.norm(arr, axis=1, keepdims=True)
    arr = arr / np.maximum(norms, 1e-15)
    return arr


@pytest.fixture
def full_octonionic_states_8():
    """8 unit-norm full octonionic states (all 8 components nonzero)."""
    rng = np.random.default_rng(456)
    arr = rng.standard_normal((8, 8))
    norms = np.linalg.norm(arr, axis=1, keepdims=True)
    arr = arr / np.maximum(norms, 1e-15)
    return arr


@pytest.fixture
def symmetric_adjacency_4():
    """Symmetric 4x4 adjacency matrix for network tests."""
    A = np.array([
        [0.0, 1.0, 0.0, 1.0],
        [1.0, 0.0, 1.0, 0.0],
        [0.0, 1.0, 0.0, 1.0],
        [1.0, 0.0, 1.0, 0.0],
    ])
    return A


# ---------------------------------------------------------------------------
# test_epsilon_zero_recovery
# ---------------------------------------------------------------------------

class TestEpsilonZeroRecovery:
    """At epsilon=0 the deformed algebra is quaternionic (associative).

    All associators should vanish and the system should behave like a
    standard (associative) dynamical system.
    """

    def test_associator_vanishes_quaternionic(self, quaternionic_states_8):
        """Quaternionic states at epsilon=0: total associator ~ 0."""
        sys = OctonionicDynamicalSystem(
            8, initial_states=quaternionic_states_8, epsilon=0.0, seed=99
        )
        assoc = sys.measure_associator()
        assert assoc < 1e-10, (
            f"Expected vanishing associator at eps=0 with quaternionic states, "
            f"got {assoc}"
        )

    def test_context_dependence_zero(self, quaternionic_states_8):
        """Context dependence = 0 at epsilon=0 for quaternionic states."""
        sys = OctonionicDynamicalSystem(
            8, initial_states=quaternionic_states_8, epsilon=0.0, seed=99
        )
        cd = sys.measure_context_dependence()
        assert cd < 1e-10, f"Expected zero context dependence, got {cd}"

    def test_network_zero_information_flow(self, quaternionic_states_8):
        """Network at epsilon=0 with quaternionic states: no associator flow."""
        net = NetworkDynamics(
            8, initial_states=quaternionic_states_8, epsilon=0.0,
            coupling=0.5, seed=99
        )
        flow = net.compute_information_flow()
        assert flow < 1e-10, f"Expected zero information flow, got {flow}"

    def test_coalition_zero_agenda_dependence(self):
        """Coalition model at epsilon=0 with quaternionic agents: ADI ~ 0."""
        rng = np.random.default_rng(77)
        arr = np.zeros((5, 8))
        arr[:, :4] = rng.standard_normal((5, 4))
        norms = np.linalg.norm(arr, axis=1, keepdims=True)
        arr = arr / np.maximum(norms, 1e-15)

        model = CoalitionModel(5, agent_states=arr, epsilon=0.0, seed=77)
        adi = model.agenda_dependence_index()
        assert adi < 1e-10, f"Expected ADI ~ 0 at eps=0, got {adi}"


# ---------------------------------------------------------------------------
# test_epsilon_monotonicity
# ---------------------------------------------------------------------------

class TestEpsilonMonotonicity:
    """Associator magnitude should generally increase with epsilon.

    As epsilon grows from 0 to 1, the algebra becomes more non-associative,
    so the total associator norm should increase (or at least not decrease).
    """

    def test_associator_nondecreasing(self, full_octonionic_states_8):
        """Total associator grows monotonically with epsilon for fixed states."""
        epsilons = np.linspace(0, 1, 6)
        assocs = []
        for eps in epsilons:
            sys = OctonionicDynamicalSystem(
                8, initial_states=full_octonionic_states_8.copy(),
                epsilon=eps, seed=42
            )
            assocs.append(sys.measure_associator())

        assocs = np.array(assocs)
        # Allow small numerical tolerance for monotonicity
        for i in range(1, len(assocs)):
            assert assocs[i] >= assocs[i - 1] - 1e-8, (
                f"Associator decreased from eps={epsilons[i-1]:.2f} to "
                f"eps={epsilons[i]:.2f}: {assocs[i-1]:.6f} -> {assocs[i]:.6f}"
            )

    def test_context_dependence_increases(self, full_octonionic_states_8):
        """Context dependence ratio increases with epsilon."""
        cd_0 = OctonionicDynamicalSystem(
            8, initial_states=full_octonionic_states_8.copy(),
            epsilon=0.0, seed=42
        ).measure_context_dependence()

        cd_1 = OctonionicDynamicalSystem(
            8, initial_states=full_octonionic_states_8.copy(),
            epsilon=1.0, seed=42
        ).measure_context_dependence()

        assert cd_1 > cd_0, (
            f"Context dependence should increase: eps=0 -> {cd_0}, eps=1 -> {cd_1}"
        )


# ---------------------------------------------------------------------------
# test_conservation
# ---------------------------------------------------------------------------

class TestConservation:
    """Total norm (energy analog) should be approximately preserved.

    For small time steps and short integration, the RK4 integrator should
    preserve the total norm to a good approximation.
    """

    def test_norm_preservation_small_dt(self, full_octonionic_states_8):
        """Total norm changes by less than 10% over a short evolution."""
        sys = OctonionicDynamicalSystem(
            8, initial_states=full_octonionic_states_8.copy(),
            epsilon=0.5, seed=42
        )
        result = sys.evolve(dt=0.001, steps=20)
        norm_init = result["total_norm"][0]
        norm_final = result["total_norm"][-1]
        relative_change = abs(norm_final - norm_init) / norm_init
        assert relative_change < 0.10, (
            f"Norm changed by {relative_change*100:.2f}% — too much for dt=0.001"
        )

    def test_trajectory_shape(self, full_octonionic_states_8):
        """Trajectory output has correct shapes."""
        sys = OctonionicDynamicalSystem(
            8, initial_states=full_octonionic_states_8.copy(),
            epsilon=0.5, seed=42
        )
        result = sys.evolve(dt=0.01, steps=10)
        assert result["trajectory"].shape == (11, 8, 8)
        assert result["times"].shape == (11,)
        assert result["total_norm"].shape == (11,)
        assert result["associator_energy"].shape == (11,)

    def test_times_array(self, full_octonionic_states_8):
        """Time array is correct."""
        sys = OctonionicDynamicalSystem(
            8, initial_states=full_octonionic_states_8.copy(),
            epsilon=0.5, seed=42
        )
        result = sys.evolve(dt=0.01, steps=5)
        expected_times = np.array([0.0, 0.01, 0.02, 0.03, 0.04, 0.05])
        np.testing.assert_allclose(result["times"], expected_times, atol=1e-12)


# ---------------------------------------------------------------------------
# test_network_symmetry
# ---------------------------------------------------------------------------

class TestNetworkSymmetry:
    """A symmetric network with identical initial states should evolve symmetrically."""

    def test_symmetric_evolution(self):
        """Pair of symmetrically placed nodes evolve identically."""
        # Build a 4-node ring: 0-1-2-3-0 with equal weights
        A = np.zeros((4, 4))
        A[0, 1] = A[1, 0] = 1.0
        A[1, 2] = A[2, 1] = 1.0
        A[2, 3] = A[3, 2] = 1.0
        A[3, 0] = A[0, 3] = 1.0

        # Identical initial states for all nodes
        state = np.array([1.0, 0.5, -0.3, 0.2, 0.1, -0.4, 0.3, -0.1])
        state = state / np.linalg.norm(state)
        init = np.tile(state, (4, 1))

        net = NetworkDynamics(4, adjacency=A, coupling=0.1,
                              initial_states=init, epsilon=0.5, seed=42)
        result = net.evolve(dt=0.005, steps=10)

        # After evolution, all nodes should have the same state (by symmetry)
        final = result["trajectory"][-1]
        for i in range(1, 4):
            np.testing.assert_allclose(
                final[0], final[i], atol=1e-8,
                err_msg=f"Node 0 and node {i} diverged in symmetric network"
            )

    def test_adjacency_matrix_stored(self, symmetric_adjacency_4):
        """Custom adjacency matrix is stored correctly."""
        net = NetworkDynamics(4, adjacency=symmetric_adjacency_4,
                              epsilon=0.5, seed=42)
        np.testing.assert_array_equal(net.adjacency, symmetric_adjacency_4)


# ---------------------------------------------------------------------------
# test_coalition_deterministic
# ---------------------------------------------------------------------------

class TestCoalitionDeterministic:
    """Same inputs always produce the same outputs (no hidden randomness)."""

    def test_same_seed_same_result(self):
        """Two CoalitionModels with same seed give identical ADI."""
        m1 = CoalitionModel(5, epsilon=0.7, seed=12345)
        m2 = CoalitionModel(5, epsilon=0.7, seed=12345)

        adi1 = m1.agenda_dependence_index()
        adi2 = m2.agenda_dependence_index()
        assert adi1 == pytest.approx(adi2, abs=1e-14), (
            f"Determinism violated: {adi1} != {adi2}"
        )

    def test_coalition_value_symmetric(self):
        """V(i,j,k) == V(i,j,k) on repeated call."""
        model = CoalitionModel(4, epsilon=0.8, seed=999)
        v1 = model.coalition_value(0, 1, 2)
        v2 = model.coalition_value(0, 1, 2)
        assert v1 == pytest.approx(v2, abs=1e-14)

    def test_associator_nonzero_at_eps1(self):
        """At epsilon=1 with generic states, the associator is nonzero."""
        model = CoalitionModel(4, epsilon=1.0, seed=777)
        assoc = model.coalition_associator(0, 1, 2)
        assert assoc.norm() > 1e-6, (
            "Expected nonzero associator at eps=1 with generic states"
        )

    def test_stable_coalitions_returns_list(self):
        """find_stable_coalitions returns a list of tuples."""
        model = CoalitionModel(5, epsilon=0.5, seed=42)
        stable = model.find_stable_coalitions()
        assert isinstance(stable, list)
        for item in stable:
            assert isinstance(item, tuple)
            assert len(item) == 3  # (combo, value, relative_dep)

    def test_agent_array_shape(self):
        """agent_array returns correct shape."""
        model = CoalitionModel(6, epsilon=0.5, seed=42)
        arr = model.agent_array()
        assert arr.shape == (6, 8)


# ---------------------------------------------------------------------------
# test_deformation_sweep_smooth
# ---------------------------------------------------------------------------

class TestDeformationSweepSmooth:
    """Observables should be smooth (Lipschitz-continuous) functions of epsilon.

    Large jumps between adjacent epsilon values indicate bugs, not physics.
    """

    def test_network_sweep_smooth(self):
        """Context dependence changes smoothly across epsilon."""
        sweep = DeformationSweep(np.linspace(0, 1, 6))
        results = sweep.sweep_network(
            N=4, coupling=0.1, dt=0.005, steps=10, seed=42
        )
        cd = results["context_dependence"]
        # Check consecutive differences are bounded
        diffs = np.abs(np.diff(cd))
        # Maximum jump should be bounded (empirical: < 50 for these params)
        assert np.all(diffs < 50), (
            f"Context dependence has discontinuous jumps: max_diff = {diffs.max()}"
        )

    def test_coalition_sweep_smooth(self):
        """Agenda dependence index changes smoothly across epsilon."""
        sweep = DeformationSweep(np.linspace(0, 1, 6))
        results = sweep.sweep_coalition(N=4, seed=42)
        adi = results["agenda_dependence"]
        diffs = np.abs(np.diff(adi))
        # ADI is normalised to [0,1], so max jump should be bounded
        assert np.all(diffs < 1.0), (
            f"ADI has discontinuous jumps: max_diff = {diffs.max()}"
        )

    def test_sweep_returns_all_keys(self):
        """Network sweep returns all expected keys."""
        sweep = DeformationSweep(np.linspace(0, 1, 3))
        results = sweep.sweep_network(N=3, coupling=0.1, dt=0.01, steps=5, seed=42)
        for key in ["epsilon", "context_dependence", "information_flow",
                     "associator_total", "total_norm", "phase_transition_epsilon"]:
            assert key in results, f"Missing key: {key}"

    def test_coalition_sweep_returns_all_keys(self):
        """Coalition sweep returns all expected keys."""
        sweep = DeformationSweep(np.linspace(0, 1, 3))
        results = sweep.sweep_coalition(N=3, seed=42)
        for key in ["epsilon", "agenda_dependence", "n_stable",
                     "mean_value", "phase_transition_epsilon"]:
            assert key in results, f"Missing key: {key}"

    def test_epsilon_values_stored(self):
        """Epsilon values match what was passed in."""
        eps = np.array([0.0, 0.25, 0.5, 0.75, 1.0])
        sweep = DeformationSweep(eps)
        results = sweep.sweep_network(N=3, coupling=0.1, dt=0.01, steps=5, seed=42)
        np.testing.assert_allclose(results["epsilon"], eps)


# ---------------------------------------------------------------------------
# Additional integration tests
# ---------------------------------------------------------------------------

class TestIntegration:
    """End-to-end integration tests."""

    def test_evolve_changes_state(self, full_octonionic_states_8):
        """Evolution should actually change the state (not a no-op)."""
        sys = OctonionicDynamicalSystem(
            8, initial_states=full_octonionic_states_8.copy(),
            epsilon=0.5, seed=42
        )
        before = sys.state_array().copy()
        sys.evolve(dt=0.01, steps=5)
        after = sys.state_array()
        assert not np.allclose(before, after, atol=1e-10), (
            "Evolution did not change the state — dynamics may be trivial"
        )

    def test_network_evolve(self):
        """Network evolution runs without error and changes state."""
        net = NetworkDynamics(4, coupling=0.2, epsilon=0.8, seed=42)
        before = net.state_array().copy()
        net.evolve(dt=0.005, steps=5)
        after = net.state_array()
        assert not np.allclose(before, after, atol=1e-10)

    def test_state_array_roundtrip(self):
        """state_array -> new system preserves values."""
        sys = OctonionicDynamicalSystem(4, epsilon=0.5, seed=42)
        arr = sys.state_array()
        sys2 = OctonionicDynamicalSystem(4, initial_states=arr, epsilon=0.5)
        arr2 = sys2.state_array()
        np.testing.assert_allclose(arr, arr2, atol=1e-14)

    def test_epsilon_override_in_evolve(self, full_octonionic_states_8):
        """Passing epsilon to evolve changes the deformation parameter."""
        sys = OctonionicDynamicalSystem(
            8, initial_states=full_octonionic_states_8.copy(),
            epsilon=0.0, seed=42
        )
        assert sys.epsilon == 0.0
        sys.evolve(dt=0.01, steps=3, epsilon=0.8)
        assert sys.epsilon == 0.8

    def test_detect_phase_transition(self):
        """Phase transition detection returns float or None."""
        sweep = DeformationSweep(np.linspace(0, 1, 6))
        sweep.sweep_network(N=4, coupling=0.1, dt=0.005, steps=10, seed=42)
        result = sweep.detect_phase_transition("context_dependence")
        assert result is None or isinstance(result, float)

    def test_helpers_array_roundtrip(self):
        """_states_to_array and _array_to_deformed are inverses."""
        states = [DeformedOctonion.random(epsilon=0.5, seed=i) for i in range(3)]
        arr = _states_to_array(states)
        assert arr.shape == (3, 8)
        recovered = _array_to_deformed(arr, 0.5)
        for s, r in zip(states, recovered):
            np.testing.assert_allclose(s.coeffs, r.coeffs, atol=1e-14)
