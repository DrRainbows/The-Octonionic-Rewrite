"""
Tests for octonion_algebra.applications -- quantified application models.

Covers:
    - Octonionic Lotka-Volterra (ecological dynamics)
    - Portfolio Associator Entropy (financial systems)
    - Coalition Associator (political / game theory)
"""

import numpy as np
import pytest

from octonion_algebra.core import Octonion, FANO_TRIPLES
from octonion_algebra.associator import associator, associator_norm
from octonion_algebra.calculus import structure_constants
from octonion_algebra.applications import (
    fano_ternary_tensor,
    octonionic_lotka_volterra_rhs,
    simulate_lotka_volterra,
    lotka_volterra_comparison,
    portfolio_associator,
    associator_entropy,
    compare_quaternionic_octonionic,
    coalition_associator,
    agenda_dependence_measure,
    optimal_coalition_ordering,
)


# ===================================================================
# Helpers / Fixtures
# ===================================================================

@pytest.fixture
def lv_params():
    """Standard Lotka-Volterra parameters for 7-species system."""
    rng = np.random.default_rng(42)
    r = rng.uniform(0.1, 0.5, size=7)
    # Interaction matrix: mild competition on off-diag, self-limiting on diag
    A = -0.05 * rng.uniform(0, 1, size=(7, 7))
    np.fill_diagonal(A, -0.1)
    T = fano_ternary_tensor() * 0.01  # small ternary coupling
    x0 = rng.uniform(0.5, 1.5, size=7)
    return x0, r, A, T


@pytest.fixture
def quaternionic_assets():
    """
    Assets confined to a quaternionic subalgebra of O.
    Use the first Fano triple (1, 2, 3): span {e0, e1, e2, e3}.
    The associator vanishes identically for elements of any
    quaternionic subalgebra.
    """
    rng = np.random.default_rng(123)
    assets = []
    for _ in range(5):
        c = np.zeros(8)
        c[0] = rng.uniform(-1, 1)
        c[1] = rng.uniform(-1, 1)
        c[2] = rng.uniform(-1, 1)
        c[3] = rng.uniform(-1, 1)
        assets.append(Octonion(c))
    return assets


@pytest.fixture
def octonionic_assets():
    """Assets spanning the full octonion algebra."""
    rng = np.random.default_rng(456)
    assets = []
    for _ in range(5):
        c = rng.uniform(-1, 1, size=8)
        assets.append(Octonion(c))
    return assets


@pytest.fixture
def random_agents():
    """Random full-octonion agents for coalition tests."""
    return [Octonion.random(seed=i + 100) for i in range(5)]


@pytest.fixture
def quaternionic_agents():
    """Agents confined to quaternionic subalgebra (1, 2, 3)."""
    rng = np.random.default_rng(789)
    agents = []
    for _ in range(4):
        c = np.zeros(8)
        c[0] = rng.uniform(-1, 1)
        c[1] = rng.uniform(-1, 1)
        c[2] = rng.uniform(-1, 1)
        c[3] = rng.uniform(-1, 1)
        agents.append(Octonion(c))
    return agents


# ===================================================================
# TestLotkaVolterra
# ===================================================================

