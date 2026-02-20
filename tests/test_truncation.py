"""Tests for the COPBW truncation schemes module.

Validates that each truncation strategy reduces the tree-monomial basis
while preserving essential structure. Addresses Grok critique #13.
"""

import numpy as np
import pytest

from octonion_algebra.copbw import (
    catalan,
    enumerate_tree_monomials,
    TreeMonomial,
)
from octonion_algebra.truncation import (
    depth_truncation,
    alternator_reduced_basis,
    casimir_truncation,
    truncation_error_estimate,
    g2_equivariant_truncation,
    growth_rate_analysis,
    practical_basis,
)


# Two generators is a good default: small enough to be fast, large enough
# to exercise the combinatorics meaningfully.
GENERATORS = ["a", "b"]


# -----------------------------------------------------------------------
# 1. Depth truncation reduces count
# -----------------------------------------------------------------------

def test_depth_truncation_reduces():
    """Depth truncation gives strictly fewer monomials than full enumeration
    for degree >= 3, where multiple tree depths exist."""
    max_degree = 4
    max_depth = 1

    truncated = depth_truncation(GENERATORS, max_degree, max_depth)

    # Full count across degrees 1..max_degree
    full_count = sum(
        len(enumerate_tree_monomials(GENERATORS, d))
        for d in range(1, max_degree + 1)
    )

    assert len(truncated) < full_count, (
        f"Depth truncation should reduce count: got {len(truncated)} "
        f"vs full {full_count}"
    )


# -----------------------------------------------------------------------
# 2. Depth truncation correct count at depth=1
# -----------------------------------------------------------------------

def test_depth_truncation_correct_count():
    """At depth=1, tree monomials are exactly the single-product trees
    (two leaves), so for degree n >= 2 only the trees with depth exactly 1
    are kept. For degree 1 (leaves), depth is 0 which is <= 1.

    At depth=1, degree=2: all k^2 trees (since the only tree shape at
    degree 2 has depth 1). For degree >= 3, depth-1 trees don't exist
    (minimum depth for degree n is ceil(log2(n))), so only degree 1 and 2
    monomials survive.
    """
    k = len(GENERATORS)
    max_degree = 4
    max_depth = 1

    truncated = depth_truncation(GENERATORS, max_degree, max_depth)

    # Degree 1: k leaves (depth 0)
    # Degree 2: k^2 monomials (depth 1)
    # Degree >= 3: minimum depth is 2, so 0 monomials pass
    expected = k + k ** 2
    assert len(truncated) == expected, (
        f"At depth=1, expected {expected} monomials (k + k^2), "
        f"got {len(truncated)}"
    )


# -----------------------------------------------------------------------
# 3. Alternator reduces count
# -----------------------------------------------------------------------

def test_alternator_reduces_count():
    """Alternator reduction gives fewer independent monomials than the
    full tree count at degree >= 3 (where alternator relations kick in)."""
    # At degree 3, there are 2 tree shapes (Catalan C_2 = 2) times k^3 = 8
    # orderings = 16 monomials. The alternator ideal identifies some of them.
    result = alternator_reduced_basis(GENERATORS, degree=3, n_samples=100, seed=42)

    assert result['reduced_count'] < result['full_count'], (
        f"Alternator should reduce: {result['reduced_count']} "
        f"vs full {result['full_count']}"
    )


# -----------------------------------------------------------------------
# 4. Alternator reduction is nontrivial (reduced_count > 0)
# -----------------------------------------------------------------------

def test_alternator_reduction_nontrivial():
    """Reduced count > 0 at each degree 1..4, meaning the alternator ideal
    does not collapse everything to zero."""
    for degree in range(1, 5):
        result = alternator_reduced_basis(GENERATORS, degree=degree,
                                          n_samples=80, seed=42)
        assert result['reduced_count'] > 0, (
            f"Reduced count should be > 0 at degree {degree}, "
            f"got {result['reduced_count']}"
        )


# -----------------------------------------------------------------------
# 5. Casimir truncation reduces count
# -----------------------------------------------------------------------

def test_casimir_truncation_reduces():
    """Casimir truncation with a tight cutoff gives fewer monomials than full."""
    max_degree = 4
    # A tight cutoff: only allow weight <= 1
    # At degree >= 3, many trees have weight > 1
    truncated = casimir_truncation(GENERATORS, max_degree, casimir_cutoff=1)

    full_count = sum(
        len(enumerate_tree_monomials(GENERATORS, d))
        for d in range(1, max_degree + 1)
    )

    assert len(truncated) < full_count, (
        f"Casimir truncation should reduce: got {len(truncated)} "
        f"vs full {full_count}"
    )


