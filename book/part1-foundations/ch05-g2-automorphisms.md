> **Rigor Level: EXPOSITORY** — Accurate exposition of G2 as the automorphism group of the octonions, including its Lie algebra and root system.
> **Novelty: EXPOSITORY** — Synthesizes known results; no new theorems claimed.

# Chapter 5: $G_2$ as the Automorphism Group of the Octonions

## 5.1 Introduction

Every algebraic structure has a group of symmetries — the transformations that preserve its operations. For the octonions, this automorphism group is the exceptional Lie group $G_2$, the smallest of the five exceptional simple Lie groups $G_2, F_4, E_6, E_7, E_8$.

$G_2$ is a 14-dimensional compact Lie group, embedded naturally in $\mathrm{SO}(7)$ as the stabilizer of the octonionic multiplication (equivalently, the 7D cross product, or the associative 3-form $\phi$). It contains $\mathrm{SU}(3)$ as a maximal subgroup — a fact of central importance for connecting octonionic mathematics to the Standard Model of particle physics (Chapter 24).

This chapter constructs $G_2$ explicitly, identifies its Lie algebra $\mathfrak{g}_2$, computes its generators, describes its subgroup structure, and establishes the key theorems that link $G_2$ to octonionic geometry.

## 5.2 Definition and First Properties

**Definition 5.2.1.** An *automorphism* of $\mathbb{O}$ is an $\mathbb{R}$-linear bijection $\alpha: \mathbb{O} \to \mathbb{O}$ that preserves multiplication:

$$\alpha(xy) = \alpha(x)\alpha(y) \quad \text{for all } x, y \in \mathbb{O}.$$

The set of all automorphisms forms a group under composition, denoted $\mathrm{Aut}(\mathbb{O})$ or $G_2$.

**Proposition 5.2.1.** Every automorphism $\alpha \in G_2$ satisfies:

1. $\alpha(1) = 1$ (the identity is fixed).
2. $\alpha(\bar{x}) = \overline{\alpha(x)}$ (conjugation is preserved).
3. $|\alpha(x)| = |x|$ (the norm is preserved; $\alpha$ is an isometry).
4. $\alpha$ maps $\mathrm{Im}(\mathbb{O})$ to itself and acts as an element of $\mathrm{SO}(7)$ on $\mathrm{Im}(\mathbb{O}) \cong \mathbb{R}^7$.

**Proof.**

(1): $\alpha(1) = \alpha(1 \cdot 1) = \alpha(1)\alpha(1)$. Since $\alpha$ is bijective, $\alpha(1) \neq 0$, and the equation $e^2 = e$ with $e \neq 0$ in a division algebra forces $e = 1$.

(2): For any $x \in \mathbb{O}$, $x + \bar{x} = 2\mathrm{Re}(x) \in \mathbb{R}$. So $\alpha(x) + \alpha(\bar{x}) = \alpha(x + \bar{x}) = 2\mathrm{Re}(x) \cdot 1$ (since $\alpha$ fixes reals). Thus $\alpha(\bar{x}) = 2\mathrm{Re}(x) - \alpha(x) = \overline{\alpha(x)}$.

(3): $|\alpha(x)|^2 = \alpha(x)\overline{\alpha(x)} = \alpha(x)\alpha(\bar{x}) = \alpha(x\bar{x}) = \alpha(|x|^2) = |x|^2$.

(4): Since $\alpha$ preserves the real part ($\mathrm{Re}(\alpha(x)) = \mathrm{Re}(x)$), it maps the orthogonal complement $\mathrm{Im}(\mathbb{O}) = \{x : \mathrm{Re}(x) = 0\} = 1^\perp$ to itself. Being norm-preserving and orientation-preserving (as a connected group contains the identity), it acts as an element of $\mathrm{SO}(7)$. $\square$

**Corollary 5.2.1.** $G_2 \subset \mathrm{SO}(7)$ (where $\mathrm{SO}(7)$ acts on $\mathrm{Im}(\mathbb{O}) \cong \mathbb{R}^7$).

## 5.3 The Dimension of $G_2$

**Theorem 5.3.1.** $\dim(G_2) = 14$.

**Proof (Dimension count).** An element of $G_2$ is an orthogonal transformation of $\mathbb{R}^7$ (so lies in $\mathrm{SO}(7)$, which has dimension $\binom{7}{2} = 21$) that additionally preserves the multiplication. The multiplication is encoded by the 7 constraints that each Fano line is preserved as an oriented triple. However, these 7 constraints are not independent.

