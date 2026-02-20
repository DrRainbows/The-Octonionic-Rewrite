"""
Concrete, quantified application models using octonionic algebra.

Addresses Grok critique #12 (applications are pure analogy, no equations, no
simulations) and #10 (complex systems just relabeling) by providing three models
where non-associativity produces measurable, quantitative differences from
standard (associative) approaches.

Models:
    1. Octonionic Lotka-Volterra -- ternary ecological interactions from Fano
       structure constants
    2. Portfolio Associator Entropy -- measuring agenda dependence in financial
       portfolio construction
    3. Coalition Associator -- agenda dependence in political coalition
       formation / game theory
"""

import numpy as np
from itertools import permutations, combinations
from octonion_algebra.core import Octonion
from octonion_algebra.associator import associator, associator_norm
from octonion_algebra.calculus import structure_constants


# ===========================================================================
# 1. Octonionic Lotka-Volterra (ecological dynamics)
# ===========================================================================

def fano_ternary_tensor():
    """
    Build the symmetric Fano ternary interaction tensor.

    The structure constants epsilon_{ijk} are totally antisymmetric, so
    sum_{jk} epsilon_{ijk} x_j x_k = 0 for all x (the contraction of an
    antisymmetric tensor with a symmetric product vanishes).

    To obtain a non-trivial ternary coupling we use the *connectivity*
    structure of the Fano plane:

        F_{ijk} = |epsilon_{ijk}|

    This tensor is 1 whenever (i, j, k) are any permutation of a Fano
    triple (i.e., they lie on a common Fano line), and 0 otherwise.
    It is fully symmetric and encodes *which* species participate in
    three-body interactions without the sign information.

    Returns:
        numpy array of shape (7, 7, 7).
    """
    return np.abs(structure_constants())


def octonionic_lotka_volterra_rhs(x, r, A, T):
    """
    Right-hand side of the octonionic Lotka-Volterra system.

    Standard Lotka-Volterra:
        dx_i/dt = x_i * (r_i + sum_j A_ij x_j)

    Octonionic extension adds ternary interactions derived from the
    Fano-plane structure constants:
        dx_i/dt = x_i * (r_i + sum_j A_ij x_j + sum_{j,k} T_ijk x_j x_k)

    The ternary term T_ijk encodes three-body interactions that model
    non-associative composition: (species_j affects species_k) affecting
    species_i != species_j affecting (species_k affects species_i).

    Args:
        x: numpy array of shape (7,) -- species populations (non-negative).
        r: numpy array of shape (7,) -- intrinsic growth rates.
        A: numpy array of shape (7, 7) -- pairwise interaction matrix.
        T: numpy array of shape (7, 7, 7) -- ternary interaction tensor
           (typically from structure_constants() scaled by some coupling).

    Returns:
        numpy array of shape (7,) -- dx/dt.
    """
    x = np.asarray(x, dtype=float)
    r = np.asarray(r, dtype=float)
    A = np.asarray(A, dtype=float)
    T = np.asarray(T, dtype=float)

    # Pairwise term: sum_j A_ij x_j
    pairwise = A @ x

    # Ternary term: sum_{j,k} T_ijk x_j x_k
    # Efficiently computed via einsum
    ternary = np.einsum('ijk,j,k->i', T, x, x)

    return x * (r + pairwise + ternary)


def simulate_lotka_volterra(x0, r, A, T, dt, n_steps):
    """
    Simulate the octonionic Lotka-Volterra system using RK4 integration.

    Args:
        x0: numpy array of shape (7,) -- initial populations.
        r: numpy array of shape (7,) -- intrinsic growth rates.
        A: numpy array of shape (7, 7) -- pairwise interaction matrix.
        T: numpy array of shape (7, 7, 7) -- ternary interaction tensor.
        dt: float -- time step.
        n_steps: int -- number of integration steps.

    Returns:
        numpy array of shape (n_steps + 1, 7) -- trajectory including
        the initial condition at index 0.
    """
    x0 = np.asarray(x0, dtype=float)
    trajectory = np.zeros((n_steps + 1, x0.shape[0]))
    trajectory[0] = x0.copy()

    x = x0.copy()
    for step in range(n_steps):
        k1 = octonionic_lotka_volterra_rhs(x, r, A, T)
        k2 = octonionic_lotka_volterra_rhs(x + 0.5 * dt * k1, r, A, T)
        k3 = octonionic_lotka_volterra_rhs(x + 0.5 * dt * k2, r, A, T)
        k4 = octonionic_lotka_volterra_rhs(x + dt * k3, r, A, T)
        x = x + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        trajectory[step + 1] = x.copy()

    return trajectory


