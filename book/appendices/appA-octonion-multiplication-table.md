> **Rigor Level: EXPOSITORY** — Complete reference tables, verified against the canonical Fano convention.
> **Novelty: EXPOSITORY** — Standard reference material; no new results claimed.

# Appendix A: Octonion Multiplication Table and Fano Plane Reference

## A.1 The Octonion Algebra: Complete Specification

The octonions $\mathbb{O}$ form an 8-dimensional normed division algebra over $\mathbb{R}$ with basis:

$$\{1, e_1, e_2, e_3, e_4, e_5, e_6, e_7\}$$

where $1$ is the real unit and $e_1, \ldots, e_7$ are the imaginary units. A general octonion is:

$$x = x_0 + x_1 e_1 + x_2 e_2 + x_3 e_3 + x_4 e_4 + x_5 e_5 + x_6 e_6 + x_7 e_7, \quad x_i \in \mathbb{R}.$$

We write $\text{Re}(x) = x_0$ and $\text{Im}(x) = x - x_0 = \sum_{i=1}^{7} x_i e_i$.

## A.2 The Fano Plane

The multiplication of imaginary octonion units is governed by the **Fano plane** $\mathbb{F}_2 P^2$, the smallest finite projective plane. It has:

- **7 points:** corresponding to the 7 imaginary units $e_1, e_2, \ldots, e_7$.
- **7 lines:** each containing exactly 3 points. Each line is a directed cycle.

### A.2.1 The Seven Lines (Standard Convention)

We use the convention where the 7 oriented lines (directed triples) are:

| Line | Triple (oriented) | Rule |
|------|-------------------|------|
| $L_1$ | $(e_1, e_2, e_3)$ | $e_1 e_2 = e_3$ |
| $L_2$ | $(e_1, e_4, e_5)$ | $e_1 e_4 = e_5$ |
| $L_3$ | $(e_2, e_4, e_6)$ | $e_2 e_4 = e_6$ |
| $L_4$ | $(e_3, e_4, e_7)$ | $e_3 e_4 = e_7$ |
| $L_5$ | $(e_1, e_7, e_6)$ | $e_1 e_7 = e_6$ |
| $L_6$ | $(e_2, e_5, e_7)$ | $e_2 e_5 = e_7$ |
| $L_7$ | $(e_3, e_6, e_5)$ | $e_3 e_6 = e_5$ |

**Orientation rule:** If $(e_i, e_j, e_k)$ is an oriented triple on a Fano line, then:
- $e_i e_j = +e_k$ (following the orientation)
- $e_j e_i = -e_k$ (against the orientation)
- $e_j e_k = +e_i$ (cyclic)
- $e_k e_j = -e_i$ (anticyclic)
- $e_k e_i = +e_j$ (cyclic)
- $e_i e_k = -e_j$ (anticyclic)

### A.2.2 Text Description of the Fano Plane Diagram

The Fano plane can be visualized as follows:

```
            e_1
           / | \
          /  |  \
         /   |   \
       e_3---e_7---e_5
       / \   |   / \
      /   \  |  /   \
     /     \ | /     \
   e_4------e_6------e_2
```

The 7 lines consist of:
1. The three sides of the outer triangle: $(e_1, e_2, e_3)$, $(e_1, e_4, e_5)$, and $(e_2, e_4, e_6)$.
2. The three altitudes/medians: $(e_3, e_4, e_7)$, $(e_1, e_7, e_6)$, $(e_2, e_5, e_7)$.
3. The inscribed circle: $(e_3, e_6, e_5)$.

Each point lies on exactly 3 lines. Each line contains exactly 3 points. Any two distinct points determine a unique line. Any two distinct lines intersect in a unique point.

### A.2.3 Index Notation for Fano Triples

An equivalent specification uses the set of **index cycles**. Define:

$$\mathcal{C} = \{(1,2,3),\; (1,4,5),\; (2,4,6),\; (3,4,7),\; (1,7,6),\; (2,5,7),\; (3,6,5)\}$$

For any cyclic permutation $(i,j,k)$ of a triple in $\mathcal{C}$:
$$e_i e_j = e_k, \quad e_j e_i = -e_k.$$

This is all the information needed to compute any product $e_i e_j$.

