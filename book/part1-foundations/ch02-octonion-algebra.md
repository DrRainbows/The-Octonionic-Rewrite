> **Rigor Level: EXPOSITORY** — Accurate exposition of established octonion algebra with complete multiplication tables and Fano plane construction.
> **Novelty: EXPOSITORY** — Synthesizes known results; no new theorems claimed.

# Chapter 2: The Octonion Algebra

## 2.1 Introduction

This chapter constructs the octonion algebra $\mathbb{O}$ in full detail, providing every tool needed for explicit computation. We give the Cayley-Dickson construction from the ground up, derive the complete multiplication table, present the Fano plane mnemonic, and establish the fundamental algebraic operations: conjugation, norm, inverse, and the decomposition into real and imaginary parts.

An AI reader — or any reader — who completes this chapter will be able to multiply any two octonions by hand, verify identities, and perform the computations that underlie all subsequent chapters.

## 2.2 The Cayley-Dickson Construction

### 2.2.1 General Framework

**Definition 2.2.1.** Let $A$ be a $*$-algebra over $\mathbb{R}$ (a real algebra with involution $a \mapsto \bar{a}$ satisfying $\overline{ab} = \bar{b}\bar{a}$ and $\overline{\bar{a}} = a$). The *Cayley-Dickson double* of $A$ is the algebra $\mathrm{CD}(A)$ whose underlying vector space is $A \oplus A$ and whose multiplication is:

$$(a, b)(c, d) = (ac - \bar{d}b, \; da + b\bar{c})$$

with conjugation $\overline{(a,b)} = (\bar{a}, -b)$ and norm $N(a,b) = N(a) + N(b)$.

**Remark.** Several sign conventions appear in the literature. The one above (following Baez and Conway-Smith) yields the standard octonion multiplication table when iterated. The alternative convention $(a,b)(c,d) = (ac - d\bar{b}, \; \bar{a}d + cb)$ produces an isomorphic algebra.

### 2.2.2 Step 1: $\mathbb{R} \to \mathbb{C}$

Start with $A = \mathbb{R}$, where conjugation is the identity: $\bar{a} = a$.

$$\mathrm{CD}(\mathbb{R}) = \{(a, b) : a, b \in \mathbb{R}\}$$

with $(a,b)(c,d) = (ac - db, da + bc)$. Setting $1 = (1,0)$ and $i = (0,1)$:

$$i^2 = (0,1)(0,1) = (0 \cdot 0 - 1 \cdot 1, 1 \cdot 0 + 1 \cdot 0) = (-1, 0) = -1.$$

This gives $\mathbb{C}$ with the identification $(a,b) \leftrightarrow a + bi$.

### 2.2.3 Step 2: $\mathbb{C} \to \mathbb{H}$

Now $A = \mathbb{C}$ with $\overline{a + bi} = a - bi$.

$$\mathrm{CD}(\mathbb{C}) = \{(z_1, z_2) : z_1, z_2 \in \mathbb{C}\}$$

Setting $j = (0, 1)$ and $k = (0, i)$:

$$j^2 = (0,1)(0,1).$$

With $a = 0, b = 1, c = 0, d = 1$:

$$j^2 = (0 \cdot 0 - \bar{1} \cdot 1, \; 1 \cdot 0 + 1 \cdot \bar{0}) = (0 - 1, 0 + 0) = (-1, 0) = -1.$$

For $ij = (i, 0)(0, 1)$, with $a = i, b = 0, c = 0, d = 1$:

$$ij = (i \cdot 0 - \bar{1} \cdot 0, \; 1 \cdot i + 0 \cdot \bar{0}) = (0, i) = k.$$

And $ji = (0, 1)(i, 0)$ with $a = 0, b = 1, c = i, d = 0$:

$$ji = (0 \cdot i - \bar{0} \cdot 1, \; 0 \cdot 0 + 1 \cdot \overline{i}) = (0 - 0, 0 + 1 \cdot (-i)) = (0, -i) = -k.$$

This confirms $ij = k$ and $ji = -k$, recovering the quaternions.

### 2.2.4 Step 3: $\mathbb{H} \to \mathbb{O}$

Now $A = \mathbb{H}$ with $\overline{a + bi + cj + dk} = a - bi - cj - dk$.

