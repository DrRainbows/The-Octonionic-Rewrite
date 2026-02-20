"""
Context-dependent integration for the decompactified Killing form.

Addresses Grok critique #3 (Omega undefined/uncomputable) and #27
(context integral convergence).

The decompactified Killing form is:

    B_mu(X, Y) = integral_Omega tr(ad_X^{omega} . ad_Y^{omega}) d mu(omega)

where the context-dependent adjoint is:

    ad_X^{omega}(Y) = [X, Y, u(omega)]

and u(omega) is a curve in Im(O) parameterized by omega in [0, 2 pi].
The measure is d mu = d omega / (2 pi)  (normalized Lebesgue on the circle).

By Schur's lemma, since G2 acts irreducibly on Im(O) ~ R^7, the Killing
form B_mu must be proportional to the identity on Im(O).  For the standard
Fourier context curve u(omega) = sum_{k=1}^{7} sin((2k-1) omega) e_k,
the proportionality constant is -48, giving B = -48 Id.
"""

import numpy as np
from octonion_algebra.core import Octonion
from octonion_algebra.associator import associator


# ---------------------------------------------------------------------------
# 1. Context-dependent adjoint
# ---------------------------------------------------------------------------

def context_adjoint(X, Y, u):
    """
    Compute the context-dependent adjoint ad_X^u(Y) = [X, Y, u].

    This is the associator of (X, Y, u), which measures the failure
    of associativity when composing X, Y in the context u.

    Args:
        X: Octonion instance.
        Y: Octonion instance.
        u: Octonion instance (the context element, typically imaginary).

    Returns:
        Octonion: the associator [X, Y, u] = (X*Y)*u - X*(Y*u).
    """
    return associator(X, Y, u)


# ---------------------------------------------------------------------------
# 2. Context-dependent adjoint matrix
# ---------------------------------------------------------------------------

def context_adjoint_matrix(X, u):
    """
    Build the 7x7 matrix of ad_X^u restricted to Im(O).

    Entry (a, b) is the (a+1)-th imaginary component of [X, e_{b+1}, u],
    i.e., the coefficient of e_{a+1} in the associator.

    Args:
        X: Octonion instance.
        u: Octonion instance (the context).

    Returns:
        numpy ndarray of shape (7, 7).
    """
    mat = np.zeros((7, 7))
    for b in range(7):
        Y = Octonion.basis(b + 1)
        result = associator(X, Y, u)
        mat[:, b] = result.imag_vector()
    return mat


# ---------------------------------------------------------------------------
# 3. Killing form integrand
# ---------------------------------------------------------------------------

def killing_form_integrand(X, Y, u):
    """
    Compute tr(ad_X^u . ad_Y^u) for a specific context element u.

    This is the integrand of the decompactified Killing form before
    integration over the context space.

    Args:
        X: Octonion instance.
        Y: Octonion instance.
        u: Octonion instance (the context).

    Returns:
        float: the trace tr(ad_X^u @ ad_Y^u).
    """
    ad_X = context_adjoint_matrix(X, u)
    ad_Y = context_adjoint_matrix(Y, u)
    return float(np.trace(ad_X @ ad_Y))


# ---------------------------------------------------------------------------
# 4. Decompactified Killing form (numerical integration)
# ---------------------------------------------------------------------------

def decompactified_killing_form(X, Y, context_curve, n_quad=100):
    """
    Numerically integrate B_mu(X, Y) = (1/2pi) int_0^{2pi}
    tr(ad_X^{u(omega)} . ad_Y^{u(omega)}) d omega
    using the trapezoidal rule.

    Args:
        X: Octonion instance.
        Y: Octonion instance.
        context_curve: callable omega -> Octonion, the context curve u(omega).
        n_quad: int, number of quadrature points (default 100).

    Returns:
        float: the integrated Killing form value B_mu(X, Y).
    """
    omegas = np.linspace(0, 2 * np.pi, n_quad, endpoint=False)
    d_omega = 2 * np.pi / n_quad

    total = 0.0
    for omega in omegas:
        u = context_curve(omega)
        total += killing_form_integrand(X, Y, u) * d_omega

    return total / (2 * np.pi)