### A.2.4 Mnemonic: The "Quadratic Residue" Pattern

The 7 triples can be generated from the base triple $(1,2,4)$ by the rule:

$$(1,2,4) \to (2,3,5) \to (3,4,6) \to (4,5,7) \to (5,6,1) \to (6,7,2) \to (7,1,3)$$

This is obtained by adding 1 modulo 7 to each index. The resulting oriented triples are:

$(1,2,4)$, $(2,3,5)$, $(3,4,6)$, $(4,5,7)$, $(5,6,1)$, $(6,7,2)$, $(7,1,3)$

which, rewritten in our standard convention (cycling within each triple as needed), reproduce the Fano lines. However, note that this "mod 7" convention yields a different but isomorphic multiplication table. In our standard convention, the triples are as listed in Section A.2.1.

## A.3 The Complete 8x8 Multiplication Table

The following table gives the product $e_i \cdot e_j$ for all pairs of basis elements, where we write $e_0 = 1$ for the real unit.

### A.3.1 Products of Unit with Imaginary Units

For all $i \in \{1, \ldots, 7\}$:

$$1 \cdot e_i = e_i \cdot 1 = e_i$$

$$1 \cdot 1 = 1$$

### A.3.2 Products of Imaginary Units with Themselves

For all $i \in \{1, \ldots, 7\}$:

$$e_i \cdot e_i = -1$$

### A.3.3 Full Multiplication Table

|  $\times$  | $1$ | $e_1$ | $e_2$ | $e_3$ | $e_4$ | $e_5$ | $e_6$ | $e_7$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | $1$ | $e_1$ | $e_2$ | $e_3$ | $e_4$ | $e_5$ | $e_6$ | $e_7$ |
| $e_1$ | $e_1$ | $-1$ | $e_3$ | $-e_2$ | $e_5$ | $-e_4$ | $-e_7$ | $e_6$ |
| $e_2$ | $e_2$ | $-e_3$ | $-1$ | $e_1$ | $e_6$ | $e_7$ | $-e_4$ | $-e_5$ |
| $e_3$ | $e_3$ | $e_2$ | $-e_1$ | $-1$ | $e_7$ | $-e_6$ | $e_5$ | $-e_4$ |
| $e_4$ | $e_4$ | $-e_5$ | $-e_6$ | $-e_7$ | $-1$ | $e_1$ | $e_2$ | $e_3$ |
| $e_5$ | $e_5$ | $e_4$ | $-e_7$ | $e_6$ | $-e_1$ | $-1$ | $-e_3$ | $e_2$ |
| $e_6$ | $e_6$ | $e_7$ | $e_4$ | $-e_5$ | $-e_2$ | $e_3$ | $-1$ | $-e_1$ |
| $e_7$ | $e_7$ | $-e_6$ | $e_5$ | $e_4$ | $-e_3$ | $-e_2$ | $e_1$ | $-1$ |

### A.3.4 Verification Principle

The table is completely antisymmetric for imaginary units: $e_i e_j = -e_j e_i$ for $i \neq j$, $i,j \geq 1$. This means for any pair of distinct imaginary units, only the upper-triangular entries need be remembered; the lower-triangular entries have opposite sign.

### A.3.5 Structure Constants $f_{ijk}$

Define the **totally antisymmetric structure constants** $f_{ijk}$ for $i,j,k \in \{1, \ldots, 7\}$ by:

$$e_i e_j = -\delta_{ij} + \sum_{k=1}^{7} f_{ijk} e_k$$

The nonzero values of $f_{ijk}$ are:

| $(i,j,k)$ | $f_{ijk}$ |
|:---:|:---:|
| $(1,2,3)$ | $+1$ |
| $(1,4,5)$ | $+1$ |
| $(2,4,6)$ | $+1$ |
| $(3,4,7)$ | $+1$ |
| $(1,7,6)$ | $+1$ |
| $(2,5,7)$ | $+1$ |
| $(3,6,5)$ | $+1$ |

and all even permutations of these triples also have $f = +1$, while odd permutations have $f = -1$. All other index triples give $f_{ijk} = 0$.

Explicitly, $f_{ijk} = +1$ for the 21 even permutations of the 7 triples:

$(1,2,3), (2,3,1), (3,1,2)$
$(1,4,5), (4,5,1), (5,1,4)$
$(2,4,6), (4,6,2), (6,2,4)$
$(3,4,7), (4,7,3), (7,3,4)$
$(1,7,6), (7,6,1), (6,1,7)$
$(2,5,7), (5,7,2), (7,2,5)$
$(3,6,5), (6,5,3), (5,3,6)$

And $f_{ijk} = -1$ for the 21 odd permutations (swap any two indices in the above).

The remaining $7^3 - 42 = 301$ index triples have $f_{ijk} = 0$ (including all triples with repeated indices).

### A.3.6 The Dual Structure Constants $\tilde{f}_{ijkl}$

The **associator structure** is encoded by the 4-index tensor. For basis elements:

$$[e_i, e_j, e_k] = (e_i e_j) e_k - e_i(e_j e_k) = \sum_l \tilde{f}_{ijkl} e_l$$

This tensor is completely antisymmetric in all four indices and takes the value $\pm 2$ on the complementary quadruples to the Fano triples. Specifically, if $(i,j,k)$ is a Fano triple, then the complementary set $\{1,\ldots,7\} \setminus \{i,j,k\}$ contains exactly four indices, and these form the support of the associator.

## A.4 The Seven Quaternionic Subalgebras

Each of the 7 lines in the Fano plane determines a **quaternionic subalgebra** of $\mathbb{O}$. This subalgebra is isomorphic to $\mathbb{H}$ and is generated by any two of the three imaginary units on that line.

### A.4.1 Complete List

| Subalgebra | Generators | Basis | Multiplication |
|:---:|:---:|:---:|:---:|
| $\mathbb{H}_1$ | $e_1, e_2$ | $\{1, e_1, e_2, e_3\}$ | $e_1 e_2 = e_3,\; e_2 e_3 = e_1,\; e_3 e_1 = e_2$ |
| $\mathbb{H}_2$ | $e_1, e_4$ | $\{1, e_1, e_4, e_5\}$ | $e_1 e_4 = e_5,\; e_4 e_5 = e_1,\; e_5 e_1 = e_4$ |
| $\mathbb{H}_3$ | $e_2, e_4$ | $\{1, e_2, e_4, e_6\}$ | $e_2 e_4 = e_6,\; e_4 e_6 = e_2,\; e_6 e_2 = e_4$ |
| $\mathbb{H}_4$ | $e_3, e_4$ | $\{1, e_3, e_4, e_7\}$ | $e_3 e_4 = e_7,\; e_4 e_7 = e_3,\; e_7 e_3 = e_4$ |
| $\mathbb{H}_5$ | $e_1, e_7$ | $\{1, e_1, e_7, e_6\}$ | $e_1 e_7 = e_6,\; e_7 e_6 = e_1,\; e_6 e_1 = e_7$ |
| $\mathbb{H}_6$ | $e_2, e_5$ | $\{1, e_2, e_5, e_7\}$ | $e_2 e_5 = e_7,\; e_5 e_7 = e_2,\; e_7 e_2 = e_5$ |
| $\mathbb{H}_7$ | $e_3, e_6$ | $\{1, e_3, e_6, e_5\}$ | $e_3 e_6 = e_5,\; e_6 e_5 = e_3,\; e_5 e_3 = e_6$ |

### A.4.2 Properties of the Quaternionic Subalgebras

1. Each $\mathbb{H}_i$ is a closed, associative subalgebra isomorphic to $\mathbb{H}$.
2. Any two imaginary units that lie on the same Fano line generate a copy of $\mathbb{H}$.
3. Any two imaginary units that do NOT lie on the same Fano line generate all of $\mathbb{O}$.
4. The intersection of any two distinct quaternionic subalgebras $\mathbb{H}_i \cap \mathbb{H}_j$ is a copy of $\mathbb{C}$ (a 2-dimensional subalgebra $\{1, e_k\}$ for the shared imaginary unit) or just $\mathbb{R} = \{1\}$ if they share no imaginary unit.
5. Each imaginary unit $e_i$ appears in exactly 3 of the 7 quaternionic subalgebras (since each point of the Fano plane lies on exactly 3 lines).

### A.4.3 The 3D Recovery via Quaternionic Slice

