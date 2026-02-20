"""
Extended tests for numerical predictions from the octonionic framework.

Each test verifies that a prediction function returns computed values with
the correct types, shapes, and mathematical properties.
"""
import numpy as np
import pytest

from octonion_algebra.predictions import (
    fano_tensor_spectral_decomposition,
    s_na_magnitude_scaling,
    hydrogen_7d_spectrum,
    copbw_growth_asymptotics,
    coherence_charge_scaling,
    hawking_temperature_table,
    g2_branching_verification,
    double_curl_spectral_gap,
    weinberg_angle_prediction,
    falsification_experiments,
)


# ===================================================================
# 1. Fano tensor spectral decomposition
# ===================================================================

class TestFanoTensorSpectral:
    """Tests for fano_tensor_spectral_decomposition."""

    @pytest.fixture(scope="class")
    def result(self):
        return fano_tensor_spectral_decomposition()

    def test_returns_dict_with_expected_keys(self, result):
        expected_keys = {
            'eigenvalues', 'frobenius_norm', 'rank', 'n_nonzero',
            'trace', 'max_eigenvalue', 'min_eigenvalue',
        }
        assert expected_keys.issubset(result.keys())

    def test_eigenvalues_shape(self, result):
        """The 49x49 matrix has exactly 49 eigenvalues."""
        assert result['eigenvalues'].shape == (49,)

    def test_eigenvalues_sorted(self, result):
        eigs = result['eigenvalues']
        assert np.all(eigs[:-1] <= eigs[1:] + 1e-12)

    def test_rank_is_positive(self, result):
        """The Fano tensor is nonzero, so rank > 0."""
        assert result['rank'] > 0

    def test_rank_equals_n_nonzero(self, result):
        assert result['rank'] == result['n_nonzero']

    def test_frobenius_norm_positive(self, result):
        assert result['frobenius_norm'] > 0

    def test_trace_is_finite(self, result):
        assert np.isfinite(result['trace'])

    def test_eigenvalues_are_real(self, result):
        """eigh guarantees real eigenvalues; verify no NaN."""
        assert np.all(np.isfinite(result['eigenvalues']))


# ===================================================================
# 2. S_NA magnitude scaling
# ===================================================================

class TestSNAScaling:
    """Tests for s_na_magnitude_scaling."""

    @pytest.fixture(scope="class")
    def result(self):
        return s_na_magnitude_scaling(N_values=[8, 12, 16])

    def test_returns_dict_with_expected_keys(self, result):
        assert 'N_values' in result
        assert 'ratios' in result
        assert 'extrapolated_continuum_limit' in result

    def test_ratios_are_positive(self, result):
        """S_NA / omega > 0 for genuinely 7D fields."""
        for r in result['ratios']:
            assert r > 0, f"Expected positive ratio, got {r}"

    def test_ratios_are_consistent(self, result):
        """Ratios should be O(1) and not diverge with grid refinement."""
        for r in result['ratios']:
            assert 0.01 < r < 100, f"Ratio {r} out of expected range"

    def test_continuum_limit_is_positive(self, result):
        assert result['extrapolated_continuum_limit'] > 0


# ===================================================================
# 3. Hydrogen 7D spectrum
# ===================================================================

class TestHydrogen7D:
    """Tests for hydrogen_7d_spectrum."""

    @pytest.fixture(scope="class")
    def result(self):
        return hydrogen_7d_spectrum(n_max=5)

    def test_returns_correct_n_values(self, result):
        assert result['n_values'] == [1, 2, 3, 4, 5]

    def test_3d_ground_state(self, result):
        """E_1(3D) = -1/2."""
        assert result['E_3d'][0] == pytest.approx(-0.5, abs=1e-14)

    def test_7d_ground_state(self, result):
        """E_1(7D) = -1/(2*(1+2)^2) = -1/18."""
        assert result['E_7d'][0] == pytest.approx(-1.0 / 18.0, abs=1e-14)

    def test_correction_ratios_less_than_one(self, result):
        """7D energies are less negative than 3D for all n,
        so |E_7d/E_3d| < 1, i.e., 0 < ratio < 1."""
        for r in result['correction_ratios']:
            assert 0 < r < 1, f"ratio = {r}, expected between 0 and 1"

    def test_correction_ratio_n1(self, result):
        """For n=1: E_7d/E_3d = (-1/18) / (-1/2) = 1/9."""
        assert result['correction_ratios'][0] == pytest.approx(1.0 / 9.0, abs=1e-14)

    def test_solid_angle_s2(self, result):
        """Area of S^2 = 4*pi."""
        assert result['solid_angle_S2'] == pytest.approx(4 * np.pi, abs=1e-10)

    def test_solid_angle_s6(self, result):
        """Area of S^6 = 16*pi^3/15."""
        expected = 16 * np.pi ** 3 / 15.0
        assert result['solid_angle_S6'] == pytest.approx(expected, abs=1e-8)


