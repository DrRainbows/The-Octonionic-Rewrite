"""Tests for the octonion_algebra.deformation module.

Tests the continuous deformation from quaternions (epsilon=0) to
full octonions (epsilon=1), verifying associativity, Killing form,
derivation dimensions, and algebraic consistency.
"""

import numpy as np
import pytest

from octonion_algebra.core import Octonion, e0, e1, e2, e3, e4, e5, e6, e7, FANO_TRIPLES
from octonion_algebra.calculus import structure_constants
from octonion_algebra.associator import associator
from octonion_algebra.deformation import (
    deformed_structure_constants,
    deformed_multiply,
    DeformedOctonion,
    deformed_associator,
    associativity_measure,
    killing_form_spectral_flow,
    derivation_dimension,
    deformation_summary,
)


# ---------------------------------------------------------------------------
# 1. Quaternionic multiplication at epsilon=0
# ---------------------------------------------------------------------------

class TestEpsilonZeroQuaternionMultiplication:
    """At epsilon=0 the deformed product on e1, e2, e3 matches quaternion rules."""

    def test_e1_times_e2_equals_e3(self):
        """e1 * e2 = e3 at epsilon=0 (quaternion i*j = k)."""
        result = deformed_multiply(e1.coeffs, e2.coeffs, epsilon=0.0)
        expected = e3.coeffs
        np.testing.assert_allclose(result, expected, atol=1e-12)

    def test_e2_times_e3_equals_e1(self):
        """e2 * e3 = e1 at epsilon=0 (quaternion j*k = i)."""
        result = deformed_multiply(e2.coeffs, e3.coeffs, epsilon=0.0)
        expected = e1.coeffs
        np.testing.assert_allclose(result, expected, atol=1e-12)

    def test_e3_times_e1_equals_e2(self):
        """e3 * e1 = e2 at epsilon=0 (quaternion k*i = j)."""
        result = deformed_multiply(e3.coeffs, e1.coeffs, epsilon=0.0)
        expected = e2.coeffs
        np.testing.assert_allclose(result, expected, atol=1e-12)

    def test_e1_squared_is_minus_one(self):
        """e1^2 = -1 at epsilon=0."""
        result = deformed_multiply(e1.coeffs, e1.coeffs, epsilon=0.0)
        expected = (-e0).coeffs
        np.testing.assert_allclose(result, expected, atol=1e-12)


# ---------------------------------------------------------------------------
# 2. Associator at epsilon=0 is zero for quaternionic inputs
# ---------------------------------------------------------------------------

class TestEpsilonZeroAssociatorVanishes:
    """At epsilon=0 the associator vanishes for any quaternionic triple."""

    def test_quaternionic_triple_e1_e2_e3(self):
        """[e1, e2, e3]_{eps=0} = 0."""
        a = DeformedOctonion(e1.coeffs, epsilon=0.0)
        b = DeformedOctonion(e2.coeffs, epsilon=0.0)
        c = DeformedOctonion(e3.coeffs, epsilon=0.0)
        assoc = deformed_associator(a, b, c, epsilon=0.0)
        np.testing.assert_allclose(assoc.coeffs, 0.0, atol=1e-12)

    def test_random_quaternionic_inputs(self):
        """Associator vanishes for arbitrary quaternionic elements at eps=0."""
        rng = np.random.default_rng(123)
        for _ in range(10):
            # Random quaternionic elements: nonzero only in components 0,1,2,3
            qa = np.zeros(8)
            qa[:4] = rng.standard_normal(4)
            qb = np.zeros(8)
            qb[:4] = rng.standard_normal(4)
            qc = np.zeros(8)
            qc[:4] = rng.standard_normal(4)

            assoc = deformed_associator(
                DeformedOctonion(qa, epsilon=0.0),
                DeformedOctonion(qb, epsilon=0.0),
                DeformedOctonion(qc, epsilon=0.0),
                epsilon=0.0
            )
            np.testing.assert_allclose(
                assoc.coeffs, 0.0, atol=1e-10,
                err_msg="Quaternionic associator should vanish at eps=0"
            )


# ---------------------------------------------------------------------------
# 3. At epsilon=1 the deformed product matches standard octonion product
# ---------------------------------------------------------------------------

class TestEpsilonOneMatchesOctonions:
    """At epsilon=1 the deformed multiplication equals standard octonionic."""

    def test_all_fano_triple_products(self):
        """e_i * e_j = e_k for all 7 Fano triples at epsilon=1."""
        bases = [e0, e1, e2, e3, e4, e5, e6, e7]
        for (i, j, k) in FANO_TRIPLES:
            result = deformed_multiply(bases[i].coeffs, bases[j].coeffs, epsilon=1.0)
            np.testing.assert_allclose(
                result, bases[k].coeffs, atol=1e-12,
                err_msg=f"e{i}*e{j} should be e{k} at eps=1"
            )

    def test_random_product_matches_standard(self):
        """Random a*b via deformed_multiply(eps=1) equals standard Octonion product."""
        rng = np.random.default_rng(77)
        for _ in range(20):
            a_coeffs = rng.standard_normal(8)
            b_coeffs = rng.standard_normal(8)
            deformed_result = deformed_multiply(a_coeffs, b_coeffs, epsilon=1.0)
            standard_result = (Octonion(a_coeffs) * Octonion(b_coeffs)).coeffs
            np.testing.assert_allclose(
                deformed_result, standard_result, atol=1e-12,
                err_msg="Deformed product at eps=1 should match standard"
            )


