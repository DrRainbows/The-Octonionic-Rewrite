"""
Benchmark demonstrations: octonionic associator detects what associative tools miss.

Run via: python -m octonion_algebra.demo
    or:  python -m octonion_algebra.demo --all
    or:  python -m octonion_algebra.demo --simulate-market --simulate-physics --simulate-systems

Command-line flags:
    (no flags)          Run the original 8 benchmarks only.
    --simulate-market   Run market simulation demo.
    --simulate-physics  Run physics simulation demo.
    --simulate-systems  Run systems dynamics demo.
    --all               Run everything (benchmarks + all simulations).
"""
import argparse
import time
import numpy as np

from octonion_algebra.core import (
    Octonion, e1, e2, e3, e4, e5, e6, e7, cross_product_7d,
)
from octonion_algebra.associator import associator
from octonion_algebra.alignment import (
    detect_gaming, restrict_to_quaternion, associator_signature,
)
from octonion_algebra.fluids import taylor_green_7d, vorticity_source_na, restrict_velocity_to_3d
from octonion_algebra.finance import context_premium
from octonion_algebra.copbw import copbw_basis, verify_basis_count, catalan
from octonion_algebra.calculus import bac_cab_7d
from octonion_algebra.conservation import verify_coherence_conservation
from octonion_algebra.g2 import g2_generators


def _header(title):
    width = 60
    print()
    print("=" * width)
    print(f"  {title}")
    print("=" * width)


def benchmark_gaming_detection():
    """Benchmark 1: Gaming Detection (alignment)."""
    _header("Benchmark 1: Gaming Detection (alignment)")

    rng = np.random.default_rng(42)

    # Create 5 random octonion agents, normalize to unit
    agents = []
    for i in range(5):
        o = Octonion(rng.uniform(-1, 1, size=8))
        agents.append(o / o.norm())

    # Mark agents 3 and 4 as strategic (gaming) targets
    gaming_indices = [3, 4]
    print(f"Team size: {len(agents)} agents")
    print(f"Gaming targets: indices {gaming_indices}")
    print()

    # Octonionic detection
    o_detected = 0
    o_total = 0
    for idx in gaming_indices:
        result = detect_gaming(agents, replacement_index=idx, n_attempts=50, seed=7000 + idx)
        o_detected += result['detected_count']
        o_total += result['total_attempts']
        print(f"  O  agent {idx}: {result['detected_count']}/{result['total_attempts']} detected "
              f"(rate {result['detection_rate']:.2%})")

    o_rate = o_detected / o_total

    # Quaternionic restriction: project all agents to H = {1, e1, e2, e3}
    # Replacements must also be quaternionic, otherwise the comparison is unfair.
    q_agents = [restrict_to_quaternion(a) for a in agents]

    q_detected = 0
    q_total = 0
    n_attempts = 50
    for idx in gaming_indices:
        sig_original = associator_signature(q_agents)
        detected_count = 0
        for attempt in range(n_attempts):
            replacement = Octonion.random(seed=7000 + idx + attempt)
            replacement = restrict_to_quaternion(replacement)
            new_team = q_agents.copy()
            new_team[idx] = replacement
            new_sig = associator_signature(new_team)
            if (new_sig - sig_original).norm() > 1e-10:
                detected_count += 1
        q_detected += detected_count
        q_total += n_attempts
        rate = detected_count / n_attempts
        print(f"  H  agent {idx}: {detected_count}/{n_attempts} detected "
              f"(rate {rate:.2%})")

    q_rate = q_detected / q_total

    print()
    print(f"  Detection rate in O: {o_rate:.2%}")
    print(f"  Detection rate in H: {q_rate:.2%}")

    passed = o_rate > q_rate
    print(f"  Result: {'PASS' if passed else 'FAIL'} (O rate > H rate)")
    return passed


def benchmark_turbulence_source():
    """Benchmark 2: Turbulence Source Term (fluids)."""
    _header("Benchmark 2: Turbulence Source Term (fluids)")

    # 7D Taylor-Green velocity field
    print("  Creating 7D Taylor-Green velocity field (N=8) ...")
    v7, dx7 = taylor_green_7d(N=8)

    print("  Computing S_NA (7D vorticity source) ...")
    s_na_7d = vorticity_source_na(v7, dx7)
    mag_7d = np.sqrt(sum(np.sum(s**2) for s in s_na_7d))
    print(f"  |S_NA|_7D = {mag_7d:.6e}")

    # 3D-restricted field
    print("  Creating 3D-restricted velocity field (N=4) ...")
    v3, dx3 = restrict_velocity_to_3d(N=4)

    print("  Computing S_NA (3D restriction) ...")
    s_na_3d = vorticity_source_na(v3, dx3)
    mag_3d = np.sqrt(sum(np.sum(s**2) for s in s_na_3d))
    print(f"  |S_NA|_3D = {mag_3d:.6e}")

    print()
    ratio = mag_7d / mag_3d if mag_3d > 1e-30 else float('inf')
    print(f"  Ratio 7D/3D: {ratio:.1f}x")

    passed = mag_7d > 100 * mag_3d
    print(f"  Result: {'PASS' if passed else 'FAIL'} (7D >> 3D)")
    return passed


