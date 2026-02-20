"""
Tests for octonionic vector calculus identities (Chapter 11).
"""
import numpy as np
import pytest
from octonion_algebra.core import (
    Octonion, cross_product_7d,
    e1, e2, e3, e4, e5, e6, e7,
)
from octonion_algebra.associator import associator
from octonion_algebra.calculus import (
    cross_product_associator,
    bac_cab_7d,
    jacobiator_7d,
    malcev_identity,
    structure_constants,
    fano_correction_tensor,
)

TOL = 1e-10

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

BASIS = [e1, e2, e3, e4, e5, e6, e7]


def random_imaginary(rng):
    """Return a random purely imaginary octonion."""
    c = np.zeros(8)
    c[1:] = rng.uniform(-1, 1, size=7)
    return Octonion(c)


def random_3d(rng):
    """Return a random imaginary octonion in span{e1, e2, e3}."""
    c = np.zeros(8)
    c[1:4] = rng.uniform(-1, 1, size=3)
    return Octonion(c)


# ---------------------------------------------------------------------------
# 1. BAC-CAB for all basis triples
# ---------------------------------------------------------------------------

def test_bac_cab_basis_triples():
    """For all 7^3 = 343 basis triples, verify modified BAC-CAB: lhs ~ rhs."""
    for a in BASIS:
        for b in BASIS:
            for c in BASIS:
                result = bac_cab_7d(a, b, c)
                diff = (result['lhs'] - result['rhs']).norm()
                assert diff < TOL, (
                    f"BAC-CAB failed for basis triple "
                    f"a={a}, b={b}, c={c}: diff={diff}"
                )


# ---------------------------------------------------------------------------
# 2. BAC-CAB for random imaginary octonions
# ---------------------------------------------------------------------------

def test_bac_cab_random():
    """For 20 random imaginary octonions, verify BAC-CAB."""
    rng = np.random.default_rng(42)
    for _ in range(20):
        a = random_imaginary(rng)
        b = random_imaginary(rng)
        c = random_imaginary(rng)
        result = bac_cab_7d(a, b, c)
        diff = (result['lhs'] - result['rhs']).norm()
        assert diff < TOL, f"BAC-CAB failed for random triple: diff={diff}"


# ---------------------------------------------------------------------------
# 3. BAC-CAB recovers 3D (correction term vanishes)
# ---------------------------------------------------------------------------

def test_bac_cab_recovers_3d():
    """For vectors in span{e1, e2, e3}, the correction term is zero."""
    rng = np.random.default_rng(99)
    for _ in range(20):
        a = random_3d(rng)
        b = random_3d(rng)
        c = random_3d(rng)
        result = bac_cab_7d(a, b, c)
        corr_norm = result['correction'].norm()
        assert corr_norm < TOL, (
            f"Correction should vanish in 3D slice, got norm={corr_norm}"
        )


# ---------------------------------------------------------------------------
# 4. Jacobiator equals 3 * Im(associator)
# ---------------------------------------------------------------------------

def test_jacobiator_equals_neg_3_2_associator():
    """For random imaginary octonions, J(a,b,c) = -(3/2) * [a,b,c].

    The jacobiator of the 7D cross product equals -(3/2) times the
    octonionic associator. For purely imaginary inputs, [a,b,c] is
    purely imaginary.
    """
    rng = np.random.default_rng(123)
    for _ in range(20):
        a = random_imaginary(rng)
        b = random_imaginary(rng)
        c = random_imaginary(rng)
        J = jacobiator_7d(a, b, c)
        assoc = associator(a, b, c)
        expected = assoc * (-1.5)
        diff = (J - expected).norm()
        assert diff < TOL, (
            f"Jacobiator != -(3/2)*[a,b,c]: diff={diff}"
        )


# ---------------------------------------------------------------------------
# 5. Jacobiator is zero in 3D
# ---------------------------------------------------------------------------

def test_jacobiator_zero_in_3d():
    """For vectors in span{e1, e2, e3}, the jacobiator vanishes."""
    rng = np.random.default_rng(456)
    for _ in range(20):
        a = random_3d(rng)
        b = random_3d(rng)
        c = random_3d(rng)
        J = jacobiator_7d(a, b, c)
        assert J.norm() < TOL, f"Jacobiator should be zero in 3D, got norm={J.norm()}"