class TestLotkaVolterra:
    """Tests for the octonionic Lotka-Volterra model."""

    def test_rhs_shape(self, lv_params):
        """RHS must return a (7,) array."""
        x0, r, A, T = lv_params
        rhs = octonionic_lotka_volterra_rhs(x0, r, A, T)
        assert rhs.shape == (7,)

    def test_rhs_zero_populations(self, lv_params):
        """If all populations are zero, RHS must be zero (dx/dt = x * ...)."""
        _, r, A, T = lv_params
        x_zero = np.zeros(7)
        rhs = octonionic_lotka_volterra_rhs(x_zero, r, A, T)
        np.testing.assert_allclose(rhs, 0.0, atol=1e-15)

    def test_trajectory_shape(self, lv_params):
        """simulate_lotka_volterra must return (n_steps+1, 7)."""
        x0, r, A, T = lv_params
        n_steps = 50
        traj = simulate_lotka_volterra(x0, r, A, T, dt=0.01, n_steps=n_steps)
        assert traj.shape == (n_steps + 1, 7)

    def test_trajectory_starts_at_x0(self, lv_params):
        """The trajectory must start at the initial condition."""
        x0, r, A, T = lv_params
        traj = simulate_lotka_volterra(x0, r, A, T, dt=0.01, n_steps=10)
        np.testing.assert_allclose(traj[0], x0)

    def test_T_zero_reduces_to_standard(self, lv_params):
        """When T = 0, the octonionic model must reproduce standard LV."""
        x0, r, A, _ = lv_params
        T_zero = np.zeros((7, 7, 7))
        # Standard RHS: x * (r + A @ x)
        rhs_oct = octonionic_lotka_volterra_rhs(x0, r, A, T_zero)
        rhs_std = x0 * (r + A @ x0)
        np.testing.assert_allclose(rhs_oct, rhs_std, atol=1e-14)

    def test_trajectory_diverges_with_T(self, lv_params):
        """Trajectories must diverge when T != 0 (non-trivial ternary coupling)."""
        x0, r, A, T = lv_params
        # Use a small T_scale to keep the simulation stable while still
        # producing measurable deviation from the standard model.
        result = lotka_volterra_comparison(x0, r, A, dt=0.01, n_steps=200,
                                           T_scale=0.001)
        # The max deviation should be strictly positive
        assert result['max_deviation'] > 0.0
        # The relative difference should be measurable
        assert result['relative_difference'] > 1e-6

    def test_comparison_dict_keys(self, lv_params):
        """lotka_volterra_comparison must return the documented keys."""
        x0, r, A, _ = lv_params
        result = lotka_volterra_comparison(x0, r, A, dt=0.01, n_steps=10)
        expected_keys = {'trajectory_standard', 'trajectory_octonionic',
                         'max_deviation', 'relative_difference',
                         'trajectory_divergence_time'}
        assert set(result.keys()) == expected_keys

    def test_positive_populations_short_sim(self, lv_params):
        """For a short simulation with small coupling, populations stay positive."""
        x0, r, A, _ = lv_params
        T_small = fano_ternary_tensor() * 0.001
        traj = simulate_lotka_volterra(x0, r, A, T_small, dt=0.005, n_steps=50)
        # All populations should remain positive in this mild regime
        assert np.all(traj > 0), "Populations went negative in mild regime"


# ===================================================================
# TestPortfolioAssociator
# ===================================================================

class TestPortfolioAssociator:
    """Tests for the portfolio associator entropy model."""

    def test_associator_total_positive(self, octonionic_assets):
        """Total associator magnitude must be positive for generic octonionic assets."""
        total = portfolio_associator(octonionic_assets)
        assert total > 0.0

    def test_associator_zero_for_quaternionic(self, quaternionic_assets):
        """Total associator magnitude must vanish for quaternionic assets."""
        total = portfolio_associator(quaternionic_assets)
        assert total < 1e-10, f"Expected ~0, got {total}"

    def test_entropy_non_negative(self, octonionic_assets):
        """Associator entropy must be non-negative."""
        S = associator_entropy(octonionic_assets)
        assert S >= 0.0

    def test_entropy_zero_for_quaternionic(self, quaternionic_assets):
        """Associator entropy must be zero for quaternionic assets."""
        S = associator_entropy(quaternionic_assets)
        assert S < 1e-10, f"Expected ~0, got {S}"

    def test_entropy_increases_with_nonassociative_assets(self):
        """
        Adding more assets spanning different octonionic directions should
        (generically) increase or maintain entropy relative to a smaller set.
        """
        rng = np.random.default_rng(999)
        small_set = [Octonion(rng.uniform(-1, 1, size=8)) for _ in range(3)]
        large_set = small_set + [Octonion(rng.uniform(-1, 1, size=8)) for _ in range(3)]
        S_small = associator_entropy(small_set)
        S_large = associator_entropy(large_set)
        # With 3 assets there is exactly 1 triple, so entropy is 0 (single
        # event).  With 6 assets there are C(6,3) = 20 triples, so entropy
        # should be positive.
        assert S_large > S_small

    def test_compare_quaternionic_octonionic(self, quaternionic_assets,
                                              octonionic_assets):
        """Comparison dict must show higher entropy for octonionic assets."""
        result = compare_quaternionic_octonionic(quaternionic_assets,
                                                  octonionic_assets)
        assert result['entropy_quaternionic'] < 1e-10
        assert result['entropy_octonionic'] > 0.0
        assert result['entropy_ratio'] == float('inf')
        assert result['associator_total_quaternionic'] < 1e-10
        assert result['associator_total_octonionic'] > 0.0

    def test_too_few_assets_raises(self):
        """portfolio_associator and associator_entropy must raise for < 3 assets."""
        assets = [Octonion.random(seed=0), Octonion.random(seed=1)]
        with pytest.raises(ValueError, match="at least 3"):
            portfolio_associator(assets)
        with pytest.raises(ValueError, match="at least 3"):
            associator_entropy(assets)


