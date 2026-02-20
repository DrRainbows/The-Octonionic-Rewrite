"""
Non-associative conservation law machinery from Chapters 16 and 18.

Implements:
- G2 transformations of octonions (infinitesimal and finite)
- Noether variations under G2 generators
- Coherence density, charge, and current
- Evolution under G2-covariant dynamics
- Verification of coherence conservation
- Associator source terms and the modified Noether equation

Key results:
  Theorem 16.1: Generalized Noether Theorem for Alternative Algebras
    partial_mu J^mu = R_D  (modified conservation with associator source)
  Theorem 18.1: G2 invariance of coherence
    C[g . Phi] = C[Phi]  for all g in G2
  Theorem 18.2: Coherence conservation under G2-covariant dynamics
    dC/dt = 0
"""

import numpy as np
from octonion_algebra.core import Octonion
from octonion_algebra.associator import associator
from octonion_algebra.g2 import g2_generators
from octonion_algebra.coherence import coherence_functional, g2_rotate_field, make_smooth_field


def _matrix_exp_taylor(M, order=20):
    """Compute matrix exponential via Taylor series: exp(M) = sum_n M^n/n!

    No scipy dependency.  Sufficient accuracy for small ||M|| with order=20.

    Args:
        M: square numpy array.
        order: number of Taylor terms.

    Returns:
        numpy array of same shape as M.
    """
    result = np.eye(M.shape[0], dtype=float)
    power = np.eye(M.shape[0], dtype=float)
    for n in range(1, order + 1):
        power = power @ M / n
        result = result + power
    return result


# ---------------------------------------------------------------------------
# 1. g2_transform_octonion
# ---------------------------------------------------------------------------

def g2_transform_octonion(o, generator, t=0.01):
    """Apply infinitesimal G2 transformation exp(t * D) to an octonion.

    D is a 7x7 antisymmetric matrix (an element of the g2 Lie algebra)
    acting on Im(O).  The real part of the octonion is unchanged.

    Args:
        o: Octonion instance.
        generator: 7x7 numpy array (G2 Lie algebra element).
        t: float, parameter for the transformation (default 0.01).

    Returns:
        Octonion: the transformed octonion.
    """
    R = _matrix_exp_taylor(t * generator, order=20)
    new_coeffs = np.zeros(8)
    new_coeffs[0] = o.coeffs[0]          # real part unchanged
    new_coeffs[1:] = R @ o.coeffs[1:]    # rotate imaginary part
    return Octonion(new_coeffs)


# ---------------------------------------------------------------------------
# 2. noether_variation
# ---------------------------------------------------------------------------

def noether_variation(field, dx, generator):
    """Compute the Noether variation delta_Phi = D . Phi for each point.

    Under a G2 generator D (a derivation of O), the infinitesimal variation
    of a field element Phi(x) is delta Phi(x) = D(Phi(x)), where D acts on
    the imaginary part of Phi as a 7x7 matrix.

    Args:
        field: list of Octonion instances (discretised 1D field).
        dx: float, grid spacing (unused here but kept for API consistency
            with current-based functions).
        generator: 7x7 numpy array, a g2 Lie algebra element.

    Returns:
        list of Octonion: variations delta Phi at each grid point.
    """
    variations = []
    for phi in field:
        d_imag = generator @ phi.coeffs[1:]
        c = np.zeros(8)
        # D is a derivation of O, so it maps Im(O) -> Im(O); real part is 0.
        c[1:] = d_imag
        variations.append(Octonion(c))
    return variations


# ---------------------------------------------------------------------------
# 3. coherence_current  (1D simplified version)
# ---------------------------------------------------------------------------

def coherence_current(field, dx):
    """Compute the coherence current J_C on a 1D discretised field.

    For a 1D field, the coherence density at site i is
        rho_C(i) = |[Phi(i), Phi(i+1), Phi(i+2)]|^2
    The current is approximated as the finite-difference flux:
        J_C(i) = ( rho_C(i) - rho_C(i-1) ) / dx
    but a more physical definition (following Eq 18.31) uses variations of
    the associator with respect to field translations.

    Here we adopt the simplified 1D version: J_C(i) is a 7-component vector
    derived from the flow of associator content along the lattice.

    J_C(i) = (2/dx) * Re( conj([Phi_i, Phi_{i+1}, Phi_{i+2}])
                              * [Phi_{i+1}, Phi_{i+2}, Phi_{i+3}] )

    evaluated component-wise on the imaginary parts. This captures the
    overlap between consecutive associator "windows" sliding along the field.

    Args:
        field: list of Octonion instances.
        dx: float, grid spacing.

    Returns:
        list of numpy arrays of shape (7,): coherence current at each
        interior point.  Length is len(field) - 3.
    """
    n = len(field)
    currents = []
    for i in range(n - 3):
        assoc_left = associator(field[i], field[i + 1], field[i + 2])
        assoc_right = associator(field[i + 1], field[i + 2], field[i + 3])
        # The coherence current is the "overlap" between consecutive
        # associator windows, projected onto each imaginary direction.
        product = assoc_left.conjugate() * assoc_right
        j_vec = (2.0 / dx) * product.imag_vector()
        currents.append(j_vec)
    return currents


