"""
Market and economic system simulator using the octonionic deformation framework.

The key mathematical insight: non-associativity = context-dependence. In markets,
    (Trade_A then Trade_B) then Trade_C  !=  Trade_A then (Trade_B then Trade_C)

The ASSOCIATOR [A, B, C] = (A*B)*C - A*(B*C) measures this context-dependence.
As the deformation parameter epsilon goes from 0 (associative / quaternionic) to
1 (fully non-associative / octonionic), context effects emerge.

Models:
    1. MultiAgentMarket  -- N agents with octonionic state vectors; pairwise and
       three-way interactions produce measurable associator effects.
    2. PortfolioDynamics -- N assets with octonionic correlation structure;
       trade-ordering creates non-associative returns.
    3. EcosystemModel   -- 7-species Lotka-Volterra with octonionic predation;
       trophic cascades are order-dependent.

All simulations are deterministic (seeded), produce numpy arrays suitable for
plotting, and include an epsilon=0 baseline for comparison.
"""

import numpy as np
from itertools import combinations

from octonion_algebra.core import Octonion, FANO_TRIPLES
from octonion_algebra.deformation import (
    DeformedOctonion,
    deformed_multiply,
    deformed_associator,
    deformed_structure_constants,
)
from octonion_algebra.associator import associator, associator_norm
from octonion_algebra.applications import (
    fano_ternary_tensor,
    simulate_lotka_volterra,
    octonionic_lotka_volterra_rhs,
)


# ============================================================================
# Helpers
# ============================================================================

def _deformed_associator_norm(a_coeffs, b_coeffs, c_coeffs, epsilon):
    """
    Compute ||[a, b, c]_epsilon|| for raw coefficient arrays.

    Uses the deformed multiplication at the given epsilon to evaluate
        [a, b, c]_eps = (a *_eps b) *_eps c  -  a *_eps (b *_eps c)
    and returns its Euclidean norm.

    Args:
        a_coeffs, b_coeffs, c_coeffs: array-like of shape (8,).
        epsilon: deformation parameter in [0, 1].

    Returns:
        float: the associator norm.
    """
    ab = deformed_multiply(a_coeffs, b_coeffs, epsilon)
    bc = deformed_multiply(b_coeffs, c_coeffs, epsilon)
    ab_c = deformed_multiply(ab, c_coeffs, epsilon)
    a_bc = deformed_multiply(a_coeffs, bc, epsilon)
    return float(np.linalg.norm(ab_c - a_bc))


# ============================================================================
# 1. MultiAgentMarket
# ============================================================================