More precisely, an automorphism $\alpha$ is determined by its action on any two imaginary units $e_i, e_j$ that do not lie on the same Fano line. Given $\alpha(e_1) = u$ and $\alpha(e_2) = v$ (unit imaginary octonions with $\langle u, v \rangle = 0$), the entire automorphism is determined:

- $\alpha(e_3) = \alpha(e_1 e_2) = uv$,
- $\alpha(e_4)$ is determined by the constraint that $\alpha(e_1)\alpha(e_4) = \alpha(e_5)$ and the norm/orthogonality conditions.

The dimension count proceeds in three steps.

**Step 1:** Choose $\alpha(e_1) = u$. Since $u$ must be a unit imaginary octonion, $u \in S^6 \subset \mathrm{Im}(\mathbb{O})$. This gives 6 free parameters.

**Step 2:** Choose $\alpha(e_2) = v$. The constraints are: $|v| = 1$ and $\langle v, u \rangle = 0$. (Since $v$ is imaginary, it is automatically orthogonal to $1$. The product $\alpha(e_3) = uv$ is automatically a unit imaginary octonion when $u$ and $v$ are orthogonal unit imaginary octonions.) So $v$ ranges over $S^5 \subset u^\perp \cap \mathrm{Im}(\mathbb{O})$, giving 5 more parameters.

**Step 3:** Given $\alpha(e_1) = u$ and $\alpha(e_2) = v$, we have $\alpha(e_3) = uv$. Now choose $\alpha(e_4) = w$. The constraints are: $|w| = 1$, $w \perp u$, $w \perp v$, $w \perp uv$. So $w \in S^3 \subset \{u, v, uv\}^\perp$. This gives $\dim(S^3) = 3$ more parameters.

**Step 4:** Once $\alpha(e_1), \alpha(e_2), \alpha(e_4)$ are chosen, ALL remaining values are determined:

- $\alpha(e_5) = \alpha(e_1)\alpha(e_4) = uw$,
- $\alpha(e_6) = \alpha(e_2)\alpha(e_4) = vw$,
- $\alpha(e_7) = \alpha(e_3)\alpha(e_4) = (uv)w$.

So the total dimension is $6 + 5 + 3 = 14$. $\square$

**Alternative proof via the stabilizer sequence:**

$$G_2 / \mathrm{SU}(3) \cong S^6, \quad \mathrm{SU}(3) / \mathrm{SU}(2) \cong S^5, \quad \mathrm{SU}(2) \cong S^3.$$

Therefore $\dim(G_2) = \dim(S^6) + \dim(S^5) + \dim(S^3) = 6 + 5 + 3 = 14$.

This fiber sequence is:

$$\mathrm{SU}(3) \hookrightarrow G_2 \to S^6$$

where the map $G_2 \to S^6$ sends $\alpha \mapsto \alpha(e_1)$. The fiber over any point is the stabilizer of a single imaginary unit, which is $\mathrm{SU}(3)$ (Theorem 5.6.1 below).

## 5.4 The Lie Algebra $\mathfrak{g}_2$

**Definition 5.4.1.** The Lie algebra $\mathfrak{g}_2 = \mathrm{Lie}(G_2)$ consists of all *derivations* of $\mathbb{O}$: $\mathbb{R}$-linear maps $D: \mathbb{O} \to \mathbb{O}$ satisfying the Leibniz rule:

$$D(xy) = D(x) \cdot y + x \cdot D(y) \quad \text{for all } x, y \in \mathbb{O}.$$

We write $\mathrm{Der}(\mathbb{O})$ for this space. It is a Lie algebra under the commutator bracket $[D_1, D_2] = D_1 D_2 - D_2 D_1$.

**Proposition 5.4.1.** Every derivation $D \in \mathrm{Der}(\mathbb{O})$ satisfies:
1. $D(1) = 0$.
2. $D(\bar{x}) = \overline{D(x)}$.
3. $D$ maps $\mathrm{Im}(\mathbb{O})$ to itself.
4. $D$ is skew-symmetric: $\langle D(x), y \rangle + \langle x, D(y) \rangle = 0$.

**Proof.** (1): $D(1) = D(1 \cdot 1) = D(1) \cdot 1 + 1 \cdot D(1) = 2D(1)$, so $D(1) = 0$.

