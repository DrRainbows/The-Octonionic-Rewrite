"""
Field equations from Chapters 28–33.

Implements octonionic electromagnetism (7D Maxwell), wave equations with
non-associative remainder, Poynting vector, angular momentum algebra,
7D Schwarzschild geometry, Hawking temperature, and Kaluza–Klein gauge counting.
"""

import numpy as np
from math import comb, pi

from octonion_algebra.core import (
    Octonion, cross_product_7d, FANO_TRIPLES,
    e1, e2, e3, e4, e5, e6, e7,
)
from octonion_algebra.associator import associator
from octonion_algebra.calculus import (
    structure_constants, fano_correction_tensor, jacobiator_7d, bac_cab_7d,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _curl_7d(F, dx):
    """
    Compute a discrete 7D curl of a vector field F on a 1D grid.

    F has shape (N, 7).  We use the structure constants c_{ijk}
    and finite-difference gradients along the single spatial coordinate
    to build a simplified 1-D curl:

        (curl F)_k = sum_{i,j} c_{ijk} * dF_j / dx_i

    On a 1-D grid, only the i=0 derivative survives (direction along the grid).
    So curl_k = sum_j c_{0,j,k} * dF_j/dx.
    """
    eps = structure_constants()
    N = F.shape[0]
    curl = np.zeros_like(F)
    # Central differences for dF_j/dx (direction index 0 in the 7-component space)
    dF = np.zeros_like(F)
    dF[1:-1, :] = (F[2:, :] - F[:-2, :]) / (2 * dx)
    dF[0, :] = (F[1, :] - F[0, :]) / dx
    dF[-1, :] = (F[-1, :] - F[-2, :]) / dx

    for k in range(7):
        for j in range(7):
            curl[:, k] += eps[0, j, k] * dF[:, j]
    return curl


def _laplacian_1d(F, dx):
    """Second derivative of each component along a 1-D grid."""
    N = F.shape[0]
    lap = np.zeros_like(F)
    lap[1:-1, :] = (F[2:, :] - 2 * F[1:-1, :] + F[:-2, :]) / (dx ** 2)
    lap[0, :] = lap[1, :]
    lap[-1, :] = lap[-2, :]
    return lap


# ---------------------------------------------------------------------------
# 1. Octonionic Maxwell curl  (Ch 29)
# ---------------------------------------------------------------------------

def octonionic_maxwell_curl(E, B, J, dx):
    """
    Compute the 7D curl of B and the associator current.

    Modified Ampère law:  curl_7(B) = J + dE/dt + alpha * J_assoc

    The associator current J_assoc is built from the Fano correction tensor
    contracted with E:
        J_assoc_k = sum_{i,j,l} T_{ijkl} * E_l * (dB_j / dx_i)

    On a 1-D grid the only spatial direction is i = 0.

    Parameters
    ----------
    E, B : ndarray, shape (N, 7)
    J    : ndarray, shape (N, 7)
    dx   : float, grid spacing

    Returns
    -------
    dict with 'curl_B' (N,7) and 'J_assoc' (N,7).
    """
    curl_B = _curl_7d(B, dx)
    T = fano_correction_tensor()
    N = E.shape[0]

    # dB_j / dx  (i = 0 direction)
    dB = np.zeros_like(B)
    dB[1:-1, :] = (B[2:, :] - B[:-2, :]) / (2 * dx)
    dB[0, :] = (B[1, :] - B[0, :]) / dx
    dB[-1, :] = (B[-1, :] - B[-2, :]) / dx

    J_assoc = np.zeros_like(E)
    i = 0  # only spatial direction on 1-D grid
    for k in range(7):
        for j in range(7):
            for l in range(7):
                J_assoc[:, k] += T[i, j, k, l] * E[:, l] * dB[:, j]

    return {'curl_B': curl_B, 'J_assoc': J_assoc}


# ---------------------------------------------------------------------------
# 2. Wave-equation remainder  (Ch 29)
# ---------------------------------------------------------------------------

def _curl_7d_full(F, dx):
    """
    Compute the full 7D curl of a 7-component field defined on a 7D grid.

    F has shape (N, N, N, N, N, N, N, 7) — a 7-component vector field
    on an N^7 grid.  Returns array of same shape.

    For efficiency this implementation supports a 3D sub-grid via
    _curl_sub (see wave_equation_remainder).
    """
    raise NotImplementedError("Full 7D grid curl not needed; see _curl_sub.")


def _deriv(F, axis, dx):
    """Central-difference derivative along the given axis."""
    d = np.zeros_like(F)
    slc_p = [slice(None)] * F.ndim
    slc_m = [slice(None)] * F.ndim
    slc_c = [slice(None)] * F.ndim

    slc_p[axis] = slice(2, None)
    slc_m[axis] = slice(None, -2)
    slc_c[axis] = slice(1, -1)
    d[tuple(slc_c)] = (F[tuple(slc_p)] - F[tuple(slc_m)]) / (2 * dx)

    # Forward/backward at boundaries
    slc_0 = [slice(None)] * F.ndim
    slc_1 = [slice(None)] * F.ndim
    slc_0[axis] = 0
    slc_1[axis] = 1
    d[tuple(slc_0)] = (F[tuple(slc_1)] - F[tuple(slc_0)]) / dx

    slc_e = [slice(None)] * F.ndim
    slc_e1 = [slice(None)] * F.ndim
    slc_e[axis] = -1
    slc_e1[axis] = -2
    d[tuple(slc_e)] = (F[tuple(slc_e)] - F[tuple(slc_e1)]) / dx

    return d


def wave_equation_remainder(A, dx):
    """
    Non-associative remainder R[A] from the double-curl identity.

    In 3D:  curl(curl A) = -Lap A + grad(div A)         (R = 0).
    In 7D:  curl(curl A) = -Lap A + grad(div A) + R[A]  (R ≠ 0).

    We compute R = curl(curl A) + Lap A - grad(div A) directly.

    A is defined on a *d*-dimensional grid where *d* is the number of
    spatial axes (= number of leading dimensions).  The last axis has
    size 7 and stores the vector components.

    For example, ``A.shape = (N, N, N, 7)`` for a field living on a 3D
    grid with 7 vector components, or ``A.shape = (N, 7)`` for a 1D grid.

    Parameters
    ----------
    A : ndarray, shape (*grid, 7)
    dx : float

    Returns
    -------
    R : ndarray, same shape as A
    """
    eps = structure_constants()
    shape = A.shape
    ndim_spatial = len(shape) - 1  # number of spatial grid dimensions
    comp_axis = len(shape) - 1     # axis index for the 7 components

    # Convenience: extract component slices
    def comp(F, c):
        """Return the c-th component of field F (last axis)."""
        return F[..., c]

    def set_comp(F, c, val):
        F[..., c] = val

    # Step 1: compute curl(A)
    curl_A = np.zeros_like(A)
    for k in range(7):
        for i in range(min(ndim_spatial, 7)):
            for j in range(7):
                if eps[i, j, k] == 0:
                    continue
                dAj_dxi = _deriv(comp(A, j), i, dx)
                curl_A[..., k] += eps[i, j, k] * dAj_dxi

    # Step 2: compute curl(curl(A))
    curl_curl_A = np.zeros_like(A)
    for k in range(7):
        for i in range(min(ndim_spatial, 7)):
            for j in range(7):
                if eps[i, j, k] == 0:
                    continue
                dcurl_j_dxi = _deriv(comp(curl_A, j), i, dx)
                curl_curl_A[..., k] += eps[i, j, k] * dcurl_j_dxi

    # Step 3: compute Laplacian(A)
    lap_A = np.zeros_like(A)
    for c in range(7):
        Ac = comp(A, c)
        for i in range(min(ndim_spatial, 7)):
            d2 = _deriv(_deriv(Ac, i, dx), i, dx)
            lap_A[..., c] += d2

    # Step 4: compute grad(div A)
    # div A = sum_i dA_i / dx_i  (only up to ndim_spatial components)
    div_A = np.zeros(shape[:-1])
    for i in range(min(ndim_spatial, 7)):
        div_A += _deriv(comp(A, i), i, dx)

    grad_div_A = np.zeros_like(A)
    for k in range(min(ndim_spatial, 7)):
        grad_div_A[..., k] = _deriv(div_A, k, dx)

    # R = curl(curl A) + Lap A - grad(div A)
    R = curl_curl_A + lap_A - grad_div_A
    return R


# ---------------------------------------------------------------------------
# 3. 7D Poynting vector  (Ch 29)
# ---------------------------------------------------------------------------

def poynting_7d(E, B):
    """
    Compute the 7D Poynting vector S = E x_7 B.

    Parameters
    ----------
    E, B : length-7 array-like  (imaginary-octonion components)

    Returns
    -------
    ndarray of shape (7,)
    """
    E_arr = np.asarray(E, dtype=float)
    B_arr = np.asarray(B, dtype=float)
    # Wrap into purely-imaginary Octonions
    E_oct = Octonion(np.concatenate(([0.0], E_arr)))
    B_oct = Octonion(np.concatenate(([0.0], B_arr)))
    S_oct = cross_product_7d(E_oct, B_oct)
    return S_oct.imag_vector()


# ---------------------------------------------------------------------------
# 4. Poynting transverse drift  (Ch 29, worked example)
# ---------------------------------------------------------------------------

def poynting_transverse_drift(alpha_angle):
    """
    Worked example from Ch 29.10.

    E = E0 (cos α e3 + sin α e2)
    B = E0 (cos α e5 + sin α e4)

    Two polarisation planes that both couple to e7 via Fano triples
    (3,4,7) and (2,5,7).  The cross-terms add constructively, giving
    a transverse Poynting drift along e7 proportional to sin(2α).

    Returns dict with 'longitudinal' (e6 coeff) and 'transverse' (e7 coeff).
    E0 is set to 1 without loss of generality.
    """
    ca = np.cos(alpha_angle)
    sa = np.sin(alpha_angle)

    # 7-component vectors (indices 0–6 → e1–e7)
    E_vec = np.zeros(7)
    E_vec[2] = ca   # e3
    E_vec[1] = sa   # e2

    B_vec = np.zeros(7)
    B_vec[4] = ca   # e5
    B_vec[3] = sa   # e4

    S = poynting_7d(E_vec, B_vec)

    return {
        'longitudinal': S[5],   # e6 component
        'transverse': S[6],     # e7 component
    }


# ---------------------------------------------------------------------------
# 5. Angular momentum commutator  (Ch 30)
# ---------------------------------------------------------------------------

def angular_momentum_commutator(a_idx, b_idx):
    """
    Compute the structure constants c_{ab,c} for the 7D angular momentum
    algebra:  [L_a, L_b] = i hbar sum_c c_{abc} L_c.

    Parameters
    ----------
    a_idx, b_idx : int in 0..6  (0-indexed: 0 → e1 direction, etc.)

    Returns
    -------
    ndarray of shape (7,): c_{ab,c} for c = 0..6.
    """
    eps = structure_constants()
    return eps[a_idx, b_idx, :].copy()


# ---------------------------------------------------------------------------
# 6. Casimir eigenvalue  (Ch 30)
# ---------------------------------------------------------------------------

def angular_momentum_casimir_eigenvalue(ell, d=7):
    """
    SO(d) Casimir eigenvalue: ell * (ell + d - 2).
    """
    return ell * (ell + d - 2)


# ---------------------------------------------------------------------------
# 7. Angular momentum degeneracy  (Ch 30)
# ---------------------------------------------------------------------------

def angular_momentum_degeneracy(ell, d=7):
    """
    Degeneracy of the SO(d) spherical harmonics at angular-momentum
    quantum number ell:

        d_ell = (2*ell + d - 2) * C(ell + d - 3, ell) / (d - 2)

    where C is the binomial coefficient.  Returns an integer.
    """
    if ell == 0:
        return 1
    numerator = (2 * ell + d - 2) * comb(ell + d - 3, ell)
    result = numerator // (d - 2)
    return int(result)


# ---------------------------------------------------------------------------
# 8. 7D Schwarzschild metric  (Ch 31)
# ---------------------------------------------------------------------------

def schwarzschild_7d(r, r_s):
    """
    7D Schwarzschild metric function f(r) = 1 - (r_s / r)^5.

    In D = d + 1 = 8 spacetime dimensions (d = 7 spatial), the exponent
    is d - 2 = 5.
    """
    return 1.0 - (r_s / r) ** 5


# ---------------------------------------------------------------------------
# 9. Hawking temperature  (Ch 31)
# ---------------------------------------------------------------------------

def hawking_temperature_7d(r_s):
    """
    Hawking temperature in 7+1 dimensions (natural units hbar = 1):

        T_H = 5 / (4 pi r_s)
    """
    return 5.0 / (4.0 * pi * r_s)


# ---------------------------------------------------------------------------
# 10. Kaluza–Klein gauge counting  (Ch 33)
# ---------------------------------------------------------------------------

def kaluza_klein_gauge_count(d_internal):
    """
    For a Kaluza–Klein reduction on an internal manifold of dimension
    d_internal, return the number of gauge fields and the maximum gauge
    group dimension.

    gauge_fields = d_internal * 4   (one per spacetime direction)
    max_gauge_dim = d_internal * (d_internal + 1) / 2

    Returns
    -------
    dict with 'gauge_count' and 'max_gauge_dim'.
    """
    gauge_count = d_internal * 4
    max_gauge_dim = d_internal * (d_internal + 1) // 2
    return {
        'gauge_count': gauge_count,
        'max_gauge_dim': max_gauge_dim,
    }
