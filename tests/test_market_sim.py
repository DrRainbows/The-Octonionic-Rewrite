"""
Tests for octonion_algebra.market_sim -- market/economic simulation engine.

Covers:
    - MultiAgentMarket:  conservation laws, epsilon scaling, determinism
    - PortfolioDynamics: associator entropy, ordering spread, epsilon comparison
    - EcosystemModel:    baseline reduction, ternary effects, biomass tracking

All tests are deterministic (seeded) and verify that:
    1. Conservation laws hold (total wealth / biomass preserved).
    2. epsilon=0 reproduces standard (associative) models.
    3. epsilon>0 produces measurably different dynamics.
    4. Associator magnitude scales with epsilon.
    5. Results are deterministic (same seed -> same output).
"""

import numpy as np
import pytest

from octonion_algebra.market_sim import (
    MultiAgentMarket,
    PortfolioDynamics,
    EcosystemModel,
    _deformed_associator_norm,
)
from octonion_algebra.deformation import deformed_multiply


# ===================================================================
# Fixtures
# ===================================================================

@pytest.fixture
def market_eps0():
    """MultiAgentMarket at epsilon=0 (associative)."""
    return MultiAgentMarket(n_agents=5, epsilon=0.0, seed=42)


@pytest.fixture
def market_eps1():
    """MultiAgentMarket at epsilon=1 (non-associative)."""
    return MultiAgentMarket(n_agents=5, epsilon=1.0, seed=42)


@pytest.fixture
def portfolio_eps0():
    """PortfolioDynamics at epsilon=0."""
    return PortfolioDynamics(n_assets=5, epsilon=0.0, seed=42)


@pytest.fixture
def portfolio_eps1():
    """PortfolioDynamics at epsilon=1."""
    return PortfolioDynamics(n_assets=5, epsilon=1.0, seed=42)


@pytest.fixture
def eco_eps0():
    """EcosystemModel at epsilon=0 (standard LV)."""
    return EcosystemModel(epsilon=0.0, seed=42)


@pytest.fixture
def eco_eps1():
    """EcosystemModel at epsilon=1 (non-associative LV)."""
    return EcosystemModel(epsilon=1.0, seed=42)


# ===================================================================
# Helper: _deformed_associator_norm
# ===================================================================

class TestDeformedAssociatorNorm:
    """Tests for the internal _deformed_associator_norm helper."""

    def test_zero_at_epsilon_zero_quaternionic(self):
        """
        For quaternionic inputs (only components 0-3), the associator
        at epsilon=0 must vanish.
        """
        rng = np.random.default_rng(0)
        for _ in range(10):
            a = np.zeros(8); a[:4] = rng.standard_normal(4)
            b = np.zeros(8); b[:4] = rng.standard_normal(4)
            c = np.zeros(8); c[:4] = rng.standard_normal(4)
            norm = _deformed_associator_norm(a, b, c, epsilon=0.0)
            assert norm < 1e-12, f"Expected ~0, got {norm}"

    def test_nonzero_at_epsilon_one_generic(self):
        """
        For generic 8-component inputs at epsilon=1, the associator
        should be non-zero.
        """
        rng = np.random.default_rng(1)
        a = rng.standard_normal(8)
        b = rng.standard_normal(8)
        c = rng.standard_normal(8)
        norm = _deformed_associator_norm(a, b, c, epsilon=1.0)
        assert norm > 1e-6, f"Expected > 0, got {norm}"

    def test_scales_with_epsilon(self):
        """
        Associator norm should generally increase as epsilon goes from
        0 to 1 for generic inputs.
        """
        rng = np.random.default_rng(2)
        a = rng.standard_normal(8)
        b = rng.standard_normal(8)
        c = rng.standard_normal(8)

        norms = [_deformed_associator_norm(a, b, c, eps)
                 for eps in [0.0, 0.25, 0.5, 0.75, 1.0]]

        # The norm at epsilon=1 should exceed the norm at epsilon=0
        assert norms[-1] > norms[0]

    def test_non_negative(self):
        """Associator norm must be non-negative."""
        rng = np.random.default_rng(3)
        for _ in range(20):
            a = rng.standard_normal(8)
            b = rng.standard_normal(8)
            c = rng.standard_normal(8)
            eps = rng.uniform(0, 1)
            norm = _deformed_associator_norm(a, b, c, eps)
            assert norm >= 0.0


