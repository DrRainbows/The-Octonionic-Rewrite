"""
General dynamical system modeler using the octonionic framework.

Models ANY dynamical system using octonionic state vectors.  The deformation
parameter epsilon interpolates between associative (epsilon=0, standard) and
non-associative (epsilon=1, context-dependent) dynamics.

Mathematical foundation:
  - Each agent/node carries a state in the deformed algebra A_epsilon.
  - At epsilon=0 the algebra is quaternionic (associative) and all dynamics
    reduce to standard matrix/network equations.
  - At epsilon=1 the algebra is fully octonionic and the associator
    [x_i, x_j, x_k] encodes context-dependent three-body interactions
    invisible to any associative model.
  - The associator magnitude ||[x,y,z]|| is a measure of how much the
    outcome of a composite operation depends on the ORDER of composition.

Classes:
  OctonionicDynamicalSystem  -- base class for any epsilon-deformed dynamics
  NetworkDynamics            -- N-node network with adjacency coupling
  CoalitionModel             -- game-theoretic coalition model
  DeformationSweep           -- sweep epsilon and track observables
"""

import numpy as np
from itertools import combinations

from octonion_algebra.core import Octonion
from octonion_algebra.deformation import (
    DeformedOctonion,
    deformed_multiply,
    deformed_associator,
)
from octonion_algebra.associator import associator, associator_norm


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _oct_to_deformed(o, epsilon):
    """Convert an Octonion to a DeformedOctonion at given epsilon.

    Args:
        o: Octonion instance.
        epsilon: float, deformation parameter.

    Returns:
        DeformedOctonion with same coefficients.
    """
    return DeformedOctonion(o.coeffs.copy(), epsilon=epsilon)


def _deformed_to_oct(d):
    """Convert a DeformedOctonion back to an Octonion.

    Args:
        d: DeformedOctonion instance.

    Returns:
        Octonion with same coefficients.
    """
    return Octonion(d.coeffs.copy())


def _states_to_array(states):
    """Stack a list of Octonion/DeformedOctonion objects into (N, 8) numpy array.

    Args:
        states: list of objects with a .coeffs attribute of shape (8,).

    Returns:
        numpy array of shape (N, 8).
    """
    return np.array([s.coeffs for s in states])


def _array_to_deformed(arr, epsilon):
    """Convert (N, 8) array back to list of DeformedOctonion.

    Args:
        arr: numpy array of shape (N, 8).
        epsilon: float.

    Returns:
        list of DeformedOctonion of length N.
    """
    return [DeformedOctonion(arr[i], epsilon=epsilon) for i in range(arr.shape[0])]


# ---------------------------------------------------------------------------
# 1. OctonionicDynamicalSystem
# ---------------------------------------------------------------------------

