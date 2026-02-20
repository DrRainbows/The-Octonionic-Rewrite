"""
Octonionic Portfolio Computation (Chapter 37)

Creates "price octonions" for financial assets and demonstrates:
- Non-commutativity: P_A * P_B != P_B * P_A
- Non-associativity: [P_A, P_B, P_C] != 0 (the "context premium")
- Scale comparison of the associator to portfolio values
- Moufang identity verification as structural constraints

Extracted from Appendix C.15 and C.16.
"""
import numpy as np
from itertools import combinations
from octonion_algebra.core import Octonion
from octonion_algebra.associator import associator


def moufang_check(a, b, c):
    """
    Verify the three Moufang identities for given octonions.

    The Moufang identities are:
        1. ((xy)z)y = x(y(zy))
        2. (x(yz))x = (xy)(zx)
        3. ((xy)x)z = x(y(xz))

    These hold in any alternative algebra (including octonions) and
    constrain but do not eliminate the context premium.

    Args:
        a, b, c: Octonion instances

    Returns:
        dict with keys:
            'moufang_1', 'moufang_2', 'moufang_3': bool (True if satisfied)
            'errors': tuple of 3 floats (norm of lhs - rhs for each identity)
    """
    # Identity 1: ((xy)z)y = x(y(zy))
    lhs1 = ((a * b) * c) * b
    rhs1 = a * (b * (c * b))
    err1 = (lhs1 - rhs1).norm()

    # Identity 2: (x(yz))x = (xy)(zx)
    lhs2 = (a * (b * c)) * a
    rhs2 = (a * b) * (c * a)
    err2 = (lhs2 - rhs2).norm()

    # Identity 3: ((xy)x)z = x(y(xz))
    lhs3 = ((a * b) * a) * c
    rhs3 = a * (b * (a * c))
    err3 = (lhs3 - rhs3).norm()

    return {
        'moufang_1': err1 < 1e-10,
        'moufang_2': err2 < 1e-10,
        'moufang_3': err3 < 1e-10,
        'errors': (err1, err2, err3),
    }


def context_premium(p_a, p_b, p_c):
    """
    Compute the context premium for three price octonions.

    The context premium is the associator [P_A, P_B, P_C], which measures
    how much the portfolio value depends on the order of composition.

    Args:
        p_a, p_b, p_c: Octonion instances (price octonions)

    Returns:
        dict with keys:
            'associator': Octonion, the associator [P_A, P_B, P_C]
            'associator_norm': float, |[P_A, P_B, P_C]|
            'left_bracket': float, |(P_A * P_B) * P_C|
            'right_bracket': float, |P_A * (P_B * P_C)|
            'context_ratio': float, |assoc| / average_bracket_norm
    """
    assoc = associator(p_a, p_b, p_c)
    assoc_norm = assoc.norm()

    left_bracket = (p_a * p_b) * p_c
    right_bracket = p_a * (p_b * p_c)
    left_norm = left_bracket.norm()
    right_norm = right_bracket.norm()

    avg_portfolio = (left_norm + right_norm) / 2
    context_ratio = assoc_norm / avg_portfolio if avg_portfolio > 1e-15 else 0.0

    return {
        'associator': assoc,
        'associator_norm': assoc_norm,
        'left_bracket': left_norm,
        'right_bracket': right_norm,
        'context_ratio': context_ratio,
    }


def portfolio_analysis(assets):
    """
    Compute context premium for all triples of assets.

    Args:
        assets: dict mapping name (str) -> Octonion (price octonion)

    Returns:
        list of dicts, one per triple, each containing:
            'triple': tuple of 3 asset names
            'associator_norm': float
            'context_ratio': float
            'left_bracket': float
            'right_bracket': float
    """
    asset_names = list(assets.keys())
    results = []

    for combo in combinations(asset_names, 3):
        i, j, k = combo
        cp = context_premium(assets[i], assets[j], assets[k])
        results.append({
            'triple': combo,
            'associator_norm': cp['associator_norm'],
            'context_ratio': cp['context_ratio'],
            'left_bracket': cp['left_bracket'],
            'right_bracket': cp['right_bracket'],
        })

    return results
