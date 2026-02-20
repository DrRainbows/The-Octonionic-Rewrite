"""Tests for 3D recovery: verifying that octonionic structures reduce
correctly to familiar 3D/quaternionic results."""
import numpy as np
import pytest

from octonion_algebra.core import (
    Octonion,
    cross_product_7d,
    cross_product_7d_vectors,
    e0, e1, e2, e3, e4, e5, e6, e7,
)
from octonion_algebra.associator import associator
from octonion_algebra.finance import moufang_check
from octonion_algebra.fluids import (
    restrict_velocity_to_3d,
    vorticity_source_na,
)


def test_cross_product_recovers_3d():
    """7D cross product restricted to e1,e2,e3 subspace gives standard 3D cross product.

    The standard 3D cross product corresponds to the Fano triple (1,2,3):
      e1 x e2 = e3, e2 x e3 = e1, e3 x e1 = e2
    """
    # e1 x e2 = e3
    result = cross_product_7d(e1, e2)
    np.testing.assert_allclose(result.coeffs, e3.coeffs, atol=1e-10,
                               err_msg="e1 x e2 should be e3")

    # e2 x e3 = e1
    result = cross_product_7d(e2, e3)
    np.testing.assert_allclose(result.coeffs, e1.coeffs, atol=1e-10,
                               err_msg="e2 x e3 should be e1")

    # e3 x e1 = e2
    result = cross_product_7d(e3, e1)
    np.testing.assert_allclose(result.coeffs, e2.coeffs, atol=1e-10,
                               err_msg="e3 x e1 should be e2")

    # Antisymmetry: e2 x e1 = -e3
    result = cross_product_7d(e2, e1)
    np.testing.assert_allclose(result.coeffs, (-e3).coeffs, atol=1e-10,
                               err_msg="e2 x e1 should be -e3")

    # Also test with the vector version
    u = np.array([1.0, 0, 0, 0, 0, 0, 0])  # e1
    v = np.array([0, 1.0, 0, 0, 0, 0, 0])  # e2
    w = cross_product_7d_vectors(u, v)
    expected = np.array([0, 0, 1.0, 0, 0, 0, 0])  # e3
    np.testing.assert_allclose(w, expected, atol=1e-10,
                               err_msg="Vector cross product e1 x e2 should be e3")


def test_associator_vanishes_quaternionic():
    """[a,b,c] = 0 when a,b,c all in span{1, e1, e2, e3}.

    The quaternionic subalgebra {1, e1, e2, e3} is associative, so the
    associator must vanish for any triple within it.
    """
    rng = np.random.default_rng(42)

    for _ in range(10):
        # Random quaternionic elements: span{1, e1, e2, e3}
        c_a = np.zeros(8)
        c_a[:4] = rng.uniform(-1, 1, size=4)
        a = Octonion(c_a)

        c_b = np.zeros(8)
        c_b[:4] = rng.uniform(-1, 1, size=4)
        b = Octonion(c_b)

        c_c = np.zeros(8)
        c_c[:4] = rng.uniform(-1, 1, size=4)
        c = Octonion(c_c)

        assoc = associator(a, b, c)
        assert assoc.norm() < 1e-10, (
            f"Associator should vanish in quaternionic subalgebra, "
            f"got norm = {assoc.norm()}"
        )


def test_vorticity_source_vanishes_3d():
    """S_NA = 0 for purely 3D velocity fields.

    When the velocity field is restricted to a 3D subspace, the
    non-associative source term vanishes because only one Fano triple
    contributes (the standard 3D cross product).
    """
    N = 4
    v_3d, dx = restrict_velocity_to_3d(N=N)
    S = vorticity_source_na(v_3d, dx)

    total_norm_sq = sum(np.sum(s**2) for s in S)
    # The 3D part (components 0,1,2) comes from the single Fano triple (1,2,3)
    # and is subtracted out in S_NA. Components 3-6 are zero because the
    # velocity has no components there.
    assert total_norm_sq < 1e-6, (
        f"S_NA should vanish for 3D velocity field, "
        f"got total |S_NA|^2 = {total_norm_sq}"
    )


def test_norm_multiplicative_quaternionic():
    """|ab| = |a||b| holds in quaternionic subspace (it holds everywhere for octonions).

    The octonions are a normed division algebra: |ab| = |a||b| for all a, b.
    We verify this specifically in the quaternionic subspace.
    """
    rng = np.random.default_rng(77)

    for _ in range(10):
        c_a = np.zeros(8)
        c_a[:4] = rng.uniform(-2, 2, size=4)
        a = Octonion(c_a)

        c_b = np.zeros(8)
        c_b[:4] = rng.uniform(-2, 2, size=4)
        b = Octonion(c_b)

        ab = a * b
        np.testing.assert_allclose(
            ab.norm(), a.norm() * b.norm(), atol=1e-10,
            err_msg="|ab| should equal |a||b| for quaternionic elements"
        )

    # Also verify for general octonions (the property holds everywhere)
    for seed in range(5):
        a = Octonion.random(seed=seed)
        b = Octonion.random(seed=seed + 100)
        ab = a * b
        np.testing.assert_allclose(
            ab.norm(), a.norm() * b.norm(), atol=1e-10,
            err_msg="|ab| should equal |a||b| for all octonions"
        )


def test_moufang_in_quaternionic():
    """Moufang identities hold in the quaternionic subspace.

    The Moufang identities hold for all octonions (since O is alternative),
    but we verify specifically within the quaternionic subalgebra.
    """
    rng = np.random.default_rng(88)

    for _ in range(5):
        c_a = np.zeros(8)
        c_a[:4] = rng.uniform(-1, 1, size=4)
        a = Octonion(c_a)

        c_b = np.zeros(8)
        c_b[:4] = rng.uniform(-1, 1, size=4)
        b = Octonion(c_b)

        c_c = np.zeros(8)
        c_c[:4] = rng.uniform(-1, 1, size=4)
        c = Octonion(c_c)

        result = moufang_check(a, b, c)
        assert result['moufang_1'], f"Moufang 1 failed in quaternionic subspace"
        assert result['moufang_2'], f"Moufang 2 failed in quaternionic subspace"
        assert result['moufang_3'], f"Moufang 3 failed in quaternionic subspace"
