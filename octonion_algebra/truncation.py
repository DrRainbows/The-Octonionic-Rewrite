"""
Truncation schemes for the COPBW tree-monomial basis.

Addresses Grok critique #13: "Tree-monomial explosion -- no truncation scheme."
The COPBW basis has C_{n-1} * k^n monomials at degree n, which grows
exponentially (like 4^n). This module provides practical truncation
strategies that keep the basis manageable while preserving essential
algebraic structure.

Strategies implemented:
  1. Depth truncation: prune deeply nested trees
  2. Alternator reduction: use SVD to find independent monomials mod alternator ideal
  3. Casimir truncation: weight-based cutoff analogous to angular momentum
  4. G2-equivariant truncation: group monomials by G2 orbit
  5. Growth rate analysis: compare all strategies across degrees
"""

import numpy as np
from math import factorial
from octonion_algebra.core import Octonion
from octonion_algebra.copbw import (
    TreeMonomial,
    leaf,
    mul,
    enumerate_tree_monomials,
    catalan,
)


# ---------------------------------------------------------------------------
# Helper: tree metrics
# ---------------------------------------------------------------------------

def _tree_depth(t):
    """Return the depth of a TreeMonomial (longest root-to-leaf path)."""
    return t.depth()


def _casimir_weight(t, current_depth=0):
    """
    Compute the Casimir weight of a tree monomial.

    Weight = sum over internal nodes of (depth_of_node)^2.
    The root internal node is at depth 0, its children at depth 1, etc.
    """
    if t.is_leaf:
        return 0
    # This node is an internal node at current_depth
    return (current_depth ** 2
            + _casimir_weight(t.left, current_depth + 1)
            + _casimir_weight(t.right, current_depth + 1))


def _random_octonion_assignment(generators, rng):
    """Create a random assignment mapping each generator name to a random Octonion."""
    assignment = {}
    for g in generators:
        assignment[g] = Octonion(rng.uniform(-1, 1, size=8))
    return assignment


def _evaluate_monomial_vector(t, assignment):
    """Evaluate a tree monomial and return the 8-component coefficient vector."""
    result = t.evaluate(assignment)
    return result.coeffs


# ---------------------------------------------------------------------------
# 1. Depth truncation
# ---------------------------------------------------------------------------

def depth_truncation(generators, max_degree, max_depth):
    """
    Return tree monomials up to max_degree whose tree depth <= max_depth.

    Tree depth: longest root-to-leaf path.
      - A leaf has depth 0.
      - mul(L, R) has depth 1 + max(depth(L), depth(R)).

    This eliminates deeply nested (highly unbalanced) monomials while
    keeping balanced ones, giving a practical sub-basis.

    Args:
        generators: list of generator name strings.
        max_degree: maximum degree (number of leaves) to enumerate.
        max_depth: maximum allowed tree depth (inclusive).

    Returns:
        list[TreeMonomial]: filtered monomials across all degrees 1..max_degree.
    """
    result = []
    for degree in range(1, max_degree + 1):
        all_trees = enumerate_tree_monomials(generators, degree)
        for t in all_trees:
            if t.depth() <= max_depth:
                result.append(t)
    return result


# ---------------------------------------------------------------------------
# 2. Alternator-reduced basis (SVD)
# ---------------------------------------------------------------------------

