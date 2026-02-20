# Appendix G — Quick-Start: Running the Code

## Prerequisites

- Python 3.9+
- numpy >= 1.20

## Installation

```bash
git clone <repo-url>
cd oct-lie-redee
pip install -e .
```

The `-e` flag installs in editable mode so source edits take effect immediately.

## Verify All Mathematical Claims

```bash
pytest
```

Every test file maps one-to-one with a specific claim in the text. A passing
suite means every numerical assertion in the book is computationally confirmed.
Run `pytest -v` for the full list of claim-to-test correspondences.

## Run the Demonstrations

```bash
python -m octonion_algebra.demo
```

Four self-contained benchmarks run in sequence:

1. **Gaming detection** — shows that an agent manipulating alignment scores
   cannot hide the associator signature; maps to Ch 26.
2. **Turbulence source** — locates the origin of a 7-dimensional vortex field
   by tracking associator zeros; maps to Ch 32.
3. **Portfolio context** — prices a synthetic derivative using octonionic
   coherence rather than scalar volatility; maps to Ch 37.
4. **COPBW completeness** — exhaustively verifies the Coherence-Ordered
   Partition of Binary Words theorem for word lengths 1–8; maps to Ch 22.

## Quick Python Example

```python
from octonion_algebra.core import e1, e2, e4
from octonion_algebra.associator import associator

# The associator measures non-associativity
a = associator(e1, e2, e4)
print(a)        # nonzero — octonions are non-associative
print(a.norm()) # = 2.0
```

The associator `[a, b, c] = (ab)c - a(bc)` is identically zero in any
associative algebra. Its nonzero value here encodes the hierarchical context
information that is the central object of study throughout the book.

## Package Structure

| Module          | Book chapters | Content                        |
|-----------------|---------------|--------------------------------|
| `core.py`       | Ch 2–4        | Octonion arithmetic, basis elements, norm |
| `associator.py` | Ch 5          | The associator and its properties |
| `g2.py`         | Ch 9–10       | G₂ automorphisms and structure constants |
| `coherence.py`  | Ch 15–16      | Coherence conservation laws    |
| `alignment.py`  | Ch 26         | Non-gameable alignment metrics |
| `fluids.py`     | Ch 32         | 7D vorticity and turbulence    |
| `finance.py`    | Ch 37         | Octonionic finance             |
| `copbw.py`      | Ch 22         | COPBW theorem                  |

## Appendix C Cross-Reference

Appendix C contains the full annotated source with mathematical derivations
inline — every function is accompanied by the equation it implements and a
citation to the relevant theorem. The modules listed above are that same code
extracted into importable, testable form. If a derivation is unclear, Appendix C
is the first place to look.