# ===================================================================
# MultiAgentMarket
# ===================================================================

class TestMultiAgentMarket:
    """Tests for MultiAgentMarket."""

    def test_initialization_shape(self, market_eps1):
        """States must have shape (n_agents, 8)."""
        assert market_eps1.states.shape == (5, 8)

    def test_initial_wealth_positive(self, market_eps1):
        """All initial wealth values must be positive."""
        assert np.all(market_eps1.states[:, 0] > 0)

    def test_total_wealth_positive(self, market_eps1):
        """Total wealth must be positive at initialization."""
        assert market_eps1.total_wealth() > 0

    def test_wealth_conservation(self, market_eps1):
        """
        Total wealth should be conserved during evolution.
        The antisymmetric interaction rule ensures exact conservation
        of the real (wealth) component.
        """
        initial_wealth = market_eps1.total_wealth()
        result = market_eps1.evolve(steps=100, dt=0.01, coupling=0.01)
        final_wealth = result['total_wealth'][-1]
        # Allow for small numerical drift
        drift = abs(final_wealth - initial_wealth) / abs(initial_wealth)
        assert drift < 0.01, f"Wealth drift {drift:.4%} exceeds 1%"

    def test_wealth_conservation_eps0(self, market_eps0):
        """Wealth conservation also holds at epsilon=0."""
        initial_wealth = market_eps0.total_wealth()
        result = market_eps0.evolve(steps=100, dt=0.01, coupling=0.01)
        final_wealth = result['total_wealth'][-1]
        drift = abs(final_wealth - initial_wealth) / abs(initial_wealth)
        assert drift < 0.01, f"Wealth drift {drift:.4%} exceeds 1%"

    def test_evolve_output_shape(self, market_eps1):
        """evolve() must return arrays with correct shapes."""
        steps = 50
        result = market_eps1.evolve(steps=steps, dt=0.01)
        assert result['states_history'].shape == (steps + 1, 5, 8)
        assert result['associator_norms'].shape == (steps + 1,)
        assert result['total_wealth'].shape == (steps + 1,)
        assert result['times'].shape == (steps + 1,)

    def test_evolve_starts_at_initial_state(self, market_eps1):
        """The first entry in states_history must match the initial states."""
        initial_states = market_eps1.states.copy()
        result = market_eps1.evolve(steps=10, dt=0.01)
        np.testing.assert_allclose(result['states_history'][0], initial_states)

    def test_associator_zero_at_eps0_quaternionic(self):
        """
        At epsilon=0, if agents only have quaternionic components (0-3),
        the mean associator norm should be near zero.
        """
        market = MultiAgentMarket(n_agents=4, epsilon=0.0, seed=42)
        # Zero out non-quaternionic components
        market.states[:, 4:] = 0.0
        norm = market.mean_associator_norm()
        assert norm < 1e-10, f"Expected ~0, got {norm}"

    def test_associator_positive_at_eps1(self, market_eps1):
        """At epsilon=1, the mean associator norm should be positive."""
        norm = market_eps1.mean_associator_norm()
        assert norm > 0.0, "Expected positive associator norm at eps=1"

    def test_associator_scales_with_epsilon(self):
        """Mean associator norm should increase from eps=0 to eps=1."""
        norms = []
        for eps in [0.0, 0.5, 1.0]:
            market = MultiAgentMarket(n_agents=4, epsilon=eps, seed=42)
            norms.append(market.mean_associator_norm())
        # eps=1 should produce larger associator than eps=0
        assert norms[2] > norms[0], (
            f"Expected increasing: eps=0 -> {norms[0]}, eps=1 -> {norms[2]}"
        )

    def test_determinism(self):
        """Same seed must produce identical results."""
        m1 = MultiAgentMarket(n_agents=5, epsilon=0.7, seed=123)
        r1 = m1.evolve(steps=20, dt=0.01)

        m2 = MultiAgentMarket(n_agents=5, epsilon=0.7, seed=123)
        r2 = m2.evolve(steps=20, dt=0.01)

        np.testing.assert_array_equal(r1['states_history'], r2['states_history'])
        np.testing.assert_array_equal(r1['associator_norms'], r2['associator_norms'])

    def test_different_seeds_differ(self):
        """Different seeds must produce different states."""
        m1 = MultiAgentMarket(n_agents=5, epsilon=1.0, seed=1)
        m2 = MultiAgentMarket(n_agents=5, epsilon=1.0, seed=2)
        assert not np.allclose(m1.states, m2.states)

    def test_pairwise_interaction_shape(self, market_eps1):
        """Pairwise interaction must return shape (8,)."""
        result = market_eps1.pairwise_interaction(0, 1)
        assert result.shape == (8,)

    def test_triple_associator_shape(self, market_eps1):
        """Triple associator must return shape (8,)."""
        result = market_eps1.triple_associator(0, 1, 2)
        assert result.shape == (8,)

    def test_times_monotonic(self, market_eps1):
        """Time array must be monotonically increasing."""
        result = market_eps1.evolve(steps=20, dt=0.01)
        times = result['times']
        assert np.all(np.diff(times) > 0)