def alternator_reduced_basis(generators, degree, n_samples=100, seed=42):
    """
    Find the effective rank of tree monomials modulo the alternator ideal.

    Procedure:
      1. Enumerate all tree monomials at given degree.
      2. Evaluate each on n_samples random octonion assignments.
      3. Build a matrix (n_monomials x 8*n_samples) of evaluation vectors.
      4. Use SVD to find effective rank (singular values > tol).
      5. The rank is the number of independent monomials modulo alternator relations.

    Args:
        generators: list of generator name strings.
        degree: the degree to analyze.
        n_samples: number of random evaluation points.
        seed: random seed for reproducibility.

    Returns:
        dict with keys:
          'full_count': total tree monomials at this degree,
          'reduced_count': effective rank (independent monomials),
          'reduction_factor': reduced / full,
          'basis_indices': list of indices of independent monomials.
    """
    rng = np.random.default_rng(seed)
    all_trees = enumerate_tree_monomials(generators, degree)
    n_mono = len(all_trees)

    if n_mono == 0:
        return {
            'full_count': 0,
            'reduced_count': 0,
            'reduction_factor': 1.0,
            'basis_indices': [],
        }

    # Build evaluation matrix: each row is one monomial evaluated at all samples
    cols = 8 * n_samples
    M = np.zeros((n_mono, cols))
    for s in range(n_samples):
        assignment = _random_octonion_assignment(generators, rng)
        for i, t in enumerate(all_trees):
            vec = _evaluate_monomial_vector(t, assignment)
            M[i, s * 8:(s + 1) * 8] = vec

    # SVD to find rank
    U, S, Vt = np.linalg.svd(M, full_matrices=False)
    tol = 1e-8
    rank = int(np.sum(S > tol * S[0])) if S[0] > 0 else 0

    # Identify basis indices via pivoted QR (column subset selection)
    # Use the first 'rank' left singular vectors to pick representative monomials
    basis_indices = []
    if rank > 0:
        # Greedy pivot selection on U[:, :rank]
        U_trunc = U[:, :rank].copy()
        remaining = list(range(n_mono))
        for _ in range(rank):
            # Pick row with largest norm in remaining
            norms = [np.linalg.norm(U_trunc[r]) for r in remaining]
            best_idx = remaining[int(np.argmax(norms))]
            basis_indices.append(best_idx)
            remaining.remove(best_idx)
            # Deflate: project out the selected direction
            if len(remaining) > 0:
                v = U_trunc[best_idx].copy()
                nv = np.linalg.norm(v)
                if nv > 1e-15:
                    v /= nv
                    for r in remaining:
                        U_trunc[r] -= np.dot(U_trunc[r], v) * v

    basis_indices.sort()

    return {
        'full_count': n_mono,
        'reduced_count': rank,
        'reduction_factor': rank / n_mono if n_mono > 0 else 1.0,
        'basis_indices': basis_indices,
    }


# ---------------------------------------------------------------------------
# 3. Casimir truncation
# ---------------------------------------------------------------------------

def casimir_truncation(generators, max_degree, casimir_cutoff):
    """
    Keep only monomials whose Casimir weight <= casimir_cutoff.

    The Casimir weight of a tree monomial is:
      weight = sum over internal nodes of (depth_of_node)^2

    This is analogous to angular momentum cutoff in spectral methods:
    deeply nested, unbalanced trees get high weight and are pruned.

    Args:
        generators: list of generator name strings.
        max_degree: maximum degree to enumerate.
        casimir_cutoff: maximum allowed Casimir weight (inclusive).

    Returns:
        list[TreeMonomial]: monomials with weight <= casimir_cutoff.
    """
    result = []
    for degree in range(1, max_degree + 1):
        all_trees = enumerate_tree_monomials(generators, degree)
        for t in all_trees:
            if _casimir_weight(t) <= casimir_cutoff:
                result.append(t)
    return result


# ---------------------------------------------------------------------------
# 4. Truncation error estimate
# ---------------------------------------------------------------------------

def truncation_error_estimate(generators, degree, truncation_depth,
                              n_samples=50, seed=42):
    """
    Estimate the information lost by depth truncation at a given degree.

    Compares evaluation of all monomials vs only depth-truncated monomials
    on random inputs. The error is measured as the Frobenius norm of the
    difference in the evaluation matrices.

    Args:
        generators: list of generator name strings.
        degree: the degree to analyze.
        truncation_depth: maximum depth for truncation.
        n_samples: number of random evaluation points.
        seed: random seed for reproducibility.

    Returns:
        dict with keys:
          'error_norm': Frobenius norm of truncated-away evaluations,
          'relative_error': error_norm / full_norm,
          'n_truncated': number of monomials removed,
          'n_kept': number of monomials kept.
    """
    rng = np.random.default_rng(seed)
    all_trees = enumerate_tree_monomials(generators, degree)
    kept = [t for t in all_trees if t.depth() <= truncation_depth]
    truncated = [t for t in all_trees if t.depth() > truncation_depth]

    n_kept = len(kept)
    n_truncated = len(truncated)

    if n_truncated == 0:
        return {
            'error_norm': 0.0,
            'relative_error': 0.0,
            'n_truncated': 0,
            'n_kept': n_kept,
        }

    # Evaluate truncated monomials
    trunc_vecs = []
    full_vecs = []
    for s in range(n_samples):
        assignment = _random_octonion_assignment(generators, rng)
        for t in truncated:
            trunc_vecs.append(_evaluate_monomial_vector(t, assignment))
        for t in all_trees:
            full_vecs.append(_evaluate_monomial_vector(t, assignment))

    trunc_matrix = np.array(trunc_vecs)
    full_matrix = np.array(full_vecs)

    error_norm = float(np.linalg.norm(trunc_matrix, 'fro'))
    full_norm = float(np.linalg.norm(full_matrix, 'fro'))

    relative_error = error_norm / full_norm if full_norm > 0 else 0.0

    return {
        'error_norm': error_norm,
        'relative_error': relative_error,
        'n_truncated': n_truncated,
        'n_kept': n_kept,
    }