# ===================================================================
# 4. COPBW growth asymptotics
# ===================================================================

class TestCOPBWGrowth:
    """Tests for copbw_growth_asymptotics."""

    @pytest.fixture(scope="class")
    def result(self):
        return copbw_growth_asymptotics(k=2, n_max=10)

    def test_copbw_dim_at_n1(self, result):
        """At n=1: dim = k^1 * C_0 = 2*1 = 2."""
        assert result['copbw_dims'][0] == 2

    def test_copbw_dim_at_n2(self, result):
        """At n=2: dim = k^2 * C_1 = 4*1 = 4."""
        assert result['copbw_dims'][1] == 4

    def test_copbw_dim_at_n3(self, result):
        """At n=3: dim = k^3 * C_2 = 8*2 = 16."""
        assert result['copbw_dims'][2] == 16

    def test_copbw_exceeds_pbw(self, result):
        """For n >= 3, COPBW dimension exceeds PBW dimension."""
        for i in range(2, len(result['n_values'])):
            assert result['copbw_dims'][i] > result['pbw_dims'][i], (
                f"n={result['n_values'][i]}: COPBW={result['copbw_dims'][i]} "
                f"<= PBW={result['pbw_dims'][i]}"
            )

    def test_ratio_grows_monotonically(self, result):
        """The ratio COPBW/PBW should grow with n (for n >= 2)."""
        ratios = result['ratios']
        for i in range(2, len(ratios)):
            assert ratios[i] >= ratios[i - 1] - 1e-10, (
                f"Ratio decreased at n={result['n_values'][i]}"
            )

    def test_catalan_asymptotic_converges(self, result):
        """The asymptotic approximation C_n ~ 4^n / sqrt(pi*n^3) should
        converge to a ratio near 1 for large n."""
        assert result['asymptotic_converges']


# ===================================================================
# 5. Coherence charge scaling
# ===================================================================

class TestCoherenceChargeScaling:
    """Tests for coherence_charge_scaling."""

    @pytest.fixture(scope="class")
    def result(self):
        return coherence_charge_scaling(N_values=[10, 20, 40, 80], n_samples=30)

    def test_mean_Q_increases_with_N(self, result):
        """Q_C should increase with N."""
        for i in range(1, len(result['mean_Q'])):
            assert result['mean_Q'][i] > result['mean_Q'][i - 1]

    def test_Q_per_triple_roughly_constant(self, result):
        """Q_C / (N-2) should be roughly constant (linear scaling)."""
        qpt = result['Q_per_triple']
        # All values should be within a factor of 3 of each other
        assert max(qpt) / min(qpt) < 3.0, (
            f"Q per triple varies too much: {qpt}"
        )

    def test_linear_fit_r_squared(self, result):
        """Linear fit should have R^2 > 0.99 (excellent linear scaling)."""
        assert result['r_squared'] > 0.99, (
            f"R^2 = {result['r_squared']}, expected > 0.99"
        )

    def test_positive_slope(self, result):
        """The slope of Q vs N should be positive."""
        assert result['linear_fit_slope'] > 0


# ===================================================================
# 6. Hawking temperature table
# ===================================================================

class TestHawkingTemperature:
    """Tests for hawking_temperature_table."""

    @pytest.fixture(scope="class")
    def result(self):
        return hawking_temperature_table(d_max=7)

    def test_d_values(self, result):
        assert result['d_values'] == [3, 4, 5, 6, 7]

    def test_T_ratios_are_exact_integers(self, result):
        """T_H(d)/T_H(3) = d-2, which is an integer."""
        expected = [1, 2, 3, 4, 5]
        assert result['T_ratios'] == expected

    def test_T_ratio_d7_is_5(self, result):
        """T_H(7D) / T_H(3D) = 5."""
        idx_7 = result['d_values'].index(7)
        assert result['T_ratios'][idx_7] == 5

    def test_metric_exponents(self, result):
        """Metric exponent = d-2."""
        expected = [1, 2, 3, 4, 5]
        assert result['metric_exponents'] == expected

    def test_solid_angle_d3(self, result):
        """Omega_2 = 4*pi (surface area of S^2)."""
        idx_3 = result['d_values'].index(3)
        assert result['solid_angles'][idx_3] == pytest.approx(4 * np.pi, abs=1e-10)

    def test_spacetime_dims(self, result):
        expected = [4, 5, 6, 7, 8]
        assert result['spacetime_dims'] == expected


