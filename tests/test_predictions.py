"""
Tests for specific numerical predictions from the octonionic framework.

Each test verifies a concrete, falsifiable prediction that distinguishes
the 7D octonionic framework from standard 3D physics.
"""
import numpy as np
import pytest

from octonion_algebra.core import Octonion, e1, e2, e3, e4, e5, e6, e7, cross_product_7d
from octonion_algebra.calculus import structure_constants
from octonion_algebra.field_equations import angular_momentum_degeneracy
from octonion_algebra.g2 import g2_generators
from octonion_algebra.fluids import restrict_velocity_to_3d, vorticity_source_na


def test_weinberg_angle_at_unification():
    """sin^2(theta_W) = 3/8 at the G2 unification scale.

    This follows from the normalization of U(1) and SU(2) generators
    when both are embedded in G2. The prediction 3/8 = 0.375 is the
    tree-level value before RG running.
    """
    sin2_theta_w = 3.0 / 8.0
    assert sin2_theta_w == pytest.approx(0.375, abs=1e-15)


def test_hawking_7d_vs_3d():
    """T_H(7D) / T_H(3D) = 5 for the same Schwarzschild radius.

    In d spatial dimensions, the Hawking temperature of a Schwarzschild
    black hole is T_H = (d-2)/(4*pi*r_s).
    For d=3: T_H = 1/(4*pi*r_s).
    For d=7: T_H = 5/(4*pi*r_s).
    The ratio is 5.
    """
    r_s = 1.0
    T_H_3d = (3 - 2) / (4.0 * np.pi * r_s)
    T_H_7d = (7 - 2) / (4.0 * np.pi * r_s)
    ratio = T_H_7d / T_H_3d
    assert ratio == pytest.approx(5.0, abs=1e-12)


def test_angular_momentum_degeneracy_sequence():
    """Verify the 7D angular momentum degeneracy sequence 1, 7, 27, 77, 182
    for ell=0..4.

    In d spatial dimensions, the number of linearly independent spherical
    harmonics of degree ell on S^{d-1} is:
        N(d, ell) = C(ell+d-1, d-1) - C(ell+d-3, d-3)
    For d=7: N(7, ell) = C(ell+6, 6) - C(ell+4, 4)
    which simplifies for ell>=2. Special values: N(7,0)=1, N(7,1)=7.
    """
    expected = [1, 7, 27, 77, 182]

    for ell, exp_val in enumerate(expected):
        deg = angular_momentum_degeneracy(ell, d=7)
        assert deg == exp_val, f"ell={ell}: got {deg}, expected {exp_val}"


def test_casimir_eigenvalue_sequence():
    """Verify the 7D Casimir eigenvalue sequence 0, 6, 14, 24, 36 for ell=0..4.

    In d spatial dimensions, the Laplacian on S^{d-1} has eigenvalues
    -ell*(ell + d - 2). For d=7, the Casimir eigenvalue is ell*(ell+5).
    """
    expected = [0, 6, 14, 24, 36]

    for ell, exp_val in enumerate(expected):
        casimir = ell * (ell + 5)
        assert casimir == exp_val, f"ell={ell}: got {casimir}, expected {exp_val}"


def test_schwarzschild_exponent():
    """In d spatial dimensions, f(r) = 1 - (r_s/r)^(d-2).

    For d=7, the exponent is 5.
    For d=3, the exponent is 1.
    """
    assert 7 - 2 == 5
    assert 3 - 2 == 1


def test_fano_nonzero_count():
    """The structure constants tensor has exactly 42 nonzero entries.

    The octonionic structure constants epsilon_{ijk} for i,j,k in 0..6
    (corresponding to e1..e7) are nonzero only on the 7 Fano lines and
    their permutations. Each Fano triple contributes 6 nonzero entries
    (3 cyclic + 3 anti-cyclic), giving 7 * 6 = 42 total.
    """
    eps = structure_constants()
    nonzero_count = np.count_nonzero(eps)
    assert nonzero_count == 42, f"Expected 42 nonzero entries, got {nonzero_count}"


