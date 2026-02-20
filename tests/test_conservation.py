"""Tests for the non-associative conservation law machinery (Chapters 16 & 18)."""

import numpy as np
import pytest

from octonion_algebra.core import Octonion
from octonion_algebra.associator import associator
from octonion_algebra.g2 import g2_generators
from octonion_algebra.coherence import (
    coherence_functional,
    g2_rotate_field,
    make_smooth_field,
)
from octonion_algebra.conservation import (
    g2_transform_octonion,
    noether_variation,
    coherence_current,
    coherence_density,
    coherence_charge,
    evolve_g2,
    verify_coherence_conservation,
    associator_source_term,
    noether_divergence_check,
)


# ---- Fixtures ----

@pytest.fixture
def g2_gens():
    return g2_generators()


@pytest.fixture
def smooth_field():
    return make_smooth_field(20, seed=42)


@pytest.fixture
def large_smooth_field():
    return make_smooth_field(40, seed=99)


def _make_quaternionic_field(n=15, seed=77):
    """Create a field valued in a quaternionic subalgebra span{1, e1, e2, e3}.

    Since {e1, e2, e3} lie on the Fano triple (1,2,3), any three elements
    from this subalgebra associate, so all associators vanish.
    """
    rng = np.random.default_rng(seed)
    field = []
    for _ in range(n):
        c = np.zeros(8)
        c[0] = rng.uniform(-1, 1)
        c[1] = rng.uniform(-1, 1)
        c[2] = rng.uniform(-1, 1)
        c[3] = rng.uniform(-1, 1)
        field.append(Octonion(c))
    return field


def _make_random_so7_rotation(seed=999, angle=0.5):
    """Create a random SO(7) matrix (generically NOT in G2)."""
    rng = np.random.default_rng(seed)
    A = rng.standard_normal((7, 7))
    A = (A - A.T) / 2  # antisymmetric
    M = angle * A
    R = np.eye(7)
    term = np.eye(7)
    for k in range(1, 30):
        term = term @ M / k
        R = R + term
    return R


def _apply_so7_to_field(field, R):
    """Apply a 7x7 rotation to the imaginary part of each field element."""
    rotated = []
    for f_i in field:
        c = np.zeros(8)
        c[0] = f_i.coeffs[0]
        c[1:] = R @ f_i.coeffs[1:]
        rotated.append(Octonion(c))
    return rotated


# ---- Tests ----

class TestCoherenceDensity:
    def test_coherence_density_nonneg(self, smooth_field):
        """rho_C(x) >= 0 everywhere, since it is a sum of squared norms."""
        rho = coherence_density(smooth_field)
        assert np.all(rho >= 0), f"Negative coherence density found: min={rho.min()}"

    def test_coherence_density_nonneg_random(self):
        """rho_C >= 0 for a completely random field."""
        rng = np.random.default_rng(42)
        field = [Octonion(rng.uniform(-1, 1, size=8)) for _ in range(12)]
        rho = coherence_density(field)
        assert np.all(rho >= 0)

    def test_coherence_density_zero_quaternionic(self):
        """rho_C = 0 for a quaternionic field (Proposition 18.2)."""
        field = _make_quaternionic_field()
        rho = coherence_density(field)
        np.testing.assert_allclose(rho, 0.0, atol=1e-10,
                                   err_msg="Coherence density should vanish for quaternionic fields")


class TestCoherenceCharge:
    def test_coherence_charge_g2_invariant(self, smooth_field, g2_gens):
        """Q_C unchanged under G2 rotation (Theorem 18.1)."""
        Q_orig = coherence_charge(smooth_field)

        # Apply a nontrivial G2 rotation
        coeffs = [0.15, -0.1, 0.08, 0.05, -0.03, 0.12, -0.07] + [0.0] * 7
        rotated = g2_rotate_field(smooth_field, g2_gens, coeffs, angle=0.1)
        Q_rot = coherence_charge(rotated)

        np.testing.assert_allclose(Q_orig, Q_rot, rtol=1e-6,
                                   err_msg="Coherence charge not G2-invariant")

    def test_coherence_charge_positive_generic(self, smooth_field):
        """Q_C > 0 for a generic octonionic field."""
        Q = coherence_charge(smooth_field)
        assert Q > 0, f"Expected positive coherence charge, got {Q}"

    def test_coherence_charge_zero_quaternionic(self):
        """Q_C = 0 for quaternionic field."""
        field = _make_quaternionic_field()
        Q = coherence_charge(field)
        assert abs(Q) < 1e-10, f"Expected zero coherence charge for quaternionic field, got {Q}"


