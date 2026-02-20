"""
Associator computation for octonions.

The associator [a, b, c] = (a*b)*c - a*(b*c) measures the failure of
associativity and encodes contextual information about composition ordering.
"""
import numpy as np
from octonion_algebra.core import Octonion


def associator(a, b, c):
    """
    Compute the associator [a, b, c] = (a*b)*c - a*(b*c).

    This is the central object of the octonionic framework.
    It measures the failure of associativity and encodes
    contextual information about composition ordering.

    The associator is:
    - Completely antisymmetric: [a,b,c] = -[b,a,c] = -[a,c,b] = ...
    - Zero when any two arguments are equal (by alternativity)
    - Zero when all three arguments lie in the same quaternionic subalgebra
    - Nonzero in general (this is the key feature, not a bug)

    Args:
        a, b, c: Octonion instances

    Returns:
        Octonion: the associator (a*b)*c - a*(b*c)
    """
    return (a * b) * c - a * (b * c)


def associator_norm(a, b, c):
    """Return |[a,b,c]|, the magnitude of the associator."""
    return associator(a, b, c).norm()
