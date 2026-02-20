import pytest
import numpy as np
from octonion_algebra.core import Octonion, e0, e1, e2, e3, e4, e5, e6, e7, oct, FANO_TRIPLES


@pytest.fixture
def basis_elements():
    return [e0, e1, e2, e3, e4, e5, e6, e7]


@pytest.fixture
def imaginary_basis():
    return [e1, e2, e3, e4, e5, e6, e7]


@pytest.fixture
def random_octonions():
    return [Octonion.random(seed=i) for i in range(5)]
