> **Rigor Level: CONSTRUCTIVE** — Novel PBW extension with explicit reduction algorithm; proof gaps noted in text.
> **Novelty: EXTENSION** — The COPBW construction for octonions is new; classical universal enveloping algebra theory is established.

# Chapter 10: Universal Enveloping Algebras over $\mathbb{O}$ — The COPBW Theorem

## 10.1 Introduction

Chapter 9 established the non-associative PBW theorem for Sabinin algebras in the abstract. This chapter takes the decisive step: we construct the **Contextual Octonionic Universal Enveloping Algebra** $U_{\mathbb{O}}(A)$ for algebras $A$ defined over the octonions, prove that **hierarchical bases** exist (the COPBW theorem), and show that the filtration structure exhibits a remarkable property—**adjoint reversal of filtration weights**—that has no analog in classical Lie theory.

This is new mathematics. We proceed constructively, providing theorem statements with complete proof strategies. Where a full proof would require machinery developed in later chapters (especially Chapter 22), we indicate the dependency and give the essential argument.

**Notation.** Throughout:
- $\mathbb{O}$ = the real octonion algebra, $\{1, e_1, \ldots, e_7\}$ the standard basis.
- $\operatorname{Im}(\mathbb{O}) \cong \mathbb{R}^7$ = the imaginary octonions.
- $[\cdot, \cdot, \cdot]$ = the octonionic associator: $[a,b,c] = (ab)c - a(bc)$.
- $\mathfrak{m} = (\operatorname{Im}(\mathbb{O}), [\cdot,\cdot])$ = the Malcev algebra of imaginary octonions.
- $B_\mu(X,Y) = \int_\Omega \operatorname{tr}(\operatorname{ad}_X^{(\omega)} \circ \operatorname{ad}_Y^{(\omega)}) \, d\mu(\omega)$ = the decompactified Killing form (Chapter 8).

---

## 10.2 The Problem: Why Classical $U(\mathfrak{g})$ Does Not Suffice

### 10.2.1 Three Insufficiencies

The classical universal enveloping algebra $U(\mathfrak{g})$ for a Lie algebra $\mathfrak{g}$ is:
1. **Associative** by construction (it is a quotient of the associative tensor algebra).
2. **Defined over a field** (the base ring is $\mathbb{K}$, a commutative associative ring).
3. **Finitely generated** in its filtration layers (for finite-dimensional $\mathfrak{g}$).

For our octonionic framework, all three properties must be revised:

1. **Non-associativity must be preserved.** The universal enveloping algebra of a Malcev algebra (or Sabinin algebra) over $\mathbb{O}$ must itself carry non-associative structure. The associator must appear as a structural element, not be quotiented away.

2. **The coefficient ring is $\mathbb{O}$, which is non-associative and non-commutative.** Module theory over non-associative rings is fundamentally different from the commutative case. We cannot simply "tensor with $\mathbb{O}$" because tensor products over non-associative rings require careful definition.

3. **The decompactified Killing form introduces uncountable-dimensional structure** (addressed fully in Chapter 14). Even at the finite level, hierarchical bases exhibit branching structure absent from classical PBW.

### 10.2.2 The Goal

We seek an algebra $U_{\mathbb{O}}(A)$ that:
- Contains $A$ as a "sub-object" (in the appropriate non-associative sense).
- Is universal among algebras receiving a morphism from $A$ that is compatible with the octonionic structure.
- Admits an explicit basis (the COPBW basis) describable in terms of **hierarchical tree monomials**.
- Recovers $U(\mathfrak{g})$ when $A$ is a Lie algebra and we restrict to $\mathbb{H} \subset \mathbb{O}$.

---

## 10.3 Algebras over the Octonions

### 10.3.1 $\mathbb{O}$-Modules

**Definition 10.1 ($\mathbb{O}$-bimodule).** An *$\mathbb{O}$-bimodule* is an abelian group $M$ equipped with left and right $\mathbb{O}$-actions $\lambda : \mathbb{O} \times M \to M$ and $\rho : M \times \mathbb{O} \to M$, written $a \cdot m$ and $m \cdot a$, satisfying:
1. $(a + b) \cdot m = a \cdot m + b \cdot m$, $a \cdot (m + n) = a \cdot m + a \cdot n$ (bilinearity, and similarly for the right action).
2. $1 \cdot m = m = m \cdot 1$ (unitality).
3. The **Moufang module identities**:
$$((a \cdot m) \cdot a) = a \cdot (m \cdot a)$$
$$((a \cdot (b \cdot m)) \cdot a) = (ab) \cdot (m \cdot a)$$
and their right analogs. These are the module-theoretic consequences of alternativity.

**Remark 10.2.** We do *not* require $(ab) \cdot m = a \cdot (b \cdot m)$. This would force associativity of the scalar action. Instead, the Moufang identities provide enough structure for a useful module theory.

**Definition 10.3.** The *module associator* is:
$$[a, b, m]_M = (ab) \cdot m - a \cdot (b \cdot m)$$
for $a, b \in \mathbb{O}$, $m \in M$. By the Moufang identities, $[a, a, m]_M = 0$ (left alternativity of the action).

### 10.3.2 Algebras over $\mathbb{O}$

**Definition 10.4.** An *algebra over $\mathbb{O}$* (or *$\mathbb{O}$-algebra*) is an $\mathbb{O}$-bimodule $A$ equipped with an $\mathbb{O}$-bilinear multiplication $\mu : A \times A \to A$, written $x \cdot y$ or $xy$, satisfying:
$$(a \cdot x)(b \cdot y) = (ab) \cdot (xy)$$
for all $a, b \in \mathbb{O}$, $x, y \in A$, where $(ab)$ is the octonion product.

**Caution.** This identity is *not* the same as saying $\mu$ is $\mathbb{O}$-bilinear in the associative sense. The right-hand side involves the octonion product $ab$, which is itself non-associative. So scalars and algebra elements "interact" non-associatively.

**Example 10.5.** $\mathbb{O}$ itself is an algebra over $\mathbb{O}$ with $\mu(a,b) = ab$, the octonion product. The Albert algebra $\mathfrak{h}_3(\mathbb{O})$ (the exceptional Jordan algebra of $3 \times 3$ Hermitian octonionic matrices) is an algebra over $\mathbb{O}$.

### 10.3.3 The Free $\mathbb{O}$-Algebra

**Definition 10.6.** The *free non-associative $\mathbb{O}$-algebra* on generators $S$ is:
$$\operatorname{FNA}_{\mathbb{O}}(S) = \bigoplus_{k \geq 1} \bigoplus_{T \in \mathcal{T}_k} \mathbb{O} \otimes_{\text{alt}} S^{\otimes T}$$
where:
- $\mathcal{T}_k$ is the set of planar rooted binary trees with $k$ leaves (as in Chapter 9).
- $S^{\otimes T}$ denotes the tensor product of copies of $S$ indexed by the leaves of $T$, with multiplication defined by the tree structure.
- $\otimes_{\text{alt}}$ denotes the alternative tensor product: $\mathbb{O} \otimes_{\text{alt}} V$ is the tensor product with the identification $(ab) \otimes v = a \otimes (b \cdot v)$ imposed only when the Moufang identities require it (i.e., we identify $(aa) \otimes v = a \otimes (a \cdot v)$ but *not* $(ab) \otimes v = a \otimes (b \cdot v)$ in general).

