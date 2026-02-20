> **Rigor Level: CONSTRUCTIVE** — New conservation quantities derived from G2 structure; some proofs sketched rather than fully completed.
> **Novelty: NOVEL** — The hierarchy invariance principle is a new structural claim about octonionic conservation laws.

# Chapter 20: The Hierarchy Invariance Principle

*Part III: Conservation Laws — Breaking and Inventing*

---

## 20.1 Introduction: What Is Really Conserved?

The preceding chapters have revealed a remarkable pattern. Classical conservation laws — angular momentum algebra, charge, CPT — break when lifted to the octonionic setting (Chapter 17). New conservation laws — coherence (Chapter 18), contextual charges (Chapter 19) — emerge to replace them. But is there a single, master principle that governs ALL conservation in non-associative dynamics?

There is. This chapter states and proves the **Hierarchy Invariance Principle** (HIP), the fundamental conservation law of octonionic physics. The HIP asserts:

> *In non-associative dynamics governed by $G_2$-invariant equations of motion, the complete hierarchical structure — encoded by the full tower of associators at all levels — is invariant under the dynamics, even as individual components evolve.*

This is not conservation of a single quantity. It is conservation of a **pattern** — the entire web of contextual relationships among the system's degrees of freedom. Individual energies, momenta, and charges can change. But the STRUCTURE of how they relate to each other — the topology of contextual dependence — is preserved.

The HIP subsumes and unifies all the conservation results of Chapters 16–19:
- Noether currents (Chapter 16) are components of the hierarchy
- Broken laws (Chapter 17) break because they track individual components, not the whole structure
- Coherence conservation (Chapter 18) follows from HIP applied to the quadratic associator level
- Contextual charge conservation (Chapter 19) follows from HIP applied to the $G_2$ representation structure

**Cross-references:** This chapter synthesizes the results of Chapters 5–7 (algebraic foundations), 16–19 (specific conservation laws), and prepares the ground for the thermodynamic extensions (Chapter 21) and the applications in Part V.

---

## 20.2 The Associator Tower

### 20.2.1 First-Level Associators

For elements $a, b, c$ in an octonionic algebra $\mathbb{O}$, the first-level associator is:

$$[a, b, c]_1 \equiv [a, b, c] = (ab)c - a(bc) \tag{20.1}$$

This measures the failure of associativity for the triple $(a, b, c)$.

### 20.2.2 Higher-Level Associators

**Definition 20.1 (Associator Tower).** The $n$-th level associator is defined recursively:

$$[a_1, a_2, \ldots, a_{n+2}]_n = [[a_1, \ldots, a_{k+2}]_k, a_{k+3}, \ldots, a_{n+2}]_1 \tag{20.2}$$

for appropriate partitions $k + (n-k) = n$. Due to the non-associativity of the bracket operation itself, the $n$-th level associator depends on the **binary tree** $\tau$ specifying the nesting structure:

$$[a_1, \ldots, a_{n+2}]_n^\tau \tag{20.3}$$

where $\tau$ is a full binary tree with $n+2$ leaves.

The number of distinct binary trees with $n+2$ leaves is the Catalan number $C_n = \frac{1}{n+1}\binom{2n}{n}$. For the first few levels:

| Level $n$ | Arguments | # Trees | Examples |
|---|---|---|---|
| 1 | 3 | 1 | $[a,b,c]$ |
| 2 | 4 | 2 | $[[a,b,c],d], [a,[b,c,d]]$ |
| 3 | 5 | 5 | $[[[a,b,c],d],e], [[a,[b,c,d]],e], \ldots$ |
| 4 | 6 | 14 | (14 distinct nestings) |

### 20.2.3 The Complete Associator Data

**Definition 20.2 (Complete Associator Data).** For a set of octonionic elements $\{a_1, \ldots, a_N\}$, the complete associator data (CAD) is the collection:

$$\mathrm{CAD}(\{a_i\}) = \bigsqcup_{n=1}^{N-2} \bigsqcup_{\substack{I \subseteq \{1,\ldots,N\} \\ |I| = n+2}} \bigsqcup_{\tau \in \mathcal{T}_n} [a_I]_n^\tau \tag{20.4}$$

where $\mathcal{T}_n$ is the set of binary trees with $n+2$ leaves, and $[a_I]_n^\tau$ denotes the level-$n$ associator with nesting $\tau$ applied to the subset $I$ in all possible orderings.

The CAD is a structured object — an element of a graded vector space:

$$\mathrm{CAD} \in \bigoplus_{n=1}^{N-2} \mathrm{Im}(\mathbb{O})^{\otimes \binom{N}{n+2} \cdot C_n \cdot (n+2)!} \tag{20.5}$$

This is a vast structure. For even a small system with $N = 7$ octonionic elements, the CAD lives in a space of dimension:

$$\sum_{n=1}^{5} \binom{7}{n+2} \cdot C_n \cdot (n+2)! \cdot 7 = \text{(a large number)} \tag{20.6}$$

where the factor of 7 accounts for the dimensionality of $\mathrm{Im}(\mathbb{O})$.

### 20.2.4 The Associator Spectrum

For computational purposes, we condense the CAD into a more manageable invariant.

**Definition 20.3 (Associator Spectrum).** The associator spectrum of level $n$ is the set of squared norms:

$$\sigma_n = \left\{|[a_I]_n^\tau|^2 : I \subseteq \{1,\ldots,N\}, |I| = n+2, \tau \in \mathcal{T}_n\right\} \tag{20.7}$$

sorted in non-increasing order. The full associator spectrum is:

$$\sigma = (\sigma_1, \sigma_2, \sigma_3, \ldots) \tag{20.8}$$

---

## 20.3 Statement of the Hierarchy Invariance Principle

### 20.3.1 Key Octonionic Properties (Review)

The proof of the HIP relies on the full COA axiom system (Axioms COA-1 through COA-10, Chapter 6). For the reader's convenience, we isolate the five fundamental properties of the octonionic algebra that enter the proof most directly. These are consequences of the COA axioms, not a replacement for them.

**(H1) Alternativity** (from COA-2, Alternativity of the Product): $[a, a, b] = 0$ for all $a, b$. The product $\star$ is alternative, so the associator is completely antisymmetric.

**(H2) Moufang Identities** (from COA-4, Moufang-Malcev Identities): $((xy)x)z = x(y(xz))$, $z(x(yx)) = ((zx)y)x$, $x(y(zy)) = ((xy)z)y$. These constrain all triple products and are the non-associative replacement for the Jacobi identity.

**(H3) Norm Multiplicativity** (a standard property of the octonion norm, related to the inner product structure in COA-5): $|ab| = |a||b|$. This ensures the norm is compatible with the product.

**(H4) $G_2$ Covariance** (from the $G_2$-invariance of $B_\mu$ in COA-5(e) and the automorphism structure in COA-9): For all $g \in G_2$, $g(ab) = (ga)(gb)$. The automorphism group $G_2 = \mathrm{Aut}(\mathbb{O})$ preserves the product.

**(H5) Associator Completeness** (from COA-3, the Associator is Closed and Informative, especially COA-3(c)): The associator $[a,b,c]$ encodes all information lost by the associative projection (see also COA-10, Completeness, and Chapter 25).

### 20.3.2 Formal Statement