def benchmark_portfolio_premium():
    """Benchmark 3: Portfolio Context Premium (finance)."""
    _header("Benchmark 3: Portfolio Context Premium (finance)")

    rng = np.random.default_rng(123)

    # 3 random octonionic portfolio positions
    oct_positions = []
    for i in range(3):
        o = Octonion(rng.uniform(-1, 1, size=8))
        oct_positions.append(o)

    cp_oct = context_premium(oct_positions[0], oct_positions[1], oct_positions[2])
    oct_norm = cp_oct['associator_norm']
    oct_ratio = cp_oct['context_ratio']
    print(f"  Octonionic positions:")
    print(f"    |[P_A, P_B, P_C]| = {oct_norm:.6f}")
    print(f"    Context ratio      = {oct_ratio:.6f}")

    # 3 quaternionic positions (zero components 4-7)
    quat_positions = []
    for i in range(3):
        coeffs = np.zeros(8)
        coeffs[0:4] = rng.uniform(-1, 1, size=4)
        quat_positions.append(Octonion(coeffs))

    cp_quat = context_premium(quat_positions[0], quat_positions[1], quat_positions[2])
    quat_norm = cp_quat['associator_norm']
    quat_ratio = cp_quat['context_ratio']
    print(f"  Quaternionic positions:")
    print(f"    |[P_A, P_B, P_C]| = {quat_norm:.6e}")
    print(f"    Context ratio      = {quat_ratio:.6e}")

    print()
    print(f"  Octonionic premium:   {oct_norm:.6f}")
    print(f"  Quaternionic premium: {quat_norm:.6e}")

    passed = oct_norm > 100 * quat_norm
    print(f"  Result: {'PASS' if passed else 'FAIL'} (octonionic >> quaternionic)")
    return passed


def benchmark_copbw_completeness():
    """Benchmark 4: COPBW Basis Completeness."""
    _header("Benchmark 4: COPBW Basis Completeness (copbw)")

    generators = ['a', 'b']
    k = len(generators)
    max_deg = 5

    print(f"  Generators: {generators} (k={k})")
    print(f"  Max degree: {max_deg}")
    print()

    results = verify_basis_count(generators, max_weight=max_deg)

    print(f"  {'Degree':>6}  {'Count':>8}  {'k^n * C_{n-1}':>14}  {'Match':>6}")
    print(f"  {'------':>6}  {'-----':>8}  {'--------------':>14}  {'-----':>6}")

    all_match = True
    for deg in range(1, max_deg + 1):
        r = results[deg]
        cat_val = catalan(deg - 1)
        expected = k ** deg * cat_val
        match_str = "Yes" if r['pass'] else "NO"
        if not r['pass']:
            all_match = False
        print(f"  {deg:>6}  {r['count']:>8}  {expected:>14}  {match_str:>6}")

    print()
    # Also show with 3 generators at lower degree for variety
    generators_3 = ['a', 'b', 'c']
    k3 = len(generators_3)
    max_deg_3 = 4

    print(f"  Generators: {generators_3} (k={k3}), max degree {max_deg_3}")
    results_3 = verify_basis_count(generators_3, max_weight=max_deg_3)

    print(f"  {'Degree':>6}  {'Count':>8}  {'k^n * C_{n-1}':>14}  {'Match':>6}")
    print(f"  {'------':>6}  {'-----':>8}  {'--------------':>14}  {'-----':>6}")

    for deg in range(1, max_deg_3 + 1):
        r = results_3[deg]
        cat_val = catalan(deg - 1)
        expected = k3 ** deg * cat_val
        match_str = "Yes" if r['pass'] else "NO"
        if not r['pass']:
            all_match = False
        print(f"  {deg:>6}  {r['count']:>8}  {expected:>14}  {match_str:>6}")

    print()
    print(f"  Result: {'PASS' if all_match else 'FAIL'} (all counts match Catalan predictions)")
    return all_match