# ---------------------------------------------------------------------------
# 4. Associator at epsilon=1 matches standard octonionic associator
# ---------------------------------------------------------------------------

def test_associator_eps1_matches_standard():
    """Deformed associator at eps=1 equals the standard octonionic associator."""
    triples = [
        (e1, e2, e4),
        (e1, e4, e6),
        (e3, e5, e7),
    ]
    for a, b, c in triples:
        da = DeformedOctonion(a.coeffs, epsilon=1.0)
        db = DeformedOctonion(b.coeffs, epsilon=1.0)
        dc = DeformedOctonion(c.coeffs, epsilon=1.0)
        deformed_assoc = deformed_associator(da, db, dc, epsilon=1.0)
        standard_assoc = associator(a, b, c)
        np.testing.assert_allclose(
            deformed_assoc.coeffs, standard_assoc.coeffs, atol=1e-12,
            err_msg=f"Associator mismatch at eps=1 for ({a}, {b}, {c})"
        )


# ---------------------------------------------------------------------------
# 5. Associativity measure: 0 at eps=0, positive at eps=1
# ---------------------------------------------------------------------------

def test_associativity_measure_zero_at_eps0():
    """Associativity measure is 0 at epsilon=0."""
    measure = associativity_measure(0.0, n_samples=100, seed=42)
    assert measure < 1e-12, f"Expected ~0 at eps=0, got {measure}"


def test_associativity_measure_positive_at_eps1():
    """Associativity measure is strictly positive at epsilon=1."""
    measure = associativity_measure(1.0, n_samples=100, seed=42)
    assert measure > 0.01, f"Expected positive at eps=1, got {measure}"


# ---------------------------------------------------------------------------
# 6. Killing form diagonal is -8 at epsilon=1
# ---------------------------------------------------------------------------

def test_killing_form_diagonal_eps1():
    """At epsilon=1 all 7 eigenvalues of the Killing form equal -8."""
    result = killing_form_spectral_flow(epsilon_values=[1.0])
    eigs = result['eigenvalues'][0]
    np.testing.assert_allclose(
        eigs, -8.0 * np.ones(7), atol=1e-10,
        err_msg="Killing form eigenvalues should all be -8 at eps=1"
    )


# ---------------------------------------------------------------------------
# 7. Derivation dimension is 3 at epsilon=0
# ---------------------------------------------------------------------------

def test_derivation_dimension_eps0():
    """dim Der(A_0) = 9 = so(3) + so(4).

    At epsilon=0, the 6 non-quaternionic Fano triples vanish, leaving the
    quaternionic triple (1,2,3) plus 4 'null' imaginary directions e4-e7 whose
    mutual cross-products are all zero. Derivations decompose as:
      - so(3) acting on {e1, e2, e3}  (3 parameters)
      - so(4) acting on {e4, e5, e6, e7} (6 parameters)
    The so(4) rotations are trivially derivations because all products among
    e4-e7 cross-terms vanish. Total = 3 + 6 = 9.
    """
    dim = derivation_dimension(0.0)
    assert dim == 9, f"Expected dim Der = 9 at eps=0, got {dim}"


# ---------------------------------------------------------------------------
# 8. Derivation dimension is 14 at epsilon=1
# ---------------------------------------------------------------------------

def test_derivation_dimension_eps1():
    """dim Der(A_1) = 14 (the g2 derivations of octonions)."""
    dim = derivation_dimension(1.0)
    assert dim == 14, f"Expected dim Der = 14 at eps=1, got {dim}"


# ---------------------------------------------------------------------------
# 9. Monotonicity: associativity_measure(eps1) <= associativity_measure(eps2)
# ---------------------------------------------------------------------------

def test_associativity_measure_monotonic():
    """Associativity measure is non-decreasing with epsilon."""
    eps_values = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
    measures = [associativity_measure(e, n_samples=200, seed=42) for e in eps_values]
    for i in range(len(measures) - 1):
        assert measures[i] <= measures[i + 1] + 1e-10, (
            f"Associativity measure not monotonic: "
            f"eps={eps_values[i]} -> {measures[i]:.6f}, "
            f"eps={eps_values[i+1]} -> {measures[i+1]:.6f}"
        )


# ---------------------------------------------------------------------------
# 10. Structure constants at eps=1 match standard structure_constants()
# ---------------------------------------------------------------------------

def test_structure_constants_eps1_matches_standard():
    """deformed_structure_constants(1.0) equals calculus.structure_constants()."""
    deformed = deformed_structure_constants(1.0)
    standard = structure_constants()
    np.testing.assert_allclose(
        deformed, standard, atol=1e-12,
        err_msg="Deformed structure constants at eps=1 should match standard"
    )