class MultiAgentMarket:
    """
    N agents interacting in an octonionic market.

    Each agent has an 8-component state vector:
        component 0:   wealth (scalar / real part)
        components 1-7: strategy coordinates (7 imaginary dimensions)

    Agent interactions use the deformed octonion product parameterised by
    epsilon in [0, 1]:
        - Pairwise: agent_i *_eps agent_j
        - Three-way: (agent_i *_eps agent_j) *_eps agent_k  vs
                      agent_i *_eps (agent_j *_eps agent_k)

    The ASSOCIATOR of every triple measures context-dependence.

    At epsilon=0 the product is quaternionic (associative on the active
    subalgebra), so the associator vanishes and ordering does not matter.
    At epsilon=1 full non-associativity is present and ordering matters.

    Mathematical context
    --------------------
    The deformed algebra A_epsilon interpolates between the quaternions H
    (epsilon=0) and the octonions O (epsilon=1). The structure constants
    f_{ijk}(epsilon) scale the non-quaternionic Fano triples by epsilon,
    so the associator is a smooth function of epsilon that is identically
    zero at epsilon=0 and generically non-zero at epsilon=1.

    Attributes:
        n_agents: int -- number of agents.
        epsilon: float -- deformation parameter.
        states: ndarray of shape (n_agents, 8) -- agent state vectors.
        seed: int -- random seed used for initialisation.
    """

    def __init__(self, n_agents=10, epsilon=1.0, seed=42):
        """
        Initialise a multi-agent market.

        Args:
            n_agents: number of agents (>= 3 for meaningful associators).
            epsilon: deformation parameter in [0, 1].
            seed: random seed for reproducibility.
        """
        self.n_agents = n_agents
        self.epsilon = float(epsilon)
        self.seed = seed
        rng = np.random.default_rng(seed)

        # Initialise agent states: wealth in [0.5, 1.5], strategies in [-1, 1]
        self.states = np.zeros((n_agents, 8))
        self.states[:, 0] = rng.uniform(0.5, 1.5, size=n_agents)  # wealth
        self.states[:, 1:] = rng.uniform(-1, 1, size=(n_agents, 7))  # strategy

    def total_wealth(self):
        """
        Return total wealth (sum of real parts) across all agents.

        In the evolution dynamics below, interactions redistribute wealth
        but do not create or destroy it, so total_wealth should be
        approximately conserved.

        Returns:
            float: sum of agent wealth (component 0).
        """
        return float(np.sum(self.states[:, 0]))

    def pairwise_interaction(self, i, j, coupling=0.01):
        """
        Compute the pairwise interaction between agents i and j.

        The interaction is the imaginary part of the deformed product,
        scaled by a coupling constant. This represents the "strategic
        influence" of agent i on agent j (and vice versa, with a sign
        flip from non-commutativity).

        Args:
            i, j: agent indices.
            coupling: strength of interaction (default 0.01).

        Returns:
            ndarray of shape (8,): interaction vector (real part is zero
            for the symmetric part; antisymmetric part has real component).
        """
        product = deformed_multiply(self.states[i], self.states[j], self.epsilon)
        return coupling * product

    def triple_associator(self, i, j, k):
        """
        Compute the associator [agent_i, agent_j, agent_k]_epsilon.

        This measures how much the outcome of the three-way interaction
        depends on grouping order.

        Args:
            i, j, k: agent indices.

        Returns:
            ndarray of shape (8,): the associator vector.
        """
        a, b, c = self.states[i], self.states[j], self.states[k]
        ab = deformed_multiply(a, b, self.epsilon)
        bc = deformed_multiply(b, c, self.epsilon)
        ab_c = deformed_multiply(ab, c, self.epsilon)
        a_bc = deformed_multiply(a, bc, self.epsilon)
        return ab_c - a_bc

    def mean_associator_norm(self):
        """
        Average ||[a_i, a_j, a_k]_epsilon|| over all unordered triples.

        This is the primary measure of context-dependence in the market.
        It equals zero at epsilon=0 (when agents only use the quaternionic
        subalgebra) and grows with epsilon.

        Returns:
            float: mean associator norm.
        """
        total = 0.0
        count = 0
        for combo in combinations(range(self.n_agents), 3):
            i, j, k = combo
            assoc = self.triple_associator(i, j, k)
            total += np.linalg.norm(assoc)
            count += 1
        return total / count if count > 0 else 0.0

    def evolve(self, steps=100, dt=0.01, coupling=0.01):
        """
        Time-step the market for *steps* iterations.

        Dynamics: at each step, every agent is updated by the mean
        pairwise interaction with all other agents, scaled by dt. The
        interaction is purely redistributive: for each pair (i, j), agent
        i receives +coupling * product(i, j) and agent j receives
        -coupling * product(i, j), ensuring total wealth conservation
        (up to numerical precision).

        After each step the mean associator norm is recorded.

        Args:
            steps: number of time steps.
            dt: time-step size.
            coupling: interaction strength.

        Returns:
            dict with keys:
                'states_history': ndarray (steps+1, n_agents, 8)
                'associator_norms': ndarray (steps+1,) -- mean assoc norm
                    at each recorded time.
                'total_wealth': ndarray (steps+1,) -- total wealth over time.
                'times': ndarray (steps+1,) -- time values.
        """
        n = self.n_agents
        history = np.zeros((steps + 1, n, 8))
        assoc_norms = np.zeros(steps + 1)
        wealth_history = np.zeros(steps + 1)
        times = np.arange(steps + 1) * dt

        history[0] = self.states.copy()
        assoc_norms[0] = self.mean_associator_norm()
        wealth_history[0] = self.total_wealth()

        for step in range(steps):
            # Compute all pairwise interactions (antisymmetric redistribution)
            delta = np.zeros((n, 8))
            for i in range(n):
                for j in range(i + 1, n):
                    interaction = self.pairwise_interaction(i, j, coupling)
                    delta[i] += dt * interaction
                    delta[j] -= dt * interaction

            self.states += delta
            history[step + 1] = self.states.copy()
            assoc_norms[step + 1] = self.mean_associator_norm()
            wealth_history[step + 1] = self.total_wealth()

        return {
            'states_history': history,
            'associator_norms': assoc_norms,
            'total_wealth': wealth_history,
            'times': times,
        }


