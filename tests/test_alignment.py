"""Tests for the non-gameable alignment module."""
import numpy as np
import pytest

from octonion_algebra.core import Octonion
from octonion_algebra.alignment import (
    all_bracketings_4,
    associator_signature,
    detect_gaming,
    restrict_to_quaternion,
    alignment_score,
)


@pytest.fixture
def random_team():
    """A team of 4 random unit octonions."""
    team = []
    for i in range(4):
        o = Octonion.random(seed=100 + i)
        team.append(o / o.norm())
    return team


@pytest.fixture
def quaternionic_team():
    """A team of 4 quaternionic (associative) unit octonions."""
    team = []
    for i in range(4):
        o = Octonion.random(seed=200 + i)
        q = restrict_to_quaternion(o)
        team.append(q)
    return team


def test_all_bracketings_count():
    """all_bracketings_4 returns 5 results (Catalan C_3 = 5)."""
    a = Octonion.random(seed=1)
    b = Octonion.random(seed=2)
    c = Octonion.random(seed=3)
    d = Octonion.random(seed=4)

    results = all_bracketings_4(a, b, c, d)
    assert len(results) == 5, f"Expected 5 bracketings, got {len(results)}"

    # Each result should be an Octonion
    for r in results:
        assert isinstance(r, Octonion), f"Bracketing result is not an Octonion: {type(r)}"


def test_associator_signature_nonzero(random_team):
    """Random team has nonzero associator signature in O.

    For generic octonions, the associator is nonzero, so the cumulative
    signature over all triples should be nonzero.
    """
    sig = associator_signature(random_team)
    assert sig.norm() > 1e-10, (
        f"Associator signature should be nonzero for random octonion team, "
        f"got norm {sig.norm()}"
    )


def test_gaming_detected(random_team):
    """detect_gaming returns detection_rate > 0.5 for octonionic team.

    In the octonionic setting, replacing any team member changes the
    associator signature, making gaming detectable.
    """
    result = detect_gaming(random_team, replacement_index=0, n_attempts=50, seed=5000)
    assert result['detection_rate'] > 0.5, (
        f"Detection rate should be > 0.5, got {result['detection_rate']}"
    )


def test_quaternion_restriction_loses_detection(quaternionic_team):
    """Restricting to quaternions reduces detection capability.

    In the quaternionic (associative) subalgebra, the associator vanishes,
    so the signature is zero and gaming is undetectable.
    """
    sig = associator_signature(quaternionic_team)
    assert sig.norm() < 1e-10, (
        f"Quaternionic team should have zero associator signature, "
        f"got norm {sig.norm()}"
    )


def test_alignment_score_real(random_team):
    """alignment_score returns a real number (float)."""
    voters = [Octonion.random(seed=300 + i) for i in range(3)]
    # Normalize voters
    voters = [v / v.norm() for v in voters]

    score = alignment_score(random_team, voters)
    assert isinstance(score, (float, np.floating)), (
        f"alignment_score should return a float, got {type(score)}"
    )
    # The score should be finite
    assert np.isfinite(score), f"alignment_score should be finite, got {score}"