$$\mathbb{O} = \mathrm{CD}(\mathbb{H}) = \{(q_1, q_2) : q_1, q_2 \in \mathbb{H}\}.$$

This is an 8-dimensional algebra over $\mathbb{R}$. Set $\ell = (0, 1)$. Then a general octonion is:

$$x = q_1 + q_2 \ell = (a_0 + a_1 i + a_2 j + a_3 k) + (a_4 + a_5 i + a_6 j + a_7 k)\ell.$$

We identify the 8 basis elements as:

| Basis | Cayley-Dickson form | Standard name |
|-------|---------------------|---------------|
| $1$ | $(1, 0)$ | $1$ |
| $e_1$ | $(i, 0)$ | $i$ in $\mathbb{H}$ part |
| $e_2$ | $(j, 0)$ | $j$ in $\mathbb{H}$ part |
| $e_3$ | $(k, 0)$ | $k$ in $\mathbb{H}$ part |
| $e_4$ | $(0, 1)$ | $\ell$ |
| $e_5$ | $(0, i)$ | $i\ell$ |
| $e_6$ | $(0, j)$ | $j\ell$ |
| $e_7$ | $(0, k)$ | $k\ell$ |

The multiplication rule $(q_1, q_2)(q_3, q_4) = (q_1 q_3 - \bar{q}_4 q_2, \; q_4 q_1 + q_2 \bar{q}_3)$ determines all products.

**Example 2.2.1.** Compute $e_4 e_1 = (0,1)(i,0)$. With $a = 0, b = 1, c = i, d = 0$:

$$(0 \cdot i - \bar{0} \cdot 1, \; 0 \cdot 0 + 1 \cdot \overline{i}) = (0, -i) = -e_5.$$

So $e_4 e_1 = -e_5$, or equivalently $e_1 e_4 = e_5$. This gives us our sign convention.

## 2.3 The Complete Multiplication Table

We now compute every product $e_i e_j$ for $i, j \in \{1, \ldots, 7\}$ using the Cayley-Dickson rule.

The result is the following $7 \times 7$ table (omitting the unit $1$, which satisfies $1 \cdot e_i = e_i \cdot 1 = e_i$ and $e_i^2 = -1$ for all $i$):

$$\begin{array}{c|ccccccc}
\times & e_1 & e_2 & e_3 & e_4 & e_5 & e_6 & e_7 \\
\hline
e_1 & -1   & e_3  & -e_2 & e_5  & -e_4 & -e_7 & e_6 \\
e_2 & -e_3 & -1   & e_1  & e_6  & e_7  & -e_4 & -e_5 \\
e_3 & e_2  & -e_1 & -1   & e_7  & -e_6 & e_5  & -e_4 \\
e_4 & -e_5 & -e_6 & -e_7 & -1   & e_1  & e_2  & e_3 \\
e_5 & e_4  & -e_7 & e_6  & -e_1 & -1   & -e_3 & e_2 \\
e_6 & e_7  & e_4  & -e_5 & -e_2 & e_3  & -1   & -e_1 \\
e_7 & -e_6 & e_5  & e_4  & -e_3 & -e_2 & e_1  & -1
\end{array}$$

**Verification procedure.** Each entry can be verified from the Cayley-Dickson rule. We verify a few critical entries.

**Check: $e_1 e_2 = e_3$.** We have $e_1 = (i, 0)$, $e_2 = (j, 0)$, so:

$$(i, 0)(j, 0) = (i \cdot j - \bar{0} \cdot 0, \; 0 \cdot i + 0 \cdot \bar{j}) = (k, 0) = e_3. \checkmark$$

**Check: $e_1 e_4 = e_5$.** We have $e_1 = (i, 0)$, $e_4 = (0, 1)$:

$$(i, 0)(0, 1) = (i \cdot 0 - \bar{1} \cdot 0, \; 1 \cdot i + 0 \cdot \bar{0}) = (0, i) = e_5. \checkmark$$

**Check: $e_2 e_4 = e_6$.** We have $e_2 = (j, 0)$, $e_4 = (0, 1)$:

$$(j, 0)(0, 1) = (j \cdot 0 - \bar{1} \cdot 0, \; 1 \cdot j + 0 \cdot \bar{0}) = (0, j) = e_6. \checkmark$$