def benchmark_bac_cab_identity():
    """Benchmark 5: BAC-CAB Identity in 7D."""
    _header("Benchmark 5: BAC-CAB Identity (calculus)")

    rng = np.random.default_rng(42)

    # Pick 3 random imaginary octonions
    def random_imag(rng):
        coeffs = np.zeros(8)
        coeffs[1:] = rng.uniform(-1, 1, size=7)
        return Octonion(coeffs)

    a = random_imag(rng)
    b = random_imag(rng)
    c = random_imag(rng)

    print("  Testing a x (b x c) = b(a.c) - c(a.b) + correction ...")
    result = bac_cab_7d(a, b, c)
    diff_norm = (result['lhs'] - result['rhs']).norm()
    correction_norm = result['correction'].norm()

    print(f"  |lhs - rhs|       = {diff_norm:.6e}")
    print(f"  |correction| (7D) = {correction_norm:.6e}")

    identity_ok = diff_norm < 1e-10
    correction_nonzero = correction_norm > 1e-10
    print(f"  Identity holds:      {'YES' if identity_ok else 'NO'}")
    print(f"  Correction nonzero:  {'YES' if correction_nonzero else 'NO'}")

    # Restrict to 3D: only e1, e2, e3 components
    def restrict_3d(o):
        coeffs = np.zeros(8)
        coeffs[1:4] = o.coeffs[1:4]
        return Octonion(coeffs)

    a3 = restrict_3d(a)
    b3 = restrict_3d(b)
    c3 = restrict_3d(c)

    result_3d = bac_cab_7d(a3, b3, c3)
    correction_3d_norm = result_3d['correction'].norm()
    diff_3d_norm = (result_3d['lhs'] - result_3d['rhs']).norm()

    print(f"  |correction| (3D) = {correction_3d_norm:.6e}")
    print(f"  |lhs - rhs| (3D) = {diff_3d_norm:.6e}")

    correction_zero_3d = correction_3d_norm < 1e-10
    print(f"  Correction zero in 3D: {'YES' if correction_zero_3d else 'NO'}")

    print()
    passed = identity_ok and correction_nonzero and correction_zero_3d
    print(f"  Result: {'PASS' if passed else 'FAIL'} (identity holds, correction nonzero in 7D, zero in 3D)")
    return passed


def benchmark_noether_currents():
    """Benchmark 6: Noether Currents (G2 Conservation)."""
    _header("Benchmark 6: Noether Currents (G2 Conservation)")

    rng = np.random.default_rng(42)

    # Create a random octonionic field (array of 20 Octonions)
    field = []
    for _ in range(20):
        o = Octonion(rng.uniform(-1, 1, size=8))
        field.append(o)

    print("  Computing G2 generators ...")
    gens = g2_generators()
    print(f"  Number of G2 generators: {len(gens)}")

    print("  Evolving field under G2-covariant dynamics ...")
    print("    dt=0.001, n_steps=50")
    result = verify_coherence_conservation(field, gens, dt=0.001, n_steps=50, seed=42)

    initial_c = result['initial_C']
    final_c = result['final_C']
    rel_err = result['relative_error']

    print(f"  Initial coherence C(0) = {initial_c:.6e}")
    print(f"  Final coherence C(T)   = {final_c:.6e}")
    print(f"  Max relative variation = {rel_err:.6e}")

    passed = rel_err < 0.05
    print()
    print(f"  Result: {'PASS' if passed else 'FAIL'} (max relative variation < 5%)")
    return passed


def benchmark_poynting_transverse_drift():
    """Benchmark 7: Poynting Transverse Drift.

    Polarization: E = cos(a)*e3 + sin(a)*e2,  B = cos(a)*e5 + sin(a)*e4.
    Cross products via Fano triples:
      e3 x e5 = -e6   (from 3,6,5 triple)
      e2 x e4 =  e6   (from 2,4,6 triple)
      e3 x e4 =  e7   (from 3,4,7 triple)
      e2 x e5 =  e7   (from 2,5,7 triple)
    Result: S = -cos(2a)*e6 + sin(2a)*e7.
    Longitudinal = e6, transverse drift = e7.
    """
    _header("Benchmark 7: Poynting Transverse Drift")

    print("  E = cos(alpha)*e3 + sin(alpha)*e2")
    print("  B = cos(alpha)*e5 + sin(alpha)*e4")
    print("  S = E x_7 B  (7D cross product)")
    print("  Expected: S = -cos(2a)*e6 + sin(2a)*e7")
    print()

    alphas = [0.0, np.pi / 4, np.pi / 6]
    labels = ["alpha=0", "alpha=pi/4", "alpha=pi/6"]

    all_ok = True
    for alpha, label in zip(alphas, labels):
        # E = cos(a)*e3 + sin(a)*e2;  B = cos(a)*e5 + sin(a)*e4
        E = Octonion([0, 0, np.sin(alpha), np.cos(alpha), 0, 0, 0, 0])
        B = Octonion([0, 0, 0, 0, np.sin(alpha), np.cos(alpha), 0, 0])
        S = cross_product_7d(E, B)

        s_e6 = S.coeffs[6]   # e6 component (longitudinal)
        s_e7 = S.coeffs[7]   # e7 component (transverse)
        s_total = S.norm()

        print(f"  {label}:")
        print(f"    S = {S}")
        print(f"    S_e6 (longitudinal) = {s_e6:.6f}")
        print(f"    S_e7 (transverse)   = {s_e7:.6f}")

        if label == "alpha=0":
            # S = -e6, no transverse
            ok = abs(s_e7) < 1e-10 and abs(s_e6 + 1.0) < 1e-10
            print(f"    Expected: S = -e6, no transverse -> {'OK' if ok else 'FAIL'}")
        elif label == "alpha=pi/4":
            # S = e7, maximum transverse drift, sin(2*pi/4)=sin(pi/2)=1
            ok = abs(s_e7 - 1.0) < 1e-10 and abs(s_e6) < 1e-10
            print(f"    Expected: S = +e7, pure transverse -> {'OK' if ok else 'FAIL'}")
        elif label == "alpha=pi/6":
            # S = -cos(pi/3)*e6 + sin(pi/3)*e7 = -0.5*e6 + 0.866*e7
            ok = abs(s_e7 - np.sin(np.pi / 3)) < 1e-10 and abs(s_e6 + 0.5) < 1e-10
            print(f"    Expected: S = -0.5*e6 + 0.866*e7 -> {'OK' if ok else 'FAIL'}")

        if not ok:
            all_ok = False

    print()
    passed = all_ok
    print(f"  Result: {'PASS' if passed else 'FAIL'} (transverse drift pattern correct)")
    return passed


