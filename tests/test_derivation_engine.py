"""
Tests for the octonionic derivation engine.

Verifies that the engine correctly derives field equations from the COA
axioms by numerical variation of the Klein-Gordon action, and that the
associator correction scales correctly for nonlinear terms.
"""

import numpy as np
import pytest

from octonion_algebra.core import Octonion
from octonion_algebra.derivation_engine import (
    FieldConfiguration,
    vary_action,
    derive_euler_lagrange,
    derive_field_equation_steps,
    verify_derivation_numerically,
    associator_correction_derivation,
    DerivationReport,
    full_derivation_demo,
)


# ===================================================================
# TestFieldConfiguration
# ===================================================================

class TestFieldConfiguration:
    """Tests for the FieldConfiguration class."""

    def test_grid_size(self):
        """grid_size returns the number of grid points."""
        phi = np.zeros((20, 8))
        fc = FieldConfiguration(phi)
        assert fc.grid_size == 20

    def test_phi_property(self):
        """phi property returns the stored array."""
        phi = np.ones((10, 8))
        fc = FieldConfiguration(phi)
        assert fc.phi.shape == (10, 8)
        np.testing.assert_array_equal(fc.phi, phi)

    def test_zero_field_zero_action(self):
        """A zero field should have zero action."""
        phi = np.zeros((30, 8))
        fc = FieldConfiguration(phi)
        S = fc.action(dx=0.1, dt=1.0, m_sq=1.0)
        assert abs(S) < 1e-15

    def test_action_is_real(self):
        """The action should always be a real (float) number."""
        rng = np.random.default_rng(0)
        phi = rng.uniform(-1, 1, size=(25, 8))
        fc = FieldConfiguration(phi)
        S = fc.action(dx=0.2, dt=0.5, m_sq=1.0)
        assert isinstance(S, float)

    def test_kinetic_energy_nonnegative(self):
        """Kinetic energy is a sum of squares, so must be >= 0."""
        rng = np.random.default_rng(1)
        phi = rng.uniform(-1, 1, size=(30, 8))
        fc = FieldConfiguration(phi)
        T = fc.kinetic_energy(dx=0.2)
        assert T >= 0.0

    def test_potential_energy_nonnegative(self):
        """Potential energy (with positive m^2) must be >= 0."""
        rng = np.random.default_rng(2)
        phi = rng.uniform(-1, 1, size=(30, 8))
        fc = FieldConfiguration(phi)
        V = fc.potential_energy(dx=0.2, m_sq=1.0)
        assert V >= 0.0

    def test_constant_field_zero_kinetic(self):
        """A spatially constant field has zero gradient -> zero kinetic energy."""
        phi = np.tile([1.0, 0.5, -0.3, 0, 0, 0, 0, 0], (40, 1))
        fc = FieldConfiguration(phi)
        T = fc.kinetic_energy(dx=0.1)
        assert T < 1e-20

    def test_invalid_shape_raises(self):
        """Passing an array with wrong second dimension should raise."""
        with pytest.raises(ValueError):
            FieldConfiguration(np.zeros((10, 5)))


# ===================================================================
# TestVariation
# ===================================================================

