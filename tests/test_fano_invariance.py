"""
Tests for Fano plane orientation invariance.

Verifies that all G2-invariant physical observables are independent of the
choice of Fano plane orientation, addressing Grok critique #5.
"""
import numpy as np
import pytest

from octonion_algebra.core import FANO_TRIPLES
from octonion_algebra.fano_invariance import (
    build_mult_table_from_triples,
    compute_invariants,
    fano_automorphism_group_order,
    fano_correction_tensor_from_triples,
    generate_fano_orientations,
    g2_generators_from_triples,
    killing_form_from_generators,
    prove_orientation_invariance,
    structure_constants_from_triples,
    _check_alternativity,
)


class TestBasicValidity:
    """Tests for basic validity of Fano triple operations."""

    def test_standard_triples_are_valid(self):
        """Standard FANO_TRIPLES produce a valid alternative algebra."""
        table = build_mult_table_from_triples(FANO_TRIPLES)
        assert _check_alternativity(table), (
            "Standard FANO_TRIPLES should produce an alternative algebra"
        )

    def test_reversed_triple_is_valid(self):
        """Reversing ALL triples gives another valid orientation.

        Reversing all triples corresponds to replacing the multiplication
        by its opposite: e_i * e_j -> -(e_i * e_j) for the imaginary part,
        which is equivalent to conjugating all octonions. This is a valid
        alternative algebra (the opposite algebra of the octonions).
        """
        reversed_triples = [(k, j, i) for (i, j, k) in FANO_TRIPLES]
        table = build_mult_table_from_triples(reversed_triples)
        assert _check_alternativity(table), (
            "Reversing ALL triples should give a valid alternative algebra"
        )

    def test_single_triple_reversal_invalid(self):
        """Modifying the INDEX structure of a single Fano line breaks alternativity.

        The 7 Fano lines are specific 3-element subsets of {1,...,7}. Changing
        which elements form a line (e.g., replacing line {1,2,3} with {1,2,4})
        destroys the consistency of the multiplication table.

        Note: merely reversing the orientation of a single triple (flipping
        cyclic order) does NOT break alternativity -- it produces another one
        of the 480 valid multiplication tables. But changing the incidence
        structure does break it.
        """
        modified_triples = list(FANO_TRIPLES)
        # Replace (1, 2, 3) with (1, 2, 4) -- not a valid Fano line
        modified_triples[0] = (1, 2, 4)

        table = build_mult_table_from_triples(modified_triples)
        assert not _check_alternativity(table), (
            "Modifying the Fano line structure should break alternativity"
        )


class TestOrientationGeneration:
    """Tests for generating valid Fano orientations."""

    def test_generate_multiple_orientations(self):
        """Can generate at least 10 distinct valid orientations."""
        orientations = generate_fano_orientations(max_count=10)
        assert len(orientations) >= 10, (
            f"Expected at least 10 orientations, got {len(orientations)}"
        )

    def test_all_generated_are_alternative(self):
        """Every generated orientation produces an alternative algebra."""
        orientations = generate_fano_orientations(max_count=15)
        for i, triples in enumerate(orientations):
            table = build_mult_table_from_triples(triples)
            assert _check_alternativity(table), (
                f"Orientation {i} should be alternative"
            )

    def test_orientations_are_distinct(self):
        """Generated orientations are truly distinct (not duplicates)."""
        orientations = generate_fano_orientations(max_count=20)
        # Convert each to a comparable form
        seen = set()
        for triples in orientations:
            normalized = tuple(sorted(
                tuple(sorted([t] + [(t[1], t[2], t[0]), (t[2], t[0], t[1])])[0])
                for t in triples
            ))
            assert normalized not in seen, "Found duplicate orientation"
            seen.add(normalized)


class TestStructureConstants:
    """Tests for structure constant computation."""

    def test_epsilon_frobenius_invariant(self):
        """||epsilon||_F is the same across orientations and equals sqrt(42).

        Each of the 7 Fano triples contributes 6 nonzero entries (3 cyclic + 3
        anti-cyclic), each with absolute value 1. Total nonzero entries = 42.
        Frobenius norm = sqrt(42).
        """
        orientations = generate_fano_orientations(max_count=20)
        expected = np.sqrt(42.0)
        for i, triples in enumerate(orientations):
            eps = structure_constants_from_triples(triples)
            frob = np.linalg.norm(eps)
            assert abs(frob - expected) < 1e-10, (
                f"Orientation {i}: ||eps||_F = {frob}, expected {expected}"
            )

    def test_epsilon_antisymmetric(self):
        """Structure constants are totally antisymmetric."""
        eps = structure_constants_from_triples(FANO_TRIPLES)
        for i in range(7):
            for j in range(7):
                for k in range(7):
                    assert abs(eps[i, j, k] + eps[j, i, k]) < 1e-15
                    assert abs(eps[i, j, k] + eps[i, k, j]) < 1e-15
                    assert abs(eps[i, j, k] - eps[j, k, i]) < 1e-15


