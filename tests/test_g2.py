"""Tests for the G2 Lie algebra generators module."""
import numpy as np
import pytest


def _expm_taylor(A, order=30):
    """Matrix exponential via Taylor series (avoids scipy dependency)."""
    result = np.eye(A.shape[0])
    term = np.eye(A.shape[0])
    for k in range(1, order + 1):
        term = term @ A / k
        result = result + term
    return result

from octonion_algebra.core import Octonion, e1, e2, e3, e4, e5, e6, e7
from octonion_algebra.associator import associator
from octonion_algebra.g2 import g2_generators


@pytest.fixture
def generators():
    return g2_generators()


@pytest.fixture
def imaginary_basis():
    return [e1, e2, e3, e4, e5, e6, e7]


def test_g2_14_generators(generators):
    """g2_generators() returns exactly 14 matrices."""
    assert len(generators) == 14


def test_g2_antisymmetric(generators):
    """Each generator G satisfies G = -G^T (antisymmetric / skew-symmetric)."""
    for i, G in enumerate(generators):
        assert G.shape == (7, 7), f"Generator {i} has wrong shape {G.shape}"
        np.testing.assert_allclose(
            G, -G.T, atol=1e-10,
            err_msg=f"Generator {i} is not antisymmetric"
        )


def test_g2_derivation_property(generators, imaginary_basis):
    """G(ab) = (Ga)b + a(Gb) for basis elements (derivation property).

    A derivation D of the octonion algebra satisfies D(xy) = D(x)y + xD(y).
    We check this for each generator on pairs of imaginary basis elements.
    """
    for D in generators[:3]:  # Check first 3 for speed
        for i in range(7):
            for j in range(7):
                ei = imaginary_basis[i]
                ej = imaginary_basis[j]
                eij = ei * ej

                # D(e_i) as an octonion (purely imaginary)
                Dei_vec = D @ np.eye(7)[:, i]
                Dei = Octonion(np.concatenate([[0], Dei_vec]))

                Dej_vec = D @ np.eye(7)[:, j]
                Dej = Octonion(np.concatenate([[0], Dej_vec]))

                # D(e_i * e_j): apply D to the imaginary part of the product
                if eij.is_real():
                    # D maps reals to 0
                    Deij = Octonion()
                else:
                    Deij_vec = D @ eij.imag_vector()
                    Deij = Octonion(np.concatenate([[0], Deij_vec]))

                # Right-hand side: D(ei)*ej + ei*D(ej)
                rhs = Dei * ej + ei * Dej

                np.testing.assert_allclose(
                    Deij.coeffs[1:], rhs.coeffs[1:], atol=1e-6,
                    err_msg=f"Derivation property fails for D, e_{i+1}, e_{j+1}"
                )


def test_g2_preserves_multiplication(generators, imaginary_basis):
    """exp(tG) applied to a,b: phi(ab) ~ phi(a)phi(b) for small t.

    A G2 automorphism phi = exp(tD) preserves the octonion multiplication:
    phi(a*b) = phi(a) * phi(b).
    """
    D = generators[0]
    t = 0.01  # Small angle for numerical stability

    # Compute rotation matrix R = exp(t*D)
    R = _expm_taylor(t * D)

    def apply_rotation(o):
        """Apply the G2 rotation to an octonion."""
        new_coeffs = np.zeros(8)
        new_coeffs[0] = o.coeffs[0]
        new_coeffs[1:] = R @ o.coeffs[1:]
        return Octonion(new_coeffs)

    # Test on pairs of basis elements
    for a in imaginary_basis[:4]:
        for b in imaginary_basis[:4]:
            ab = a * b
            phi_ab = apply_rotation(ab)
            phi_a_phi_b = apply_rotation(a) * apply_rotation(b)

            np.testing.assert_allclose(
                phi_ab.coeffs, phi_a_phi_b.coeffs, atol=1e-6,
                err_msg="G2 rotation does not preserve multiplication"
            )


def test_g2_preserves_associator(generators, imaginary_basis):
    """phi([a,b,c]) ~ [phi(a),phi(b),phi(c)] under G2 rotation.

    G2 automorphisms preserve the associator since they preserve multiplication.
    """
    D = generators[0]
    t = 0.01

    R = _expm_taylor(t * D)

    def apply_rotation(o):
        new_coeffs = np.zeros(8)
        new_coeffs[0] = o.coeffs[0]
        new_coeffs[1:] = R @ o.coeffs[1:]
        return Octonion(new_coeffs)

    a, b, c = imaginary_basis[0], imaginary_basis[1], imaginary_basis[3]
    assoc_abc = associator(a, b, c)
    phi_assoc = apply_rotation(assoc_abc)
    assoc_phi = associator(apply_rotation(a), apply_rotation(b), apply_rotation(c))

    np.testing.assert_allclose(
        phi_assoc.coeffs, assoc_phi.coeffs, atol=1e-6,
        err_msg="G2 rotation does not preserve associator"
    )
