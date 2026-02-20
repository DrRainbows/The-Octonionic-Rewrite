"""
Octonion algebra implementation using the Fano plane.
Basis: {1, e1, e2, e3, e4, e5, e6, e7}
An octonion is represented as a tuple of 8 real numbers (x0, x1, ..., x7)
where x = x0 + x1*e1 + x2*e2 + ... + x7*e7.
"""
import numpy as np
from typing import Tuple, List

# Fano plane triples: (i, j, k) means e_i * e_j = +e_k
# All cyclic permutations also hold: e_j * e_k = +e_i, e_k * e_i = +e_j
FANO_TRIPLES = [
    (1, 2, 3),
    (1, 4, 5),
    (2, 4, 6),
    (3, 4, 7),
    (1, 7, 6),
    (2, 5, 7),
    (3, 6, 5),
]

def _build_multiplication_table():
    """
    Build the 8x8 multiplication table for octonion basis elements.
    table[i][j] = (sign, index) means e_i * e_j = sign * e_index.
    Index 0 represents the real unit 1.
    """
    table = [[(0, 0)] * 8 for _ in range(8)]

    # e_0 * e_0 = 1
    table[0][0] = (1, 0)

    # e_0 * e_i = e_i and e_i * e_0 = e_i
    for i in range(1, 8):
        table[0][i] = (1, i)
        table[i][0] = (1, i)

    # e_i * e_i = -1 for i >= 1
    for i in range(1, 8):
        table[i][i] = (-1, 0)

    # Fano plane triples
    for (i, j, k) in FANO_TRIPLES:
        # Cyclic: e_i * e_j = +e_k
        table[i][j] = (1, k)
        table[j][k] = (1, i)
        table[k][i] = (1, j)
        # Anti-cyclic: e_j * e_i = -e_k
        table[j][i] = (-1, k)
        table[k][j] = (-1, i)
        table[i][k] = (-1, j)

    return table

MULT_TABLE = _build_multiplication_table()


class Octonion:
    """
    An element of the octonion algebra O.

    Attributes:
        coeffs: numpy array of shape (8,) representing
                 x = coeffs[0] + coeffs[1]*e1 + ... + coeffs[7]*e7
    """

    def __init__(self, coeffs=None, **kwargs):
        """
        Initialize an octonion.

        Args:
            coeffs: array-like of 8 real numbers, or None for zero.
            kwargs: named components, e.g., Octonion(e0=1, e1=2, e3=-1)
        """
        if coeffs is not None:
            self.coeffs = np.array(coeffs, dtype=float)
            assert self.coeffs.shape == (8,), "Octonion requires exactly 8 components"
        elif kwargs:
            self.coeffs = np.zeros(8)
            for key, val in kwargs.items():
                if key == 'real' or key == 'e0':
                    self.coeffs[0] = val
                else:
                    idx = int(key[1:])  # e.g., 'e3' -> 3
                    self.coeffs[idx] = val
        else:
            self.coeffs = np.zeros(8)

    @classmethod
    def basis(cls, i):
        """Return the i-th basis element (e_0 = 1, e_1, ..., e_7)."""
        c = np.zeros(8)
        c[i] = 1.0
        return cls(c)

    @classmethod
    def real(cls, r):
        """Return a real octonion (scalar)."""
        return cls([r, 0, 0, 0, 0, 0, 0, 0])

    @classmethod
    def random(cls, seed=None):
        """Return a random octonion with components in [-1, 1]."""
        rng = np.random.default_rng(seed)
        return cls(rng.uniform(-1, 1, size=8))

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
        return ' '.join(parts) if parts else '0'

    def __add__(self, other):
        if isinstance(other, (int, float)):
            other = Octonion.real(other)
        return Octonion(self.coeffs + other.coeffs)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            other = Octonion.real(other)
        return Octonion(self.coeffs - other.coeffs)

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            other = Octonion.real(other)
        return Octonion(other.coeffs - self.coeffs)

    def __neg__(self):
        return Octonion(-self.coeffs)

    def __mul__(self, other):
        """
        Octonion multiplication using the Fano plane multiplication table.
        For scalar multiplication, use smul().
        """
        if isinstance(other, (int, float)):
            return Octonion(self.coeffs * other)
        result = np.zeros(8)
        for i in range(8):
            if abs(self.coeffs[i]) < 1e-15:
                continue
            for j in range(8):
                if abs(other.coeffs[j]) < 1e-15:
                    continue
                sign, idx = MULT_TABLE[i][j]
                result[idx] += sign * self.coeffs[i] * other.coeffs[j]
        return Octonion(result)

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return Octonion(self.coeffs * other)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Octonion(self.coeffs / other)
        # Division by an octonion: self * other^{-1}
        return self * other.inverse()

    def conjugate(self):
        """Return the conjugate: x0 - x1*e1 - ... - x7*e7."""
        c = self.coeffs.copy()
        c[1:] = -c[1:]
        return Octonion(c)

    def norm_squared(self):
        """Return |x|^2 = x * conj(x) = sum of squares of all components."""
        return np.dot(self.coeffs, self.coeffs)

    def norm(self):
        """Return |x| = sqrt(sum of squares)."""
        return np.sqrt(self.norm_squared())

    def inverse(self):
        """Return x^{-1} = conj(x) / |x|^2."""
        ns = self.norm_squared()
        if ns < 1e-30:
            raise ZeroDivisionError("Cannot invert zero octonion")
        return self.conjugate() / ns

    def real_part(self):
        """Return the real (scalar) part."""
        return self.coeffs[0]

    def imag_part(self):
        """Return the imaginary part as an Octonion with zero real part."""
        c = self.coeffs.copy()
        c[0] = 0.0
        return Octonion(c)

    def imag_vector(self):
        """Return the imaginary part as a 7-component numpy array."""
        return self.coeffs[1:].copy()

    def dot(self, other):
        """Inner product: Re(x * conj(y)) = sum of component products."""
        return np.dot(self.coeffs, other.coeffs)

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            other = Octonion.real(other)
        return np.allclose(self.coeffs, other.coeffs, atol=1e-10)

    def is_zero(self, tol=1e-10):
        return self.norm() < tol

    def is_real(self, tol=1e-10):
        return np.all(np.abs(self.coeffs[1:]) < tol)

    def is_imaginary(self, tol=1e-10):
        return abs(self.coeffs[0]) < tol


