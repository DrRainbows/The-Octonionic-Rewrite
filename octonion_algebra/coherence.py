"""
Coherence conservation under G2 rotation.

Extracted from Appendix C.11 of the book. The coherence functional
C = sum_i |[f(i), f(i+1), f(i+2)]|^2 measures total associator content
of an octonionic field over consecutive triples. It is invariant under
G2 rotations (automorphisms of O) but not under generic SO(7) rotations.
"""

import numpy as np
from octonion_algebra.core import Octonion
from octonion_algebra.associator import associator
from octonion_algebra.g2 import g2_generators


def coherence_functional(field):
    """
    Compute the coherence functional for an octonionic field.

    C = sum_{i} |[f(i), f(i+1), f(i+2)]|^2

    where the sum runs over all consecutive triples and [a, b, c] is
    the associator (a*b)*c - a*(b*c).

    Args:
        field: list of Octonion instances.

    Returns:
        float: the coherence value C.
    """
    C = 0.0
    for i in range(len(field) - 2):
        assoc = associator(field[i], field[i + 1], field[i + 2])
        C += assoc.norm_squared()
    return C


def g2_rotate_field(field, g2_gens, coeffs, angle):
    """
    Apply a G2 rotation to an octonionic field.

    Constructs a Lie algebra element as a linear combination of G2 generators,
    exponentiates it to obtain an SO(7) matrix (within the G2 subgroup), and
    applies the resulting rotation to the imaginary part of each field element.

    Args:
        field: list of Octonion instances.
        g2_gens: list of 7x7 numpy arrays (G2 generators, from g2_generators()).
        coeffs: array-like of floats, coefficients for the linear combination
                of generators. Length must match len(g2_gens) or be shorter
                (remaining generators get coefficient 0).
        angle: float, overall rotation angle (scales the Lie algebra element).

    Returns:
        list of Octonion instances: the rotated field.
    """
    # Build Lie algebra element g = angle * sum_a coeffs[a] * g2_gens[a]
    g = np.zeros((7, 7))
    for a, c in enumerate(coeffs):
        g += c * g2_gens[a]
    g = angle * g

    # Matrix exponential via Taylor series (30 terms for convergence)
    R = np.eye(7)
    g_power = np.eye(7)
    for n in range(1, 30):
        g_power = g_power @ g / n
        R = R + g_power

    # Apply rotation to each field element
    rotated_field = []
    for f_i in field:
        new_coeffs = np.zeros(8)
        new_coeffs[0] = f_i.coeffs[0]      # Real part unchanged
        new_coeffs[1:] = R @ f_i.coeffs[1:]  # Rotate imaginary part
        rotated_field.append(Octonion(new_coeffs))

    return rotated_field


def make_smooth_field(n_points, seed=42):
    """
    Create a smooth octonionic field on [0, 2*pi] for testing.

    Each component is a smooth function of position, built from products
    of sines and cosines with different frequencies.

    Args:
        n_points: int, number of grid points.
        seed: int, random seed (used only for reproducibility label;
              the field is deterministic given n_points).

    Returns:
        list of Octonion instances of length n_points.
    """
    np.random.seed(seed)
    x_grid = np.linspace(0, 2 * np.pi, n_points)
    field = []
    for i in range(n_points):
        coeffs = np.zeros(8)
        for k in range(8):
            coeffs[k] = np.sin((k + 1) * x_grid[i]) * np.cos(0.5 * k * x_grid[i])
        field.append(Octonion(coeffs))
    return field
