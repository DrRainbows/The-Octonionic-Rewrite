"""Tests for the octonionic finance (portfolio) module."""
import numpy as np
import pytest

from octonion_algebra.core import Octonion
from octonion_algebra.alignment import restrict_to_quaternion
from octonion_algebra.finance import (
    moufang_check,
    context_premium,
    portfolio_analysis,
)


@pytest.fixture
def random_octonions():
    """Three random octonions for testing."""
    return [Octonion.random(seed=i) for i in range(10, 13)]


@pytest.fixture
def quaternionic_octonions():
    """Three quaternionic octonions (components 0-3 only)."""
    result = []
    for i in range(3):
        o = Octonion.random(seed=50 + i)
        q = restrict_to_quaternion(o)
        # Scale up so they are not unit (more interesting test)
        result.append(q * 2.0)
    return result


def test_moufang_identities(random_octonions):
    """moufang_check returns all True for random octonions.

    The Moufang identities hold in any alternative algebra, including
    the octonions.
    """
    a, b, c = random_octonions
    result = moufang_check(a, b, c)

    assert result['moufang_1'], f"Moufang identity 1 failed, error = {result['errors'][0]}"
    assert result['moufang_2'], f"Moufang identity 2 failed, error = {result['errors'][1]}"
    assert result['moufang_3'], f"Moufang identity 3 failed, error = {result['errors'][2]}"

    # Errors should be very small
    for i, err in enumerate(result['errors']):
        assert err < 1e-10, f"Moufang identity {i+1} error too large: {err}"


def test_context_premium_nonzero(random_octonions):
    """context_premium > 0 for non-quaternionic inputs.

    Generic octonions are not associative, so the context premium
    (associator norm) should be nonzero.
    """
    a, b, c = random_octonions
    cp = context_premium(a, b, c)

    assert cp['associator_norm'] > 1e-10, (
        f"Context premium should be nonzero for generic octonions, "
        f"got {cp['associator_norm']}"
    )
    assert cp['context_ratio'] > 0, (
        f"Context ratio should be positive, got {cp['context_ratio']}"
    )


def test_context_premium_zero_quaternionic(quaternionic_octonions):
    """context_premium ~ 0 for quaternionic inputs.

    Quaternions are associative, so the associator (and hence the
    context premium) should vanish.
    """
    a, b, c = quaternionic_octonions
    cp = context_premium(a, b, c)

    assert cp['associator_norm'] < 1e-10, (
        f"Context premium should be zero for quaternionic inputs, "
        f"got {cp['associator_norm']}"
    )


def test_portfolio_analysis_returns_triples():
    """portfolio_analysis returns list of dicts, one per triple of assets."""
    assets = {
        'A': Octonion.random(seed=70),
        'B': Octonion.random(seed=71),
        'C': Octonion.random(seed=72),
        'D': Octonion.random(seed=73),
    }

    results = portfolio_analysis(assets)

    # C(4,3) = 4 triples
    assert len(results) == 4, f"Expected 4 triples, got {len(results)}"

    for r in results:
        assert 'triple' in r, "Result dict missing 'triple' key"
        assert 'associator_norm' in r, "Result dict missing 'associator_norm' key"
        assert 'context_ratio' in r, "Result dict missing 'context_ratio' key"
        assert 'left_bracket' in r, "Result dict missing 'left_bracket' key"
        assert 'right_bracket' in r, "Result dict missing 'right_bracket' key"
        assert len(r['triple']) == 3, f"Triple should have 3 names, got {len(r['triple'])}"
        assert isinstance(r['associator_norm'], float), "associator_norm should be float"