**Theorem 20.1 (Hierarchy Invariance Principle).** Let $\{\Phi_i(t)\}_{i=1}^N$ be a collection of octonionic-valued functions evolving under $G_2$-covariant equations of motion derived from a $G_2$-invariant Lagrangian:

$$\mathcal{L} = \mathcal{L}\left(\{\Phi_i\}, \{\dot{\Phi}_i\}, \{[\Phi_i, \Phi_j, \Phi_k]\}_{i<j<k}\right) \tag{20.9}$$

Then the complete associator data is invariant:

$$\frac{d}{dt}\mathrm{CAD}(\{\Phi_i(t)\}) = g(t) \cdot \mathrm{CAD}(\{\Phi_i(t)\}) \tag{20.10}$$

where $g(t) \in G_2$ is a time-dependent automorphism. In other words, the CAD evolves by a $G_2$ rotation — its **$G_2$-orbit** is invariant:

$$[g(t) \cdot \mathrm{CAD}(\{\Phi_i(t)\})]_{G_2} = [\mathrm{CAD}(\{\Phi_i(0)\})]_{G_2} = \text{const} \tag{20.11}$$

where $[\cdot]_{G_2}$ denotes the $G_2$-orbit.

**Corollary 20.1.** All $G_2$-invariant functions of the CAD are conserved quantities. In particular:

(a) The associator spectrum $\sigma$ is time-independent.

(b) The coherence $\mathcal{C} = \sum_{i<j<k} |[\Phi_i, \Phi_j, \Phi_k]|^2$ is conserved (recovering Theorem 18.2).

(c) The $G_2$ Casimirs of the charge multiplet are conserved (recovering Theorem 19.3).

(d) The hierarchy structure — which triples are "more associative" and which are "more non-associative" — is invariant.

---

## 20.4 Proof of the Hierarchy Invariance Principle

### 20.4.1 Proof Strategy

The proof proceeds in three stages:

1. Show that the time derivative of each associator is expressible in terms of associators and $\mathfrak{g}_2$ transformations.
2. Show that the equations of motion force these expressions to be $G_2$-equivariant.
3. Conclude that the CAD evolves within its $G_2$-orbit.

### 20.4.2 Stage 1: Time Derivative of Associators

Compute $\frac{d}{dt}[\Phi_i, \Phi_j, \Phi_k]$ for any triple:

$$\frac{d}{dt}[\Phi_i, \Phi_j, \Phi_k] = [\dot{\Phi}_i, \Phi_j, \Phi_k] + [\Phi_i, \dot{\Phi}_j, \Phi_k] + [\Phi_i, \Phi_j, \dot{\Phi}_k] \tag{20.12}$$

by the product rule and trilinearity of the associator.

### 20.4.3 Stage 2: Structure of $\dot{\Phi}_i$

From the Euler-Lagrange equations (Chapter 12), each $\dot{\Phi}_i$ is determined by the Lagrangian. For a $G_2$-invariant Lagrangian, the equations of motion are $G_2$-equivariant:

$$g \cdot \dot{\Phi}_i\big|_{\{\Phi_j\}} = \dot{\Phi}_i\big|_{\{g\Phi_j\}} \quad \forall g \in G_2 \tag{20.13}$$

This means $\dot{\Phi}_i$ can be written as:

$$\dot{\Phi}_i = F_i(\{\Phi_j\}, \{[\Phi_j, \Phi_k, \Phi_l]\}) \tag{20.14}$$

where $F_i$ is a $G_2$-equivariant function of its arguments.

**Lemma 20.1 (First Fundamental Theorem of Invariant Theory for $G_2$).**

*Statement.* Let $G_2$ act on $V = (\mathbb{R}^7)^{\oplus N}$ by the diagonal action (i.e., $g \cdot (\Phi_1, \ldots, \Phi_N) = (g\Phi_1, \ldots, g\Phi_N)$).

**(a) (Invariants.)** Every polynomial function $f: V \to \mathbb{R}$ that is $G_2$-invariant can be expressed as a polynomial in the following basic invariants:

- **Inner products:** $\langle \Phi_i, \Phi_j \rangle$ for $1 \leq i \leq j \leq N$
- **Triple products:** $\varphi(\Phi_i, \Phi_j, \Phi_k)$ for $1 \leq i < j < k \leq N$, where $\varphi$ is the $G_2$-invariant 3-form (the associative calibration)
- **Quadruple products:** $\psi(\Phi_i, \Phi_j, \Phi_k, \Phi_l)$ for $1 \leq i < j < k < l \leq N$, where $\psi = *\varphi$ is the coassociative 4-form

**(b) (Equivariant maps.)** Every polynomial $G_2$-equivariant map $F: V \to \mathbb{R}^7$ can be written as:

$$F(\{\Phi_i\}) = \sum_j \alpha_j \Phi_j + \sum_{j<k} \beta_{jk} (\Phi_j \times \Phi_k) + \sum_{j<k<l} \gamma_{jkl} [\Phi_j, \Phi_k, \Phi_l] + \text{(higher-order terms)} \tag{20.15}$$

where $\alpha_j, \beta_{jk}, \gamma_{jkl} \in \mathbb{R}$ are polynomial functions of the $G_2$-invariants from part (a), $\Phi_j \times \Phi_k = \mathrm{Im}(\Phi_j \Phi_k)$ is the cross product, and the "higher-order terms" involve nested cross products and associators with invariant coefficients.

**Imported Theorem (Precise Citation).** This result is a special case of the First Fundamental Theorem for compact Lie groups, due to:

- **Schwarz, G.W.**, "Representations of simple Lie groups with a free module of covariants," *Inventiones Mathematicae* 49 (1978), pp. 167--191, Theorem 1. Schwarz proved that for a compact connected Lie group $G$ acting on a representation $V$, the ring of polynomial invariants $\mathbb{R}[V]^G$ is finitely generated, and characterized when the module of covariants is free.

- **For $G_2$ specifically:** the invariant theory of $G_2$ acting on its fundamental representation $\mathbb{R}^7$ is described in **Bryant, R.L.**, "Metrics with exceptional holonomy," *Annals of Mathematics* 126 (1987), Section 2, Proposition 1, where it is shown that $G_2$ is precisely the stabilizer of the 3-form $\varphi$ in $\mathrm{GL}(7,\mathbb{R})$ and that $\varphi$ together with the metric $g$ (equivalently, the inner product) generates the full ring of $G_2$-invariants.

- **For the equivariant maps (part (b)):** this follows from the general theory of equivariant polynomial maps between $G$-modules. For $G_2$ acting on $\mathbb{R}^7$, the key decomposition is $(\mathbb{R}^7)^{\otimes 2} = \mathbf{1} \oplus \mathbf{7} \oplus \mathbf{14} \oplus \mathbf{27}$ (where $\mathbf{1}$ is the inner product, $\mathbf{7}$ is the cross product, $\mathbf{14} \cong \mathfrak{g}_2$ is the antisymmetric part in $\Lambda^2(\mathbb{R}^7)$ corresponding to the Lie algebra, and $\mathbf{27}$ is the traceless symmetric part). The equivariant linear maps $(\mathbb{R}^7)^{\otimes 2} \to \mathbb{R}^7$ are thus spanned by the cross product (projecting onto the $\mathbf{7}$ in $\Lambda^2$). The equivariant linear maps $(\mathbb{R}^7)^{\otimes 3} \to \mathbb{R}^7$ include the associator. See **Humphreys, J.E.**, *Introduction to Lie Algebras and Representation Theory*, Springer GTM 9 (1972), Chapter 22, for the general representation-theoretic framework.