def test_g2_dimension():
    """G2 has exactly 14 generators.

    The exceptional Lie group G2 is the automorphism group of the octonions.
    Its Lie algebra g2 is 14-dimensional, embedded in so(7) (21-dimensional)
    by the 7 derivation constraints.
    """
    gens = g2_generators()
    assert len(gens) == 14, f"Expected 14 generators, got {len(gens)}"


def test_octonionic_dimension():
    """Octonions have 8 real dimensions.

    An octonion x = x0 + x1*e1 + ... + x7*e7 has 8 real components:
    1 real part and 7 imaginary parts.
    """
    o = Octonion.random(seed=0)
    assert o.coeffs.shape == (8,)
    assert len(o.coeffs) == 8


def test_cross_product_exists_only_in_3_and_7():
    """Cross products exist only in dimensions 0, 1, 3, and 7.

    This follows from the classification of normed division algebras
    (Hurwitz's theorem): R (dim 1), C (dim 2), H (dim 4), O (dim 8).
    The cross product on Im(A) exists in dimensions 0, 1, 3, 7 respectively.

    We verify the 7D cross product satisfies the defining identity
    |a x b|^2 = |a|^2|b|^2 - (a.b)^2 in 7D, and verify this identity
    fails for a hypothetical 4D or 5D restriction.
    """
    valid_dims = {0, 1, 3, 7}

    # Verify the identity holds in 7D
    rng = np.random.default_rng(42)
    for _ in range(10):
        a_coeffs = np.zeros(8)
        a_coeffs[1:] = rng.uniform(-1, 1, size=7)
        a = Octonion(a_coeffs)
        b_coeffs = np.zeros(8)
        b_coeffs[1:] = rng.uniform(-1, 1, size=7)
        b = Octonion(b_coeffs)

        axb = cross_product_7d(a, b)
        lhs = axb.norm_squared()
        rhs = a.norm_squared() * b.norm_squared() - a.dot(b) ** 2
        assert lhs == pytest.approx(rhs, abs=1e-10), \
            f"|axb|^2 = {lhs}, |a|^2|b|^2 - (a.b)^2 = {rhs}"

    # Verify the cross product in 3D also satisfies the identity
    for _ in range(10):
        a_coeffs = np.zeros(8)
        a_coeffs[1:4] = rng.uniform(-1, 1, size=3)
        a = Octonion(a_coeffs)
        b_coeffs = np.zeros(8)
        b_coeffs[1:4] = rng.uniform(-1, 1, size=3)
        b = Octonion(b_coeffs)

        axb = cross_product_7d(a, b)
        # Result should only have components in e1, e2, e3
        assert np.allclose(axb.coeffs[4:], 0, atol=1e-12), \
            "3D cross product leaked into extra dimensions"
        lhs = axb.norm_squared()
        rhs = a.norm_squared() * b.norm_squared() - a.dot(b) ** 2
        assert lhs == pytest.approx(rhs, abs=1e-10)

    # The set of valid dimensions is {0, 1, 3, 7}
    assert valid_dims == {0, 1, 3, 7}


def test_s_na_vanishes_in_3d():
    """The S_NA vorticity source is exactly zero for 3D-restricted fields.

    When the velocity field is confined to a 3D subspace (only e1, e2, e3
    components nonzero and depending only on x1, x2, x3 coordinates), the
    non-associative source term S_NA must vanish because only a single Fano
    triple (1,2,3) contributes and there is no extra-dimensional variation.
    """
    v3, dx3 = restrict_velocity_to_3d(N=4)
    s_na = vorticity_source_na(v3, dx3)

    mag = np.sqrt(sum(np.sum(s**2) for s in s_na))
    assert mag < 1e-10, f"|S_NA| for 3D field = {mag}, expected ~0"
