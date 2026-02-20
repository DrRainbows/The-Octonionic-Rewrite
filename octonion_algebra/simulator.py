"""
7D Octonionic Physics Simulation Engine.

A working simulation engine that evolves octonionic field equations on
1D spatial grids and produces numpy arrays suitable for plotting/analysis.

Every simulation includes an epsilon=0 (associative/quaternionic) baseline
for comparison with the full octonionic (epsilon=1) dynamics.

Mathematical context
--------------------
The octonionic Klein-Gordon equation on a 1D lattice:

    d^2 phi/dt^2 = Lap(phi) - m^2 phi - epsilon * A[phi]

where A[phi] is the associator self-interaction:

    A[phi](x) = [phi(x-dx), phi(x), phi(x+dx)]_eps

computed using the deformed multiplication at parameter epsilon in [0,1].
At epsilon=0, A vanishes (quaternionic/associative limit) and the equation
reduces to the standard Klein-Gordon equation.  At epsilon=1 the full
non-associative corrections are present.

The 7D Maxwell equations on the same lattice:

    dE/dt = curl_7(B) - J_assoc(epsilon)
    dB/dt = -curl_7(E)

where curl_7 uses the octonionic structure constants c_{ijk} from the
Fano plane, and J_assoc is the non-associative current from the Fano
correction tensor (Ch 29).

Coherence charge Q_C = sum_i |[phi(i), phi(i+1), phi(i+2)]|^2 is
conserved under G2-covariant dynamics (Theorem 18.2).

References
----------
- Chapter 11:  Octonionic calculus, structure constants
- Chapter 16:  Noether theorem for alternative algebras
- Chapter 18:  Coherence conservation under G2
- Chapter 29:  7D Maxwell equations, Poynting vector
- Chapters 28-33: Field equations in 7D
"""

import numpy as np

from octonion_algebra.core import Octonion, FANO_TRIPLES
from octonion_algebra.calculus import structure_constants, fano_correction_tensor
from octonion_algebra.deformation import (
    deformed_multiply,
    DeformedOctonion,
    deformed_structure_constants,
)
from octonion_algebra.time_evolution import (
    evolve_klein_gordon as _base_evolve_kg,
    compute_energy as _base_compute_energy,
)
from octonion_algebra.field_equations import poynting_7d


# ---------------------------------------------------------------------------
# Vectorised helpers
# ---------------------------------------------------------------------------

def _oct_multiply_array(a, b):
    """Multiply two (N, 8) arrays element-wise using the Fano multiplication table.

    This is a vectorised version of single-octonion multiplication that
    operates on entire field arrays at once using numpy broadcasting.

    Parameters
    ----------
    a, b : ndarray, shape (N, 8)

    Returns
    -------
    ndarray, shape (N, 8)
    """
    from octonion_algebra.core import MULT_TABLE

    result = np.zeros_like(a)
    for i in range(8):
        ai = a[:, i]
        for j in range(8):
            bj = b[:, j]
            sign, idx = MULT_TABLE[i][j]
            if sign != 0:
                result[:, idx] += sign * ai * bj
    return result


def _deformed_multiply_array(a, b, epsilon):
    """Multiply two (N, 8) arrays using deformed structure constants.

    At epsilon=0 only the quaternionic triple (1,2,3) is active.
    At epsilon=1 this equals the full octonionic product.

    Parameters
    ----------
    a, b : ndarray, shape (N, 8)
    epsilon : float in [0, 1]

    Returns
    -------
    ndarray, shape (N, 8)
    """
    from octonion_algebra.deformation import _build_deformed_mult_table

    table = _build_deformed_mult_table(epsilon)
    result = np.zeros_like(a)
    for i in range(8):
        ai = a[:, i]
        for j in range(8):
            bj = b[:, j]
            coeff, idx = table[i][j]
            if abs(coeff) > 1e-15:
                result[:, idx] += coeff * ai * bj
    return result


