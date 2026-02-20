"""
Tests for octonion_algebra.field_equations (Phase 3C.3 / 3C.4).

Covers: Poynting vector, transverse drift, angular momentum,
Casimir eigenvalues, degeneracy, Schwarzschild 7D, Hawking temperature,
wave-equation remainder, and Kaluza–Klein gauge counting.
"""

import numpy as np
import pytest
from math import pi, sin

from octonion_algebra.field_equations import (
    poynting_7d,
    poynting_transverse_drift,
    angular_momentum_commutator,
    angular_momentum_casimir_eigenvalue,
    angular_momentum_degeneracy,
    schwarzschild_7d,
    hawking_temperature_7d,
    wave_equation_remainder,
    kaluza_klein_gauge_count,
)
from octonion_algebra.calculus import structure_constants


# -----------------------------------------------------------------------
# Poynting transverse drift
# -----------------------------------------------------------------------

def test_poynting_transverse_drift_zero_at_alpha_0():
    """At alpha=0, only the e2-e3 plane is active -> no transverse drift."""
    result = poynting_transverse_drift(0.0)
    assert abs(result['transverse']) < 1e-12


def test_poynting_transverse_drift_max_at_pi_4():
    """At alpha=pi/4, sin(2*alpha) = 1 -> maximum transverse drift."""
    result = poynting_transverse_drift(pi / 4)
    assert abs(result['transverse'] - 1.0) < 1e-12


def test_poynting_transverse_drift_sin_2alpha():
    """For 10 random alpha values, transverse component equals sin(2*alpha)."""
    rng = np.random.default_rng(42)
    for _ in range(10):
        alpha = rng.uniform(0, 2 * pi)
        result = poynting_transverse_drift(alpha)
        expected = sin(2 * alpha)
        assert abs(result['transverse'] - expected) < 1e-12, (
            f"alpha={alpha}: got {result['transverse']}, expected {expected}"
        )


# -----------------------------------------------------------------------
# Angular momentum structure constants
# -----------------------------------------------------------------------

def test_angular_momentum_structure_constants():
    """
    For all pairs (a, b), verify that the commutator coefficients
    c_{abc} match the structure constant tensor.
    """
    eps = structure_constants()
    for a in range(7):
        for b in range(7):
            coeffs = angular_momentum_commutator(a, b)
            for c in range(7):
                assert abs(coeffs[c] - eps[a, b, c]) < 1e-14, (
                    f"Mismatch at ({a},{b},{c}): "
                    f"got {coeffs[c]}, expected {eps[a, b, c]}"
                )


# -----------------------------------------------------------------------
# Casimir eigenvalue
# -----------------------------------------------------------------------

def test_casimir_eigenvalue_3d():
    """In d=3 (SO(3)), Casimir eigenvalue is ell*(ell+1)."""
    for ell in range(6):
        assert angular_momentum_casimir_eigenvalue(ell, d=3) == ell * (ell + 1)


def test_casimir_eigenvalue_7d():
    """In d=7 (SO(7)), Casimir eigenvalue is ell*(ell+5)."""
    for ell in range(6):
        assert angular_momentum_casimir_eigenvalue(ell, d=7) == ell * (ell + 5)


# -----------------------------------------------------------------------
# Degeneracy
# -----------------------------------------------------------------------

def test_degeneracy_3d():
    """In d=3, degeneracy is 2*ell + 1."""
    for ell in range(10):
        assert angular_momentum_degeneracy(ell, d=3) == 2 * ell + 1


def test_degeneracy_7d():
    """In d=7, degeneracy for ell=0..4 is 1, 7, 27, 77, 182."""
    expected = [1, 7, 27, 77, 182]
    for ell, exp in enumerate(expected):
        result = angular_momentum_degeneracy(ell, d=7)
        assert result == exp, (
            f"ell={ell}: got {result}, expected {exp}"
        )


# -----------------------------------------------------------------------
# Schwarzschild 7D
# -----------------------------------------------------------------------

def test_schwarzschild_horizon():
    """f(r_s) = 0 at the horizon."""
    r_s = 2.0
    assert abs(schwarzschild_7d(r_s, r_s)) < 1e-14


def test_schwarzschild_far_field():
    """f(r) -> 1 as r -> infinity."""
    r_s = 1.0
    assert abs(schwarzschild_7d(1e6, r_s) - 1.0) < 1e-14


# -----------------------------------------------------------------------
# Hawking temperature
# -----------------------------------------------------------------------

def test_hawking_temperature():
    """T_H = 5 / (4 pi r_s)."""
    r_s = 3.0
    expected = 5.0 / (4.0 * pi * r_s)
    assert abs(hawking_temperature_7d(r_s) - expected) < 1e-14


# -----------------------------------------------------------------------
# Wave-equation remainder
# -----------------------------------------------------------------------

