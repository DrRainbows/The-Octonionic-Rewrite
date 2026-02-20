"""
Comprehensive tests for octonion_algebra.axiom_verification.

Tests cover all six COA axioms (A1-A6), the concrete Omega example for the
decompactified Killing form, sedenion arithmetic, and associator injectivity.
"""

import numpy as np
import pytest

from octonion_algebra.core import Octonion, e0, e1, e2, e3, e4, e5, e6, e7
from octonion_algebra.axiom_verification import (
    verify_alternativity,
    verify_composition_algebra,
    verify_division_algebra,
    verify_nucleus_is_real,
    verify_maximality,
    verify_nondegeneracy,
    concrete_omega_example,
    verify_all_coa_axioms,
    sedenion_multiply,
    associator_injectivity_check,
)


# ---- A1: Alternativity ----

class TestAlternativity:
    def test_alternativity_passes(self):
        """Verify (xx)y = x(xy) and (yx)x = y(xx) for random samples."""
        result = verify_alternativity(n_samples=500, seed=123)
        assert result['passed'], f"Alternativity failed, max error = {result['max_error']}"
        assert result['max_error'] < 1e-10
        assert result['n_tested'] == 500

    def test_alternativity_on_basis(self):
        """Alternativity must hold exactly on basis elements."""
        for ei in [e1, e2, e3, e4, e5, e6, e7]:
            for ej in [e1, e2, e3, e4, e5, e6, e7]:
                lhs = (ei * ei) * ej
                rhs = ei * (ei * ej)
                np.testing.assert_allclose(
                    lhs.coeffs, rhs.coeffs, atol=1e-14,
                    err_msg=f"Left alternativity failed for ({ei}, {ej})",
                )
                lhs_r = (ej * ei) * ei
                rhs_r = ej * (ei * ei)
                np.testing.assert_allclose(
                    lhs_r.coeffs, rhs_r.coeffs, atol=1e-14,
                    err_msg=f"Right alternativity failed for ({ej}, {ei})",
                )


# ---- A2: Non-degeneracy ----

class TestNondegeneracy:
    def test_nondegeneracy(self):
        """Norm is positive-definite: N(x)>0 for x!=0, N(0)=0."""
        result = verify_nondegeneracy(n_samples=300, seed=77)
        assert result['passed']
        assert result['min_nonzero_norm'] > 0
        assert result['n_tested'] == 300

    def test_zero_norm(self):
        """The zero octonion has norm zero."""
        assert Octonion().norm_squared() == 0.0

    def test_basis_norms(self):
        """Each basis element has norm 1."""
        for i in range(8):
            np.testing.assert_allclose(Octonion.basis(i).norm(), 1.0, atol=1e-15)


# ---- A3: Composition algebra ----

class TestComposition:
    def test_composition_passes(self):
        """N(xy) = N(x)N(y) for random pairs."""
        result = verify_composition_algebra(n_samples=500, seed=99)
        assert result['passed'], f"Composition failed, max error = {result['max_error']}"
        assert result['max_error'] < 1e-10

    def test_composition_on_basis(self):
        """Composition property on all pairs of imaginary basis elements."""
        bases = [e1, e2, e3, e4, e5, e6, e7]
        for a in bases:
            for b in bases:
                lhs = (a * b).norm_squared()
                rhs = a.norm_squared() * b.norm_squared()
                np.testing.assert_allclose(lhs, rhs, atol=1e-14)


# ---- A4: Division algebra ----

class TestDivision:
    def test_division_passes(self):
        """No zero divisors among random nonzero octonions; inverses work."""
        result = verify_division_algebra(n_samples=500, seed=55)
        assert result['passed'], f"Division failed, max_inverse_error = {result['max_inverse_error']}"
        assert result['max_inverse_error'] < 1e-10

    def test_inverse_identity(self):
        """x * x^{-1} = 1 for several random octonions."""
        one = Octonion.real(1.0)
        for seed in range(20):
            x = Octonion.random(seed=seed)
            product = x * x.inverse()
            np.testing.assert_allclose(product.coeffs, one.coeffs, atol=1e-10)


# ---- A5: Nucleus = R*1 ----

class TestNucleus:
    def test_nucleus_real_only(self):
        """Nucleus contains only real multiples of 1."""
        result = verify_nucleus_is_real(n_samples=200, seed=33)
        assert result['passed']
        assert result['nucleus_contains_only_reals']
        assert result['max_real_error'] < 1e-10
        # Must have found a nonzero associator for each e_i
        assert len(result['imaginary_nonzero_examples']) == 7

    def test_real_in_nucleus(self):
        """A real multiple of 1 always associates to zero."""
        from octonion_algebra.associator import associator
        rng = np.random.default_rng(42)
        for _ in range(50):
            r = rng.standard_normal()
            a = Octonion.real(r)
            x = Octonion(rng.standard_normal(8))
            y = Octonion(rng.standard_normal(8))
            assert associator(a, x, y).norm() < 1e-10


# ---- A6: Maximality / Sedenions ----