# ---- Convenience constructors ----
def oct(x0=0, x1=0, x2=0, x3=0, x4=0, x5=0, x6=0, x7=0):
    """Shorthand constructor for an octonion."""
    return Octonion([x0, x1, x2, x3, x4, x5, x6, x7])

# Basis elements
e0 = Octonion.basis(0)  # = 1
e1 = Octonion.basis(1)
e2 = Octonion.basis(2)
e3 = Octonion.basis(3)
e4 = Octonion.basis(4)
e5 = Octonion.basis(5)
e6 = Octonion.basis(6)
e7 = Octonion.basis(7)


def cross_product_7d(a, b):
    """
    Compute the 7-dimensional cross product of two imaginary octonions.

    For a, b in Im(O) ~ R^7:
        a x b = Im(a * b) = (a*b - b*a) / 2

    This is the unique (up to sign) bilinear antisymmetric product on R^7
    satisfying |a x b|^2 = |a|^2|b|^2 - (a.b)^2.

    Args:
        a: Octonion (must be purely imaginary, i.e., real part = 0)
        b: Octonion (must be purely imaginary)

    Returns:
        Octonion: the cross product (purely imaginary)
    """
    # The cross product is the imaginary part of the octonion product
    # for purely imaginary inputs
    product = a * b
    return product.imag_part()


def cross_product_7d_vectors(u, v):
    """
    Compute the 7D cross product for R^7 vectors (numpy arrays of length 7).

    Uses the structure constants f_{ijk} from the Fano plane.

    Args:
        u, v: numpy arrays of shape (7,)

    Returns:
        numpy array of shape (7,): u x v
    """
    result = np.zeros(7)
    # Structure constants from Fano triples
    # f_{ijk} = +1 for cyclic permutations of Fano triples
    for (i, j, k) in FANO_TRIPLES:
        # Convert to 0-indexed for the 7D vector
        ii, jj, kk = i - 1, j - 1, k - 1
        # Cyclic permutations: f_{ijk} = f_{jki} = f_{kij} = +1
        result[kk] += u[ii] * v[jj] - u[jj] * v[ii]
        result[ii] += u[jj] * v[kk] - u[kk] * v[jj]
        result[jj] += u[kk] * v[ii] - u[ii] * v[kk]
    return result