To recover classical 3D vector calculus from the octonionic framework, choose any one quaternionic subalgebra $\mathbb{H}_i$ and restrict all operations to it. Since $\text{Im}(\mathbb{H}_i) \cong \mathbb{R}^3$, and the restricted cross product is the standard 3D cross product, all classical formulas (curl, divergence, gradient in 3D, angular momentum, Lorentz force, etc.) are recovered. See Chapter 15.

## A.5 The 480 Multiplication Tables

### A.5.1 Source of Non-Uniqueness

The multiplication table for $\mathbb{O}$ is not unique. Different choices of:

1. **Basis labeling:** Permutations of the indices $\{1, \ldots, 7\}$ (there are $7! = 5040$ such permutations).
2. **Sign choices:** For each Fano line, one can reverse the orientation (changing $e_i e_j = +e_k$ to $e_i e_j = -e_k$), which flips the sign of the structure constants on that line.

yield different but isomorphic multiplication tables.

### A.5.2 Counting the 480 Tables

The group of symmetries of the Fano plane is $\text{GL}(3, \mathbb{F}_2) \cong \text{PSL}(2,7)$, which has order 168. This group acts on the 7 points and preserves the incidence structure (which triples of points are collinear).

The full symmetry group acting on multiplication tables consists of:
- The 168 automorphisms of the Fano plane (permutations preserving lines).
- For each automorphism, a choice of orientation for each of the 7 lines. However, not all $2^7 = 128$ sign choices are independent: flipping all 7 signs gives an isomorphic algebra (equivalent to $x \mapsto \bar{x}$), so there are effectively $2^7 / 2 = 64$ distinct sign patterns.

But we must count more carefully. The number of distinct octonion multiplication tables is:

$$\frac{7! \times 2^7}{|\text{Aut}(\mathbb{O}) \ltimes \text{sign symmetries}|} = 480$$

More precisely: there are $7! = 5040$ ways to label the 7 imaginary units. For each labeling, there are $2^7 = 128$ possible sign assignments to the 7 Fano triples (each line can be oriented in two ways), but the constraint that the table must define an alternative algebra reduces this. The result is that exactly **480** distinct multiplication tables exist, falling into a single orbit under the action of $G_2$ (the automorphism group of $\mathbb{O}$, which has order related to these symmetries through its action on the 7 imaginary directions).

### A.5.3 Equivalence Classes

All 480 tables are related by:

1. **$G_2$ transformations:** The 14-dimensional Lie group $G_2 = \text{Aut}(\mathbb{O})$ acts on $\text{Im}(\mathbb{O})$ as a subgroup of $\text{SO}(7)$. Two multiplication tables are equivalent if and only if they are related by a $G_2$ rotation of the imaginary units.

2. **Sign flips:** Replacing any $e_i \to -e_i$ changes the signs of all products involving $e_i$. This corresponds to an automorphism of the octonion algebra if and only if the transformation is in $G_2$.

3. **Index permutations preserving the Fano structure:** The 168 automorphisms of the Fano plane, combined with orientation choices.

The key fact is: **all 480 multiplication tables define isomorphic algebras.** There is exactly one octonion algebra up to isomorphism. The choice of table is a choice of basis, analogous to choosing coordinate axes.

### A.5.4 The Standard Table vs. Common Alternatives

Our standard table (Section A.3.3) uses the triples:

$(1,2,3), (1,4,5), (2,4,6), (3,4,7), (1,7,6), (2,5,7), (3,6,5)$

Another common convention (used by Baez, Cartan-Schouten) uses:

$(1,2,4), (2,3,5), (3,4,6), (4,5,7), (5,6,1), (6,7,2), (7,1,3)$

These are related by the index permutation and are both valid.

A third common convention (used in some physics literature) is:

$(1,2,3), (1,4,5), (1,7,6), (2,4,6), (2,5,7), (3,5,6), (3,7,4)$

All three define the same algebra.

## A.6 Conjugation, Norm, and Inverse

### A.6.1 Conjugation

For $x = x_0 + \sum_{i=1}^{7} x_i e_i$, the **conjugate** is:

$$\bar{x} = x_0 - \sum_{i=1}^{7} x_i e_i$$