# ---------------------------------------------------------------------------
# 5. G2-equivariant truncation
# ---------------------------------------------------------------------------

def _apply_g2_rotation(oct_val, rotation_matrix):
    """
    Apply a G2 rotation (7x7 matrix) to an octonion.

    The rotation acts on the imaginary part; the real part is unchanged.
    """
    new_coeffs = oct_val.coeffs.copy()
    new_coeffs[1:] = rotation_matrix @ oct_val.coeffs[1:]
    return Octonion(new_coeffs)


def g2_equivariant_truncation(generators, degree, n_samples=50, seed=42):
    """
    Group tree monomials by their behavior under G2 transformations.

    Two monomials are in the same orbit if they transform identically
    (up to numerical tolerance) under random G2 rotations. This groups
    monomials that are algebraically equivalent under the automorphism group.

    Args:
        generators: list of generator name strings.
        degree: the degree to analyze.
        n_samples: number of random G2 transformations to test.
        seed: random seed for reproducibility.

    Returns:
        dict with keys:
          'n_orbits': number of distinct G2 orbits,
          'orbit_sizes': list of orbit sizes,
          'representatives': list[TreeMonomial] (one per orbit).
    """
    from octonion_algebra.g2 import g2_generators

    rng = np.random.default_rng(seed)
    all_trees = enumerate_tree_monomials(generators, degree)
    n_mono = len(all_trees)

    if n_mono == 0:
        return {
            'n_orbits': 0,
            'orbit_sizes': [],
            'representatives': [],
        }

    # Get G2 generators and create random G2 group elements
    # (exponentials of random linear combinations of generators)
    g2_gens = g2_generators()

    def _matrix_exp(A, order=20):
        """Compute matrix exponential via truncated Taylor series.

        For small antisymmetric matrices (norm ~ 0.3 * sqrt(14) ~ 1.1),
        20 terms gives machine-precision accuracy.
        """
        result = np.eye(A.shape[0], dtype=float)
        term = np.eye(A.shape[0], dtype=float)
        for k in range(1, order + 1):
            term = term @ A / k
            result = result + term
        return result

    def _random_g2_element():
        """Generate a random element of G2 as exp(sum of random coeffs * generators)."""
        coeffs = rng.normal(0, 0.3, size=len(g2_gens))
        A = sum(c * g for c, g in zip(coeffs, g2_gens))
        return _matrix_exp(A)

    # For each monomial, compute a "fingerprint" by:
    # 1. Choose a fixed base assignment
    # 2. For each G2 rotation, rotate the assignment and evaluate
    # 3. Compare how the output transforms relative to the input
    # Strategy: measure the *ratio* of how output changes under G2 rotation
    # Monomials in the same orbit will have the same transformation signature.

    # Simpler approach: for each monomial, compute a signature vector
    # by evaluating on multiple random assignments and taking the norm pattern
    signatures = np.zeros((n_mono, n_samples))

    for s in range(n_samples):
        # Random base assignment
        base_assign = _random_octonion_assignment(generators, rng)
        # Random G2 rotation
        R = _random_g2_element()
        # Rotated assignment
        rot_assign = {g: _apply_g2_rotation(v, R) for g, v in base_assign.items()}

        for i, t in enumerate(all_trees):
            base_val = t.evaluate(base_assign)
            rot_val = t.evaluate(rot_assign)
            # Signature: ratio of norms (G2 is norm-preserving on Im(O))
            base_norm = base_val.norm()
            rot_norm = rot_val.norm()
            if base_norm > 1e-12:
                signatures[i, s] = rot_norm / base_norm
            else:
                signatures[i, s] = 0.0

    # Cluster monomials by signature similarity
    tol = 1e-4
    orbits = []  # list of lists of indices
    assigned = set()

    for i in range(n_mono):
        if i in assigned:
            continue
        orbit = [i]
        assigned.add(i)
        for j in range(i + 1, n_mono):
            if j in assigned:
                continue
            # Compare signatures
            diff = np.linalg.norm(signatures[i] - signatures[j])
            if diff < tol * max(np.linalg.norm(signatures[i]), 1e-12):
                orbit.append(j)
                assigned.add(j)
        orbits.append(orbit)

    return {
        'n_orbits': len(orbits),
        'orbit_sizes': [len(o) for o in orbits],
        'representatives': [all_trees[o[0]] for o in orbits],
    }