(2): $0 = D(\mathrm{Re}(x)) = D((x + \bar{x})/2) = (D(x) + D(\bar{x}))/2$. But $\mathrm{Re}(D(x)) = \mathrm{Re}(D(\mathrm{Im}(x)))$. Since $D$ sends imaginary octonions to imaginary octonions (which we now prove): for $x \in \mathrm{Im}(\mathbb{O})$, $\bar{x} = -x$, and from $0 = D(x\bar{x}) = D(x)\bar{x} + xD(\bar{x})$, we can show $D(\bar{x}) = \overline{D(x)}$.

(3): Follows from (2): if $\bar{x} = -x$, then $\overline{D(x)} = D(\bar{x}) = D(-x) = -D(x)$, so $D(x)$ is imaginary.

(4): $0 = D(|x|^2) = D(x\bar{x}) = D(x)\bar{x} + xD(\bar{x}) = D(x)\bar{x} + x\overline{D(x)}$. Taking the real part: $\mathrm{Re}(D(x)\bar{x}) + \mathrm{Re}(x\overline{D(x)}) = 2\langle D(x), x \rangle = 0$. By polarization, $\langle D(x), y \rangle + \langle x, D(y) \rangle = 0$. $\square$

Therefore $\mathfrak{g}_2 \subset \mathfrak{so}(7)$ (the Lie algebra of $\mathrm{SO}(7)$, which consists of skew-symmetric linear maps on $\mathbb{R}^7$).

## 5.5 The 14 Generators of $\mathfrak{g}_2$

$\mathfrak{so}(7)$ has dimension $\binom{7}{2} = 21$. Its standard basis consists of the maps $E_{ij}$ ($1 \leq i < j \leq 7$) defined by $E_{ij}(e_k) = \delta_{jk} e_i - \delta_{ik} e_j$. Of these 21 generators, exactly 14 are derivations of $\mathbb{O}$, forming a basis of $\mathfrak{g}_2$.

**Construction.** For each imaginary octonion $a \in \mathrm{Im}(\mathbb{O})$, define the *adjoint map*:

$$\mathrm{ad}_a: \mathbb{O} \to \mathbb{O}, \quad \mathrm{ad}_a(x) = [a, x] = ax - xa.$$

This is NOT a derivation in general (unlike the Lie algebra case). However, the map:

$$D_{a,b} = [L_a, L_b] + [L_a, R_b] + [R_a, R_b]$$

where $L_a(x) = ax$ and $R_a(x) = xa$, IS a derivation for any $a, b \in \mathrm{Im}(\mathbb{O})$. Moreover, every derivation of $\mathbb{O}$ has this form.

**Theorem 5.5.1 (Schafer).** The derivation algebra of $\mathbb{O}$ is spanned by maps of the form:

$$D_{a,b}(x) = [[a, b], x] - 3[a, b, x]$$

for $a, b \in \mathrm{Im}(\mathbb{O})$, where $[a, b] = ab - ba$ is the commutator and $[a, b, x] = (ab)x - a(bx)$ is the associator.

Equivalently:

$$D_{a,b}(x) = \frac{1}{2}(a(bx) - b(ax) + (xb)a - (xa)b + a(xb) - b(xa))$$

after simplification using the alternative laws.

**A concrete basis.** One can choose the following 14 derivations as a basis for $\mathfrak{g}_2$, organized by the root system. The root system of $G_2$ consists of 12 roots (6 positive, 6 negative) plus 2 zero weights (the Cartan subalgebra).

Choose the Cartan subalgebra $\mathfrak{h} = \mathrm{span}\{H_1, H_2\}$ where:

$$H_1 = D_{e_1, -e_3}, \quad H_2 = D_{e_2, -e_1}.$$

The Cartan subalgebra of $\mathfrak{g}_2$ is 2-dimensional (since $\mathrm{rank}(G_2) = 2$). Under the action of $\mathfrak{h} = \mathrm{span}\{H_1, H_2\}$, the eigenvalues on each basis element $e_k$ are determined by the $G_2$ root system.

Under the action of $\mathfrak{h}$, the imaginary octonion space $\mathrm{Im}(\mathbb{O}) \cong \mathbb{R}^7$ decomposes as:

$$\mathbb{R}^7 = \mathbb{R}^1 \oplus \mathbb{C}^3$$

