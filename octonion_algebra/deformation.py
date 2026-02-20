"""
Continuous deformation from quaternions (epsilon=0) to octonions (epsilon=1).

The octonions O have 7 Fano triples defining their multiplication.
The quaternions H use only the triple (1,2,3). We create a continuous
deformation parameter epsilon in [0,1] that interpolates:
  - epsilon = 0: only the (1,2,3) triple is active (quaternionic, associative)
  - epsilon = 1: all 7 Fano triples are active (full octonionic, non-associative)

This gives a smooth family of algebras A_epsilon, enabling study of how
associativity, the Killing form, and the derivation algebra evolve.
"""

import numpy as np
from octonion_algebra.core import Octonion, FANO_TRIPLES, MULT_TABLE


# The quaternionic triple (1-indexed basis labels)
_QUATERNIONIC_TRIPLE = (1, 2, 3)


def deformed_structure_constants(epsilon):
    """
    Return 7x7x7 structure constants f_{ijk}(epsilon) where the quaternionic
    triple (0,1,2) in 0-indexed (i.e. e1,e2,e3) has full strength and the
    other 6 Fano triples are scaled by epsilon.

    Args:
        epsilon: float in [0, 1]. 0 = quaternionic, 1 = octonionic.

    Returns:
        numpy array of shape (7, 7, 7).
    """
    eps = np.zeros((7, 7, 7), dtype=float)
    for triple in FANO_TRIPLES:
        a, b, c = triple
        # Determine the weight: 1 for quaternionic triple, epsilon for others
        weight = 1.0 if triple == _QUATERNIONIC_TRIPLE else float(epsilon)

        # Convert from 1-indexed to 0-indexed
        i, j, k = a - 1, b - 1, c - 1

        # Cyclic permutations are positive
        eps[i, j, k] = +weight
        eps[j, k, i] = +weight
        eps[k, i, j] = +weight
        # Anti-cyclic permutations are negative
        eps[j, i, k] = -weight
        eps[k, j, i] = -weight
        eps[i, k, j] = -weight

    return eps


def _build_deformed_mult_table(epsilon):
    """
    Build the 8x8 deformed multiplication table.

    Returns a list of lists: table[i][j] = (coefficient, index) meaning
    e_i *_eps e_j = coefficient * e_index.

    For the real unit (index 0) all multiplications are unchanged.
    For imaginary x imaginary, the cross-term coefficients from
    non-quaternionic Fano triples are scaled by epsilon.
    """
    table = [[(0.0, 0)] * 8 for _ in range(8)]

    # e_0 * e_0 = 1
    table[0][0] = (1.0, 0)

    # e_0 * e_i = e_i and e_i * e_0 = e_i
    for i in range(1, 8):
        table[0][i] = (1.0, i)
        table[i][0] = (1.0, i)

    # e_i * e_i = -1 for all imaginary basis elements i >= 1.
    # This is a fundamental property of the normed algebra and is not deformed.
    for i in range(1, 8):
        table[i][i] = (-1.0, 0)

    # Fano plane triples with deformation
    for triple in FANO_TRIPLES:
        i, j, k = triple
        weight = 1.0 if triple == _QUATERNIONIC_TRIPLE else float(epsilon)

        # Cyclic: e_i * e_j = +weight * e_k
        table[i][j] = (weight, k)
        table[j][k] = (weight, i)
        table[k][i] = (weight, j)
        # Anti-cyclic: e_j * e_i = -weight * e_k
        table[j][i] = (-weight, k)
        table[k][j] = (-weight, i)
        table[i][k] = (-weight, j)

    return table