**Check: $e_5 e_6 = -e_3$.** We have $e_5 = (0, i)$, $e_6 = (0, j)$:

$$(0, i)(0, j) = (0 \cdot 0 - \bar{j} \cdot i, \; j \cdot 0 + i \cdot \bar{0}) = (-(-j)(i), 0) = (ji, 0) = (-k, 0) = -e_3. \checkmark$$

**Note on sign convention.** The multiplication table above corresponds to a specific orientation of the Fano plane. Other conventions exist in the literature (Cartan, Conway-Smith, Baez each differ in some signs). All yield isomorphic algebras; what matters is internal consistency. The table given here is self-consistent and matches the Cayley-Dickson construction with the convention stated in Definition 2.2.1.

## 2.4 The Fano Plane

The products among the seven imaginary units can be encoded by the *Fano plane* — the unique projective plane of order 2, denoted $PG(2, \mathbb{F}_2)$.

### 2.4.1 Structure

The Fano plane has:
- **7 points:** $e_1, e_2, e_3, e_4, e_5, e_6, e_7$
- **7 lines:** Each line contains exactly 3 points, each point lies on exactly 3 lines.

The 7 oriented lines (cycles) encoding the multiplication are:

$$(1, 2, 3), \quad (1, 4, 5), \quad (1, 7, 6), \quad (2, 4, 6), \quad (2, 5, 7), \quad (3, 4, 7), \quad (3, 6, 5)$$

**Reading the Fano plane.** Each oriented triple $(i, j, k)$ encodes:

$$e_i e_j = e_k, \quad e_j e_k = e_i, \quad e_k e_i = e_j$$

and the reversed products give negatives:

$$e_j e_i = -e_k, \quad e_k e_j = -e_i, \quad e_i e_k = -e_j.$$

**Example 2.4.1.** From the line $(2, 4, 6)$: $e_2 e_4 = e_6$, $e_4 e_6 = e_2$, $e_6 e_2 = e_4$. And conversely, $e_4 e_2 = -e_6$, $e_6 e_4 = -e_2$, $e_2 e_6 = -e_4$.

### 2.4.2 Visual Description

The Fano plane is typically drawn as a triangle with its three medians and inscribed circle:

```
        e_1
       / | \
      /  |  \
    e_3--e_7--e_5
      \  |  /
       \ | /
        e_4
       / | \
      /  |  \
    e_2--+--e_6
```

More precisely, the standard representation is:
- Vertices of an equilateral triangle: $e_1$ (top), $e_2$ (bottom-left), $e_4$ (bottom-right).
- Midpoints of sides: $e_3$ (left side), $e_5$ (right side), $e_6$ (bottom).
- Center: $e_7$.
- Lines: three sides of the triangle, three medians, and the inscribed circle.

Each line is oriented (has a cyclic direction). The orientation determines the sign of the product.

### 2.4.3 Complete List of Products from the Fano Plane

From the 7 lines, we read off 21 products (each line gives 3 positive products):

| Line | Products |
|------|----------|
| $(1,2,3)$ | $e_1 e_2 = e_3$, $e_2 e_3 = e_1$, $e_3 e_1 = e_2$ |
| $(1,4,5)$ | $e_1 e_4 = e_5$, $e_4 e_5 = e_1$, $e_5 e_1 = e_4$ |
| $(2,4,6)$ | $e_2 e_4 = e_6$, $e_4 e_6 = e_2$, $e_6 e_2 = e_4$ |
| $(3,4,7)$ | $e_3 e_4 = e_7$, $e_4 e_7 = e_3$, $e_7 e_3 = e_4$ |
| $(1, 7, 6)$ | $e_1 e_7 = e_6$, $e_7 e_6 = e_1$, $e_6 e_1 = e_7$ |
| $(2, 5, 7)$ | $e_2 e_5 = e_7$, $e_5 e_7 = e_2$, $e_7 e_2 = e_5$ |
| $(3, 6, 5)$ | $e_3 e_6 = e_5$, $e_6 e_5 = e_3$, $e_5 e_3 = e_6$ |

Note that the last three lines involve the orientation $(1,7,6)$ rather than $(1,6,7)$: from the multiplication table, $e_1 e_7 = e_6$ (not $e_1 e_6 = e_7$), so the cyclic order is $1 \to 7 \to 6$.