def test_wave_equation_remainder_3d_zero():
    """
    For a field on a 3D grid with only components 0–2 active, the
    remainder should be zero because the Jacobi identity holds in 3D.
    """
    N = 20
    dx = 0.3
    # Build a (N, N, N, 7) field with components 0–2 only
    grid = np.linspace(0, (N - 1) * dx, N)
    X, Y, Z = np.meshgrid(grid, grid, grid, indexing='ij')
    A = np.zeros((N, N, N, 7))
    A[..., 0] = np.sin(X) * np.cos(Y)
    A[..., 1] = np.cos(Y) * np.sin(Z)
    A[..., 2] = np.sin(X + Z)
    R = wave_equation_remainder(A, dx)
    # Interior points only (avoid boundary artefacts)
    interior = R[3:-3, 3:-3, 3:-3, :]
    assert np.max(np.abs(interior)) < 0.05, (
        f"3D remainder max = {np.max(np.abs(interior)):.6g}, expected ~0"
    )


def test_fano_correction_tensor_nonzero_and_3d_antisymmetry():
    """
    The Fano correction tensor T_{ijkl} is nonzero overall, but when restricted
    to derivative indices i,m in a 3D subspace {0,1,2}, it is antisymmetric
    in (i,m): T[k,i,m,n] = -T[k,m,i,n].

    This means the double-curl remainder R = curl(curl A) + Lap A - grad(div A)
    vanishes for 7-component fields on a 3D grid, because the symmetric
    Hessian contracts to zero with the antisymmetric tensor. The genuine
    non-associative remainder only appears on a full 7D spatial grid.

    This test verifies:
    (a) T is not identically zero (it has many nonzero entries).
    (b) T is antisymmetric in (2nd, 3rd) indices when restricted to {0,1,2},
        explaining why the 3D-grid remainder is zero.
    (c) The numerical double-curl identity holds on a 3D grid.
    """
    from octonion_algebra.calculus import fano_correction_tensor

    T = fano_correction_tensor()

    # (a) T should have nonzero entries
    assert np.max(np.abs(T)) > 0.5, (
        f"Fano correction tensor should be nonzero, max = {np.max(np.abs(T))}"
    )
    nonzero_count = np.count_nonzero(np.abs(T) > 1e-12)
    assert nonzero_count > 100, (
        f"Expected many nonzero T entries, got {nonzero_count}"
    )

    # (b) Antisymmetry in (i,m) for i,m in {0,1,2}:
    #     T[k,i,m,n] + T[k,m,i,n] = 0 for all k, n and i,m in {0,1,2}
    max_sym = 0.0
    for k in range(7):
        for i in range(3):
            for m in range(3):
                for n in range(7):
                    sym_part = abs(T[k, i, m, n] + T[k, m, i, n])
                    if sym_part > max_sym:
                        max_sym = sym_part
    assert max_sym < 1e-12, (
        f"T should be antisymmetric in (i,m) for i,m in {{0,1,2}}, "
        f"max |T[k,i,m,n] + T[k,m,i,n]| = {max_sym}"
    )

    # (c) Verify on the actual numerical computation: the remainder is zero
    #     for a 7-component field on a 3D grid.
    N = 16
    dx = 0.3
    grid = np.linspace(0, (N - 1) * dx, N)
    X, Y, Z = np.meshgrid(grid, grid, grid, indexing='ij')
    A = np.zeros((N, N, N, 7))
    for k in range(7):
        A[..., k] = np.sin((k + 1) * X) * np.cos((k + 2) * Y) * np.sin((k + 3) * Z)
    R = wave_equation_remainder(A, dx)
    interior = R[3:-3, 3:-3, 3:-3, :]
    assert np.max(np.abs(interior)) < 0.05, (
        f"3D-grid remainder should be ~0 by antisymmetry, "
        f"max = {np.max(np.abs(interior)):.6g}"
    )


# -----------------------------------------------------------------------
# Poynting 7D basis vectors
# -----------------------------------------------------------------------

def test_poynting_7d_basis_vectors():
    """E = e2, B = e3 -> S = e1 (from Fano triple (1,2,3))."""
    # 7-component vectors (index 0 = e1, index 1 = e2, etc.)
    E = np.zeros(7)
    E[1] = 1.0  # e2
    B = np.zeros(7)
    B[2] = 1.0  # e3
    S = poynting_7d(E, B)
    # Should be +e1 (index 0)
    assert abs(S[0] - 1.0) < 1e-12
    # All other components should be zero
    for k in range(1, 7):
        assert abs(S[k]) < 1e-12, f"S[{k}] = {S[k]}, expected 0"


# -----------------------------------------------------------------------
# Kaluza–Klein gauge counting
# -----------------------------------------------------------------------

def test_kaluza_klein_gauge_count():
    """For d_internal=3: gauge_count=12, max_gauge_dim=6."""
    result = kaluza_klein_gauge_count(3)
    assert result['gauge_count'] == 12
    assert result['max_gauge_dim'] == 6
