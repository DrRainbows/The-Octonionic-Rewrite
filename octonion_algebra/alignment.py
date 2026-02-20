"""
Non-Gameable Alignment (Chapter 26)

Implements the alignment function and demonstrates that in the octonionic
(non-associative) setting, any agent replacement changes the associator
signature, making gaming detectable. In the quaternionic (associative)
restriction, gaming is undetectable.

Extracted from Appendix C.12.
"""
import numpy as np
from octonion_algebra.core import Octonion, FANO_TRIPLES
from octonion_algebra.associator import associator


def all_bracketings_4(a, b, c, d):
    """
    Return all 5 Catalan bracketings of 4 elements (fixed order).

    The Catalan number C_3 = 5 gives the number of distinct ways to
    parenthesise a product of 4 elements in a non-associative algebra.

    Args:
        a, b, c, d: Octonion instances

    Returns:
        List of 5 Octonion values, one per bracketing.
    """
    return [
        ((a * b) * c) * d,        # left-left-left
        (a * (b * c)) * d,        # right-left
        (a * b) * (c * d),        # balanced
        a * ((b * c) * d),        # left-right
        a * (b * (c * d)),        # right-right-right
    ]


def associator_signature(team):
    """
    Compute the associator 'checksum' over all triples in the team.

    Sums associator(team[i], team[j], team[k]) for all triples i < j < k.
    In the octonionic setting this signature changes under any single-agent
    replacement, making gaming detectable.

    Args:
        team: list of Octonion instances

    Returns:
        Octonion: the cumulative associator signature
    """
    sig = Octonion()
    n = len(team)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                sig = sig + associator(team[i], team[j], team[k])
    return sig


def alignment_score(team, voters):
    """
    Compute alignment: average real part of (bracketing * voter).

    Averages over all 5 Catalan bracketings of the 4-member team and
    over all voters.

    Args:
        team: list of 4 Octonion instances (unit octonions)
        voters: list of Octonion instances (unit octonions)

    Returns:
        float: the alignment score
    """
    brack_vals = all_bracketings_4(
        team[0], team[1], team[2], team[3]
    )
    total = 0.0
    for bv in brack_vals:
        for voter in voters:
            total += (bv * voter).real_part()
    return total / (len(brack_vals) * len(voters))


def detect_gaming(team, replacement_index, n_attempts=100, seed=10000):
    """
    Try random replacements at the given index and check whether the
    associator signature changes (indicating detectable gaming).

    Args:
        team: list of Octonion instances (the original team)
        replacement_index: int, which team member to replace
        n_attempts: number of random replacement attempts
        seed: base seed for reproducible random replacements

    Returns:
        dict with keys:
            'detected_count': number of attempts where signature changed
            'total_attempts': n_attempts
            'detection_rate': fraction of detected attempts
    """
    sig_original = associator_signature(team)
    detected_count = 0

    for attempt in range(n_attempts):
        replacement = Octonion.random(seed=seed + attempt)
        replacement = replacement / replacement.norm()

        new_team = team.copy()
        new_team[replacement_index] = replacement

        new_sig = associator_signature(new_team)
        sig_diff = (new_sig - sig_original).norm()

        if sig_diff > 1e-10:
            detected_count += 1

    return {
        'detected_count': detected_count,
        'total_attempts': n_attempts,
        'detection_rate': detected_count / n_attempts,
    }


def restrict_to_quaternion(o):
    """
    Project an octonion to the quaternionic subalgebra {1, e1, e2, e3}
    and normalize to unit norm.

    Args:
        o: Octonion instance

    Returns:
        Octonion: the projected and normalized quaternion
    """
    c = np.zeros(8)
    c[0:4] = o.coeffs[0:4]
    result = Octonion(c)
    n = result.norm()
    if n > 1e-15:
        result = result / n
    return result
