"""
Tests for the interderivability module.

Validates:
- Graded derivation depth computation and consistency
- Alternator quotient non-triviality (addresses critique #30)
- COPBW vs PBW basis comparison (addresses critique #7)
- Full interderivability proof (addresses critique #6)
"""

import pytest
import numpy as np

from octonion_algebra.interderivability import (
    STRUCTURES,
    graded_derivation_depth,
    verify_derivation_consistency,
    alternator_quotient_dimension,
    alternator_ideal_generators,
    quotient_nontriviality_proof,
    derivability_matrix,
    interderivability_classes,
    copbw_vs_pbw_comparison,
)


# ---------------------------------------------------------------------------
# Derivation depth tests
# ---------------------------------------------------------------------------

class TestDerivationDepth:
    """Tests for the graded derivation graph."""

    def test_self_derivation_zero(self):
        """Depth from any structure to itself must be 0."""
        for s in STRUCTURES:
            d = graded_derivation_depth(s, s)
            assert d == 0, f"Self-derivation depth for '{s}' is {d}, expected 0"

    def test_alternativity_to_antisymmetry(self):
        """Alternativity implies associator antisymmetry at depth 1."""
        d = graded_derivation_depth('alternativity', 'associator_antisymmetry')
        assert d == 1, f"Expected depth 1, got {d}"

    def test_fano_to_cross_product(self):
        """Fano multiplication implies cross product at depth 1."""
        d = graded_derivation_depth('fano_multiplication', 'cross_product')
        assert d == 1, f"Expected depth 1, got {d}"

    def test_fano_to_alternativity(self):
        """Fano multiplication implies alternativity at depth 1."""
        d = graded_derivation_depth('fano_multiplication', 'alternativity')
        assert d == 1

    def test_composition_norm_to_alternativity(self):
        """Composition norm implies alternativity at depth 1 (Hurwitz)."""
        d = graded_derivation_depth('composition_norm', 'alternativity')
        assert d == 1

    def test_cross_product_to_fano(self):
        """Cross product determines Fano triples at depth 1."""
        d = graded_derivation_depth('cross_product', 'fano_multiplication')
        assert d == 1

    def test_all_depths_finite(self):
        """Every pair of structures has finite derivation depth."""
        for s in STRUCTURES:
            for t in STRUCTURES:
                d = graded_derivation_depth(s, t, max_depth=20)
                assert d is not None, (
                    f"No finite derivation path from '{s}' to '{t}'"
                )

    def test_unknown_structure_raises(self):
        """Unknown structure names raise ValueError."""
        with pytest.raises(ValueError):
            graded_derivation_depth('nonexistent', 'alternativity')
        with pytest.raises(ValueError):
            graded_derivation_depth('alternativity', 'nonexistent')


# ---------------------------------------------------------------------------
# Interderivability class tests
# ---------------------------------------------------------------------------

class TestInterderivability:
    """Tests for the interderivability equivalence classes."""

    def test_all_structures_interderivable(self):
        """All 7 structures form a single interderivability class."""
        classes = interderivability_classes(max_depth=20)
        assert len(classes) == 1, (
            f"Expected 1 interderivability class, got {len(classes)}: {classes}"
        )
        assert classes[0] == set(STRUCTURES)

    def test_derivation_consistency_triangle(self):
        """Triangle inequality holds for all triples of structures."""
        result = verify_derivation_consistency(max_depth=10)
        assert result['consistent'], (
            f"Triangle inequality violations: {result['triangle_violations']}"
        )
        assert result['n_pairs_checked'] > 0


# ---------------------------------------------------------------------------
# Alternator quotient tests
# ---------------------------------------------------------------------------

class TestAlternatorQuotient:
    """Tests for the alternator quotient non-triviality."""

    def test_quotient_nontrivial_degree_2(self):
        """Quotient dimension is positive at degree 2."""
        generators = ['a', 'b']
        result = alternator_quotient_dimension(generators, max_degree=2)
        deg2_data = result['degree_data'][1]  # index 1 = degree 2
        assert deg2_data['degree'] == 2
        assert deg2_data['quotient_dim'] > 0, (
            f"Quotient collapsed to trivial at degree 2: {deg2_data}"
        )

    def test_quotient_nontrivial_degree_3(self):
        """Quotient dimension is positive at degree 3."""
        generators = ['a', 'b']
        result = alternator_quotient_dimension(generators, max_degree=3)
        deg3_data = result['degree_data'][2]  # index 2 = degree 3
        assert deg3_data['degree'] == 3
        assert deg3_data['quotient_dim'] > 0, (
            f"Quotient collapsed to trivial at degree 3: {deg3_data}"
        )

    def test_quotient_grows(self):
        """Quotient dimension is strictly increasing with degree."""
        generators = ['a', 'b']
        result = alternator_quotient_dimension(generators, max_degree=4)
        dims = [d['quotient_dim'] for d in result['degree_data']]
        for i in range(1, len(dims)):
            assert dims[i] > dims[i - 1], (
                f"Quotient dimension not strictly increasing: {dims}"
            )

    def test_alternator_ideal_nonempty(self):
        """Alternator ideal has elements at degree >= 2."""
        generators = ['a', 'b']
        for deg in range(2, 5):
            ideal = alternator_ideal_generators(generators, deg)
            assert len(ideal) > 0, (
                f"Alternator ideal empty at degree {deg}"
            )

    def test_alternator_ideal_empty_degree_1(self):
        """Alternator ideal is empty at degree 1 (single generators)."""
        generators = ['a', 'b']
        ideal = alternator_ideal_generators(generators, 1)
        assert len(ideal) == 0