# ---------------------------------------------------------------------------
# 4. coherence_density
# ---------------------------------------------------------------------------

def coherence_density(field):
    """Compute local coherence density rho_C(x) = |[Phi_i, Phi_{i+1}, Phi_{i+2}]|^2.

    Definition 18.2 specialised to the discrete 1D case.

    Args:
        field: list of Octonion instances.

    Returns:
        numpy array of floats, length len(field)-2.
    """
    n = len(field)
    rho = np.zeros(n - 2)
    for i in range(n - 2):
        a = associator(field[i], field[i + 1], field[i + 2])
        rho[i] = a.norm_squared()
    return rho


# ---------------------------------------------------------------------------
# 5. coherence_charge
# ---------------------------------------------------------------------------

def coherence_charge(field):
    """Integrated coherence charge Q_C = sum rho_C(x).

    Theorem 18.3: Q_C >= 0 with equality iff the field is everywhere
    associative.  Q_C is conserved under G2 rotations (Theorem 18.1).

    Args:
        field: list of Octonion instances.

    Returns:
        float: the total coherence charge.
    """
    return float(np.sum(coherence_density(field)))


# ---------------------------------------------------------------------------
# 6. evolve_g2
# ---------------------------------------------------------------------------

def evolve_g2(field, g2_gens, dt, n_steps, seed=0):
    """Evolve a field under G2-covariant dynamics.

    Simple model: at each time step, apply a small random G2 rotation to
    every element of the field.  Since G2 automorphisms preserve the
    associator (Eq 18.16), the coherence functional should be conserved.

    Args:
        field: list of Octonion instances (initial configuration).
        g2_gens: list of 7x7 numpy arrays (G2 generators).
        dt: float, time step size.
        n_steps: int, number of evolution steps.
        seed: int, random seed for reproducibility.

    Returns:
        list of lists of Octonion: field at each time step (length n_steps+1,
        including the initial configuration).
    """
    rng = np.random.default_rng(seed)
    n_gens = len(g2_gens)
    trajectory = [field]

    current_field = field
    for _ in range(n_steps):
        # Random linear combination of G2 generators
        coeffs = rng.standard_normal(n_gens)
        coeffs /= np.linalg.norm(coeffs)  # normalise direction
        current_field = g2_rotate_field(current_field, g2_gens, coeffs, angle=dt)
        trajectory.append(current_field)

    return trajectory


# ---------------------------------------------------------------------------
# 7. verify_coherence_conservation
# ---------------------------------------------------------------------------

def verify_coherence_conservation(field, g2_gens, dt=0.01, n_steps=50, seed=0):
    """Evolve field under G2 dynamics and verify coherence conservation.

    Returns a dict with diagnostic quantities.

    Args:
        field: list of Octonion instances.
        g2_gens: list of 7x7 numpy arrays (G2 generators).
        dt: float, time step.
        n_steps: int, number of steps.
        seed: int, random seed.

    Returns:
        dict with keys:
            'initial_C': float, coherence at t=0
            'final_C': float, coherence at t=n_steps*dt
            'max_deviation': float, max |C(t) - C(0)| over all steps
            'relative_error': float, max_deviation / initial_C
            'trajectory_C': numpy array of C values at each step
    """
    trajectory = evolve_g2(field, g2_gens, dt, n_steps, seed=seed)
    c_values = np.array([coherence_functional(f) for f in trajectory])

    initial_c = c_values[0]
    max_dev = float(np.max(np.abs(c_values - initial_c)))

    return {
        'initial_C': float(initial_c),
        'final_C': float(c_values[-1]),
        'max_deviation': max_dev,
        'relative_error': max_dev / initial_c if initial_c > 0 else 0.0,
        'trajectory_C': c_values,
    }


# ---------------------------------------------------------------------------
# 8. associator_source_term
# ---------------------------------------------------------------------------