def lotka_volterra_comparison(x0, r, A, dt, n_steps, T_scale=1.0):
    """
    Compare standard (T=0) vs octonionic (T != 0) Lotka-Volterra trajectories.

    The ternary tensor is constructed from the Fano ternary tensor (symmetric
    connectivity indicator derived from octonionic structure) scaled by
    ``T_scale``.

    Args:
        x0: numpy array of shape (7,) -- initial populations.
        r: numpy array of shape (7,) -- intrinsic growth rates.
        A: numpy array of shape (7, 7) -- pairwise interaction matrix.
        dt: float -- time step.
        n_steps: int -- number of integration steps.
        T_scale: float -- scaling factor for the ternary tensor (default 1.0).

    Returns:
        dict with keys:
            'trajectory_standard': (n_steps+1, 7) array -- standard LV.
            'trajectory_octonionic': (n_steps+1, 7) array -- octonionic LV.
            'max_deviation': float -- max absolute difference across all
                species and time steps.
            'relative_difference': float -- max_deviation normalised by
                the max population in the standard trajectory.
            'trajectory_divergence_time': float -- first time at which
                the per-step max deviation exceeds 1% of the instantaneous
                max standard population, or -1 if it never does.
    """
    x0 = np.asarray(x0, dtype=float)
    T_zero = np.zeros((7, 7, 7))
    T_oct = fano_ternary_tensor() * T_scale

    traj_std = simulate_lotka_volterra(x0, r, A, T_zero, dt, n_steps)
    traj_oct = simulate_lotka_volterra(x0, r, A, T_oct, dt, n_steps)

    diff = np.abs(traj_oct - traj_std)
    max_deviation = float(np.max(diff))

    max_pop_std = float(np.max(np.abs(traj_std)))
    relative_difference = max_deviation / max_pop_std if max_pop_std > 1e-30 else 0.0

    # Trajectory divergence time: first step where per-step max deviation > 1%
    divergence_time = -1.0
    for step in range(n_steps + 1):
        step_max_std = float(np.max(np.abs(traj_std[step])))
        step_max_diff = float(np.max(diff[step]))
        if step_max_std > 1e-30 and step_max_diff / step_max_std > 0.01:
            divergence_time = step * dt
            break

    return {
        'trajectory_standard': traj_std,
        'trajectory_octonionic': traj_oct,
        'max_deviation': max_deviation,
        'relative_difference': relative_difference,
        'trajectory_divergence_time': divergence_time,
    }


# ===========================================================================
# 2. Portfolio Associator Entropy (financial systems)
# ===========================================================================

def portfolio_associator(assets):
    """
    Given a list of 3 or more Octonion-valued asset risk vectors, compute
    all 3-element associators and return the total associator magnitude.

    The associator [a, b, c] = (a*b)*c - a*(b*c) measures how much the
    portfolio outcome depends on the order of combining assets -- a form
    of "agenda dependence" invisible in any associative (e.g. quaternionic
    or real-valued) risk model.

    Args:
        assets: list of Octonion instances (length >= 3).

    Returns:
        float -- sum of |[a_i, a_j, a_k]| over all ordered triples (i<j<k).
    """
    n = len(assets)
    if n < 3:
        raise ValueError("Need at least 3 assets to compute associators")

    total = 0.0
    for combo in combinations(range(n), 3):
        i, j, k = combo
        total += associator_norm(assets[i], assets[j], assets[k])
    return total