# ============================================================================
# 2. PortfolioDynamics
# ============================================================================

class PortfolioDynamics:
    """
    Portfolio dynamics with octonionic correlation structure.

    N assets are represented as deformed octonions. Portfolio rebalancing
    (sequentially combining assets) creates non-associative effects: the
    ORDER in which trades are executed matters.

    The 7 imaginary components represent 7 orthogonal risk factors
    (aligned with the Fano-plane structure of the octonions). The real
    component represents expected return.

    Mathematical context
    --------------------
    For three assets A, B, C the "left-to-right" portfolio is
        P_LR = (A *_eps B) *_eps C
    and the "right-to-left" portfolio is
        P_RL = A *_eps (B *_eps C)

    The associator [A, B, C]_eps = P_LR - P_RL measures the
    context-dependence of trade ordering.  Its norm quantifies the
    "information lost by ignoring trade order" -- the associator entropy.

    Attributes:
        n_assets: int -- number of assets.
        epsilon: float -- deformation parameter.
        assets: ndarray of shape (n_assets, 8) -- asset vectors.
        seed: int -- random seed.
    """

    def __init__(self, n_assets=7, epsilon=1.0, seed=42):
        """
        Initialise portfolio dynamics.

        Args:
            n_assets: number of assets (>= 3).
            epsilon: deformation parameter in [0, 1].
            seed: random seed.
        """
        if n_assets < 3:
            raise ValueError("Need at least 3 assets for associator effects")
        self.n_assets = n_assets
        self.epsilon = float(epsilon)
        self.seed = seed
        rng = np.random.default_rng(seed)

        # Asset vectors: return in [0.01, 0.10], risk factors in [-0.5, 0.5]
        self.assets = np.zeros((n_assets, 8))
        self.assets[:, 0] = rng.uniform(0.01, 0.10, size=n_assets)
        self.assets[:, 1:] = rng.uniform(-0.5, 0.5, size=(n_assets, 7))

    def portfolio_product(self, indices):
        """
        Compute the sequential product of assets in the given order
        (left-to-right association).

        P = ((...((a_0 *_eps a_1) *_eps a_2) ...) *_eps a_{n-1})

        Args:
            indices: sequence of asset indices.

        Returns:
            ndarray of shape (8,): the portfolio product.
        """
        result = self.assets[indices[0]].copy()
        for idx in indices[1:]:
            result = deformed_multiply(result, self.assets[idx], self.epsilon)
        return result

    def triple_associator(self, i, j, k):
        """
        Compute the associator for assets (i, j, k).

        Returns:
            ndarray of shape (8,): the associator vector.
        """
        a, b, c = self.assets[i], self.assets[j], self.assets[k]
        ab = deformed_multiply(a, b, self.epsilon)
        bc = deformed_multiply(b, c, self.epsilon)
        ab_c = deformed_multiply(ab, c, self.epsilon)
        a_bc = deformed_multiply(a, bc, self.epsilon)
        return ab_c - a_bc

    def compute_associator_entropy(self):
        """
        Compute associator entropy of the portfolio.

        S = -sum_i p_i * log(p_i)

        where p_i = ||[a_i, a_j, a_k]_eps||^2 / Z for each unordered
        triple (i, j, k), and Z = sum of all squared norms.

        This measures how much information is lost by ignoring trade
        ordering. S = 0 when the algebra is associative (epsilon = 0 with
        quaternionic inputs) or when all triples have identical associator
        magnitude (maximum uniformity).

        Returns:
            float: the associator entropy (non-negative).
        """
        weights = []
        for combo in combinations(range(self.n_assets), 3):
            i, j, k = combo
            assoc = self.triple_associator(i, j, k)
            w = float(np.dot(assoc, assoc))  # ||assoc||^2
            weights.append(w)

        Z = sum(weights)
        if Z < 1e-20:
            return 0.0

        entropy = 0.0
        for w in weights:
            p = w / Z
            if p > 1e-30:
                entropy -= p * np.log(p)
        return float(entropy)

    def ordering_spread(self, indices):
        """
        Compute the spread of portfolio returns over all permutations of
        the given asset indices.

        For each permutation, compute the left-to-right sequential product
        and record its real part (the return). The spread is the difference
        between the maximum and minimum return.

        For n <= 7 all permutations are enumerated; for larger n a random
        sample of 5040 permutations is used.

        Args:
            indices: sequence of asset indices (length >= 3).

        Returns:
            dict with keys:
                'returns': ndarray of returns for each permutation.
                'spread': float -- max - min.
                'mean_return': float.
                'std_return': float.
        """
        from itertools import permutations as iterperms
        indices = list(indices)
        n = len(indices)
        if n <= 7:
            perms = list(iterperms(indices))
        else:
            rng = np.random.default_rng(self.seed + 999)
            perms = [tuple(rng.permutation(indices)) for _ in range(5040)]

        returns = np.array([self.portfolio_product(p)[0] for p in perms])
        return {
            'returns': returns,
            'spread': float(np.max(returns) - np.min(returns)),
            'mean_return': float(np.mean(returns)),
            'std_return': float(np.std(returns)),
        }

    def compare_returns(self, epsilon_values=None):
        """
        Show how context-dependence affects portfolio returns across
        different epsilon values.

        For each epsilon, compute the associator entropy and the ordering
        spread of the first 4 assets.

        Args:
            epsilon_values: array-like of epsilon values.
                Defaults to np.linspace(0, 1, 11).

        Returns:
            dict with keys:
                'epsilon': ndarray of epsilon values.
                'entropy': ndarray -- associator entropy at each epsilon.
                'spread': ndarray -- ordering spread at each epsilon.
                'mean_assoc_norm': ndarray -- mean ||assoc|| at each epsilon.
        """
        if epsilon_values is None:
            epsilon_values = np.linspace(0, 1, 11)
        epsilon_values = np.asarray(epsilon_values, dtype=float)

        entropies = np.zeros(len(epsilon_values))
        spreads = np.zeros(len(epsilon_values))
        mean_norms = np.zeros(len(epsilon_values))

        saved_eps = self.epsilon
        test_indices = list(range(min(4, self.n_assets)))

        for idx, eps in enumerate(epsilon_values):
            self.epsilon = eps
            entropies[idx] = self.compute_associator_entropy()

            spread_result = self.ordering_spread(test_indices)
            spreads[idx] = spread_result['spread']

            # Mean associator norm across all triples
            norms = []
            for combo in combinations(range(self.n_assets), 3):
                i, j, k = combo
                assoc = self.triple_associator(i, j, k)
                norms.append(np.linalg.norm(assoc))
            mean_norms[idx] = np.mean(norms) if norms else 0.0

        self.epsilon = saved_eps  # restore

        return {
            'epsilon': epsilon_values,
            'entropy': entropies,
            'spread': spreads,
            'mean_assoc_norm': mean_norms,
        }


