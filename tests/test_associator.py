"""Tests for octonion_algebra.associator module."""
import numpy as np
import pytest
from octonion_algebra.core import Octonion, e0, e1, e2, e3, e4, e5, e6, e7
from octonion_algebra.associator import associator, associator_norm


def test_associator_nonzero():
    """The associator [e1, e2, e4] should be nonzero."""
    result = associator(e1, e2, e4)
    assert result.norm() > 1e-10, "[e1, e2, e4] should be nonzero"


def test_associator_value():
    """[e1, e2, e4] = 2*e7 (exact coefficients)."""
    result = associator(e1, e2, e4)
    expected = Octonion.basis(7) * 2  # 2*e7
    np.testing.assert_allclose(result.coeffs, expected.coeffs, atol=1e-12,
                               err_msg="[e1, e2, e4] should equal 2*e7")


def test_associator_antisymmetric_swap_first(random_octonions):
    """Antisymmetry under swapping first two arguments: [a,b,c] = -[b,a,c]."""
    a, b, c = random_octonions[0], random_octonions[1], random_octonions[2]
    lhs = associator(a, b, c)
    rhs = associator(b, a, c)
    np.testing.assert_allclose(lhs.coeffs, (-rhs).coeffs, atol=1e-10,
                               err_msg="[a,b,c] should equal -[b,a,c]")


def test_associator_antisymmetric_swap_last(random_octonions):
    """Antisymmetry under swapping last two arguments: [a,b,c] = -[a,c,b]."""
    a, b, c = random_octonions[0], random_octonions[1], random_octonions[2]
    lhs = associator(a, b, c)
    rhs = associator(a, c, b)
    np.testing.assert_allclose(lhs.coeffs, (-rhs).coeffs, atol=1e-10,
                               err_msg="[a,b,c] should equal -[a,c,b]")


def test_associator_vanishes_equal_args(random_octonions):
    """Associator vanishes when any two arguments are equal (alternativity)."""
    a, b = random_octonions[0], random_octonions[1]

    r1 = associator(a, a, b)
    assert r1.norm() < 1e-10, "[a,a,b] should be zero"

    r2 = associator(a, b, a)
    assert r2.norm() < 1e-10, "[a,b,a] should be zero"

    r3 = associator(b, a, a)
    assert r3.norm() < 1e-10, "[b,a,a] should be zero"


def test_associator_vanishes_quaternionic():
    """Associator vanishes for elements in the same quaternionic subalgebra.

    (e1, e2, e3) form a Fano line, so [e1, e2, e3] = 0.
    """
    result = associator(e1, e2, e3)
    assert result.norm() < 1e-12, \
        "[e1, e2, e3] should be zero (same quaternionic subalgebra)"


def test_moufang_identities(random_octonions):
    """Verify all three Moufang identities for random octonions.

    1. a*(b*(a*c)) = (a*b*a)*c            (left Moufang)
    2. ((c*a)*b)*a = c*(a*b*a)            (right Moufang)
    3. (a*b)*(c*a) = a*((b*c)*a)          (middle Moufang)

    where a*b*a is unambiguous by flexibility (a*(b*a) = (a*b)*a).
    """
    a, b, c = random_octonions[0], random_octonions[1], random_octonions[2]

    # a*b*a is unambiguous by the flexible identity
    aba = a * (b * a)

    # Left Moufang: a*(b*(a*c)) = (a*b*a)*c
    lhs1 = a * (b * (a * c))
    rhs1 = aba * c
    np.testing.assert_allclose(lhs1.coeffs, rhs1.coeffs, atol=1e-9,
                               err_msg="Left Moufang identity failed")

    # Right Moufang: ((c*a)*b)*a = c*(a*b*a)
    lhs2 = ((c * a) * b) * a
    rhs2 = c * aba
    np.testing.assert_allclose(lhs2.coeffs, rhs2.coeffs, atol=1e-9,
                               err_msg="Right Moufang identity failed")

    # Middle Moufang: (a*b)*(c*a) = a*((b*c)*a)
    lhs3 = (a * b) * (c * a)
    rhs3 = a * ((b * c) * a)
    np.testing.assert_allclose(lhs3.coeffs, rhs3.coeffs, atol=1e-9,
                               err_msg="Middle Moufang identity failed")


def test_associator_in_imag():
    """For purely imaginary inputs, the associator is purely imaginary."""
    seeds = [10, 11, 12, 13, 14, 15]
    for i in range(0, len(seeds) - 2, 3):
        a = Octonion.random(seed=seeds[i]).imag_part()
        b = Octonion.random(seed=seeds[i + 1]).imag_part()
        c = Octonion.random(seed=seeds[i + 2]).imag_part()
        result = associator(a, b, c)
        assert abs(result.real_part()) < 1e-10, \
            f"Associator of imaginary octonions should be imaginary, got real part {result.real_part()}"
