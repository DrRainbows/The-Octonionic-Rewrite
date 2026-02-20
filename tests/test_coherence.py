"""Tests for the coherence conservation module."""
import numpy as np
import pytest

from octonion_algebra.core import Octonion
from octonion_algebra.coherence import (
    coherence_functional,
    g2_rotate_field,
    make_smooth_field,
)
from octonion_algebra.g2 import g2_generators


@pytest.fixture
def smooth_field():
    return make_smooth_field(20, seed=42)


@pytest.fixture
def g2_gens():
    return g2_generators()


def test_coherence_nonnegative(smooth_field):
    """C[field] >= 0 since it is a sum of squared norms."""
    C = coherence_functional(smooth_field)
    assert C >= 0, f"Coherence functional is negative: {C}"


def test_coherence_nonzero_generic():
    """C[random field] > 0 for a generic (non-trivial) octonionic field."""
    rng = np.random.default_rng(123)
    field = [Octonion(rng.uniform(-1, 1, size=8)) for _ in range(10)]
    C = coherence_functional(field)
    assert C > 0, f"Coherence functional should be positive for generic field, got {C}"


def test_coherence_g2_invariant(smooth_field, g2_gens):
    """C[field] ~ C[g2_rotate(field)] for small G2 rotation.

    The coherence functional is invariant under G2 automorphisms because
    G2 preserves the octonion multiplication (and hence the associator).
    """
    C_original = coherence_functional(smooth_field)

    # Small G2 rotation using first few generators
    coeffs = [0.1, -0.05, 0.03] + [0.0] * 11
    rotated_field = g2_rotate_field(smooth_field, g2_gens, coeffs, angle=0.05)
    C_rotated = coherence_functional(rotated_field)

    np.testing.assert_allclose(
        C_original, C_rotated, rtol=1e-6,
        err_msg="Coherence functional not invariant under G2 rotation"
    )


def test_coherence_not_so7_invariant(smooth_field):
    """A random SO(7) rotation (not in G2) changes C.

    Generic elements of SO(7) do NOT preserve octonion multiplication,
    so the coherence functional should change.
    """
    C_original = coherence_functional(smooth_field)

    # Create a random SO(7) rotation (generic, not G2)
    rng = np.random.default_rng(999)
    A = rng.standard_normal((7, 7))
    # Make antisymmetric
    A = (A - A.T) / 2
    # Exponentiate to get SO(7) element via Taylor series
    M = 0.5 * A
    R = np.eye(7)
    term = np.eye(7)
    for k in range(1, 30):
        term = term @ M / k
        R = R + term

    # Apply rotation to field
    rotated_field = []
    for f_i in smooth_field:
        new_coeffs = np.zeros(8)
        new_coeffs[0] = f_i.coeffs[0]
        new_coeffs[1:] = R @ f_i.coeffs[1:]
        rotated_field.append(Octonion(new_coeffs))

    C_rotated = coherence_functional(rotated_field)

    # They should NOT be equal for a generic SO(7) rotation
    assert abs(C_original - C_rotated) > 1e-6, (
        f"Coherence functional should change under generic SO(7) rotation, "
        f"but C_original={C_original}, C_rotated={C_rotated}"
    )


def test_coherence_conserved(smooth_field, g2_gens):
    """Coherence is approximately preserved under a sequence of G2 rotations.

    This tests that applying multiple small G2 rotations in succession
    preserves the coherence functional (since each individual rotation does).
    """
    C_original = coherence_functional(smooth_field)

    # Apply several successive small G2 rotations
    field = smooth_field
    for step in range(5):
        coeffs = np.zeros(14)
        coeffs[step % 14] = 0.1
        field = g2_rotate_field(field, g2_gens, coeffs, angle=0.02)

    C_after = coherence_functional(field)

    np.testing.assert_allclose(
        C_original, C_after, rtol=1e-4,
        err_msg="Coherence not conserved under successive G2 rotations"
    )