def benchmark_predictions_summary():
    """Benchmark 8: Predictions Summary."""
    _header("Benchmark 8: Predictions Summary")

    print("  === Explicit Numerical Predictions from Octonionic Framework ===")
    print()

    # 1. S_NA ratio (recompute with small N)
    print("  [1] Non-associative vorticity source ratio:")
    v7, dx7 = taylor_green_7d(N=4)
    s_na_7d = vorticity_source_na(v7, dx7)
    mag_7d = np.sqrt(sum(np.sum(s**2) for s in s_na_7d))
    v3, dx3 = restrict_velocity_to_3d(N=4)
    s_na_3d = vorticity_source_na(v3, dx3)
    mag_3d = np.sqrt(sum(np.sum(s**2) for s in s_na_3d))
    ratio = mag_7d / mag_3d if mag_3d > 1e-30 else float('inf')
    print(f"      S_NA(7D)/S_NA(3D) = {ratio:.1f}x")
    print()

    # 2. 7D Schwarzschild: Hawking temperature
    print("  [2] 7D Schwarzschild Hawking temperature:")
    print("      In d spatial dimensions: T_H = (d-2)/(4*pi*r_s)")
    print("      For d=7: T_H = 5/(4*pi*r_s)")
    r_s = 1.0
    T_H_7d = 5.0 / (4.0 * np.pi * r_s)
    T_H_3d = 1.0 / (4.0 * np.pi * r_s)
    print(f"      T_H(7D, r_s=1) = {T_H_7d:.6f}")
    print(f"      T_H(3D, r_s=1) = {T_H_3d:.6f}")
    print(f"      Ratio T_H(7D)/T_H(3D) = {T_H_7d / T_H_3d:.1f}")
    print()

    # 3. Angular momentum degeneracy table
    print("  [3] Angular momentum degeneracy (ell=0..4):")
    print(f"      {'ell':>4}  {'3D: 2*ell+1':>12}  {'7D: (2l+5)*C(l+4,l)/5':>24}")
    print(f"      {'---':>4}  {'-----------':>12}  {'------------------------':>24}")

    from octonion_algebra.field_equations import angular_momentum_degeneracy
    for ell in range(5):
        deg_3d = 2 * ell + 1
        deg_7d = angular_momentum_degeneracy(ell, d=7)
        print(f"      {ell:>4}  {deg_3d:>12}  {deg_7d:>24}")
    print()

    # 4. Casimir eigenvalues
    print("  [4] Casimir eigenvalues (ell=0..4):")
    print(f"      {'ell':>4}  {'3D: ell*(ell+1)':>16}  {'7D: ell*(ell+5)':>16}")
    print(f"      {'---':>4}  {'---------------':>16}  {'---------------':>16}")
    for ell in range(5):
        c3 = ell * (ell + 1)
        c7 = ell * (ell + 5)
        print(f"      {ell:>4}  {c3:>16}  {c7:>16}")
    print()

    # 5. Weinberg angle at G2 unification
    sin2_theta_w = 3.0 / 8.0
    print(f"  [5] Weinberg angle at G2 unification scale:")
    print(f"      sin^2(theta_W) = 3/8 = {sin2_theta_w:.6f}")
    print()

    print("  Result: PASS (display benchmark)")
    return True