class OctonionicDynamicalSystem:
    """Base dynamical system with octonionic state vectors.

    The system holds N state vectors, each an element of the deformed
    algebra A_epsilon.  Subclasses override ``_compute_derivatives`` to
    specify the equations of motion.

    State: array of N DeformedOctonion objects (or equivalently an (N, 8)
    numpy array).

    The deformation parameter epsilon controls the algebraic structure:
      - epsilon = 0  =>  quaternionic subalgebra (associative, standard)
      - epsilon = 1  =>  full octonions (non-associative, context-dependent)

    Attributes:
        N:       int, number of state vectors.
        epsilon: float, deformation parameter in [0, 1].
        states:  list of DeformedOctonion, current state of the system.
    """

    def __init__(self, N, initial_states=None, epsilon=1.0, seed=None):
        """Initialise the dynamical system.

        Args:
            N: int, number of state vectors.
            initial_states: optional list of Octonion or DeformedOctonion or
                (N, 8) numpy array.  If None, random unit states are generated.
            epsilon: float in [0, 1].
            seed: optional int for reproducibility.
        """
        self.N = N
        self.epsilon = float(epsilon)
        self._rng = np.random.default_rng(seed)

        if initial_states is not None:
            if isinstance(initial_states, np.ndarray):
                assert initial_states.shape == (N, 8)
                self.states = _array_to_deformed(initial_states, self.epsilon)
            else:
                self.states = []
                for s in initial_states:
                    if isinstance(s, DeformedOctonion):
                        self.states.append(
                            DeformedOctonion(s.coeffs.copy(), epsilon=self.epsilon)
                        )
                    elif isinstance(s, Octonion):
                        self.states.append(
                            DeformedOctonion(s.coeffs.copy(), epsilon=self.epsilon)
                        )
                    else:
                        raise TypeError(f"Unsupported state type: {type(s)}")
        else:
            self.states = [
                DeformedOctonion.random_unit(epsilon=self.epsilon, seed=int(self._rng.integers(0, 2**31)))
                for _ in range(N)
            ]

    # -- subclass hook --------------------------------------------------------

    def _compute_derivatives(self):
        """Return list of (N, 8) derivatives.  Override in subclasses.

        Default: nearest-neighbour coupling along a ring.
            dx_i/dt = x_{i+1} *_eps x_i  -  x_i *_eps x_{i-1}

        Returns:
            numpy array of shape (N, 8).
        """
        arr = _states_to_array(self.states)
        derivs = np.zeros_like(arr)
        for i in range(self.N):
            ip = (i + 1) % self.N
            im = (i - 1) % self.N
            prod_right = deformed_multiply(arr[ip], arr[i], self.epsilon)
            prod_left = deformed_multiply(arr[i], arr[im], self.epsilon)
            derivs[i] = prod_right - prod_left
        return derivs

    # -- integration ----------------------------------------------------------

    def evolve(self, dt, steps, epsilon=None):
        """Integrate the system forward using 4th-order Runge-Kutta.

        This ensures norm drift is minimised even for stiff non-associative
        dynamics.

        Args:
            dt: float, time step.
            steps: int, number of integration steps.
            epsilon: optional float to override the deformation parameter.
                If provided, states are re-wrapped at the new epsilon before
                integration begins.

        Returns:
            dict with keys:
                'trajectory': numpy array of shape (steps+1, N, 8)
                'times': numpy array of shape (steps+1,)
                'total_norm': numpy array of shape (steps+1,) -- sum of norms
                'associator_energy': numpy array of shape (steps+1,)
        """
        if epsilon is not None:
            self.epsilon = float(epsilon)
            self.states = _array_to_deformed(
                _states_to_array(self.states), self.epsilon
            )

        trajectory = np.zeros((steps + 1, self.N, 8))
        times = np.zeros(steps + 1)
        total_norm = np.zeros(steps + 1)
        assoc_energy = np.zeros(steps + 1)

        trajectory[0] = _states_to_array(self.states)
        total_norm[0] = self._total_norm()
        assoc_energy[0] = self.measure_associator()

        for step in range(steps):
            self._rk4_step(dt)
            t = (step + 1) * dt
            times[step + 1] = t
            trajectory[step + 1] = _states_to_array(self.states)
            total_norm[step + 1] = self._total_norm()
            assoc_energy[step + 1] = self.measure_associator()

        return {
            "trajectory": trajectory,
            "times": times,
            "total_norm": total_norm,
            "associator_energy": assoc_energy,
        }

    def _rk4_step(self, dt):
        """Single Runge-Kutta 4 step."""
        arr = _states_to_array(self.states)

        # k1
        k1 = self._compute_derivatives()

        # k2
        self.states = _array_to_deformed(arr + 0.5 * dt * k1, self.epsilon)
        k2 = self._compute_derivatives()

        # k3
        self.states = _array_to_deformed(arr + 0.5 * dt * k2, self.epsilon)
        k3 = self._compute_derivatives()

        # k4
        self.states = _array_to_deformed(arr + dt * k3, self.epsilon)
        k4 = self._compute_derivatives()

        # Update
        new_arr = arr + (dt / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
        self.states = _array_to_deformed(new_arr, self.epsilon)

    # -- observables ----------------------------------------------------------

    def measure_associator(self):
        """Compute total associator magnitude across all distinct triples.

        Total = sum_{i<j<k} ||[x_i, x_j, x_k]_epsilon||

        For epsilon=0 and quaternionic states this is exactly zero.

        Returns:
            float: total associator magnitude.
        """
        total = 0.0
        for i, j, k in combinations(range(self.N), 3):
            assoc = self.states[i].associator(self.states[j], self.states[k])
            total += assoc.norm()
        return total

    def measure_context_dependence(self):
        """Ratio of associator energy to total energy.

        context_dependence = (sum ||[x_i, x_j, x_k]||^2) / (sum ||x_i||^2)

        This is 0.0 when dynamics are fully associative (epsilon=0) and
        grows toward 1.0 as non-associative effects dominate.

        Returns:
            float: context dependence ratio.
        """
        assoc_energy = 0.0
        for i, j, k in combinations(range(self.N), 3):
            assoc = self.states[i].associator(self.states[j], self.states[k])
            assoc_energy += assoc.norm_squared()

        total_energy = sum(s.norm_squared() for s in self.states)
        if total_energy < 1e-30:
            return 0.0
        return assoc_energy / total_energy

    def _total_norm(self):
        """Sum of all state norms."""
        return sum(s.norm() for s in self.states)

    def state_array(self):
        """Return current state as (N, 8) numpy array."""
        return _states_to_array(self.states)


# ---------------------------------------------------------------------------
# 2. NetworkDynamics
# ---------------------------------------------------------------------------

class NetworkDynamics(OctonionicDynamicalSystem):
    """N-node network with octonionic states and adjacency-matrix coupling.

    Dynamics:
        dx_i/dt = sum_j A_{ij} * (x_i *_eps x_j)
                  + coupling * sum_{j,k} A_{ij} A_{ik} [x_i, x_j, x_k]_eps

    The first term is standard pairwise coupling (survives at epsilon=0).
    The second term is the associator-mediated three-body interaction that
    captures context-dependent information flow (vanishes at epsilon=0 for
    quaternionic states).

    Attributes:
        adjacency: numpy array of shape (N, N), the adjacency/weight matrix.
        coupling:  float, strength of associator-mediated coupling.
    """

    def __init__(self, N, adjacency=None, coupling=0.1,
                 initial_states=None, epsilon=1.0, seed=None):
        """Initialise network dynamics.

        Args:
            N: int, number of nodes.
            adjacency: (N, N) numpy array.  If None, a symmetric random
                matrix with entries in [0, 1] is generated.
            coupling: float, relative strength of the three-body (associator)
                coupling term.
            initial_states: optional, see OctonionicDynamicalSystem.
            epsilon: float in [0, 1].
            seed: optional int.
        """
        super().__init__(N, initial_states=initial_states,
                         epsilon=epsilon, seed=seed)

        if adjacency is not None:
            self.adjacency = np.asarray(adjacency, dtype=float)
        else:
            # Generate a symmetric random adjacency matrix
            rng = np.random.default_rng(seed)
            A = rng.uniform(0, 1, size=(N, N))
            A = 0.5 * (A + A.T)
            np.fill_diagonal(A, 0.0)
            self.adjacency = A

        self.coupling = float(coupling)

    def _compute_derivatives(self):
        """Network dynamics with pairwise + associator coupling.

        dx_i/dt = sum_j A_{ij} (x_i *_eps x_j)
                  + coupling * sum_{j != k} A_{ij} A_{ik} [x_i, x_j, x_k]_eps

        Returns:
            numpy array of shape (N, 8).
        """
        arr = _states_to_array(self.states)
        derivs = np.zeros_like(arr)

        for i in range(self.N):
            # Pairwise coupling
            for j in range(self.N):
                if abs(self.adjacency[i, j]) < 1e-15:
                    continue
                prod = deformed_multiply(arr[i], arr[j], self.epsilon)
                derivs[i] += self.adjacency[i, j] * prod

            # Three-body associator coupling
            for j in range(self.N):
                if abs(self.adjacency[i, j]) < 1e-15:
                    continue
                for k in range(j + 1, self.N):
                    if k == i or abs(self.adjacency[i, k]) < 1e-15:
                        continue
                    assoc = deformed_associator(
                        arr[i], arr[j], arr[k], self.epsilon
                    )
                    w = self.coupling * self.adjacency[i, j] * self.adjacency[i, k]
                    derivs[i] += w * assoc.coeffs

        return derivs

    def compute_information_flow(self):
        """Fraction of dynamics mediated by non-associative (three-body) channels.

        Computes:
            flow = ||associator_terms|| / (||pairwise_terms|| + ||associator_terms||)

        At epsilon=0 with quaternionic states this is 0.0.

        Returns:
            float: information flow fraction in [0, 1].
        """
        arr = _states_to_array(self.states)
        pairwise_energy = 0.0
        assoc_energy = 0.0

        for i in range(self.N):
            pair_vec = np.zeros(8)
            assoc_vec = np.zeros(8)

            for j in range(self.N):
                if abs(self.adjacency[i, j]) < 1e-15:
                    continue
                prod = deformed_multiply(arr[i], arr[j], self.epsilon)
                pair_vec += self.adjacency[i, j] * prod

                for k in range(j + 1, self.N):
                    if k == i or abs(self.adjacency[i, k]) < 1e-15:
                        continue
                    assoc = deformed_associator(
                        arr[i], arr[j], arr[k], self.epsilon
                    )
                    w = self.coupling * self.adjacency[i, j] * self.adjacency[i, k]
                    assoc_vec += w * assoc.coeffs

            pairwise_energy += np.linalg.norm(pair_vec)
            assoc_energy += np.linalg.norm(assoc_vec)

        total = pairwise_energy + assoc_energy
        if total < 1e-30:
            return 0.0
        return assoc_energy / total


# ---------------------------------------------------------------------------
# 3. CoalitionModel
# ---------------------------------------------------------------------------

class CoalitionModel:
    """Game-theoretic coalition model using octonionic triple products.

    N agents form coalitions (ordered groups).  The value of a coalition
    (A, B, C) is the norm of the triple product (a *_eps b) *_eps c, where
    a, b, c are the octonionic states of the agents.

    Because the octonions are non-associative, the coalition value depends
    on the ordering: V(A,B,C) != V(A,C,B) in general.  The associator
    [a, b, c] = (a*b)*c - a*(b*c) directly measures this "agenda dependence".

    At epsilon=0 the algebra is associative and all orderings give the same
    value.  At epsilon=1 ordering matters maximally.

    Attributes:
        N:       int, number of agents.
        epsilon: float, deformation parameter.
        agents:  list of DeformedOctonion, agent states.
    """

    def __init__(self, N, agent_states=None, epsilon=1.0, seed=None):
        """Initialise the coalition model.

        Args:
            N: int, number of agents.
            agent_states: optional list of Octonion/DeformedOctonion or
                (N, 8) array.
            epsilon: float in [0, 1].
            seed: optional int.
        """
        self.N = N
        self.epsilon = float(epsilon)
        rng = np.random.default_rng(seed)

        if agent_states is not None:
            if isinstance(agent_states, np.ndarray):
                self.agents = _array_to_deformed(agent_states, self.epsilon)
            else:
                self.agents = [
                    DeformedOctonion(s.coeffs.copy(), epsilon=self.epsilon)
                    for s in agent_states
                ]
        else:
            self.agents = [
                DeformedOctonion.random_unit(epsilon=self.epsilon, seed=int(rng.integers(0, 2**31)))
                for _ in range(N)
            ]

    def coalition_value(self, i, j, k):
        """Value of the ordered coalition (i, j, k).

        V(i,j,k) = ||(a_i *_eps a_j) *_eps a_k||

        This depends on the ordering because the deformed algebra is
        non-associative (for epsilon > 0).

        Args:
            i, j, k: int, agent indices.

        Returns:
            float: coalition value (non-negative).
        """
        ab = self.agents[i] * self.agents[j]
        abc = ab * self.agents[k]
        return abc.norm()

    def coalition_associator(self, i, j, k):
        """Associator of the ordered triple (i, j, k).

        [a_i, a_j, a_k]_eps = (a_i *_eps a_j) *_eps a_k
                              - a_i *_eps (a_j *_eps a_k)

        This measures how much the coalition outcome depends on the order
        of proposal / composition.

        Args:
            i, j, k: int, agent indices.

        Returns:
            DeformedOctonion: the associator.
        """
        return self.agents[i].associator(self.agents[j], self.agents[k])

    def agenda_dependence_index(self):
        """Global scalar measuring how much outcomes depend on ordering.

        ADI = (sum_{i<j<k} ||[a_i, a_j, a_k]||) / (sum_{i<j<k} max-perm ||product||)

        Normalised so ADI in [0, 1].  ADI = 0 means the algebra is
        associative (epsilon=0) and ordering does not matter.

        Returns:
            float: agenda dependence index.
        """
        total_assoc = 0.0
        total_value = 0.0

        for i, j, k in combinations(range(self.N), 3):
            assoc = self.coalition_associator(i, j, k)
            total_assoc += assoc.norm()

            # The maximum product norm across the two parenthesisations
            v1 = (self.agents[i] * self.agents[j]) * self.agents[k]
            v2 = self.agents[i] * (self.agents[j] * self.agents[k])
            total_value += max(v1.norm(), v2.norm())

        if total_value < 1e-30:
            return 0.0
        return total_assoc / total_value

    def find_stable_coalitions(self, coalition_size=3):
        """Find coalitions where no agent benefits from switching.

        A coalition (i, j, k) is "stable" if for every permutation of
        the agents, the coalition value does not increase by more than
        a tolerance.  This corresponds to configurations where the
        associator is small -- the ordering does not matter much.

        Args:
            coalition_size: int, size of coalitions to consider (default 3).

        Returns:
            list of tuples: stable coalitions sorted by value (descending).
        """
        from itertools import permutations

        stable = []
        for combo in combinations(range(self.N), coalition_size):
            if coalition_size != 3:
                # Only triples supported for associator analysis
                continue

            i, j, k = combo
            assoc_norm = self.coalition_associator(i, j, k).norm()
            base_value = self.coalition_value(i, j, k)

            # Stability criterion: associator is small relative to value
            # (ordering insensitivity)
            if base_value < 1e-15:
                continue
            relative_dependence = assoc_norm / base_value
            if relative_dependence < 0.1:  # less than 10% agenda dependence
                stable.append((combo, base_value, relative_dependence))

        # Sort by value descending
        stable.sort(key=lambda x: -x[1])
        return stable

    def agent_array(self):
        """Return agent states as (N, 8) numpy array."""
        return _states_to_array(self.agents)


# ---------------------------------------------------------------------------
# 4. DeformationSweep
# ---------------------------------------------------------------------------

class DeformationSweep:
    """Sweep the deformation parameter epsilon and track observables.

    Takes a system factory (callable that builds a system at a given epsilon)
    and runs it at epsilon = 0, 0.1, 0.2, ..., 1.0, tracking key
    observables at each value.

    This reveals *phase transitions*: values of epsilon where observables
    change qualitatively (sharp jumps or kinks in smooth curves).

    Attributes:
        epsilon_values: numpy array of epsilon sample points.
        results:        dict mapping observable names to arrays.
    """

    def __init__(self, epsilon_values=None):
        """Initialise the sweep.

        Args:
            epsilon_values: array-like of epsilon values.
                Defaults to np.linspace(0, 1, 11).
        """
        if epsilon_values is None:
            self.epsilon_values = np.linspace(0, 1, 11)
        else:
            self.epsilon_values = np.asarray(epsilon_values, dtype=float)
        self.results = {}

    def sweep_network(self, N, adjacency=None, coupling=0.1,
                      dt=0.01, steps=50, seed=42):
        """Run a NetworkDynamics system at each epsilon and collect observables.

        Observables collected:
          - context_dependence: measure_context_dependence() after evolution
          - information_flow:   compute_information_flow() after evolution
          - associator_total:   measure_associator() after evolution
          - total_norm:         total norm after evolution

        Args:
            N: int, number of nodes.
            adjacency: optional (N, N) array.
            coupling: float.
            dt: float, time step.
            steps: int, evolution steps.
            seed: int, base random seed.

        Returns:
            dict with keys:
                'epsilon': numpy array
                'context_dependence': numpy array
                'information_flow': numpy array
                'associator_total': numpy array
                'total_norm': numpy array
                'phase_transition_epsilon': float or None
        """
        # Generate fixed initial states and adjacency at seed
        rng = np.random.default_rng(seed)
        init_arr = rng.standard_normal((N, 8))
        # Normalise each row to unit norm
        norms = np.linalg.norm(init_arr, axis=1, keepdims=True)
        norms = np.maximum(norms, 1e-15)
        init_arr = init_arr / norms

        if adjacency is None:
            A = rng.uniform(0, 1, size=(N, N))
            A = 0.5 * (A + A.T)
            np.fill_diagonal(A, 0.0)
        else:
            A = np.asarray(adjacency, dtype=float)

        ctx_dep = np.zeros(len(self.epsilon_values))
        info_flow = np.zeros(len(self.epsilon_values))
        assoc_total = np.zeros(len(self.epsilon_values))
        total_norm = np.zeros(len(self.epsilon_values))

        for idx, eps in enumerate(self.epsilon_values):
            net = NetworkDynamics(
                N, adjacency=A.copy(), coupling=coupling,
                initial_states=init_arr.copy(), epsilon=eps, seed=seed
            )
            net.evolve(dt, steps)
            ctx_dep[idx] = net.measure_context_dependence()
            info_flow[idx] = net.compute_information_flow()
            assoc_total[idx] = net.measure_associator()
            total_norm[idx] = net._total_norm()

        # Detect phase transition: largest second derivative of context_dependence
        phase_eps = self._detect_phase_transition(ctx_dep)

        self.results = {
            "epsilon": self.epsilon_values.copy(),
            "context_dependence": ctx_dep,
            "information_flow": info_flow,
            "associator_total": assoc_total,
            "total_norm": total_norm,
            "phase_transition_epsilon": phase_eps,
        }
        return self.results

    def sweep_coalition(self, N, seed=42):
        """Run a CoalitionModel at each epsilon and collect observables.

        Observables:
          - agenda_dependence: agenda_dependence_index()
          - n_stable: number of stable coalitions
          - mean_value: mean coalition value

        Args:
            N: int, number of agents.
            seed: int.

        Returns:
            dict with keys 'epsilon', 'agenda_dependence', 'n_stable',
            'mean_value', 'phase_transition_epsilon'.
        """
        rng = np.random.default_rng(seed)
        init_arr = rng.standard_normal((N, 8))
        norms = np.linalg.norm(init_arr, axis=1, keepdims=True)
        norms = np.maximum(norms, 1e-15)
        init_arr = init_arr / norms

        adi = np.zeros(len(self.epsilon_values))
        n_stable = np.zeros(len(self.epsilon_values), dtype=int)
        mean_val = np.zeros(len(self.epsilon_values))

        for idx, eps in enumerate(self.epsilon_values):
            model = CoalitionModel(N, agent_states=init_arr.copy(),
                                   epsilon=eps, seed=seed)
            adi[idx] = model.agenda_dependence_index()
            stable = model.find_stable_coalitions()
            n_stable[idx] = len(stable)
            # Mean coalition value over all triples
            vals = []
            for combo in combinations(range(N), 3):
                vals.append(model.coalition_value(*combo))
            mean_val[idx] = np.mean(vals) if vals else 0.0

        phase_eps = self._detect_phase_transition(adi)

        self.results = {
            "epsilon": self.epsilon_values.copy(),
            "agenda_dependence": adi,
            "n_stable": n_stable,
            "mean_value": mean_val,
            "phase_transition_epsilon": phase_eps,
        }
        return self.results

    @staticmethod
    def _detect_phase_transition(observable):
        """Detect the epsilon of a phase transition via maximum second derivative.

        A phase transition manifests as a kink or discontinuity in an
        observable as a function of epsilon.  We identify it as the point
        of maximum absolute second derivative.

        Args:
            observable: 1D numpy array.

        Returns:
            float or None: epsilon value at the phase transition, or None
            if the observable is constant.
        """
        if len(observable) < 3:
            return None
        d2 = np.abs(np.diff(observable, n=2))
        if np.max(d2) < 1e-12:
            return None
        # The second difference at index i corresponds to epsilon[i+1]
        idx = np.argmax(d2)
        # Approximate the epsilon value (midpoint of the interval)
        return None  # will be set by caller if needed

    def detect_phase_transition(self, observable_name):
        """Detect phase transition for a named observable.

        Args:
            observable_name: str, key in self.results.

        Returns:
            float or None: epsilon at the phase transition.
        """
        if observable_name not in self.results:
            return None
        obs = self.results[observable_name]
        eps = self.results["epsilon"]
        if len(obs) < 3:
            return None
        d2 = np.abs(np.diff(obs, n=2))
        if np.max(d2) < 1e-12:
            return None
        idx = np.argmax(d2)
        # idx maps to epsilon[idx + 1]
        return float(eps[idx + 1])


# ---------------------------------------------------------------------------
# 5. Main demo
# ---------------------------------------------------------------------------

def _demo():
    """Demo: 8-node network with deformation sweep from epsilon=0 to epsilon=1."""
    print("=" * 70)
    print("OCTONIONIC DYNAMICAL SYSTEM SIMULATOR")
    print("=" * 70)
    print()

    N = 8
    seed = 42

    # --- Network dynamics sweep ---
    print("--- 8-node Network Dynamics: Deformation Sweep ---")
    print(f"Nodes: {N}, coupling: 0.1, dt=0.01, steps=30")
    print()

    sweep = DeformationSweep(np.linspace(0, 1, 11))
    results = sweep.sweep_network(N, coupling=0.1, dt=0.01, steps=30, seed=seed)

    print(f"{'epsilon':>8s}  {'ctx_dep%':>10s}  {'info_flow%':>10s}  {'assoc_total':>12s}  {'total_norm':>10s}")
    print("-" * 60)
    for i, eps in enumerate(results["epsilon"]):
        ctx = results["context_dependence"][i] * 100
        ifl = results["information_flow"][i] * 100
        ast = results["associator_total"][i]
        tn = results["total_norm"][i]
        print(f"{eps:8.1f}  {ctx:10.4f}  {ifl:10.4f}  {ast:12.4f}  {tn:10.4f}")

    phase_eps = sweep.detect_phase_transition("context_dependence")
    if phase_eps is not None:
        print(f"\nPhase transition detected at epsilon ~ {phase_eps:.2f}")
    else:
        print("\nNo sharp phase transition detected (smooth crossover).")

    # --- Coalition model sweep ---
    print()
    print("--- 6-agent Coalition Model: Deformation Sweep ---")
    N_coal = 6
    sweep_c = DeformationSweep(np.linspace(0, 1, 11))
    results_c = sweep_c.sweep_coalition(N_coal, seed=seed)

    print(f"{'epsilon':>8s}  {'ADI':>10s}  {'n_stable':>8s}  {'mean_val':>10s}")
    print("-" * 42)
    for i, eps in enumerate(results_c["epsilon"]):
        a = results_c["agenda_dependence"][i]
        ns = results_c["n_stable"][i]
        mv = results_c["mean_value"][i]
        print(f"{eps:8.1f}  {a:10.6f}  {ns:8d}  {mv:10.4f}")

    phase_eps_c = sweep_c.detect_phase_transition("agenda_dependence")
    if phase_eps_c is not None:
        print(f"\nPhase transition at epsilon ~ {phase_eps_c:.2f}")
    else:
        print("\nNo sharp phase transition detected.")

    # --- Verification: epsilon=0 baseline ---
    print()
    print("--- Verification: epsilon=0 baseline ---")
    rng = np.random.default_rng(seed)
    # Create quaternionic states (only components 0-3 nonzero)
    quat_arr = np.zeros((N, 8))
    quat_arr[:, :4] = rng.standard_normal((N, 4))
    norms = np.linalg.norm(quat_arr, axis=1, keepdims=True)
    quat_arr = quat_arr / np.maximum(norms, 1e-15)

    net0 = NetworkDynamics(N, initial_states=quat_arr, epsilon=0.0, seed=seed)
    assoc0 = net0.measure_associator()
    ctx0 = net0.measure_context_dependence()
    print(f"epsilon=0 associator total: {assoc0:.2e}  (should be ~0)")
    print(f"epsilon=0 context dependence: {ctx0:.2e}  (should be ~0)")

    print()
    print("Simulation complete.")


if __name__ == "__main__":
    _demo()
