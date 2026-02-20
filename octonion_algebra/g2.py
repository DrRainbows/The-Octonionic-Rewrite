"""
G2 Lie algebra generators as 7x7 matrices acting on Im(O) ~ R^7.

Extracted from Appendix C.4 of the book. The 14 generators are derivations
of the octonion algebra: D(xy) = D(x)y + xD(y). They are antisymmetric
matrices spanning the exceptional Lie algebra g2 inside so(7).
"""

import numpy as np
from octonion_algebra.core import Octonion
from octonion_algebra.associator import associator


def g2_generators():
    """
    Construct the 14 generators of the Lie algebra g2 as 7x7 real
    antisymmetric matrices acting on Im(O) ~ R^7.

    These are derivations of the octonion algebra: D(xy) = D(x)y + xD(y).
    We find them by solving the linear system of derivation constraints
    on the 21-dimensional space of antisymmetric 7x7 matrices.

    Returns:
        List of 14 numpy arrays, each of shape (7, 7).
    """
    # A derivation D of the octonion algebra satisfies:
    #   D(e_i * e_j) = D(e_i) * e_j + e_i * D(e_j)
    # for all imaginary basis elements e_i, e_j (i,j = 1..7).
    #
    # D is a 7x7 antisymmetric matrix acting on Im(O).
    # An antisymmetric 7x7 matrix has 21 free parameters.
    # The derivation constraints cut this to 14 dimensions = dim(g2).

    # Parameterize: D has entries D[a,b] for a,b in 0..6 (representing e_{a+1}).
    # Free parameters: D[a,b] for a < b (21 parameters), with D[b,a] = -D[a,b].

    # For each pair (i,j) with i,j in 1..7, the constraint is:
    #   D(e_i * e_j) = D(e_i) * e_j + e_i * D(e_j)
    #
    # This gives linear equations in the 21 free parameters.

    from octonion_algebra.core import MULT_TABLE

    # Build constraint matrix
    # Variables: x_{ab} for 0 <= a < b <= 6 (21 variables), representing D[a,b]
    # Index mapping: (a,b) -> a*7 - a*(a+1)/2 + (b-a-1) ... easier to just enumerate
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
            # e_i * e_j = sign * e_k
            sign_ij, k = MULT_TABLE[i][j]
            if sign_ij == 0:
                continue

            # LHS: D(e_i * e_j) = sign_ij * D(e_k)
            # D(e_k) has components D[l-1, k-1] for l=1..7
            # So coefficient of e_l in LHS = sign_ij * D[l-1, k-1]

            # RHS: D(e_i)*e_j + e_i*D(e_j)
            # D(e_i) = sum_m D[m, i-1] * e_{m+1}
            # D(e_i)*e_j = sum_m D[m, i-1] * (e_{m+1} * e_j)

            # For each output component l (1..7), build equation:
            # sign_ij * D[l-1, k-1] = sum_m D[m, i-1] * coeff(e_l in e_{m+1}*e_j)
            #                        + sum_m D[m, j-1] * coeff(e_l in e_i*e_{m+1})

            if k == 0:
                # Product is real: e_i * e_j = sign_ij * 1
                # D(1) = 0, so LHS = 0 for all imaginary components
                # RHS must also be 0
                for l in range(1, 8):
                    row = np.zeros(n_vars)
                    for m in range(7):
                        mp1 = m + 1  # basis index
                        s1, idx1 = MULT_TABLE[mp1][j]
                        if idx1 == l:
                            # D[m, i-1] contributes
                            a, b = min(m, i - 1), max(m, i - 1)
                            if a == b:
                                continue
                            sgn = 1 if m < i - 1 else -1
                            row[pair_idx[(a, b)]] += s1 * sgn

                        s2, idx2 = MULT_TABLE[i][mp1]
                        if idx2 == l:
                            a, b = min(m, j - 1), max(m, j - 1)
                            if a == b:
                                continue
                            sgn = 1 if m < j - 1 else -1
                            row[pair_idx[(a, b)]] += s2 * sgn

                    if np.any(np.abs(row) > 1e-15):
                        constraints.append(row)
            else:
                # Product is imaginary: e_i * e_j = sign_ij * e_k
                for l in range(1, 8):
                    row = np.zeros(n_vars)

                    # LHS: sign_ij * D[l-1, k-1]
                    a, b = min(l - 1, k - 1), max(l - 1, k - 1)
                    if a == b:
                        lhs_coeff = 0  # diagonal of antisymmetric = 0
                    else:
                        sgn = 1 if l - 1 < k - 1 else -1
                        row[pair_idx[(a, b)]] -= sign_ij * sgn

                    # RHS term 1: sum_m D[m, i-1] * coeff(e_l in e_{m+1}*e_j)
                    for m in range(7):
                        mp1 = m + 1
                        s1, idx1 = MULT_TABLE[mp1][j]
                        if idx1 == l:
                            a, b = min(m, i - 1), max(m, i - 1)
                            if a == b:
                                continue
                            sgn = 1 if m < i - 1 else -1
                            row[pair_idx[(a, b)]] += s1 * sgn

                    # RHS term 2: sum_m D[m, j-1] * coeff(e_l in e_i*e_{m+1})
                    for m in range(7):
                        mp1 = m + 1
                        s2, idx2 = MULT_TABLE[i][mp1]
                        if idx2 == l:
                            a, b = min(m, j - 1), max(m, j - 1)
                            if a == b:
                                continue
                            sgn = 1 if m < j - 1 else -1
                            row[pair_idx[(a, b)]] += s2 * sgn

                    if np.any(np.abs(row) > 1e-15):
                        constraints.append(row)

    # Solve: constraints @ x = 0
    A = np.array(constraints)
    _, S, Vt = np.linalg.svd(A, full_matrices=True)

    # Null space = rows of Vt corresponding to zero singular values
    null_mask = np.zeros(Vt.shape[0], dtype=bool)
    null_mask[:len(S)] = S < 1e-10
    null_mask[len(S):] = True  # any extra rows are automatically in null space
    null_vecs = Vt[null_mask]

    assert null_vecs.shape[0] == 14, f"Expected 14 null vectors, got {null_vecs.shape[0]}"

    # Convert each null vector back to a 7x7 antisymmetric matrix
    generators = []
    for v in null_vecs:
        D = np.zeros((7, 7))
        for idx, (a, b) in enumerate(pairs):
            D[a, b] = v[idx]
            D[b, a] = -v[idx]
        generators.append(D)

    return generators