def associator_entropy(assets):
    """
    Compute the associator entropy of a collection of Octonion-valued assets.

        S = -sum_i p_i * log(p_i)

    where p_i = |[a_i, a_j, a_k]|^2 / Z for each unordered triple (i,j,k)
    and Z = sum of all |[a_i, a_j, a_k]|^2.

    This measures the complexity / uniformity of non-associative interactions
    across the portfolio.  S = 0 for associative (e.g. quaternionic) assets.

    Args:
        assets: list of Octonion instances (length >= 3).

    Returns:
        float -- the associator entropy (non-negative).
    """
    n = len(assets)
    if n < 3:
        raise ValueError("Need at least 3 assets to compute associator entropy")

    weights = []
    for combo in combinations(range(n), 3):
        i, j, k = combo
        w = associator_norm(assets[i], assets[j], assets[k]) ** 2
        weights.append(w)

    Z = sum(weights)
    if Z < 1e-20:
        # Below this threshold the weights are indistinguishable from
        # floating-point noise (e.g. quaternionic assets with ||assoc|| ~ 1e-16).
        return 0.0

    entropy = 0.0
    for w in weights:
        p = w / Z
        if p > 1e-30:
            entropy -= p * np.log(p)
    return float(entropy)


def compare_quaternionic_octonionic(assets_h, assets_o):
    """
    Compare associator entropy between quaternionic and octonionic asset sets.

    Quaternionic assets live in a quaternionic subalgebra of O (spanned by
    {1, e_i, e_j, e_k} for a single Fano triple), where the associator
    vanishes identically.  Octonionic assets span the full algebra and
    generically have non-zero associators.

    Args:
        assets_h: list of Octonion instances confined to a quaternionic
                  subalgebra (entropy will be ~0).
        assets_o: list of Octonion instances spanning the full octonion
                  algebra (entropy generically > 0).

    Returns:
        dict with keys:
            'entropy_quaternionic': float
            'entropy_octonionic': float
            'entropy_ratio': float -- octonionic / quaternionic (inf if
                quaternionic entropy is 0)
            'associator_total_quaternionic': float
            'associator_total_octonionic': float
    """
    ent_h = associator_entropy(assets_h)
    ent_o = associator_entropy(assets_o)
    assoc_h = portfolio_associator(assets_h)
    assoc_o = portfolio_associator(assets_o)

    if ent_h < 1e-30:
        ratio = float('inf') if ent_o > 1e-30 else 1.0
    else:
        ratio = ent_o / ent_h

    return {
        'entropy_quaternionic': ent_h,
        'entropy_octonionic': ent_o,
        'entropy_ratio': ratio,
        'associator_total_quaternionic': assoc_h,
        'associator_total_octonionic': assoc_o,
    }


# ===========================================================================
# 3. Coalition Associator (political / game theory)
# ===========================================================================

def coalition_associator(agents):
    """
    Compute the coalition associator for a collection of agents represented
    as Octonion-valued preference vectors.

    For each unordered triple (i, j, k) the associator
        [A_i, A_j, A_k] = (A_i * A_j) * A_k - A_i * (A_j * A_k)
    measures how much the coalition outcome depends on the grouping order
    (agenda dependence).

    Args:
        agents: list of Octonion instances (length >= 3).

    Returns:
        float -- total coalition associator magnitude (sum over all triples).
    """
    n = len(agents)
    if n < 3:
        raise ValueError("Need at least 3 agents")

    total = 0.0
    for combo in combinations(range(n), 3):
        i, j, k = combo
        total += associator_norm(agents[i], agents[j], agents[k])
    return total