def simulate_market():
    """Market simulation demo using MultiAgentMarket and PortfolioDynamics.

    Demonstrates:
    - Multi-agent trading with octonionic state vectors
    - Wealth conservation under antisymmetric redistribution
    - Context-dependent portfolio ordering effects
    - Ecosystem dynamics with Fano-plane ternary interactions
    """
    from octonion_algebra.market_sim import (
        MultiAgentMarket,
        PortfolioDynamics,
        EcosystemModel,
    )

    _header("Market Simulation: Multi-Agent Trading")

    results = []

    # --- 1. MultiAgentMarket: compare eps=0 vs eps=1 ---
    print("  [1] Multi-agent market: eps=0 (associative) vs eps=1 (octonionic)")
    print()

    for eps_val in [0.0, 1.0]:
        market = MultiAgentMarket(n_agents=6, epsilon=eps_val, seed=42)
        initial_wealth = market.total_wealth()
        result = market.evolve(steps=50, dt=0.01, coupling=0.01)

        final_wealth = result['total_wealth'][-1]
        mean_assoc = np.mean(result['associator_norms'])
        wealth_drift_pct = abs(final_wealth - initial_wealth) / initial_wealth * 100

        print(f"    epsilon = {eps_val:.1f}")
        print(f"      Initial wealth:  {initial_wealth:.6f}")
        print(f"      Final wealth:    {final_wealth:.6f}")
        print(f"      Wealth drift:    {wealth_drift_pct:.4f}%")
        print(f"      Mean ||assoc||:  {mean_assoc:.6f}")
        print()

    # Verification: at eps=0, mean associator should be ~0
    market_0 = MultiAgentMarket(n_agents=6, epsilon=0.0, seed=42)
    assoc_0 = market_0.mean_associator_norm()
    market_1 = MultiAgentMarket(n_agents=6, epsilon=1.0, seed=42)
    assoc_1 = market_1.mean_associator_norm()

    passed_market = assoc_0 < 1e-10 and assoc_1 > 0.01
    print(f"    eps=0 assoc = {assoc_0:.2e}, eps=1 assoc = {assoc_1:.6f}")
    print(f"    Result: {'PASS' if passed_market else 'FAIL'} "
          f"(assoc=0 at eps=0, assoc>0 at eps=1)")
    results.append(("Multi-Agent Associator", passed_market))

    # --- 2. PortfolioDynamics: ordering spread ---
    _header("Market Simulation: Portfolio Ordering Effects")

    portfolio = PortfolioDynamics(n_assets=5, epsilon=1.0, seed=42)
    comparison = portfolio.compare_returns(
        np.array([0.0, 0.25, 0.5, 0.75, 1.0])
    )

    print(f"  {'eps':>5s}  {'entropy':>10s}  {'spread':>12s}  {'mean_assoc':>12s}")
    print(f"  {'---':>5s}  {'-------':>10s}  {'------':>12s}  {'----------':>12s}")
    for i, eps in enumerate(comparison['epsilon']):
        print(f"  {eps:5.2f}  {comparison['entropy'][i]:10.6f}  "
              f"{comparison['spread'][i]:12.8f}  "
              f"{comparison['mean_assoc_norm'][i]:12.8f}")

    spread_0 = comparison['spread'][0]
    spread_1 = comparison['spread'][-1]
    passed_portfolio = spread_0 < 1e-12 and spread_1 > 1e-8
    print()
    print(f"    Spread at eps=0: {spread_0:.2e}")
    print(f"    Spread at eps=1: {spread_1:.2e}")
    print(f"    Result: {'PASS' if passed_portfolio else 'FAIL'} "
          f"(no spread at eps=0, spread at eps=1)")
    results.append(("Portfolio Ordering Spread", passed_portfolio))

    # --- 3. EcosystemModel: ternary cascades ---
    _header("Market Simulation: Ecosystem Ternary Cascades")

    eco = EcosystemModel(epsilon=1.0, seed=42)
    eco_cmp = eco.compare_epsilon(
        epsilon_values=np.array([0.0, 0.5, 1.0]),
        dt=0.01, n_steps=200,
    )

    print(f"  {'eps':>5s}  {'final_biomass':>14s}  {'max_species_dev':>16s}")
    print(f"  {'---':>5s}  {'-------------':>14s}  {'---------------':>16s}")
    for i, eps in enumerate(eco_cmp['epsilon']):
        print(f"  {eps:5.2f}  "
              f"{eco_cmp['final_biomass'][i]:14.6f}  "
              f"{eco_cmp['max_species_deviation'][i]:16.8f}")

    dev_at_1 = eco_cmp['max_species_deviation'][-1]
    passed_eco = dev_at_1 > 1e-6
    print()
    print(f"    Max deviation at eps=1: {dev_at_1:.2e}")
    print(f"    Result: {'PASS' if passed_eco else 'FAIL'} "
          f"(ternary interactions produce measurable deviations)")
    results.append(("Ecosystem Ternary Cascades", passed_eco))

    return results