where $\mathbb{R}^1$ is the trivial representation of $\mathrm{SU}(3) \subset G_2$ (a fixed imaginary direction) and $\mathbb{C}^3$ is the fundamental representation of $\mathrm{SU}(3)$.

The 14 generators can be organized as:
- **2 Cartan generators** $H_1, H_2$ (diagonal).
- **6 short root generators** corresponding to the $\mathrm{SU}(3)$ roots.
- **6 long root generators** corresponding to the coset $G_2 / \mathrm{SU}(3)$.

## 5.6 Subgroup Structure

### 5.6.1 $\mathrm{SU}(3) \subset G_2$

**Theorem 5.6.1.** The stabilizer of a single imaginary unit $e_i$ in $G_2$ is isomorphic to $\mathrm{SU}(3)$:

$$\mathrm{Stab}_{G_2}(e_i) \cong \mathrm{SU}(3).$$

**Proof.** Fix $e_1$, say. An automorphism $\alpha \in G_2$ with $\alpha(e_1) = e_1$ must also fix the quaternionic subalgebra $\mathbb{H}_{1jk}$ for any Fano line through $1$. The orthogonal complement of $\mathrm{span}\{e_1\}$ in $\mathrm{Im}(\mathbb{O})$ is 6-dimensional. Using $e_1$ to define a complex structure $J: v \mapsto e_1 \cdot v$ on this 6-dimensional space (restricted to $\{e_1\}^\perp \cap \mathrm{Im}(\mathbb{O})$), the stabilizer acts by complex-linear, norm-preserving, determinant-1 transformations, yielding $\mathrm{SU}(3)$.

More concretely, the space $\{e_1\}^\perp$ has basis $\{e_2, e_3, e_4, e_5, e_6, e_7\}$. Multiplication by $e_1$ on the left defines a complex structure (since $e_1^2 = -1$). The complex eigenspaces are:

Since $e_1 \cdot e_2 = e_3$, the pair $(e_2, e_3)$ forms a complex pair under the complex structure $J = L_{e_1}$. Similarly, $e_1 \cdot e_4 = e_5$ gives the pair $(e_4, e_5)$, and $e_1 \cdot e_7 = e_6$ gives the pair $(e_7, e_6)$.

Defining complex coordinates $z_1 = e_2 + ie_3$, $z_2 = e_4 + ie_5$, $z_3 = e_7 + ie_6$ (here $i$ is a formal $\sqrt{-1}$ for the complex structure, identified with the action of $e_1$), the stabilizer of $e_1$ acts on $(z_1, z_2, z_3) \in \mathbb{C}^3$ by unitary transformations. The constraint that it preserves the octonionic multiplication forces the determinant to be 1, giving $\mathrm{SU}(3)$. $\square$

**Corollary 5.6.1.** The quotient $G_2/\mathrm{SU}(3) \cong S^6$.

This is the 6-sphere of unit imaginary octonions.

### 5.6.2 $\mathrm{SU}(2) \subset \mathrm{SU}(3) \subset G_2$

**Theorem 5.6.2.** The stabilizer of two orthogonal imaginary units in $G_2$ is isomorphic to $\mathrm{SU}(2)$:

$$\mathrm{Stab}_{G_2}(e_1, e_2) \cong \mathrm{SU}(2).$$

**Proof.** If $\alpha$ fixes both $e_1$ and $e_2$, then it fixes $e_3 = e_1 e_2$ as well. The quaternionic subalgebra $\mathbb{H}_{123}$ is pointwise fixed. The remaining space $\mathrm{span}\{e_4, e_5, e_6, e_7\}$ is 4-dimensional. The constraints from the Fano lines through $e_1$ and $e_2$ further restrict the action on this 4-dimensional space. The resulting stabilizer is $\mathrm{SU}(2) \cong S^3$, acting on the 4-dimensional complement. $\square$

### 5.6.3 The Full Stabilizer Chain

$$\{1\} \subset \mathrm{SU}(2) \subset \mathrm{SU}(3) \subset G_2 \subset \mathrm{SO}(7)$$

with dimensions $0 \subset 3 \subset 8 \subset 14 \subset 21$, and the homogeneous spaces:

$$G_2/\mathrm{SU}(3) = S^6, \quad \mathrm{SU}(3)/\mathrm{SU}(2) = S^5, \quad \mathrm{SU}(2)/\{1\} = S^3.$$