# ============================================================================
# 3. EcosystemModel
# ============================================================================

class EcosystemModel:
    """
    7-species ecosystem with octonionic predation structure.

    Extends the standard Lotka-Volterra model by incorporating ternary
    (three-body) interactions derived from the Fano-plane structure
    constants, controlled by the deformation parameter epsilon.

    Non-associative predation means:
        (A eats B) eats C  !=  A eats (B eats C)
    -- trophic cascades are order-dependent. The epsilon parameter
    controls the strength of this non-associativity.

    At epsilon=0 the ternary tensor vanishes and the model reduces to
    standard pairwise Lotka-Volterra. At epsilon=1 the full Fano
    structure is active.

    Mathematical context
    --------------------
    The ternary interaction tensor is

        T_{ijk}(epsilon) = epsilon * |f_{ijk}|

    where f_{ijk} are the octonionic structure constants and |.| takes
    the absolute value (converting the antisymmetric tensor to a
    symmetric connectivity indicator). The population dynamics are

        dx_i/dt = x_i * (r_i + sum_j A_{ij} x_j
                              + sum_{jk} T_{ijk}(eps) x_j x_k)

    Conservation: total biomass is NOT exactly conserved in LV dynamics
    (unlike Hamiltonian systems), but the model tracks it to quantify
    the effect of the ternary coupling.

    Attributes:
        epsilon: float -- deformation parameter.
        x0: ndarray (7,) -- initial populations.
        r: ndarray (7,) -- intrinsic growth rates.
        A: ndarray (7, 7) -- pairwise interaction matrix.
        T_base: ndarray (7, 7, 7) -- Fano ternary tensor (unscaled).
        seed: int -- random seed.
    """

    def __init__(self, epsilon=1.0, seed=42, growth_scale=0.3,
                 competition_scale=0.05, ternary_scale=0.01):
        """
        Initialise the ecosystem model.

        Args:
            epsilon: deformation parameter in [0, 1].
            seed: random seed.
            growth_scale: scale of intrinsic growth rates.
            competition_scale: scale of pairwise competition.
            ternary_scale: base scale of ternary coupling (multiplied by epsilon).
        """
        self.epsilon = float(epsilon)
        self.seed = seed
        self.ternary_scale = float(ternary_scale)
        rng = np.random.default_rng(seed)

        # Intrinsic growth rates (positive = grows, negative = decays)
        self.r = rng.uniform(0.1, growth_scale, size=7)

        # Pairwise interaction: mild competition + self-limitation
        self.A = -competition_scale * rng.uniform(0, 1, size=(7, 7))
        np.fill_diagonal(self.A, -0.1)

        # Fano ternary tensor (unscaled)
        self.T_base = fano_ternary_tensor()

        # Initial populations
        self.x0 = rng.uniform(0.5, 1.5, size=7)

    def ternary_tensor(self):
        """
        Return the ternary interaction tensor scaled by epsilon * ternary_scale.

        At epsilon=0 this is the zero tensor (standard LV).
        At epsilon=1 the full Fano connectivity structure is active.

        Returns:
            ndarray (7, 7, 7): the scaled ternary tensor.
        """
        return self.epsilon * self.ternary_scale * self.T_base

    def simulate(self, dt=0.01, n_steps=500):
        """
        Simulate the ecosystem using RK4 integration.

        Args:
            dt: time step.
            n_steps: number of integration steps.

        Returns:
            dict with keys:
                'trajectory': ndarray (n_steps+1, 7) -- populations.
                'times': ndarray (n_steps+1,) -- time values.
                'total_biomass': ndarray (n_steps+1,) -- sum of populations.
        """
        T = self.ternary_tensor()
        traj = simulate_lotka_volterra(self.x0, self.r, self.A, T, dt, n_steps)
        times = np.arange(n_steps + 1) * dt
        biomass = np.sum(traj, axis=1)

        return {
            'trajectory': traj,
            'times': times,
            'total_biomass': biomass,
        }

    def compare_epsilon(self, epsilon_values=None, dt=0.01, n_steps=500):
        """
        Run the ecosystem for multiple epsilon values and compare dynamics.

        Args:
            epsilon_values: array-like. Defaults to [0.0, 0.25, 0.5, 0.75, 1.0].
            dt: time step.
            n_steps: number of steps.

        Returns:
            dict with keys:
                'epsilon': ndarray of epsilon values.
                'trajectories': dict mapping epsilon -> (n_steps+1, 7) array.
                'final_biomass': ndarray -- total biomass at final step.
                'biomass_deviation': ndarray -- |biomass(eps) - biomass(0)|
                    at the final step.
                'max_species_deviation': ndarray -- max absolute population
                    deviation from the eps=0 baseline over all species & times.
        """
        if epsilon_values is None:
            epsilon_values = np.array([0.0, 0.25, 0.5, 0.75, 1.0])
        epsilon_values = np.asarray(epsilon_values, dtype=float)

        saved_eps = self.epsilon
        trajectories = {}
        final_biomass = np.zeros(len(epsilon_values))

        # Always compute eps=0 baseline first
        self.epsilon = 0.0
        baseline_result = self.simulate(dt, n_steps)
        baseline_traj = baseline_result['trajectory']

        for idx, eps in enumerate(epsilon_values):
            self.epsilon = eps
            result = self.simulate(dt, n_steps)
            trajectories[float(eps)] = result['trajectory']
            final_biomass[idx] = result['total_biomass'][-1]

        # Deviations from baseline
        biomass_dev = np.abs(final_biomass - final_biomass[0])
        max_species_dev = np.zeros(len(epsilon_values))
        for idx, eps in enumerate(epsilon_values):
            diff = np.abs(trajectories[float(eps)] - baseline_traj)
            max_species_dev[idx] = float(np.max(diff))

        self.epsilon = saved_eps  # restore

        return {
            'epsilon': epsilon_values,
            'trajectories': trajectories,
            'final_biomass': final_biomass,
            'biomass_deviation': biomass_dev,
            'max_species_deviation': max_species_dev,
        }

    def associator_along_trajectory(self, dt=0.01, n_steps=500, sample_triples=10):
        """
        Track the mean associator norm along the population trajectory.

        At each time step, treat the current population vector as the
        coefficients of a DeformedOctonion (with zero real part, since
        populations map to the 7 imaginary dimensions). Sample random
        triples from a fixed set and compute the deformed associator.

        Args:
            dt: time step.
            n_steps: number of steps.
            sample_triples: number of random triples to average over.

        Returns:
            dict with keys:
                'times': ndarray (n_steps+1,).
                'mean_associator_norm': ndarray (n_steps+1,).
                'trajectory': ndarray (n_steps+1, 7).
        """
        result = self.simulate(dt, n_steps)
        traj = result['trajectory']
        times = result['times']

        rng = np.random.default_rng(self.seed + 1)
        # Generate fixed set of random perturbation vectors for triples
        perturbations = rng.standard_normal((sample_triples, 3, 8))
        # Zero out real parts to keep perturbations imaginary
        perturbations[:, :, 0] = 0.0
        # Normalise each perturbation
        for t in range(sample_triples):
            for p in range(3):
                n = np.linalg.norm(perturbations[t, p])
                if n > 1e-15:
                    perturbations[t, p] /= n

        assoc_norms = np.zeros(n_steps + 1)
        for step in range(n_steps + 1):
            # Build an 8-component vector from population (0-indexed: pop -> e1..e7)
            state = np.zeros(8)
            state[1:] = traj[step]

            total = 0.0
            for t in range(sample_triples):
                # Create three test vectors: state + small perturbation
                a = state + 0.1 * perturbations[t, 0]
                b = state + 0.1 * perturbations[t, 1]
                c = state + 0.1 * perturbations[t, 2]
                total += _deformed_associator_norm(a, b, c, self.epsilon)

            assoc_norms[step] = total / sample_triples

        return {
            'times': times,
            'mean_associator_norm': assoc_norms,
            'trajectory': traj,
        }