def associator_source_term(field, dx, generator):
    """Compute the associator source term R_D from Eq 16.27.

    In the discretised 1D setting, R_D measures how the associator prevents
    exact Noether conservation.  For each interior triple (i, i+1, i+2):

        R_D(i) = Re( conj(D(Phi_i)) * [dPhi_i, dPhi_{i+1}, Phi_i] )

    where dPhi_i = (Phi_{i+1} - Phi_{i-1}) / (2*dx) is the centred
    finite-difference approximation to the field derivative, and D is the
    g2 generator acting on the imaginary part.

    The key property (Theorem 16.1(a)) is that R_D vanishes for fields
    valued in a quaternionic subalgebra H subset O, since all associators
    are then zero.

    Args:
        field: list of Octonion instances (length >= 4).
        dx: float, grid spacing.
        generator: 7x7 numpy array, a g2 generator.

    Returns:
        numpy array of floats, the source term at each interior point.
        Length is len(field)-2 (excludes boundary points that need stencil).
    """
    n = len(field)
    source = np.zeros(n - 2)

    for i in range(1, n - 1):
        # centred finite difference for field derivative
        dphi_coeffs = (field[i + 1].coeffs - field[i - 1].coeffs) / (2.0 * dx)
        dphi = Octonion(dphi_coeffs)

        # D(Phi_i)
        d_imag = generator @ field[i].coeffs[1:]
        d_phi = Octonion(np.concatenate([[0.0], d_imag]))

        # Associator [dphi, Phi_{i+1 or i-1}, Phi_i]
        # Use forward neighbour for the third slot to form a meaningful triple
        if i + 1 < n:
            assoc = associator(dphi, field[min(i + 1, n - 1)], field[i])
        else:
            assoc = associator(dphi, field[i], field[max(i - 1, 0)])

        # R_D(i) = Re( conj(D(Phi)) * assoc )
        product = d_phi.conjugate() * assoc
        source[i - 1] = product.real_part()

    return source


# ---------------------------------------------------------------------------
# 9. noether_divergence_check
# ---------------------------------------------------------------------------

def noether_divergence_check(field, dx, generator):
    """Verify the modified Noether equation: div(J) ~ R_D.

    Computes the discrete divergence of the Noether current and the
    associator source term, then reports how well they match.

    The Noether current in 1D for a free-field-like Lagrangian is:
        J(i) = Re( conj(dPhi_i) * delta_Phi_i )
    where dPhi is the discretised field derivative and delta_Phi = D(Phi).
    The divergence is:
        div J(i) = (J(i+1) - J(i-1)) / (2*dx)

    Args:
        field: list of Octonion instances (length >= 5).
        dx: float, grid spacing.
        generator: 7x7 numpy array, g2 generator.

    Returns:
        dict with keys:
            'divergence': numpy array, div(J) at interior points
            'source': numpy array, R_D at interior points
            'error': numpy array, |div(J) - R_D| at interior points
            'max_error': float
    """
    n = len(field)

    # Compute Noether current J(i) = Re( conj(dPhi_i) * D(Phi_i) )
    # at each point where the derivative stencil is valid.
    j_current = np.zeros(n)
    for i in range(1, n - 1):
        dphi_coeffs = (field[i + 1].coeffs - field[i - 1].coeffs) / (2.0 * dx)
        dphi = Octonion(dphi_coeffs)

        d_imag = generator @ field[i].coeffs[1:]
        delta_phi = Octonion(np.concatenate([[0.0], d_imag]))

        product = dphi.conjugate() * delta_phi
        j_current[i] = product.real_part()

    # Divergence via centred differences
    div_j = np.zeros(n - 4)
    for i in range(2, n - 2):
        div_j[i - 2] = (j_current[i + 1] - j_current[i - 1]) / (2.0 * dx)

    # Source term (trimmed to match)
    source_full = associator_source_term(field, dx, generator)
    # source_full has length n-2, indexed from 0 (corresponding to field index 1).
    # div_j is indexed from field index 2 to n-3.  Source at field index i is
    # source_full[i-1].  So we want source_full[1:-1].
    source = source_full[1:-1] if len(source_full) > 2 else source_full

    # Ensure matching lengths
    min_len = min(len(div_j), len(source))
    div_j = div_j[:min_len]
    source = source[:min_len]

    error = np.abs(div_j - source)

    return {
        'divergence': div_j,
        'source': source,
        'error': error,
        'max_error': float(np.max(error)) if len(error) > 0 else 0.0,
    }