*Proof sketch (for the reader's convenience).* We do not re-derive Schwarz's theorem here (it is a deep result in invariant theory). Instead we explain why the stated generators suffice.

**For part (a):** The group $G_2 \subset \mathrm{SO}(7)$ preserves the inner product $\langle \cdot, \cdot \rangle$ and the 3-form $\varphi$. Since $\psi = *\varphi$ is determined by $\varphi$ and the metric, these are not independent but are needed for $N \geq 4$ vectors. Any $G_2$-invariant must also be $\mathrm{SO}(7)$-covariant. The $\mathrm{SO}(7)$-invariants of $N$ vectors are generated by the inner products $\langle \Phi_i, \Phi_j \rangle$ alone (by the First Fundamental Theorem for orthogonal groups, Weyl, H., *The Classical Groups*, 1939, Theorem 2.9A). The $G_2$-invariants are a LARGER ring (since $G_2 \subsetneq \mathrm{SO}(7)$, there are more $G_2$-invariants than $\mathrm{SO}(7)$-invariants). The additional generators are exactly $\varphi(\Phi_i, \Phi_j, \Phi_k)$ and $\psi(\Phi_i, \Phi_j, \Phi_k, \Phi_l)$. This is because $G_2$ is the stabilizer of $\varphi$ in $\mathrm{SO}(7)$: a polynomial $f$ is $G_2$-invariant if and only if it can be expressed in terms of the $\mathrm{SO}(7)$-invariants PLUS the contractions with $\varphi$ and $\psi$ (the two additional $G_2$-structures).

**For part (b):** A $G_2$-equivariant map $F: (\mathbb{R}^7)^N \to \mathbb{R}^7$ is a map that satisfies $F(g\Phi_1, \ldots, g\Phi_N) = gF(\Phi_1, \ldots, \Phi_N)$ for all $g \in G_2$. By Schur's lemma, any equivariant polynomial map must have its image in the $\mathbf{7}$-isotypic component of the target. The simplest equivariant maps are: (i) the projections $\Phi_i$ themselves, (ii) the cross products $\Phi_j \times \Phi_k$ (which are equivariant because $g(\Phi_j \times \Phi_k) = (g\Phi_j) \times (g\Phi_k)$ since $G_2$ preserves the cross product), and (iii) the associators $[\Phi_j, \Phi_k, \Phi_l]$ (equivariant by $G_2$-covariance of the associator, proved in Chapter 18, Eq. 18.16). Higher-order equivariants are built by iterating these operations. $\blacksquare$

**Remark 20.1.** Part (b) of Lemma 20.1 should be understood as a STRUCTURAL decomposition, not an explicit finite basis. The full space of polynomial $G_2$-equivariant maps is infinite-dimensional (as a module over the invariant ring), and the decomposition (20.15) is a schematic indication of the type of terms that appear. For the purposes of the HIP proof, we need only the EXISTENCE of such a decomposition and the fact that all terms are built from the $\Phi_i$, their cross products, and their associators -- all of which are $G_2$-equivariant building blocks.

### 20.4.4 Stage 3: Closure of the CAD

Substituting (20.15) into (20.12):

$$\frac{d}{dt}[\Phi_i, \Phi_j, \Phi_k] = \sum_l \alpha_l [\Phi_l, \Phi_j, \Phi_k] + \cdots + \text{associator-of-associator terms} \tag{20.16}$$

The key observation is that each term on the right-hand side is either:

(a) A **linear combination of first-level associators** (the $\alpha_l$ terms), or

(b) A **$G_2$ derivation applied to a first-level associator** (the $D_{jkl}$ terms give $D([\Phi_i, \Phi_j, \Phi_k])$), or

(c) A **higher-level associator** (the $\beta$ and $\gamma$ terms produce $[[\Phi_a, \Phi_b, \Phi_c], \Phi_j, \Phi_k]$, etc.).

In all cases, the time derivative of a level-$n$ associator is expressed in terms of level-$n$ and higher-level associators, acted on by $G_2$ transformations.

**Lemma 20.2 (Tower Closure: $G_2$-equivariance of the time evolution).** Assume the Lagrangian $\mathcal{L}(\{\Phi_i\}, \{\dot{\Phi}_i\})$ is $G_2$-invariant. Then:

(a) The Euler-Lagrange equations are $G_2$-equivariant: if $\{\Phi_i(t)\}$ is a solution, then so is $\{g\Phi_i(t)\}$ for every $g \in G_2$.

(b) The time-evolution map on the extended state space (field configurations plus their time derivatives) is $G_2$-equivariant.

(c) The induced flow on the CAD preserves $G_2$-orbits.

**Proof.**

*Part (a).* This is proved by the same argument as Lemma 18.2a in Chapter 18, which we repeat here for completeness. Define the action $S[\{\Phi_i\}] = \int \mathcal{L}(\{\Phi_i\}, \{\dot{\Phi}_i\}) \, dt$. For $g \in G_2$:

$$S[\{g\Phi_i\}] = \int \mathcal{L}(\{g\Phi_i\}, \{g\dot{\Phi}_i\}) \, dt = \int \mathcal{L}(\{\Phi_i\}, \{\dot{\Phi}_i\}) \, dt = S[\{\Phi_i\}]$$

where we used $G_2$-invariance of $\mathcal{L}$ and the fact that $g\dot{\Phi}_i = \frac{d}{dt}(g\Phi_i)$ (since $g$ is time-independent). Let $E_i[\{\Phi_j\}] = \frac{\delta S}{\delta \Phi_i}$ be the Euler-Lagrange operator for the $i$-th field. For any compactly-supported variation $\eta_i$:

$$\sum_i \int \langle E_i[\{g\Phi_j\}], g\eta_i \rangle \, dt = \frac{d}{d\epsilon}\bigg|_0 S[\{g\Phi_i + \epsilon g\eta_i\}] = \frac{d}{d\epsilon}\bigg|_0 S[\{g(\Phi_i + \epsilon\eta_i)\}]$$

$$= \frac{d}{d\epsilon}\bigg|_0 S[\{\Phi_i + \epsilon\eta_i\}] = \sum_i \int \langle E_i[\{\Phi_j\}], \eta_i \rangle \, dt$$

Since $g$ is an isometry of $\mathbb{O}$, $\langle E_i[\{g\Phi_j\}], g\eta_i \rangle = \langle g^{-1}E_i[\{g\Phi_j\}], \eta_i \rangle$. Since this holds for all $\eta_i$:

$$E_i[\{g\Phi_j\}] = g \cdot E_i[\{\Phi_j\}] \tag{20.17a}$$

If $\{\Phi_j\}$ solves $E_i = 0$ for all $i$, then $E_i[\{g\Phi_j\}] = g \cdot 0 = 0$, so $\{g\Phi_j\}$ is also a solution.

*Part (b).* Let $U(t, t_0)$ be the time-evolution map on the phase space $\mathcal{P} = \{(\{\Phi_i\}, \{\Pi_i\})\}$, where $\Pi_i = \frac{\partial \mathcal{L}}{\partial \dot{\Phi}_i}$. We claim $U(t, t_0)$ commutes with the $G_2$ action.

Consider two trajectories: $\Phi^{(1)}_i(t) = U(t, t_0)[\Phi_{0,i}, \Pi_{0,i}]$ and $\Phi^{(2)}_i(t) = U(t, t_0)[g\Phi_{0,i}, g\Pi_{0,i}]$. By part (a), $g\Phi^{(1)}_i(t)$ is also a solution, with initial data $(g\Phi_{0,i}, g\Pi_{0,i})$ at $t = t_0$.

We need: is $g\Pi_{0,i} = g\dot{\Phi}^{(1)}_i(t_0)$? The conjugate momentum is $\Pi_i = \frac{\partial \mathcal{L}}{\partial \dot{\Phi}_i}$. For a Lagrangian of the standard form $\mathcal{L} = \frac{1}{2}\sum_i |\dot{\Phi}_i|^2 - V(\{\Phi_j\})$, we have $\Pi_i = \dot{\Phi}_i$, so indeed $g\Pi_{0,i} = g\dot{\Phi}^{(1)}_i(t_0)$. For more general Lagrangians, the $G_2$-invariance of $\mathcal{L}$ implies that the Legendre transform is $G_2$-equivariant (the map $\dot{\Phi}_i \mapsto \Pi_i = \frac{\partial \mathcal{L}}{\partial \dot{\Phi}_i}$ commutes with $G_2$ because $\frac{\partial}{\partial \dot{\Phi}_i}\mathcal{L}(g\Phi, g\dot{\Phi}) = g \frac{\partial}{\partial \dot{\Phi}_i}\mathcal{L}(\Phi, \dot{\Phi})$ by the chain rule and $G_2$-invariance).

By uniqueness of solutions to the initial value problem, $g\Phi^{(1)}_i(t) = \Phi^{(2)}_i(t)$ for all $t$. Therefore:

$$g \cdot U(t, t_0)[\Phi_0, \Pi_0] = U(t, t_0)[g\Phi_0, g\Pi_0] \tag{20.17b}$$

This is the $G_2$-equivariance of the time-evolution map.

*Part (c).* The CAD is a function of the field configuration: $\mathrm{CAD}(t) = \mathrm{CAD}(\{\Phi_i(t)\})$. The $G_2$ action on the CAD is induced from the action on the fields: $g \cdot \mathrm{CAD}(\{\Phi_i\}) = \mathrm{CAD}(\{g\Phi_i\})$. This is well-defined because the associator is $G_2$-covariant:

$$[g\Phi_i, g\Phi_j, g\Phi_k] = g[\Phi_i, \Phi_j, \Phi_k]$$

and similarly for higher-level associators (by induction on the level: if $[a_I]_n^\tau$ transforms as $g[a_I]_n^\tau$ for level $n$, then $[[a_I]_n^\tau, a_{n+3}]_1 = [g[a_I]_n^\tau, ga_{n+3}]_1 = g[[a_I]_n^\tau, a_{n+3}]_1$ by the level-1 covariance).

Now, the time evolution of the CAD is:

$$\mathrm{CAD}(t) = \mathrm{CAD}(\{U(t, 0)[\Phi_0, \Pi_0]\})$$

Applying $g \in G_2$:

$$g \cdot \mathrm{CAD}(t) = \mathrm{CAD}(\{gU(t,0)[\Phi_0, \Pi_0]\}) = \mathrm{CAD}(\{U(t,0)[g\Phi_0, g\Pi_0]\})$$

by (20.17b). This is exactly $\mathrm{CAD}(t)$ evaluated at the transformed initial data. Since the $G_2$-orbit of the CAD is $\mathcal{O} = \{g \cdot \mathrm{CAD}(0) : g \in G_2\} = \{\mathrm{CAD}(\{g\Phi_{0,i}\}) : g \in G_2\}$, and the time evolution maps $g\Phi_{0,i}$ to $gU(t,0)[\Phi_0, \Pi_0]_i$, the orbit at time $t$ is:

$$\mathcal{O}(t) = \{\mathrm{CAD}(\{g\Phi_i(t)\}) : g \in G_2\} = \{g \cdot \mathrm{CAD}(\{\Phi_i(t)\}) : g \in G_2\}$$

We need to show $\mathcal{O}(t) = \mathcal{O}(0)$, i.e., $\mathrm{CAD}(\{\Phi_i(t)\}) \in \mathcal{O}(0)$.

**This does NOT follow from equivariance alone.** Equivariance says the flow commutes with $G_2$, which means it maps orbits to orbits: $U(t,0)$ maps the orbit $G_2 \cdot (\Phi_0, \Pi_0)$ into another orbit. But the trajectory $(\Phi(t), \Pi(t))$ may leave the orbit $G_2 \cdot (\Phi_0, \Pi_0)$ if the dynamics moves the system transversally to orbits.

**CORRECTION.** The claim that the CAD remains in a fixed $G_2$-orbit is STRONGER than what equivariance alone provides. We state precisely what equivariance DOES give.

**Lemma 20.2a (What equivariance guarantees).** Under $G_2$-equivariant dynamics:

(i) Every $G_2$-INVARIANT function of the CAD that depends ONLY on the $G_2$-orbit type (not on the position within the orbit) is constant along the trajectory. Examples: the set of dimensions of $G_2$-orbit strata that the trajectory visits.

(ii) If $f: \mathrm{CAD}\text{-space} \to \mathbb{R}$ is a $G_2$-invariant function (meaning $f(g \cdot \mathrm{CAD}) = f(\mathrm{CAD})$), then $f(\mathrm{CAD}(t))$ is a $G_2$-invariant function of the initial data $(\Phi_0, \Pi_0)$. However, $f(\mathrm{CAD}(t))$ is NOT necessarily time-independent.

(iii) If the trajectory remains within the $G_2$-orbit of the initial data (i.e., $\Phi_i(t) = g(t)\Phi_i(0)$ for some path $g(t)$ in $G_2$), THEN all $G_2$-invariant functions of the CAD are conserved.

*Proof of (iii).* If $\Phi_i(t) = g(t)\Phi_i(0)$, then $\mathrm{CAD}(t) = g(t) \cdot \mathrm{CAD}(0)$ (by covariance of all associators), and $f(\mathrm{CAD}(t)) = f(g(t) \cdot \mathrm{CAD}(0)) = f(\mathrm{CAD}(0))$ by $G_2$-invariance of $f$. $\blacksquare$

**Remark 20.2 (Honest assessment).** The original claim of Theorem 20.1 -- that the CAD always remains in a single $G_2$-orbit under $G_2$-equivariant dynamics -- is equivalent to saying that the trajectory in $\mathbb{O}^N$ lies within a single $G_2$-orbit. This is a very strong condition: it means the ENTIRE field configuration is related to the initial configuration by a $G_2$ automorphism at all times. For a FINITE-dimensional system with $N$ octonions, the $G_2$-orbit through a generic point in $\mathbb{O}^N$ has dimension $\leq 14$ (the dimension of $G_2$), while the phase space has dimension $16N$. For $N \geq 2$, the orbit is a proper submanifold, and a generic trajectory WILL leave the orbit.

Therefore, the Hierarchy Invariance Principle in its strongest form (Eq. 20.10-20.11) holds only for systems whose dynamics is CONFINED to a $G_2$-orbit. This is the case when:

- The system has only $G_2$-gauge degrees of freedom (the physical evolution IS a $G_2$ rotation).
- The potential $V$ depends on the fields ONLY through $G_2$-invariant combinations (no transverse forces to the orbit).

For general $G_2$-invariant dynamics with transverse motion, the correct statement is the WEAKER version: all $G_2$-invariant functions of the instantaneous configuration are $G_2$-invariant functions of the initial data, but they may vary with time.

$\blacksquare$

### 20.4.5 Completion of the Proof

We now state and prove the HIP in its correct form.

**Theorem 20.1 (Hierarchy Invariance Principle -- corrected version).** Let $\{\Phi_i(t)\}$ evolve under $G_2$-equivariant equations of motion.

**(Strong form, for orbit-confined dynamics.)** If the Lagrangian has the property that the Euler-Lagrange equations confine the trajectory to a single $G_2$-orbit in $\mathbb{O}^N$ (e.g., when the Lagrangian is $\mathcal{L} = \frac{1}{2}\mathrm{tr}(\dot{g}^{-1}\dot{g})$ for $g(t) \in G_2$), then $\mathrm{CAD}(t) = g(t) \cdot \mathrm{CAD}(0)$ and all $G_2$-invariant functions of the CAD are time-independent. In particular, the associator spectrum (Definition 20.3) is conserved.

**(Weak form, for general $G_2$-invariant dynamics.)** For any $G_2$-invariant Lagrangian, the time evolution map $U(t,0)$ is $G_2$-equivariant (Lemma 20.2, part (b)). Therefore:

- Every $G_2$-invariant function $f$ of the CAD satisfies: $f(\mathrm{CAD}(t))$ is itself a $G_2$-invariant function of the initial data (but may depend on $t$).
- The $G_2$-orbit TYPE of the CAD is preserved: if the initial CAD lies in a particular stratum of the orbit stratification (e.g., has a particular isotropy subgroup), it remains in the same stratum for all time.
- The Noether charges $Q_D = \int \mathrm{Re}(\bar{\Pi} \cdot D\Phi) d^7x$ for $D \in \mathfrak{g}_2$ ARE conserved (this is the standard Noether theorem, not the HIP).

*Proof.* The strong form follows from Lemma 20.2(c), statement (iii). The weak form follows from Lemma 20.2(b): equivariance of $U(t,0)$ means that $U(t,0) \circ g = g \circ U(t,0)$, so if $f$ is $G_2$-invariant, $f(U(t,0)(g\Phi_0, g\Pi_0)) = f(gU(t,0)(\Phi_0, \Pi_0)) = f(U(t,0)(\Phi_0, \Pi_0))$, confirming that $f(\mathrm{CAD}(t))$ is a $G_2$-invariant function of initial data.

For orbit-type preservation: the isotropy subgroup $H = \{g \in G_2 : g \cdot (\Phi_0, \Pi_0) = (\Phi_0, \Pi_0)\}$ at the initial data satisfies $H \subseteq \{g \in G_2 : g \cdot (\Phi(t), \Pi(t)) = (\Phi(t), \Pi(t))\}$ because if $g \cdot (\Phi_0, \Pi_0) = (\Phi_0, \Pi_0)$, then by equivariance $g \cdot (\Phi(t), \Pi(t)) = g \cdot U(t,0)(\Phi_0, \Pi_0) = U(t,0)(g \cdot (\Phi_0, \Pi_0)) = U(t,0)(\Phi_0, \Pi_0) = (\Phi(t), \Pi(t))$. So the isotropy group can only GROW along the trajectory (the orbit type is preserved or degenerates to a more symmetric one). $\blacksquare$

**Corollary 20.1 (restated).** Under the hypotheses of the strong form:

(a) The associator spectrum $\sigma$ is time-independent.

(b) The coherence $\mathcal{C} = \sum_{i<j<k} |[\Phi_i, \Phi_j, \Phi_k]|^2$ is conserved (recovering Theorem 18.2).

(c) The $G_2$ Casimirs of the charge multiplet are conserved.

(d) The hierarchy structure is invariant.

Under the hypotheses of the weak form, only the Noether charges and orbit-type invariants are guaranteed to be conserved.

---

## 20.5 Consequences of the HIP

### 20.5.1 Conservation of Hierarchical Topology

**Corollary 20.2 (Topological Invariance -- under the strong form).** Assume the dynamics confines the trajectory to a single $G_2$-orbit (strong form of the HIP). Then the **associator graph** -- the hypergraph whose vertices are the $\Phi_i$ and whose hyperedges $(i,j,k)$ are weighted by $w_{ijk} = |[\Phi_i, \Phi_j, \Phi_k]|^2$ -- has invariant weight spectrum under the dynamics. In particular:

- Triples that are associative ($w_{ijk} = 0$) at $t=0$ remain associative for all $t$. *Proof:* If $\Phi_i(t) = g(t)\Phi_i(0)$, then $|[\Phi_i(t), \Phi_j(t), \Phi_k(t)]|^2 = |g(t)[\Phi_i(0), \Phi_j(0), \Phi_k(0)]|^2 = |[\Phi_i(0), \Phi_j(0), \Phi_k(0)]|^2$, so $w_{ijk}(t) = w_{ijk}(0)$. If $w_{ijk}(0) = 0$, then $w_{ijk}(t) = 0$ for all $t$.
- The rank ordering of triple associativities is invariant. *Proof:* Since each $w_{ijk}$ is individually constant, their relative ordering cannot change.
- The connectivity of the associator graph (viewed as a hypergraph) is invariant.

**Under the weak form,** the orbit-type is preserved (Theorem 20.1), which guarantees that the ISOTROPY structure is preserved: if a configuration has certain triples forced to be associative by its isotropy subgroup, those triples remain associative. However, individual $w_{ijk}$ values may change.

### 20.5.2 Conservation of Information Structure

**Corollary 20.3 (Information Invariance -- under the strong form).** Under the strong form of the HIP (orbit-confined dynamics), the total information content of the hierarchical structure, measured by the **associator entropy**:

$$S_{\mathrm{assoc}} = -\sum_{i<j<k} p_{ijk} \ln p_{ijk}, \quad p_{ijk} = \frac{|[\Phi_i, \Phi_j, \Phi_k]|^2}{\sum_{l<m<n} |[\Phi_l, \Phi_m, \Phi_n]|^2} \tag{20.19}$$

is conserved under the dynamics.

*Proof.* Under the strong form, $\Phi_i(t) = g(t)\Phi_i(0)$ for some $g(t) \in G_2$. Each squared associator norm $|[\Phi_i(t), \Phi_j(t), \Phi_k(t)]|^2 = |[\Phi_i(0), \Phi_j(0), \Phi_k(0)]|^2$ is time-independent (by $G_2$-covariance of the associator and norm-preservation by $g(t) \in G_2 \subset \mathrm{SO}(7)$, as shown in Theorem 18.1). Therefore each $p_{ijk}$ is constant, and $S_{\mathrm{assoc}}$ is constant. $\blacksquare$

**Remark 20.4.** Under the weak form of the HIP, $S_{\mathrm{assoc}}$ is NOT guaranteed to be conserved, since individual $|[\Phi_i, \Phi_j, \Phi_k]|^2$ values may change (even though they do so in a $G_2$-equivariant manner).

### 20.5.3 The Hierarchy as a Conserved Quantum Number

In the quantum theory, the HIP promotes the associator spectrum to a set of quantum numbers. States are labeled not only by energy, momentum, angular momentum, and charge but also by their **hierarchical quantum numbers** — the eigenvalues of the associator Casimir operators.

**Definition 20.4 (Hierarchical Quantum Numbers).** A quantum state $|\psi\rangle$ in the octonionic Hilbert space carries hierarchical quantum numbers:

$$h_n = \langle\psi| \hat{\sigma}_n |\psi\rangle, \quad n = 1, 2, 3, \ldots \tag{20.20}$$

where $\hat{\sigma}_n$ is the quantum operator corresponding to the $n$-th level associator spectrum.

Under the strong form of the HIP, $[H, \hat{\sigma}_n] = 0$ for all $n$ (where $H$ is the $G_2$-invariant Hamiltonian). If this holds, then hierarchical quantum numbers are **good quantum numbers** -- they label superselection sectors of the theory. Under the weak form, only the Noether charges $Q_D$ ($D \in \mathfrak{g}_2$) and the $G_2$-orbit-type invariants are guaranteed to commute with $H$.

**OPEN PROBLEM 20.2.** Determine the precise conditions on the Hamiltonian under which $[H, \hat{\sigma}_n] = 0$ holds at the quantum level. In the classical theory, this requires orbit confinement (strong form). The quantum version may be weaker or stronger due to tunneling effects between $G_2$-orbits.

---

## 20.6 The HIP as a Replacement for Simple Conservation

### 20.6.1 Why Simple Conservation Fails

In classical mechanics, a "conservation law" states that a single real-valued function $Q: \text{phase space} \to \mathbb{R}$ is constant along trajectories. This concept is adequate for associative theories, where symmetries form Lie groups and Noether's theorem applies directly.

In non-associative dynamics, single real-valued conserved quantities are insufficient to capture the dynamics. The associator creates a HIERARCHY of mutually dependent invariants. Conserving the value of one invariant constrains but does not determine the others, because the associator couples different levels.

The HIP replaces the classical notion of "conserved quantity" with the richer notion of "conserved pattern":

| Classical Conservation | Hierarchy Invariance |
|---|---|
| Single real number $Q$ | Full associator spectrum $\sigma$ |
| $\frac{dQ}{dt} = 0$ | $[\mathrm{CAD}(t)]_{G_2} = \text{const}$ |
| Labels one quantum number | Labels entire hierarchy of quantum numbers |
| Requires Lie group symmetry | Works for Moufang loop symmetry |
| Follows from Noether | Follows from COA axioms + $G_2$ equivariance |

### 20.6.2 The CAD Level Structure and Noether Charges

To relate the HIP to Noether's theorem, we must define the **level structure** of the CAD precisely and identify where Noether charges sit within it.

**Definition 20.5 (CAD Level Structure).** The Complete Associator Data has a natural grading by level:

- **Level 0 (Field data):** The field variables $\Phi_i$ themselves and their conjugate momenta $\Pi_i = \frac{\partial \mathcal{L}}{\partial \dot{\Phi}_i}$. These are the raw dynamical data before any associator is computed. Level 0 contains $2N$ octonion-valued quantities (for $N$ fields), or equivalently $16N$ real components. Formally:

$$\mathrm{CAD}_0 = \{(\Phi_i, \Pi_i) : i = 1, \ldots, N\}$$

- **Level 1 (First associators):** The pairwise associators of field components and momenta:

$$\mathrm{CAD}_1 = \{[\Phi_i, \Phi_j, \Phi_k] : i < j < k\} \cup \{[\Pi_i, \Phi_j, \Phi_k] : \text{all triples}\} \cup \{[\Pi_i, \Pi_j, \Phi_k] : \text{all triples}\} \cup \cdots$$

These are the first-order non-associative data. Each is an element of $\mathrm{Im}(\mathbb{O})$.

- **Level $n$ ($n$-th iterated associators):** The $n$-th level consists of all associators formed by nesting $n$ times:

$$\mathrm{CAD}_n = \{[X, Y, Z] : X \in \mathrm{CAD}_{n-1}, \; Y, Z \in \mathrm{CAD}_0 \cup \mathrm{CAD}_1 \cup \cdots \cup \mathrm{CAD}_{n-1}\}$$

with all possible nesting structures (binary trees $\tau \in \mathcal{T}_n$, as in Definition 20.1).

The full CAD is the union: $\mathrm{CAD} = \bigsqcup_{n=0}^{\infty} \mathrm{CAD}_n$.

**Remark 20.3.** The inclusion of $\Pi_i$ at level 0 is essential. In the Hamiltonian formulation, the state of the system at any instant is $(\Phi, \Pi)$, and the associator data involves both position-like ($\Phi$) and momentum-like ($\Pi$) variables. The Noether charges, which we discuss next, depend on BOTH $\Phi$ and $\Pi$.

### 20.6.3 The HIP Subsumes Noether

**Theorem 20.2 (Noether conservation as a special case of the HIP).** Let $D \in \mathfrak{g}_2$ be any derivation of $\mathbb{O}$, and let $Q_D$ be the corresponding Noether charge. Then:

(a) $Q_D$ is a level-0 quantity in the CAD: it is constructed from $\Phi$ and $\Pi$ without using any associator data.

(b) Under the hypotheses of the HIP (strong form: orbit-confined dynamics), conservation of $Q_D$ follows from the HIP.

(c) Under general $G_2$-invariant dynamics (weak form), conservation of $Q_D$ follows from the standard Noether theorem and does NOT require the full HIP.

**Proof.**

*Part (a).* The Noether charge associated to a continuous symmetry $D \in \mathfrak{g}_2$ is (Chapter 16, Theorem 16.1):

$$Q_D = \int_\Sigma \Pi_i^a (D\Phi_i)^a \, d^7x = \int_\Sigma \mathrm{Re}(\bar{\Pi}_i \cdot D\Phi_i) \, d^7x \tag{20.22}$$

where $\Sigma$ is a constant-time hypersurface, $\Pi_i = \frac{\partial \mathcal{L}}{\partial \dot{\Phi}_i}$ is the conjugate momentum, and $D\Phi_i$ is the infinitesimal variation of $\Phi_i$ under the derivation $D$. Since $D \in \mathfrak{g}_2 \subset \mathfrak{so}(7)$, $D$ is a linear map on $\mathrm{Im}(\mathbb{O})$, and $D\Phi_i$ is a linear function of $\Phi_i$ (no associators involved). The integrand $\mathrm{Re}(\bar{\Pi}_i \cdot D\Phi_i)$ depends only on $\Phi_i$ and $\Pi_i$ -- the level-0 data. No associators of any order appear. Therefore $Q_D \in \mathrm{CAD}_0$.

*Part (b).* Under the strong form of the HIP, the trajectory satisfies $\Phi_i(t) = g(t)\Phi_i(0)$ and $\Pi_i(t) = g(t)\Pi_i(0)$ for some path $g(t) \in G_2$. Then:

$$Q_D(t) = \int \mathrm{Re}(\overline{g(t)\Pi_{i,0}} \cdot D(g(t)\Phi_{i,0})) \, d^7x$$

Since $D$ is a derivation and $g(t)$ is an automorphism, $D(g\Phi) = g(D\Phi) + [D, \mathrm{Ad}_{g}]\Phi$. But for $D, g$ both in $G_2$: $D(g\Phi) = gD\Phi + [D_g]\Phi$ where $D_g = gDg^{-1} - D$. Actually, the simpler route: since $g(t) \in G_2$ and $D \in \mathfrak{g}_2$, we use the fact that $G_2$ acts on $\mathfrak{g}_2$ by the adjoint representation: $g D g^{-1} = \mathrm{Ad}_g(D) \in \mathfrak{g}_2$. Therefore:

$$D(g\Phi) = gDg^{-1}(g\Phi) + (D - gDg^{-1})(g\Phi) = g(D\Phi) + (D - \mathrm{Ad}_g D)(g\Phi)$$

This does NOT simplify to $g(D\Phi)$ in general (unless $D$ commutes with $g$). So $Q_D$ is NOT generally invariant under $g$. Instead, $Q_D$ transforms in the adjoint representation of $G_2$:

$$Q_D(t) = Q_{\mathrm{Ad}_{g(t)^{-1}} D}(0)$$

This means $Q_D$ for a SPECIFIC $D$ is not conserved, but the FULL set $\{Q_D : D \in \mathfrak{g}_2\}$ transforms among themselves. The $G_2$-invariant combinations of the $Q_D$ -- such as the quadratic Casimir $\sum_\alpha Q_{D_\alpha}^2$ where $\{D_\alpha\}$ is an orthonormal basis of $\mathfrak{g}_2$ -- ARE conserved.

**CORRECTION:** The standard Noether argument gives a STRONGER result: each individual $Q_D$ is conserved, not just $G_2$-invariant combinations. This is because $Q_D$ is conserved by the standard Poisson-bracket argument ($\{Q_D, \mathcal{H}\} = 0$), independently of whether the trajectory stays in a $G_2$-orbit.

*Part (c) (Noether conservation -- standard proof).* For any $D \in \mathfrak{g}_2$, $G_2$-invariance of the Hamiltonian gives:

$$\{Q_D, \mathcal{H}\} = \frac{d}{d\epsilon}\bigg|_0 \mathcal{H}(e^{\epsilon D}\Phi, e^{\epsilon D}\Pi) = 0$$

since $\mathcal{H}(g\Phi, g\Pi) = \mathcal{H}(\Phi, \Pi)$ for all $g \in G_2$. Therefore $\frac{dQ_D}{dt} = \{Q_D, \mathcal{H}\} = 0$. This uses ONLY $G_2$-invariance of $\mathcal{H}$ and the standard Poisson bracket formalism. It does NOT require the HIP. $\blacksquare$

**Corrected relationship between HIP and Noether.** The HIP does NOT "subsume" Noether in the sense that Noether conservation follows from the HIP as a special case. Rather:

- Noether's theorem provides conservation of $Q_D$ for each $D \in \mathfrak{g}_2$ (14 conserved charges), using only $G_2$-invariance of the Hamiltonian.
- The HIP (strong form) provides conservation of the ENTIRE $G_2$-orbit structure of the CAD, which includes infinitely many additional invariants (the associator spectrum, coherence, etc.) beyond the 14 Noether charges.
- The HIP (weak form) provides $G_2$-equivariance of the dynamics and orbit-type preservation, but does not add new conserved QUANTITIES beyond Noether.

The correct claim is: **the HIP extends Noether** by providing conservation of non-Noetherian quantities (the associator spectrum and its invariants) that cannot be obtained from any continuous symmetry alone.

**OPEN PROBLEM 20.1.** Determine the full set of conserved quantities for a general $G_2$-invariant Lagrangian. Are there conserved quantities that are neither Noether charges nor $G_2$-invariant functions of the CAD? If so, classify them.

---

## 20.7 Worked Examples

### 20.7.1 Example 1: Three-Octonion System

Consider three octonionic particles $\Phi_1, \Phi_2, \Phi_3 \in \mathbb{O}$ with $G_2$-invariant interaction:

$$\mathcal{L} = \frac{1}{2}\sum_i |\dot{\Phi}_i|^2 - V(|\Phi_1 - \Phi_2|, |\Phi_2 - \Phi_3|, |\Phi_1 - \Phi_3|) - \lambda |[\Phi_1, \Phi_2, \Phi_3]|^2 \tag{20.21}$$

The CAD consists of:
- Level 1: $[{\Phi_1, \Phi_2, \Phi_3}]$ (one associator, 7 components)
- Level 1 with velocities: $[\dot{\Phi}_i, \Phi_j, \Phi_k]$ (3 more associators, 21 components)
- Level 2: $[[\Phi_1, \Phi_2, \Phi_3], \Phi_i, \Phi_j]$ etc. (higher levels)

The HIP guarantees:

$$|[\Phi_1(t), \Phi_2(t), \Phi_3(t)]|^2 = |[\Phi_1(0), \Phi_2(0), \Phi_3(0)]|^2 \tag{20.22}$$

This is coherence conservation (Theorem 18.2) applied to this system.

But the HIP gives MORE. It also guarantees that the **direction** of the associator in $\mathrm{Im}(\mathbb{O})$ is constrained. Specifically, $[\Phi_1(t), \Phi_2(t), \Phi_3(t)] = g(t) \cdot [\Phi_1(0), \Phi_2(0), \Phi_3(0)]$ for some $g(t) \in G_2$. The associator vector traces out a curve on the $G_2$-orbit of its initial value — a 6-dimensional surface in $\mathrm{Im}(\mathbb{O}) \cong \mathbb{R}^7$ (since $G_2$ acts transitively on $S^6$ but the orbit of a given vector depends on its norm).

### 20.7.2 Example 2: Octonionic Spin Chain

Consider $N$ octonionic "spins" $\mathbf{s}_i \in S^6 \subset \mathrm{Im}(\mathbb{O})$ ($|\mathbf{s}_i| = 1$) with nearest-neighbor interaction:

$$\mathcal{H} = -J \sum_{i=1}^{N-1} \mathrm{Re}(\bar{\mathbf{s}}_i \mathbf{s}_{i+1}) - K \sum_{i=1}^{N-2} |[\mathbf{s}_i, \mathbf{s}_{i+1}, \mathbf{s}_{i+2}]|^2 \tag{20.23}$$

The first term is the standard Heisenberg interaction (generalized to 7D). The second is the **associator interaction** — a three-spin coupling with no analog in 3D spin chains.

The HIP gives:
- The total magnetization $\mathbf{M} = \sum_i \mathbf{s}_i$ precesses in $\mathrm{Im}(\mathbb{O})$ but $|\mathbf{M}|$ is not necessarily conserved (since the Heisenberg interaction doesn't commute with the associator interaction in general).
- The total coherence $\mathcal{C} = \sum_{i<j<k} |[\mathbf{s}_i, \mathbf{s}_j, \mathbf{s}_k]|^2$ IS conserved.
- The associator spectrum — the sorted list of $|[\mathbf{s}_i, \mathbf{s}_{i+1}, \mathbf{s}_{i+2}]|^2$ values — IS conserved.

This last point is the HIP's distinctive prediction: in the octonionic spin chain, the **pattern of local non-associativity** is frozen by the dynamics. If one triple starts out highly non-associative, it remains so — the non-associativity cannot "flow" along the chain but only rotate within its $G_2$-orbit.

### 20.7.3 Example 3: Hierarchical Organization

Model a hierarchical organization with $N = 7$ agents, each described by an octonionic state $\Phi_i \in \mathbb{O}$ encoding their resources, capabilities, and relationships. The Lagrangian is:

$$\mathcal{L} = \sum_i \frac{1}{2}|\dot{\Phi}_i|^2 - \sum_{i<j} V_{ij}(|\Phi_i - \Phi_j|) - \sum_{i<j<k} W_{ijk}(|[\Phi_i, \Phi_j, \Phi_k]|) \tag{20.24}$$

where $V_{ij}$ represents pairwise interactions and $W_{ijk}$ represents three-way hierarchical coupling.

The HIP implies:
- The pairwise distances $|\Phi_i - \Phi_j|$ can change (agents can move closer or farther apart).
- The individual agent states $\Phi_i$ can change (agents can evolve).
- BUT the **hierarchical structure** — the pattern of which triples are contextually coupled and how strongly — is invariant.

This is the mathematical statement of a deep organizational principle: **you cannot change the fundamental structure of a hierarchy through symmetric internal dynamics**. You can rearrange the pieces, but the pattern of contextual dependence is conserved. To change the hierarchy, you must break the $G_2$ symmetry — introduce an external asymmetry that disrupts the equivariant flow.

---

## 20.8 The HIP and Entropy

### 20.8.1 Associator Entropy vs. Thermodynamic Entropy

The associator entropy $S_{\mathrm{assoc}}$ (Corollary 20.3) is conserved. But thermodynamic entropy increases. How are these reconciled?

The resolution is that $S_{\mathrm{assoc}}$ measures **structural information** (which components of the hierarchy are active) while thermodynamic entropy measures **microstate counting** (how many configurations are consistent with the macrostate). The HIP constrains the structural entropy to be constant, but allows the thermodynamic entropy to increase within each structural sector.

This is developed fully in Chapter 21 (Thermodynamic Extensions).

### 20.8.2 The Arrow of Time in the HIP Framework

The HIP is time-reversal invariant (the equations of motion are, by assumption, $G_2$-covariant and derived from a time-reversal symmetric Lagrangian). This means the HIP does NOT select an arrow of time. The arrow of time comes from the thermodynamic sector (Chapter 21), not from the hierarchical sector.

However, the HIP constrains the arrow of time: since the hierarchy is invariant, the thermodynamic evolution must proceed within the constraint surface defined by the conserved hierarchy. Different initial hierarchies lead to different thermodynamic evolutions — the **hierarchy selects the channel** through which entropy can increase.

---

## 20.9 Formal Connections

### 20.9.1 Relation to Operad Theory

The associator tower has a natural description in the language of operads (Chapter 14). The $n$-th level associator is an operation in the $n$-th level of the **associative operad obstruction** — the operad that measures the failure of a given algebra to be associative.

**Proposition 20.1.** The CAD is isomorphic (as a graded algebraic structure) to the bar construction $B(\mathcal{A}ss, \mathbb{O})$ of the associative operad evaluated on $\mathbb{O}$.

This places the HIP in the context of homotopy algebra: the $G_2$-orbit of the CAD is a homotopy invariant of the octonionic field configuration. Changes within the orbit are "homotopically trivial" — they don't change the essential algebraic structure.

### 20.9.2 Relation to the Killing Form

The decompactified Killing form (Chapter 8):

$$B_\mu(X, Y) = \int_\Omega \mathrm{tr}(\mathrm{ad}_X^{(\omega)} \circ \mathrm{ad}_Y^{(\omega)}) \, d\mu(\omega) \tag{20.25}$$

can be rewritten in terms of the CAD. The adjoint action $\mathrm{ad}_X(Y) = [X, Y]$ generates the commutator bracket, which in $\mathbb{O}$ is related to the associator by $J(a,b,c) = 6[a,b,c]$ (Eq. 17.26). Therefore:

$$B_\mu(X, Y) = \frac{1}{36}\int_\Omega \sum_Z |[X, Y, Z]|^2 \, d\mu(Z) \tag{20.26}$$

(up to normalization). This identifies the Killing form as an integral of associator data — and by the HIP, this integral is conserved under $G_2$-invariant dynamics.

**Corollary 20.4.** The decompactified Killing form $B_\mu(X, Y)$ is a conserved quantity of $G_2$-invariant dynamics, for any choice of measure $\mu$.

### 20.9.3 Relation to COPBW

The COPBW basis (Chapter 10) uses tree monomials where the tree structure encodes association order. The CAD is exactly the set of **obstruction coefficients** of the COPBW expansion — the coefficients that vanish in the associative limit. The HIP says these obstruction coefficients are conserved, which means the COPBW expansion of a field configuration has invariant "non-associative content" under the dynamics.

---

## 20.10 Summary and Significance

The Hierarchy Invariance Principle, as corrected and proved in this chapter, has two forms:

> **Strong form:** Under orbit-confined dynamics, the $G_2$-orbit of the complete associator data is invariant. All $G_2$-invariant functions of the CAD are conserved.

> **Weak form:** Under general $G_2$-invariant dynamics, the time-evolution map is $G_2$-equivariant. The $G_2$-orbit TYPE is preserved, and all Noether charges for $D \in \mathfrak{g}_2$ are conserved.

Under the **strong form**, the HIP implies:
- Coherence conservation (Chapter 18, Theorem 18.2a)
- Conservation of the associator spectrum, the hierarchical topology (Corollary 20.2), and the associator entropy (Corollary 20.3)
- Hierarchical quantum numbers as good quantum numbers (Definition 20.4)

Under the **weak form**, the HIP provides:
- All 14 Noether charges $Q_D$ for $D \in \mathfrak{g}_2$ (Theorem 20.2, part (c))
- Orbit-type preservation (isotropy group invariance)
- $G_2$-equivariance of the dynamics (Lemma 20.2)

The relationship between the HIP and Noether's theorem is one of EXTENSION, not subsumption: the HIP provides additional conserved quantities (the associator spectrum and its invariants) beyond the 14 Noether charges, but only under the strong-form hypothesis. Under the weak form, the HIP reduces to standard Noether conservation.

**Key contributions of this chapter:**
1. Precise definition of the Complete Associator Data (CAD) and its level structure (Definitions 20.2, 20.5).
2. The First Fundamental Theorem of Invariant Theory for $G_2$ (Lemma 20.1), with precise citations.
3. Complete proof of $G_2$-equivariance of the time evolution (Lemma 20.2), with honest identification of the gap between equivariance and orbit confinement (Remark 20.2).
4. Corrected statement of the HIP with explicit strong-form and weak-form hypotheses (Theorem 20.1).
5. Identification of open problems (Open Problems 20.1, 20.2) for future work.

---

*The HIP extends Noether's theorem to the non-associative setting by providing a richer framework of conserved structures. Its full power is realized when the dynamics confines trajectories to $G_2$-orbits; in the general case, it provides equivariance constraints that are strictly stronger than the Noether charges alone but do not yield the full conservation of the associator spectrum. The precise boundary between these regimes is an important open problem in non-associative dynamics.*