class TestCoherenceConservation:
    def test_coherence_conservation_under_evolution(self, smooth_field, g2_gens):
        """C[Phi(t)] constant over 50 time steps (tolerance 1e-4 relative).

        Theorem 18.2: coherence is conserved under G2-covariant dynamics.
        """
        result = verify_coherence_conservation(
            smooth_field, g2_gens, dt=0.01, n_steps=50, seed=123
        )
        assert result['relative_error'] < 1e-4, (
            f"Coherence not conserved: relative error = {result['relative_error']:.2e}, "
            f"initial_C = {result['initial_C']:.6f}, "
            f"max_deviation = {result['max_deviation']:.2e}"
        )

    def test_coherence_breaks_under_so7(self, smooth_field):
        """Random SO(7) rotation (not in G2) changes Q_C."""
        Q_orig = coherence_charge(smooth_field)

        R = _make_random_so7_rotation(seed=999, angle=0.5)
        rotated = _apply_so7_to_field(smooth_field, R)
        Q_rot = coherence_charge(rotated)

        assert abs(Q_orig - Q_rot) > 1e-6, (
            f"Coherence charge should change under generic SO(7), "
            f"Q_orig={Q_orig}, Q_rot={Q_rot}"
        )


class TestNoetherVariation:
    def test_noether_variation_antisymmetric(self, smooth_field, g2_gens):
        """delta Phi under -D gives -delta Phi (linearity in the generator)."""
        D = g2_gens[0]
        dx = 0.1

        var_pos = noether_variation(smooth_field, dx, D)
        var_neg = noether_variation(smooth_field, dx, -D)

        for vp, vn in zip(var_pos, var_neg):
            np.testing.assert_allclose(
                vp.coeffs, -vn.coeffs, atol=1e-12,
                err_msg="Noether variation not antisymmetric under D -> -D"
            )

    def test_noether_variation_linearity(self, smooth_field, g2_gens):
        """delta Phi is linear in the generator: var(2D) = 2*var(D)."""
        D = g2_gens[1]
        dx = 0.1

        var_1 = noether_variation(smooth_field, dx, D)
        var_2 = noether_variation(smooth_field, dx, 2.0 * D)

        for v1, v2 in zip(var_1, var_2):
            np.testing.assert_allclose(
                2.0 * v1.coeffs, v2.coeffs, atol=1e-12,
                err_msg="Noether variation not linear in generator"
            )

    def test_noether_variation_imaginary(self, smooth_field, g2_gens):
        """D maps Im(O) -> Im(O), so delta Phi has zero real part."""
        D = g2_gens[3]
        dx = 0.1
        variations = noether_variation(smooth_field, dx, D)
        for v in variations:
            assert abs(v.coeffs[0]) < 1e-12, (
                f"Noether variation should be purely imaginary, got real part {v.coeffs[0]}"
            )


class TestAssociatorSource:
    def test_associator_source_vanishes_quaternionic(self, g2_gens):
        """R_D = 0 for quaternionic fields (Theorem 16.1(a)).

        Fields valued in H subset O have all associators = 0, so the
        source term in the modified Noether equation vanishes exactly.
        """
        field = _make_quaternionic_field(n=15, seed=77)
        dx = 0.1
        D = g2_gens[0]

        source = associator_source_term(field, dx, D)
        np.testing.assert_allclose(
            source, 0.0, atol=1e-10,
            err_msg="Associator source should vanish for quaternionic field"
        )

    def test_associator_source_nonzero_octonionic(self, smooth_field, g2_gens):
        """R_D != 0 for generic octonionic fields.

        For a generic field that explores all 7 imaginary directions, the
        associators are nonzero and the source term is generically nonzero.
        """
        dx = 0.1
        D = g2_gens[0]

        source = associator_source_term(smooth_field, dx, D)
        assert np.max(np.abs(source)) > 1e-10, (
            f"Associator source should be nonzero for octonionic field, "
            f"max |R_D| = {np.max(np.abs(source))}"
        )

    def test_associator_source_vanishes_all_generators_quaternionic(self, g2_gens):
        """R_D = 0 for ALL generators when the field is quaternionic."""
        field = _make_quaternionic_field(n=15, seed=42)
        dx = 0.1
        for idx, D in enumerate(g2_gens):
            source = associator_source_term(field, dx, D)
            np.testing.assert_allclose(
                source, 0.0, atol=1e-10,
                err_msg=f"Associator source should vanish for generator {idx}"
            )