The complete list of 7 oriented lines is:

$$(1,2,3), \quad (1,4,5), \quad (2,4,6), \quad (3,4,7), \quad (1,7,6), \quad (2,5,7), \quad (3,6,5)$$

These 7 oriented cycles, together with $e_i^2 = -1$, completely determine the octonion multiplication.

## 2.5 Conjugation, Norm, and Inverse

**Definition 2.5.1 (Conjugation).** For $x = x_0 + \sum_{i=1}^{7} x_i e_i \in \mathbb{O}$:

$$\bar{x} = x_0 - \sum_{i=1}^{7} x_i e_i.$$

**Properties of Conjugation:**

1. $\overline{\bar{x}} = x$ (involution).
2. $\overline{x + y} = \bar{x} + \bar{y}$ (additive).
3. $\overline{xy} = \bar{y}\bar{x}$ (anti-homomorphism).
4. $x + \bar{x} = 2x_0 \in \mathbb{R}$ (real part extraction).
5. $x\bar{x} = \bar{x}x = |x|^2 \in \mathbb{R}_{\geq 0}$ (norm).

**Proof of property 3.** This follows from the Cayley-Dickson construction. For $x = (q_1, q_2)$ and $y = (q_3, q_4)$:

$$\overline{xy} = \overline{(q_1 q_3 - \bar{q}_4 q_2, \; q_4 q_1 + q_2 \bar{q}_3)} = (\overline{q_1 q_3 - \bar{q}_4 q_2}, \; -(q_4 q_1 + q_2 \bar{q}_3)).$$

Meanwhile:

$$\bar{y}\bar{x} = (\bar{q}_3, -q_4)(\bar{q}_1, -q_2) = (\bar{q}_3 \bar{q}_1 - \overline{(-q_2)}(-q_4), \; (-q_2)\bar{q}_3 + (-q_4)\overline{\bar{q}_1}).$$

Simplifying: $= (\bar{q}_3 \bar{q}_1 - \bar{q}_2 q_4, \; -q_2 \bar{q}_3 - q_4 q_1)$. One verifies these expressions agree using $\overline{q_1 q_3} = \bar{q}_3 \bar{q}_1$ (which holds in $\mathbb{H}$). $\square$

**Definition 2.5.2 (Norm).** The *norm* of $x \in \mathbb{O}$ is:

$$|x|^2 = N(x) = x\bar{x} = \bar{x}x = \sum_{i=0}^{7} x_i^2.$$

This is the standard Euclidean norm on $\mathbb{R}^8$.

**Theorem 2.5.1 (Composition Property).** For all $x, y \in \mathbb{O}$:

$$|xy|^2 = |x|^2 |y|^2.$$

**Proof.** We compute:

$$|xy|^2 = (xy)\overline{(xy)} = (xy)(\bar{y}\bar{x}).$$