class TestMaximality:
    def test_maximality_sedenion_zero_divisors(self):
        """Sedenions have zero divisors => dim 8 is maximal for normed division algebras."""
        result = verify_maximality()
        assert result['passed']
        assert result['octonion_dim'] == 8
        assert result['sedenion_has_zero_divisors']

    def test_sedenion_multiply_basic(self):
        """Sedenion multiplication: unit * unit = unit, and (1,0)*(a,b)=(a,b)."""
        # Sedenion identity is (1, 0, ..., 0)
        identity = [0.0] * 16
        identity[0] = 1.0

        # Random element
        rng = np.random.default_rng(42)
        x = rng.standard_normal(16).tolist()

        # identity * x = x
        product = sedenion_multiply(identity, x)
        np.testing.assert_allclose(product, x, atol=1e-12,
                                   err_msg="Left multiplication by sedenion identity failed")

        # x * identity = x
        product2 = sedenion_multiply(x, identity)
        np.testing.assert_allclose(product2, x, atol=1e-12,
                                   err_msg="Right multiplication by sedenion identity failed")

    def test_sedenion_conjugate_norm(self):
        """For sedenions, x * conj(x) should equal |x|^2 * identity
        (this is the norm form, which holds even for sedenions)."""
        rng = np.random.default_rng(7)
        x = rng.standard_normal(16)
        # Conjugate: negate components 1..15
        x_conj = x.copy()
        x_conj[1:] = -x_conj[1:]
        product = np.array(sedenion_multiply(x.tolist(), x_conj.tolist()))
        expected_norm_sq = np.dot(x, x)
        # Real part should be |x|^2, imaginary parts should be ~0
        np.testing.assert_allclose(product[0], expected_norm_sq, rtol=1e-10)
        np.testing.assert_allclose(product[1:], 0.0, atol=1e-10)

    def test_sedenion_not_alternative(self):
        """Sedenions fail left alternativity: (xx)y != x(xy) for some x, y."""
        # Use basis elements that go beyond octonions
        # x = e1 + e9, y = e2 + e10
        x = [0.0] * 16
        x[1] = 1.0
        x[9] = 1.0
        y = [0.0] * 16
        y[2] = 1.0
        y[10] = 1.0

        xx = sedenion_multiply(x, x)
        xxy = sedenion_multiply(xx, y)
        xy = sedenion_multiply(x, y)
        x_xy = sedenion_multiply(x, xy)

        diff = np.array(xxy) - np.array(x_xy)
        # If sedenions were alternative, this would be zero.
        # They are not, so for generic elements it should be nonzero.
        # But for this particular choice we need to verify:
        # If this specific pair happens to be alternative, try another.
        if np.linalg.norm(diff) < 1e-10:
            # Try a more general element
            rng = np.random.default_rng(0)
            x = rng.standard_normal(16).tolist()
            y = rng.standard_normal(16).tolist()
            xx = sedenion_multiply(x, x)
            xxy = sedenion_multiply(xx, y)
            xy = sedenion_multiply(x, y)
            x_xy = sedenion_multiply(x, xy)
            diff = np.array(xxy) - np.array(x_xy)

        assert np.linalg.norm(diff) > 1e-10, \
            "Sedenions should NOT be alternative, but (xx)y = x(xy) held"


# ---- Concrete Omega / Killing form ----

class TestConcreteOmega:
    def test_concrete_omega_negative_definite(self):
        """The decompactified Killing form B_mu must be negative-definite."""
        result = concrete_omega_example(N_modes=40)
        assert result['is_negative_definite'], (
            f"Killing form not negative definite; eigenvalues = {result['eigenvalues']}"
        )
        assert np.all(result['eigenvalues'] < 0)

    def test_concrete_omega_g2_invariant(self):
        """
        For the G2-invariant Killing form, B_mu should be proportional to
        -Id on the 7D imaginary space (since G2 acts irreducibly on R^7).
        """
        result = concrete_omega_example(N_modes=80)
        B = result['killing_matrix']
        eigs = result['eigenvalues']

        # All eigenvalues should be equal (proportional to -Id)
        # They should all be negative.
        assert np.all(eigs < 0), f"Not all eigenvalues negative: {eigs}"

        # Check proportionality: all eigenvalues close to each other
        ratio = eigs.max() / eigs.min()
        assert abs(ratio - 1.0) < 0.05, (
            f"Eigenvalues not proportional to -Id: ratio = {ratio}, eigs = {eigs}"
        )

    def test_concrete_omega_symmetry(self):
        """The Killing matrix must be symmetric."""
        result = concrete_omega_example(N_modes=20)
        B = result['killing_matrix']
        np.testing.assert_allclose(B, B.T, atol=1e-12)


# ---- Associator injectivity ----

class TestAssociatorInjectivity:
    def test_associator_injectivity(self):
        """
        Associator [a,b,c] = 0 iff a,b,c lie in a quaternionic subalgebra
        (i.e., their imaginary parts span a Fano-line subspace).
        """
        result = associator_injectivity_check(n_samples=200, seed=42)
        assert result['injectivity_holds']
        # For generic random triples, there should be no zero-associator
        # examples (probability zero for 7D random vectors to land in a
        # 3D subspace).
        assert len(result['zero_associator_examples']) == 0, (
            f"Found {len(result['zero_associator_examples'])} unexpected zero-associator triples"
        )

    def test_fano_triples_have_zero_associator(self):
        """Basis triples on a Fano line have zero associator."""
        from octonion_algebra.associator import associator_norm
        from octonion_algebra.core import FANO_TRIPLES
        for (i, j, k) in FANO_TRIPLES:
            ei = Octonion.basis(i)
            ej = Octonion.basis(j)
            ek = Octonion.basis(k)
            assert associator_norm(ei, ej, ek) < 1e-12, \
                f"Fano triple ({i},{j},{k}) should have zero associator"


# ---- Full suite ----

class TestFullSuite:
    def test_full_axiom_suite(self):
        """verify_all_coa_axioms() should report all_passed = True."""
        results = verify_all_coa_axioms()
        assert results['all_passed'], (
            "Full axiom suite did not pass. Failing axioms: "
            + ", ".join(
                k for k in results
                if k != 'all_passed'
                and isinstance(results[k], dict)
                and not results[k].get('passed', results[k].get('is_negative_definite', True))
            )
        )