# ===================================================================
# PortfolioDynamics
# ===================================================================

class TestPortfolioDynamics:
    """Tests for PortfolioDynamics."""

    def test_initialization(self, portfolio_eps1):
        """Assets must be properly initialized."""
        assert portfolio_eps1.assets.shape == (5, 8)
        assert portfolio_eps1.n_assets == 5
        assert portfolio_eps1.epsilon == 1.0

    def test_too_few_assets_raises(self):
        """Initializing with fewer than 3 assets must raise."""
        with pytest.raises(ValueError, match="at least 3"):
            PortfolioDynamics(n_assets=2)

    def test_portfolio_product_shape(self, portfolio_eps1):
        """Portfolio product must return shape (8,)."""
        result = portfolio_eps1.portfolio_product([0, 1, 2])
        assert result.shape == (8,)

    def test_triple_associator_shape(self, portfolio_eps1):
        """Triple associator must return shape (8,)."""
        result = portfolio_eps1.triple_associator(0, 1, 2)
        assert result.shape == (8,)

    def test_entropy_non_negative(self, portfolio_eps1):
        """Associator entropy must be non-negative."""
        S = portfolio_eps1.compute_associator_entropy()
        assert S >= 0.0

    def test_entropy_zero_at_eps0_quaternionic_assets(self):
        """
        At epsilon=0 with quaternionic assets (components 0-3 only),
        associator entropy should be zero.
        """
        portfolio = PortfolioDynamics(n_assets=4, epsilon=0.0, seed=42)
        # Restrict to quaternionic subalgebra
        portfolio.assets[:, 4:] = 0.0
        S = portfolio.compute_associator_entropy()
        assert S < 1e-10, f"Expected ~0, got {S}"

    def test_entropy_positive_at_eps1(self, portfolio_eps1):
        """At epsilon=1, entropy should be positive for generic assets."""
        S = portfolio_eps1.compute_associator_entropy()
        assert S > 0.0, "Expected positive entropy at eps=1"

    def test_ordering_spread_smaller_at_eps0_than_eps1(self):
        """
        At epsilon=0, the ordering spread should be smaller than at
        epsilon=1 for the same assets. Note: even at eps=0, the algebra
        is non-commutative so different orderings of a sequential product
        can differ. But non-associativity (eps=1) adds an additional
        source of ordering-dependence that increases the spread.
        """
        portfolio_0 = PortfolioDynamics(n_assets=5, epsilon=0.0, seed=42)
        portfolio_1 = PortfolioDynamics(n_assets=5, epsilon=1.0, seed=42)
        spread_0 = portfolio_0.ordering_spread([0, 1, 2, 3])['spread']
        spread_1 = portfolio_1.ordering_spread([0, 1, 2, 3])['spread']
        assert spread_1 > spread_0, (
            f"Expected spread(eps=1) > spread(eps=0): {spread_1} vs {spread_0}"
        )

    def test_ordering_spread_positive_at_eps1(self, portfolio_eps1):
        """At epsilon=1, ordering spread should be positive."""
        result = portfolio_eps1.ordering_spread([0, 1, 2, 3])
        assert result['spread'] > 0.0

    def test_ordering_spread_keys(self, portfolio_eps1):
        """ordering_spread must return the documented keys."""
        result = portfolio_eps1.ordering_spread([0, 1, 2])
        expected_keys = {'returns', 'spread', 'mean_return', 'std_return'}
        assert set(result.keys()) == expected_keys

    def test_compare_returns_shape(self, portfolio_eps1):
        """compare_returns must return arrays of matching length."""
        eps_vals = np.array([0.0, 0.5, 1.0])
        result = portfolio_eps1.compare_returns(eps_vals)
        n = len(eps_vals)
        assert result['epsilon'].shape == (n,)
        assert result['entropy'].shape == (n,)
        assert result['spread'].shape == (n,)
        assert result['mean_assoc_norm'].shape == (n,)

    def test_compare_returns_monotonic_assoc(self, portfolio_eps1):
        """
        Mean associator norm should generally increase from eps=0 to eps=1.
        """
        result = portfolio_eps1.compare_returns(np.array([0.0, 0.5, 1.0]))
        assert result['mean_assoc_norm'][-1] > result['mean_assoc_norm'][0], (
            "Associator norm should increase with epsilon"
        )

    def test_compare_returns_restores_epsilon(self, portfolio_eps1):
        """compare_returns must restore the original epsilon after running."""
        original_eps = portfolio_eps1.epsilon
        portfolio_eps1.compare_returns(np.array([0.0, 0.5, 1.0]))
        assert portfolio_eps1.epsilon == original_eps

    def test_determinism(self):
        """Same seed must produce identical results."""
        p1 = PortfolioDynamics(n_assets=5, epsilon=0.8, seed=77)
        p2 = PortfolioDynamics(n_assets=5, epsilon=0.8, seed=77)
        np.testing.assert_array_equal(p1.assets, p2.assets)
        assert p1.compute_associator_entropy() == p2.compute_associator_entropy()

    def test_different_epsilon_different_mean_assoc_norm(self):
        """
        For generic (full 8D) assets, the mean associator norm at
        epsilon=1 should exceed epsilon=0. We test this via
        compare_returns which sweeps over epsilon values.
        """
        portfolio = PortfolioDynamics(n_assets=5, epsilon=1.0, seed=42)
        result = portfolio.compare_returns(np.array([0.0, 1.0]))
        # The mean associator norm should increase from eps=0 to eps=1
        assert result['mean_assoc_norm'][1] > result['mean_assoc_norm'][0], (
            f"Expected norm(eps=1) > norm(eps=0): "
            f"{result['mean_assoc_norm'][1]} vs {result['mean_assoc_norm'][0]}"
        )


