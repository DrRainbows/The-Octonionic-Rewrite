"""Tests for octonion_algebra.core module."""
import numpy as np
import pytest
from octonion_algebra.core import (
    Octonion, e0, e1, e2, e3, e4, e5, e6, e7, oct,
    FANO_TRIPLES, cross_product_7d,
)


def test_basis_squares(imaginary_basis):
    """e_i^2 = -1 for all imaginary basis elements i=1..7."""
    for ei in imaginary_basis:
        result = ei * ei
        expected = Octonion.real(-1)
        np.testing.assert_allclose(result.coeffs, expected.coeffs, atol=1e-12)


def test_fano_triples():
    """e_i * e_j = e_k and e_j * e_i = -e_k for all 7 Fano triples."""
    bases = [e0, e1, e2, e3, e4, e5, e6, e7]
    for (i, j, k) in FANO_TRIPLES:
        result_ij = bases[i] * bases[j]
        np.testing.assert_allclose(result_ij.coeffs, bases[k].coeffs, atol=1e-12,
                                   err_msg=f"e{i}*e{j} should be e{k}")
        result_ji = bases[j] * bases[i]
        np.testing.assert_allclose(result_ji.coeffs, (-bases[k]).coeffs, atol=1e-12,
                                   err_msg=f"e{j}*e{i} should be -e{k}")


def test_cyclic_fano():
    """Cyclic permutations of Fano triples: e_j*e_k = e_i, e_k*e_i = e_j."""
    bases = [e0, e1, e2, e3, e4, e5, e6, e7]
    for (i, j, k) in FANO_TRIPLES:
        result_jk = bases[j] * bases[k]
        np.testing.assert_allclose(result_jk.coeffs, bases[i].coeffs, atol=1e-12,
                                   err_msg=f"e{j}*e{k} should be e{i}")
        result_ki = bases[k] * bases[i]
        np.testing.assert_allclose(result_ki.coeffs, bases[j].coeffs, atol=1e-12,
                                   err_msg=f"e{k}*e{i} should be e{j}")


def test_norm_multiplicative(random_octonions):
    """Norm is multiplicative: |ab| = |a|*|b| for random octonion pairs."""
    for i in range(len(random_octonions)):
        for j in range(i + 1, len(random_octonions)):
            a = random_octonions[i]
            b = random_octonions[j]
            product_norm = (a * b).norm()
            norms_product = a.norm() * b.norm()
            np.testing.assert_allclose(product_norm, norms_product, rtol=1e-10,
                                       err_msg=f"Norm not multiplicative for pair ({i},{j})")


def test_inverse(random_octonions):
    """a * a^{-1} = 1 for random nonzero octonions."""
    one = Octonion.real(1)
    for a in random_octonions:
        result = a * a.inverse()
        np.testing.assert_allclose(result.coeffs, one.coeffs, atol=1e-10)


def test_conjugation_anti_homomorphism(random_octonions):
    """conj(ab) = conj(b) * conj(a) for random octonion pairs."""
    for i in range(len(random_octonions)):
        for j in range(i + 1, len(random_octonions)):
            a = random_octonions[i]
            b = random_octonions[j]
            lhs = (a * b).conjugate()
            rhs = b.conjugate() * a.conjugate()
            np.testing.assert_allclose(lhs.coeffs, rhs.coeffs, atol=1e-10,
                                       err_msg=f"Conjugation anti-homomorphism failed for pair ({i},{j})")


def test_left_alternativity(random_octonions):
    """Left alternativity: (a*a)*b = a*(a*b) for random octonions."""
    for i in range(len(random_octonions)):
        a = random_octonions[i]
        b = random_octonions[(i + 1) % len(random_octonions)]
        lhs = (a * a) * b
        rhs = a * (a * b)
        np.testing.assert_allclose(lhs.coeffs, rhs.coeffs, atol=1e-10,
                                   err_msg=f"Left alternativity failed for index {i}")


def test_right_alternativity(random_octonions):
    """Right alternativity: (b*a)*a = b*(a*a) for random octonions."""
    for i in range(len(random_octonions)):
        a = random_octonions[i]
        b = random_octonions[(i + 1) % len(random_octonions)]
        lhs = (b * a) * a
        rhs = b * (a * a)
        np.testing.assert_allclose(lhs.coeffs, rhs.coeffs, atol=1e-10,
                                   err_msg=f"Right alternativity failed for index {i}")


def test_nonassociative():
    """Octonions are not associative: (e1*e2)*e4 != e1*(e2*e4)."""
    lhs = (e1 * e2) * e4
    rhs = e1 * (e2 * e4)
    assert not np.allclose(lhs.coeffs, rhs.coeffs, atol=1e-10), \
        "(e1*e2)*e4 should differ from e1*(e2*e4)"


def test_noncommutative():
    """Octonions are not commutative: e1*e2 != e2*e1."""
    lhs = e1 * e2
    rhs = e2 * e1
    assert not np.allclose(lhs.coeffs, rhs.coeffs, atol=1e-10), \
        "e1*e2 should differ from e2*e1"


def test_cross_product_antisymmetric(random_octonions):
    """Cross product is antisymmetric: a x b = -(b x a) for imaginary octonions."""
    for i in range(len(random_octonions)):
        a = random_octonions[i].imag_part()
        b = random_octonions[(i + 1) % len(random_octonions)].imag_part()
        ab = cross_product_7d(a, b)
        ba = cross_product_7d(b, a)
        np.testing.assert_allclose(ab.coeffs, (-ba).coeffs, atol=1e-10,
                                   err_msg=f"Cross product antisymmetry failed for index {i}")


def test_cross_product_orthogonal(random_octonions):
    """Cross product is orthogonal to its inputs: a . (a x b) = 0."""
    for i in range(len(random_octonions)):
        a = random_octonions[i].imag_part()
        b = random_octonions[(i + 1) % len(random_octonions)].imag_part()
        cp = cross_product_7d(a, b)
        dot_a = a.dot(cp)
        dot_b = b.dot(cp)
        assert abs(dot_a) < 1e-10, f"a . (a x b) should be 0, got {dot_a}"
        assert abs(dot_b) < 1e-10, f"b . (a x b) should be 0, got {dot_b}"


def test_cross_product_magnitude(random_octonions):
    """|a x b|^2 = |a|^2|b|^2 - (a.b)^2 for imaginary octonions."""
    for i in range(len(random_octonions)):
        a = random_octonions[i].imag_part()
        b = random_octonions[(i + 1) % len(random_octonions)].imag_part()
        cp = cross_product_7d(a, b)
        lhs = cp.norm_squared()
        rhs = a.norm_squared() * b.norm_squared() - a.dot(b) ** 2
        np.testing.assert_allclose(lhs, rhs, atol=1e-10,
                                   err_msg=f"Cross product magnitude identity failed for index {i}")