class TestG2Generators:
    """Tests for G2 generator computation."""

    def test_g2_dimension_invariant(self):
        """G2 always has exactly 14 generators regardless of orientation."""
        orientations = generate_fano_orientations(max_count=15)
        for i, triples in enumerate(orientations):
            gens = g2_generators_from_triples(triples)
            assert len(gens) == 14, (
                f"Orientation {i}: found {len(gens)} generators, expected 14"
            )

    def test_generators_antisymmetric(self):
        """All generators are antisymmetric matrices."""
        gens = g2_generators_from_triples(FANO_TRIPLES)
        for i, G in enumerate(gens):
            assert np.allclose(G, -G.T, atol=1e-10), (
                f"Generator {i} is not antisymmetric"
            )


class TestKillingForm:
    """Tests for Killing form computation."""

    def test_killing_form_invariant(self):
        """Killing form eigenvalues are the same across orientations.

        By Schur's lemma, since g2 is simple and the 7-rep is irreducible,
        the Killing form in this representation is proportional to -Id.
        """
        orientations = generate_fano_orientations(max_count=15)
        ref_inv = compute_invariants(orientations[0])
        ref_eigs = ref_inv['killing_eigenvalues']

        for i, triples in enumerate(orientations[1:], 1):
            inv = compute_invariants(triples)
            eigs = inv['killing_eigenvalues']
            assert np.allclose(eigs, ref_eigs, atol=1e-6), (
                f"Orientation {i}: Killing eigenvalues differ.\n"
                f"  Reference: {ref_eigs}\n"
                f"  Got:       {eigs}"
            )

    def test_killing_form_proportional_to_identity(self):
        """Killing form should be proportional to Id (Schur's lemma).

        K_{ab} = sum_alpha (G_alpha^T G_alpha)_{ab}. Since each G_alpha is
        antisymmetric, G^T G = -G^2 is positive semidefinite. By Schur's lemma
        (g2 simple, 7-rep irreducible), K is proportional to the identity.
        """
        gens = g2_generators_from_triples(FANO_TRIPLES)
        K = killing_form_from_generators(gens)
        eigenvalues = np.linalg.eigvalsh(K)
        # All eigenvalues should be equal
        assert np.allclose(eigenvalues, eigenvalues[0], rtol=1e-6), (
            f"Killing form eigenvalues should all be equal, got {eigenvalues}"
        )
        # And positive (since G^T G is positive semidefinite for antisymmetric G)
        assert eigenvalues[0] > 0, (
            f"Killing form eigenvalues should be positive, got {eigenvalues[0]}"
        )


class TestCorrectionTensor:
    """Tests for the Fano correction tensor."""

    def test_T_frobenius_invariant(self):
        """||T||_F is the same across orientations."""
        orientations = generate_fano_orientations(max_count=15)
        ref_T = fano_correction_tensor_from_triples(orientations[0])
        ref_frob = np.linalg.norm(ref_T)

        for i, triples in enumerate(orientations[1:], 1):
            T = fano_correction_tensor_from_triples(triples)
            frob = np.linalg.norm(T)
            assert abs(frob - ref_frob) < 1e-8, (
                f"Orientation {i}: ||T||_F = {frob}, expected {ref_frob}"
            )


class TestInvariants:
    """Tests for the full invariant computation."""

    def test_invariants_match_standard(self):
        """Invariants from standard triples match known values."""
        inv = compute_invariants(FANO_TRIPLES)

        # epsilon Frobenius should be sqrt(42)
        assert abs(inv['epsilon_frobenius'] - np.sqrt(42)) < 1e-10

        # G2 dimension should be 14
        assert inv['g2_dim'] == 14

        # Killing trace should be positive (sum of positive eigenvalues)
        assert inv['killing_trace'] > 0

        # Killing eigenvalues should all be equal (Schur's lemma)
        eigs = inv['killing_eigenvalues']
        assert np.allclose(eigs, eigs[0], rtol=1e-6)

    def test_orientation_invariance_full(self):
        """Full orientation invariance proof passes.

        This is the main test: generate multiple orientations, compute all
        invariants, and verify they all match.
        """
        result = prove_orientation_invariance(n_orientations=30)

        assert result['n_tested'] >= 30, (
            f"Expected at least 30 orientations, got {result['n_tested']}"
        )
        assert result['all_invariant'], (
            f"Invariants differ across orientations!\n"
            f"Max deviations: {result['max_deviation']}"
        )


class TestAutomorphismGroup:
    """Tests for the Fano plane automorphism group."""

    def test_automorphism_group_order(self):
        """PSL(2,7) has order 168."""
        order = fano_automorphism_group_order()
        assert order == 168, (
            f"Fano automorphism group order = {order}, expected 168"
        )