### 5.6.4 $\mathrm{SO}(4) \subset G_2$

**Proposition 5.6.3.** $G_2$ contains $\mathrm{SO}(4)$ as a subgroup, acting on a quaternionic subalgebra and its orthogonal complement.

### 5.6.5 The Embedding $G_2 \subset \mathrm{SO}(7) \subset \mathrm{SO}(8)$

The group $\mathrm{SO}(7)$ has dimension 21. The embedding $G_2 \hookrightarrow \mathrm{SO}(7)$ is such that the 21-dimensional adjoint representation of $\mathrm{SO}(7)$ decomposes under $G_2$ as:

$$\mathfrak{so}(7) = \mathfrak{g}_2 \oplus \mathbb{R}^7$$

where $\mathbb{R}^7$ is the 7-dimensional fundamental representation of $G_2$. That is, the 7 "missing" dimensions of $\mathrm{SO}(7)$ relative to $G_2$ transform as the standard representation of $G_2$.

## 5.7 Representation Theory of $G_2$

### 5.7.1 The Root System

$G_2$ has rank 2. Its root system consists of 12 roots: 6 short roots and 6 long roots, arranged in a hexagonal pattern with the ratio of long to short root lengths being $\sqrt{3}$.

The simple roots are $\alpha_1$ (short) and $\alpha_2$ (long), with the Cartan matrix:

$$A = \begin{pmatrix} 2 & -3 \\ -1 & 2 \end{pmatrix}$$

The angle between the simple roots is $150°$.

The positive roots are: $\alpha_1$, $\alpha_2$, $\alpha_1 + \alpha_2$, $2\alpha_1 + \alpha_2$, $3\alpha_1 + \alpha_2$, $3\alpha_1 + 2\alpha_2$.

### 5.7.2 Fundamental Representations

$G_2$ has two fundamental representations:

1. **The 7-dimensional representation $\mathbf{7}$**: This is the action of $G_2$ on $\mathrm{Im}(\mathbb{O}) \cong \mathbb{R}^7$. It is the smallest faithful representation of $G_2$.

2. **The 14-dimensional adjoint representation $\mathbf{14}$**: This is $\mathfrak{g}_2$ itself, the derivation algebra of $\mathbb{O}$.

Under the subgroup $\mathrm{SU}(3) \subset G_2$, these decompose as:

$$\mathbf{7} = \mathbf{1} \oplus \mathbf{3} \oplus \bar{\mathbf{3}}$$

$$\mathbf{14} = \mathbf{8} \oplus \mathbf{3} \oplus \bar{\mathbf{3}}$$

The $\mathbf{8}$ is the adjoint representation of $\mathrm{SU}(3)$ (i.e., the gluons in physics language). The $\mathbf{3}$ and $\bar{\mathbf{3}}$ are the fundamental and anti-fundamental representations (i.e., quarks and anti-quarks).

### 5.7.3 The Casimir Operator

The quadratic Casimir operator of $G_2$ in the 7-dimensional representation takes the form:

$$C_2 = \sum_{A=1}^{14} T^A T^A$$

where $\{T^A\}$ are the 14 generators in the 7-dimensional representation (7×7 skew-symmetric matrices). Its eigenvalue in the representation $\mathbf{7}$ is:

$$C_2(\mathbf{7}) = 4$$

(with appropriate normalization convention).

## 5.8 $G_2$ and the 3-Form $\phi$

**Theorem 5.8.1.** The following are equivalent characterizations of $G_2 \subset GL(7, \mathbb{R})$:

1. $G_2 = \mathrm{Aut}(\mathbb{O})$ (automorphisms of the octonion algebra).
2. $G_2 = \mathrm{Stab}(\phi)$ (stabilizer of the associative 3-form).
3. $G_2 = \mathrm{Stab}(\times)$ (stabilizer of the 7D cross product).
4. $G_2 = \mathrm{Stab}(\phi) \cap \mathrm{Stab}(\psi)$ where $\psi = *\phi$ is the coassociative 4-form.
5. $G_2 = \{g \in \mathrm{SO}(7) : g^*\phi = \phi\}$.

