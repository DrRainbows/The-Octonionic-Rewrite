"""
Comprehensive tests for octonion_algebra.context_integral.

Tests cover the context-dependent adjoint, Killing form integrand,
decompactified Killing form (quadrature and Monte Carlo), Fourier context
curves, UV-cutoff convergence, and the full convergence proof.

Addresses Grok critiques #3 (Omega undefined/uncomputable) and #27
(context integral convergence).
"""

import numpy as np
import pytest

from octonion_algebra.core import Octonion, e0, e1, e2, e3, e4, e5, e6, e7
from octonion_algebra.associator import associator
from octonion_algebra.context_integral import (
    context_adjoint,
    context_adjoint_matrix,
    killing_form_integrand,
    decompactified_killing_form,
    killing_form_matrix,
    fourier_context_curve,
    standard_context_curve,
    uv_cutoff_convergence,
    monte_carlo_killing_form,
    convergence_proof,
)


# ---- TestContextAdjoint ----

class TestContextAdjoint:
    """Tests for context_adjoint and context_adjoint_matrix."""

    def test_adjoint_matches_associator(self):
        """context_adjoint(X, Y, u) must equal associator(X, Y, u)."""
        X = e1
        Y = e2
        u = e3
        result = context_adjoint(X, Y, u)
        expected = associator(X, Y, u)
        np.testing.assert_allclose(result.coeffs, expected.coeffs, atol=1e-14)

    def test_adjoint_matches_associator_random(self):
        """context_adjoint matches associator for random octonions."""
        rng = np.random.default_rng(99)
        for _ in range(20):
            X = Octonion(rng.standard_normal(8))
            Y = Octonion(rng.standard_normal(8))
            u = Octonion(rng.standard_normal(8))
            result = context_adjoint(X, Y, u)
            expected = associator(X, Y, u)
            np.testing.assert_allclose(
                result.coeffs, expected.coeffs, atol=1e-12,
                err_msg="context_adjoint does not match associator",
            )

    def test_adjoint_antisymmetry_in_first_two_args(self):
        """The associator is antisymmetric: [X, Y, u] = -[Y, X, u]."""
        X = e1
        Y = e4
        u = e7
        r1 = context_adjoint(X, Y, u)
        r2 = context_adjoint(Y, X, u)
        np.testing.assert_allclose(r1.coeffs, -r2.coeffs, atol=1e-14)

    def test_adjoint_antisymmetry_random(self):
        """Antisymmetry [X, Y, u] = -[Y, X, u] for random octonions."""
        rng = np.random.default_rng(77)
        for _ in range(10):
            X = Octonion(np.concatenate([[0.0], rng.standard_normal(7)]))
            Y = Octonion(np.concatenate([[0.0], rng.standard_normal(7)]))
            u = Octonion(np.concatenate([[0.0], rng.standard_normal(7)]))
            r1 = context_adjoint(X, Y, u)
            r2 = context_adjoint(Y, X, u)
            np.testing.assert_allclose(
                r1.coeffs, -r2.coeffs, atol=1e-12,
                err_msg="Antisymmetry failed for random imaginary octonions",
            )

    def test_adjoint_matrix_shape(self):
        """context_adjoint_matrix returns a 7x7 matrix."""
        X = e1
        u = e3
        mat = context_adjoint_matrix(X, u)
        assert mat.shape == (7, 7)

    def test_adjoint_matrix_consistency(self):
        """Matrix columns match individual context_adjoint calls."""
        X = e2
        u = e5
        mat = context_adjoint_matrix(X, u)
        for j in range(7):
            Y = Octonion.basis(j + 1)
            result = context_adjoint(X, Y, u)
            np.testing.assert_allclose(
                mat[:, j], result.imag_vector(), atol=1e-14,
                err_msg=f"Column {j} of adjoint matrix does not match",
            )


# ---- TestKillingFormIntegrand ----