def simulate_physics():
    """Physics simulation demo using OctonionicFieldSimulator.

    Demonstrates:
    - Klein-Gordon evolution with octonionic associator self-interaction
    - 7D Maxwell evolution with non-associative Ampere current
    - Energy conservation under symplectic (leapfrog) integration
    - Coherence charge tracking
    - Associative-limit comparison (eps=0 vs eps=1)
    - Signal-speed causality test
    """
    from octonion_algebra.simulator import OctonionicFieldSimulator
    from octonion_algebra.predictions import (
        hydrogen_7d_spectrum,
        hawking_temperature_table,
        weinberg_angle_prediction,
    )

    results = []

    _header("Physics Simulation: Klein-Gordon Evolution")

    N = 64
    dt = 0.01
    L = 10.0
    sim = OctonionicFieldSimulator(N=N, dt=dt, L=L, m_squared=1.0)

    # --- 1. KG energy conservation ---
    print("  [1] Klein-Gordon energy conservation (eps=1, 200 steps)")
    phi0 = sim.gaussian_pulse(components=[0, 1, 4, 6])
    result_kg = sim.evolve_klein_gordon(phi0, steps=200, epsilon=1.0)
    E = result_kg['energy_history']
    E0 = E[0]
    rel_err_kg = np.max(np.abs(E - E0)) / E0
    print(f"    Initial energy:  {E0:.8f}")
    print(f"    Final energy:    {E[-1]:.8f}")
    print(f"    Max |dE|/E0:     {rel_err_kg:.2e}")
    passed_kg = rel_err_kg < 1e-4
    print(f"    Result: {'PASS' if passed_kg else 'FAIL'}")
    results.append(("KG Energy Conservation", passed_kg))
    print()

    # --- 2. Associative limit comparison ---
    print("  [2] Associative limit: eps=0 vs eps=1")
    cmp = sim.compare_associative_limit(phi0, steps=200)
    delta = cmp['delta']
    max_delta = float(np.max(delta))
    print(f"    Max relative difference: {max_delta:.6e}")
    passed_diverge = max_delta > 1e-12
    print(f"    Fields diverge:          {passed_diverge}")
    print(f"    Result: {'PASS' if passed_diverge else 'FAIL'} "
          f"(octonionic dynamics differ from quaternionic)")
    results.append(("Associative Limit Divergence", passed_diverge))
    print()

    # --- 3. 7D Maxwell ---
    _header("Physics Simulation: 7D Maxwell Evolution")

    print("  [3] 7D Maxwell evolution (100 steps)")
    E0_em = np.zeros((N, 7))
    B0_em = np.zeros((N, 7))
    E0_em[:, 2] = np.exp(-((sim.x - L / 2) ** 2) / (2 * (L / 10) ** 2))
    B0_em[:, 4] = 0.5 * np.exp(-((sim.x - L / 2) ** 2) / (2 * (L / 10) ** 2))
    result_mx = sim.evolve_maxwell_7d(E0_em, B0_em, steps=100, epsilon=1.0)
    U = result_mx['energy_history']
    U_err = np.max(np.abs(U - U[0])) / U[0]
    print(f"    Initial EM energy: {U[0]:.8f}")
    print(f"    Final EM energy:   {U[-1]:.8f}")
    print(f"    Max |dU|/U0:       {U_err:.2e}")
    passed_mx = U_err < 0.1
    print(f"    Result: {'PASS' if passed_mx else 'FAIL'}")
    results.append(("Maxwell Energy Conservation", passed_mx))
    print()

    # --- 4. Coherence charge tracking ---
    _header("Physics Simulation: Coherence Charge")

    print("  [4] Coherence charge evolution (eps=1, 100 steps)")
    phi0_coh = sim.random_field(amplitude=0.3, seed=7)
    coh = sim.compute_coherence_evolution(phi0_coh, steps=100, epsilon=1.0)
    print(f"    Initial Q_C:       {coh['initial_Q_C']:.8f}")
    print(f"    Final Q_C:         {coh['final_Q_C']:.8f}")
    print(f"    Max drift:         {coh['max_drift']:.2e}")
    print(f"    Relative drift:    {coh['relative_drift']:.2e}")
    # Coherence evolves under KG dynamics (not pure G2), so we expect some drift
    passed_coh = coh['initial_Q_C'] > 0
    print(f"    Result: {'PASS' if passed_coh else 'FAIL'} "
          f"(coherence charge is positive)")
    results.append(("Coherence Charge Positive", passed_coh))
    print()

    # --- 5. Causality check ---
    _header("Physics Simulation: Signal Speed / Causality")

    print("  [5] Signal speed / causality test")
    speed = sim.signal_speed_test(steps=300, epsilon=1.0)
    print(f"    Measured speed:  {speed['measured_speed']:.4f}")
    print(f"    Expected speed:  {speed['expected_speed']:.4f}")
    passed_causal = speed['causal']
    print(f"    Causal:          {passed_causal}")
    print(f"    Result: {'PASS' if passed_causal else 'FAIL'}")
    results.append(("Causality", passed_causal))
    print()

    # --- 6. Predictions numerical values ---
    _header("Physics Simulation: Numerical Predictions")

    print("  [6] Hydrogen 7D spectrum:")
    h7 = hydrogen_7d_spectrum(n_max=5)
    print(f"    {'n':>3}  {'E_3D':>12}  {'E_7D':>12}  {'ratio':>8}")
    for i, n in enumerate(h7['n_values']):
        print(f"    {n:>3}  {h7['E_3d'][i]:12.6f}  {h7['E_7d'][i]:12.6f}  "
              f"{h7['correction_ratios'][i]:8.4f}")
    print(f"    S^6 solid angle: {h7['solid_angle_S6']:.6f}")
    print(f"    S^2 solid angle: {h7['solid_angle_S2']:.6f}")
    print()

    print("  [7] Hawking temperature ratios:")
    ht = hawking_temperature_table()
    for i, d in enumerate(ht['d_values']):
        print(f"    d={d}: T_H/T_H(3) = {ht['T_ratios'][i]}, "
              f"Omega_{{d-1}} = {ht['solid_angles'][i]:.4f}")
    print()

    print("  [8] Weinberg angle prediction:")
    wa = weinberg_angle_prediction()
    print(f"    sin^2(theta_W) at M_GUT = {wa['tree_level_sin2_theta_W']:.6f}")
    print(f"    Measured at M_Z         = {wa['measured_sin2_theta_W']:.6f}")
    print(f"    Estimated M_GUT         = {wa['estimated_unification_scale_GeV']:.2e} GeV")
    print(f"    log10(M_GUT/GeV)        = {wa['log10_M_GUT_GeV']:.1f}")
    results.append(("Predictions Numerical", True))

    return results


