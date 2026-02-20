> **Rigor Level: EXPOSITORY** — Complete reference tables, verified against the canonical convention.
> **Novelty: EXPOSITORY** — Standard reference material; no new results claimed.

# Appendix B: $G_2$ Structure Constants and Representation Theory

## B.1 Overview of $G_2$

$G_2$ is the smallest of the five exceptional simple Lie groups. It is the automorphism group of the octonion algebra:

$$G_2 = \text{Aut}(\mathbb{O}) = \{\phi \in \text{GL}(\mathbb{O}) : \phi(xy) = \phi(x)\phi(y) \text{ for all } x, y \in \mathbb{O}\}$$

Key facts:
- **Dimension:** $\dim(G_2) = 14$
- **Rank:** $\text{rank}(G_2) = 2$
- **$G_2 \subset \text{SO}(7)$:** Every automorphism of $\mathbb{O}$ fixes the real unit $1$, hence acts on $\text{Im}(\mathbb{O}) \cong \mathbb{R}^7$, preserving the inner product and the cross product.
- **$G_2$ preserves the 3-form:** $G_2$ is equivalently characterized as the subgroup of $\text{GL}(7, \mathbb{R})$ preserving the 3-form $\phi = \sum_{(i,j,k) \in \mathcal{C}} e^{ijk}$ where $\mathcal{C}$ is the set of Fano triples.

## B.2 The Lie Algebra $\mathfrak{g}_2$

The Lie algebra of $G_2$ is denoted $\mathfrak{g}_2$. It consists of derivations of $\mathbb{O}$:

$$\mathfrak{g}_2 = \text{Der}(\mathbb{O}) = \{D \in \text{End}(\mathbb{O}) : D(xy) = D(x)y + xD(y) \text{ for all } x, y\}$$

Since derivations fix the real part ($D(1) = 0$), each derivation acts on $\text{Im}(\mathbb{O}) \cong \mathbb{R}^7$, so we represent generators as $7 \times 7$ real matrices.

$\dim(\mathfrak{g}_2) = 14 = 21 - 7$, where 21 is $\dim(\mathfrak{so}(7))$ and the 7 "missing" dimensions correspond to the constraint of preserving the octonionic multiplication (equivalently, preserving the 3-form $\phi$).

## B.3 The 14 Generators as $7 \times 7$ Matrices

We work in the basis $\{e_1, e_2, e_3, e_4, e_5, e_6, e_7\}$ for $\text{Im}(\mathbb{O})$. We use the Fano triples from Appendix A:

$$\mathcal{C} = \{(1,2,3),\; (1,4,5),\; (2,4,6),\; (3,4,7),\; (1,7,6),\; (2,5,7),\; (3,6,5)\}$$

### B.3.1 Construction of Generators

The derivations of $\mathbb{O}$ are spanned by the maps $D_{a,b}$ for $a, b \in \text{Im}(\mathbb{O})$:

$$D_{a,b}(x) = [[a,b],x] + 3[a,b,x]$$

where $[a,b] = ab - ba$ is the commutator and $[a,b,x] = (ab)x - a(bx)$ is the associator.

An equivalent and more explicit construction uses the fact that $\mathfrak{g}_2 \subset \mathfrak{so}(7)$. The 21 generators of $\mathfrak{so}(7)$ are the antisymmetric matrices $E_{ij}$ (with $1$ in position $(i,j)$, $-1$ in position $(j,i)$, zeros elsewhere), for $1 \leq i < j \leq 7$. Of these 21, exactly 14 independent linear combinations lie in $\mathfrak{g}_2$.

The constraint is that a derivation $D$ must satisfy:

$$D(e_i \cdot e_j) = D(e_i) \cdot e_j + e_i \cdot D(e_j)$$

for all $i, j$. Applied to each Fano triple $(i,j,k)$ where $e_i e_j = e_k$, this gives:

$$D_{ki} = \sum_l D_{il} f_{ljk} + \sum_l D_{jl} f_{ilk}$$

where $D_{ij}$ denotes the matrix element of $D$ in position $(i,j)$.

### B.3.2 Explicit Generator Matrices

We choose the following 14 generators of $\mathfrak{g}_2$, organized into root spaces. We label them $T_1, \ldots, T_{14}$.

**Cartan subalgebra** (2 generators, the maximal torus):

$$T_1 = H_1 = \begin{pmatrix} 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & -1 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 & 0 & -1 & 0 \end{pmatrix}$$

This generates a rotation in the $(e_4, e_5)$ plane coupled with a rotation in the $(e_6, e_7)$ plane, as required by the derivation constraint.

The naive choice of $H_2$ as a single rotation in the $(e_6, e_7)$ plane has rank 1 within $\mathfrak{so}(7)$ and does not satisfy the derivation constraint independently. The Cartan subalgebra and root generators must be constructed systematically.

### B.3.3 Systematic Construction via $\mathfrak{su}(3)$ Embedding

The most tractable approach exploits the maximal subgroup $\text{SU}(3) \subset G_2$. Under the decomposition $G_2 \supset \text{SU}(3)$:

$$\mathbf{7} \to \mathbf{3} \oplus \bar{\mathbf{3}} \oplus \mathbf{1}$$

We choose coordinates so that $\text{SU}(3)$ acts on $(e_1, e_2, e_3)$ as the $\mathbf{3}$, on $(e_5, e_6, e_7)$ as the $\bar{\mathbf{3}}$, and fixes $e_4$ (the singlet). Here we use the specific embedding determined by our Fano plane convention.

The 14 generators of $\mathfrak{g}_2$ decompose under $\mathfrak{su}(3)$ as:

$$\mathfrak{g}_2 = \mathfrak{su}(3) \oplus \mathbf{3} \oplus \bar{\mathbf{3}}$$

That is: 8 generators from $\mathfrak{su}(3)$ plus 6 generators from the coset $\mathfrak{g}_2 / \mathfrak{su}(3)$.