By alternativity (Chapter 3), for any $x, y \in \mathbb{O}$ the subalgebra generated by $x$ and $y$ is associative (Artin's theorem). Therefore:

$$(xy)(\bar{y}\bar{x}) = x(y\bar{y})\bar{x} = x \cdot |y|^2 \cdot \bar{x} = |y|^2 \cdot x\bar{x} = |y|^2 \cdot |x|^2.$$

(The middle step uses the fact that $|y|^2 \in \mathbb{R}$ commutes with everything.) $\square$

**Definition 2.5.3 (Inverse).** For $x \neq 0$:

$$x^{-1} = \frac{\bar{x}}{|x|^2}.$$

**Verification:** $x \cdot x^{-1} = x \cdot \bar{x}/|x|^2 = |x|^2/|x|^2 = 1$. Similarly $x^{-1} \cdot x = 1$.

**Definition 2.5.4 (Real and Imaginary Parts).**

$$\mathrm{Re}(x) = \frac{x + \bar{x}}{2} = x_0, \quad \mathrm{Im}(x) = \frac{x - \bar{x}}{2} = \sum_{i=1}^{7} x_i e_i.$$

We write $\mathrm{Im}(\mathbb{O})$ for the 7-dimensional space of purely imaginary octonions.

## 2.6 Inner Product and Orthogonality

**Definition 2.6.1.** The inner product on $\mathbb{O}$ is:

$$\langle x, y \rangle = \mathrm{Re}(\bar{x}y) = \mathrm{Re}(x\bar{y}) = \sum_{i=0}^{7} x_i y_i.$$

This is the standard Euclidean inner product on $\mathbb{R}^8$.

**Proposition 2.6.1.** The basis elements $\{1, e_1, \ldots, e_7\}$ are orthonormal:

$$\langle e_i, e_j \rangle = \delta_{ij}, \quad \langle 1, e_i \rangle = 0, \quad \langle 1, 1 \rangle = 1.$$

**Proof.** For $i \neq j$: $\langle e_i, e_j \rangle = \mathrm{Re}(\bar{e}_i e_j) = \mathrm{Re}(-e_i e_j)$. Since $e_i e_j = \pm e_k$ for some $k \in \{1, \ldots, 7\}$ (for $i \neq j$), we have $\mathrm{Re}(\pm e_k) = 0$. For $i = j$: $\langle e_i, e_i \rangle = \mathrm{Re}(-e_i \cdot e_i) = \mathrm{Re}(-(-1)) = 1$. $\square$

## 2.7 Subalgebra Structure

The octonions contain a rich lattice of subalgebras, each isomorphic to one of $\mathbb{R}$, $\mathbb{C}$, or $\mathbb{H}$.

**Proposition 2.7.1.** Every imaginary unit $e_i$ generates a subalgebra $\mathbb{R} \oplus \mathbb{R} e_i \cong \mathbb{C}$.

**Proof.** The subalgebra $\langle 1, e_i \rangle$ has basis $\{1, e_i\}$ with $e_i^2 = -1$. This satisfies exactly the complex number relations. $\square$

**Proposition 2.7.2.** Every oriented line $(i, j, k)$ in the Fano plane generates a subalgebra $\langle 1, e_i, e_j, e_k \rangle \cong \mathbb{H}$.

**Proof.** From the Fano plane, $e_i e_j = e_k$, $e_j e_k = e_i$, $e_k e_i = e_j$, and $e_i^2 = e_j^2 = e_k^2 = -1$. Moreover, $e_i e_j e_k = e_i \cdot e_i = -1$ (using the line relation). These are exactly Hamilton's quaternion relations. The four-dimensional subspace $\mathrm{span}\{1, e_i, e_j, e_k\}$ is closed under multiplication (which can be verified by checking all 16 products), so it forms a subalgebra isomorphic to $\mathbb{H}$. $\square$

**Corollary 2.7.1.** $\mathbb{O}$ contains exactly 7 quaternionic subalgebras, one for each line of the Fano plane.

**Remark (7 subalgebras vs. 480 multiplication tables).** There are exactly 7 *essentially distinct* quaternionic subalgebras of $\mathbb{O}$, one for each line of the Fano plane. Each such subalgebra is a fixed 4-dimensional subspace $\mathrm{span}\{1, e_i, e_j, e_k\} \subset \mathbb{O}$. Separately, the literature records that there are 480 distinct valid multiplication tables for $\mathbb{O}$ (see Appendix A, Section A.5). These 480 tables arise from the $7! = 5040$ possible relabelings of the imaginary units combined with $2^7 = 128$ sign choices for the Fano line orientations, modulo the symmetries of the algebra. All 480 tables define isomorphic copies of $\mathbb{O}$; the choice of table is a choice of basis. Throughout this text, when we refer to "the 7 quaternionic subalgebras," we mean the 7 geometrically distinct ones corresponding to the 7 lines of the Fano plane within a fixed choice of multiplication table.

These subalgebras are:

$$\mathbb{H}_{123}, \; \mathbb{H}_{145}, \; \mathbb{H}_{246}, \; \mathbb{H}_{347}, \; \mathbb{H}_{176}, \; \mathbb{H}_{257}, \; \mathbb{H}_{365}$$

corresponding to the 7 lines of the Fano plane. Any two of these quaternionic subalgebras share exactly one imaginary direction (since any two lines of the Fano plane intersect in exactly one point).

## 2.8 Worked Examples

**Example 2.8.1 (General Multiplication).** Let $x = 1 + 2e_1 - e_3 + 3e_5$ and $y = -1 + e_2 + 2e_4 - e_7$.

We compute $xy$ by distributing and using the multiplication table:

$$xy = (1)(-1) + (1)(e_2) + (1)(2e_4) + (1)(-e_7)$$
$$+ (2e_1)(-1) + (2e_1)(e_2) + (2e_1)(2e_4) + (2e_1)(-e_7)$$
$$+ (-e_3)(-1) + (-e_3)(e_2) + (-e_3)(2e_4) + (-e_3)(-e_7)$$
$$+ (3e_5)(-1) + (3e_5)(e_2) + (3e_5)(2e_4) + (3e_5)(-e_7)$$

Now we evaluate each term:

| Term | Value |
|------|-------|
| $(1)(-1)$ | $-1$ |
| $(1)(e_2)$ | $e_2$ |
| $(1)(2e_4)$ | $2e_4$ |
| $(1)(-e_7)$ | $-e_7$ |
| $(2e_1)(-1)$ | $-2e_1$ |
| $(2e_1)(e_2)$ | $2e_3$ |
| $(2e_1)(2e_4)$ | $4e_5$ |
| $(2e_1)(-e_7)$ | $-2e_6$ (since $e_1 e_7 = e_6$) |
| $(-e_3)(-1)$ | $e_3$ |
| $(-e_3)(e_2)$ | $e_1$ (since $e_3 e_2 = -e_1$, so $-e_3 e_2 = e_1$) |
| $(-e_3)(2e_4)$ | $-2e_7$ (since $e_3 e_4 = e_7$) |
| $(-e_3)(-e_7)$ | $-e_4$ (since $e_3 e_7 = -e_4$, so $(-e_3)(-e_7) = e_3 e_7 = -e_4$) |
| $(3e_5)(-1)$ | $-3e_5$ |
| $(3e_5)(e_2)$ | $-3e_7$ (since $e_5 e_2 = -e_7$ from the multiplication table) |

| $(3e_5)(2e_4)$ | $-6e_1$ (since $e_5 e_4 = -e_1$) |
| $(3e_5)(-e_7)$ | $-3e_2$ (since $e_5 e_7 = e_2$, so $3e_5 \cdot (-e_7) = -3e_2$) |

Now we collect by basis element:

- **Scalar ($1$):** $-1$
- **$e_1$:** $-2 + 1 - 6 = -7$
- **$e_2$:** $1 - 3 = -2$
- **$e_3$:** $2 + 1 = 3$
- **$e_4$:** $2 - 1 = 1$
- **$e_5$:** $4 - 3 = 1$
- **$e_6$:** $-2$
- **$e_7$:** $-1 - 2 - 3 = -6$

**Result:** $xy = -1 - 7e_1 - 2e_2 + 3e_3 + e_4 + e_5 - 2e_6 - 6e_7$.

**Verification via norm:** $|x|^2 = 1 + 4 + 1 + 9 = 15$. $|y|^2 = 1 + 1 + 4 + 1 = 7$. $|xy|^2 = 1 + 49 + 4 + 9 + 1 + 1 + 4 + 36 = 105 = 15 \times 7$. $\checkmark$

**Example 2.8.2 (Inverse Computation).** Let $x = 1 + e_1 + e_2 + e_4$.

Then $|x|^2 = 1 + 1 + 1 + 1 = 4$, $\bar{x} = 1 - e_1 - e_2 - e_4$, and:

$$x^{-1} = \frac{1 - e_1 - e_2 - e_4}{4} = \frac{1}{4} - \frac{1}{4}e_1 - \frac{1}{4}e_2 - \frac{1}{4}e_4.$$

Verification: $x \cdot x^{-1} = (1 + e_1 + e_2 + e_4)\frac{(1 - e_1 - e_2 - e_4)}{4}$. Expanding the numerator:

$$(1)(1) + (1)(-e_1) + (1)(-e_2) + (1)(-e_4) + (e_1)(1) + (e_1)(-e_1) + (e_1)(-e_2) + (e_1)(-e_4)$$
$$+ (e_2)(1) + (e_2)(-e_1) + (e_2)(-e_2) + (e_2)(-e_4) + (e_4)(1) + (e_4)(-e_1) + (e_4)(-e_2) + (e_4)(-e_4)$$

$$= 1 - e_1 - e_2 - e_4 + e_1 + 1 - e_3 - e_5 + e_2 + e_3 + 1 - e_6 + e_4 + e_5 + e_6 + 1$$

$$= 4.$$

So $x \cdot x^{-1} = 4/4 = 1$. $\checkmark$

**Example 2.8.3 (Non-Associativity).** Take $a = e_1$, $b = e_2$, $c = e_4$.

$$(e_1 e_2) e_4 = e_3 \cdot e_4 = e_7.$$
$$e_1 (e_2 e_4) = e_1 \cdot e_6 = -e_7.$$

Therefore $(e_1 e_2)e_4 \neq e_1(e_2 e_4)$, and the associator is:

$$[e_1, e_2, e_4] = (e_1 e_2)e_4 - e_1(e_2 e_4) = e_7 - (-e_7) = 2e_7.$$

This is the fundamental example of non-associativity in $\mathbb{O}$. The associator is nonzero, purely imaginary, and carries information about the triple $(e_1, e_2, e_4)$. Chapter 7 develops the full theory of this object.

## 2.9 The Octonion Algebra as a Real Vector Space

As a vector space, $\mathbb{O} \cong \mathbb{R}^8$ with the standard Euclidean structure. The multiplication map $\mu: \mathbb{O} \times \mathbb{O} \to \mathbb{O}$ is bilinear and determined by the $8 \times 8 \times 8$ structure constants:

$$e_i e_j = \sum_k c_{ij}^k e_k$$

where $c_{ij}^k \in \{-1, 0, 1\}$ and $e_0 = 1$. These structure constants are fully determined by the Fano plane and the rules $e_0 e_i = e_i e_0 = e_i$, $e_i^2 = -e_0$.

The structure constants are completely antisymmetric in the sense that:

$$c_{ij}^k = -c_{ji}^k = c_{jk}^i = c_{ki}^j$$

for $i, j, k \in \{1, \ldots, 7\}$ (with appropriate sign conventions from the Fano orientation). This antisymmetry of the structure constants is a reflection of the alternating property of octonion multiplication (Chapter 3).

## 2.10 The Norm Form and Degen's Eight-Square Identity

The composition property $N(xy) = N(x)N(y)$ is equivalent to the following identity for sums of eight squares. If $x = \sum_{i=0}^{7} x_i e_i$ and $y = \sum_{j=0}^{7} y_j e_j$, then:

$$(x_0^2 + x_1^2 + \cdots + x_7^2)(y_0^2 + y_1^2 + \cdots + y_7^2) = z_0^2 + z_1^2 + \cdots + z_7^2$$

where each $z_k$ is a bilinear expression in the $x_i$ and $y_j$. Explicitly, $z_k$ is the $k$-th component of the product $xy$.

This identity was first discovered by Degen (1818), rediscovered by Graves and Cayley, and connects to the Radon-Hurwitz theory of sums of squares.

**Theorem 2.10.1 (Hurwitz Sum-of-Squares).** An identity of the form

$$(x_1^2 + \cdots + x_n^2)(y_1^2 + \cdots + y_n^2) = z_1^2 + \cdots + z_n^2$$

with each $z_i$ bilinear in $x$ and $y$ exists if and only if $n \in \{1, 2, 4, 8\}$.

This is equivalent to Hurwitz's theorem on normed division algebras.

## 2.11 Summary and Forward References

The octonion algebra $\mathbb{O}$ is a specific, concrete, computable algebraic structure. Every product can be determined from the Fano plane or the multiplication table. Every element has a conjugate, norm, and inverse.

What makes $\mathbb{O}$ extraordinary — and what the rest of this book exploits — is the combination of:

1. **Composition property** (norm is multiplicative): ensures magnitude is well-behaved.
2. **Division property** (every equation solvable): ensures no information is lost.
3. **Non-associativity** (associator nonzero): ensures contextual information is preserved.

The next chapter (Chapter 3) establishes exactly what form of associativity the octonions *do* satisfy — alternativity — and the identities that govern computation in this non-associative but deeply structured algebra.

---

*In Chapter 3, we develop the theory of alternative algebras, proving the Moufang identities and Artin's theorem that any subalgebra generated by two elements is associative.*