# ---------------------------------------------------------------------------
# 6. Jacobiator nonzero for the canonical example e1, e2, e4
# ---------------------------------------------------------------------------

def test_jacobiator_nonzero_7d():
    """For e1, e2, e4: J = -3*e7 (the canonical example from the book)."""
    J = jacobiator_7d(e1, e2, e4)
    expected = e7 * (-3.0)
    diff = (J - expected).norm()
    assert diff < TOL, f"Expected J = -3*e7, got {J}, diff={diff}"
    # Confirm it is indeed nonzero
    assert J.norm() > 1.0, f"Jacobiator should be nonzero, got norm={J.norm()}"


# ---------------------------------------------------------------------------
# 7. Cross-product associator is alternating
# ---------------------------------------------------------------------------

def test_cross_product_associator_vs_octonionic():
    """[a,b,c]_x = [a,b,c] - (b.c)*a + (a.b)*c for purely imaginary inputs.

    The cross-product associator differs from the octonionic associator
    by dot-product correction terms. This identity connects the two.
    """
    rng = np.random.default_rng(789)
    for _ in range(20):
        a = random_imaginary(rng)
        b = random_imaginary(rng)
        c = random_imaginary(rng)

        cpa = cross_product_associator(a, b, c)
        assoc = associator(a, b, c)
        correction = a * (-b.dot(c)) + c * a.dot(b)
        expected = assoc + correction
        diff = (cpa - expected).norm()
        assert diff < TOL, (
            f"[a,b,c]_x != [a,b,c] - (b.c)a + (a.b)c: diff={diff}"
        )


# ---------------------------------------------------------------------------
# 8. Malcev identity
# ---------------------------------------------------------------------------

def test_malcev_identity():
    """Verify the Malcev identity for 10 random imaginary octonions."""
    rng = np.random.default_rng(1001)
    for _ in range(10):
        a = random_imaginary(rng)
        b = random_imaginary(rng)
        c = random_imaginary(rng)
        result = malcev_identity(a, b, c)
        assert result['error'] < TOL, (
            f"Malcev identity failed: error={result['error']}"
        )


# ---------------------------------------------------------------------------
# 9. Structure constants are antisymmetric
# ---------------------------------------------------------------------------

def test_structure_constants_antisymmetric():
    """epsilon_{ijk} = -epsilon_{jik} for all i, j, k."""
    eps = structure_constants()
    for i in range(7):
        for j in range(7):
            for k in range(7):
                assert abs(eps[i, j, k] + eps[j, i, k]) < TOL, (
                    f"Not antisymmetric in first two indices: "
                    f"eps[{i},{j},{k}]={eps[i,j,k]}, "
                    f"eps[{j},{i},{k}]={eps[j,i,k]}"
                )


# ---------------------------------------------------------------------------
# 10. Structure constants count: exactly 42 nonzero entries
# ---------------------------------------------------------------------------

def test_structure_constants_count():
    """7 Fano lines x 6 permutations = 42 nonzero entries."""
    eps = structure_constants()
    count = np.count_nonzero(eps)
    assert count == 42, f"Expected 42 nonzero entries, got {count}"


# ---------------------------------------------------------------------------
# 11. Fano correction tensor symmetries
# ---------------------------------------------------------------------------

def test_fano_correction_tensor_symmetries():
    """T_{ijkl} = -T_{jikl} and T_{ijkl} = -T_{ijlk}."""
    T = fano_correction_tensor()
    for i in range(7):
        for j in range(7):
            for k in range(7):
                for l in range(7):
                    # Antisymmetric in first two indices
                    assert abs(T[i, j, k, l] + T[j, i, k, l]) < TOL, (
                        f"T not antisymmetric in (i,j): "
                        f"T[{i},{j},{k},{l}]={T[i,j,k,l]}, "
                        f"T[{j},{i},{k},{l}]={T[j,i,k,l]}"
                    )
                    # Antisymmetric in last two indices
                    assert abs(T[i, j, k, l] + T[i, j, l, k]) < TOL, (
                        f"T not antisymmetric in (k,l): "
                        f"T[{i},{j},{k},{l}]={T[i,j,k,l]}, "
                        f"T[{i},{j},{l},{k}]={T[i,j,l,k]}"
                    )