Properties:
- $\bar{\bar{x}} = x$ (involutory)
- $\overline{x + y} = \bar{x} + \bar{y}$ (linear)
- $\overline{xy} = \bar{y}\bar{x}$ (anti-homomorphism — note the reversal of order)
- $\overline{\lambda x} = \lambda \bar{x}$ for $\lambda \in \mathbb{R}$
- $x + \bar{x} = 2x_0 = 2\text{Re}(x) \in \mathbb{R}$
- $x - \bar{x} = 2\text{Im}(x)$
- $x\bar{x} = \bar{x}x = |x|^2 \in \mathbb{R}_{\geq 0}$ (this is real and non-negative)

### A.6.2 Norm

The **norm** (or modulus) is:

$$|x| = \sqrt{x\bar{x}} = \sqrt{\sum_{i=0}^{7} x_i^2}$$

This is the standard Euclidean norm on $\mathbb{R}^8$.

The **squared norm** is:

$$|x|^2 = N(x) = x\bar{x} = x_0^2 + x_1^2 + x_2^2 + x_3^2 + x_4^2 + x_5^2 + x_6^2 + x_7^2$$

**Multiplicativity:** $|xy| = |x| \cdot |y|$ for all $x, y \in \mathbb{O}$. This is the defining property of a composition algebra.

**Inner product:** For $x, y \in \mathbb{O}$:

$$\langle x, y \rangle = \text{Re}(x\bar{y}) = \text{Re}(\bar{x}y) = \sum_{i=0}^{7} x_i y_i$$

This is the standard Euclidean inner product on $\mathbb{R}^8$.

### A.6.3 Inverse

For any nonzero $x \in \mathbb{O}$, the **inverse** is:

$$x^{-1} = \frac{\bar{x}}{|x|^2}$$

Verification:

$$x \cdot x^{-1} = x \cdot \frac{\bar{x}}{|x|^2} = \frac{x\bar{x}}{|x|^2} = \frac{|x|^2}{|x|^2} = 1$$

$$x^{-1} \cdot x = \frac{\bar{x}}{|x|^2} \cdot x = \frac{\bar{x}x}{|x|^2} = \frac{|x|^2}{|x|^2} = 1$$

**Warning:** Because $\mathbb{O}$ is non-associative, $x^{-1}(xy) = y$ and $(yx)x^{-1} = y$ do hold (by alternativity), but in general $(xy)z^{-1} \neq x(yz^{-1})$.

### A.6.4 The Real Part, Imaginary Part, and Trace

$$\text{Re}(x) = \frac{x + \bar{x}}{2} = x_0$$

$$\text{Im}(x) = \frac{x - \bar{x}}{2} = \sum_{i=1}^{7} x_i e_i$$

The **trace** of $x$ is $\text{Tr}(x) = 2\text{Re}(x) = x + \bar{x}$.

## A.7 Worked Examples

### A.7.1 Example: Basic Multiplication

Let $a = 2 + 3e_1 - e_3$ and $b = 1 + e_2 + 2e_5$.

We compute $ab$ by expanding bilinearly:

$$ab = (2)(1) + (2)(e_2) + (2)(2e_5) + (3e_1)(1) + (3e_1)(e_2) + (3e_1)(2e_5) + (-e_3)(1) + (-e_3)(e_2) + (-e_3)(2e_5)$$

Now evaluate each term using the multiplication table:

| Term | Computation | Result |
|:---:|:---:|:---:|
| $(2)(1)$ | $= 2$ | $2$ |
| $(2)(e_2)$ | $= 2e_2$ | $2e_2$ |
| $(2)(2e_5)$ | $= 4e_5$ | $4e_5$ |
| $(3e_1)(1)$ | $= 3e_1$ | $3e_1$ |
| $(3e_1)(e_2)$ | $= 3(e_1 e_2) = 3e_3$ | $3e_3$ |
| $(3e_1)(2e_5)$ | $= 6(e_1 e_5)$ | Need: $e_1 e_5 = ?$ |
| $(-e_3)(1)$ | $= -e_3$ | $-e_3$ |
| $(-e_3)(e_2)$ | $= -(e_3 e_2)$ | Need: $e_3 e_2 = ?$ |
| $(-e_3)(2e_5)$ | $= -2(e_3 e_5)$ | Need: $e_3 e_5 = ?$ |