# ---------------------------------------------------------------------------
# COPBW vs PBW tests
# ---------------------------------------------------------------------------

class TestCOPBWvsPBW:
    """Tests for the COPBW vs PBW basis comparison."""

    def test_copbw_larger_than_pbw(self):
        """COPBW dimension exceeds PBW dimension for degree >= 3."""
        result = copbw_vs_pbw_comparison(k=2, max_degree=6)
        for i, deg in enumerate(result['degrees']):
            if deg >= 3:
                assert result['copbw_dims'][i] > result['pbw_dims'][i], (
                    f"At degree {deg}: COPBW={result['copbw_dims'][i]} "
                    f"not > PBW={result['pbw_dims'][i]}"
                )

    def test_copbw_ratio_grows(self):
        """Ratio COPBW/PBW strictly increases with degree (for degree >= 2)."""
        result = copbw_vs_pbw_comparison(k=2, max_degree=6)
        ratios = result['ratios']
        # From degree 2 onward, ratio should increase
        for i in range(2, len(ratios)):
            assert ratios[i] > ratios[i - 1], (
                f"Ratio not increasing at degree {result['degrees'][i]}: "
                f"{ratios[i]} <= {ratios[i - 1]}"
            )

    def test_copbw_degree_1_equal(self):
        """At degree 1, COPBW and PBW have the same dimension (= k)."""
        result = copbw_vs_pbw_comparison(k=2, max_degree=3)
        assert result['copbw_dims'][0] == result['pbw_dims'][0] == 2

    def test_copbw_known_values(self):
        """Verify known COPBW dimensions for k=2."""
        result = copbw_vs_pbw_comparison(k=2, max_degree=5)
        # C_0*2^1=2, C_1*2^2=4, C_2*2^3=16, C_3*2^4=80, C_4*2^5=448
        expected_copbw = [2, 4, 16, 80, 448]
        for i, exp in enumerate(expected_copbw):
            assert result['copbw_dims'][i] == exp, (
                f"Degree {i+1}: expected COPBW={exp}, got {result['copbw_dims'][i]}"
            )


# ---------------------------------------------------------------------------
# Full interderivability proof test
# ---------------------------------------------------------------------------

class TestFullProof:
    """Integration test: all interderivability checks pass together."""

    def test_full_interderivability_proof(self):
        """
        Complete proof that:
        1. All structures are interderivable (single class)
        2. Triangle inequality holds
        3. Quotient is non-trivial at all tested degrees
        4. COPBW strictly exceeds PBW for degree >= 3
        """
        # (1) Single interderivability class
        classes = interderivability_classes(max_depth=20)
        assert len(classes) == 1, f"Not a single class: {classes}"

        # (2) Triangle inequality
        consistency = verify_derivation_consistency(max_depth=10)
        assert consistency['consistent'], (
            f"Violations: {consistency['triangle_violations']}"
        )

        # (3) Quotient non-triviality
        proof = quotient_nontriviality_proof(max_degree=4)
        assert proof['nontrivial'], (
            f"Quotient trivial at some degree: {proof['proof_details']}"
        )
        assert proof['growth_rate'] > 1.0, (
            f"Quotient not growing: rate={proof['growth_rate']}"
        )

        # (4) COPBW > PBW for high degrees
        comparison = copbw_vs_pbw_comparison(k=2, max_degree=5)
        for i, deg in enumerate(comparison['degrees']):
            if deg >= 3:
                assert comparison['copbw_dims'][i] > comparison['pbw_dims'][i]

        # (5) Derivability matrix has all finite entries
        dm = derivability_matrix()
        assert np.all(np.isfinite(dm['matrix'])), "Some derivation depths are infinite"
        assert dm['max_finite_depth'] > 0