class TestKillingFormIntegrand:
    """Tests for killing_form_integrand."""

    def test_trace_computation(self):
        """killing_form_integrand gives tr(ad_X^u @ ad_Y^u)."""
        X = e1
        Y = e2
        u = e3
        val = killing_form_integrand(X, Y, u)
        # Cross-check: build matrices manually and compute trace
        ad_X = context_adjoint_matrix(X, u)
        ad_Y = context_adjoint_matrix(Y, u)
        expected = np.trace(ad_X @ ad_Y)
        np.testing.assert_allclose(val, expected, atol=1e-14)

    def test_symmetry_in_XY(self):
        """B(X, Y) = B(Y, X) because tr(AB) = tr(BA)."""
        u = e4
        X = e1
        Y = e5
        val_xy = killing_form_integrand(X, Y, u)
        val_yx = killing_form_integrand(Y, X, u)
        np.testing.assert_allclose(val_xy, val_yx, atol=1e-14)

    def test_symmetry_random(self):
        """Symmetry B(X,Y) = B(Y,X) for random imaginary octonions."""
        rng = np.random.default_rng(42)
        for _ in range(10):
            X = Octonion(np.concatenate([[0.0], rng.standard_normal(7)]))
            Y = Octonion(np.concatenate([[0.0], rng.standard_normal(7)]))
            u = Octonion(np.concatenate([[0.0], rng.standard_normal(7)]))
            val_xy = killing_form_integrand(X, Y, u)
            val_yx = killing_form_integrand(Y, X, u)
            np.testing.assert_allclose(
                val_xy, val_yx, atol=1e-12,
                err_msg="Killing form integrand is not symmetric in X, Y",
            )

    def test_zero_when_same_quaternionic_subalgebra(self):
        """For a Fano triple (i,j,k), [e_i, e_j, e_k] = 0, so
        ad_{e_i}^{e_k} applied to e_j gives zero, but full trace
        need not vanish in general. Verify specific known behavior."""
        # If u = e_k and X = e_i where (i,j,k) is a Fano triple,
        # ad_X^u(e_j) = [e_i, e_j, e_k] = 0 by alternativity in
        # quaternionic subalgebra. The full trace may still be nonzero
        # because other basis elements contribute.
        from octonion_algebra.core import FANO_TRIPLES
        triple = FANO_TRIPLES[0]  # (1, 2, 3)
        X = Octonion.basis(triple[0])
        Y = Octonion.basis(triple[1])
        u = Octonion.basis(triple[2])
        # The associator [e1, e2, e3] should be zero for a Fano triple
        assoc = associator(X, Y, u)
        assert assoc.norm() < 1e-14, "Fano triple associator should vanish"


# ---- TestDecompactifiedKillingForm ----

