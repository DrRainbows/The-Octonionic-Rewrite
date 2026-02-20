"""
Tests for G2 -> SU(3) -> SU(2) x U(1) branching chain.

Verifies the explicit decomposition of G2 representations under the
Standard Model subgroup chain, addressing Grok critique #10.
"""

import numpy as np
import pytest
from octonion_algebra.g2 import g2_generators
from octonion_algebra.g2_unification import (
    su3_subalgebra,
    verify_su3_commutation,
    branching_7_rep,
    branching_14_rep,
    su2_u1_subalgebra,
    hypercharge_assignment,
    weinberg_angle_prediction,
    g2_branching_summary,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture(scope="module")
def g2_gens():
    """G2 generators (computed once per module)."""
    return g2_generators()


@pytest.fixture(scope="module")
def su3_gens():
    """SU(3) generators extracted from G2 (stabilizing e7)."""
    return su3_subalgebra(stabilized_index=6)


@pytest.fixture(scope="module")
def su3_check(su3_gens):
    """Commutation relation verification for SU(3) generators."""
    return verify_su3_commutation(su3_gens)


@pytest.fixture(scope="module")
def branch7():
    """7-rep branching under SU(3)."""
    return branching_7_rep(stabilized_index=6)


@pytest.fixture(scope="module")
def branch14():
    """14-rep branching under SU(3)."""
    return branching_14_rep(stabilized_index=6)


@pytest.fixture(scope="module")
def su2_u1(su3_gens):
    """SU(2) x U(1) decomposition of SU(3)."""
    return su2_u1_subalgebra(su3_gens)


@pytest.fixture(scope="module")
def summary():
    """Full branching summary."""
    return g2_branching_summary(stabilized_index=6)


# ===========================================================================
# TestSU3Extraction
# ===========================================================================

class TestSU3Extraction:
    """Tests for the extraction of SU(3) subset G2."""

    def test_su3_correct_count(self, su3_gens):
        """SU(3) has exactly 8 generators (dim SU(3) = 8)."""
        assert len(su3_gens) == 8, f"Expected 8 SU(3) generators, got {len(su3_gens)}"

    def test_su3_generators_antisymmetric(self, su3_gens):
        """Each SU(3) generator is a 7x7 antisymmetric matrix."""
        for i, T in enumerate(su3_gens):
            assert T.shape == (7, 7), f"Generator {i} has wrong shape {T.shape}"
            np.testing.assert_allclose(
                T, -T.T, atol=1e-10,
                err_msg=f"SU(3) generator {i} is not antisymmetric"
            )

    def test_su3_preserve_e7(self, su3_gens):
        """Each SU(3) generator annihilates e7 (stabilized direction)."""
        e7 = np.zeros(7)
        e7[6] = 1.0
        for i, T in enumerate(su3_gens):
            result = T @ e7
            np.testing.assert_allclose(
                result, np.zeros(7), atol=1e-10,
                err_msg=f"SU(3) generator {i} does not annihilate e7"
            )

    def test_su3_commutators_close(self, su3_check):
        """Commutators of SU(3) generators close within the algebra."""
        assert su3_check['is_valid'], (
            f"SU(3) commutators do not close, max error = {su3_check['max_error']}"
        )

    def test_su3_commutation_error_small(self, su3_check):
        """Commutation closure error is below 1e-6."""
        assert su3_check['max_error'] < 1e-6, (
            f"Commutation error {su3_check['max_error']} exceeds tolerance"
        )

    def test_su3_linearly_independent(self, su3_gens):
        """The 8 SU(3) generators are linearly independent."""
        gen_vecs = np.array([g.flatten() for g in su3_gens])
        rank = np.linalg.matrix_rank(gen_vecs, tol=1e-10)
        assert rank == 8, f"Expected rank 8, got {rank}"

    def test_su3_within_g2(self, su3_gens, g2_gens):
        """Each SU(3) generator lies in the span of G2 generators."""
        g2_vecs = np.array([g.flatten() for g in g2_gens])
        for i, T in enumerate(su3_gens):
            t_vec = T.flatten()
            coeffs, _, _, _ = np.linalg.lstsq(g2_vecs.T, t_vec, rcond=None)
            reconstructed = g2_vecs.T @ coeffs
            error = np.max(np.abs(t_vec - reconstructed))
            assert error < 1e-8, (
                f"SU(3) gen {i} not in span of G2, error = {error}"
            )


# ===========================================================================
# TestBranching7
# ===========================================================================

class TestBranching7:
    """Tests for the 7-rep decomposition: 7 -> 1 + 3 + 3-bar."""

    def test_dimensions_sum_to_7(self, branch7):
        """Dimensions sum to 7: 1 + 3 + 3 = 7."""
        total = branch7['singlet_dim'] + branch7['triplet_dim'] + branch7['anti_triplet_dim']
        assert total == 7, f"Dimensions sum to {total}, expected 7"

    def test_singlet_is_1(self, branch7):
        """Singlet has dimension 1."""
        assert branch7['singlet_dim'] == 1

    def test_triplet_is_3(self, branch7):
        """Triplet has dimension 3."""
        assert branch7['triplet_dim'] == 3

    def test_anti_triplet_is_3(self, branch7):
        """Anti-triplet has dimension 3."""
        assert branch7['anti_triplet_dim'] == 3

    def test_projections_orthogonal(self, branch7):
        """Projection matrices are mutually orthogonal."""
        P1 = branch7['singlet_projection']
        P3 = branch7['triplet_projection']
        P3bar = branch7['anti_triplet_projection']

        # P1 * P3 = 0
        np.testing.assert_allclose(
            P1 @ P3, np.zeros((7, 7)), atol=1e-8,
            err_msg="Singlet and triplet projections not orthogonal"
        )
        # P1 * P3bar = 0
        np.testing.assert_allclose(
            P1 @ P3bar, np.zeros((7, 7)), atol=1e-8,
            err_msg="Singlet and anti-triplet projections not orthogonal"
        )
        # P3 * P3bar = 0
        np.testing.assert_allclose(
            P3 @ P3bar, np.zeros((7, 7)), atol=1e-8,
            err_msg="Triplet and anti-triplet projections not orthogonal"
        )

    def test_projections_sum_to_identity(self, branch7):
        """Projections sum to the identity: P1 + P3 + P3bar = I_7."""
        P1 = branch7['singlet_projection']
        P3 = branch7['triplet_projection']
        P3bar = branch7['anti_triplet_projection']

        np.testing.assert_allclose(
            P1 + P3 + P3bar, np.eye(7), atol=1e-8,
            err_msg="Projections do not sum to identity"
        )

    def test_projections_are_idempotent(self, branch7):
        """Each projection matrix satisfies P^2 = P."""
        for name in ['singlet_projection', 'triplet_projection', 'anti_triplet_projection']:
            P = branch7[name]
            np.testing.assert_allclose(
                P @ P, P, atol=1e-8,
                err_msg=f"{name} is not idempotent"
            )

    def test_singlet_is_stabilized_direction(self, branch7):
        """Singlet projection projects onto e7."""
        P1 = branch7['singlet_projection']
        e7 = np.zeros(7)
        e7[6] = 1.0
        np.testing.assert_allclose(
            P1 @ e7, e7, atol=1e-10,
            err_msg="Singlet does not project onto e7"
        )


# ===========================================================================
# TestBranching14
# ===========================================================================

class TestBranching14:
    """Tests for the adjoint 14-rep decomposition: 14 -> 8 + 3 + 3-bar."""

    def test_dimensions_sum_to_14(self, branch14):
        """Dimensions sum to 14: 8 + 3 + 3 = 14."""
        total = branch14['adjoint_dim'] + branch14['triplet_dim'] + branch14['anti_triplet_dim']
        assert total == 14, f"Dimensions sum to {total}, expected 14"

    def test_adjoint_is_8(self, branch14):
        """Adjoint (SU(3) part) has dimension 8."""
        assert branch14['adjoint_dim'] == 8

    def test_coset_is_6(self, branch14):
        """Coset space has dimension 6 = 14 - 8."""
        assert branch14['coset_dim'] == 6, (
            f"Coset dimension is {branch14['coset_dim']}, expected 6"
        )


# ===========================================================================
# TestSU2U1
# ===========================================================================

class TestSU2U1:
    """Tests for SU(3) -> SU(2) x U(1) decomposition."""

    def test_su2_has_3_generators(self, su2_u1):
        """SU(2) has exactly 3 generators."""
        assert len(su2_u1['su2_generators']) == 3, (
            f"Expected 3 SU(2) generators, got {len(su2_u1['su2_generators'])}"
        )

    def test_u1_generator_exists(self, su2_u1):
        """A U(1) generator is found."""
        assert su2_u1['u1_generator'] is not None

    def test_su2_closes(self, su2_u1):
        """SU(2) generators close under commutation."""
        assert su2_u1['is_valid'], (
            f"SU(2) does not close, error = {su2_u1['su2_commutation_error']}"
        )

    def test_su2_generators_antisymmetric(self, su2_u1):
        """SU(2) generators are antisymmetric."""
        for i, T in enumerate(su2_u1['su2_generators']):
            np.testing.assert_allclose(
                T, -T.T, atol=1e-10,
                err_msg=f"SU(2) generator {i} is not antisymmetric"
            )

    def test_su2_commutation_structure(self, su2_u1):
        """SU(2) commutators have the form [T_a, T_b] = sum_c f_abc T_c."""
        gens = su2_u1['su2_generators']
        gen_vecs = np.array([g.flatten() for g in gens])

        for a in range(3):
            for b in range(a + 1, 3):
                comm = gens[a] @ gens[b] - gens[b] @ gens[a]
                comm_vec = comm.flatten()
                coeffs, _, _, _ = np.linalg.lstsq(gen_vecs.T, comm_vec, rcond=None)
                reconstructed = gen_vecs.T @ coeffs
                error = np.max(np.abs(comm_vec - reconstructed))
                assert error < 1e-6, (
                    f"[T_{a}, T_{b}] not in SU(2) span, error = {error}"
                )


# ===========================================================================
# TestWeinbergAngle
# ===========================================================================

class TestWeinbergAngle:
    """Tests for the Weinberg angle prediction."""

    def test_sin2_theta_w_is_3_over_8(self):
        """sin^2(theta_W) = 3/8 at unification."""
        result = weinberg_angle_prediction()
        np.testing.assert_allclose(
            result['sin2_theta_W'], 3.0 / 8.0, atol=1e-10,
            err_msg="Weinberg angle prediction differs from 3/8"
        )

    def test_trace_ratio_matches(self):
        """Trace ratio equals 3/8."""
        result = weinberg_angle_prediction()
        np.testing.assert_allclose(
            result['trace_ratio'], 3.0 / 8.0, atol=1e-10,
            err_msg="Trace ratio differs from 3/8"
        )

    def test_derivation_steps_present(self):
        """Derivation steps are provided and non-empty."""
        result = weinberg_angle_prediction()
        assert len(result['derivation_steps']) > 0, "No derivation steps"
        for step in result['derivation_steps']:
            assert isinstance(step, str) and len(step) > 0


# ===========================================================================
# TestFullChain
# ===========================================================================

class TestFullChain:
    """Tests for the complete branching chain summary."""

    def test_g2_dim_14(self, summary):
        """G2 has 14 generators."""
        assert summary['g2']['dim'] == 14

    def test_su3_dim_8_in_summary(self, summary):
        """SU(3) has 8 generators in the summary."""
        assert summary['su3']['dim'] == 8

    def test_branching_7_total(self, summary):
        """7-rep branching dimensions: 1 + 3 + 3 = 7."""
        b7 = summary['branching_7']
        assert b7['1'] + b7['3'] + b7['3_bar'] == 7

    def test_branching_14_total(self, summary):
        """14-rep branching dimensions: 8 + 3 + 3 = 14."""
        b14 = summary['branching_14']
        assert b14['8'] + b14['3'] + b14['3_bar'] == 14

    def test_weinberg_in_summary(self, summary):
        """Weinberg angle in summary matches 3/8."""
        np.testing.assert_allclose(
            summary['weinberg_angle']['sin2_theta_W'],
            summary['weinberg_angle']['expected'],
            atol=1e-10,
        )

    def test_all_cross_checks_pass(self, summary):
        """All cross-checks in the summary pass."""
        for key, val in summary['cross_checks'].items():
            assert val, f"Cross-check '{key}' failed"

    def test_summary_all_checks_flag(self, summary):
        """The all_checks_pass flag is True."""
        assert summary['all_checks_pass'], "Not all checks pass in summary"


# ===========================================================================
# TestAlternativeStabilizers
# ===========================================================================

class TestAlternativeStabilizers:
    """Test that the construction works for different stabilized directions."""

    def test_stabilize_e1(self):
        """Stabilizing e1 (index 0) also yields 8 SU(3) generators."""
        gens = su3_subalgebra(stabilized_index=0)
        assert len(gens) == 8, f"Expected 8, got {len(gens)}"

    def test_stabilize_e4(self):
        """Stabilizing e4 (index 3) also yields 8 SU(3) generators."""
        gens = su3_subalgebra(stabilized_index=3)
        assert len(gens) == 8, f"Expected 8, got {len(gens)}"