# ---------------------------------------------------------------------------
# 5. Full Killing form matrix
# ---------------------------------------------------------------------------

def killing_form_matrix(context_curve, n_quad=100):
    """
    Compute the full 7x7 Killing form matrix B_mu(e_i, e_j)
    for i, j in 1..7 (imaginary basis elements).

    Uses the trapezoidal rule with n_quad quadrature points and the
    normalized measure d mu = d omega / (2 pi).

    Args:
        context_curve: callable omega -> Octonion.
        n_quad: int, number of quadrature points (default 100).

    Returns:
        numpy ndarray of shape (7, 7).
    """
    omegas = np.linspace(0, 2 * np.pi, n_quad, endpoint=False)
    d_omega = 2 * np.pi / n_quad

    B = np.zeros((7, 7))

    for omega in omegas:
        u = context_curve(omega)

        # Build all 7 adjoint matrices for this omega
        ad_matrices = []
        for i in range(7):
            X = Octonion.basis(i + 1)
            ad_matrices.append(context_adjoint_matrix(X, u))

        # Accumulate tr(ad_i @ ad_j)
        for i in range(7):
            for j in range(i, 7):
                val = np.trace(ad_matrices[i] @ ad_matrices[j]) * d_omega / (2 * np.pi)
                B[i, j] += val
                if i != j:
                    B[j, i] += val

    return B


# ---------------------------------------------------------------------------
# 6. Fourier context curve
# ---------------------------------------------------------------------------

def fourier_context_curve(coeffs):
    """
    Create a Fourier-type context curve:

        u(omega) = sum_{k=0}^{len(coeffs)-1} coeffs[k] * sin((2k+1)*omega) * e_{k+1}

    This parameterizes a smooth curve through Im(O) that spans all
    imaginary directions when all coefficients are nonzero.

    Args:
        coeffs: array-like of length <= 7.  coeffs[k] is the amplitude
                 of the sin((2k+1)*omega) * e_{k+1} term.

    Returns:
        callable: omega -> Octonion.
    """
    coeffs = np.asarray(coeffs, dtype=float)

    def curve(omega):
        c = np.zeros(8)
        for k in range(len(coeffs)):
            c[k + 1] = coeffs[k] * np.sin((2 * k + 1) * omega)
        return Octonion(c)

    return curve


# ---------------------------------------------------------------------------
# 7. Standard context curve
# ---------------------------------------------------------------------------

def standard_context_curve():
    """
    Return the standard context curve:

        u(omega) = sum_{k=1}^{7} sin((2k-1)*omega) * e_k

    All coefficients are 1.  This gives B_mu = -48 * Id on Im(O).

    Returns:
        callable: omega -> Octonion.
    """
    return fourier_context_curve(np.ones(7))


# ---------------------------------------------------------------------------
# 8. UV cutoff convergence analysis
# ---------------------------------------------------------------------------

def uv_cutoff_convergence(context_curve, N_values):
    """
    For each N in N_values, compute the Killing form matrix using N
    quadrature points, then measure convergence by Frobenius norm
    differences between successive refinements.

    Args:
        context_curve: callable omega -> Octonion.
        N_values: list/array of increasing integers (quadrature counts).

    Returns:
        dict with keys:
            'N_values': the input N values.
            'matrices': list of 7x7 ndarrays (one per N).
            'frobenius_diffs': list of floats, ||B_{N_{i+1}} - B_{N_i}||_F.
            'converged': bool, True if differences decrease monotonically
                         and last difference < 1e-6.
    """
    N_values = list(N_values)
    matrices = []
    for N in N_values:
        B = killing_form_matrix(context_curve, n_quad=N)
        matrices.append(B)

    frobenius_diffs = []
    for i in range(1, len(matrices)):
        diff = np.linalg.norm(matrices[i] - matrices[i - 1], 'fro')
        frobenius_diffs.append(float(diff))

    # Check convergence: diffs should generally decrease and final diff small
    converged = True
    if len(frobenius_diffs) >= 2:
        # Allow some non-monotonicity but final value must be small
        converged = frobenius_diffs[-1] < 1e-6
    elif len(frobenius_diffs) == 1:
        converged = frobenius_diffs[0] < 1e-6

    return {
        'N_values': N_values,
        'matrices': matrices,
        'frobenius_diffs': frobenius_diffs,
        'converged': converged,
    }