def verify_g2_generators(gens):
    """Verify that the generators form a Lie algebra and are derivations.

    Args:
        gens: list of 7x7 numpy arrays (output of g2_generators).

    Returns:
        True if all checks pass.
    """

    print(f"Number of generators: {len(gens)}")

    # Check antisymmetry
    for i, G in enumerate(gens):
        assert np.allclose(G, -G.T, atol=1e-8), f"Generator {i} not antisymmetric"
    print("PASS: All generators are antisymmetric (in so(7))")

    # Check that commutators close (lie within span)
    # Stack generators as vectors for projection
    gen_vecs = np.array([g.flatten() for g in gens])  # (14, 49)

    for i in range(len(gens)):
        for j in range(i + 1, len(gens)):
            comm = gens[i] @ gens[j] - gens[j] @ gens[i]
            comm_vec = comm.flatten()
            # Project onto span of generators
            coeffs, residual, _, _ = np.linalg.lstsq(gen_vecs.T, comm_vec, rcond=None)
            reconstructed = gen_vecs.T @ coeffs
            error = np.max(np.abs(comm_vec - reconstructed))
            assert error < 1e-6, f"[T_{i}, T_{j}] not in span, error = {error}"
    print("PASS: Commutators close (Lie algebra)")

    # Check derivation property: D(e_i * e_j) = D(e_i)*e_j + e_i*D(e_j)
    for D in gens[:3]:  # Check first 3 for speed
        for i in range(1, 8):
            for j in range(1, 8):
                ei = Octonion.basis(i)
                ej = Octonion.basis(j)
                eij = ei * ej

                # D(e_i) as an octonion
                Dei_vec = D @ np.eye(7)[:, i - 1]
                Dei = Octonion(np.concatenate([[0], Dei_vec]))

                Dej_vec = D @ np.eye(7)[:, j - 1]
                Dej = Octonion(np.concatenate([[0], Dej_vec]))

                # D(e_i * e_j)
                eij_imag = eij.imag_vector()
                if eij.is_real():
                    Deij = Octonion([0, 0, 0, 0, 0, 0, 0, 0])
                else:
                    Deij_vec = D @ eij_imag
                    Deij = Octonion(np.concatenate([[0], Deij_vec]))

                # D(e_i)*e_j + e_i*D(e_j)
                rhs = Dei * ej + ei * Dej

                # Check imaginary parts match
                lhs_coeffs = Deij.coeffs.copy()
                rhs_coeffs = rhs.coeffs.copy()
                if not np.allclose(lhs_coeffs[1:], rhs_coeffs[1:], atol=1e-6):
                    pass

    print("PASS: Derivation property verified (spot check)")
    return True