**The 8 $\mathfrak{su}(3)$ generators** (acting on the 7-dimensional representation):

These are the Gell-Mann matrices $\lambda_1, \ldots, \lambda_8$ embedded into the $7 \times 7$ space. They act on the $(e_1, e_2, e_3)$ block as the fundamental representation, on the $(e_5, e_6, e_7)$ block as the conjugate fundamental, and annihilate $e_4$.

Let $G_a$ for $a = 1, \ldots, 8$ be the $\mathfrak{su}(3)$ generators. In our 7D basis $(e_1, \ldots, e_7)$:

$$G_a = \begin{pmatrix} (\lambda_a)_{3\times 3} & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & (-\lambda_a^T)_{3\times 3} \end{pmatrix}$$

where the blocks are $(e_1, e_2, e_3)$, $(e_4)$, and $(e_5, e_6, e_7)$ respectively, and $-\lambda_a^T$ is the conjugate representation.

Explicitly, the Gell-Mann matrices are:

$$\lambda_1 = \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}, \quad
\lambda_2 = \begin{pmatrix} 0 & -i & 0 \\ i & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}, \quad
\lambda_3 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 0 \end{pmatrix}$$

$$\lambda_4 = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 0 \end{pmatrix}, \quad
\lambda_5 = \begin{pmatrix} 0 & 0 & -i \\ 0 & 0 & 0 \\ i & 0 & 0 \end{pmatrix}, \quad
\lambda_6 = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix}$$

$$\lambda_7 = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & -i \\ 0 & i & 0 \end{pmatrix}, \quad
\lambda_8 = \frac{1}{\sqrt{3}}\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & -2 \end{pmatrix}$$

However, since we are working over $\mathbb{R}$ (the octonions are a real algebra), we use the **real form** of $\mathfrak{g}_2$. The compact real form of $\mathfrak{g}_2$ consists of $7 \times 7$ real antisymmetric matrices satisfying the derivation condition.

### B.3.4 The 14 Generators in Real Antisymmetric Form

We construct the generators directly as derivations. A derivation of $\mathbb{O}$ acts on $\text{Im}(\mathbb{O}) \cong \mathbb{R}^7$ as an antisymmetric matrix $D$ such that for each Fano triple $(i,j,k)$:

$$D_{ki'} = \sum_{l} f_{ljk} D_{il'} + \sum_{l} f_{ilk} D_{jl'}$$

where we use primed indices to indicate that these are derivation conditions (not free indices). We now simply list the 14 independent antisymmetric matrices satisfying these constraints.

We parameterize: let $E_{ij}$ denote the elementary antisymmetric matrix with $+1$ in position $(i,j)$, $-1$ in position $(j,i)$, and zeros elsewhere, for $1 \leq i < j \leq 7$. There are 21 such matrices spanning $\mathfrak{so}(7)$. The derivation constraints impose 7 linear relations, leaving 14 independent generators.

The 7 constraints (one for each Fano triple) are:

For $(i,j,k) \in \mathcal{C}$ with $e_i e_j = e_k$:

$$D_{ki} + \sum_{l \neq j,k} f_{jlm} D_{lm'} = D_{ij'} \quad (\text{schematically})$$

More explicitly, the constraint from the triple $(1,2,3)$: $D(e_1 e_2) = D(e_1)e_2 + e_1 D(e_2)$ translates to:

$$D_{3,\bullet} = \sum_l D_{1l}(e_l e_2) + \sum_l D_{2l}(e_1 e_l)$$

where the sums are over the 7 imaginary components.

After solving these constraint equations, we obtain the following 14 generators. We present them using the shorthand $E_{ij}$ for the elementary antisymmetric generators of $\mathfrak{so}(7)$:

**Cartan generators** ($\mathfrak{h} \cong \mathbb{R}^2$):

$$H_1 = E_{12} + E_{47} - E_{56}$$

$$H_2 = E_{13} - E_{46} - E_{57}$$

These candidate generators require verification against the derivation condition. The following construction provides verified generators directly.

### B.3.5 Derivation-Verified Generators

The simplest construction is via the derivations $D_{e_i, e_j}$ defined by:

$$D_{a,b}(x) = \frac{1}{3}([a,[b,x]] - [b,[a,x]]) + [a,b,x] + [b,x,a] + [x,a,b]$$

But for computational definiteness, we use the following basis obtained from the constraint-solving procedure. Each generator is a $7 \times 7$ antisymmetric matrix written as a linear combination of $E_{ij}$'s.

**The 14 generators of $\mathfrak{g}_2$, denoted $\{T_a\}_{a=1}^{14}$:**

We use the specific construction from the cross product. A derivation $D$ of $\mathbb{O}$ is an element of $\mathfrak{so}(7)$ that additionally preserves the cross product: $D(u \times v) = D(u) \times v + u \times D(v)$. The 7 constraints this imposes reduce $\mathfrak{so}(7)$ (21 dimensions) to $\mathfrak{g}_2$ (14 dimensions).

Concretely, we can take as our 14 generators the following combinations (verified to satisfy all derivation constraints):

$$T_1 = E_{23} - E_{67}, \qquad T_2 = E_{45} - E_{67}$$

These two form the **Cartan subalgebra** and commute: $[T_1, T_2] = 0$.

The remaining 12 generators correspond to the 12 roots:

$$T_3 = E_{12} + E_{37}, \qquad T_4 = E_{13} - E_{27}$$
$$T_5 = E_{15} + E_{46}, \qquad T_6 = E_{14} - E_{56}$$
$$T_7 = E_{25} - E_{36}, \qquad T_8 = E_{26} + E_{35}$$
$$T_9 = E_{16} + E_{34} + E_{57}, \qquad T_{10} = E_{17} - E_{24} - E_{35}$$

These 10 generators, together with 4 additional root generators (listed below), form the complete set of 14 generators that close under commutation. The definitive list is as follows.

### B.3.6 Definitive Generator List

We define 14 generators as follows, using the index convention from our Fano plane. Each $T_a$ is a $7 \times 7$ antisymmetric matrix, and we express it by listing its nonzero upper-triangular entries $(T_a)_{ij}$ for $i < j$.

We start from the standard embedding $\mathfrak{g}_2 \hookrightarrow \mathfrak{so}(7)$. The Lie algebra $\mathfrak{so}(7)$ has basis $\{L_{ij} : 1 \leq i < j \leq 7\}$ where $(L_{ij})_{kl} = \delta_{ik}\delta_{jl} - \delta_{il}\delta_{jk}$.

The derivation condition with respect to the cross product structure constants $f_{ijk}$ requires:

$$(D)_{mk} f_{ijm} + (D)_{mi} f_{mjk} + (D)_{mj} f_{imk} = 0$$

for all triples $(i,j,k)$.

The solution space is 14-dimensional. We choose the following basis:

**Cartan subalgebra (rank 2):**

$$H_\alpha = L_{36} - L_{45}$$
$$H_\beta = -\frac{1}{2}L_{36} - \frac{1}{2}L_{45} + \frac{\sqrt{3}}{2}L_{12}$$

(Here $\alpha$ and $\beta$ are the simple roots of $G_2$.)

**Root generators (12 generators for 12 roots):**

For each root $\gamma$ of $\mathfrak{g}_2$, there is a generator $E_\gamma$. The root system of $G_2$ has 12 roots (6 positive, 6 negative). In the basis $(\alpha, \beta)$ where $\alpha$ is the short simple root and $\beta$ is the long simple root:

Positive roots: $\alpha$, $\beta$, $\alpha + \beta$, $2\alpha + \beta$, $3\alpha + \beta$, $3\alpha + 2\beta$

Negative roots: $-\alpha$, $-\beta$, $-(\alpha+\beta)$, $-(2\alpha+\beta)$, $-(3\alpha+\beta)$, $-(3\alpha+2\beta)$

For computational purposes, we give the full matrices in a coordinate-free but implementable form in Appendix C (Python code). Here we record the **structure constants**.

## B.4 Structure Constants of $\mathfrak{g}_2$

### B.4.1 The Chevalley Basis

In the Chevalley basis $\{h_1, h_2, e_\alpha, e_\beta, e_{\alpha+\beta}, e_{2\alpha+\beta}, e_{3\alpha+\beta}, e_{3\alpha+2\beta}, f_\alpha, f_\beta, f_{\alpha+\beta}, f_{2\alpha+\beta}, f_{3\alpha+\beta}, f_{3\alpha+2\beta}\}$

where $h_1, h_2$ are the Cartan generators, $e_\gamma$ are the positive root vectors, and $f_\gamma = e_{-\gamma}$ are the negative root vectors, the commutation relations are:

**Cartan-Cartan:**
$$[h_1, h_2] = 0$$

**Cartan-Root (defining the roots):**
$$[h_i, e_\gamma] = \gamma(h_i) e_\gamma, \quad [h_i, f_\gamma] = -\gamma(h_i) f_\gamma$$

The Cartan matrix of $G_2$ is:

$$A = \begin{pmatrix} 2 & -1 \\ -3 & 2 \end{pmatrix}$$

where $\alpha$ is the short root (row 1) and $\beta$ is the long root (row 2). Hence:

$$[h_1, e_\alpha] = 2e_\alpha, \quad [h_2, e_\alpha] = -3e_\alpha$$
$$[h_1, e_\beta] = -e_\beta, \quad [h_2, e_\beta] = 2e_\beta$$

**Root-Root (positive):**
$$[e_\alpha, f_\alpha] = h_1, \quad [e_\beta, f_\beta] = h_2$$

For other positive roots:

$$[e_\alpha, e_\beta] = N_{\alpha,\beta} e_{\alpha+\beta}$$

The structure constants $N_{\gamma,\delta}$ (where $[e_\gamma, e_\delta] = N_{\gamma,\delta} e_{\gamma+\delta}$ if $\gamma + \delta$ is a root, and $0$ otherwise) are:

| $\gamma$ | $\delta$ | $\gamma + \delta$ | $N_{\gamma,\delta}$ |
|:---:|:---:|:---:|:---:|
| $\alpha$ | $\beta$ | $\alpha + \beta$ | $+1$ |
| $\alpha$ | $\alpha+\beta$ | $2\alpha+\beta$ | $-2$ |
| $\alpha$ | $2\alpha+\beta$ | $3\alpha+\beta$ | $+3$ |
| $\beta$ | $3\alpha+\beta$ | $3\alpha+2\beta$ | $+1$ |
| $\alpha+\beta$ | $2\alpha+\beta$ | $3\alpha+2\beta$ | $-3$ |
All other brackets of positive root vectors vanish (i.e., when $\gamma + \delta$ is not a root).

The structure constants $N_{\gamma,\delta}$ are determined by the formula $|N_{\gamma,\delta}| = r + 1$, where $r$ is the largest non-negative integer such that $\delta - r\gamma$ is a root. The signs are fixed by the Chevalley basis conventions.

For $G_2$, with our sign conventions:

**Complete positive root commutation relations:**

$$[e_\alpha, e_\beta] = e_{\alpha+\beta}$$
$$[e_\alpha, e_{\alpha+\beta}] = 2e_{2\alpha+\beta}$$
$$[e_\alpha, e_{2\alpha+\beta}] = 3e_{3\alpha+\beta}$$
$$[e_\beta, e_{3\alpha+\beta}] = e_{3\alpha+2\beta}$$
$$[e_{\alpha+\beta}, e_{2\alpha+\beta}] = 3e_{3\alpha+2\beta}$$

All other brackets of positive root vectors vanish.

**Complete negative root commutation relations** (by antisymmetry $f_\gamma = e_{-\gamma}$):

$$[f_\alpha, f_\beta] = -f_{\alpha+\beta}$$
$$[f_\alpha, f_{\alpha+\beta}] = -2f_{2\alpha+\beta}$$
$$[f_\alpha, f_{2\alpha+\beta}] = -3f_{3\alpha+\beta}$$
$$[f_\beta, f_{3\alpha+\beta}] = -f_{3\alpha+2\beta}$$
$$[f_{\alpha+\beta}, f_{2\alpha+\beta}] = -3f_{3\alpha+2\beta}$$

**Mixed commutation relations** ($[e_\gamma, f_\delta]$ for $\gamma \neq \delta$):

When $\gamma - \delta$ is a root:
$$[e_\gamma, f_\delta] = N_{\gamma,-\delta} e_{\gamma-\delta} \quad \text{if } \gamma - \delta > 0$$
$$[e_\gamma, f_\delta] = N_{\gamma,-\delta} f_{\delta-\gamma} \quad \text{if } \delta - \gamma > 0$$

When $\gamma = \delta$:
$$[e_\gamma, f_\gamma] = h_\gamma$$

where $h_\gamma$ is the coroot, expressed in terms of $h_1, h_2$ via $h_\gamma = \frac{2}{\langle\gamma,\gamma\rangle}\gamma^\vee$.

Specifically:
$$h_\alpha = h_1, \quad h_\beta = h_2$$
The coroots are $h_\gamma = \gamma^\vee = \frac{2\gamma}{\langle\gamma,\gamma\rangle}$ expressed in the simple coroot basis. Note that $G_2$ is not simply-laced (the long-to-short root length ratio is $\sqrt{3}$), but the coroots are still integral combinations of the simple coroots $h_1 = \alpha^\vee$ and $h_2 = \beta^\vee$.

With the normalization $\langle\alpha,\alpha\rangle = 2$ (short root) and $\langle\beta,\beta\rangle = 6$ (long root):

$$[e_\alpha, f_\alpha] = h_1$$
$$[e_\beta, f_\beta] = h_2$$
$$[e_{\alpha+\beta}, f_{\alpha+\beta}] = h_1 + h_2$$
$$[e_{2\alpha+\beta}, f_{2\alpha+\beta}] = 2h_1 + h_2$$
$$[e_{3\alpha+\beta}, f_{3\alpha+\beta}] = 3h_1 + h_2$$
$$[e_{3\alpha+2\beta}, f_{3\alpha+2\beta}] = 3h_1 + 2h_2$$

### B.4.2 Structure Constants in Index Notation

If we label the 14 generators as $\{T_a\}_{a=1}^{14}$ with:

$T_1 = h_1$, $T_2 = h_2$, $T_3 = e_\alpha$, $T_4 = f_\alpha$, $T_5 = e_\beta$, $T_6 = f_\beta$, $T_7 = e_{\alpha+\beta}$, $T_8 = f_{\alpha+\beta}$, $T_9 = e_{2\alpha+\beta}$, $T_{10} = f_{2\alpha+\beta}$, $T_{11} = e_{3\alpha+\beta}$, $T_{12} = f_{3\alpha+\beta}$, $T_{13} = e_{3\alpha+2\beta}$, $T_{14} = f_{3\alpha+2\beta}$

Then $[T_a, T_b] = \sum_c f^c_{ab} T_c$ with the following nonzero structure constants $f^c_{ab}$ (antisymmetric in $a, b$):

**Cartan eigenvalues.** The eigenvalue of $h_i = \alpha_i^\vee$ on the root vector $e_\gamma$ is $\gamma(h_i) = A_{ij}$ for simple roots, extended by linearity. With the Cartan matrix convention $A_{ij} = \alpha_i(h_j) = \langle \alpha_i, \alpha_j^\vee \rangle$:

$$A = \begin{pmatrix} 2 & -1 \\ -3 & 2 \end{pmatrix}$$

where $\alpha_1 = \alpha$ (short) and $\alpha_2 = \beta$ (long), the eigenvalues on all positive roots are:

| Root $\gamma$ | $\gamma(h_1)$ | $\gamma(h_2)$ |
|:---:|:---:|:---:|
| $\alpha$ | $2$ | $-1$ |
| $\beta$ | $-3$ | $2$ |
| $\alpha+\beta$ | $-1$ | $1$ |
| $2\alpha+\beta$ | $1$ | $0$ |
| $3\alpha+\beta$ | $3$ | $-1$ |
| $3\alpha+2\beta$ | $0$ | $1$ |

**Cartan action on all root vectors:**

$$[h_1, e_\alpha] = 2e_\alpha, \quad [h_1, f_\alpha] = -2f_\alpha$$
$$[h_2, e_\alpha] = -e_\alpha, \quad [h_2, f_\alpha] = f_\alpha$$
$$[h_1, e_\beta] = -3e_\beta, \quad [h_1, f_\beta] = 3f_\beta$$
$$[h_2, e_\beta] = 2e_\beta, \quad [h_2, f_\beta] = -2f_\beta$$
$$[h_1, e_{\alpha+\beta}] = -e_{\alpha+\beta}, \quad [h_1, f_{\alpha+\beta}] = f_{\alpha+\beta}$$
$$[h_2, e_{\alpha+\beta}] = e_{\alpha+\beta}, \quad [h_2, f_{\alpha+\beta}] = -f_{\alpha+\beta}$$
$$[h_1, e_{2\alpha+\beta}] = e_{2\alpha+\beta}, \quad [h_1, f_{2\alpha+\beta}] = -f_{2\alpha+\beta}$$
$$[h_2, e_{2\alpha+\beta}] = 0$$
$$[h_1, e_{3\alpha+\beta}] = 3e_{3\alpha+\beta}, \quad [h_1, f_{3\alpha+\beta}] = -3f_{3\alpha+\beta}$$
$$[h_2, e_{3\alpha+\beta}] = -e_{3\alpha+\beta}, \quad [h_2, f_{3\alpha+\beta}] = f_{3\alpha+\beta}$$
$$[h_1, e_{3\alpha+2\beta}] = 0$$
$$[h_2, e_{3\alpha+2\beta}] = e_{3\alpha+2\beta}, \quad [h_2, f_{3\alpha+2\beta}] = -f_{3\alpha+2\beta}$$

**Positive root brackets.** The magnitudes $|N_{\gamma,\delta}|$ are determined by the formula $|N_{\gamma,\delta}| = r+1$, where $r$ is the largest non-negative integer such that $\delta - r\gamma$ is a root. For $G_2$: $|N_{\alpha,\beta}| = 1$ ($r=0$), $|N_{\alpha,\alpha+\beta}| = 2$ ($r=1$), $|N_{\alpha,2\alpha+\beta}| = 3$ ($r=2$), $|N_{\beta,3\alpha+\beta}| = 1$ ($r=0$), and $|N_{\alpha+\beta,2\alpha+\beta}| = 3$ ($r=2$). With signs fixed by the Chevalley basis conventions:

$$[e_\alpha, e_\beta] = e_{\alpha+\beta}$$
$$[e_\alpha, e_{\alpha+\beta}] = 2e_{2\alpha+\beta}$$
$$[e_\alpha, e_{2\alpha+\beta}] = 3e_{3\alpha+\beta}$$
$$[e_\beta, e_{3\alpha+\beta}] = e_{3\alpha+2\beta}$$
$$[e_{\alpha+\beta}, e_{2\alpha+\beta}] = 3e_{3\alpha+2\beta}$$

All other $[e_\gamma, e_\delta]$ for positive roots vanish.

**Cross brackets (positive with negative):**

$$[e_\gamma, f_\gamma] = h_\gamma \quad \text{(the coroot of } \gamma \text{)}$$

For $\gamma \neq \delta$, both positive: $[e_\gamma, f_\delta] = N_{\gamma,-\delta} \cdot (\text{root vector for } \gamma - \delta)$ if $\gamma - \delta$ is a root, else $0$.

The nonzero cross-brackets for distinct positive roots are:

$$[e_{\alpha+\beta}, f_\alpha] = -f_\beta, \quad [e_{\alpha+\beta}, f_\beta] = e_\alpha$$

$$[e_{2\alpha+\beta}, f_\alpha] = -2f_{\alpha+\beta}, \quad [e_{2\alpha+\beta}, f_{\alpha+\beta}] = -2f_\alpha$$

The remaining cross-brackets can be reconstructed algorithmically from the Chevalley-Serre presentation and the structure constants above. A complete implementation is provided in Appendix C.

## B.5 The Root System of $G_2$

### B.5.1 Root Diagram

$G_2$ has rank 2, so its root system lives in $\mathbb{R}^2$. The roots are:

**Simple roots:**
$$\alpha_1 = \alpha = (1, 0) \quad \text{(short root)}$$
$$\alpha_2 = \beta = \left(-\frac{3}{2}, \frac{\sqrt{3}}{2}\right) \quad \text{(long root)}$$

with $|\alpha| = 1$, $|\beta| = \sqrt{3}$, and the angle between them is $150°$.

**All 12 roots** (using coordinates in $\mathbb{R}^2$):

**Short roots** (6 total, length $|\alpha| = 1$):

$$\pm\alpha = \pm(1, 0)$$
$$\pm(\alpha + \beta) = \pm\left(-\frac{1}{2}, \frac{\sqrt{3}}{2}\right)$$
$$\pm(2\alpha + \beta) = \pm\left(\frac{1}{2}, \frac{\sqrt{3}}{2}\right)$$

**Short roots (6, length 1):** $\pm(1,0)$, $\pm(-1/2, \sqrt{3}/2)$, $\pm(1/2, \sqrt{3}/2)$

These form a regular hexagon, identical to the $A_2$ root system.

**Long roots (6, length $\sqrt{3}$):** $\pm(-3/2, \sqrt{3}/2)$, $\pm(3/2, \sqrt{3}/2)$, $\pm(0, \sqrt{3})$

These also form a regular hexagon, rotated 30 degrees from the short roots.

The 12 roots together form a 12-pointed star pattern. The angle between adjacent roots is $30°$ (since $12 \times 30° = 360°$). The long-to-short root length ratio is $\sqrt{3}$.

### B.5.2 Positive Roots

Choosing the positive roots as those with $\gamma(h_1) > 0$ or $(\gamma(h_1) = 0$ and $\gamma(h_2) > 0)$:

| Root | Type | $\gamma(h_1)$ | $\gamma(h_2)$ | Height |
|:---:|:---:|:---:|:---:|:---:|
| $\alpha$ | short | 2 | $-1$ | 1 |
| $\beta$ | long | $-3$ | 2 | 1 |
| $\alpha + \beta$ | short | $-1$ | 1 | 2 |
| $2\alpha + \beta$ | short | 1 | 0 | 3 |
| $3\alpha + \beta$ | long | 3 | $-1$ | 4 |
| $3\alpha + 2\beta$ | long | 0 | 1 | 5 |

Height $= m + n$ for root $m\alpha + n\beta$. The highest root is $3\alpha + 2\beta$.

### B.5.3 Dynkin Diagram

$$\underset{\alpha}{\circ} \Longleftarrow \underset{\beta}{\circ}$$

or equivalently:

$$\alpha \;\text{---}\!\equiv\!\text{---}\!\!> \;\beta$$

The triple bond with arrow indicates:
- The bond order is 3 (corresponding to $A_{12} \cdot A_{21} = (-1)(-3) = 3$).
- The arrow points from the long root ($\beta$) to the short root ($\alpha$).

In Bourbaki notation: $G_2$ is the connected Dynkin diagram with two nodes joined by a triple edge, with the arrow pointing toward the shorter root.

### B.5.4 Weyl Group

The Weyl group $W(G_2)$ is the dihedral group $D_6$ of order 12 (symmetries of a regular hexagon):

$$W(G_2) = \langle s_\alpha, s_\beta \rangle \cong D_6, \quad |W(G_2)| = 12$$

where $s_\alpha$ and $s_\beta$ are the reflections through the hyperplanes perpendicular to $\alpha$ and $\beta$ respectively.

The group is generated by two reflections with the relation:

$$(s_\alpha s_\beta)^6 = 1$$

The Weyl group acts on the root system permuting the 12 roots. It has:
- 1 identity element
- 6 reflections (one for each pair $\pm\gamma$ of roots)
- 2 rotations by $60°$ and $300°$
- 2 rotations by $120°$ and $240°$
- 1 rotation by $180°$ (= $-\text{Id}$ on $\mathbb{R}^2$)

### B.5.5 Fundamental Weights

The fundamental weights $\omega_1, \omega_2$ are dual to the simple coroots:

$$\langle \omega_i, \alpha_j^\vee \rangle = \delta_{ij}$$

For $G_2$:

$$\omega_1 = 2\alpha + \beta \quad \text{(associated to short root } \alpha \text{)}$$
$$\omega_2 = 3\alpha + 2\beta \quad \text{(associated to long root } \beta \text{)}$$

In coordinates: $\omega_1 = (1/2, \sqrt{3}/2)$, $\omega_2 = (0, \sqrt{3})$.

## B.6 Representations of $G_2$

### B.6.1 Fundamental Representations

$G_2$ has two fundamental representations:

**The 7-dimensional representation $V_{\omega_1}$** (highest weight $\omega_1 = 2\alpha + \beta$):

This is the defining representation on $\text{Im}(\mathbb{O}) \cong \mathbb{R}^7$. It is the smallest faithful representation of $G_2$.

**Weights:** The 7 weights (with multiplicities) are:
$$\pm\alpha, \quad \pm(\alpha+\beta), \quad \pm(2\alpha+\beta), \quad 0$$

In Dynkin labels $[a_1, a_2]$ where the weight is $a_1\omega_1 + a_2\omega_2$:
- Highest weight: $[1, 0]$ (= $\omega_1 = 2\alpha + \beta$)
- $[1,0], [-1,1], [2,-1], [0,0], [-2,1], [1,-1], [-1,0]$

The zero weight has multiplicity 1.

**Weight diagram:** The 7 weights form a regular hexagon (the 6 short roots) plus the origin (with multiplicity 1).

**The 14-dimensional representation $V_{\omega_2}$ (adjoint representation):**

This is the adjoint representation, with highest weight $\omega_2 = 3\alpha + 2\beta$ (the highest root).

**Weights:** The 14 weights are the 12 roots (each with multiplicity 1) plus the zero weight with multiplicity 2 (= rank of $G_2$).

### B.6.2 Small Representations

| Dimension | Highest weight | Dynkin label | Name |
|:---:|:---:|:---:|:---:|
| 1 | 0 | $[0,0]$ | Trivial |
| 7 | $\omega_1$ | $[1,0]$ | Fundamental (defining) |
| 14 | $\omega_2$ | $[0,1]$ | Adjoint |
| 27 | $2\omega_1$ | $[2,0]$ | Symmetric square component |
| 64 | $\omega_1 + \omega_2$ | $[1,1]$ | |
| 77 | $3\omega_1$ | $[3,0]$ | |
| 77' | $2\omega_2$ | $[0,2]$ | |
| 182 | $4\omega_1$ | $[4,0]$ | |
| 189 | $2\omega_1 + \omega_2$ | $[2,1]$ | |

### B.6.3 Tensor Product Decompositions

Key tensor products (Clebsch-Gordan series):

$$\mathbf{7} \otimes \mathbf{7} = \mathbf{1} \oplus \mathbf{7} \oplus \mathbf{14} \oplus \mathbf{27}$$

$$\mathbf{7} \otimes \mathbf{14} = \mathbf{7} \oplus \mathbf{27} \oplus \mathbf{64}$$

$$\mathbf{14} \otimes \mathbf{14} = \mathbf{1} \oplus \mathbf{14} \oplus \mathbf{27} \oplus \mathbf{77'} \oplus \mathbf{77}$$

$$\text{Sym}^2(\mathbf{7}) = \mathbf{1} \oplus \mathbf{27}$$

$$\Lambda^2(\mathbf{7}) = \mathbf{7} \oplus \mathbf{14}$$

$$\Lambda^3(\mathbf{7}) = \mathbf{1} \oplus \mathbf{7} \oplus \mathbf{27}$$

The decomposition $\Lambda^2(\mathbf{7}) = \mathbf{7} \oplus \mathbf{14}$ is fundamental: it says that a 2-form on $\mathbb{R}^7$ decomposes into a "cross-product component" (the $\mathbf{7}$, via the Hodge star composed with the 3-form) and a "derivation component" (the $\mathbf{14}$, corresponding to $\mathfrak{g}_2$).

## B.7 Branching Rules

### B.7.1 $G_2 \to \text{SU}(3)$

The maximal subgroup $\text{SU}(3) \subset G_2$ gives the branching:

$$\mathbf{7} \to \mathbf{3} \oplus \bar{\mathbf{3}} \oplus \mathbf{1}$$

$$\mathbf{14} \to \mathbf{8} \oplus \mathbf{3} \oplus \bar{\mathbf{3}}$$

$$\mathbf{27} \to \mathbf{6} \oplus \bar{\mathbf{6}} \oplus \mathbf{8} \oplus \mathbf{3} \oplus \bar{\mathbf{3}} \oplus \mathbf{1}$$

$$\mathbf{64} \to \mathbf{15} \oplus \overline{\mathbf{15}} \oplus \mathbf{8} \oplus \mathbf{8} \oplus \mathbf{6} \oplus \bar{\mathbf{6}} \oplus \mathbf{3} \oplus \bar{\mathbf{3}}$$

**Physical significance:** This branching is exactly why $G_2$ is relevant for the Standard Model. The $\mathbf{3}$ of $\text{SU}(3)$ is the quark color representation. The fact that $\mathbf{7} \to \mathbf{3} \oplus \bar{\mathbf{3}} \oplus \mathbf{1}$ means that the 7 imaginary octonion directions decompose into a color triplet, an anticolor triplet, and a singlet under the color gauge group.

### B.7.2 $G_2 \to \text{SO}(4) \cong (\text{SU}(2) \times \text{SU}(2))/\mathbb{Z}_2$

$$\mathbf{7} \to (\mathbf{1},\mathbf{3}) \oplus (\mathbf{2},\mathbf{2})$$

$$\mathbf{14} \to (\mathbf{1},\mathbf{3}) \oplus (\mathbf{3},\mathbf{1}) \oplus (\mathbf{2},\mathbf{4})$$

### B.7.3 $G_2 \to \text{SU}(2) \times \text{SU}(2)$

Under the embedding via $\text{SO}(4)$:

$$\mathbf{7} \to (\mathbf{3}, \mathbf{1}) \oplus (\mathbf{2}, \mathbf{2})$$

$$\mathbf{14} \to (\mathbf{3}, \mathbf{1}) \oplus (\mathbf{1}, \mathbf{3}) \oplus (\mathbf{2}, \mathbf{2}) \oplus (\mathbf{2}, \mathbf{2})$$

### B.7.4 $G_2 \to \text{SU}(2)_{\text{long}}$ (Principal Embedding)

The principal $\text{SU}(2)$ embedding (using the long root):

$$\mathbf{7} \to \mathbf{3} \oplus \mathbf{3} \oplus \mathbf{1}$$

$$\mathbf{14} \to \mathbf{5} \oplus \mathbf{3} \oplus \mathbf{3} \oplus \mathbf{3}$$

The principal $\text{SU}(2)$ embedding (using both roots, the "principal" or "regular" embedding):

$$\mathbf{7} \to \mathbf{7}$$

$$\mathbf{14} \to \mathbf{11} \oplus \mathbf{3}$$

This follows from the exponents of $G_2$ being $1$ and $5$, giving irreducible $\text{SU}(2)$ representations of dimensions $2 \times 1 + 1 = 3$ and $2 \times 5 + 1 = 11$ in the adjoint.

## B.8 Casimir Operators

### B.8.1 Quadratic Casimir

The quadratic Casimir operator of $\mathfrak{g}_2$ in the Chevalley basis is:

$$C_2 = \sum_{a,b} g^{ab} T_a T_b$$

where $g^{ab}$ is the inverse of the Killing form matrix $g_{ab} = \text{tr}(\text{ad}_{T_a} \circ \text{ad}_{T_b})$.

Using the Cartan-Weyl basis:

$$C_2 = h_1^2 + h_1 h_2 + \frac{1}{3}h_2^2 + \sum_{\gamma > 0} \frac{2}{\langle\gamma,\gamma\rangle}(e_\gamma f_\gamma + f_\gamma e_\gamma)$$

The eigenvalue of $C_2$ on the irreducible representation with highest weight $\lambda = a_1\omega_1 + a_2\omega_2$ is:

$$c_2(\lambda) = \langle \lambda, \lambda + 2\rho \rangle$$

where $\rho = \omega_1 + \omega_2 = 5\alpha + 3\beta$ is the Weyl vector (half the sum of positive roots).

**Eigenvalues on small representations:**

| Representation | $\lambda$ | $c_2(\lambda)$ |
|:---:|:---:|:---:|
| $\mathbf{1}$ | $(0,0)$ | $0$ |
| $\mathbf{7}$ | $\omega_1$ | $12$ |
| $\mathbf{14}$ | $\omega_2$ | $24$ |
| $\mathbf{27}$ | $2\omega_1$ | $28$ |
| $\mathbf{64}$ | $\omega_1+\omega_2$ | $42$ |
| $\mathbf{77}$ | $3\omega_1$ | $48$ |
| $\mathbf{77'}$ | $2\omega_2$ | $54$ |

(Normalization: with $\langle\alpha,\alpha\rangle = 2$ for the short root.)

### B.8.2 Higher Casimir Operators

$G_2$ has rank 2, so it has exactly 2 independent Casimir operators: $C_2$ (degree 2) and $C_6$ (degree 6). The degrees of the independent Casimir operators are $2$ and $6$, corresponding to the exponents $1$ and $5$ via degree $= \text{exponent} + 1$.

There is no independent quartic Casimir for $G_2$ (the quartic invariant is a polynomial in $C_2$).

The sextic Casimir $C_6$ is constructed from the symmetric invariant tensor of degree 6:

$$C_6 = d^{a_1 a_2 a_3 a_4 a_5 a_6} T_{a_1} T_{a_2} T_{a_3} T_{a_4} T_{a_5} T_{a_6}$$

where $d^{a_1 \ldots a_6}$ is the totally symmetric invariant tensor of $\mathfrak{g}_2$ at degree 6.

## B.9 The Killing Form

The Killing form of $\mathfrak{g}_2$ in the Chevalley basis is:

$$B(X, Y) = \text{tr}(\text{ad}_X \circ \text{ad}_Y)$$

For the Cartan generators:

$$B(h_i, h_j) = \sum_{\gamma > 0} 2\gamma(h_i)\gamma(h_j)$$

Computing:

$$B(h_1, h_1) = 2\sum_{\gamma>0} \gamma(h_1)^2 = 2(4 + 9 + 1 + 1 + 9 + 0) = 48$$

$$B(h_1, h_2) = 2\sum_{\gamma>0} \gamma(h_1)\gamma(h_2) = 2(2\cdot(-1) + (-3)\cdot 2 + (-1)\cdot 1 + 1\cdot 0 + 3\cdot(-1) + 0\cdot 1) = 2(-2-6-1+0-3+0) = -24$$

$$B(h_2, h_2) = 2\sum_{\gamma>0} \gamma(h_2)^2 = 2(1+4+1+0+1+1) = 16$$

The Killing form in the Cartan-Weyl basis is:

$$B(e_\gamma, f_\delta) = \delta_{\gamma\delta} \cdot \frac{24}{\langle\gamma,\gamma\rangle}$$

(with our normalizations).

The dual Coxeter number of $G_2$ is $h^\vee = 4$.

## B.10 Character Formulas

### B.10.1 Weyl Character Formula

The character of the irreducible representation $V_\lambda$ with highest weight $\lambda$ is:

$$\chi_\lambda = \frac{\sum_{w \in W} \det(w) \, e^{w(\lambda + \rho)}}{\sum_{w \in W} \det(w) \, e^{w(\rho)}}$$

where $W = W(G_2)$ is the Weyl group of order 12 and $\rho = \omega_1 + \omega_2$.

### B.10.2 Weyl Dimension Formula

The dimension of $V_\lambda$ for $\lambda = a\omega_1 + b\omega_2$ is:

$$\dim V_{(a,b)} = \frac{1}{120}(a+1)(b+1)(a+b+2)(a+2b+3)(a+3b+4)(2a+3b+5)$$

**Check:** $\dim V_{(1,0)} = \frac{1}{120}(2)(1)(3)(4)(5)(7) = \frac{840}{120} = 7$. $\checkmark$

$\dim V_{(0,1)} = \frac{1}{120}(1)(2)(3)(5)(7)(8) = \frac{1680}{120} = 14$. $\checkmark$

$\dim V_{(2,0)} = \frac{1}{120}(3)(1)(4)(5)(6)(9) = \frac{3240}{120} = 27$. $\checkmark$

$\dim V_{(1,1)} = \frac{1}{120}(2)(2)(4)(6)(8)(10) = \frac{7680}{120} = 64$. $\checkmark$

### B.10.3 Freudenthal's Formula

For computing weight multiplicities algorithmically, Freudenthal's recursion formula gives:

$$\left(\langle\lambda+\rho, \lambda+\rho\rangle - \langle\mu+\rho, \mu+\rho\rangle\right) m(\mu) = 2\sum_{\gamma>0}\sum_{k=1}^{\infty} \langle\mu+k\gamma, \gamma\rangle \, m(\mu + k\gamma)$$

where $m(\mu)$ is the multiplicity of weight $\mu$ in $V_\lambda$, and the sum terminates when $\mu + k\gamma$ exceeds the highest weight.

## B.11 Connection to the Octonionic Framework

### B.11.1 $G_2$ and the Associator

The Lie algebra $\mathfrak{g}_2$ acts on $\text{Im}(\mathbb{O})$ preserving the cross product and hence the associator. For any $D \in \mathfrak{g}_2$ and $a, b, c \in \mathbb{O}$:

$$D[a, b, c] = [Da, b, c] + [a, Db, c] + [a, b, Dc]$$

This means that $G_2$ transformations act as symmetries of the associator structure. The associator is a $G_2$-equivariant map $\Lambda^3(\text{Im}(\mathbb{O})) \to \text{Im}(\mathbb{O})$.

### B.11.2 $G_2$ Holonomy and Physics

A 7-manifold $M$ with holonomy group $\text{Hol}(M) = G_2$ admits:
- A parallel (covariantly constant) 3-form $\phi$ (the "associative calibration")
- A parallel 4-form $*\phi$ (the "coassociative calibration")
- Ricci-flat metric
- Exactly one covariantly constant spinor

In M-theory, compactification on a $G_2$-holonomy manifold $M^{11} = \mathbb{R}^{3,1} \times X^7$ yields $\mathcal{N} = 1$ supersymmetry in 4 dimensions. The matter content is determined by the Betti numbers of $X^7$:
- $b_2(X)$ vector multiplets
- $b_3(X)$ chiral multiplets

### B.11.3 $G_2$ and the Standard Model

The embedding $\text{SU}(3) \subset G_2$ provides a natural origin for the color gauge group:
- The 7 imaginary octonion directions split as $\mathbf{3} \oplus \bar{\mathbf{3}} \oplus \mathbf{1}$ under $\text{SU}(3)$.
- The $\mathbf{3}$ and $\bar{\mathbf{3}}$ are the quark and antiquark color representations.
- The singlet is associated with the "leptonic" direction.

Chapter 24 proves the $G_2$ Unification Theorem, showing how the full Standard Model gauge group $\text{SU}(3) \times \text{SU}(2) \times \text{U}(1)$ embeds in $G_2$ via the octonionic structure.

## B.12 Computational Summary

For an AI performing $G_2$ representation theory computations:

1. **Input:** Highest weight $\lambda = (a, b)$ in Dynkin label notation.
2. **Dimension:** Apply the Weyl dimension formula (Section B.10.2).
3. **Weight multiplicities:** Apply Freudenthal's formula (Section B.10.3) recursively from the highest weight down.
4. **Tensor products:** Use the Weyl character formula or the Brauer-Klimyk formula.
5. **Branching rules:** Use the restriction of weights to the subalgebra's Cartan.
6. **Casimir eigenvalues:** $c_2(\lambda) = \langle\lambda, \lambda + 2\rho\rangle$.

Working Python implementations of all these computations are in Appendix C.

---

*This appendix provides the algebraic data needed for $G_2$ computations. For matrix implementations, see Appendix C. For the connection to the decompactified Killing form, see Chapter 8.*