def deformed_multiply(a_coeffs, b_coeffs, epsilon):
    """
    Multiply two 8-component arrays using deformed structure constants.

    The real part multiplication is unchanged; only the imaginary cross-terms
    use deformed constants.

    Args:
        a_coeffs: array-like of 8 floats.
        b_coeffs: array-like of 8 floats.
        epsilon: deformation parameter in [0, 1].

    Returns:
        numpy array of shape (8,): the product coefficients.
    """
    a = np.asarray(a_coeffs, dtype=float)
    b = np.asarray(b_coeffs, dtype=float)
    table = _build_deformed_mult_table(epsilon)

    result = np.zeros(8)
    for i in range(8):
        if abs(a[i]) < 1e-15:
            continue
        for j in range(8):
            if abs(b[j]) < 1e-15:
                continue
            coeff, idx = table[i][j]
            result[idx] += coeff * a[i] * b[j]

    return result


class DeformedOctonion:
    """
    An element of the deformed algebra A_epsilon.

    At epsilon=0 this is the quaternions embedded in 8D.
    At epsilon=1 this is the full octonion algebra.

    Attributes:
        coeffs: numpy array of shape (8,).
        epsilon: deformation parameter in [0, 1].
    """

    def __init__(self, coeffs=None, epsilon=1.0):
        if coeffs is not None:
            self.coeffs = np.array(coeffs, dtype=float)
            assert self.coeffs.shape == (8,), "Requires exactly 8 components"
        else:
            self.coeffs = np.zeros(8)
        self.epsilon = float(epsilon)

    @classmethod
    def basis(cls, i, epsilon=1.0):
        """Return the i-th basis element."""
        c = np.zeros(8)
        c[i] = 1.0
        return cls(c, epsilon=epsilon)

    @classmethod
    def random(cls, epsilon=1.0, seed=None):
        """Return a random element with components in [-1, 1]."""
        rng = np.random.default_rng(seed)
        return cls(rng.uniform(-1, 1, size=8), epsilon=epsilon)

    @classmethod
    def random_unit(cls, epsilon=1.0, seed=None):
        """Return a random unit-norm element."""
        o = cls.random(epsilon=epsilon, seed=seed)
        n = o.norm()
        if n < 1e-15:
            return cls.basis(0, epsilon=epsilon)
        return cls(o.coeffs / n, epsilon=epsilon)

    def __repr__(self):
        parts = []
        names = ['1', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7']
        for i, (c, n) in enumerate(zip(self.coeffs, names)):
            if abs(c) < 1e-12:
                continue
            if i == 0:
                parts.append(f"{c:.6g}")
            else:
                parts.append(f"{c:+.6g}*{n}")
        label = ' '.join(parts) if parts else '0'
        return f"DeformedOctonion({label}, eps={self.epsilon})"

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return DeformedOctonion(self.coeffs * other, epsilon=self.epsilon)
        if isinstance(other, DeformedOctonion):
            assert abs(self.epsilon - other.epsilon) < 1e-15, \
                "Cannot multiply DeformedOctonions with different epsilon"
            result = deformed_multiply(self.coeffs, other.coeffs, self.epsilon)
            return DeformedOctonion(result, epsilon=self.epsilon)
        return NotImplemented

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return DeformedOctonion(self.coeffs * other, epsilon=self.epsilon)
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, (int, float)):
            c = self.coeffs.copy()
            c[0] += other
            return DeformedOctonion(c, epsilon=self.epsilon)
        if isinstance(other, DeformedOctonion):
            return DeformedOctonion(self.coeffs + other.coeffs, epsilon=self.epsilon)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            c = self.coeffs.copy()
            c[0] -= other
            return DeformedOctonion(c, epsilon=self.epsilon)
        if isinstance(other, DeformedOctonion):
            return DeformedOctonion(self.coeffs - other.coeffs, epsilon=self.epsilon)
        return NotImplemented

    def __neg__(self):
        return DeformedOctonion(-self.coeffs, epsilon=self.epsilon)

    def conjugate(self):
        """Return the conjugate: x0 - x1*e1 - ... - x7*e7."""
        c = self.coeffs.copy()
        c[1:] = -c[1:]
        return DeformedOctonion(c, epsilon=self.epsilon)

    def norm_squared(self):
        """Return |x|^2 = sum of squares of all components."""
        return np.dot(self.coeffs, self.coeffs)

    def norm(self):
        """Return |x| = sqrt(sum of squares)."""
        return np.sqrt(self.norm_squared())

    def associator(self, b, c):
        """Compute [self, b, c]_eps = (self *_eps b) *_eps c - self *_eps (b *_eps c)."""
        return (self * b) * c - self * (b * c)