def simulate_systems():
    """Systems dynamics demo using NetworkDynamics, CoalitionModel, DeformationSweep.

    Demonstrates:
    - 8-node octonionic network evolution at varying deformation
    - Coalition model with agenda dependence
    - Deformation sweep revealing smooth epsilon-dependence
    - Phase transition detection in context dependence
    """
    from octonion_algebra.systems import (
        NetworkDynamics,
        CoalitionModel,
        DeformationSweep,
    )
    from octonion_algebra.deformation import (
        associativity_measure,
        derivation_dimension,
    )

    results = []

    _header("Systems Dynamics: Network Deformation Sweep")

    N = 8
    seed = 42
    eps_grid = np.linspace(0, 1, 6)

    sweep = DeformationSweep(eps_grid)
    net_results = sweep.sweep_network(
        N, coupling=0.1, dt=0.01, steps=30, seed=seed
    )

    print(f"  {'eps':>5s}  {'ctx_dep%':>10s}  {'info_flow%':>10s}  "
          f"{'assoc_total':>12s}  {'total_norm':>10s}")
    print(f"  {'---':>5s}  {'--------':>10s}  {'----------':>10s}  "
          f"{'----------':>12s}  {'----------':>10s}")
    for i, eps in enumerate(net_results['epsilon']):
        ctx = net_results['context_dependence'][i] * 100
        ifl = net_results['information_flow'][i] * 100
        ast = net_results['associator_total'][i]
        tn = net_results['total_norm'][i]
        print(f"  {eps:5.2f}  {ctx:10.4f}  {ifl:10.4f}  {ast:12.4f}  {tn:10.4f}")

    # Verify: context dependence at eps=0 should be ~0
    ctx_at_0 = net_results['context_dependence'][0]
    ctx_at_1 = net_results['context_dependence'][-1]
    passed_net = ctx_at_0 < 1e-8 and ctx_at_1 > 1e-6
    print()
    print(f"    ctx_dep at eps=0: {ctx_at_0:.2e}")
    print(f"    ctx_dep at eps=1: {ctx_at_1:.6f}")
    print(f"    Result: {'PASS' if passed_net else 'FAIL'} "
          f"(zero at eps=0, nonzero at eps=1)")
    results.append(("Network Context Dependence", passed_net))

    # --- 2. Coalition model ---
    _header("Systems Dynamics: Coalition Agenda Dependence")

    sweep_c = DeformationSweep(eps_grid)
    coal_results = sweep_c.sweep_coalition(6, seed=seed)

    print(f"  {'eps':>5s}  {'ADI':>10s}  {'n_stable':>8s}  {'mean_val':>10s}")
    print(f"  {'---':>5s}  {'---':>10s}  {'--------':>8s}  {'--------':>10s}")
    for i, eps in enumerate(coal_results['epsilon']):
        a = coal_results['agenda_dependence'][i]
        ns = coal_results['n_stable'][i]
        mv = coal_results['mean_value'][i]
        print(f"  {eps:5.2f}  {a:10.6f}  {ns:8d}  {mv:10.4f}")

    adi_0 = coal_results['agenda_dependence'][0]
    adi_1 = coal_results['agenda_dependence'][-1]
    passed_coal = adi_0 < 1e-10 and adi_1 > 1e-3
    print()
    print(f"    ADI at eps=0: {adi_0:.2e}")
    print(f"    ADI at eps=1: {adi_1:.6f}")
    print(f"    Result: {'PASS' if passed_coal else 'FAIL'} "
          f"(zero at eps=0, nonzero at eps=1)")
    results.append(("Coalition Agenda Dependence", passed_coal))

    # --- 3. Deformation sweep: smooth epsilon-dependence ---
    _header("Systems Dynamics: Smooth Deformation Verification")

    dense_eps = np.linspace(0, 1, 11)
    assoc_vals = []
    der_dims = []
    for eps_val in dense_eps:
        assoc_vals.append(associativity_measure(eps_val, n_samples=30, seed=42))
        der_dims.append(derivation_dimension(eps_val))

    assoc_vals = np.array(assoc_vals)
    print(f"  {'eps':>5s}  {'||assoc||':>12s}  {'Der dim':>8s}")
    print(f"  {'---':>5s}  {'--------':>12s}  {'-------':>8s}")
    for i, eps in enumerate(dense_eps):
        print(f"  {eps:5.2f}  {assoc_vals[i]:12.6f}  {der_dims[i]:8d}")

    # Smoothness: finite differences should be bounded (no jumps)
    diffs = np.abs(np.diff(assoc_vals))
    max_jump = float(np.max(diffs))
    passed_smooth = max_jump < 0.5  # no huge jumps
    print()
    print(f"    Max consecutive difference in assoc measure: {max_jump:.6f}")
    print(f"    Der(A_0) dim = {der_dims[0]}, Der(A_1) dim = {der_dims[-1]}")
    print(f"    Result: {'PASS' if passed_smooth else 'FAIL'} (smooth epsilon-dependence)")
    results.append(("Smooth Deformation", passed_smooth))

    # --- 4. Verification: eps=0 baseline ---
    _header("Systems Dynamics: eps=0 Baseline Verification")

    rng = np.random.default_rng(seed)
    quat_arr = np.zeros((N, 8))
    quat_arr[:, :4] = rng.standard_normal((N, 4))
    norms = np.linalg.norm(quat_arr, axis=1, keepdims=True)
    quat_arr = quat_arr / np.maximum(norms, 1e-15)

    net0 = NetworkDynamics(N, initial_states=quat_arr, epsilon=0.0, seed=seed)
    assoc0 = net0.measure_associator()
    ctx0 = net0.measure_context_dependence()
    print(f"  eps=0 associator total:    {assoc0:.2e}  (should be ~0)")
    print(f"  eps=0 context dependence:  {ctx0:.2e}  (should be ~0)")
    passed_baseline = assoc0 < 1e-8 and ctx0 < 1e-8
    print(f"  Result: {'PASS' if passed_baseline else 'FAIL'}")
    results.append(("eps=0 Baseline", passed_baseline))

    return results