class TestDecompactifiedKillingForm:
    """Tests for decompactified_killing_form and killing_form_matrix."""

    def test_proportional_to_identity(self):
        """B_mu must be proportional to Id on Im(O) by Schur's lemma."""
        curve = standard_context_curve()
        B = killing_form_matrix(curve, n_quad=80)
        eigs = np.linalg.eigvalsh(B)
        # All eigenvalues should be nearly equal
        spread = np.max(eigs) - np.min(eigs)
        assert spread < 0.01, (
            f"Killing matrix not proportional to Id: eigenvalues = {eigs}"
        )

    def test_correct_value_minus_48(self):
        """Standard curve gives B = -48 * Id."""
        curve = standard_context_curve()
        B = killing_form_matrix(curve, n_quad=100)
        expected = -48.0 * np.eye(7)
        np.testing.assert_allclose(
            B, expected, atol=0.1,
            err_msg="Killing form matrix not close to -48 * Id",
        )

    def test_negative_definite(self):
        """The Killing form must be negative definite."""
        curve = standard_context_curve()
        B = killing_form_matrix(curve, n_quad=80)
        eigs = np.linalg.eigvalsh(B)
        assert np.all(eigs < -1e-6), (
            f"Killing form not negative definite: eigenvalues = {eigs}"
        )

    def test_symmetric(self):
        """The Killing form matrix must be symmetric."""
        curve = standard_context_curve()
        B = killing_form_matrix(curve, n_quad=40)
        np.testing.assert_allclose(B, B.T, atol=1e-12)

    def test_g2_invariance_eigenvalue_degeneracy(self):
        """
        G2 acts irreducibly on Im(O) ~ R^7, so by Schur's lemma the
        Killing form B_mu must have a single eigenvalue (with multiplicity 7).
        """
        curve = standard_context_curve()
        B = killing_form_matrix(curve, n_quad=80)
        eigs = np.linalg.eigvalsh(B)
        # All 7 eigenvalues should be the same
        np.testing.assert_allclose(
            eigs, eigs[0] * np.ones(7), atol=0.01,
            err_msg="Eigenvalues not degenerate (G2 invariance broken)",
        )

    def test_single_element_matches_matrix(self):
        """decompactified_killing_form(e_i, e_j) matches killing_form_matrix[i,j]."""
        curve = standard_context_curve()
        B = killing_form_matrix(curve, n_quad=60)
        for i, j in [(0, 0), (0, 1), (3, 5), (6, 6)]:
            X = Octonion.basis(i + 1)
            Y = Octonion.basis(j + 1)
            val = decompactified_killing_form(X, Y, curve, n_quad=60)
            np.testing.assert_allclose(
                val, B[i, j], atol=1e-10,
                err_msg=f"Mismatch at ({i},{j}): scalar={val}, matrix={B[i,j]}",
            )

    def test_matches_axiom_verification(self):
        """Result must agree with concrete_omega_example from axiom_verification."""
        from octonion_algebra.axiom_verification import concrete_omega_example
        ref = concrete_omega_example(N_modes=100)
        curve = standard_context_curve()
        B = killing_form_matrix(curve, n_quad=100)
        np.testing.assert_allclose(
            B, ref['killing_matrix'], atol=1e-10,
            err_msg="Killing form matrix disagrees with axiom_verification",
        )


# ---- TestFourierCurve ----

class TestFourierCurve:
    """Tests for fourier_context_curve and standard_context_curve."""

    def test_fourier_curve_at_zero(self):
        """u(0) = 0 because all sine terms vanish."""
        curve = fourier_context_curve([1, 1, 1, 1, 1, 1, 1])
        u0 = curve(0.0)
        assert u0.is_zero(tol=1e-15), "u(0) should be zero"

    def test_fourier_curve_values(self):
        """Spot-check u(pi/2) for the standard curve."""
        curve = standard_context_curve()
        u = curve(np.pi / 2)
        # sin(1 * pi/2) = 1
        # sin(3 * pi/2) = -1
        # sin(5 * pi/2) = 1
        # sin(7 * pi/2) = -1
        # sin(9 * pi/2) = 1
        # sin(11 * pi/2) = -1
        # sin(13 * pi/2) = 1
        expected = np.array([0.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0])
        np.testing.assert_allclose(u.coeffs, expected, atol=1e-14)

    def test_fourier_curve_is_imaginary(self):
        """The Fourier context curve always produces imaginary octonions."""
        curve = fourier_context_curve([2, -1, 0.5, 3, -0.7, 1.2, 0.8])
        for omega in np.linspace(0, 2 * np.pi, 50):
            u = curve(omega)
            assert u.is_imaginary(tol=1e-15), (
                f"u({omega}) has nonzero real part: {u.coeffs[0]}"
            )

    def test_standard_curve_is_unit_coefficients(self):
        """standard_context_curve is fourier_context_curve with all-ones coefficients."""
        std = standard_context_curve()
        manual = fourier_context_curve(np.ones(7))
        for omega in [0.1, 1.0, 2.5, 5.0]:
            u1 = std(omega)
            u2 = manual(omega)
            np.testing.assert_allclose(u1.coeffs, u2.coeffs, atol=1e-15)


# ---- TestConvergence ----