def deformed_associator(a, b, c, epsilon):
    """
    Compute the deformed associator [a, b, c]_epsilon.

    [a,b,c]_eps = (a *_eps b) *_eps c - a *_eps (b *_eps c)

    At epsilon=0 this should be zero for inputs in the quaternionic
    subalgebra spanned by {1, e1, e2, e3}.

    Args:
        a, b, c: DeformedOctonion instances or 8-component arrays.
        epsilon: deformation parameter.

    Returns:
        DeformedOctonion: the associator.
    """
    if not isinstance(a, DeformedOctonion):
        a = DeformedOctonion(a, epsilon=epsilon)
    if not isinstance(b, DeformedOctonion):
        b = DeformedOctonion(b, epsilon=epsilon)
    if not isinstance(c, DeformedOctonion):
        c = DeformedOctonion(c, epsilon=epsilon)
    return a.associator(b, c)


def associativity_measure(epsilon, n_samples=200, seed=42):
    """
    Average ||[a,b,c]_epsilon|| over random unit elements of A_epsilon.

    The sampling space is smoothly deformed: the non-quaternionic components
    (e4..e7) of each random element are scaled by epsilon. This ensures:
      - At epsilon=0, only quaternionic elements are sampled, and the
        deformed product restricted to the quaternionic subalgebra is
        associative, giving measure 0.
      - At epsilon=1, random elements span all 8 dimensions, giving the
        full octonionic associativity measure.

    Args:
        epsilon: deformation parameter in [0, 1].
        n_samples: number of random triples to sample.
        seed: random seed for reproducibility.

    Returns:
        float: the average associator norm.
    """
    rng = np.random.default_rng(seed)
    total = 0.0

    # Weighting mask: components 0-3 (quaternionic) always active,
    # components 4-7 (non-quaternionic) scaled by epsilon.
    weight_mask = np.array([1.0, 1.0, 1.0, 1.0,
                            float(epsilon), float(epsilon),
                            float(epsilon), float(epsilon)])

    for i in range(n_samples):
        # Generate random elements with epsilon-weighted components
        a_raw = rng.standard_normal(8) * weight_mask
        norm_a = np.linalg.norm(a_raw)
        if norm_a > 1e-15:
            a_raw /= norm_a

        b_raw = rng.standard_normal(8) * weight_mask
        norm_b = np.linalg.norm(b_raw)
        if norm_b > 1e-15:
            b_raw /= norm_b

        c_raw = rng.standard_normal(8) * weight_mask
        norm_c = np.linalg.norm(c_raw)
        if norm_c > 1e-15:
            c_raw /= norm_c

        a = DeformedOctonion(a_raw, epsilon=epsilon)
        b = DeformedOctonion(b_raw, epsilon=epsilon)
        c = DeformedOctonion(c_raw, epsilon=epsilon)

        assoc = a.associator(b, c)
        total += assoc.norm()

    return total / n_samples