def _compute_laplacian(phi, dx):
    """Discrete 1D Laplacian with Dirichlet (zero-ghost) boundaries.

    Uses the standard 3-point stencil, consistent with the leapfrog
    integrator in time_evolution.py so the symplectic energy is exact.

    Parameters
    ----------
    phi : ndarray, shape (N, C)  where C is the number of components
    dx  : float

    Returns
    -------
    ndarray, same shape as phi
    """
    lap = np.zeros_like(phi)
    lap[1:-1] = (phi[2:] - 2.0 * phi[1:-1] + phi[:-2]) / (dx ** 2)
    # Dirichlet ghost: phi[-1] = phi[N] = 0
    lap[0] = (phi[1] - 2.0 * phi[0]) / (dx ** 2)
    lap[-1] = (phi[-2] - 2.0 * phi[-1]) / (dx ** 2)
    return lap


def _associator_correction(phi, dx, epsilon):
    """Compute the associator self-interaction for each grid point.

    A[phi](x_i) = [phi(x_{i-1}), phi(x_i), phi(x_{i+1})]_epsilon

    using the deformed product.  At interior points we use the standard
    stencil; at boundaries we use one-sided triples so that the output
    array has the same shape as phi.

    Parameters
    ----------
    phi     : ndarray, shape (N, 8)
    dx      : float  (unused numerically, kept for interface consistency)
    epsilon : float in [0, 1]

    Returns
    -------
    ndarray, shape (N, 8) -- the associator at each grid point.
    """
    N = phi.shape[0]
    assoc = np.zeros_like(phi)

    if N < 3 or abs(epsilon) < 1e-15:
        return assoc

    # Interior points: [phi(i-1), phi(i), phi(i+1)]
    a = phi[:-2]   # (N-2, 8)
    b = phi[1:-1]  # (N-2, 8)
    c = phi[2:]    # (N-2, 8)

    ab = _deformed_multiply_array(a, b, epsilon)
    bc = _deformed_multiply_array(b, c, epsilon)
    ab_c = _deformed_multiply_array(ab, c, epsilon)
    a_bc = _deformed_multiply_array(a, bc, epsilon)

    assoc[1:-1] = ab_c - a_bc

    # Boundary: use the nearest interior triple
    assoc[0] = assoc[1]
    assoc[-1] = assoc[-2]

    return assoc


# ===================================================================
# OctonionicFieldSimulator
# ===================================================================

