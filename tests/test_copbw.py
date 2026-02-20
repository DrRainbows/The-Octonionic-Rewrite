"""Tests for the COPBW basis construction module."""
import numpy as np
import pytest

from octonion_algebra.core import Octonion, e1, e2, e3
from octonion_algebra.copbw import (
    catalan,
    TreeMonomial,
    leaf,
    mul,
    enumerate_tree_monomials,
    verify_basis_count,
    copbw_basis,
)


def test_catalan_values():
    """catalan(n) returns correct values for small n."""
    assert catalan(0) == 1, f"C(0) should be 1, got {catalan(0)}"
    assert catalan(1) == 1, f"C(1) should be 1, got {catalan(1)}"
    assert catalan(2) == 2, f"C(2) should be 2, got {catalan(2)}"
    assert catalan(3) == 5, f"C(3) should be 5, got {catalan(3)}"
    assert catalan(4) == 14, f"C(4) should be 14, got {catalan(4)}"


def test_tree_monomial_leaf():
    """leaf("x") evaluates to x given an assignment."""
    x_val = Octonion.random(seed=42)
    t = leaf("x")

    assert t.is_leaf
    assert t.label == "x"
    assert t.size() == 1
    assert t.depth() == 0

    result = t.evaluate({"x": x_val})
    np.testing.assert_allclose(
        result.coeffs, x_val.coeffs, atol=1e-15,
        err_msg="Leaf evaluation should return the assigned value"
    )


def test_tree_monomial_product():
    """mul(leaf, leaf) evaluates correctly as octonion product."""
    a_val = e1
    b_val = e2

    t = mul(leaf("a"), leaf("b"))

    assert not t.is_leaf
    assert t.size() == 2
    assert t.depth() == 1

    result = t.evaluate({"a": a_val, "b": b_val})
    expected = a_val * b_val  # e1 * e2 = e3

    np.testing.assert_allclose(
        result.coeffs, expected.coeffs, atol=1e-15,
        err_msg="Product tree should evaluate to octonion product"
    )


def test_enumerate_degree_2():
    """Correct count for 2 generators at degree 2.

    For degree 2 with k generators, we have k^2 ordered pairs times
    C_1 = 1 tree shape = k^2 monomials.
    """
    generators = ["a", "b"]
    trees = enumerate_tree_monomials(generators, degree=2)

    # k=2, degree=2: k^2 * C_1 = 4 * 1 = 4
    expected_count = 2**2 * catalan(1)
    assert len(trees) == expected_count, (
        f"Expected {expected_count} tree monomials for 2 generators degree 2, "
        f"got {len(trees)}"
    )

    # Each should be a product of two leaves
    for t in trees:
        assert not t.is_leaf
        assert t.size() == 2


def test_basis_count_matches_catalan():
    """verify_basis_count returns True for small cases.

    For weight n with k generators, the count should be k^n * C_{n-1}.
    """
    generators = ["x", "y"]
    results = verify_basis_count(generators, max_weight=4)

    for weight, info in results.items():
        assert info['pass'], (
            f"Weight {weight}: count={info['count']}, expected={info['expected']}"
        )


def test_copbw_basis_structure():
    """copbw_basis returns dict with correct keys (degree -> list of trees)."""
    generators = ["a", "b"]
    max_degree = 3
    basis = copbw_basis(generators, max_degree=max_degree)

    assert isinstance(basis, dict), f"copbw_basis should return dict, got {type(basis)}"

    for d in range(1, max_degree + 1):
        assert d in basis, f"Degree {d} missing from basis dict"
        assert isinstance(basis[d], list), f"basis[{d}] should be a list"
        assert len(basis[d]) > 0, f"basis[{d}] should not be empty"

        # Each element should be a TreeMonomial
        for t in basis[d]:
            assert isinstance(t, TreeMonomial), (
                f"Element in basis[{d}] should be TreeMonomial, got {type(t)}"
            )
            assert t.size() == d, (
                f"Tree in basis[{d}] should have size {d}, got {t.size()}"
            )

    # Verify counts match: degree d should have k^d * C_{d-1} trees
    k = len(generators)
    assert len(basis[1]) == k  # 2 leaves
    assert len(basis[2]) == k**2 * catalan(1)  # 4
    assert len(basis[3]) == k**3 * catalan(2)  # 16