# ===================================================================
# EcosystemModel
# ===================================================================

class TestEcosystemModel:
    """Tests for EcosystemModel."""

    def test_initialization(self, eco_eps1):
        """Model parameters must have correct shapes."""
        assert eco_eps1.r.shape == (7,)
        assert eco_eps1.A.shape == (7, 7)
        assert eco_eps1.T_base.shape == (7, 7, 7)
        assert eco_eps1.x0.shape == (7,)

    def test_ternary_tensor_zero_at_eps0(self, eco_eps0):
        """At epsilon=0, the ternary tensor must be all zeros."""
        T = eco_eps0.ternary_tensor()
        np.testing.assert_allclose(T, 0.0, atol=1e-15)

    def test_ternary_tensor_nonzero_at_eps1(self, eco_eps1):
        """At epsilon=1, the ternary tensor must have non-zero entries."""
        T = eco_eps1.ternary_tensor()
        assert np.max(np.abs(T)) > 0

    def test_ternary_tensor_scales_with_epsilon(self):
        """The ternary tensor should scale linearly with epsilon."""
        eco05 = EcosystemModel(epsilon=0.5, seed=42)
        eco10 = EcosystemModel(epsilon=1.0, seed=42)
        T05 = eco05.ternary_tensor()
        T10 = eco10.ternary_tensor()
        # T(0.5) should be exactly 0.5 * T(1.0)
        np.testing.assert_allclose(T05, 0.5 * T10, atol=1e-15)

    def test_simulate_output_shape(self, eco_eps1):
        """simulate() must return arrays with correct shapes."""
        n_steps = 100
        result = eco_eps1.simulate(dt=0.01, n_steps=n_steps)
        assert result['trajectory'].shape == (n_steps + 1, 7)
        assert result['times'].shape == (n_steps + 1,)
        assert result['total_biomass'].shape == (n_steps + 1,)

    def test_simulate_starts_at_x0(self, eco_eps1):
        """Trajectory must start at the initial populations."""
        result = eco_eps1.simulate(dt=0.01, n_steps=10)
        np.testing.assert_allclose(result['trajectory'][0], eco_eps1.x0)

    def test_eps0_reproduces_standard_lv(self):
        """
        At epsilon=0, the ternary tensor is zero so the model should
        reproduce standard pairwise Lotka-Volterra exactly.
        """
        eco = EcosystemModel(epsilon=0.0, seed=42)
        n_steps = 100
        dt = 0.01

        # Our model
        result = eco.simulate(dt=dt, n_steps=n_steps)
        traj_model = result['trajectory']

        # Direct standard LV (T=0)
        from octonion_algebra.applications import simulate_lotka_volterra
        T_zero = np.zeros((7, 7, 7))
        traj_std = simulate_lotka_volterra(eco.x0, eco.r, eco.A, T_zero, dt, n_steps)

        np.testing.assert_allclose(traj_model, traj_std, atol=1e-12)

    def test_eps1_differs_from_eps0(self):
        """
        At epsilon=1, the trajectory should differ from the eps=0 baseline.
        """
        eco0 = EcosystemModel(epsilon=0.0, seed=42)
        eco1 = EcosystemModel(epsilon=1.0, seed=42)
        n_steps = 200
        dt = 0.01

        traj0 = eco0.simulate(dt=dt, n_steps=n_steps)['trajectory']
        traj1 = eco1.simulate(dt=dt, n_steps=n_steps)['trajectory']

        max_diff = np.max(np.abs(traj1 - traj0))
        assert max_diff > 1e-6, f"Expected measurable difference, got {max_diff}"

    def test_positive_populations_short_sim(self, eco_eps1):
        """For a short simulation, populations should stay positive."""
        result = eco_eps1.simulate(dt=0.005, n_steps=50)
        assert np.all(result['trajectory'] > 0), "Populations went negative"

    def test_biomass_tracks_populations(self, eco_eps1):
        """Total biomass must equal sum of populations at each step."""
        result = eco_eps1.simulate(dt=0.01, n_steps=50)
        expected_biomass = np.sum(result['trajectory'], axis=1)
        np.testing.assert_allclose(result['total_biomass'], expected_biomass)

    def test_compare_epsilon_output_keys(self, eco_eps1):
        """compare_epsilon must return the documented keys."""
        result = eco_eps1.compare_epsilon(
            epsilon_values=np.array([0.0, 1.0]),
            dt=0.01, n_steps=50,
        )
        expected_keys = {
            'epsilon', 'trajectories', 'final_biomass',
            'biomass_deviation', 'max_species_deviation',
        }
        assert set(result.keys()) == expected_keys

    def test_compare_epsilon_baseline_zero_deviation(self, eco_eps1):
        """At epsilon=0, deviation from baseline must be zero."""
        result = eco_eps1.compare_epsilon(
            epsilon_values=np.array([0.0, 1.0]),
            dt=0.01, n_steps=50,
        )
        # First entry is eps=0 (baseline), deviation should be 0
        assert result['biomass_deviation'][0] < 1e-12
        assert result['max_species_deviation'][0] < 1e-12

    def test_compare_epsilon_nonzero_deviation_at_eps1(self, eco_eps1):
        """At epsilon=1, deviation from baseline should be measurable."""
        result = eco_eps1.compare_epsilon(
            epsilon_values=np.array([0.0, 1.0]),
            dt=0.01, n_steps=200,
        )
        assert result['max_species_deviation'][-1] > 1e-6

    def test_compare_epsilon_restores_epsilon(self, eco_eps1):
        """compare_epsilon must restore the original epsilon."""
        original_eps = eco_eps1.epsilon
        eco_eps1.compare_epsilon(np.array([0.0, 0.5, 1.0]), dt=0.01, n_steps=10)
        assert eco_eps1.epsilon == original_eps

    def test_associator_along_trajectory_shape(self, eco_eps1):
        """associator_along_trajectory must return correct shapes."""
        n_steps = 50
        result = eco_eps1.associator_along_trajectory(
            dt=0.01, n_steps=n_steps, sample_triples=3,
        )
        assert result['times'].shape == (n_steps + 1,)
        assert result['mean_associator_norm'].shape == (n_steps + 1,)
        assert result['trajectory'].shape == (n_steps + 1, 7)

    def test_associator_along_trajectory_positive_at_eps1(self, eco_eps1):
        """At epsilon=1, the tracked associator norms should be positive."""
        result = eco_eps1.associator_along_trajectory(
            dt=0.01, n_steps=50, sample_triples=5,
        )
        # Mean of the tracked norms should be positive
        mean_norm = np.mean(result['mean_associator_norm'])
        assert mean_norm > 0.0

    def test_determinism(self):
        """Same seed must produce identical trajectories."""
        eco1 = EcosystemModel(epsilon=0.7, seed=99)
        eco2 = EcosystemModel(epsilon=0.7, seed=99)
        traj1 = eco1.simulate(dt=0.01, n_steps=50)['trajectory']
        traj2 = eco2.simulate(dt=0.01, n_steps=50)['trajectory']
        np.testing.assert_array_equal(traj1, traj2)


