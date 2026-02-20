"""
Octonionic Fluid Dynamics (Chapters 11, C.5, C.13)

Implements octonionic differential operators (gradient, divergence, 7D curl)
on discretized grids, plus the 7D vorticity source term S_NA that arises
from non-associativity and vanishes on any 3D slice.

Extracted from Appendix C.5 and C.13.
"""
import numpy as np
from octonion_algebra.core import FANO_TRIPLES


def octonionic_gradient(f_grid, dx, dims=7):
    """
    Compute the octonionic gradient of a scalar field on a discretized grid.

    In 7D, the gradient is:
        grad(f) = sum_{i=1}^{7} (df/dx_i) e_i

    which is an octonion-valued (purely imaginary) field.

    Args:
        f_grid: numpy array of shape (N,)*dims -- scalar field values on a
                grid (or fewer dimensions, specified by dims).
        dx: grid spacing (scalar, assumed uniform in all directions)
        dims: number of spatial dimensions (default 7)

    Returns:
        List of dims numpy arrays, each the same shape as f_grid,
        representing the components of the gradient.
    """
    grad_components = []
    for axis in range(dims):
        df = np.gradient(f_grid, dx, axis=axis)
        grad_components.append(df)
    return grad_components


def octonionic_divergence(F_components, dx):
    """
    Compute the octonionic divergence of a vector field.

    div(F) = sum_{i=1}^{7} dF_i/dx_i

    Args:
        F_components: list of numpy arrays (same shape), the
                      components of the vector field.
        dx: grid spacing

    Returns:
        numpy array (same shape): the divergence (scalar field).
    """
    div = np.zeros_like(F_components[0])
    for i in range(len(F_components)):
        div += np.gradient(F_components[i], dx, axis=i)
    return div


def octonionic_curl_7d(F_components, dx):
    """
    Compute the 7D curl of a vector field using the octonionic cross product.

    The 7D curl is defined as:
        (curl F)_k = sum_{i,j} f_{ijk} dF_j/dx_i

    where f_{ijk} are the octonion structure constants from the Fano plane.

    This exists ONLY in 3D and 7D (corresponding to Im(H) and Im(O)).

    Args:
        F_components: list of 7 numpy arrays (same shape), the 7 components
                      of the vector field F = F_1 e_1 + ... + F_7 e_7.
        dx: grid spacing

    Returns:
        List of 7 numpy arrays: the components of curl(F).
    """
    assert len(F_components) == 7, "7D curl requires exactly 7 components"

    # Precompute all partial derivatives dF_j/dx_i
    partials = []
    for j in range(7):
        partials_j = []
        for i in range(7):
            partials_j.append(np.gradient(F_components[j], dx, axis=i))
        partials.append(partials_j)
    # partials[j][i] = dF_j / dx_i

    curl = [np.zeros_like(F_components[0]) for _ in range(7)]

    for (a, b, c) in FANO_TRIPLES:
        # Convert to 0-indexed
        ii, jj, kk = a - 1, b - 1, c - 1
        # f_{ijk} = +1 for (i,j,k) = cyclic perm of Fano triple
        curl[kk] += partials[jj][ii] - partials[ii][jj]
        curl[ii] += partials[kk][jj] - partials[jj][kk]
        curl[jj] += partials[ii][kk] - partials[kk][ii]

    return curl


def taylor_green_7d(N=8):
    """
    Create a 7D Taylor-Green-like velocity field.

    v_k(x) = sin(x_k) * cos(x_{k+1 mod 7}) for k = 0..6

    Args:
        N: number of grid points per dimension (default 8, small for 7D memory)

    Returns:
        Tuple of (v_components, dx) where:
            v_components: list of 7 numpy arrays of shape (N,)*7
            dx: grid spacing (float)
    """
    dx = 2 * np.pi / N
    coords_1d = np.linspace(0, 2 * np.pi - dx, N)
    grids = np.meshgrid(*[coords_1d for _ in range(7)], indexing='ij')

    v = []
    for k in range(7):
        v_k = np.sin(grids[k]) * np.cos(grids[(k + 1) % 7])
        v.append(v_k)

    return v, dx


def vorticity_source_na(v, dx):
    """
    Compute the non-associative vorticity source term S_NA.

    S_NA = full 7D curl minus the 3D-compatible part (Fano triple (1,2,3) only).
    This quantity is nonzero in the full 7D setting but vanishes when the
    velocity field is restricted to any 3D slice.

    Args:
        v: list of 7 numpy arrays (velocity components)
        dx: grid spacing

    Returns:
        List of 7 numpy arrays: the components of S_NA.
    """
    curl_v = octonionic_curl_7d(v, dx)

    # Recompute partials for extracting the 3D-compatible part
    partials = []
    for j in range(7):
        partials_j = []
        for i in range(7):
            partials_j.append(np.gradient(v[j], dx, axis=i))
        partials.append(partials_j)

    # 3D curl contribution: only Fano triple (1,2,3) -> 0-indexed (0,1,2)
    curl_3d_part = [np.zeros_like(v[0]) for _ in range(7)]
    ii, jj, kk = 0, 1, 2
    curl_3d_part[kk] += partials[jj][ii] - partials[ii][jj]
    curl_3d_part[ii] += partials[kk][jj] - partials[jj][kk]
    curl_3d_part[jj] += partials[ii][kk] - partials[kk][ii]

    S_NA = [curl_v[k] - curl_3d_part[k] for k in range(7)]
    return S_NA


def restrict_velocity_to_3d(N=4):
    """
    Create a 3D-restricted velocity field embedded in a full 7D grid.

    v_k = sin(x_k) * cos(x_{k+1 mod 3}) for k = 0,1,2; rest = 0.
    The field only depends on coordinates x_0, x_1, x_2 and is constant
    along x_3, ..., x_6. Uses a full (N,)*7 grid.

    When the 7D curl is applied, S_NA should vanish because only
    the (0,1,2) Fano triple contributes and the field has no variation
    along the extra dimensions.

    Args:
        N: grid points per dimension (default 4, small for 7D memory)

    Returns:
        Tuple of (v_7d_restricted, dx) where:
            v_7d_restricted: list of 7 numpy arrays of shape (N,)*7
            dx: grid spacing (float)
    """
    dx = 2 * np.pi / N
    coords = np.linspace(0, 2 * np.pi - dx, N)
    grids = np.meshgrid(*[coords for _ in range(7)], indexing='ij')

    # 3D velocity tiled across 7D grid: only depends on x_0, x_1, x_2
    v = [np.zeros_like(grids[0]) for _ in range(7)]
    for k in range(3):
        v[k] = np.sin(grids[k]) * np.cos(grids[(k + 1) % 3])

    return v, dx