class TestVariation:
    """Tests for the vary_action function."""

    def test_variation_shape(self):
        """Variation should have the same shape as the field array."""
        phi = np.random.default_rng(3).uniform(-1, 1, size=(15, 8))
        fc = FieldConfiguration(phi)
        var = vary_action(fc, dx=0.2, m_sq=1.0)
        assert var.shape == (15, 8)

    def test_zero_field_zero_variation(self):
        """Variation of a zero field should be zero (S is at a minimum)."""
        phi = np.zeros((20, 8))
        fc = FieldConfiguration(phi)
        var = vary_action(fc, dx=0.2, m_sq=1.0)
        assert np.max(np.abs(var)) < 1e-10

    def test_variation_symmetry(self):
        """For a symmetric field phi(x)=phi(-x), the variation should also
        be symmetric.  We approximate this with a palindromic field array."""
        rng = np.random.default_rng(5)
        half = rng.uniform(-0.5, 0.5, size=(10, 8))
        phi = np.concatenate([half, half[::-1]], axis=0)
        fc = FieldConfiguration(phi)
        var = vary_action(fc, dx=0.2, m_sq=1.0)
        # The variation at index i should equal the variation at N-1-i
        N = phi.shape[0]
        max_asym = np.max(np.abs(var[:N // 2] - var[N // 2:][::-1]))
        assert max_asym < 1e-7


# ===================================================================
# TestEulerLagrange
# ===================================================================

class TestEulerLagrange:
    """Tests for derive_euler_lagrange."""

    def test_agreement(self):
        """Numerical and analytic Euler-Lagrange should agree."""
        rng = np.random.default_rng(10)
        phi = rng.uniform(-0.5, 0.5, size=(30, 8))
        fc = FieldConfiguration(phi)
        result = derive_euler_lagrange(fc, dx=0.25, m_sq=1.0)
        assert result['agreement'] is True

    def test_max_error_small(self):
        """max_error should be well below 1e-3."""
        rng = np.random.default_rng(11)
        phi = rng.uniform(-0.5, 0.5, size=(30, 8))
        fc = FieldConfiguration(phi)
        result = derive_euler_lagrange(fc, dx=0.25, m_sq=1.0)
        assert result['max_error'] < 1e-3

    def test_returns_correct_keys(self):
        """Result dict should contain the expected keys."""
        phi = np.zeros((10, 8))
        fc = FieldConfiguration(phi)
        result = derive_euler_lagrange(fc, dx=0.2, m_sq=1.0)
        for key in ['numerical', 'analytic', 'max_error', 'agreement']:
            assert key in result


# ===================================================================
# TestDerivationSteps
# ===================================================================

class TestDerivationSteps:
    """Tests for derive_field_equation_steps."""

    def test_correct_number_of_steps(self):
        """There should be exactly 5 derivation steps."""
        steps = derive_field_equation_steps()
        assert len(steps) == 5

    def test_each_step_has_axiom(self):
        """Every step must reference a COA axiom or physical principle."""
        steps = derive_field_equation_steps()
        for s in steps:
            assert 'axiom_used' in s
            assert len(s['axiom_used']) > 0

    def test_steps_in_order(self):
        """Step numbers should be 1, 2, 3, 4, 5 in sequence."""
        steps = derive_field_equation_steps()
        numbers = [s['step_number'] for s in steps]
        assert numbers == [1, 2, 3, 4, 5]

    def test_each_step_has_description(self):
        """Every step must have a non-empty description."""
        steps = derive_field_equation_steps()
        for s in steps:
            assert 'description' in s
            assert len(s['description']) > 10


# ===================================================================
# TestAssociatorCorrection
# ===================================================================

class TestAssociatorCorrection:
    """Tests for associator_correction_derivation."""

    def test_correction_is_cubic(self):
        """The correction should scale as O(phi^3).  We check that the
        ratio  correction_norm / field_norm^3  is roughly constant when
        we scale the field by a factor."""
        rng = np.random.default_rng(20)
        phi_base = rng.uniform(-1, 1, size=(20, 8))

        ratios = []
        for scale in [0.5, 1.0, 2.0]:
            fc = FieldConfiguration(phi_base * scale)
            res = associator_correction_derivation(fc, dx=0.2)
            ratios.append(res['ratio'])

        # All ratios should be close to each other (within a factor of 2)
        assert max(ratios) < 2.0 * min(ratios) + 1e-10

    def test_zero_field_zero_correction(self):
        """A zero field should produce zero associator correction."""
        phi = np.zeros((15, 8))
        fc = FieldConfiguration(phi)
        res = associator_correction_derivation(fc, dx=0.2)
        assert res['correction_norm'] < 1e-15
        assert res['field_norm'] < 1e-15

    def test_quaternionic_field_zero_correction(self):
        """A field restricted to a quaternionic subalgebra (e0, e1, e2, e3)
        should have zero associator correction because quaternions are
        associative."""
        rng = np.random.default_rng(30)
        phi = np.zeros((20, 8))
        phi[:, :4] = rng.uniform(-1, 1, size=(20, 4))
        fc = FieldConfiguration(phi)
        res = associator_correction_derivation(fc, dx=0.2)
        assert res['correction_norm'] < 1e-12


# ===================================================================
# TestVerifyDerivation
# ===================================================================

class TestVerifyDerivation:
    """Tests for verify_derivation_numerically."""

    def test_agreement(self):
        """The global verification should report agreement."""
        result = verify_derivation_numerically(N=30, dx=0.25, m_sq=1.0)
        assert result['agreement'] is True

    def test_max_error_reported(self):
        """max_error should be a positive float."""
        result = verify_derivation_numerically(N=30, dx=0.25, m_sq=1.0)
        assert isinstance(result['max_error'], float)
        assert result['max_error'] >= 0.0


# ===================================================================
# TestDerivationReport
# ===================================================================

class TestDerivationReport:
    """Tests for the DerivationReport class."""

    def test_add_step(self):
        """Adding steps should populate the summary."""
        report = DerivationReport()
        report.add_step(1, "test step", "test axiom", "test result")
        summary = report.summary()
        assert len(summary['steps']) == 1
        assert summary['steps'][0]['step_number'] == 1

    def test_verify_all_passes(self):
        """verify_all should return True when everything works."""
        report = DerivationReport()
        assert report.verify_all() is True

    def test_summary_has_verifications(self):
        """After verify_all, summary should contain verification data."""
        report = DerivationReport()
        report.verify_all()
        summary = report.summary()
        assert 'verifications' in summary
        assert 'euler_lagrange' in summary['verifications']
        assert 'associator_correction' in summary['verifications']

    def test_to_string_not_empty(self):
        """to_string should return a non-empty report."""
        report = DerivationReport()
        report.add_step(1, "demo", "axiom A1", "ok")
        report.verify_all()
        text = report.to_string()
        assert len(text) > 100
        assert "OCTONIONIC DERIVATION REPORT" in text


# ===================================================================
# TestFullDemo
# ===================================================================

class TestFullDemo:
    """Tests for full_derivation_demo."""

    def test_demo_completes(self):
        """full_derivation_demo should complete without error."""
        report = full_derivation_demo()
        assert report is not None

    def test_demo_report_type(self):
        """The returned object should be a DerivationReport."""
        report = full_derivation_demo()
        assert isinstance(report, DerivationReport)

    def test_demo_all_verifications_pass(self):
        """All verifications in the demo report should pass."""
        report = full_derivation_demo()
        summary = report.summary()
        assert summary['verifications']['all_pass'] is True

    def test_demo_has_steps(self):
        """The demo report should contain derivation steps."""
        report = full_derivation_demo()
        summary = report.summary()
        assert len(summary['steps']) >= 5