**Proof of $(1) \Leftrightarrow (2)$.** The 3-form $\phi$ is defined by $\phi(a, b, c) = \langle a \times b, c \rangle$ (Section 4.6). An automorphism $\alpha$ preserves the multiplication, hence the cross product: $\alpha(a) \times \alpha(b) = \alpha(a \times b)$. Since $\alpha$ also preserves the inner product: $\phi(\alpha(a), \alpha(b), \alpha(c)) = \langle \alpha(a) \times \alpha(b), \alpha(c) \rangle = \langle \alpha(a \times b), \alpha(c) \rangle = \langle a \times b, c \rangle = \phi(a, b, c)$. So $\alpha^* \phi = \phi$.

Conversely, if $g \in GL(7)$ stabilizes $\phi$, one can reconstruct the cross product from $\phi$ (via $\langle g(a) \times g(b), g(c) \rangle = \phi(g(a), g(b), g(c)) = \phi(a,b,c) = \langle a \times b, c \rangle$, which implies $g(a) \times g(b) = g(a \times b)$ since $g$ is invertible and $c$ is arbitrary). Then one extends the cross product to the full octonionic multiplication via $uv = -\langle u, v \rangle + u \times v$ for imaginary octonions, showing $g$ preserves the multiplication. $\square$

## 5.9 $G_2$ Manifolds and Holonomy

**Definition 5.9.1.** A *$G_2$-manifold* is a 7-dimensional Riemannian manifold $(M^7, g)$ whose holonomy group is contained in $G_2 \subset \mathrm{SO}(7)$.

Equivalently, a $G_2$-manifold admits a *torsion-free* $G_2$-structure: a 3-form $\phi$ (locally modeled on the octonionic 3-form) satisfying $\nabla \phi = 0$ (where $\nabla$ is the Levi-Civita connection).