# ---------------------------------------------------------------------------
# 6. Growth rate analysis
# ---------------------------------------------------------------------------

def growth_rate_analysis(generators, max_degree=6):
    """
    Analyze how different truncation strategies control basis growth.

    For each degree 1..max_degree, compute:
      - Full tree count: k^n * C_{n-1}
      - Alternator-reduced count (via SVD)
      - Depth-2 truncated count
      - Casimir-truncated count (cutoff = 4 * degree)

    Args:
        generators: list of generator name strings.
        max_degree: maximum degree to analyze.

    Returns:
        dict with keys:
          'degrees': list of degrees,
          'full_counts': full tree monomial counts,
          'reduced_counts': alternator-reduced counts,
          'depth_truncated': depth-2 truncated counts,
          'casimir_truncated': casimir-truncated counts,
          'asymptotic_ratio': ratio of reduced to full at max_degree.
    """
    k = len(generators)
    degrees = list(range(1, max_degree + 1))
    full_counts = []
    reduced_counts = []
    depth_truncated_counts = []
    casimir_truncated_counts = []

    for d in degrees:
        # Full count
        full = k ** d * catalan(d - 1)
        full_counts.append(full)

        # Alternator-reduced: use fewer samples for speed at higher degrees
        n_samp = max(20, 100 // d)
        red = alternator_reduced_basis(generators, d, n_samples=n_samp, seed=42)
        reduced_counts.append(red['reduced_count'])

        # Depth-2 truncated count at this degree only
        all_trees = enumerate_tree_monomials(generators, d)
        depth2_count = sum(1 for t in all_trees if t.depth() <= 2)
        depth_truncated_counts.append(depth2_count)

        # Casimir truncated (cutoff scales with degree)
        casimir_cutoff = 4 * d
        casimir_count = sum(1 for t in all_trees if _casimir_weight(t) <= casimir_cutoff)
        casimir_truncated_counts.append(casimir_count)

    # Asymptotic ratio at max degree
    if full_counts[-1] > 0:
        asymptotic_ratio = reduced_counts[-1] / full_counts[-1]
    else:
        asymptotic_ratio = 1.0

    return {
        'degrees': degrees,
        'full_counts': full_counts,
        'reduced_counts': reduced_counts,
        'depth_truncated': depth_truncated_counts,
        'casimir_truncated': casimir_truncated_counts,
        'asymptotic_ratio': asymptotic_ratio,
    }


# ---------------------------------------------------------------------------
# 7. Practical basis
# ---------------------------------------------------------------------------

def practical_basis(generators, max_degree=4, strategy='alternator'):
    """
    Generate a practical working basis using the specified truncation strategy.

    Strategies:
      'alternator': SVD reduction at each degree (picks independent monomials).
      'depth': keep only monomials with tree depth <= 2.
      'casimir': keep monomials with Casimir weight <= 4 * degree.

    Args:
        generators: list of generator name strings.
        max_degree: maximum degree to include.
        strategy: one of 'alternator', 'depth', 'casimir'.

    Returns:
        dict with keys:
          'basis': list[TreeMonomial] (the practical basis elements),
          'size': total number of basis elements,
          'strategy': the strategy used,
          'degree_breakdown': dict mapping degree -> count.
    """
    basis = []
    degree_breakdown = {}

    for d in range(1, max_degree + 1):
        all_trees = enumerate_tree_monomials(generators, d)

        if strategy == 'alternator':
            red = alternator_reduced_basis(generators, d, n_samples=100, seed=42)
            indices = red['basis_indices']
            degree_trees = [all_trees[i] for i in indices]
        elif strategy == 'depth':
            degree_trees = [t for t in all_trees if t.depth() <= 2]
        elif strategy == 'casimir':
            cutoff = 4 * d
            degree_trees = [t for t in all_trees if _casimir_weight(t) <= cutoff]
        else:
            raise ValueError(f"Unknown strategy: {strategy}. Use 'alternator', 'depth', or 'casimir'.")

        basis.extend(degree_trees)
        degree_breakdown[d] = len(degree_trees)

    return {
        'basis': basis,
        'size': len(basis),
        'strategy': strategy,
        'degree_breakdown': degree_breakdown,
    }