# ---------------------------------------------------------------------------
# 11. Norm multiplicativity at eps=0 and eps=1
# ---------------------------------------------------------------------------

class TestNormMultiplicativity:
    """Check |a *_eps b| = |a| * |b| at key epsilon values."""

    def test_norm_multiplicative_eps1(self):
        """Norm is multiplicative at eps=1 (full octonions are a composition algebra)."""
        rng = np.random.default_rng(55)
        for _ in range(20):
            a = DeformedOctonion(rng.standard_normal(8), epsilon=1.0)
            b = DeformedOctonion(rng.standard_normal(8), epsilon=1.0)
            product_norm = (a * b).norm()
            norms_product = a.norm() * b.norm()
            np.testing.assert_allclose(
                product_norm, norms_product, rtol=1e-10,
                err_msg="Norm should be multiplicative at eps=1"
            )

    def test_norm_multiplicative_eps0_quaternionic(self):
        """Norm is multiplicative at eps=0 for quaternionic inputs."""
        rng = np.random.default_rng(55)
        for _ in range(20):
            # Quaternionic inputs: only components 0,1,2,3
            a_coeffs = np.zeros(8)
            a_coeffs[:4] = rng.standard_normal(4)
            b_coeffs = np.zeros(8)
            b_coeffs[:4] = rng.standard_normal(4)
            a = DeformedOctonion(a_coeffs, epsilon=0.0)
            b = DeformedOctonion(b_coeffs, epsilon=0.0)
            product_norm = (a * b).norm()
            norms_product = a.norm() * b.norm()
            np.testing.assert_allclose(
                product_norm, norms_product, rtol=1e-10,
                err_msg="Norm should be multiplicative at eps=0 for quaternionic inputs"
            )


# ---------------------------------------------------------------------------
# 12. DeformedOctonion class basics
# ---------------------------------------------------------------------------

class TestDeformedOctonionClass:
    """Test DeformedOctonion class methods and properties."""

    def test_conjugate(self):
        """Conjugation negates imaginary parts."""
        x = DeformedOctonion([1, 2, 3, 4, 5, 6, 7, 8], epsilon=0.5)
        xbar = x.conjugate()
        np.testing.assert_allclose(xbar.coeffs[0], 1.0)
        np.testing.assert_allclose(xbar.coeffs[1:], -x.coeffs[1:])

    def test_norm(self):
        """Norm is sqrt of sum of squares."""
        x = DeformedOctonion([3, 0, 0, 4, 0, 0, 0, 0], epsilon=0.5)
        np.testing.assert_allclose(x.norm(), 5.0, atol=1e-12)

    def test_scalar_multiplication(self):
        """Scalar multiplication works correctly."""
        x = DeformedOctonion([1, 2, 3, 4, 5, 6, 7, 8], epsilon=0.5)
        result = x * 2.0
        np.testing.assert_allclose(result.coeffs, x.coeffs * 2.0)
        result2 = 3.0 * x
        np.testing.assert_allclose(result2.coeffs, x.coeffs * 3.0)

    def test_addition_subtraction(self):
        """Addition and subtraction of DeformedOctonion instances."""
        a = DeformedOctonion([1, 2, 3, 4, 0, 0, 0, 0], epsilon=0.5)
        b = DeformedOctonion([0, 0, 0, 0, 5, 6, 7, 8], epsilon=0.5)
        s = a + b
        np.testing.assert_allclose(s.coeffs, [1, 2, 3, 4, 5, 6, 7, 8])
        d = a - b
        np.testing.assert_allclose(d.coeffs, [1, 2, 3, 4, -5, -6, -7, -8])


# ---------------------------------------------------------------------------
# 13. Structure constants: quaternionic triple always has weight 1
# ---------------------------------------------------------------------------

def test_structure_constants_quaternionic_triple_unchanged():
    """The quaternionic triple (0,1,2) always has weight 1 regardless of epsilon."""
    for eps_val in [0.0, 0.3, 0.5, 0.7, 1.0]:
        sc = deformed_structure_constants(eps_val)
        # 0-indexed: e1=0, e2=1, e3=2
        assert sc[0, 1, 2] == 1.0, f"f_012 should be +1 at eps={eps_val}"
        assert sc[1, 0, 2] == -1.0, f"f_102 should be -1 at eps={eps_val}"


# ---------------------------------------------------------------------------
# 14. deformation_summary returns correct structure
# ---------------------------------------------------------------------------

def test_deformation_summary_structure():
    """deformation_summary returns dict with correct keys and sizes."""
    result = deformation_summary(n_epsilon=3)
    assert 'epsilon' in result
    assert 'associativity_measure' in result
    assert 'derivation_dimension' in result
    assert 'killing_eigenvalues' in result
    assert len(result['epsilon']) == 3
    assert len(result['associativity_measure']) == 3
    assert len(result['derivation_dimension']) == 3
    assert len(result['killing_eigenvalues']) == 3
    np.testing.assert_allclose(result['epsilon'], [0.0, 0.5, 1.0], atol=1e-12)