# ===================================================================
# 7. G2 branching verification
# ===================================================================

class TestG2Branching:
    """Tests for g2_branching_verification."""

    @pytest.fixture(scope="class")
    def result(self):
        return g2_branching_verification()

    def test_g2_dim_is_14(self, result):
        assert result['g2_dim'] == 14

    def test_su3_stabiliser_dim_is_8(self, result):
        assert result['su3_stabiliser_dim'] == 8

    def test_coset_dim_is_6(self, result):
        assert result['coset_dim'] == 6

    def test_dims_sum(self, result):
        """14 = 8 + 6."""
        assert result['su3_stabiliser_dim'] + result['coset_dim'] == result['g2_dim']

    def test_dims_verified(self, result):
        assert result['dims_verified']

    def test_branching_14_string(self, result):
        assert result['branching_14'] == "14 = 8 + 6"


# ===================================================================
# 8. Double-curl spectral gap
# ===================================================================

class TestDoubleCurlSpectralGap:
    """Tests for double_curl_spectral_gap."""

    @pytest.fixture(scope="class")
    def result(self):
        return double_curl_spectral_gap(N=16, dx=0.3)

    def test_returns_dict_with_expected_keys(self, result):
        keys = {'frequencies', 'relative_remainders', 'max_remainder',
                'min_remainder', 'mean_remainder', 'fano_tensor_nonzero',
                'fano_tensor_norm'}
        assert keys.issubset(result.keys())

    def test_frequencies_positive(self, result):
        for f in result['frequencies']:
            assert f > 0

    def test_fano_tensor_is_nonzero(self, result):
        """The Fano correction tensor must be nonzero."""
        assert result['fano_tensor_nonzero']
        assert result['fano_tensor_norm'] > 1.0

    def test_remainders_are_non_negative(self, result):
        """Non-associative remainder should be >= 0."""
        for r in result['relative_remainders']:
            assert r >= 0, f"Expected non-negative remainder, got {r}"

    def test_mean_remainder_is_finite(self, result):
        """Mean relative remainder should be a reasonable finite number."""
        assert np.isfinite(result['mean_remainder'])
        assert result['mean_remainder'] < 1000


# ===================================================================
# 9. Weinberg angle prediction
# ===================================================================

class TestWeinbergAngle:
    """Tests for weinberg_angle_prediction."""

    @pytest.fixture(scope="class")
    def result(self):
        return weinberg_angle_prediction()

    def test_tree_level_exactly_three_eighths(self, result):
        assert result['tree_level_sin2_theta_W'] == pytest.approx(0.375, abs=1e-15)

    def test_measured_value(self, result):
        assert result['measured_sin2_theta_W'] == pytest.approx(0.2312, abs=1e-10)

    def test_unification_scale_order_of_magnitude(self, result):
        """log10(M_GUT) should be roughly 14-16 GeV."""
        log10_M = result['log10_M_GUT_GeV']
        assert 10 < log10_M < 20, f"log10(M_GUT) = {log10_M}, expected 10-20"

    def test_running_coefficient_positive(self, result):
        assert result['running_coefficient'] > 0


# ===================================================================
# 10. Falsification experiments
# ===================================================================

class TestFalsificationExperiments:
    """Tests for falsification_experiments."""

    @pytest.fixture(scope="class")
    def result(self):
        return falsification_experiments()

    def test_returns_three_experiments(self, result):
        assert 'experiment_1' in result
        assert 'experiment_2' in result
        assert 'experiment_3' in result

    def test_each_experiment_has_required_fields(self, result):
        required = {'name', 'description', 'falsification_threshold',
                    'predicted_value', 'measurement_precision_needed'}
        for key in ['experiment_1', 'experiment_2', 'experiment_3']:
            assert required.issubset(result[key].keys()), (
                f"{key} missing fields: {required - set(result[key].keys())}"
            )

    def test_experiment_2_predicted_value(self, result):
        """G2 dimension must be exactly 14."""
        assert result['experiment_2']['predicted_value'] == 14