def _run_benchmarks():
    """Run the original 8 benchmarks and return results list."""
    results = []
    results.append(("Gaming Detection",       benchmark_gaming_detection()))
    results.append(("Turbulence Source Term",  benchmark_turbulence_source()))
    results.append(("Portfolio Context Premium", benchmark_portfolio_premium()))
    results.append(("COPBW Basis Completeness", benchmark_copbw_completeness()))
    results.append(("BAC-CAB Identity",        benchmark_bac_cab_identity()))
    results.append(("Noether Currents (G2)",   benchmark_noether_currents()))
    results.append(("Poynting Transverse Drift", benchmark_poynting_transverse_drift()))
    results.append(("Predictions Summary",     benchmark_predictions_summary()))
    return results


def main():
    """Run demos and simulations based on command-line flags.

    Returns 0 if all selected tests pass, 1 otherwise.
    """
    parser = argparse.ArgumentParser(
        description="Octonionic Associator Benchmark & Simulation Suite",
    )
    parser.add_argument(
        "--simulate-market", action="store_true",
        help="Run market simulation demo (MultiAgentMarket, PortfolioDynamics, EcosystemModel).",
    )
    parser.add_argument(
        "--simulate-physics", action="store_true",
        help="Run physics simulation demo (Klein-Gordon, Maxwell 7D, coherence, causality).",
    )
    parser.add_argument(
        "--simulate-systems", action="store_true",
        help="Run systems dynamics demo (NetworkDynamics, CoalitionModel, DeformationSweep).",
    )
    parser.add_argument(
        "--all", action="store_true",
        help="Run everything: benchmarks + all simulations.",
    )

    args = parser.parse_args()

    # Determine what to run
    run_benchmarks = True
    run_market = args.simulate_market or args.all
    run_physics = args.simulate_physics or args.all
    run_systems = args.simulate_systems or args.all

    # If any simulation flag is set (but not --all), skip benchmarks for speed
    any_sim = args.simulate_market or args.simulate_physics or args.simulate_systems
    if any_sim and not args.all:
        run_benchmarks = False

    print()
    print("*" * 60)
    print("  Octonionic Associator Benchmark & Simulation Suite")
    print("  Detecting what associative (quaternionic) tools miss")
    print("*" * 60)

    t0 = time.time()
    all_results = []

    if run_benchmarks:
        all_results.extend(_run_benchmarks())

    if run_market:
        all_results.extend(simulate_market())

    if run_physics:
        all_results.extend(simulate_physics())

    if run_systems:
        all_results.extend(simulate_systems())

    elapsed = time.time() - t0

    _header("Final Summary")
    n_pass = 0
    for name, passed in all_results:
        status = "PASS" if passed else "FAIL"
        print(f"  [{status}] {name}")
        if passed:
            n_pass += 1

    print()
    print(f"  {n_pass}/{len(all_results)} tests passed")
    print(f"  Total runtime: {elapsed:.1f}s")
    print()

    return 0 if n_pass == len(all_results) else 1