class OctonionicFieldSimulator:
    """1D simulation engine for octonionic field dynamics.

    Initialise with grid parameters, then call the individual evolution
    methods to produce time-series data as numpy arrays.

    Parameters
    ----------
    N  : int
        Number of spatial grid points (default 64).
    dt : float
        Time step (default 0.01).
    L  : float
        Spatial extent of the domain [0, L] (default 10.0).
    m_squared : float
        Mass-squared parameter for Klein-Gordon (default 1.0).

    Attributes
    ----------
    x      : ndarray, shape (N,)   -- spatial grid
    dx     : float                 -- grid spacing L / N
    fields : dict                  -- named field arrays, each (N, 8) or (N, 7)
    """

    def __init__(self, N=64, dt=0.01, L=10.0, m_squared=1.0):
        self.N = N
        self.dt = dt
        self.L = L
        self.dx = L / N
        self.m_squared = m_squared
        self.x = np.linspace(0, L - self.dx, N)
        self.fields = {}

    # ------------------------------------------------------------------
    # Initial-condition helpers
    # ------------------------------------------------------------------

    def gaussian_pulse(self, sigma=None, center=None, components=None):
        """Create a Gaussian initial condition for the octonion field.

        Each excited component gets a slightly shifted centre and
        a different mode modulation so that neighbouring grid points
        are NOT proportional octonions.  This ensures the associator
        is nonzero and non-associative dynamics are actually triggered.

        Parameters
        ----------
        sigma      : float, default L/10
        center     : float, default L/2
        components : list of int, which of the 8 components to excite
                     (default [0, 1] -- real + e1).

        Returns
        -------
        phi0 : ndarray, shape (N, 8)
        """
        if sigma is None:
            sigma = self.L / 10.0
        if center is None:
            center = self.L / 2.0
        if components is None:
            components = [0, 1]

        phi0 = np.zeros((self.N, 8))
        for idx, c in enumerate(components):
            # Shift centre and modulate so each component varies differently
            shift = 0.3 * sigma * idx
            freq = 1.0 + 0.5 * idx
            envelope = np.exp(
                -((self.x - center - shift) ** 2) / (2 * sigma ** 2)
            )
            modulation = np.cos(freq * np.pi * self.x / self.L)
            phi0[:, c] = envelope * modulation
        return phi0

    def sine_mode(self, mode=1, components=None):
        """Create a standing-wave initial condition sin(mode * pi * x / L).

        Parameters
        ----------
        mode       : int, mode number (default 1)
        components : list of int, default [0]

        Returns
        -------
        phi0 : ndarray, shape (N, 8)
        """
        if components is None:
            components = [0]
        phi0 = np.zeros((self.N, 8))
        for c in components:
            phi0[:, c] = np.sin(mode * np.pi * self.x / self.L)
        return phi0

    def random_field(self, amplitude=0.1, seed=42):
        """Create a smoothed random octonionic field.

        The field is generated from random Fourier modes with a k^{-2}
        power spectrum so that the gradient energy is finite.

        Parameters
        ----------
        amplitude : float
        seed      : int

        Returns
        -------
        phi0 : ndarray, shape (N, 8)
        """
        rng = np.random.default_rng(seed)
        phi0 = np.zeros((self.N, 8))
        for c in range(8):
            # Random Fourier coefficients with k^{-2} damping
            modes = rng.standard_normal(self.N // 2)
            field_c = np.zeros(self.N)
            for k in range(1, self.N // 2):
                field_c += modes[k] * np.sin(
                    2 * np.pi * k * self.x / self.L
                ) / (k ** 2)
            phi0[:, c] = amplitude * field_c
        return phi0

    # ==================================================================
    # 1.  Klein-Gordon evolution with associator correction
    # ==================================================================

    def evolve_klein_gordon(self, phi0, pi0=None, steps=200, epsilon=1.0):
        """Evolve the octonionic Klein-Gordon equation.

        Uses symplectic leapfrog (Stormer-Verlet) time-stepping so that
        energy is conserved to O(dt^2) with no secular drift.

        The equation of motion is:

            d^2 phi/dt^2 = Lap(phi) - m^2 phi
                           - epsilon * alpha * [phi(x-dx), phi(x), phi(x+dx)]

        where alpha is a coupling constant chosen so that the associator
        correction is perturbative (alpha = 0.01 * dx^2).

        Parameters
        ----------
        phi0    : ndarray, shape (N, 8) -- initial field
        pi0     : ndarray, shape (N, 8) or None (zero momentum)
        steps   : int -- number of time steps
        epsilon : float in [0, 1] -- deformation parameter.
                  0 = associative (quaternionic) limit.
                  1 = full octonionic dynamics.

        Returns
        -------
        dict with keys:
            'phi_history'    : ndarray, shape (steps+1, N, 8)
            'pi_history'     : ndarray, shape (steps+1, N, 8)
            'energy_history' : ndarray, shape (steps+1,)
            'times'          : ndarray, shape (steps+1,)
            'epsilon'        : float
        """
        phi = np.array(phi0, dtype=float)
        if pi0 is None:
            pi = np.zeros_like(phi)
        else:
            pi = np.array(pi0, dtype=float)

        dt = self.dt
        dx = self.dx
        m2 = self.m_squared

        # Coupling for the associator correction -- perturbative but visible.
        # Scaled by dx^2 for dimensional consistency (associator has 3 field
        # factors, the Laplacian has 1/dx^2, so alpha ~ dx^2 keeps the ratio
        # of associator to Laplacian terms resolution-independent).
        alpha = 0.1 * dx ** 2

        # Preallocate history arrays for speed
        phi_hist = np.empty((steps + 1, self.N, 8))
        pi_hist = np.empty((steps + 1, self.N, 8))
        energy_hist = np.empty(steps + 1)

        phi_hist[0] = phi
        pi_hist[0] = pi
        energy_hist[0] = self._kg_energy(phi, pi)

        for n in range(steps):
            # Force F(phi) = Lap(phi) - m^2 phi - alpha * A[phi]
            force = (
                _compute_laplacian(phi, dx)
                - m2 * phi
                - alpha * _associator_correction(phi, dx, epsilon)
            )

            # Leapfrog: half-kick, drift, half-kick
            pi_half = pi + 0.5 * dt * force
            phi_new = phi + dt * pi_half

            force_new = (
                _compute_laplacian(phi_new, dx)
                - m2 * phi_new
                - alpha * _associator_correction(phi_new, dx, epsilon)
            )
            pi_new = pi_half + 0.5 * dt * force_new

            phi = phi_new
            pi = pi_new

            phi_hist[n + 1] = phi
            pi_hist[n + 1] = pi
            energy_hist[n + 1] = self._kg_energy(phi, pi)

        times = np.arange(steps + 1) * dt

        return {
            'phi_history': phi_hist,
            'pi_history': pi_hist,
            'energy_history': energy_hist,
            'times': times,
            'epsilon': epsilon,
        }

    def _kg_energy(self, phi, pi):
        """Discrete Klein-Gordon energy (matches the leapfrog Hamiltonian).

        E = (1/2) sum [ |pi|^2 - phi . Lap(phi) + m^2 |phi|^2 ] * dx
        """
        dx = self.dx
        m2 = self.m_squared
        lap = _compute_laplacian(phi, dx)
        kinetic = np.sum(pi ** 2) * dx
        gradient = -np.sum(phi * lap) * dx
        mass = m2 * np.sum(phi ** 2) * dx
        return 0.5 * (kinetic + gradient + mass)

    # ==================================================================
    # 2.  7D Maxwell evolution
    # ==================================================================

    def evolve_maxwell_7d(self, E0, B0, steps=200, epsilon=1.0):
        """Evolve 7D Maxwell equations with non-associative corrections.

        The first-order system is:

            dE/dt =  curl_7(B) - epsilon * alpha * J_assoc
            dB/dt = -curl_7(E)

        where curl_7 uses the Fano structure constants and J_assoc
        is the non-associative Ampere correction.

        A symplectic splitting is used: advance B by half a step using
        the curl of E, then advance E by a full step using the curl of B,
        then advance B by another half step.

        Parameters
        ----------
        E0, B0  : ndarray, shape (N, 7) -- initial electric and magnetic fields
        steps   : int
        epsilon : float in [0, 1]

        Returns
        -------
        dict with keys:
            'E_history'       : ndarray, shape (steps+1, N, 7)
            'B_history'       : ndarray, shape (steps+1, N, 7)
            'energy_history'  : ndarray, shape (steps+1,)
            'poynting_history': ndarray, shape (steps+1, N, 7)
            'times'           : ndarray, shape (steps+1,)
            'epsilon'         : float
        """
        eps_tensor = structure_constants()
        T = fano_correction_tensor()
        dt = self.dt
        dx = self.dx
        alpha = 0.01  # associator coupling

        E = np.array(E0, dtype=float)
        B = np.array(B0, dtype=float)

        E_hist = np.empty((steps + 1, self.N, 7))
        B_hist = np.empty((steps + 1, self.N, 7))
        en_hist = np.empty(steps + 1)
        poynt_hist = np.empty((steps + 1, self.N, 7))

        E_hist[0] = E
        B_hist[0] = B
        en_hist[0] = self._maxwell_energy(E, B)
        poynt_hist[0] = self._poynting_field(E, B)

        for n in range(steps):
            # --- half-step B ---
            curl_E = self._curl_7d(E, eps_tensor)
            B = B - 0.5 * dt * curl_E

            # --- full-step E ---
            curl_B = self._curl_7d(B, eps_tensor)
            J_assoc = self._j_assoc(E, B, T, epsilon)
            E = E + dt * (curl_B - epsilon * alpha * J_assoc)

            # --- half-step B ---
            curl_E = self._curl_7d(E, eps_tensor)
            B = B - 0.5 * dt * curl_E

            E_hist[n + 1] = E
            B_hist[n + 1] = B
            en_hist[n + 1] = self._maxwell_energy(E, B)
            poynt_hist[n + 1] = self._poynting_field(E, B)

        times = np.arange(steps + 1) * dt

        return {
            'E_history': E_hist,
            'B_history': B_hist,
            'energy_history': en_hist,
            'poynting_history': poynt_hist,
            'times': times,
            'epsilon': epsilon,
        }

    def _curl_7d(self, F, eps_tensor):
        """Discrete 1D 7D curl.  (curl F)_k = sum_j c_{0jk} dF_j/dx."""
        dF = np.zeros_like(F)
        dF[1:-1] = (F[2:] - F[:-2]) / (2 * self.dx)
        dF[0] = (F[1] - F[0]) / self.dx
        dF[-1] = (F[-1] - F[-2]) / self.dx
        curl = np.zeros_like(F)
        for k in range(7):
            for j in range(7):
                c = eps_tensor[0, j, k]
                if abs(c) > 1e-15:
                    curl[:, k] += c * dF[:, j]
        return curl

    def _j_assoc(self, E, B, T, epsilon):
        """Non-associative Ampere current from the Fano correction tensor.

        J_assoc_k = sum_{j,l} T[0,j,k,l] * E[:,l] * dB[:,j] / dx
        """
        dB = np.zeros_like(B)
        dB[1:-1] = (B[2:] - B[:-2]) / (2 * self.dx)
        dB[0] = (B[1] - B[0]) / self.dx
        dB[-1] = (B[-1] - B[-2]) / self.dx

        J = np.zeros_like(E)
        for k in range(7):
            for j in range(7):
                for l in range(7):
                    c = T[0, j, k, l]
                    if abs(c) > 1e-15:
                        J[:, k] += c * E[:, l] * dB[:, j]
        return epsilon * J

    def _maxwell_energy(self, E, B):
        """EM energy: U = (1/2) int (|E|^2 + |B|^2) dx."""
        return 0.5 * (np.sum(E ** 2) + np.sum(B ** 2)) * self.dx

    def _poynting_field(self, E, B):
        """Compute the 7D Poynting vector at each grid point.

        S(x) = E(x) x_7 B(x), using the octonionic cross product.
        Vectorised over the spatial grid.
        """
        eps_tensor = structure_constants()
        S = np.zeros_like(E)
        for k in range(7):
            for (a, b, c_idx) in FANO_TRIPLES:
                i, j, kk = a - 1, b - 1, c_idx - 1
                if kk == k:
                    S[:, k] += E[:, i] * B[:, j] - E[:, j] * B[:, i]
                if i == k:
                    S[:, k] += E[:, j] * B[:, kk] - E[:, kk] * B[:, j]
                if j == k:
                    S[:, k] += E[:, kk] * B[:, i] - E[:, i] * B[:, kk]
        return S

    # ==================================================================
    # 3.  Coherence evolution
    # ==================================================================

    def compute_coherence_evolution(self, phi0, pi0=None, steps=200, epsilon=1.0):
        """Evolve KG and track the coherence charge Q_C at each step.

        Q_C = sum_{i=0}^{N-3} |[phi(i), phi(i+1), phi(i+2)]|^2

        Under G2-covariant dynamics Q_C is exactly conserved.  Under the
        KG evolution (which is only *approximately* G2-covariant on the
        lattice), Q_C should drift slowly; the drift measures the degree
        of G2-symmetry breaking by the lattice.

        Parameters
        ----------
        phi0    : ndarray, shape (N, 8)
        pi0     : ndarray, shape (N, 8) or None
        steps   : int
        epsilon : float

        Returns
        -------
        dict with keys:
            'Q_C_history'  : ndarray, shape (steps+1,)
            'times'        : ndarray, shape (steps+1,)
            'initial_Q_C'  : float
            'final_Q_C'    : float
            'max_drift'    : float  -- max |Q_C(t) - Q_C(0)|
            'relative_drift': float -- max_drift / Q_C(0) if Q_C(0) > 0
        """
        result = self.evolve_klein_gordon(phi0, pi0, steps, epsilon)
        phi_hist = result['phi_history']
        times = result['times']

        qc = np.empty(steps + 1)
        for n in range(steps + 1):
            qc[n] = self._coherence_charge(phi_hist[n], epsilon)

        q0 = qc[0]
        max_drift = float(np.max(np.abs(qc - q0)))
        rel_drift = max_drift / q0 if q0 > 1e-30 else 0.0

        return {
            'Q_C_history': qc,
            'times': times,
            'initial_Q_C': float(q0),
            'final_Q_C': float(qc[-1]),
            'max_drift': max_drift,
            'relative_drift': rel_drift,
        }

    def _coherence_charge(self, phi, epsilon):
        """Compute Q_C = sum_i |[phi_i, phi_{i+1}, phi_{i+2}]_eps|^2."""
        N = phi.shape[0]
        if N < 3:
            return 0.0

        a = phi[:-2]
        b = phi[1:-1]
        c = phi[2:]

        ab = _deformed_multiply_array(a, b, epsilon)
        bc = _deformed_multiply_array(b, c, epsilon)
        ab_c = _deformed_multiply_array(ab, c, epsilon)
        a_bc = _deformed_multiply_array(a, bc, epsilon)

        assoc = ab_c - a_bc  # (N-2, 8)
        return float(np.sum(assoc ** 2))

    # ==================================================================
    # 4.  Associative-limit comparison
    # ==================================================================

    def compare_associative_limit(self, phi0, pi0=None, steps=200):
        """Run the same initial conditions at epsilon=1 and epsilon=0.

        Returns both trajectories and a per-step L2 difference metric:

            Delta(t) = ||phi_{eps=1}(t) - phi_{eps=0}(t)||_2 / ||phi_{eps=0}(t)||_2

        Parameters
        ----------
        phi0  : ndarray, shape (N, 8)
        pi0   : ndarray, shape (N, 8) or None
        steps : int

        Returns
        -------
        dict with keys:
            'oct_result'  : dict from evolve_klein_gordon(epsilon=1)
            'quat_result' : dict from evolve_klein_gordon(epsilon=0)
            'delta'       : ndarray, shape (steps+1,)  -- relative L2 diff
            'times'       : ndarray, shape (steps+1,)
        """
        oct_res = self.evolve_klein_gordon(phi0, pi0, steps, epsilon=1.0)
        quat_res = self.evolve_klein_gordon(phi0, pi0, steps, epsilon=0.0)

        phi_oct = oct_res['phi_history']
        phi_quat = quat_res['phi_history']

        norms_quat = np.sqrt(
            np.sum(phi_quat ** 2, axis=(1, 2))
        )  # (steps+1,)
        norms_quat = np.maximum(norms_quat, 1e-30)

        diff = np.sqrt(np.sum((phi_oct - phi_quat) ** 2, axis=(1, 2)))
        delta = diff / norms_quat

        return {
            'oct_result': oct_res,
            'quat_result': quat_res,
            'delta': delta,
            'times': oct_res['times'],
        }

    # ==================================================================
    # 5.  Signal-speed (causality) test
    # ==================================================================

    def signal_speed_test(self, steps=300, epsilon=1.0):
        """Measure the wavefront propagation speed.

        Creates a narrow Gaussian pulse at the centre, evolves with
        m^2=0, and tracks how far the leading edge has moved after
        half the simulation time (to avoid boundary reflections).

        Parameters
        ----------
        steps   : int
        epsilon : float

        Returns
        -------
        dict with keys:
            'measured_speed' : float
            'expected_speed' : float  (always 1.0)
            'causal'         : bool   (measured_speed <= 1.0 + tol)
        """
        old_m2 = self.m_squared
        self.m_squared = 0.0  # massless for clean speed measurement

        sigma = 3.0 * self.dx
        center = self.L / 2.0
        phi0 = np.zeros((self.N, 8))
        phi0[:, 0] = np.exp(-((self.x - center) ** 2) / (2 * sigma ** 2))
        pi0 = np.zeros((self.N, 8))

        result = self.evolve_klein_gordon(phi0, pi0, steps, epsilon=epsilon)

        self.m_squared = old_m2  # restore

        # Measure the rightward wavefront at the initial time
        amp_init = np.sqrt(np.sum(phi0 ** 2, axis=1))
        peak = np.max(amp_init)
        threshold = 0.01 * peak
        center_idx = self.N // 2

        init_front = center_idx
        for i in range(self.N - 1, center_idx - 1, -1):
            if amp_init[i] > threshold:
                init_front = i
                break

        # Measure at half the simulation time (avoid boundary reflection)
        mid_step = steps // 2
        phi_mid = result['phi_history'][mid_step]
        amp_mid = np.sqrt(np.sum(phi_mid ** 2, axis=1))

        wavefront_idx = center_idx
        for i in range(self.N - 1, center_idx - 1, -1):
            if amp_mid[i] > threshold:
                wavefront_idx = i
                break

        distance = (wavefront_idx - init_front) * self.dx
        elapsed = mid_step * self.dt

        if elapsed > 0 and distance > 0:
            speed = distance / elapsed
        else:
            speed = 0.0

        tolerance = 0.3  # 30% for discretisation / dispersion
        return {
            'measured_speed': float(speed),
            'expected_speed': 1.0,
            'causal': speed <= 1.0 + tolerance,
        }


# ===================================================================
# Module-level convenience wrappers
# ===================================================================

def evolve_klein_gordon(phi0, pi0, dx, dt, steps, m_squared=1.0, epsilon=1.0):
    """Module-level wrapper matching the signature expected in the spec.

    Parameters
    ----------
    phi0, pi0 : ndarray, shape (N, 8)
    dx, dt    : float
    steps     : int
    m_squared : float
    epsilon   : float

    Returns
    -------
    dict  (same keys as OctonionicFieldSimulator.evolve_klein_gordon)
    """
    N = phi0.shape[0]
    L = N * dx
    sim = OctonionicFieldSimulator(N=N, dt=dt, L=L, m_squared=m_squared)
    return sim.evolve_klein_gordon(phi0, pi0, steps, epsilon=epsilon)


def evolve_maxwell_7d(E0, B0, dx, dt, steps, epsilon=1.0):
    """Module-level wrapper for 7D Maxwell evolution.

    Parameters
    ----------
    E0, B0 : ndarray, shape (N, 7)
    dx, dt : float
    steps  : int
    epsilon: float

    Returns
    -------
    dict  (same keys as OctonionicFieldSimulator.evolve_maxwell_7d)
    """
    N = E0.shape[0]
    L = N * dx
    sim = OctonionicFieldSimulator(N=N, dt=dt, L=L)
    return sim.evolve_maxwell_7d(E0, B0, steps, epsilon=epsilon)


def compute_coherence_evolution(phi0, pi0, dx, dt, steps, epsilon=1.0):
    """Module-level wrapper for coherence tracking."""
    N = phi0.shape[0]
    L = N * dx
    sim = OctonionicFieldSimulator(N=N, dt=dt, L=L)
    return sim.compute_coherence_evolution(phi0, pi0, steps, epsilon=epsilon)


def compare_associative_limit(phi0, pi0, dx, dt, steps):
    """Module-level wrapper for the eps=0 vs eps=1 comparison."""
    N = phi0.shape[0]
    L = N * dx
    sim = OctonionicFieldSimulator(N=N, dt=dt, L=L)
    return sim.compare_associative_limit(phi0, pi0, steps)


# ===================================================================
# Main demo
# ===================================================================

def _demo():
    """Run a comprehensive demonstration of the simulation engine."""
    print("=" * 72)
    print("  Octonionic Field Simulator -- Demonstration Run")
    print("=" * 72)
    print()

    N = 64
    dt = 0.01
    L = 10.0
    sim = OctonionicFieldSimulator(N=N, dt=dt, L=L, m_squared=1.0)

    # ----- 1. Klein-Gordon energy conservation -----
    print("[1] Klein-Gordon energy conservation (epsilon=1, 200 steps)")
    phi0 = sim.gaussian_pulse(components=[0, 1, 4, 6])
    result_kg = sim.evolve_klein_gordon(phi0, steps=200, epsilon=1.0)
    E = result_kg['energy_history']
    E0 = E[0]
    rel_err = np.max(np.abs(E - E0)) / E0
    print(f"    Initial energy:  {E0:.8f}")
    print(f"    Final energy:    {E[-1]:.8f}")
    print(f"    Max |dE|/E0:     {rel_err:.2e}")
    print(f"    PASS: {rel_err < 1e-4}")
    print()

    # ----- 2. Quaternionic (eps=0) vs Octonionic (eps=1) -----
    print("[2] Associative limit comparison (epsilon=0 vs epsilon=1)")
    cmp = sim.compare_associative_limit(phi0, steps=200)
    delta = cmp['delta']
    print(f"    Max relative difference: {np.max(delta):.6e}")
    print(f"    Final relative diff:     {delta[-1]:.6e}")
    print(f"    Fields diverge:          {np.max(delta) > 1e-12}")
    print()

    # ----- 3. 7D Maxwell -----
    print("[3] 7D Maxwell evolution (100 steps)")
    E0_em = np.zeros((N, 7))
    B0_em = np.zeros((N, 7))
    # Localised E-field pulse in the e3 direction
    E0_em[:, 2] = np.exp(-((sim.x - L / 2) ** 2) / (2 * (L / 10) ** 2))
    # B-field in the e5 direction (orthogonal Fano partner)
    B0_em[:, 4] = 0.5 * np.exp(-((sim.x - L / 2) ** 2) / (2 * (L / 10) ** 2))
    result_mx = sim.evolve_maxwell_7d(E0_em, B0_em, steps=100, epsilon=1.0)
    U = result_mx['energy_history']
    U_err = np.max(np.abs(U - U[0])) / U[0]
    print(f"    Initial EM energy: {U[0]:.8f}")
    print(f"    Final EM energy:   {U[-1]:.8f}")
    print(f"    Max |dU|/U0:       {U_err:.2e}")
    print()

    # ----- 4. Coherence charge tracking -----
    print("[4] Coherence charge evolution (epsilon=1, 100 steps)")
    phi0_coh = sim.random_field(amplitude=0.3, seed=7)
    coh = sim.compute_coherence_evolution(phi0_coh, steps=100, epsilon=1.0)
    print(f"    Initial Q_C:       {coh['initial_Q_C']:.8f}")
    print(f"    Final Q_C:         {coh['final_Q_C']:.8f}")
    print(f"    Max drift:         {coh['max_drift']:.2e}")
    print(f"    Relative drift:    {coh['relative_drift']:.2e}")
    print()

    # ----- 5. Causality check -----
    print("[5] Signal speed / causality test")
    speed = sim.signal_speed_test(steps=300, epsilon=1.0)
    print(f"    Measured speed:  {speed['measured_speed']:.4f}")
    print(f"    Expected speed:  {speed['expected_speed']:.4f}")
    print(f"    Causal:          {speed['causal']}")
    print()

    # ----- Summary -----
    print("=" * 72)
    print("  Summary")
    print("=" * 72)
    print(f"  Energy conservation (KG):  {'PASS' if rel_err < 1e-4 else 'FAIL'}")
    print(f"  Non-trivial dynamics:      {'PASS' if np.max(delta) > 1e-12 else 'FAIL'}")
    print(f"  Maxwell energy:            {'PASS' if U_err < 0.1 else 'FAIL'}")
    print(f"  Causality:                 {'PASS' if speed['causal'] else 'FAIL'}")
    print()
    print("All arrays are numpy ndarrays ready for matplotlib / analysis.")
    print(f"  phi_history shape: {result_kg['phi_history'].shape}")
    print(f"  E_history shape:   {result_mx['E_history'].shape}")
    print(f"  Q_C_history shape: {coh['Q_C_history'].shape}")


if __name__ == '__main__':
    _demo()