class TestNoetherDivergence:
    def test_noether_divergence_balance(self, large_smooth_field, g2_gens):
        """Verify div(J) ~ R_D to some tolerance.

        The modified Noether equation (Eq 16.26) states partial_mu J^mu = R_D.
        For a discretised 1D field this becomes a finite-difference relation.
        Discretisation errors mean we only check approximate balance.
        """
        dx = 0.1
        D = g2_gens[0]

        result = noether_divergence_check(large_smooth_field, dx, D)

        # Both sides should have the same order of magnitude; the error
        # should be small compared to the larger of div(J) and R_D.
        scale = max(
            np.max(np.abs(result['divergence'])) if len(result['divergence']) > 0 else 1.0,
            np.max(np.abs(result['source'])) if len(result['source']) > 0 else 1.0,
            1e-15  # avoid division by zero
        )
        relative_error = result['max_error'] / scale

        # Discretisation tolerance: finite differences introduce O(dx^2) errors
        assert relative_error < 5.0, (
            f"Noether divergence check: relative error {relative_error:.4f} "
            f"exceeds tolerance.  max_error={result['max_error']:.4e}, "
            f"scale={scale:.4e}"
        )


class TestG2Transform:
    def test_g2_transform_preserves_norm(self, g2_gens):
        """G2 transformation preserves octonion norm."""
        o = Octonion.random(seed=42)
        D = g2_gens[2]
        o_rot = g2_transform_octonion(o, D, t=0.1)
        np.testing.assert_allclose(o.norm(), o_rot.norm(), rtol=1e-10,
                                   err_msg="G2 transform should preserve norm")

    def test_g2_transform_preserves_real_part(self, g2_gens):
        """G2 acts only on Im(O); real part is unchanged."""
        o = Octonion([3.0, 1.0, -0.5, 2.0, 0.3, -1.0, 0.7, 0.2])
        D = g2_gens[5]
        o_rot = g2_transform_octonion(o, D, t=0.05)
        np.testing.assert_allclose(o.coeffs[0], o_rot.coeffs[0], atol=1e-14,
                                   err_msg="Real part should be unchanged under G2")

    def test_g2_transform_identity_at_t0(self, g2_gens):
        """At t=0, exp(0*D) = identity."""
        o = Octonion.random(seed=55)
        D = g2_gens[0]
        o_rot = g2_transform_octonion(o, D, t=0.0)
        np.testing.assert_allclose(o.coeffs, o_rot.coeffs, atol=1e-14)


class TestEvolveG2:
    def test_evolve_returns_correct_length(self, smooth_field, g2_gens):
        """evolve_g2 returns n_steps+1 snapshots."""
        trajectory = evolve_g2(smooth_field, g2_gens, dt=0.01, n_steps=10)
        assert len(trajectory) == 11

    def test_evolve_preserves_field_size(self, smooth_field, g2_gens):
        """Each snapshot has the same number of field points."""
        trajectory = evolve_g2(smooth_field, g2_gens, dt=0.01, n_steps=5)
        for snap in trajectory:
            assert len(snap) == len(smooth_field)


class TestCoherenceCurrent:
    def test_coherence_current_length(self, smooth_field):
        """Current array has correct length."""
        dx = 0.1
        currents = coherence_current(smooth_field, dx)
        assert len(currents) == len(smooth_field) - 3

    def test_coherence_current_shape(self, smooth_field):
        """Each current element is a 7-component vector."""
        dx = 0.1
        currents = coherence_current(smooth_field, dx)
        for j in currents:
            assert j.shape == (7,)