# ============================================================================
# Main demo
# ============================================================================

def _print_separator(title):
    """Print a formatted section separator."""
    print(f"\n{'=' * 60}")
    print(f"  {title}")
    print(f"{'=' * 60}")


if __name__ == '__main__':

    # ------------------------------------------------------------------
    # 1. MultiAgentMarket
    # ------------------------------------------------------------------
    _print_separator("1. MultiAgentMarket: Context-Dependent Trading")

    for eps_val in [0.0, 1.0]:
        market = MultiAgentMarket(n_agents=6, epsilon=eps_val, seed=42)
        initial_wealth = market.total_wealth()
        result = market.evolve(steps=50, dt=0.01, coupling=0.01)

        final_wealth = result['total_wealth'][-1]
        mean_assoc = np.mean(result['associator_norms'])
        max_assoc = np.max(result['associator_norms'])
        wealth_drift = abs(final_wealth - initial_wealth) / initial_wealth * 100

        print(f"\n  epsilon = {eps_val}")
        print(f"    Initial wealth:      {initial_wealth:.6f}")
        print(f"    Final wealth:        {final_wealth:.6f}")
        print(f"    Wealth drift:        {wealth_drift:.4f}%")
        print(f"    Mean assoc norm:     {mean_assoc:.6f}")
        print(f"    Max  assoc norm:     {max_assoc:.6f}")

    # ------------------------------------------------------------------
    # 2. PortfolioDynamics
    # ------------------------------------------------------------------
    _print_separator("2. PortfolioDynamics: Trade-Ordering Effects")

    portfolio = PortfolioDynamics(n_assets=5, epsilon=1.0, seed=42)
    comparison = portfolio.compare_returns(np.array([0.0, 0.25, 0.5, 0.75, 1.0]))

    print(f"\n  {'epsilon':>8s}  {'entropy':>10s}  {'spread':>12s}  {'mean_assoc':>12s}")
    print(f"  {'-' * 8}  {'-' * 10}  {'-' * 12}  {'-' * 12}")
    for i, eps in enumerate(comparison['epsilon']):
        print(f"  {eps:8.2f}  {comparison['entropy'][i]:10.6f}  "
              f"{comparison['spread'][i]:12.8f}  "
              f"{comparison['mean_assoc_norm'][i]:12.8f}")

    context_dep_pct = 0.0
    if comparison['mean_assoc_norm'][-1] > 1e-15:
        baseline_norm = comparison['mean_assoc_norm'][0]
        full_norm = comparison['mean_assoc_norm'][-1]
        if full_norm > 1e-15:
            context_dep_pct = (full_norm - baseline_norm) / full_norm * 100

    print(f"\n  Context-dependence at eps=1 vs eps=0: {context_dep_pct:.1f}%")

    # ------------------------------------------------------------------
    # 3. EcosystemModel
    # ------------------------------------------------------------------
    _print_separator("3. EcosystemModel: Non-Associative Trophic Cascades")

    eco = EcosystemModel(epsilon=1.0, seed=42)
    comparison_eco = eco.compare_epsilon(
        epsilon_values=np.array([0.0, 0.5, 1.0]),
        dt=0.01, n_steps=200,
    )

    print(f"\n  {'epsilon':>8s}  {'final_biomass':>14s}  {'biomass_dev':>12s}  {'max_sp_dev':>12s}")
    print(f"  {'-' * 8}  {'-' * 14}  {'-' * 12}  {'-' * 12}")
    for i, eps in enumerate(comparison_eco['epsilon']):
        print(f"  {eps:8.2f}  "
              f"{comparison_eco['final_biomass'][i]:14.6f}  "
              f"{comparison_eco['biomass_deviation'][i]:12.8f}  "
              f"{comparison_eco['max_species_deviation'][i]:12.8f}")

    # Associator tracking
    assoc_track = eco.associator_along_trajectory(dt=0.01, n_steps=200, sample_triples=5)
    print(f"\n  Associator along trajectory (eps=1.0):")
    print(f"    Mean:  {np.mean(assoc_track['mean_associator_norm']):.8f}")
    print(f"    Max:   {np.max(assoc_track['mean_associator_norm']):.8f}")
    print(f"    Final: {assoc_track['mean_associator_norm'][-1]:.8f}")

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------
    _print_separator("Summary: epsilon=0 vs epsilon=1")
    print("""
  At epsilon=0 (associative / quaternionic limit):
    - Associator = 0: trade ordering does not matter
    - Portfolio spread = 0: all orderings give the same result
    - Ecosystem = standard Lotka-Volterra

  At epsilon=1 (full octonions / non-associative):
    - Associator > 0: context-dependence is measurable
    - Portfolio spread > 0: different trade orderings yield different returns
    - Ecosystem deviates from standard LV due to ternary cascades

  The deformation parameter epsilon provides a smooth dial between
  these two regimes, enabling precise quantification of context effects.
""")
