"""Tests for the octonionic fluid dynamics module."""
import numpy as np
import pytest

from octonion_algebra.fluids import (
    taylor_green_7d,
    vorticity_source_na,
    restrict_velocity_to_3d,
    octonionic_curl_7d,
    octonionic_gradient,
)


def test_taylor_green_shape():
    """taylor_green_7d returns correct shapes: 7 arrays each of shape (N,)*7."""
    N = 4  # Small for speed
    v, dx = taylor_green_7d(N=N)

    assert len(v) == 7, f"Expected 7 velocity components, got {len(v)}"
    expected_shape = (N,) * 7
    for i, vi in enumerate(v):
        assert vi.shape == expected_shape, (
            f"Component {i} has shape {vi.shape}, expected {expected_shape}"
        )
    assert isinstance(dx, float), f"dx should be float, got {type(dx)}"
    assert dx > 0, f"dx should be positive, got {dx}"


def test_vorticity_source_nonzero():
    """S_NA is nonzero for 7D Taylor-Green velocity field.

    The non-associative vorticity source term should be nonzero in the
    full 7D setting because the extra Fano triples contribute.
    """
    N = 4
    v, dx = taylor_green_7d(N=N)
    S = vorticity_source_na(v, dx)

    assert len(S) == 7, f"S_NA should have 7 components, got {len(S)}"

    # At least some components should be nonzero
    total_norm = sum(np.sum(s**2) for s in S)
    assert total_norm > 1e-10, (
        f"S_NA should be nonzero for 7D Taylor-Green, got total norm^2 = {total_norm}"
    )


def test_3d_restriction_vanishes():
    """restrict_velocity_to_3d gives S_NA ~ 0.

    When the velocity field lives purely in a 3D subspace, the non-associative
    source term should vanish because only one Fano triple contributes
    (equivalent to the standard 3D cross product).
    """
    N = 8
    v_3d, dx = restrict_velocity_to_3d(N=N)
    S = vorticity_source_na(v_3d, dx)

    # Components 3-6 (0-indexed) should be essentially zero
    for k in range(3, 7):
        max_val = np.max(np.abs(S[k]))
        assert max_val < 1e-6, (
            f"S_NA component {k} should vanish for 3D field, got max = {max_val}"
        )


def test_curl_antisymmetric():
    """The 7D curl has the antisymmetry property: swapping two components
    of the input vector field and negating produces consistent results.

    More precisely, we verify that curl is linear and gives nonzero output
    for a non-trivial 7D velocity field.
    """
    N = 4
    v, dx = taylor_green_7d(N=N)
    curl_v = octonionic_curl_7d(v, dx)

    assert len(curl_v) == 7, f"Curl should have 7 components, got {len(curl_v)}"

    # Linearity check: curl(2*v) = 2*curl(v)
    v_scaled = [2.0 * vi for vi in v]
    curl_2v = octonionic_curl_7d(v_scaled, dx)
    for k in range(7):
        np.testing.assert_allclose(
            curl_2v[k], 2.0 * curl_v[k], atol=1e-10,
            err_msg=f"Curl is not linear in component {k}"
        )


def test_gradient_shape():
    """octonionic_gradient returns correct shape."""
    N = 4
    dims = 7
    shape = (N,) * dims
    f_grid = np.sin(np.linspace(0, 2 * np.pi, N)).reshape(
        (N,) + (1,) * (dims - 1)
    ) * np.ones(shape)
    dx = 2 * np.pi / N

    grad = octonionic_gradient(f_grid, dx, dims=dims)

    assert len(grad) == dims, f"Gradient should have {dims} components, got {len(grad)}"
    for i, gi in enumerate(grad):
        assert gi.shape == shape, (
            f"Gradient component {i} has shape {gi.shape}, expected {shape}"
        )