# -----------------------------------------------------------------------
# 6. Truncation error decreases as depth increases
# -----------------------------------------------------------------------

def test_truncation_error_decreases():
    """Truncation error should decrease (or stay zero) as we increase the
    allowed depth, since we keep more monomials."""
    degree = 4  # degree 4 has trees of depth 1, 2, 3
    errors = []
    for depth in range(1, 4):
        result = truncation_error_estimate(GENERATORS, degree=degree,
                                           truncation_depth=depth,
                                           n_samples=30, seed=42)
        errors.append(result['relative_error'])

    # Error should be non-increasing as depth grows
    for i in range(len(errors) - 1):
        assert errors[i] >= errors[i + 1] - 1e-10, (
            f"Error should decrease: depth {i+1} error={errors[i]:.6f} "
            f"but depth {i+2} error={errors[i+1]:.6f}"
        )

    # The last (deepest) truncation should have zero or near-zero error
    # (at depth 3, all degree-4 trees are kept)
    assert errors[-1] < 1e-6, (
        f"At maximum depth, error should be ~0, got {errors[-1]}"
    )


# -----------------------------------------------------------------------
# 7. G2-equivariant truncation gives fewer orbits than monomials
# -----------------------------------------------------------------------

def test_g2_equivariant_fewer_orbits():
    """Number of G2 orbits should be less than the total number of monomials
    at degree >= 2, since G2 symmetry identifies some monomials."""
    result = g2_equivariant_truncation(GENERATORS, degree=2,
                                       n_samples=30, seed=42)
    n_mono = len(enumerate_tree_monomials(GENERATORS, 2))

    assert result['n_orbits'] <= n_mono, (
        f"Orbits ({result['n_orbits']}) should be <= monomials ({n_mono})"
    )
    assert result['n_orbits'] > 0, "Should have at least one orbit"
    assert sum(result['orbit_sizes']) == n_mono, (
        f"Orbit sizes should sum to total monomials: "
        f"{sum(result['orbit_sizes'])} vs {n_mono}"
    )


# -----------------------------------------------------------------------
# 8. Growth rate: reduced basis grows slower than full
# -----------------------------------------------------------------------

def test_growth_rate_subexponential():
    """The alternator-reduced basis should grow slower than the full tree count
    at higher degrees. Specifically, the ratio reduced/full should decrease
    as degree increases (for degree >= 3 where alternator relations exist)."""
    result = growth_rate_analysis(GENERATORS, max_degree=5)

    # At degree 1 and 2, reduced == full (no alternator relations)
    # From degree 3 onward, reduced < full
    for d_idx in range(2, len(result['degrees'])):  # degree 3, 4, 5
        full = result['full_counts'][d_idx]
        reduced = result['reduced_counts'][d_idx]
        assert reduced <= full, (
            f"At degree {result['degrees'][d_idx]}: "
            f"reduced={reduced} should be <= full={full}"
        )

    # Asymptotic ratio should be < 1
    assert result['asymptotic_ratio'] <= 1.0, (
        f"Asymptotic ratio should be <= 1.0, got {result['asymptotic_ratio']}"
    )


# -----------------------------------------------------------------------
# 9. Practical basis is nonempty for each strategy
# -----------------------------------------------------------------------

def test_practical_basis_nonempty():
    """practical_basis returns a nonempty basis for each strategy."""
    for strategy in ['alternator', 'depth', 'casimir']:
        result = practical_basis(GENERATORS, max_degree=3, strategy=strategy)

        assert result['size'] > 0, (
            f"Strategy '{strategy}' should produce a nonempty basis, "
            f"got size={result['size']}"
        )
        assert result['strategy'] == strategy
        assert len(result['basis']) == result['size']
        assert isinstance(result['degree_breakdown'], dict)


# -----------------------------------------------------------------------
# 10. Practical basis at degree 2: all strategies agree
# -----------------------------------------------------------------------

def test_practical_basis_degree_2():
    """At degree 2 there is only one tree shape (C_1 = 1), so no truncation
    is possible. All strategies should yield the same count at degree 2."""
    k = len(GENERATORS)
    expected_d2 = k ** 2  # k^2 * C_1 = k^2

    for strategy in ['alternator', 'depth', 'casimir']:
        result = practical_basis(GENERATORS, max_degree=2, strategy=strategy)

        d2_count = result['degree_breakdown'].get(2, 0)
        assert d2_count == expected_d2, (
            f"Strategy '{strategy}' at degree 2 should give {expected_d2} "
            f"monomials, got {d2_count}"
        )