# ===================================================================
# Cross-model integration tests
# ===================================================================

class TestIntegration:
    """Cross-model integration tests."""

    def test_epsilon_zero_all_models_associative(self):
        """
        At epsilon=0, all three models should exhibit zero or near-zero
        associator effects.
        """
        # Market
        market = MultiAgentMarket(n_agents=4, epsilon=0.0, seed=42)
        market.states[:, 4:] = 0.0  # restrict to quaternionic
        assert market.mean_associator_norm() < 1e-10

        # Portfolio
        portfolio = PortfolioDynamics(n_assets=4, epsilon=0.0, seed=42)
        portfolio.assets[:, 4:] = 0.0
        assert portfolio.compute_associator_entropy() < 1e-10

        # Ecosystem (ternary tensor = 0)
        eco = EcosystemModel(epsilon=0.0, seed=42)
        T = eco.ternary_tensor()
        np.testing.assert_allclose(T, 0.0, atol=1e-15)

    def test_epsilon_one_all_models_non_associative(self):
        """
        At epsilon=1, all three models should exhibit measurable
        non-associative effects.
        """
        # Market
        market = MultiAgentMarket(n_agents=5, epsilon=1.0, seed=42)
        assert market.mean_associator_norm() > 0.0

        # Portfolio
        portfolio = PortfolioDynamics(n_assets=5, epsilon=1.0, seed=42)
        assert portfolio.compute_associator_entropy() > 0.0

        # Ecosystem
        eco = EcosystemModel(epsilon=1.0, seed=42)
        T = eco.ternary_tensor()
        assert np.max(np.abs(T)) > 0

    def test_all_models_deterministic(self):
        """All models must be reproducible with the same seed."""
        for seed in [10, 20, 30]:
            m1 = MultiAgentMarket(n_agents=4, epsilon=0.5, seed=seed)
            m2 = MultiAgentMarket(n_agents=4, epsilon=0.5, seed=seed)
            np.testing.assert_array_equal(m1.states, m2.states)

            p1 = PortfolioDynamics(n_assets=4, epsilon=0.5, seed=seed)
            p2 = PortfolioDynamics(n_assets=4, epsilon=0.5, seed=seed)
            np.testing.assert_array_equal(p1.assets, p2.assets)

            e1 = EcosystemModel(epsilon=0.5, seed=seed)
            e2 = EcosystemModel(epsilon=0.5, seed=seed)
            np.testing.assert_array_equal(e1.x0, e2.x0)
            np.testing.assert_array_equal(e1.r, e2.r)
            np.testing.assert_array_equal(e1.A, e2.A)

    def test_associator_monotonic_in_epsilon(self):
        """
        For fixed random inputs, associator norms should generally
        increase as epsilon goes from 0 to 1.
        """
        rng = np.random.default_rng(42)
        a = rng.standard_normal(8)
        b = rng.standard_normal(8)
        c = rng.standard_normal(8)

        epsilons = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
        norms = [_deformed_associator_norm(a, b, c, eps) for eps in epsilons]

        # Final should exceed initial
        assert norms[-1] > norms[0]
        # No norm should be negative
        assert all(n >= 0 for n in norms)