def killing_form_spectral_flow(epsilon_values=None):
    """
    For each epsilon, compute the Killing-like form on the 7 imaginary
    directions via left multiplication matrices.

    For each basis element e_i (i=1..7), the left multiplication map
    L_{e_i} acts on the full 8D space. We compute
    B(e_i, e_j) = tr(L_{e_i} @ L_{e_j}) and return the 7 eigenvalues
    of the 7x7 matrix B as a function of epsilon.

    At epsilon=0 the quaternionic directions (e1,e2,e3) should give
    eigenvalue -8 and extra directions contribute differently.
    At epsilon=1 all eigenvalues should be -8.

    Args:
        epsilon_values: array-like of epsilon values.
            Defaults to np.linspace(0, 1, 11).

    Returns:
        dict with keys:
            'epsilon': array of epsilon values
            'eigenvalues': array of shape (len(epsilon_values), 7),
                sorted eigenvalues for each epsilon.
    """
    if epsilon_values is None:
        epsilon_values = np.linspace(0, 1, 11)
    epsilon_values = np.asarray(epsilon_values)

    all_eigs = []
    for eps_val in epsilon_values:
        table = _build_deformed_mult_table(eps_val)

        # Build left multiplication matrices L_{e_i} for i=1..7
        # L_{e_i} is an 8x8 matrix: (L_{e_i})_{k,j} = coefficient when
        # e_i * e_j has component in e_k direction
        L_matrices = []
        for i in range(1, 8):
            L = np.zeros((8, 8))
            for j in range(8):
                coeff, idx = table[i][j]
                L[idx, j] += coeff
            L_matrices.append(L)

        # Compute the Killing-like form B(e_i, e_j) = tr(L_{e_i} @ L_{e_j})
        B = np.zeros((7, 7))
        for a in range(7):
            for b in range(7):
                B[a, b] = np.trace(L_matrices[a] @ L_matrices[b])

        eigs = np.sort(np.linalg.eigvalsh(B))
        all_eigs.append(eigs)

    return {
        'epsilon': epsilon_values,
        'eigenvalues': np.array(all_eigs),
    }