Looking up from the table:
- $e_1 e_5 = -e_4$ (from Fano triple $(1,4,5)$: $e_1 e_4 = e_5$, so $e_1 e_5 = -e_4$ by cycling and sign)
- $e_3 e_2 = -e_1$ (from Fano triple $(1,2,3)$: $e_1 e_2 = e_3$, so $e_3 e_2 = -(e_2 e_3) = -e_1$... let us be careful. From the triple $(1,2,3)$: $e_2 e_3 = e_1$, so $e_3 e_2 = -e_1$.)
- $e_3 e_5 = -e_6$ (from Fano triple $(3,6,5)$: $e_3 e_6 = e_5$, so $e_3 e_5 = -(e_5 e_3)$... more carefully: from $(3,6,5)$, $e_5 e_3 = e_6$, hence $e_3 e_5 = -e_6$.)

Continuing:

| Term | Result |
|:---:|:---:|
| $(3e_1)(2e_5)$ | $6(-e_4) = -6e_4$ |
| $(-e_3)(e_2)$ | $-(-e_1) = e_1$ |
| $(-e_3)(2e_5)$ | $-2(-e_6) = 2e_6$ |

Collecting all terms:

$$ab = 2 + (3+1)e_1 + 2e_2 + (3-1)e_3 + (-6)e_4 + 4e_5 + 2e_6$$

$$\boxed{ab = 2 + 4e_1 + 2e_2 + 2e_3 - 6e_4 + 4e_5 + 2e_6}$$

### A.7.2 Example: Conjugation

For $x = 3 + e_1 - 2e_4 + 5e_7$:

$$\bar{x} = 3 - e_1 + 2e_4 - 5e_7$$

### A.7.3 Example: Norm Computation

For $x = 3 + e_1 - 2e_4 + 5e_7$:

$$|x|^2 = 3^2 + 1^2 + 0^2 + 0^2 + (-2)^2 + 0^2 + 0^2 + 5^2 = 9 + 1 + 4 + 25 = 39$$

$$|x| = \sqrt{39}$$

### A.7.4 Example: Inverse Computation

For $x = 3 + e_1 - 2e_4 + 5e_7$ with $|x|^2 = 39$:

$$x^{-1} = \frac{\bar{x}}{|x|^2} = \frac{3 - e_1 + 2e_4 - 5e_7}{39} = \frac{3}{39} - \frac{1}{39}e_1 + \frac{2}{39}e_4 - \frac{5}{39}e_7$$

Verification: $x \cdot x^{-1} = x\bar{x}/|x|^2 = |x|^2/|x|^2 = 1$. $\checkmark$

### A.7.5 Example: Norm Multiplicativity

Let $a = e_1 + e_2$ and $b = e_3 + e_4$.

$|a|^2 = 1 + 1 = 2$, $|b|^2 = 1 + 1 = 2$.

$ab = e_1 e_3 + e_1 e_4 + e_2 e_3 + e_2 e_4$

From the table:
- $e_1 e_3 = -e_2$ (from $(1,2,3)$: $e_1 e_2 = e_3$, so $e_3 e_1 = e_2$ and $e_1 e_3 = -e_2$)
- $e_1 e_4 = e_5$ (from $(1,4,5)$)
- $e_2 e_3 = e_1$ (from $(1,2,3)$: $e_2 e_3 = e_1$)
- $e_2 e_4 = e_6$ (from $(2,4,6)$)

So $ab = -e_2 + e_5 + e_1 + e_6 = e_1 - e_2 + e_5 + e_6$.

$|ab|^2 = 1 + 1 + 1 + 1 = 4 = 2 \times 2 = |a|^2 |b|^2$. $\checkmark$

### A.7.6 Example: Demonstrating Non-Associativity

Let $a = e_1$, $b = e_2$, $c = e_4$.

$(ab)c = (e_1 e_2)e_4 = e_3 e_4 = e_7$

$a(bc) = e_1(e_2 e_4) = e_1 e_6$

From the table: $e_1 e_6 = ?$. From the Fano triple $(1,7,6)$: $e_1 e_7 = e_6$, so $e_6 e_1 = e_7$ and $e_1 e_6 = -e_7$.

Therefore:

$$(e_1 e_2)e_4 = e_7, \quad e_1(e_2 e_4) = -e_7$$

The **associator** is:

$$[e_1, e_2, e_4] = (e_1 e_2)e_4 - e_1(e_2 e_4) = e_7 - (-e_7) = 2e_7$$

This is nonzero, confirming non-associativity.

### A.7.7 Example: Verifying the Conjugation Anti-Homomorphism

Let $x = 1 + e_1$ and $y = 1 + e_2$.

$xy = (1)(1) + (1)(e_2) + (e_1)(1) + e_1 e_2 = 1 + e_2 + e_1 + e_3$

$\overline{xy} = 1 - e_1 - e_2 - e_3$

Now: $\bar{y} = 1 - e_2$, $\bar{x} = 1 - e_1$.

$\bar{y}\bar{x} = (1)(1) + (1)(-e_1) + (-e_2)(1) + (-e_2)(-e_1) = 1 - e_1 - e_2 + e_2 e_1$

$e_2 e_1 = -e_1 e_2 = -e_3$

$\bar{y}\bar{x} = 1 - e_1 - e_2 - e_3 = \overline{xy}$. $\checkmark$

## A.8 The Octonion Product Formula

For general octonions $x = x_0 + \vec{x}$ and $y = y_0 + \vec{y}$ where $\vec{x}, \vec{y} \in \text{Im}(\mathbb{O})$:

$$xy = (x_0 y_0 - \vec{x} \cdot \vec{y}) + (x_0 \vec{y} + y_0 \vec{x} + \vec{x} \times \vec{y})$$

where:
- $\vec{x} \cdot \vec{y} = \sum_{i=1}^{7} x_i y_i$ is the standard inner product on $\mathbb{R}^7$.
- $\vec{x} \times \vec{y}$ is the **7-dimensional cross product** with components:

$$(\vec{x} \times \vec{y})_k = \sum_{i,j=1}^{7} f_{ijk} x_i y_j$$

where $f_{ijk}$ are the structure constants from Section A.3.5.

This formula is the direct generalization of the quaternion product formula (Section 1.3.3 of Chapter 1) to 7 dimensions.

## A.9 Moufang Identities and Alternativity

The octonions satisfy the following identities, which serve as partial substitutes for full associativity:

**Alternative laws:**
- **Left alternative:** $(xx)y = x(xy)$ for all $x, y \in \mathbb{O}$.
- **Right alternative:** $(yx)x = y(xx)$ for all $x, y \in \mathbb{O}$.
- **Flexible identity:** $(xy)x = x(yx)$ for all $x, y \in \mathbb{O}$.

**Moufang identities:** For all $x, y, z \in \mathbb{O}$:

1. $((xy)z)y = x(y(zy))$
2. $(x(yz))x = (xy)(zx)$
3. $((xy)x)z = x(y(xz))$

**Artin's Theorem:** Any subalgebra of $\mathbb{O}$ generated by two elements is associative (and hence isomorphic to $\mathbb{R}$, $\mathbb{C}$, or $\mathbb{H}$).

**Consequence:** The associator $[a,b,c]$ vanishes whenever any two of the three arguments are equal, or whenever all three lie in the same quaternionic subalgebra.

## A.10 Quick Reference Card

For rapid computation, the essential data:

**Fano triples (oriented):** $(1,2,3)$, $(1,4,5)$, $(2,4,6)$, $(3,4,7)$, $(1,7,6)$, $(2,5,7)$, $(3,6,5)$.

**Rule:** If $(i,j,k)$ is an even (cyclic) permutation of a Fano triple: $e_i e_j = +e_k$.
If $(i,j,k)$ is an odd permutation: $e_i e_j = -e_k$.
If $i = j$: $e_i e_j = -1$.
If $\{i,j\}$ does not appear in any triple: this cannot happen (every pair of distinct indices appears in exactly one triple).

**Conjugate:** Negate all imaginary parts.
**Norm squared:** Sum of squares of all 8 components.
**Inverse:** Conjugate divided by norm squared.
**Product formula:** $(x_0 + \vec{x})(y_0 + \vec{y}) = (x_0 y_0 - \vec{x}\cdot\vec{y}) + (x_0\vec{y} + y_0\vec{x} + \vec{x}\times_7\vec{y})$.

---

*This appendix provides all data needed to compute any octonion expression. For computational implementations, see Appendix C.*