**Theorem 5.9.1 (Berger's Classification).** $G_2$ appears in Berger's list of possible holonomy groups of irreducible, simply-connected, non-symmetric Riemannian manifolds. The existence of compact $G_2$-manifolds was proved by Joyce (1996).

**Significance for the framework.** $G_2$-manifolds are the compactification spaces in M-theory that yield $N = 1$ supersymmetry in 4 dimensions. The internal space of M-theory is 7-dimensional with $G_2$ holonomy, making the connection between octonions and fundamental physics geometric and inevitable.

## 5.10 The Embedding $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1) \hookrightarrow G_2$

**Theorem 5.10.1.** The Standard Model gauge group $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$ can be embedded in $G_2$, with the following correspondence:

- $\mathrm{SU}(3)$: the color gauge group, acting on the 3-dimensional complex subspace of $\mathrm{Im}(\mathbb{O})$ (the quark color triplet).
- $\mathrm{SU}(2)$: a subgroup of $\mathrm{SU}(3)$, acting as the weak isospin.
- $\mathrm{U}(1)$: the hypercharge, acting as a phase rotation.

**Proof sketch.** We have established $\mathrm{SU}(3) \subset G_2$ as the stabilizer of a single imaginary unit (Theorem 5.6.1). Within $\mathrm{SU}(3)$, the subgroup $\mathrm{SU}(2)$ is the stabilizer of a second imaginary unit (Theorem 5.6.2). The $\mathrm{U}(1)$ factor sits in the center of certain subgroups.

More precisely, the decomposition of $\mathrm{Im}(\mathbb{O})$ under $\mathrm{SU}(3)$ is $\mathbf{1} \oplus \mathbf{3} \oplus \bar{\mathbf{3}}$. The $\mathbf{3}$ can be identified with the color triplet of QCD. Under further restriction to $\mathrm{SU}(2) \subset \mathrm{SU}(3)$, the $\mathbf{3}$ decomposes as $\mathbf{2} \oplus \mathbf{1}$, giving the weak doublet and singlet.

The precise embedding requires careful identification of the $\mathrm{U}(1)$ hypercharge. Defining $Y$ as a specific generator of the Cartan subalgebra of $\mathfrak{su}(3)$, the electric charge formula $Q = I_3 + Y/2$ can be recovered. $\square$

**Remark 5.10.1.** The dimension count is: $\dim(\mathrm{SU}(3)) + \dim(\mathrm{SU}(2)) + \dim(\mathrm{U}(1)) = 8 + 3 + 1 = 12 < 14 = \dim(G_2)$. So the Standard Model gauge group does not fill all of $G_2$ — there are two additional dimensions. These correspond to transformations that mix the "known" forces with the additional octonionic structure, and they are a primary subject of Chapter 24.

## 5.11 Worked Example: An Explicit $G_2$ Transformation

Consider the $G_2$ transformation that rotates $e_1 \to e_2$, preserving the octonionic multiplication.

This is NOT simply a rotation in the $(e_1, e_2)$ plane (which would be an $\mathrm{SO}(7)$ element but not generally a $G_2$ element). A $G_2$ rotation must simultaneously transform all other basis elements to maintain the Fano plane structure.

Let $\alpha \in G_2$ with $\alpha(e_1) = e_2$. Then:

- $\alpha(e_2)$ must satisfy: $\alpha(e_1)\alpha(e_2) = \alpha(e_1 e_2) = \alpha(e_3)$. So we need $e_2 \alpha(e_2) = \alpha(e_3)$.
- From the Fano plane, we need a consistent assignment. One valid choice (there is a family parametrized by $\mathrm{SU}(3)$) is obtained by choosing $\alpha(e_2) = e_4$. Then $\alpha(e_3) = e_2 e_4 = e_6$.
- Next: $\alpha(e_4)$ must satisfy $\alpha(e_1)\alpha(e_4) = \alpha(e_5)$, i.e., $e_2 \alpha(e_4) = \alpha(e_5)$. And $\alpha(e_2)\alpha(e_4) = \alpha(e_6)$, i.e., $e_4 \alpha(e_4) = \alpha(e_6)$.
- Choosing $\alpha(e_4) = e_3$ (so that $\alpha(e_5) = e_2 e_3 = e_1$ and $\alpha(e_6) = e_4 e_3 = -e_7$).

Let us verify consistency step by step. With $\alpha(e_1) = e_2$, $\alpha(e_2) = e_4$, $\alpha(e_3) = e_6$, $\alpha(e_4) = e_3$:

$\alpha(e_5) = \alpha(e_1 e_4) = \alpha(e_1)\alpha(e_4) = e_2 e_3 = e_1$. So $\alpha(e_5) = e_1$.

$\alpha(e_6) = \alpha(e_2 e_4) = \alpha(e_2)\alpha(e_4) = e_4 e_3 = -e_7$. So $\alpha(e_6) = -e_7$.

$\alpha(e_7) = \alpha(e_3 e_4) = \alpha(e_3)\alpha(e_4) = e_6 e_3 = e_5$. So $\alpha(e_7) = e_5$.

Verification: $|\alpha(e_i)| = 1$ for all $i$. $\checkmark$ The $\alpha(e_i)$ are pairwise orthogonal. Let us check: $\{e_2, e_4, e_6, e_3, e_1, -e_7, e_5\}$ — these are all distinct (up to sign) basis elements, hence orthogonal. $\checkmark$

Let us verify one multiplication: $\alpha(e_5 e_3) = \alpha(e_6)$. On the other hand, $\alpha(e_5)\alpha(e_3) = e_1 \cdot e_6 = -e_7$. And indeed $\alpha(e_6) = -e_7$. $\checkmark$

This gives one explicit element of $G_2$, represented as a $7 \times 7$ signed permutation matrix.

## 5.12 Summary and Forward References

$G_2$ is the automorphism group of the octonions — the group of all symmetries that preserve octonionic multiplication. With 14 dimensions, it is considerably smaller than the full rotation group $\mathrm{SO}(7)$ (21 dimensions), reflecting the rigidity imposed by the non-associative multiplication structure.

Key facts for subsequent chapters:

- $G_2$ is the symmetry group of the Contextual Octonionic Algebra (Chapter 6).
- The decomposition $\mathfrak{so}(7) = \mathfrak{g}_2 \oplus \mathbb{R}^7$ gives a natural splitting of rotations into "symmetric" ($G_2$) and "contextual" ($\mathbb{R}^7$) parts (Chapter 7).
- The embedding $\mathrm{SU}(3) \subset G_2$ is the algebraic origin of color charge (Chapter 24).
- $G_2$ holonomy determines the geometry of the extended 7D framework (Chapters 28–33).
- The generators of $\mathfrak{g}_2$ as derivations of $\mathbb{O}$ will reappear as the "transparent" operations in the COA framework — those that preserve the multiplication structure (Chapter 6).

---

*Chapter 6 introduces the new axiomatic framework — the Contextual Octonionic Algebra — that extends Lie theory into the non-associative, uncountable-basis territory.*