def agenda_dependence_measure(agents):
    """
    Normalised agenda-dependence measure for a triple of agents.

        D(A, B, C) = ||[A, B, C]|| / (||A|| * ||B|| * ||C||)

    This lives in [0, some_max] and equals 0 iff the agents lie in an
    associative subalgebra.  For unit-norm octonionic agents drawn from
    the full algebra, empirical maximum is around 2.

    When more than 3 agents are given, the function returns the *average*
    normalised measure over all unordered triples.

    Args:
        agents: list of Octonion instances (length >= 3).

    Returns:
        float -- average normalised agenda dependence (non-negative).
    """
    n = len(agents)
    if n < 3:
        raise ValueError("Need at least 3 agents")

    total = 0.0
    count = 0
    for combo in combinations(range(n), 3):
        i, j, k = combo
        norms_product = agents[i].norm() * agents[j].norm() * agents[k].norm()
        if norms_product < 1e-30:
            continue
        d = associator_norm(agents[i], agents[j], agents[k]) / norms_product
        total += d
        count += 1

    return total / count if count > 0 else 0.0


def optimal_coalition_ordering(agents):
    """
    Find the permutation of agents that minimises and maximises the total
    sequential coalition associator magnitude.

    For a given ordering (sigma_1, sigma_2, ..., sigma_n), the total
    associator cost is the sum of |[a_{sigma_i}, a_{sigma_{i+1}},
    a_{sigma_{i+2}}]| over consecutive triples.  This measures the total
    agenda dependence along the sequential coalition-formation process.

    For n > 8, the brute-force search becomes infeasible, so a greedy
    heuristic is used instead.

    Args:
        agents: list of Octonion instances (length >= 3).

    Returns:
        dict with keys:
            'min_ordering': tuple of indices minimising total associator cost.
            'min_cost': float -- the minimum total associator cost.
            'max_ordering': tuple of indices maximising total associator cost.
            'max_cost': float -- the maximum total associator cost.
    """
    n = len(agents)
    if n < 3:
        raise ValueError("Need at least 3 agents")

    def _sequential_cost(perm):
        """Sum of associator norms over consecutive triples in a permutation."""
        cost = 0.0
        for t in range(len(perm) - 2):
            cost += associator_norm(
                agents[perm[t]], agents[perm[t + 1]], agents[perm[t + 2]]
            )
        return cost

    if n <= 8:
        # Brute-force over all permutations (feasible up to 8! = 40320)
        best_min = (None, float('inf'))
        best_max = (None, float('-inf'))
        for perm in permutations(range(n)):
            cost = _sequential_cost(perm)
            if cost < best_min[1]:
                best_min = (perm, cost)
            if cost > best_max[1]:
                best_max = (perm, cost)
        return {
            'min_ordering': best_min[0],
            'min_cost': float(best_min[1]),
            'max_ordering': best_max[0],
            'max_cost': float(best_max[1]),
        }
    else:
        # Greedy heuristic for large n
        # Minimisation: greedily pick next agent that minimises the new triple
        indices = list(range(n))

        # --- Minimising ordering ---
        remaining_min = set(indices)
        order_min = [0]
        remaining_min.discard(0)
        # Pick second element: minimise associator with first and any third
        if n > 1:
            best_second = min(remaining_min,
                              key=lambda j: sum(
                                  associator_norm(agents[order_min[0]], agents[j], agents[k])
                                  for k in remaining_min if k != j))
            order_min.append(best_second)
            remaining_min.discard(best_second)

        while remaining_min:
            best_next = min(remaining_min,
                            key=lambda j: associator_norm(
                                agents[order_min[-2]], agents[order_min[-1]], agents[j]))
            order_min.append(best_next)
            remaining_min.discard(best_next)

        # --- Maximising ordering ---
        remaining_max = set(indices)
        order_max = [0]
        remaining_max.discard(0)
        if n > 1:
            best_second = max(remaining_max,
                              key=lambda j: sum(
                                  associator_norm(agents[order_max[0]], agents[j], agents[k])
                                  for k in remaining_max if k != j))
            order_max.append(best_second)
            remaining_max.discard(best_second)

        while remaining_max:
            best_next = max(remaining_max,
                            key=lambda j: associator_norm(
                                agents[order_max[-2]], agents[order_max[-1]], agents[j]))
            order_max.append(best_next)
            remaining_max.discard(best_next)

        return {
            'min_ordering': tuple(order_min),
            'min_cost': float(_sequential_cost(tuple(order_min))),
            'max_ordering': tuple(order_max),
            'max_cost': float(_sequential_cost(tuple(order_max))),
        }