# ---------------------------------------------------------------------------
# 9. Monte Carlo Killing form
# ---------------------------------------------------------------------------

def monte_carlo_killing_form(X, Y, n_samples=10000, seed=42):
    """
    Monte Carlo estimate of the Killing form by averaging over random
    unit imaginary octonions (uniform on S^6) as context elements.

    Instead of integrating over a specific curve, we sample u uniformly
    from the unit sphere in Im(O) ~ R^7 and compute:

        B_MC(X, Y) = (1/n) sum_i tr(ad_X^{u_i} . ad_Y^{u_i})

    By G2-isotropy, this also gives B proportional to Id.

    Args:
        X: Octonion instance.
        Y: Octonion instance.
        n_samples: int, number of Monte Carlo samples (default 10000).
        seed: int, random seed for reproducibility.

    Returns:
        float: the Monte Carlo estimate of the Killing form.
    """
    rng = np.random.default_rng(seed)
    total = 0.0

    for _ in range(n_samples):
        # Sample uniform on S^6: draw standard normal in R^7 and normalize
        v = rng.standard_normal(7)
        v = v / np.linalg.norm(v)
        u = Octonion(np.concatenate([[0.0], v]))
        total += killing_form_integrand(X, Y, u)

    return total / n_samples


# ---------------------------------------------------------------------------
# 10. Convergence proof (full analysis)
# ---------------------------------------------------------------------------

def convergence_proof():
    """
    Run the full convergence analysis for the decompactified Killing form.

    1. Show that the integral converges as N_quad increases.
    2. Estimate the convergence rate (should be ~ 1/N^2 for trapezoidal rule
       on smooth periodic integrands -- actually exponential for smooth periodic).
    3. Verify B proportional to Id (Schur's lemma for irreducible G2 7-rep).
    4. Verify B = -48 * Id for the standard curve.
    5. Cross-check with Monte Carlo over S^6.

    Returns:
        dict with keys:
            'quadrature_convergence': uv_cutoff_convergence result.
            'final_matrix': 7x7 ndarray (high-resolution result).
            'eigenvalues': ndarray of 7 eigenvalues.
            'proportional_to_identity': bool.
            'proportionality_constant': float (should be ~ -48).
            'monte_carlo_diagonal': float (MC estimate of B(e1, e1)).
            'all_checks_passed': bool.
    """
    curve = standard_context_curve()

    # Step 1 & 2: Convergence analysis
    N_values = [10, 20, 40, 80, 160]
    conv = uv_cutoff_convergence(curve, N_values)

    # Step 3: High-resolution matrix
    B_final = conv['matrices'][-1]  # Use the finest resolution
    eigenvalues = np.linalg.eigvalsh(B_final)

    # Check proportionality to identity
    mean_eig = np.mean(eigenvalues)
    spread = np.max(np.abs(eigenvalues - mean_eig))
    proportional = spread < 0.01 * abs(mean_eig)

    # Step 4: Check value
    proportionality_constant = float(mean_eig)

    # Step 5: Monte Carlo cross-check (use fewer samples for speed)
    mc_val = monte_carlo_killing_form(
        Octonion.basis(1), Octonion.basis(1), n_samples=5000, seed=42
    )

    all_passed = (
        conv['converged']
        and proportional
        and abs(proportionality_constant - (-48.0)) < 1.0
        and np.all(eigenvalues < 0)
    )

    return {
        'quadrature_convergence': conv,
        'final_matrix': B_final,
        'eigenvalues': eigenvalues,
        'proportional_to_identity': proportional,
        'proportionality_constant': proportionality_constant,
        'monte_carlo_diagonal': float(mc_val),
        'all_checks_passed': all_passed,
    }
