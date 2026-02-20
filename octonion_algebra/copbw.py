"""
COPBW (Contextual Octonionic PBW) Basis Construction and Verification.

Extracted from Appendix C sections C.7 and C.10.

In the non-associative setting, monomials are binary trees encoding
association structure. The COPBW theorem (Chapter 22) proves that
tree monomials, modulo the alternator ideal, form a basis for U_O(S).
"""

import numpy as np
from math import factorial
from octonion_algebra.core import Octonion


class TreeMonomial:
    """
    A tree monomial in the COPBW (Contextual Octonionic PBW) basis.

    In the non-associative setting, monomials are not just ordered products
    but TREES encoding the association structure. For example, for three
    generators a, b, c:
    - ((a*b)*c) and (a*(b*c)) are DIFFERENT tree monomials
    - Their difference is the associator [a,b,c]

    A tree monomial is represented as a binary tree where:
    - Leaves are generators (elements of the algebra)
    - Internal nodes are multiplication operations
    - The SHAPE of the tree encodes the association

    Attributes:
        left: TreeMonomial or str (generator name)
        right: TreeMonomial or str (generator name), or None for a leaf
        label: str, the generator name (for leaves only)
    """

    def __init__(self, left=None, right=None, label=None):
        if label is not None:
            # Leaf node (generator)
            self.left = None
            self.right = None
            self.label = label
            self.is_leaf = True
        else:
            self.left = left
            self.right = right
            self.label = None
            self.is_leaf = False

    def __repr__(self):
        if self.is_leaf:
            return self.label
        return f"({self.left} * {self.right})"

    def depth(self):
        if self.is_leaf:
            return 0
        return 1 + max(self.left.depth(), self.right.depth())

    def size(self):
        """Number of leaves (generators)."""
        if self.is_leaf:
            return 1
        return self.left.size() + self.right.size()

    def evaluate(self, assignment):
        """
        Evaluate the tree monomial given an assignment of generators to Octonions.

        Args:
            assignment: dict mapping generator names to Octonion instances.

        Returns:
            Octonion: the value of this tree monomial.
        """
        if self.is_leaf:
            return assignment[self.label]
        left_val = self.left.evaluate(assignment)
        right_val = self.right.evaluate(assignment)
        return left_val * right_val


def leaf(name):
    """Create a leaf (generator) node."""
    return TreeMonomial(label=name)


def mul(left, right):
    """Create a multiplication node."""
    return TreeMonomial(left=left, right=right)


def enumerate_tree_monomials(generators, degree):
    """
    Enumerate all tree monomials of a given degree (number of generators).

    For degree n, the number of binary trees is the Catalan number C_{n-1}.
    For n generators, there are n! orderings times C_{n-1} tree shapes.

    This is the key difference from classical PBW: in the associative case,
    all tree shapes for the same ordering give the same value, so only
    orderings matter. In the non-associative case, BOTH ordering and shape
    matter, and the associator captures the difference between shapes.

    Args:
        generators: list of generator name strings
        degree: number of generator factors in each monomial

    Returns:
        list of TreeMonomial instances
    """
    if degree == 1:
        return [leaf(g) for g in generators]

    monomials = []

    # For each way to split degree into (left_deg, right_deg)
    for left_deg in range(1, degree):
        right_deg = degree - left_deg
        left_trees = enumerate_tree_monomials(generators, left_deg)
        right_trees = enumerate_tree_monomials(generators, right_deg)

        for lt in left_trees:
            for rt in right_trees:
                monomials.append(mul(lt, rt))

    return monomials


def copbw_basis(generators, max_degree=3):
    """
    Construct the COPBW basis up to a given degree.

    The COPBW basis consists of tree monomials, ordered by:
    1. Degree (number of generator factors)
    2. Within each degree, a specific tree ordering that respects
       the octonionic structure

    In the classical PBW theorem, the basis is {x1^a1 * x2^a2 * ... * xn^an}
    with a fixed ordering. In COPBW, we must additionally track the
    association structure (tree shape).

    The COPBW theorem (Chapter 22) proves that these tree monomials,
    modulo the alternator ideal, form a basis for U_O(S).

    Args:
        generators: list of generator name strings
        max_degree: maximum degree to enumerate

    Returns:
        dict mapping degree -> list of TreeMonomial instances
    """
    basis = {}
    for d in range(1, max_degree + 1):
        trees = enumerate_tree_monomials(generators, d)
        basis[d] = trees
    return basis


def catalan(n):
    """
    Compute the n-th Catalan number.

    C(n) = (2n)! / ((n+1)! * n!)

    Args:
        n: non-negative integer

    Returns:
        int: the n-th Catalan number
    """
    return factorial(2 * n) // (factorial(n + 1) * factorial(n))


def count_bracketings(seq):
    """
    Count distinct binary tree shapes for a fixed sequence.

    For a sequence of length n, the number of bracketings is the
    Catalan number C_{n-1}.

    Args:
        seq: a list or tuple representing the fixed ordered sequence

    Returns:
        int: number of distinct bracketings
    """
    n = len(seq)
    if n == 1:
        return 1
    total = 0
    for split in range(1, n):
        left_count = count_bracketings(seq[:split])
        right_count = count_bracketings(seq[split:])
        total += left_count * right_count
    return total


def verify_basis_count(generators, max_weight=4):
    """
    Verify that COPBW basis counts match theoretical predictions.

    For weight n with k generators, tree monomials = k^n * C_{n-1},
    where C_{n-1} is the (n-1)-th Catalan number. This counts
    k^n ordered sequences times C_{n-1} bracketings each.

    Args:
        generators: list of generator name strings
        max_weight: maximum weight to verify (inclusive)

    Returns:
        dict mapping weight -> {'count': int, 'expected': int, 'pass': bool}
    """
    k = len(generators)
    results = {}

    for weight in range(1, max_weight + 1):
        trees = enumerate_tree_monomials(generators, weight)
        count = len(trees)
        expected = k ** weight * catalan(weight - 1)
        results[weight] = {
            'count': count,
            'expected': expected,
            'pass': count == expected,
        }

    return results