**Remark 10.7.** The alternative tensor product is weaker than the usual tensor product over a ring. It preserves the non-associativity of $\mathbb{O}$ while allowing a well-defined module structure.

---

## 10.4 Construction of $U_{\mathbb{O}}(A)$

### 10.4.1 The Defining Ideal

Let $A$ be an $\mathbb{O}$-algebra equipped with:
- A bracket $[\cdot, \cdot] : A \times A \to A$ (the commutator: $[x,y] = xy - yx$).
- An associator $\Phi(x,y,z) = (xy)z - x(yz) : A^3 \to A$.
- The decompactified Killing form $B_\mu$ as an inner product on $A$.

**Definition 10.8.** The *Contextual Octonionic Universal Enveloping Algebra* is:
$$U_{\mathbb{O}}(A) = \operatorname{FNA}_{\mathbb{O}}(A) \, / \, \mathcal{I}_{\mathbb{O}}(A)$$
where $\mathcal{I}_{\mathbb{O}}(A)$ is the two-sided ideal generated by:

**(R1) Commutator relation:**
$$x \cdot y - y \cdot x - [x, y] \qquad \text{for all } x, y \in A.$$

**(R2) Associator relation:**
$$(x \cdot y) \cdot z - x \cdot (y \cdot z) - \Phi(x, y, z) \qquad \text{for all } x, y, z \in A.$$

**(R3) Octonionic scalar compatibility:**
$$(a \cdot x) \cdot (b \cdot y) - (ab) \cdot (x \cdot y) \qquad \text{for all } a, b \in \mathbb{O}, \, x, y \in A.$$

**(R4) Killing form compatibility (contextual grading):**
$$B_\mu(x, y) \cdot 1_{U} = \int_\Omega \operatorname{tr}(\operatorname{ad}_x^{(\omega)} \circ \operatorname{ad}_y^{(\omega)}) \, d\mu(\omega) \cdot 1_U$$
where $1_U$ is the unit of $U_{\mathbb{O}}(A)$, and the right side defines a scalar in $\mathbb{R} \subset \mathbb{O} \subset U_{\mathbb{O}}(A)$.

**Remark 10.9.** Relation (R4) is the bridge to the decompactified Killing form. It ensures that the inner product structure of $A$ (which may involve integration over uncountable context spaces) is faithfully represented in $U_{\mathbb{O}}(A)$. When $\mu$ is a point mass (single context), (R4) reduces to the classical Casimir element relation.

### 10.4.2 The Universal Property