# ===================================================================
# TestCoalitionAssociator
# ===================================================================

class TestCoalitionAssociator:
    """Tests for the coalition associator / agenda dependence model."""

    def test_coalition_associator_positive(self, random_agents):
        """Coalition associator must be positive for generic octonionic agents."""
        total = coalition_associator(random_agents)
        assert total > 0.0

    def test_coalition_associator_zero_for_quaternionic(self, quaternionic_agents):
        """Coalition associator must vanish for quaternionic agents."""
        total = coalition_associator(quaternionic_agents)
        assert total < 1e-10

    def test_agenda_dependence_non_negative(self, random_agents):
        """Agenda dependence measure must be non-negative."""
        d = agenda_dependence_measure(random_agents)
        assert d >= 0.0

    def test_agenda_dependence_zero_for_quaternionic(self, quaternionic_agents):
        """Agenda dependence must be ~0 for quaternionic agents."""
        d = agenda_dependence_measure(quaternionic_agents)
        assert d < 1e-10

    def test_antisymmetry_of_associator(self):
        """[a,b,c] = -[b,a,c]: swapping first two arguments negates the associator."""
        a = Octonion.random(seed=10)
        b = Octonion.random(seed=11)
        c = Octonion.random(seed=12)
        abc = associator(a, b, c)
        bac = associator(b, a, c)
        np.testing.assert_allclose(abc.coeffs, -bac.coeffs, atol=1e-12)

    def test_optimal_ordering_min_le_max(self, random_agents):
        """The minimum cost ordering must have cost <= the maximum cost ordering."""
        result = optimal_coalition_ordering(random_agents)
        assert result['min_cost'] <= result['max_cost'] + 1e-12

    def test_optimal_ordering_keys(self, random_agents):
        """optimal_coalition_ordering must return the documented keys."""
        result = optimal_coalition_ordering(random_agents)
        expected_keys = {'min_ordering', 'min_cost', 'max_ordering', 'max_cost'}
        assert set(result.keys()) == expected_keys

    def test_optimal_ordering_valid_permutations(self, random_agents):
        """Both orderings must be valid permutations of agent indices."""
        result = optimal_coalition_ordering(random_agents)
        n = len(random_agents)
        assert sorted(result['min_ordering']) == list(range(n))
        assert sorted(result['max_ordering']) == list(range(n))

    def test_too_few_agents_raises(self):
        """Functions must raise ValueError for fewer than 3 agents."""
        agents = [Octonion.random(seed=0), Octonion.random(seed=1)]
        with pytest.raises(ValueError, match="at least 3"):
            coalition_associator(agents)
        with pytest.raises(ValueError, match="at least 3"):
            agenda_dependence_measure(agents)
        with pytest.raises(ValueError, match="at least 3"):
            optimal_coalition_ordering(agents)
