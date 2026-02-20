"""
Octonionic Vector Calculus Identities (Chapter 11).

Implements the key algebraic identities of 7D vector calculus that arise
from the octonionic cross product, including the modified BAC-CAB rule,
the jacobiator, the Malcev identity, and the Fano correction tensor.
"""
import numpy as np
from octonion_algebra.core import Octonion, cross_product_7d, FANO_TRIPLES
from octonion_algebra.associator import associator


def cross_product_associator(a, b, c):
    """
    Compute the cross-product associator [a, b, c]_x = (a x b) x c - a x (b x c).

    This is the purely 7D quantity measuring the failure of the cross product
    to satisfy the Jacobi identity. It vanishes identically in 3D.

    Args:
        a, b, c: Octonion instances (must be purely imaginary).

    Returns:
        Octonion: the cross-product associator (purely imaginary).
    """
    ab_cross = cross_product_7d(a, b)
    bc_cross = cross_product_7d(b, c)
    return cross_product_7d(ab_cross, c) - cross_product_7d(a, bc_cross)


def bac_cab_7d(a, b, c):
    """
    Verify the modified BAC-CAB rule in 7D (Theorem 11.4).

    a x (b x c) = b(a.c) - c(a.b) + (1/2)[a, b, c]_x

    Args:
        a, b, c: Octonion instances (purely imaginary).

    Returns:
        dict with keys:
            'lhs':        a x (b x c)
            'bac_cab':    b(a.c) - c(a.b)  (classical BAC-CAB term)
            'correction': (1/2)[a, b, c]_x  (non-associative correction)
            'rhs':        bac_cab + correction (should equal lhs)
    """
    bc_cross = cross_product_7d(b, c)
    lhs = cross_product_7d(a, bc_cross)

    a_dot_c = a.dot(c)
    a_dot_b = a.dot(b)
    bac_cab = b * a_dot_c - c * a_dot_b

    # The correction is -(1/2) times the octonionic associator [a,b,c],
    # NOT the cross-product associator. For purely imaginary octonions,
    # [a,b,c] is purely imaginary, and:
    #   a x (b x c) = b(a.c) - c(a.b) - (1/2)[a,b,c]
    correction = associator(a, b, c) * (-0.5)

    rhs = bac_cab + correction

    return {
        'lhs': lhs,
        'bac_cab': bac_cab,
        'correction': correction,
        'rhs': rhs,
    }


def jacobiator_7d(a, b, c):
    """
    Compute the jacobiator J(a, b, c) = a x (b x c) + b x (c x a) + c x (a x b).

    In 3D this is zero (the Jacobi identity). In 7D it equals
    3 * Im([a, b, c]) where [a, b, c] is the octonionic associator.

    Args:
        a, b, c: Octonion instances (purely imaginary).

    Returns:
        Octonion: the jacobiator (purely imaginary).
    """
    term1 = cross_product_7d(a, cross_product_7d(b, c))
    term2 = cross_product_7d(b, cross_product_7d(c, a))
    term3 = cross_product_7d(c, cross_product_7d(a, b))
    return term1 + term2 + term3


def malcev_identity(a, b, c):
    """
    Verify the Malcev identity (Theorem 11.3, property 6).

    (a x b) x (a x c) = ((a x b) x c) x a + ((b x c) x a) x a + ((c x a) x a) x b

    This is the replacement for the Jacobi identity in 7D.

    Args:
        a, b, c: Octonion instances (purely imaginary).

    Returns:
        dict with keys:
            'lhs':   (a x b) x (a x c)
            'rhs':   ((a x b) x c) x a + ((b x c) x a) x a + ((c x a) x a) x b
            'error': norm of lhs - rhs
    """
    ab = cross_product_7d(a, b)
    ac = cross_product_7d(a, c)
    bc = cross_product_7d(b, c)
    ca = cross_product_7d(c, a)

    lhs = cross_product_7d(ab, ac)

    term1 = cross_product_7d(cross_product_7d(ab, c), a)
    term2 = cross_product_7d(cross_product_7d(bc, a), a)
    term3 = cross_product_7d(cross_product_7d(ca, a), b)

    rhs = term1 + term2 + term3

    return {
        'lhs': lhs,
        'rhs': rhs,
        'error': (lhs - rhs).norm(),
    }


def structure_constants():
    """
    Build the 3-index structure constant tensor epsilon_{ijk} from FANO_TRIPLES.

    Uses 0-indexed coordinates (0..6) corresponding to e1..e7.

    Returns:
        numpy array of shape (7, 7, 7):
            epsilon[i][j][k] = +1 for positively oriented Fano lines,
                               -1 for negatively oriented,
                                0 otherwise.
    """
    eps = np.zeros((7, 7, 7), dtype=float)
    for (a, b, c) in FANO_TRIPLES:
        # Convert from 1-indexed to 0-indexed
        i, j, k = a - 1, b - 1, c - 1
        # Cyclic permutations are positive
        eps[i, j, k] = +1.0
        eps[j, k, i] = +1.0
        eps[k, i, j] = +1.0
        # Anti-cyclic permutations are negative
        eps[j, i, k] = -1.0
        eps[k, j, i] = -1.0
        eps[i, k, j] = -1.0
    return eps


def fano_correction_tensor():
    """
    Build the 4-index Fano correction tensor T_{ijkl}.

    T_{ijkl} = sum_m epsilon_{ijm} * epsilon_{mkl} - delta_{ik}*delta_{jl} + delta_{il}*delta_{jk}

    This tensor measures the failure of the Jacobi identity in 7D.
    In 3D the analogous tensor is identically zero.

    Returns:
        numpy array of shape (7, 7, 7, 7).
    """
    eps = structure_constants()
    T = np.zeros((7, 7, 7, 7), dtype=float)
    for i in range(7):
        for j in range(7):
            for k in range(7):
                for l in range(7):
                    contraction = 0.0
                    for m in range(7):
                        contraction += eps[i, j, m] * eps[m, k, l]
                    delta_term = (1.0 if i == k else 0.0) * (1.0 if j == l else 0.0) \
                               - (1.0 if i == l else 0.0) * (1.0 if j == k else 0.0)
                    T[i, j, k, l] = contraction - delta_term
    return T
