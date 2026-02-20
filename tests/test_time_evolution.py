"""
Tests for octonion_algebra.time_evolution.

Verifies well-posedness and causality of octonionic Klein-Gordon evolution:
- Shape consistency
- Energy positivity and conservation
- Signal speed = 1 (causality)
- Quaternionic slice consistency
- Associator perturbation bound (cubic)
- Zero field stability
- Full well-posedness summary
"""

import numpy as np
import pytest

from octonion_algebra.time_evolution import (
    octonionic_klein_gordon_rhs,
    evolve_klein_gordon,
    compute_energy,
    verify_energy_conservation,
    signal_speed_test,
    quaternionic_slice_consistency,
    associator_perturbation_bound,
    well_posedness_summary,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_gaussian_field(N=50, dx=0.2, amplitude=1.0, seed=42):
    """Create a Gaussian initial field for testing."""
    x = np.arange(N) * dx
    center = N // 2 * dx
    sigma = 3.0 * dx
    phi0 = np.zeros((N, 8))
    phi0[:, 0] = amplitude * np.exp(-((x - center) ** 2) / (2.0 * sigma ** 2))
    pi0 = np.zeros((N, 8))
    return phi0, pi0, dx


def _make_sinusoidal_field(N=50, dx=0.2):
    """Create a sinusoidal initial field compatible with Dirichlet BC."""
    x = np.arange(N) * dx
    L = (N - 1) * dx
    phi0 = np.zeros((N, 8))
    # Use sin(n*pi*x/L) which vanishes at x=0 and x=L (Dirichlet eigenmodes)
    phi0[:, 0] = np.sin(np.pi * x / L)
    phi0[:, 1] = 0.5 * np.sin(2.0 * np.pi * x / L)
    pi0 = np.zeros((N, 8))
    return phi0, pi0, dx


# ---------------------------------------------------------------------------
# test_klein_gordon_rhs_shape
# ---------------------------------------------------------------------------

def test_klein_gordon_rhs_shape():
    """Output shapes of octonionic_klein_gordon_rhs match input shapes."""
    N = 30
    dx = 0.1
    phi = np.random.default_rng(1).standard_normal((N, 8))
    pi_field = np.random.default_rng(2).standard_normal((N, 8))

    dphi, dpi = octonionic_klein_gordon_rhs(phi, pi_field, dx, m_squared=1.0)

    assert dphi.shape == (N, 8), f"dphi shape {dphi.shape} != expected (N, 8)"
    assert dpi.shape == (N, 8), f"dpi shape {dpi.shape} != expected (N, 8)"


# ---------------------------------------------------------------------------
# test_energy_positive
# ---------------------------------------------------------------------------

def test_energy_positive():
    """Energy is strictly positive for a nonzero field."""
    phi0, pi0, dx = _make_gaussian_field(amplitude=1.0)
    energy = compute_energy(phi0, pi0, dx, m_squared=1.0)
    assert energy > 0, f"Energy {energy} should be positive for nonzero field"


def test_energy_zero_for_zero_field():
    """Energy is zero for the zero field."""
    N = 30
    dx = 0.2
    phi0 = np.zeros((N, 8))
    pi0 = np.zeros((N, 8))
    energy = compute_energy(phi0, pi0, dx, m_squared=1.0)
    assert abs(energy) < 1e-15, f"Energy {energy} should be zero for zero field"


# ---------------------------------------------------------------------------
# test_energy_conservation_free_field
# ---------------------------------------------------------------------------

def test_energy_conservation_free_field():
    """Energy is conserved (< 1% relative error) for a free field (m^2 = 0)."""
    N = 50
    dx = 0.2
    dt = 0.05
    n_steps = 200

    phi0, pi0, _ = _make_sinusoidal_field(N, dx)

    result = verify_energy_conservation(phi0, pi0, dx, dt, n_steps, m_squared=0.0)

    assert result['conserved'], (
        f"Energy not conserved for free field: "
        f"max relative error = {result['max_relative_error']:.6e}"
    )
    assert result['max_relative_error'] < 0.01, (
        f"Relative error {result['max_relative_error']:.6e} exceeds 1%"
    )


# ---------------------------------------------------------------------------
# test_energy_conservation_massive_field
# ---------------------------------------------------------------------------

def test_energy_conservation_massive_field():
    """Energy is conserved (< 1% relative error) for a massive field (m^2 > 0)."""
    N = 50
    dx = 0.2
    dt = 0.05
    n_steps = 200

    phi0, pi0, _ = _make_sinusoidal_field(N, dx)

    result = verify_energy_conservation(phi0, pi0, dx, dt, n_steps, m_squared=2.0)

    assert result['conserved'], (
        f"Energy not conserved for massive field: "
        f"max relative error = {result['max_relative_error']:.6e}"
    )
    assert result['max_relative_error'] < 0.01, (
        f"Relative error {result['max_relative_error']:.6e} exceeds 1%"
    )


# ---------------------------------------------------------------------------
# test_signal_speed_unity
# ---------------------------------------------------------------------------

def test_signal_speed_unity():
    """Wavefront propagates at speed 1 (within tolerance)."""
    result = signal_speed_test(N=100, dx=0.1, dt=0.05, n_steps=200)
    assert abs(result['measured_speed'] - 1.0) < 0.3, (
        f"Measured speed {result['measured_speed']:.4f} differs from 1.0 "
        f"by more than tolerance"
    )


# ---------------------------------------------------------------------------
# test_signal_speed_causal
# ---------------------------------------------------------------------------

def test_signal_speed_causal():
    """No superluminal propagation: measured speed <= 1 + tolerance."""
    result = signal_speed_test(N=100, dx=0.1, dt=0.05, n_steps=200)
    assert result['causal'], (
        f"Signal appears superluminal: measured speed = {result['measured_speed']:.4f}"
    )


# ---------------------------------------------------------------------------
# test_quaternionic_slice_no_leakage
# ---------------------------------------------------------------------------

def test_quaternionic_slice_no_leakage():
    """A field restricted to quaternionic components stays quaternionic."""
    result = quaternionic_slice_consistency(N=50, dx=0.2, dt=0.1, n_steps=100)
    assert result['stays_quaternionic'], (
        f"Quaternionic field leaked into octonionic directions: "
        f"max leakage = {result['max_leakage']:.6e}"
    )


# ---------------------------------------------------------------------------
# test_quaternionic_matches_standard
# ---------------------------------------------------------------------------

def test_quaternionic_matches_standard():
    """Quaternionic-restricted evolution matches standard Klein-Gordon on H."""
    result = quaternionic_slice_consistency(N=50, dx=0.2, dt=0.1, n_steps=100)
    assert result['matches_standard'], (
        "Quaternionic evolution does not match standard KG"
    )


# ---------------------------------------------------------------------------
# test_associator_bound_cubic
# ---------------------------------------------------------------------------

def test_associator_bound_cubic():
    """
    The associator correction is bounded by C * ||phi||^3 (cubic in amplitude).

    We test with two amplitudes: if the bound is cubic, then scaling phi by
    factor alpha should scale the associator by alpha^3.
    """
    N = 50
    dx = 0.2

    # Create a field with multiple nonzero octonionic components
    rng = np.random.default_rng(42)
    phi_base = np.zeros((N, 8))
    x = np.arange(N) * dx
    for k in range(8):
        phi_base[:, k] = 0.1 * np.sin((k + 1) * np.pi * x / (N * dx))

    # Compute associator bound at two amplitudes
    alpha = 2.0
    bound_1 = associator_perturbation_bound(phi_base, dx)
    bound_alpha = associator_perturbation_bound(alpha * phi_base, dx)

    # If associator is cubic: bound(alpha * phi) ~ alpha^3 * bound(phi)
    if bound_1 > 1e-15:
        ratio = bound_alpha / bound_1
        expected_ratio = alpha ** 3
        # Allow some tolerance for discretization
        assert abs(ratio - expected_ratio) / expected_ratio < 0.1, (
            f"Associator scaling ratio {ratio:.4f} differs from expected "
            f"cubic scaling {expected_ratio:.1f} by more than 10%"
        )
    else:
        # If bound is essentially zero for small amplitude, that's fine
        # (quaternionic subspace or very small field)
        pass


# ---------------------------------------------------------------------------
# test_zero_field_stays_zero
# ---------------------------------------------------------------------------

def test_zero_field_stays_zero():
    """Zero initial data produces zero for all time."""
    N = 30
    dx = 0.2
    dt = 0.1
    n_steps = 50

    phi0 = np.zeros((N, 8))
    pi0 = np.zeros((N, 8))

    result = evolve_klein_gordon(phi0, pi0, dx, dt, n_steps, m_squared=1.0)

    for step_idx, phi in enumerate(result['phi_history']):
        assert np.max(np.abs(phi)) < 1e-14, (
            f"Nonzero field at step {step_idx}: max = {np.max(np.abs(phi))}"
        )
    for step_idx, pi in enumerate(result['pi_history']):
        assert np.max(np.abs(pi)) < 1e-14, (
            f"Nonzero momentum at step {step_idx}: max = {np.max(np.abs(pi))}"
        )


# ---------------------------------------------------------------------------
# test_well_posedness_summary
# ---------------------------------------------------------------------------

def test_well_posedness_summary():
    """Full well-posedness summary passes all checks."""
    result = well_posedness_summary()

    assert result['well_posed'], (
        f"Well-posedness summary failed: "
        f"energy_conserved={result['energy_conservation']['conserved']}, "
        f"causal={result['signal_speed']['causal']}, "
        f"stays_quat={result['quaternionic_consistency']['stays_quaternionic']}, "
        f"matches_std={result['quaternionic_consistency']['matches_standard']}"
    )
    assert result['perturbation_bound'] >= 0, (
        "Perturbation bound should be non-negative"
    )