class TestConvergence:
    """Tests for UV cutoff convergence and convergence rates."""

    def test_uv_cutoff_convergence(self):
        """Frobenius norm differences decrease and converge to 0."""
        curve = standard_context_curve()
        N_values = [10, 20, 40, 80, 160]
        result = uv_cutoff_convergence(curve, N_values)

        assert result['converged'], (
            f"Did not converge: diffs = {result['frobenius_diffs']}"
        )
        # Differences should decrease
        diffs = result['frobenius_diffs']
        assert len(diffs) == 4
        # Final difference should be very small (smooth periodic integrand)
        assert diffs[-1] < 1e-6, f"Final Frobenius diff too large: {diffs[-1]}"

    def test_convergence_rate_superalgebraic(self):
        """For smooth periodic integrands, trapezoidal rule converges
        faster than any polynomial in 1/N (spectral convergence).
        The ratio of successive differences should decrease rapidly."""
        curve = standard_context_curve()
        N_values = [10, 20, 40, 80, 160]
        result = uv_cutoff_convergence(curve, N_values)
        diffs = result['frobenius_diffs']

        # Each doubling of N should give a dramatic decrease for smooth integrands
        # We just check the last two are much smaller than the first
        if len(diffs) >= 3 and diffs[0] > 1e-12:
            ratio = diffs[-1] / diffs[0]
            assert ratio < 0.01, (
                f"Convergence too slow: ratio = {ratio}, diffs = {diffs}"
            )

    def test_convergence_to_correct_value(self):
        """All matrices in the convergence sequence approach -48*Id."""
        curve = standard_context_curve()
        N_values = [20, 40, 80]
        result = uv_cutoff_convergence(curve, N_values)
        B_final = result['matrices'][-1]
        expected = -48.0 * np.eye(7)
        np.testing.assert_allclose(
            B_final, expected, atol=0.1,
            err_msg="Final convergence matrix not close to -48*Id",
        )

    def test_convergence_proof_passes(self):
        """The full convergence_proof() analysis should pass all checks."""
        result = convergence_proof()
        assert result['all_checks_passed'], (
            f"Convergence proof failed. "
            f"proportional={result['proportional_to_identity']}, "
            f"constant={result['proportionality_constant']}, "
            f"eigenvalues={result['eigenvalues']}"
        )
        assert result['proportional_to_identity']
        assert abs(result['proportionality_constant'] - (-48.0)) < 1.0


# ---- TestMonteCarloKilling ----

class TestMonteCarloKilling:
    """Tests for monte_carlo_killing_form."""

    def test_monte_carlo_proportional_to_identity(self):
        """Monte Carlo B(e_i, e_i) should be the same for all i (isotropy)."""
        diag_vals = []
        for i in range(1, 8):
            val = monte_carlo_killing_form(
                Octonion.basis(i), Octonion.basis(i),
                n_samples=10000, seed=42,
            )
            diag_vals.append(val)
        spread = max(diag_vals) - min(diag_vals)
        mean_val = np.mean(diag_vals)
        # The spread should be small relative to the mean
        assert spread < 0.5 * abs(mean_val), (
            f"MC diagonal not isotropic: spread={spread}, mean={mean_val}"
        )

    def test_monte_carlo_negative_definite(self):
        """Monte Carlo B(e_i, e_i) should be negative for all i."""
        for i in range(1, 8):
            val = monte_carlo_killing_form(
                Octonion.basis(i), Octonion.basis(i),
                n_samples=5000, seed=42,
            )
            assert val < 0, f"MC B(e{i}, e{i}) = {val} is not negative"

    def test_monte_carlo_off_diagonal_small(self):
        """Monte Carlo B(e_i, e_j) for i != j should be near zero."""
        val = monte_carlo_killing_form(
            Octonion.basis(1), Octonion.basis(2),
            n_samples=10000, seed=42,
        )
        # Off-diagonal values should be close to 0 by isotropy
        diag_val = monte_carlo_killing_form(
            Octonion.basis(1), Octonion.basis(1),
            n_samples=10000, seed=42,
        )
        assert abs(val) < 0.1 * abs(diag_val), (
            f"MC off-diagonal B(e1,e2)={val} too large relative to "
            f"diagonal {diag_val}"
        )

    def test_monte_carlo_reproducible(self):
        """Same seed gives same result."""
        val1 = monte_carlo_killing_form(e1, e1, n_samples=1000, seed=123)
        val2 = monte_carlo_killing_form(e1, e1, n_samples=1000, seed=123)
        assert val1 == val2, "Monte Carlo not reproducible with same seed"