def derivation_dimension(epsilon, tol=1e-6):
    """
    Compute the dimension of Der(A_epsilon) by solving the derivation
    constraint D(a *_eps b) = D(a) *_eps b + a *_eps D(b) as a linear system
    over 7x7 antisymmetric matrices.

    At epsilon=0 this is 9 = so(3) + so(4), because the 4 null imaginary
    directions e4-e7 (whose cross-products vanish) admit an so(4) of trivial
    derivations, plus so(3) from the quaternionic subalgebra.
    At epsilon=1 this is 14 (g2, derivations of the full octonion algebra).

    Args:
        epsilon: deformation parameter in [0, 1].
        tol: singular value threshold for null space detection.

    Returns:
        int: dimension of the derivation algebra.
    """
    table = _build_deformed_mult_table(epsilon)

    # A derivation D is a 7x7 antisymmetric matrix acting on Im(A_eps) ~ R^7.
    # D has 21 free parameters (upper triangle of antisymmetric matrix).
    # Constraint: D(e_i *_eps e_j) = D(e_i) *_eps e_j + e_i *_eps D(e_j)
    # for all i, j = 1..7.

    # Index the 21 free parameters
    pairs = []
    pair_idx = {}
    for a in range(7):
        for b in range(a + 1, 7):
            pair_idx[(a, b)] = len(pairs)
            pairs.append((a, b))
    n_vars = len(pairs)  # 21

    constraints = []

    for i in range(1, 8):
        for j in range(1, 8):
            if i == j:
                continue
            # e_i *_eps e_j
            coeff_ij, k = table[i][j]
            if coeff_ij == 0.0:
                # No product relation for this pair at this epsilon
                # The constraint is: 0 = D(e_i)*e_j + e_i*D(e_j)
                # which in the output component l means:
                for l in range(1, 8):
                    row = np.zeros(n_vars)
                    for m in range(7):
                        mp1 = m + 1  # 1-indexed basis
                        s1, idx1 = table[mp1][j]
                        if idx1 == l:
                            a_idx, b_idx = min(m, i - 1), max(m, i - 1)
                            if a_idx == b_idx:
                                continue
                            sgn = 1 if m < i - 1 else -1
                            row[pair_idx[(a_idx, b_idx)]] += s1 * sgn

                        s2, idx2 = table[i][mp1]
                        if idx2 == l:
                            a_idx, b_idx = min(m, j - 1), max(m, j - 1)
                            if a_idx == b_idx:
                                continue
                            sgn = 1 if m < j - 1 else -1
                            row[pair_idx[(a_idx, b_idx)]] += s2 * sgn

                    if np.any(np.abs(row) > 1e-15):
                        constraints.append(row)
                continue

            if k == 0:
                # Product is real: e_i *_eps e_j = coeff_ij * 1
                # D(1) = 0, so LHS = 0 for all imaginary components
                for l in range(1, 8):
                    row = np.zeros(n_vars)
                    for m in range(7):
                        mp1 = m + 1
                        s1, idx1 = table[mp1][j]
                        if idx1 == l:
                            a_idx, b_idx = min(m, i - 1), max(m, i - 1)
                            if a_idx == b_idx:
                                continue
                            sgn = 1 if m < i - 1 else -1
                            row[pair_idx[(a_idx, b_idx)]] += s1 * sgn

                        s2, idx2 = table[i][mp1]
                        if idx2 == l:
                            a_idx, b_idx = min(m, j - 1), max(m, j - 1)
                            if a_idx == b_idx:
                                continue
                            sgn = 1 if m < j - 1 else -1
                            row[pair_idx[(a_idx, b_idx)]] += s2 * sgn

                    if np.any(np.abs(row) > 1e-15):
                        constraints.append(row)
            else:
                # Product is imaginary: e_i *_eps e_j = coeff_ij * e_k
                for l in range(1, 8):
                    row = np.zeros(n_vars)

                    # LHS: coeff_ij * D[l-1, k-1]
                    a_idx, b_idx = min(l - 1, k - 1), max(l - 1, k - 1)
                    if a_idx != b_idx:
                        sgn = 1 if l - 1 < k - 1 else -1
                        row[pair_idx[(a_idx, b_idx)]] -= coeff_ij * sgn

                    # RHS term 1: sum_m D[m, i-1] * coeff(e_l in e_{m+1} *_eps e_j)
                    for m in range(7):
                        mp1 = m + 1
                        s1, idx1 = table[mp1][j]
                        if idx1 == l:
                            a_idx, b_idx = min(m, i - 1), max(m, i - 1)
                            if a_idx == b_idx:
                                continue
                            sgn = 1 if m < i - 1 else -1
                            row[pair_idx[(a_idx, b_idx)]] += s1 * sgn

                    # RHS term 2: sum_m D[m, j-1] * coeff(e_l in e_i *_eps e_{m+1})
                    for m in range(7):
                        mp1 = m + 1
                        s2, idx2 = table[i][mp1]
                        if idx2 == l:
                            a_idx, b_idx = min(m, j - 1), max(m, j - 1)
                            if a_idx == b_idx:
                                continue
                            sgn = 1 if m < j - 1 else -1
                            row[pair_idx[(a_idx, b_idx)]] += s2 * sgn

                    if np.any(np.abs(row) > 1e-15):
                        constraints.append(row)

    if len(constraints) == 0:
        # No constraints means all 21 dimensions are free
        return n_vars

    A = np.array(constraints)
    _, S, Vt = np.linalg.svd(A, full_matrices=True)

    # Null space dimension = number of singular values below tolerance
    # plus any extra rows of Vt beyond S
    n_nonzero = np.sum(S > tol)
    null_dim = Vt.shape[0] - n_nonzero
    return int(null_dim)


def deformation_summary(n_epsilon=11):
    """
    Compute a summary table of deformation quantities for
    epsilon = 0, 1/(n_epsilon-1), ..., 1.

    Returns:
        dict with keys:
            'epsilon': list of epsilon values
            'associativity_measure': list of average associator norms
            'derivation_dimension': list of Der dimensions
            'killing_eigenvalues': list of 7-eigenvalue arrays
    """
    eps_vals = np.linspace(0, 1, n_epsilon)
    assoc_measures = []
    der_dims = []

    # Compute Killing form spectral flow in one call
    killing = killing_form_spectral_flow(eps_vals)

    for i, eps_val in enumerate(eps_vals):
        assoc_measures.append(associativity_measure(eps_val, n_samples=50, seed=42))
        der_dims.append(derivation_dimension(eps_val))

    return {
        'epsilon': eps_vals.tolist(),
        'associativity_measure': assoc_measures,
        'derivation_dimension': der_dims,
        'killing_eigenvalues': killing['eigenvalues'].tolist(),
    }