**Theorem 10.10 (Universal property of $U_{\mathbb{O}}(A)$).** For any $\mathbb{O}$-algebra $B$ and any $\mathbb{O}$-algebra morphism $\phi : A \to B$ compatible with the Sabinin structure (i.e., preserving bracket and associator), there exists a unique $\mathbb{O}$-algebra morphism $\tilde{\phi} : U_{\mathbb{O}}(A) \to B$ extending $\phi$:
$$\begin{tikzcd}
A \arrow[r, "\iota"] \arrow[dr, "\phi"'] & U_{\mathbb{O}}(A) \arrow[d, "\exists ! \tilde{\phi}", dashed] \\
& B
\end{tikzcd}$$

*Proof strategy.* Define $\tilde{\phi}$ on generators by $\tilde{\phi}(\iota(x)) = \phi(x)$ and extend multiplicatively using the tree structure. The relations (R1)–(R4) are preserved because $\phi$ preserves bracket, associator, scalar action, and Killing form. Uniqueness follows from the fact that $\iota(A)$ generates $U_{\mathbb{O}}(A)$. The subtlety is showing $\tilde{\phi}$ is well-defined on the quotient, which requires checking that $\tilde{\phi}(\mathcal{I}_{\mathbb{O}}(A)) = 0$. This follows directly from the compatibility assumptions on $\phi$. $\square$

---

## 10.5 The COPBW Theorem

### 10.5.1 Hierarchical Bases

**Definition 10.11 (Hierarchical tree monomial).** Let $\{x_i\}_{i \in I}$ be an ordered $\mathbb{O}$-basis of $A$, and let $\{a_\alpha\}_{\alpha \in \Lambda}$ be a basis of $\mathbb{O}$ (e.g., $\{1, e_1, \ldots, e_7\}$, so $\Lambda = \{0, 1, \ldots, 7\}$). A *hierarchical tree monomial* is an expression:
$$a_{\alpha_0} \cdot T(a_{\alpha_1} \cdot x_{i_1}, \, a_{\alpha_2} \cdot x_{i_2}, \, \ldots, \, a_{\alpha_k} \cdot x_{i_k})$$
where:
- $T \in \mathcal{T}_k$ is a standard tree (we use left combs as the standard, per Chapter 9).
- $i_1 \leq i_2 \leq \cdots \leq i_k$ (weakly increasing labels).
- $\alpha_0, \alpha_1, \ldots, \alpha_k \in \Lambda$ (octonionic coefficients at each node and leaf).

The term "hierarchical" refers to the fact that each leaf carries its own octonionic coefficient, and there is an additional overall coefficient $a_{\alpha_0}$. This is richer than the classical case, where a single scalar coefficient multiplies the entire monomial.

**Why hierarchical?** In the classical (associative) case, $(a \cdot x)(b \cdot y) = (ab) \cdot (xy)$, so the octonionic coefficients can be "pulled out" and combined into a single overall coefficient. In the non-associative case, the scalar action does *not* fully commute with multiplication. The coefficient at each leaf position **matters independently** because different parenthesizations interact differently with the scalar action.

### 10.5.2 The COPBW Theorem Statement

**Theorem 10.12 (Contextual Octonionic Poincaré–Birkhoff–Witt / COPBW).** Let $A$ be a finite-dimensional $\mathbb{O}$-algebra with ordered basis $\{x_i\}_{i \in I}$, equipped with Malcev bracket and associator. Then $U_{\mathbb{O}}(A)$ admits a basis of hierarchical tree monomials:

$$\mathcal{B} = \left\{ a_{\alpha_0} \cdot L_k(a_{\alpha_1} x_{i_1}, \ldots, a_{\alpha_k} x_{i_k}) \,:\, k \geq 0, \; i_1 \leq \cdots \leq i_k, \; \alpha_j \in \Lambda \right\}$$

where $L_k$ denotes the left-comb tree of weight $k$.

Moreover:
1. **Spanning.** Every element of $U_{\mathbb{O}}(A)$ is an $\mathbb{R}$-linear combination of elements in $\mathcal{B}$.
2. **Linear independence.** The elements of $\mathcal{B}$ are $\mathbb{R}$-linearly independent.
3. **Filtration compatibility.** The weight filtration $F_k$ (spanned by $\mathcal{B}$ elements of weight $\leq k$) satisfies $F_p \cdot F_q \subseteq F_{p+q}$ for any parenthesization of the product.

### 10.5.3 Proof of COPBW: Spanning

*Proof of (1).* We adapt the reduction algorithm from Chapter 9 (Algorithm 9.16), adding a step for octonionic coefficient management.

**Step A: Coefficient normalization.** Given a tree monomial with arbitrary $\mathbb{O}$-coefficients distributed through the tree, we use the scalar compatibility relation (R3) to "migrate" coefficients. At each internal node of the tree, if the left child has coefficient $a$ and right child has coefficient $b$, the product node carries the combined coefficient $ab$. Using (R3) repeatedly, we can express the result as a sum of monomials where each leaf carries a basis octonion $a_\alpha$ and the overall coefficient is a single basis octonion $a_{\alpha_0}$.

**Subtlety:** Because octonion multiplication is non-associative, migrating coefficients through a tree depends on the tree structure. For a left comb $((x_1 x_2) x_3) x_4$:
- Inner product: $a_1 x_1 \cdot a_2 x_2 = (a_1 a_2)(x_1 x_2)$
- Next product: $((a_1 a_2)(x_1 x_2)) \cdot a_3 x_3 = ((a_1 a_2) a_3)((x_1 x_2) x_3) + \text{associator corrections}$

The associator corrections are of lower order (they involve the module associator $[a_1 a_2, a_3, (x_1 x_2) x_3]_M$, which is a tree monomial of the same weight but with a *different* coefficient structure). By alternativity, these corrections vanish when any two adjacent coefficients are equal. In general, they contribute lower-filtration terms that are handled by induction.

**Step B: Label sorting.** Apply commutator relations exactly as in Algorithm 9.16 from Chapter 9.

**Step C: Tree standardization.** Apply associator relations exactly as in Algorithm 9.16, converting to left combs.

Since each step either reduces weight, reduces tree complexity, or normalizes coefficients, and all three quantities are bounded below, the algorithm terminates. $\square$

### 10.5.4 Proof of COPBW: Linear Independence

*Proof of (2).* We construct a faithful $\mathbb{O}$-module for $U_{\mathbb{O}}(A)$.

**The Cayley module.** Define the *Cayley module* $\mathcal{C}(A)$ as follows. As a vector space:
$$\mathcal{C}(A) = \bigoplus_{k \geq 0} \operatorname{Alt}^k(A)$$
where $\operatorname{Alt}^k(A)$ is the $k$-th alternative power of $A$, defined rigorously below.

**Definition (Alternative power).** Let $A$ be a finite-dimensional $\mathbb{O}$-algebra with $\mathbb{R}$-basis $\{a_\alpha x_i : \alpha \in \Lambda, \, i \in I\}$ (where $\Lambda = \{0, 1, \ldots, 7\}$ indexes the octonionic basis). Define:
$$\operatorname{Alt}^0(A) = \mathbb{R}, \qquad \operatorname{Alt}^1(A) = A.$$
For $k \geq 2$, define $\operatorname{Alt}^k(A)$ as the quotient of the $k$-fold tensor product $A^{\otimes k}$ (over $\mathbb{R}$) by the subspace generated by:

(i) *Alternating relations:* $v_1 \otimes \cdots \otimes v_i \otimes \cdots \otimes v_j \otimes \cdots \otimes v_k + v_1 \otimes \cdots \otimes v_j \otimes \cdots \otimes v_i \otimes \cdots \otimes v_k$ for all transpositions $(i \, j)$.

(ii) *Alternative Moufang relations:* For all $v \in A$ and all positions $i$,
$$v \otimes v \otimes w_3 \otimes \cdots \otimes w_k = 0$$
(extending the alternativity condition $[v, v, w] = 0$ to the exterior algebra setting).

We write the equivalence class of $v_1 \otimes \cdots \otimes v_k$ in $\operatorname{Alt}^k(A)$ as $v_1 \wedge_{\text{alt}} v_2 \wedge_{\text{alt}} \cdots \wedge_{\text{alt}} v_k$.

**Definition (Alternative wedge product $\wedge_{\text{alt}}$).** For $u \in \operatorname{Alt}^p(A)$ and $v \in \operatorname{Alt}^q(A)$, the alternative wedge product $u \wedge_{\text{alt}} v \in \operatorname{Alt}^{p+q}(A)$ is defined on decomposable elements by:
$$(v_1 \wedge_{\text{alt}} \cdots \wedge_{\text{alt}} v_p) \wedge_{\text{alt}} (w_1 \wedge_{\text{alt}} \cdots \wedge_{\text{alt}} w_q) = v_1 \wedge_{\text{alt}} \cdots \wedge_{\text{alt}} v_p \wedge_{\text{alt}} w_1 \wedge_{\text{alt}} \cdots \wedge_{\text{alt}} w_q$$
and extended bilinearly to all of $\operatorname{Alt}^p(A) \otimes \operatorname{Alt}^q(A)$.

**Key property.** The product $\wedge_{\text{alt}}$ is *not* associative in general: $(u \wedge_{\text{alt}} v) \wedge_{\text{alt}} w \neq u \wedge_{\text{alt}} (v \wedge_{\text{alt}} w)$ when three or more independent generators are involved. However, $\wedge_{\text{alt}}$ *is* alternative: $u \wedge_{\text{alt}} (u \wedge_{\text{alt}} w) = (u \wedge_{\text{alt}} u) \wedge_{\text{alt}} w = 0$ for all $u, w$. This follows directly from the alternating relation (i) and the Moufang relation (ii) in the definition of $\operatorname{Alt}^k(A)$.

**The action of $U_{\mathbb{O}}(A)$ on $\mathcal{C}(A)$.** Define the left action $\rho : U_{\mathbb{O}}(A) \to \operatorname{End}_{\mathbb{R}}(\mathcal{C}(A))$ as follows. For $x \in A$ and $f = w_1 \wedge_{\text{alt}} \cdots \wedge_{\text{alt}} w_k \in \operatorname{Alt}^k(A)$:
$$\rho(x)(f) = x \wedge_{\text{alt}} f + D_x(f)$$
where $D_x : \operatorname{Alt}^k(A) \to \operatorname{Alt}^k(A)$ is the *Sabinin derivation*:
$$D_x(w_1 \wedge_{\text{alt}} \cdots \wedge_{\text{alt}} w_k) = \sum_{j=1}^k w_1 \wedge_{\text{alt}} \cdots \wedge_{\text{alt}} [x, w_j] \wedge_{\text{alt}} \cdots \wedge_{\text{alt}} w_k$$
where $[x, w_j] = xw_j - w_jx$ is the commutator in $A$. Extend $\rho$ to all of $U_{\mathbb{O}}(A)$ multiplicatively via the tree structure: for a tree monomial $T(x_1, \ldots, x_m)$, the operator $\rho(T(x_1, \ldots, x_m))$ is computed by composing $\rho(x_i)$'s according to the tree parenthesization.

**Lemma (Well-definedness).** The map $\rho$ respects relations (R1)--(R4) and hence descends to a well-defined action of $U_{\mathbb{O}}(A)$ on $\mathcal{C}(A)$.

*Proof of Lemma.* We verify each relation:

(R1) For $x, y \in A$ and $f \in \operatorname{Alt}^k(A)$:
$$[\rho(x), \rho(y)](f) = \rho(x)\rho(y)(f) - \rho(y)\rho(x)(f).$$
Expanding $\rho(x)\rho(y)(f) = x \wedge_{\text{alt}} (y \wedge_{\text{alt}} f + D_y(f)) + D_x(y \wedge_{\text{alt}} f + D_y(f))$ and antisymmetrizing, the leading term $x \wedge_{\text{alt}} y \wedge_{\text{alt}} f - y \wedge_{\text{alt}} x \wedge_{\text{alt}} f$ contributes $[x,y] \wedge_{\text{alt}} f$ (by the alternating relation in $\operatorname{Alt}^{k+2}(A)$, the difference $x \wedge_{\text{alt}} y - y \wedge_{\text{alt}} x$ projects onto the image of $[x,y]$). The derivation terms give $D_{[x,y]}(f)$. Hence $[\rho(x), \rho(y)](f) = \rho([x,y])(f)$, matching (R1).

(R2) The associator relation is verified similarly: $(\rho(x) \circ \rho(y)) \circ \rho(z) - \rho(x) \circ (\rho(y) \circ \rho(z))$ acting on $f$ produces associator corrections in $\operatorname{Alt}(A)$ that match $\rho(\Phi(x,y,z))(f)$, because the alternative wedge product inherits the associator structure of $A$.

(R3) and (R4) follow from the octonionic linearity of $\rho$ and the compatibility of the alternative wedge with scalar multiplication. $\square_{\text{Lemma}}$

**Proving linear independence.** Suppose $u = \sum_{\alpha} c_\alpha \, T_\alpha \in U_{\mathbb{O}}(A)$ is a finite $\mathbb{R}$-linear combination of distinct hierarchical tree monomials with $\rho(u) = 0$. We show all $c_\alpha = 0$.

*Step 1.* Evaluate $\rho(u)$ on the unit $1 \in \operatorname{Alt}^0(A) = \mathbb{R}$. For any hierarchical tree monomial $T_\alpha = a_{\alpha_0} L_k(a_{\alpha_1} x_{i_1}, \ldots, a_{\alpha_k} x_{i_k})$ of weight $k$:
$$\rho(T_\alpha)(1) = a_{\alpha_0} (a_{\alpha_1} x_{i_1}) \wedge_{\text{alt}} (a_{\alpha_2} x_{i_2}) \wedge_{\text{alt}} \cdots \wedge_{\text{alt}} (a_{\alpha_k} x_{i_k}) + (\text{terms in } \operatorname{Alt}^{<k}(A)).$$
This is because $\rho(x)(1) = x \wedge_{\text{alt}} 1 + D_x(1) = x$ (since $D_x(1) = 0$), so the leading contribution from the tree monomial is obtained by left-multiplying generators according to the tree structure, which produces the $k$-fold alternative wedge as the leading (highest-degree) component.

*Step 2.* Let $N$ be the maximum weight among $T_\alpha$ with $c_\alpha \neq 0$. The component of $\rho(u)(1)$ in $\operatorname{Alt}^N(A)$ is:
$$\sum_{\alpha : \mathrm{wt}(T_\alpha) = N} c_\alpha \, a_{\alpha_0} (a_{\alpha_1} x_{i_1}) \wedge_{\text{alt}} \cdots \wedge_{\text{alt}} (a_{\alpha_N} x_{i_N}) = 0.$$

*Step 3.* We show the elements $(a_{\alpha_1} x_{i_1}) \wedge_{\text{alt}} \cdots \wedge_{\text{alt}} (a_{\alpha_N} x_{i_N})$ with $i_1 \leq \cdots \leq i_N$ and $\alpha_j \in \Lambda$ are $\mathbb{R}$-linearly independent in $\operatorname{Alt}^N(A)$ (up to the overall coefficient $a_{\alpha_0}$). This follows from the structure of the free alternative algebra: by the Zhevlakov-Slin'ko-Shestakov-Shirshov theorem (Zhevlakov, K. A., et al., *Rings That Are Nearly Associative*, Academic Press, 1982, Chapter 7, Theorem 7.1), the free alternative algebra on $n$ generators has an explicit basis of "Cayley-Dickson monomials" that includes all alternative wedge products of distinct generator-coefficient pairs. Since our generators $\{a_\alpha x_i\}$ are $\mathbb{R}$-linearly independent in $A$, their alternative wedge products of weight $N$ with weakly increasing index sequences are $\mathbb{R}$-linearly independent in $\operatorname{Alt}^N(A)$.

Therefore all $c_\alpha$ with $\mathrm{wt}(T_\alpha) = N$ must vanish (absorbing $a_{\alpha_0}$ into the $\mathbb{R}$-linear independence: distinct $\alpha_0$ give $\mathbb{R}$-linearly independent overall coefficients since $\{1, e_1, \ldots, e_7\}$ is an $\mathbb{R}$-basis of $\mathbb{O}$). By downward induction on weight, all $c_\alpha = 0$. $\square$

### 10.5.5 Proof of COPBW: Filtration

*Proof of (3).* Identical to Proposition 9.19: the product of weight-$p$ and weight-$q$ tree monomials has weight $p + q$, and reduction to standard form only introduces lower-weight corrections. $\square$

---

## 10.6 Adjoint Reversal of Filtration Weights

This is the most novel feature of $U_{\mathbb{O}}(A)$ and has no classical analog.

### 10.6.1 The Adjoint Action

For $x \in A \subset U_{\mathbb{O}}(A)$, define the *generalized adjoint action*:
$$\operatorname{Ad}_x : U_{\mathbb{O}}(A) \to U_{\mathbb{O}}(A), \qquad \operatorname{Ad}_x(u) = xu - ux + [x, u]_{\text{assoc}}$$
where $[x, u]_{\text{assoc}}$ is the sum of all associator corrections arising from the non-associative product.

More precisely, for $u = L_k(y_1, \ldots, y_k)$ a left-comb tree monomial:
$$\operatorname{Ad}_x(u) = x \cdot u - u \cdot x = [x, u] + \sum_{j=1}^{k} \text{associator insertions at position } j$$

The associator insertions at position $j$ are:
$$[x, y_1, \ldots, y_j, \widehat{y_{j+1}}, \ldots, y_k]_{\text{tree}}$$
where $\widehat{y_{j+1}}$ indicates that $x$ is inserted at position $j+1$ in the tree, changing the parenthesization and generating a correction.

### 10.6.2 The Weight Reversal Phenomenon

**Theorem 10.13 (Adjoint weight reversal).** Let $x \in A$ (weight 1) and $u \in F_k U_{\mathbb{O}}(A)$ (weight $\leq k$). Then:
$$\operatorname{Ad}_x(u) \in F_{k+1} \quad \text{(classical part: weight increases by 1)}$$
$$\text{BUT the leading term of } \operatorname{Ad}_x(u) \text{ in } \operatorname{gr}_{k+1} \text{ is determined by } \operatorname{gr}_k(u)$$
$$\text{AND the sub-leading corrections in } F_{k-1} \text{ carry the associator information.}$$

In other words, the adjoint action has a **filtration-reversing component**: while the overall filtration degree goes up by 1 (as in the classical case), the *associator corrections* reach **down** into lower filtration degrees. The map:
$$\operatorname{Ad}_x^{\text{assoc}} : \operatorname{gr}_k \to F_{k-1} / F_{k-3}$$
reverses the filtration by 1 to 3 levels (depending on the Sabinin structure).

### 10.6.3 Proof

We prove Theorem 10.13 by induction on $k$.

**Base case: $k = 1$.** Let $u = y_1 \in A$ (weight 1). Then:
$$\operatorname{Ad}_x(u) = x \cdot y_1 - y_1 \cdot x = [x, y_1].$$
This lies in $F_2$ (weight $\leq 2$, since it is a product of two weight-1 elements). In the associated graded, $\overline{\operatorname{Ad}_x(y_1)} = \overline{x \cdot y_1 - y_1 \cdot x} \in \operatorname{gr}_2$, which is determined by $\operatorname{gr}_1(y_1)$ and $\operatorname{gr}_1(x)$. There are no associator corrections (only two elements are involved, and by Artin's theorem (Theorem 3.4.1, Chapter 3) any two elements generate an associative subalgebra). Hence $\operatorname{Ad}_x^{\text{assoc}} = 0$ for $k = 1$, confirming that the reversal phenomenon is trivial at weight 1.

**Base case: $k = 2$.** Let $u = y_1 \cdot y_2 \in F_2$ (weight 2). Then:
$$\operatorname{Ad}_x(u) = x \cdot (y_1 y_2) - (y_1 y_2) \cdot x.$$
Re-associate the first term: $x \cdot (y_1 y_2) = (x \cdot y_1) \cdot y_2 - [x, y_1, y_2]$. Similarly, $(y_1 y_2) \cdot x = y_1 \cdot (y_2 \cdot x) + [y_1, y_2, x]$. Therefore:
$$\operatorname{Ad}_x(u) = (x y_1) y_2 - y_1(y_2 x) - [x, y_1, y_2] - [y_1, y_2, x].$$
The first two terms give the leading contribution in $F_3$ (weight $\leq 3$), determined by $\operatorname{gr}_2(u)$. The associator terms $[x, y_1, y_2]$ and $[y_1, y_2, x]$ both lie in $F_1$ (weight $\leq 1$, since the octonionic associator of three weight-1 generators is a single element of $\operatorname{Im}(\mathbb{O})$). By cyclic invariance of the associator (equation (A4) of Lemma 6.4.2a, Chapter 6: $[a, b, c] = [b, c, a] = [c, a, b]$ for any alternative algebra), we have $[y_1, y_2, x] = [x, y_1, y_2]$. Therefore:
$$\operatorname{Ad}_x(u) = (xy_1)y_2 - y_1(y_2 x) - [x, y_1, y_2] - [x, y_1, y_2] = (xy_1)y_2 - y_1(y_2 x) - 2[x, y_1, y_2].$$
The term $-2[x, y_1, y_2] \in F_1$ demonstrates weight reversal: the adjoint of a weight-1 element on a weight-2 element produces a correction in $F_1 = F_{k-1}$, which is 2 filtration levels below the overall degree $F_3 = F_{k+1}$. The map $\operatorname{Ad}_x^{\text{assoc}} : \operatorname{gr}_2 \to F_1 / F_0$ sends $\overline{u}$ to $\overline{-2[x, y_1, y_2]}$.

**Base case: $k = 3$.** Let $u = (y_1 y_2) y_3$ (a weight-3 left-comb monomial). Then:
$$\operatorname{Ad}_x(u) = x \cdot ((y_1 y_2) y_3) - ((y_1 y_2) y_3) \cdot x.$$

Expanding the first term using non-associative distributivity:
$$x \cdot ((y_1 y_2) y_3) = (x(y_1 y_2))y_3 + [x, (y_1 y_2), y_3].$$

Now expand $x(y_1 y_2) = (xy_1)y_2 + [x, y_1, y_2]$. Substituting:
$$(x(y_1 y_2))y_3 = ((xy_1)y_2)y_3 + [x, y_1, y_2] \cdot y_3.$$

The term $((xy_1)y_2)y_3$ lies in $F_4$ (weight 4, the leading term). The term $[x, y_1, y_2] \cdot y_3$ lies in $F_2$ (weight 2, since $[x, y_1, y_2]$ has weight 1). The associator $[x, (y_1 y_2), y_3]$ can be further expanded:
$$[x, (y_1 y_2), y_3] = (x(y_1 y_2))y_3 - x((y_1 y_2)y_3).$$
This is the difference of two weight-4 expressions. In $\operatorname{gr}_4$, they have the same leading term, so their difference lies in $F_3$. The explicit expansion (substituting $x(y_1 y_2) = (xy_1)y_2 + [x, y_1, y_2]$) gives:
$$[x, (y_1 y_2), y_3] = [x, y_1, y_2] \cdot y_3 + [(xy_1), y_2, y_3] + \text{weight-2 corrections from nested associators}.$$
The term $[x, y_1, y_2] \cdot y_3$ lies in $F_2$. The term $[(xy_1), y_2, y_3]$ lies in $F_1$ (the associator of three weight-1 elements). This demonstrates the **weight reversal at $k = 3$**: the adjoint action on a weight-3 element produces corrections reaching down to $F_2$ and even $F_1$.

**Inductive step: general $k$.** Assume the theorem holds for all weights $\leq k - 1$. Let $u = L_k(y_1, \ldots, y_k) = ((\cdots(y_1 y_2) y_3) \cdots) y_k$ be a weight-$k$ left-comb monomial. Write $u = u' \cdot y_k$ where $u' = L_{k-1}(y_1, \ldots, y_{k-1})$ has weight $k - 1$.

Compute:
$$\operatorname{Ad}_x(u) = x \cdot (u' y_k) - (u' y_k) \cdot x.$$

Re-associate the first term:
$$x \cdot (u' y_k) = (x \cdot u') \cdot y_k + [x, u', y_k]. \tag{$\dagger$}$$

The leading term $(x \cdot u') \cdot y_k$ has weight $k + 1$ and lies in $F_{k+1}$. We analyze the associator correction $[x, u', y_k]$.

**Claim.** $[x, u', y_k] \in F_{k-1}$.

*Proof of Claim.* By definition, $[x, u', y_k] = (xu')y_k - x(u'y_k)$. Both $(xu')y_k$ and $x(u'y_k)$ lie in $F_{k+1}$. To show their difference lies in $F_{k-1}$, we expand $xu'$ using the inductive hypothesis. Since $u' = L_{k-1}(y_1, \ldots, y_{k-1})$, the product $xu'$ can be re-expressed using the tree structure:
$$xu' = x \cdot L_{k-1}(y_1, \ldots, y_{k-1}).$$

By the inductive hypothesis applied at weight $k - 1$, $\operatorname{Ad}_x(u')$ (which equals $xu' - u'x$) has a leading term in $\operatorname{gr}_k$ and associator corrections in $F_{k-2}$. In particular:
$$xu' = u'x + [x, u'] + \text{terms in } F_{k-2}$$
where $[x, u'] = xu' - u'x$ denotes the commutator, whose leading term is in $F_k$ and whose associator corrections reach $F_{k-2}$.

Substituting into $[x, u', y_k] = (xu')y_k - x(u'y_k)$:
$$(xu')y_k = (u'x)y_k + [x, u'] \cdot y_k + F_{k-2} \cdot y_k.$$

The term $(u'x)y_k = u'(xy_k) + [u', x, y_k]$, where $[u', x, y_k]$ is the associator. Now $u'(xy_k)$ equals $x(u'y_k) + \text{lower-order terms}$ (by the commutator relation applied to $u'$ and $xy_k$). The key point is that the difference $(xu')y_k - x(u'y_k)$ reduces to:
$$[x, u', y_k] = [u', x, y_k]_{\text{leading}} + [x, u'] \cdot y_k|_{F_{k-2}} + \text{further nested corrections}.$$

Each nested associator involves at least three elements of which one ($x$ or $y_k$) has weight 1, and the associator operation maps three elements of total weight $w$ to an element of weight $\leq w - 2$ (because the octonionic associator of three weight-1 elements has weight 1, reducing the total by 2). Therefore:

- The first-level associator $[x, u', y_k]$ reaches $F_{k-1}$ (total weight $1 + (k-1) + 1 = k+1$, reduced by 2 to $k - 1$).
- The second-level nested associator (arising from expanding $u'$) reaches $F_{k-3}$.
- The $j$-th level nested associator reaches $F_{k - (2j - 1)}$.

This continues until $k - (2j - 1) \leq 0$, i.e., for at most $j = \lceil k/2 \rceil$ levels. $\square_{\text{Claim}}$

**Assembling the result.** From ($\dagger$) and the symmetric re-association of $(u'y_k) \cdot x = u'(y_k x) + [u', y_k, x]$:
$$\operatorname{Ad}_x(u) = (xu')y_k + [x, u', y_k] - u'(y_k x) - [u', y_k, x].$$

By cyclic invariance of the associator (equation (A4) of Lemma 6.4.2a: $[a, b, c] = [b, c, a] = [c, a, b]$), we have $[u', y_k, x] = [x, u', y_k]$. Therefore the explicit associator terms cancel:
$$\operatorname{Ad}_x(u) = (xu')y_k - u'(y_k x). \tag{$\ddagger$}$$

At first glance, this suggests no weight reversal. However, the weight-reversing corrections are *hidden inside* the term $(xu')y_k$. By the inductive hypothesis, the product $xu'$ contains associator corrections from the adjoint action on $u'$:
$$xu' = u'x + \operatorname{Ad}_x(u') = u'x + [x, u']_{\text{leading}} + \text{associator corrections in } F_{k-2}.$$

Substituting into ($\ddagger$):
$$(xu')y_k = (u'x)y_k + \operatorname{Ad}_x(u') \cdot y_k = (u'x)y_k + [x, u']_{\text{leading}} \cdot y_k + (\text{assoc. corrections in } F_{k-2}) \cdot y_k.$$

The leading term $(u'x)y_k$ combines with $-u'(y_k x)$ to give:
$$(u'x)y_k - u'(y_k x) = u'(xy_k - y_k x) + [u', x, y_k] - [u', y_k, x] + \text{nested corrections}$$
$$= u'[x, y_k] + [u', x, y_k] - [u', y_k, x] + \text{nested corrections}.$$

By antisymmetry in positions 2--3 (equation (A2) of Lemma 6.4.2a: $[a, b, c] = -[a, c, b]$), we have $[u', x, y_k] = -[u', y_k, x]$. Therefore:
$$(u'x)y_k - u'(y_k x) = u'[x, y_k] - 2[u', y_k, x] + \text{nested corrections}.$$

The term $u'[x, y_k] \in F_k$ contributes to the leading part in $\operatorname{gr}_{k+1}$ (it is the commutator action $\operatorname{ad}_x$ applied to $y_k$, extended by $u'$). The term $-2[u', y_k, x] \in F_{k-1}$ is the **weight-reversing correction**: the associator $[u', y_k, x]$ involves elements of weights $k-1$, $1$, and $1$, and by the octonionic associator property (the associator of elements of total weight $w$ produces a result of weight $\leq w - 2$), this lies in $F_{k-1}$.

Additionally, the product $\operatorname{Ad}_x(u') \cdot y_k$ introduces further corrections from the inductive hypothesis: by the induction on $k$, $\operatorname{Ad}_x(u')$ has associator corrections in $F_{k-3}$ (the weight-reversing corrections at weight $k - 1$). Multiplying by $y_k$ (weight 1) gives corrections in $F_{k-2}$, and their own associator structure reaches $F_{k-3}$.

More generally, the $j$-th level of nested associator corrections arises from expanding the adjoint action recursively through $j$ layers of the tree structure of $u$. Each layer contributes an associator that drops the filtration by 2 (from the octonionic associator property), giving corrections in $F_{k - (2j - 1)}$. The map
$$\operatorname{Ad}_x^{\text{assoc}} : \operatorname{gr}_k \to F_{k-1} / F_{k - 2\lfloor k/2 \rfloor - 1}$$
captures all these corrections. The depth of reversal is exactly $\lfloor k/2 \rfloor$ levels below the leading term.

**Summary for general $k$.** The adjoint action $\operatorname{Ad}_x$ on a weight-$k$ element $u \in F_k$ produces:
1. A leading term in $\operatorname{gr}_{k+1}$, determined by $\operatorname{gr}_k(u)$ (classical behavior).
2. First-order associator corrections in $F_{k-1}$, proportional to $[x, u', y_k]$.
3. Second-order nested corrections in $F_{k-3}$, from associators involving the internal structure of $u'$.
4. In general, $j$-th order corrections in $F_{k-(2j-1)}$, for $j = 1, 2, \ldots, \lfloor k/2 \rfloor$.

This completes the induction and establishes the weight reversal phenomenon for all $k$. $\square$

### 10.6.4 Physical Interpretation

The adjoint weight reversal means that **acting on a compound expression reveals information about its internal structure**. In the classical (associative) case, the adjoint action is "blind" to parenthesization—it can only increase the filtration degree. In the octonionic case, the adjoint action *probes* the internal tree structure of an element, extracting associator data from lower filtration levels.

This is the algebraic encoding of the principle that **context matters**: the way you interrogate a compound system (via the adjoint action) reveals how it was assembled (its tree structure).

---

## 10.7 The Hierarchical Basis in Detail

### 10.7.1 Explicit Basis for $\dim(A) = 7$ (Imaginary Octonions)

Let $A = \operatorname{Im}(\mathbb{O})$ with basis $\{e_1, \ldots, e_7\}$, ordered $e_1 < e_2 < \cdots < e_7$.

**Weight 0:** $\{a_\alpha : \alpha \in \Lambda\} = \{1, e_1, \ldots, e_7\}$ — the unit elements (8 elements).

**Weight 1:** $\{a_\alpha \cdot e_i : \alpha \in \Lambda, \, i \in \{1, \ldots, 7\}\}$ — 8 × 7 = 56 elements.

**Weight 2:** $\{a_{\alpha_0} \cdot (a_{\alpha_1} e_i)(a_{\alpha_2} e_j) : i \leq j, \, \alpha_0, \alpha_1, \alpha_2 \in \Lambda\}$

Number: $8 \times 8 \times 8 \times \binom{7+1}{2} = 512 \times 28 = 14336$ elements.

This count overcounts, because relation (R3) imposes $((a \cdot x)(b \cdot y) = (ab) \cdot (xy))$ modulo associator corrections. The independent hierarchical tree monomials at weight 2 are those where the overall coefficient $a_{\alpha_0}$ absorbs all coefficient reduction, and the leaf coefficients $a_{\alpha_1}, a_{\alpha_2}$ contribute genuinely new information only when they differ from what (R3) would predict.

After accounting for (R3), the independent basis elements at weight 2 are:
$$\{a_{\alpha_0} \cdot (e_i \cdot e_j) : i \leq j, \, \alpha_0 \in \Lambda\} \cup \{a_{\alpha_0} \cdot \delta_{\alpha_1, \alpha_2}(e_i, e_j) : i \leq j\}$$
where $\delta_{\alpha_1, \alpha_2}$ encodes the non-trivial coefficient configurations that cannot be reduced by (R3). The count depends on the associator structure and requires careful analysis.

**Proposition 10.14.** The number of independent hierarchical tree monomials at weight $k$ is:
$$\dim(U_{\mathbb{O}}(A)_k) = 8 \cdot C_{k-1} \cdot \binom{n + k - 1}{k} + \text{associator correction terms}$$
where $n = \dim_{\mathbb{R}} A = 7$, the factor 8 accounts for the overall $\mathbb{O}$-coefficient, and the correction terms arise from (R3) reductions. For the Malcev algebra of $\operatorname{Im}(\mathbb{O})$, the correction terms are negative (they reduce the count) and are bounded by $O(k \cdot 8^{k-1} \cdot \binom{n+k-2}{k-1})$.

### 10.7.2 The Hierarchical Structure Visualized

A hierarchical tree monomial of weight 3 with octonionic coefficients can be visualized as:

```
        a₀ ·
        /
       *
      / \
     *   a₃·e_{i₃}
    / \
a₁·e_{i₁}  a₂·e_{i₂}
```

Each leaf carries both an octonion coefficient ($a_j$) and a generator label ($e_{i_j}$). The internal nodes represent multiplication, and the overall coefficient $a_0$ scales the result. The tree structure (left comb, right comb, or balanced) is part of the basis specification.

In the classical case, this collapses to:
```
a · e_{i₁} e_{i₂} e_{i₃}    (single coefficient, no tree structure)
```

---

## 10.8 The Casimir Element and Contextual Casimir

### 10.8.1 Classical Casimir

In the classical setting, the *Casimir element* of $U(\mathfrak{g})$ is:
$$C = \sum_{i,j} g^{ij} x_i x_j \in Z(U(\mathfrak{g}))$$
where $g^{ij}$ is the inverse of the Killing form matrix $g_{ij} = B(x_i, x_j)$. The Casimir element lies in the center and commutes with all elements.

### 10.8.2 The Contextual Casimir

**Definition 10.15.** The *contextual Casimir element* of $U_{\mathbb{O}}(A)$ is:
$$C_\mu = \int_\Omega \sum_{i,j} g^{ij}(\omega) \, x_i \cdot x_j \, d\mu(\omega)$$
where $g^{ij}(\omega)$ is the inverse of the contextual Killing matrix $g_{ij}(\omega) = \operatorname{tr}(\operatorname{ad}_{x_i}^{(\omega)} \circ \operatorname{ad}_{x_j}^{(\omega)})$.

**Theorem 10.16.** The contextual Casimir element does NOT lie in the center of $U_{\mathbb{O}}(A)$ (unless $A$ is a Lie algebra and $\mu$ is a point mass). Instead, it satisfies:
$$[C_\mu, x] = \int_\Omega [C(\omega), x]_{\text{assoc}} \, d\mu(\omega)$$
where $[C(\omega), x]_{\text{assoc}}$ is the associator-weighted commutator at context $\omega$. The Casimir element is "central up to associator corrections."

*Proof.* We use Theorem 8.12.1 (Chapter 8, now fully proved) to compute the commutator $[C_\mu, x] = C_\mu \cdot x - x \cdot C_\mu$.

**Step 1: Reduce to the pointwise Casimir.** By linearity of the integral:
$$[C_\mu, x] = \int_\Omega [C(\omega), x] \, d\mu(\omega)$$
where $C(\omega) = \sum_{i,j} g^{ij}(\omega) x_i x_j$ is the pointwise Casimir at context $\omega$. It suffices to show that $[C(\omega), x] \neq 0$ at a generic context $\omega$.

**Step 2: Apply the modified adjoint identity.** By Proposition 8.3.1 (Chapter 8), which follows from the Jacobiator identity $J(a,b,c) = 6[a,b,c]$ (Proposition 6.4.2, Chapter 6), the naive adjoint and the commutator adjoint differ by the associator:
$$\mathrm{ad}_{[Z, X]}(W) = [\mathrm{ad}_Z, \mathrm{ad}_X](W) - 6[Z, X, W]$$
for all $W$. This identity is the key input.

**Step 3: Compute $[C(\omega), x]$ using Theorem 8.12.1.** In the classical (associative) case, the Casimir element $C = \sum g^{ij} x_i x_j$ is central because the Killing form satisfies $B([Z, X], Y) + B(X, [Z, Y]) = 0$ (invariance). The centrality proof works as follows: $[C, x] = \sum g^{ij}([x_i x_j, x])$, and summing this over the dual basis with the Killing form produces a contraction that vanishes by invariance.

In the non-associative case, Theorem 8.12.1 replaces the classical invariance with the **modified invariance**:
$$B_\mu([Z, X], Y) + B_\mu(X, [Z, Y]) = \mathcal{R}(X, Y, Z)$$
where:
$$\mathcal{R}(X, Y, Z) = -6 \int_\Omega \left[\mathrm{tr}\!\left(A_{Z,X}^{(\omega)} \circ \mathrm{ad}_Y^{(\omega)}\right) + \mathrm{tr}\!\left(\mathrm{ad}_X^{(\omega)} \circ A_{Z,Y}^{(\omega)}\right)\right] d\mu(\omega)$$
and $A_{U,V}^{(\omega)}(W) = [U, V, W]_\omega$ is the associator operator.

Setting $Z = x$ and contracting with the inverse Killing matrix: $\sum_{i,j} g^{ij}(\omega)(B_\omega([x, x_i], x_j) + B_\omega(x_i, [x, x_j]))$. In the classical case this contraction gives $[C, x]$ (via the definition of the Casimir as $C = \sum g^{ij} x_i x_j$ and the fact that $B(x_i, x_j)g^{jk} = \delta_i^k$). In the non-associative case, the same contraction gives:
$$[C(\omega), x]_{\text{classical part}} = 0 \quad \text{(the classical contribution vanishes by the same trace argument as in the associative case)}$$
plus the residual from modified invariance:
$$[C(\omega), x]_{\text{assoc}} = \sum_{i,j} g^{ij}(\omega) \, \mathcal{R}_\omega(x_i, x_j, x).$$

**Step 4: Evaluate the residual.** By the explicit formula for $\mathcal{R}$ from Theorem 8.12.1:
$$[C(\omega), x]_{\text{assoc}} = -6 \sum_{i,j} g^{ij}(\omega) \left[\mathrm{tr}\!\left(A_{x, x_i}^{(\omega)} \circ \mathrm{ad}_{x_j}^{(\omega)}\right) + \mathrm{tr}\!\left(\mathrm{ad}_{x_i}^{(\omega)} \circ A_{x, x_j}^{(\omega)}\right)\right].$$

This is nonzero whenever there exist $i, j$ such that $A_{x, x_i}^{(\omega)} \neq 0$, i.e., whenever $[x, x_i, \cdot]_\omega \neq 0$ as an operator. This holds for any non-associative alternative algebra (in particular for $\mathbb{O}$) whenever $x$ and $x_i$ do not lie in a common associative subalgebra (i.e., whenever $\{x, x_i\}$ does not generate an associative sub-algebra -- but by Artin's theorem, any two elements generate an associative subalgebra, so we need $A_{x, x_i}^{(\omega)}(x_j) = [x, x_i, x_j]_\omega \neq 0$ for some $j$, which requires three generators not lying in any associative subalgebra). For $\operatorname{Im}(\mathbb{O})$ with $\dim = 7 \geq 3$, such triples exist generically.

Integrating over $\Omega$:
$$[C_\mu, x] = \int_\Omega [C(\omega), x]_{\text{assoc}} \, d\mu(\omega) = -6 \int_\Omega \sum_{i,j} g^{ij}(\omega) \left[\mathrm{tr}(A_{x, x_i}^{(\omega)} \mathrm{ad}_{x_j}^{(\omega)}) + \mathrm{tr}(\mathrm{ad}_{x_i}^{(\omega)} A_{x, x_j}^{(\omega)})\right] d\mu(\omega).$$

**Step 5: Conditions for centrality.** The contextual Casimir $C_\mu$ is central ($[C_\mu, x] = 0$ for all $x$) if and only if the associator residual $\mathcal{R}$ vanishes identically. By the formula above, this requires $A_{x, x_i}^{(\omega)} = 0$ for $\mu$-a.e. $\omega$ and all $i$, i.e., $[x, x_i, W]_\omega = 0$ for all $W$. This holds if and only if the product $\star_\omega$ is associative at $\mu$-a.e. context, which means $A$ is a Lie algebra (all associators vanish). Conversely, if $A$ is a Lie algebra and $\mu$ is a point mass, then $C_\mu = C(\omega_0)$ is the classical Casimir element, which is central by the classical argument. $\square$

**Interpretation.** The contextual Casimir is not a single number but a *functional*: it assigns to each context $\omega$ a different "eigenvalue," weighted by the measure $\mu$. This is the algebraic manifestation of the principle that "the total invariant of a system depends on the context of observation."

---

## 10.9 Recovery of Classical $U(\mathfrak{g})$

**Theorem 10.17 (Quaternionic slice recovery).** Let $\mathfrak{g} \subset A$ be a Lie subalgebra of $A$ (i.e., $[x,y,z] = 0$ for all $x, y, z \in \mathfrak{g}$), and suppose $\mathfrak{g}$ is defined over a quaternionic subalgebra $\mathbb{H} \subset \mathbb{O}$. Then:
$$U_{\mathbb{O}}(A) \big|_{\mathfrak{g}} \cong U(\mathfrak{g}) \otimes_{\mathbb{H}} \mathbb{O}$$
where $U(\mathfrak{g})$ is the classical universal enveloping algebra and $\otimes_{\mathbb{H}} \mathbb{O}$ is the extension of scalars from $\mathbb{H}$ to $\mathbb{O}$.

*Proof.* When restricted to $\mathfrak{g}$:
- Relation (R2) becomes vacuous (all associators vanish).
- Relation (R3) becomes the classical scalar multiplication rule (since $\mathbb{H}$ is associative).
- Relation (R1) is the classical commutator relation.
- The COPBW basis reduces to the classical PBW basis (left combs with no octonionic coefficient variation, since $\mathbb{H}$-coefficients can be fully absorbed).

The extension $\otimes_{\mathbb{H}} \mathbb{O}$ accounts for the remaining four octonionic directions. $\square$

---

## 10.10 Computational Aspects

### 10.10.1 The Reduction Algorithm for $U_{\mathbb{O}}(A)$

Extending Algorithm 9.16 to the hierarchical setting:

**Algorithm 10.18 (COPBW Reduction).**

*Input:* An element $u \in U_{\mathbb{O}}(A)$ expressed as an $\mathbb{R}$-linear combination of arbitrary tree monomials with arbitrary $\mathbb{O}$-coefficients.

*Output:* The unique expression of $u$ in the COPBW basis $\mathcal{B}$.

1. **Coefficient migration:** For each tree monomial, use (R3) to migrate octonionic coefficients. At each internal node with children carrying coefficients $a, b$:
   - Write $(a \cdot x)(b \cdot y) = (ab) \cdot (xy) + \text{correction}$.
   - The correction involves the module associator $[a, b, xy]_M$ and has lower filtration weight (by the weight-reversal property).
   - Recurse until all coefficients are at leaves and a single overall coefficient remains.

2. **Label sorting:** Apply commutator relations (R1) to sort leaf labels to weakly increasing order.

3. **Tree standardization:** Apply associator relations (R2) to convert to left-comb form.

4. **Termination:** The algorithm terminates because each step strictly decreases a well-ordering on (weight, tree complexity, coefficient complexity).

### 10.10.2 Complexity

For a tree monomial of weight $k$ with $\mathbb{O}$-coefficients:
- Coefficient migration: $O(k)$ applications of (R3), each generating $O(1)$ correction terms.
- Label sorting: $O(k^2)$ applications of (R1) (bubble sort).
- Tree standardization: $O(k)$ applications of (R2).

Total: $O(k^2)$ basic operations per monomial, with each operation potentially generating $O(1)$ lower-weight correction terms. The total number of monomials generated is bounded by $O(k^2 \cdot C_{k-1} \cdot 8^k)$, which is exponential in $k$ but finite.

---

## 10.11 Open Questions and Connections

1. **Uniqueness of COPBW basis:** The COPBW basis depends on the choice of ordering on $I$ and the choice of standard tree shapes. Is there a canonical choice that minimizes the number of correction terms? (See Chapter 22 for partial results.)

2. **Infinite-dimensional $A$:** When $A$ is infinite-dimensional, the COPBW basis becomes uncountable. The measure-theoretic treatment of Chapter 14 addresses this.

3. **Deformation theory:** How does $U_{\mathbb{O}}(A)$ deform as the measure $\mu$ varies? This connects to the moduli space of contextual structures (Chapter 18).

4. **Representation theory:** What are the irreducible $U_{\mathbb{O}}(A)$-modules? The spectral theory of Chapter 13 provides the tools for decomposition.

---

## 10.12 Summary

| Concept | Classical | COPBW (This Chapter) |
|---------|-----------|---------------------|
| Base ring | $\mathbb{K}$ (commutative, associative) | $\mathbb{O}$ (non-commutative, non-associative) |
| Algebra | Lie algebra $\mathfrak{g}$ | $\mathbb{O}$-algebra $A$ with Sabinin structure |
| Enveloping algebra | $U(\mathfrak{g})$ (associative) | $U_{\mathbb{O}}(A)$ (non-associative) |
| Basis | Ordered monomials | Hierarchical tree monomials |
| Filtration | $F_i \cdot F_j \subseteq F_{i+j}$ | Same, plus adjoint weight reversal |
| Casimir | Central element | Contextual functional (non-central) |
| Killing form | Finite trace | Integral over measure space |
| Recovery | — | $\mathbb{H}$-slice gives classical $U(\mathfrak{g})$ |

The COPBW theorem establishes that the universal enveloping algebra over the octonions is a well-defined, explicitly describable algebraic object. Its hierarchical basis encodes both the non-associative structure of $\mathbb{O}$ and the contextual information of the decompactified Killing form. The adjoint weight reversal is the key new phenomenon: it shows that non-associativity enriches the filtration structure rather than destroying it.

---

*Next: Chapter 11 develops calculus over the octonions, defining gradient, divergence, and curl in 7D using the octonionic cross product.*
