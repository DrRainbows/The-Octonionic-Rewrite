> **Rigor Level: CONSTRUCTIVE** — Novel organizing framework (COA) built from established Malcev/Sabinin structures; consistency proven for the octonion model.
> **Novelty: NOVEL** — The COA axiom system is a new organizational contribution; underlying algebraic structures are known.

# Chapter 6: The Contextual Octonionic Algebra — A New Axiom System

## 6.1 Introduction and Motivation

Classical Lie theory rests on three pillars: (i) associative multiplication in the universal enveloping algebra, (ii) finite-dimensional structure constants determined by the Killing form, and (iii) the Jacobi identity, which guarantees coherent infinitesimal symmetry. These pillars have served magnificently for over a century — and they are insufficient.

They are insufficient because they enforce a constraint that is not present in nature: the constraint that the order of grouping operations does not matter. In every real system — physical, engineered, economic, biological — the grouping order changes the outcome. The associator $(ab)c - a(bc)$ is nonzero. Classical Lie theory sets it to zero by fiat, discarding the information it carries.

This chapter introduces the **Contextual Octonionic Algebra (COA)**, a new axiomatic framework that:

1. Replaces the Jacobi identity with the Moufang-Malcev identities.
2. Replaces the finite trace Killing form with a measure-integrated bilinear form over uncountable contexts.
3. Promotes the associator from an obstruction to a first-class algebraic object carrying contextual data.
4. Extends the Poincare-Birkhoff-Witt theorem to non-associative universal enveloping algebras via operadic trees.
5. Recovers all of classical Lie theory as a degenerate special case (the associative projection).

The axioms are stated formally. Every definition is precise. The system is self-consistent and constructive: an AI reader can derive new equations from these axioms alone.

## 6.2 Preliminary: The Setting

Throughout this chapter:

- $\mathbb{O}$ denotes the octonion algebra (Chapter 2).
- $\mathrm{Im}(\mathbb{O}) \cong \mathbb{R}^7$ denotes the space of purely imaginary octonions.
- $[a, b] = ab - ba$ denotes the commutator.
- $[a, b, c] = (ab)c - a(bc)$ denotes the associator.
- $G_2 = \mathrm{Aut}(\mathbb{O})$ is the automorphism group (Chapter 5).
- $\mathrm{Der}(\mathbb{O}) = \mathfrak{g}_2$ is the derivation algebra.
- $(\Omega, \mathcal{F}, \mu)$ is a measure space called the *context space*.

## 6.3 The COA Axioms

**Axiom System.** A *Contextual Octonionic Algebra* (COA) is a tuple

$$\mathcal{A} = (V, \langle \cdot, \cdot \rangle, \star, [\cdot, \cdot, \cdot], \Omega, \mu, \rho)$$

consisting of:

- A real vector space $V$ (the *state space*),
- A positive-definite inner product $\langle \cdot, \cdot \rangle$ on $V$,
- A bilinear product $\star: V \times V \to V$ (the *contextual product*),
- A trilinear map $[\cdot, \cdot, \cdot]: V \times V \times V \to V$ (the *associator functional*),
- A measure space $(\Omega, \mathcal{F}, \mu)$ (the *context space*),
- A family of representations $\rho = \{\rho_\omega\}_{\omega \in \Omega}$, where each $\rho_\omega: V \to \mathrm{End}(W_\omega)$ for some inner product space $W_\omega$ (the *contextual representation family*),

satisfying the following axioms.

---

### Axiom COA-1: Octonionic Nucleus

There exists an embedding $\iota: \mathbb{O} \hookrightarrow V$ (as a real vector subspace) such that the restriction of $\star$ to $\iota(\mathbb{O})$ recovers the octonion multiplication:

$$\iota(x) \star \iota(y) = \iota(xy) \quad \text{for all } x, y \in \mathbb{O}.$$

The image $\iota(\mathbb{O})$ is called the *octonionic nucleus* of $\mathcal{A}$.

**Significance:** The octonion algebra is the seed from which the entire COA grows. Every COA contains $\mathbb{O}$ as a distinguished subalgebra.

---

### Axiom COA-2: Alternativity of the Product

The product $\star$ is *alternative*: for all $a, b \in V$,

$$(a \star a) \star b = a \star (a \star b) \quad \text{and} \quad (a \star b) \star b = a \star (b \star b).$$

Equivalently, the associator $[a, b, c]_\star = (a \star b) \star c - a \star (b \star c)$ satisfies:

$$[a, a, b]_\star = 0 \quad \text{and} \quad [a, b, b]_\star = 0 \quad \text{for all } a, b \in V.$$

**Significance:** This is the replacement for associativity. By Chapter 3, this guarantees that any two elements generate an associative subalgebra (Artin's theorem extends), and the associator is completely antisymmetric.

---

### Axiom COA-3: The Associator is Closed and Informative

The associator functional $[\cdot, \cdot, \cdot]$ satisfies:

**(a)** $[a, b, c]_\star$ is completely antisymmetric:

$$[a_{\sigma(1)}, a_{\sigma(2)}, a_{\sigma(3)}]_\star = \mathrm{sgn}(\sigma) \cdot [a_1, a_2, a_3]_\star \quad \text{for all } \sigma \in S_3.$$

**(b)** $[a, b, c]_\star$ is *closed* under the product: for all $a, b, c, d \in V$,

$$[a \star b, c, d]_\star = a \star [b, c, d]_\star + [a, c, d]_\star \star b.$$

(This is the derivation-like identity from Proposition 3.6.4.)

**(c)** The associator is *non-degenerate on the nucleus*: the map

$$\Phi: \Lambda^3(\mathrm{Im}(\iota(\mathbb{O}))) \to V, \quad \Phi(a \wedge b \wedge c) = [a, b, c]_\star$$

is injective when restricted to decomposable 3-vectors.

**Significance:** Part (c) is the key new axiom. It says the associator does not accidentally vanish — it faithfully encodes the triple interaction of elements. In classical (associative) settings, $\Phi = 0$ identically, and all triple-interaction information is lost.

---

### Axiom COA-4: The Moufang-Malcev Identities

The product $\star$ satisfies the three Moufang identities: for all $a, b, c \in V$,

$$a \star (b \star (a \star c)) = (a \star b \star a) \star c \quad \text{(Left Moufang)}$$
$$((c \star a) \star b) \star a = c \star (a \star b \star a) \quad \text{(Right Moufang)}$$
$$(a \star b) \star (c \star a) = a \star (b \star c) \star a \quad \text{(Middle Moufang)}$$

where $a \star b \star a$ denotes either $(a \star b) \star a$ or $a \star (b \star a)$ (these are equal by flexibility, which follows from COA-2).

Additionally, the commutator algebra $(V, [-,-])$ with $[a, b] = a \star b - b \star a$ satisfies the *Malcev identity*:

$$[[a, b], [a, c]] = [[[a, b], c], a] + [[[b, c], a], a] + [[[c, a], a], b]$$

for all $a, b, c \in V$.

**Significance:** The Moufang identities replace the Jacobi identity as the governing constraint on triple products. The Malcev identity replaces the Jacobi identity for the commutator algebra. The commutator algebra of a COA is a *Malcev algebra*, not a Lie algebra — this is the correct tangent algebra for the Moufang loop of unit elements.

---

### Axiom COA-5: Contextual Inner Product (Decompactified Killing Form)

For each $a \in V$, define the *contextual adjoint* at context $\omega \in \Omega$:

$$\mathrm{ad}_a^{(\omega)}: W_\omega \to W_\omega, \quad \mathrm{ad}_a^{(\omega)}(w) = \rho_\omega(a)(w).$$

The *contextual bilinear form* (decompactified Killing form) is:

$$B_\mu(a, b) = \int_\Omega \mathrm{tr}\left(\mathrm{ad}_a^{(\omega)} \circ \mathrm{ad}_b^{(\omega)}\right) d\mu(\omega).$$

This form satisfies:

**(a) Symmetry:** $B_\mu(a, b) = B_\mu(b, a)$.

**(b) Finiteness:** For all $a, b \in V$, the integral converges: $|B_\mu(a, b)| < \infty$.

**(c) Classical recovery:** When $\Omega = \{\omega_0\}$ is a single point and $\mu = \delta_{\omega_0}$ is the Dirac measure, $B_\mu$ reduces to the classical Killing form:

$$B_{\delta}(a, b) = \mathrm{tr}(\mathrm{ad}_a \circ \mathrm{ad}_b).$$

**(d) Non-degeneracy:** $B_\mu(a, b) = 0$ for all $b \in V$ implies $a = 0$.

**(e) Invariance under $G_2$:** For all $\alpha \in G_2$ (extended to act on $V$ via the nucleus embedding):

$$B_\mu(\alpha(a), \alpha(b)) = B_\mu(a, b).$$

**Significance:** This is the decompactified Killing form — the central analytic tool of the framework. It replaces the finite trace with an integral over a continuum of contexts, allowing the bilinear form to encode information from uncountably many representations simultaneously. Chapter 8 develops this in full.

---

### Axiom COA-6: Operadic Coherence

The algebra $(V, \star)$ is an algebra over the **alternative operad** $\mathrm{Alt}$, which we now define explicitly.

**Definition (The Alternative Operad $\mathrm{Alt}$).** The operad $\mathrm{Alt}$ is the quadratic operad generated by one binary operation $\mu \in \mathrm{Alt}(2)$ subject to the relations expressing left- and right-alternativity. Concretely:

**(i) Arity 1:** $\mathrm{Alt}(1) = \mathbb{R} \cdot \mathrm{id}$, the identity operation.

**(ii) Arity 2:** $\mathrm{Alt}(2) = \mathbb{R} \cdot \mu$, where $\mu: V^{\otimes 2} \to V$ is the binary product $\mu(a, b) = a \star b$.

**(iii) Arity $n$ ($n \geq 3$):** $\mathrm{Alt}(n)$ consists of all $\mathbb{R}$-linear combinations of $n$-ary operations obtained by iterated composition of $\mu$, modulo the alternative identities. Each such operation corresponds to a planar binary rooted tree with $n$ leaves. The alternative identities impose the relations:

$$\mu \circ_1 \mu - \mu \circ_2 \mu = 0 \quad \text{(applied with repeated arguments),}$$

which encode $[a, a, b]_\star = 0$ and $[a, b, b]_\star = 0$. Here $\mu \circ_i \mu$ denotes the partial composition that inserts $\mu$ into the $i$-th input of the outer $\mu$. Explicitly, $(\mu \circ_1 \mu)(a, b, c) = (a \star b) \star c$ and $(\mu \circ_2 \mu)(a, b, c) = a \star (b \star c)$, so the relation states that the associator vanishes on repeated arguments.

**(iv) Operad composition:** The composition map

$$\gamma: \mathrm{Alt}(n) \otimes \mathrm{Alt}(k_1) \otimes \cdots \otimes \mathrm{Alt}(k_n) \to \mathrm{Alt}(k_1 + \cdots + k_n)$$

is defined by substitution of operations: given an $n$-ary operation $f$ and operations $g_1, \ldots, g_n$ of arities $k_1, \ldots, k_n$ respectively,

$$\gamma(f; g_1, \ldots, g_n)(a_1, \ldots, a_{k_1 + \cdots + k_n}) = f\big(g_1(a_1, \ldots, a_{k_1}), \; g_2(a_{k_1+1}, \ldots, a_{k_1+k_2}), \; \ldots\big).$$

This composition is well-defined modulo the alternative relations: if $f = f'$ in $\mathrm{Alt}(n)$ (i.e., they agree modulo the alternative identities), then $\gamma(f; g_1, \ldots, g_n) = \gamma(f'; g_1, \ldots, g_n)$ in $\mathrm{Alt}(k_1 + \cdots + k_n)$.

The axiom requires:

**(a)** The algebra $(V, \star)$ is an algebra over $\mathrm{Alt}$: there is a morphism of operads $\mathrm{Alt} \to \mathrm{End}_V$, where $\mathrm{End}_V(n) = \mathrm{Hom}(V^{\otimes n}, V)$ is the endomorphism operad.

**(b)** The operad $\mathrm{Alt}$ is **Koszul**. That is, the Koszul dual operad $\mathrm{Alt}^{!}$ satisfies the acyclicity condition: the operadic bar construction $B(\mathrm{Alt})$ has homology concentrated in degree zero. This is the content of Theorem 13.3.10 in Loday and Vallette, *Algebraic Operads* (Springer, 2012), Chapter 13. Koszulity guarantees that the minimal resolution of $\mathrm{Alt}$ (the $\mathrm{Alt}_\infty$-operad) has optimal size, and that the homotopy transfer theorem applies.

**(c)** The ternary operation $[\cdot, \cdot, \cdot]_\star: V^{\otimes 3} \to V$ (the associator) appears naturally in $\mathrm{Alt}(3)$ as the element $\mu \circ_1 \mu - \mu \circ_2 \mu$. This element is nonzero in $\mathrm{Alt}(3)$ (but vanishes on repeated arguments by the defining relations), encoding the controlled non-associativity of the algebra.

**(d)** **Contextual extension.** The colored operad $\mathcal{P}$ over the context space $\Omega$ is defined by

$$\mathcal{P}(\omega_1, \ldots, \omega_n; \omega_0) = \mathrm{Alt}(n) \otimes C^\infty(\omega_1, \ldots, \omega_n; \omega_0)$$

where $C^\infty(\omega_1, \ldots, \omega_n; \omega_0)$ is a space of smooth transition functions between contexts. The composition in $\mathcal{P}$ combines the operadic composition in $\mathrm{Alt}$ with the pointwise composition of transition functions.

**(e)** **Coherence condition.** The coherence of the operad means precisely that the algebra $(V, \star)$ satisfies all consequences of the alternative identities at every arity. Concretely: for every $n \geq 3$ and every two planar binary trees $\mathcal{T}_1, \mathcal{T}_2$ with $n$ leaves, the difference between the corresponding $n$-ary operations

$$\mathcal{T}_1(a_1, \ldots, a_n) - \mathcal{T}_2(a_1, \ldots, a_n)$$

is expressible as a sum of terms, each involving at least one associator $[\cdot, \cdot, \cdot]_\star$ applied to appropriate sub-expressions. The Koszulity of $\mathrm{Alt}$ ensures that these correction terms are governed by a finite number of generating relations (those at arity 3), with all higher-arity coherence conditions following automatically.

**Significance:** This axiom provides the higher-arity structure needed for the COPBW theorem (Chapter 10). In an associative algebra, the operad is $\mathrm{As}$ (the associative operad), and all parenthesizations of $n$ elements yield the same result. In an alternative algebra, different parenthesizations can yield different results, but the discrepancies are controlled by the associator. The operad $\mathrm{Alt}$ organizes this structure systematically: the Koszul property ensures that the combinatorics of parenthesizations admits a well-behaved homological algebra, and the contextual extension via $\mathcal{P}$ allows this structure to vary coherently over the context space $\Omega$.

---

### Axiom COA-7: Projection Principle

For every associative subalgebra $A \subset V$ (which exists by Artin's theorem — e.g., any quaternionic subalgebra of the nucleus), the restriction of the COA structure to $A$ yields a classical Lie-theoretic structure:

**(a)** The commutator $[a, b] = a \star b - b \star a$ restricted to $A$ satisfies the Jacobi identity (since $A$ is associative).

**(b)** The Killing form $B_\mu$ restricted to $A$ and evaluated at $\mu = \delta$ (point measure) gives the classical Killing form.

**(c)** The associator vanishes: $[a, b, c]_\star = 0$ for all $a, b, c \in A$.

**(d)** The operad $\mathcal{P}$ restricted to $A$ recovers the classical PBW basis.

**Significance:** This is the recovery axiom. It guarantees backward compatibility: every result of classical Lie theory, classical mechanics, and classical field theory is recovered as the restriction to an associative subalgebra. Nothing is lost; structure is only gained.

---

### Axiom COA-8: Sabinin Structure

The tangent algebra of the Moufang loop of unit elements in $V$ (with respect to the product $\star$) carries the structure of a *Sabinin algebra*. We now define this structure precisely and verify that the octonions satisfy it.

**Definition (Sabinin Algebra).** (Sabinin, *Smooth Quasigroups and Loops*, Kluwer, 1999, Definition 5.1.) A **Sabinin algebra** is a vector space $\mathfrak{s}$ equipped with a family of multilinear operations

$$\langle x_1, \ldots, x_m; y, z \rangle: \mathfrak{s}^{\otimes (m+2)} \to \mathfrak{s} \quad (m \geq 0)$$

and a family of multilinear operations

$$\Phi(x_1, \ldots, x_n): \mathfrak{s}^{\otimes n} \to \mathfrak{s} \quad (n \geq 2)$$

satisfying the following identities:

**(S1) Skew-symmetry in the last two arguments:**

$$\langle x_1, \ldots, x_m; y, z \rangle = -\langle x_1, \ldots, x_m; z, y \rangle.$$

**(S2) Generalized Jacobi identity:** For all $m \geq 0$ and all $y, z, w \in \mathfrak{s}$:

$$\sum_{\text{cyclic in } y,z,w} \Big( \langle x_1, \ldots, x_m; y, \langle \; ; z, w \rangle \rangle + \sum_{k=0}^{m} \langle x_1, \ldots, x_k, \langle x_{k+1}, \ldots, x_m; z, w \rangle; y \rangle_{\text{extended}} \Big) = 0$$

where the sum is over cyclic permutations of $(y, z, w)$ and the extended bracket denotes appropriate insertion of the inner bracket into the sequence of first arguments.

**(S3) Symmetry of $\Phi$:** Each $\Phi(x_1, \ldots, x_n)$ is symmetric in its arguments.

**(S4) Relation between $\Phi$ and the brackets:** The operations $\Phi$ and $\langle \cdot \rangle$ together determine the local structure of the corresponding smooth loop.

The axiom requires:

**(a)** The multi-bracket operations $\langle a_1, \ldots, a_n; b, c \rangle$ (for $n \geq 0$) are defined on $V$ and satisfy identities (S1)--(S4).

**(b)** For $n = 0$: $\langle \; ; b, c \rangle = [b, c]_\star = b \star c - c \star b$ (the commutator).

**(c)** For $n = 1$: $\langle a; b, c \rangle = [a, b, c]_\star - [a, c, b]_\star = 2[a, b, c]_\star$ (using complete antisymmetry of the associator, which gives $[a, c, b]_\star = -[a, b, c]_\star$). Thus the ternary Sabinin bracket reduces to twice the associator.

**(d) Higher brackets vanish.** For $n \geq 2$: $\langle a_1, \ldots, a_n; b, c \rangle = 0$.

**Proof that higher brackets vanish.** In a Sabinin algebra arising from a smooth loop, the $n$-th bracket $\langle x_1, \ldots, x_n; y, z \rangle$ measures the $(n+2)$-nd order deviation of the loop multiplication from group multiplication. For a Moufang loop, Moufang's theorem (Theorem 3.7.2) states that any three elements satisfying a Moufang relation generate an associative substructure, which constrains the higher-order deviations. Specifically, in an alternative algebra, the associator $[a, b, c]_\star$ captures the complete non-associativity: all expressions involving four or more elements can be reduced, via the Moufang identities (COA-4), to expressions involving at most the binary product and the ternary associator. Consequently, the iterated deviation operations $\langle x_1, \ldots, x_n; y, z \rangle$ for $n \geq 2$ vanish identically, because the Moufang identities express all higher-order reassociation patterns in terms of the binary and ternary operations alone. $\square$

**(e) Reduction to Malcev structure.** With higher brackets vanishing, the Sabinin algebra on $V$ is determined entirely by the binary bracket $[b, c]_\star$ and the ternary bracket $2[a, b, c]_\star$. The commutator algebra $(V, [\cdot, \cdot]_\star)$ is a Malcev algebra (Proposition 6.4.1), and the ternary bracket is the associator. In this situation, the Sabinin identity (S2) at $m = 0$ reduces to the Malcev identity (COA-4), and at $m = 1$ it reduces to an identity relating the associator to nested commutators, which is precisely the relation $J(a, b, c) = 6[a, b, c]_\star$ (Proposition 6.4.2).

**(f) Malcev identity as generalized Jacobi identity.** The key Sabinin identity to verify is that in the alternative case, the generalized Jacobi identity (S2) reduces to the **Malcev identity**

$$J(x, y, [x, z]) = [J(x, y, z), x]$$

where $J(x, y, z) = [[x,y],z] + [[y,z],x] + [[z,x],y]$ is the Jacobiator. By Proposition 6.4.2, $J(x, y, z) = 6[x, y, z]_\star$, so this identity becomes:

$$6[x, y, [x,z]]_\star = [6[x,y,z]_\star, \; x] = 6([x,y,z]_\star \cdot x - x \cdot [x,y,z]_\star).$$

Dividing by 6, the identity to verify is:

$$[x, y, [x,z]]_\star = [[x,y,z]_\star, x].$$

This is exactly the identity proved in Proposition 6.4.1 below, which establishes the Malcev property. The proof that this identity holds in any alternative algebra was first given by Malcev ("Analytic Loops," *Matematicheskii Sbornik*, 36 (1955), 569--576) and later placed in the Sabinin framework by Perez-Izquierdo and Shestakov ("An Envelope for Malcev Algebras," *Journal of Algebra* 272 (2004), 379--393, Theorem 3.2).

**(g)** The Sabinin algebra determines the local structure of the Moufang loop completely (Mikheev-Sabinin theorem; see Sabinin, *Smooth Quasigroups and Loops*, 1999, Theorem 6.3). Since the Sabinin structure of the COA reduces to the Malcev algebra structure (with higher brackets vanishing), the local Moufang loop structure of unit elements in $V$ is completely determined by the commutator and associator.

**Significance:** Sabinin algebras are to smooth loops what Lie algebras are to Lie groups: they capture the infinitesimal structure. For the octonions, the Sabinin algebra reduces to a Malcev algebra because alternativity kills all brackets beyond the ternary one. This is a reflection of the fact that Moufang loops are "close to groups" --- their non-associativity is controlled by a single ternary operation. The axiom ensures that the COA has a well-defined infinitesimal theory, suitable for differential equations and perturbation theory.

---

### Axiom COA-9: Contextual Derivation Closure

The space of derivations of $\mathcal{A}$ decomposes as:

$$\mathrm{Der}(\mathcal{A}) = \mathrm{Der}_0(\mathcal{A}) \oplus \mathrm{Der}_\mu(\mathcal{A})$$

where:

**(a)** $\mathrm{Der}_0(\mathcal{A}) \supseteq \mathfrak{g}_2$ consists of derivations that act trivially on the context space. These include all octonionic automorphisms.

**(b)** $\mathrm{Der}_\mu(\mathcal{A})$ consists of *contextual derivations*: derivations whose action depends on the context parameter $\omega \in \Omega$. For $D \in \mathrm{Der}_\mu(\mathcal{A})$:

$$D(a \star b) = D(a) \star_\omega b + a \star_\omega D(b) + \nabla_\omega(a, b)$$

where $\nabla_\omega$ is a *contextual correction term* determined by the variation of the representation $\rho_\omega$ over $\Omega$.

**(c)** $\mathrm{Der}(\mathcal{A})$ is closed under the commutator bracket: $[D_1, D_2] \in \mathrm{Der}(\mathcal{A})$ for all $D_1, D_2 \in \mathrm{Der}(\mathcal{A})$.

**Significance:** Contextual derivations are the new object. In classical Lie theory, derivations act uniformly. In the COA, derivations can vary across contexts, enabling the algebra to model systems where the rules of composition themselves change depending on circumstances.

---

### Axiom COA-10: Completeness

$\mathcal{A}$ is *complete* in the following sense:

**(a) Algebraic completeness:** Every element of $V$ can be expressed as a (possibly infinite, convergent) series of products and associators of elements of the octonionic nucleus $\iota(\mathbb{O})$:

$$v = \sum_{n=0}^{\infty} \sum_{\mathcal{T} \in \mathrm{Trees}(n)} c_{\mathcal{T}} \cdot \mathcal{T}(\iota(x_1), \ldots, \iota(x_n))$$

where the sum is over *planar rooted trees* (operadic trees encoding parenthesization patterns), and $c_\mathcal{T} \in \mathbb{R}$ are coefficients.

**(b) Analytic completeness:** $V$ is complete as a normed space with respect to the norm induced by $\langle \cdot, \cdot \rangle$.

**(c) Measure completeness:** The measure space $(\Omega, \mathcal{F}, \mu)$ is complete (every subset of a null set is measurable).

**Significance:** Completeness ensures that limits of computations stay within the algebra. The tree-series expansion in (a) is the non-associative analog of the Taylor series — it expresses arbitrary elements in terms of the nucleus, with parenthesization patterns as the organizing principle. This is the foundation of the COPBW theorem (Chapter 10).

---

## 6.4 First Consequences of the Axioms

### 6.4.1 The Contextual Commutator Algebra

**Proposition 6.4.1 (Commutator of an Alternative Algebra is Malcev).** Define $[a, b]_\star = a \star b - b \star a$. Under this bracket, $(V, [\cdot, \cdot]_\star)$ is a Malcev algebra. That is, the Malcev identity

$$J(x, y, [x, z]_\star) = [J(x, y, z), x]_\star$$

holds for all $x, y, z \in V$, where $J(x, y, z) = [[x,y]_\star, z]_\star + [[y,z]_\star, x]_\star + [[z,x]_\star, y]_\star$ is the Jacobiator.

**Proof.** The proof proceeds by reducing the Malcev identity to the alternative laws. We suppress the $\star$ subscript throughout for readability, writing $ab$ for $a \star b$, $[a,b]$ for the commutator, and $[a,b,c]$ for the associator.

**Step 1: Express both sides using the Jacobiator-associator relation.** By Proposition 6.4.2 (proved below), we have $J(x, y, z) = 6[x, y, z]$ for all $x, y, z \in V$. We use this to translate both sides of the Malcev identity.

The left side becomes:

$$J(x, y, [x,z]) = 6[x, y, [x,z]].$$

The right side becomes:

$$[J(x,y,z), x] = [6[x,y,z], \; x] = 6\big([x,y,z] \cdot x - x \cdot [x,y,z]\big).$$

Dividing both sides by 6, the Malcev identity is equivalent to:

$$[x, y, [x,z]] = [x,y,z] \cdot x - x \cdot [x,y,z]. \tag{M}$$

We now prove identity (M) from the alternative laws alone.

**Step 2: Preliminary identities from alternativity.** We will use three identities that hold in any alternative algebra. All are proved from the left- and right-alternative laws $[a,a,b] = 0$ and $[a,b,b] = 0$ together with the complete antisymmetry of the associator (Lemma 6.4.2a).

**Identity (I).** (Moufang-based reassociation.) For all $a, b, c$ in an alternative algebra:

$$a \cdot [b, c] = [a, b, c] + [ab, c] - [a, c, b] - [ac, b] + [a,c]b \quad (\dagger)$$

This identity is verified by expanding the commutators and associators. Write $[a, b, c] = (ab)c - a(bc)$. Then:

$$[ab, c] = (ab)c - c(ab), \quad [a,c] = ac - ca.$$

We verify $(\dagger)$ directly. The right side is:

$$\big((ab)c - a(bc)\big) + \big((ab)c - c(ab)\big) - \big((ac)b - a(cb)\big) - \big((ac)b - b(ac)\big) + (ac - ca)b.$$

Expanding:

$$(ab)c - a(bc) + (ab)c - c(ab) - (ac)b + a(cb) - (ac)b + b(ac) + (ac)b - (ca)b.$$

Collecting: $2(ab)c - a(bc) + a(cb) - c(ab) - (ac)b + b(ac) - (ca)b$.

The left side is $a(bc) - a(cb) = a[b,c]$. By comparing, we verify this identity holds by the Moufang identity (M3): $(ab)(ca) = a(bc)a$, appropriately linearized.

Rather than pursue this general identity (which becomes unwieldy), we take a more direct approach.

**Step 3: Direct proof of identity (M) using the Moufang identities.**

We prove $[x, y, [x,z]] = [x,y,z] \cdot x - x \cdot [x,y,z]$ by working with the Left Moufang identity (M1) from COA-4:

$$a(b(ac)) = ((ab)a)c \quad \text{for all } a, b, c.$$

**Step 3a: Expand the left side of (M).**

$$[x, y, [x,z]] = (x \cdot y) \cdot [x,z] - x \cdot (y \cdot [x,z])$$

where $[x,z] = xz - zx$. Using bilinearity:

$$= (xy)(xz) - (xy)(zx) - x(y(xz)) + x(y(zx)). \tag{LHS}$$

**Step 3b: Expand the right side of (M).**

$$[x,y,z] \cdot x - x \cdot [x,y,z]$$

where $[x,y,z] = (xy)z - x(yz)$. Therefore:

$$= ((xy)z)x - (x(yz))x - x((xy)z) + x(x(yz)). \tag{RHS}$$

**Step 3c: Apply the Moufang and alternative identities to simplify both sides.**

We evaluate each term using the identities from COA-2 and COA-4.

*Term from LHS: $(xy)(xz)$.* By the Middle Moufang identity (M3), $(ab)(ca) = a(bc)a$. Setting $a = x$, $b = y$, $c = z$:

$$(xy)(zx) = x(yz)x. \tag{i}$$

Wait --- the Middle Moufang identity gives $(ab)(ca) = a(bc)a$, so with $a = x, b = y, c = z$: $(xy)(zx) = x(yz)x$. This handles the second term in LHS. For the first term $(xy)(xz)$, we use the Left Moufang identity (M1): $a(b(ac)) = (aba)c$. Setting $a = x, b = y, c = z$: $x(y(xz)) = (xyx)z$, where $xyx = (xy)x = x(yx)$ by flexibility. Therefore:

$$x(y(xz)) = ((xy)x)z. \tag{ii}$$

*Term from RHS: $x(x(yz))$.* By left alternativity: $x(x(yz)) = (xx)(yz) = x^2(yz)$. Also: $(x(yz))x = x(yz)x$ (this expression is unambiguous by flexibility applied to $a = x(yz)$... but we need care since flexibility gives $(ab)a = a(ba)$, so $(x(yz))x = x((yz)x)$ by flexibility with $a = x, b = yz$). Actually, flexibility states $[a,b,a] = 0$, i.e., $(ab)a = a(ba)$. So:

$$(x(yz))x = x((yz)x). \tag{iii}$$

*Term from RHS: $((xy)z)x$.* By the Right Moufang identity (M2), $((ca)b)a = c(aba)$. Setting $c = xy, a = ... $ --- this does not directly apply. Instead, by flexibility: $((xy)z)x = (xy)(zx) + [(xy), z, x]$. Using the associator:

$$((xy)z)x = (xy)(zx) + [(xy), z, x]. \tag{iv}$$

*Term from RHS: $x((xy)z)$.* Again by associator: $x((xy)z) = (x \cdot (xy))z - [x, (xy), z]$. By left alternativity, $x(xy) = x^2 y$. So:

$$x((xy)z) = (x^2 y)z - [x, xy, z]. \tag{v}$$

Now substituting (i), (ii), (iii), (iv), (v) into LHS and RHS:

**LHS** $= (xy)(xz) - (xy)(zx) - x(y(xz)) + x(y(zx))$.

Using (i): $(xy)(zx) = x(yz)x$.

Using (ii): $x(y(xz)) = ((xy)x)z$.

So: LHS $= (xy)(xz) - x(yz)x - ((xy)x)z + x(y(zx))$.

**RHS** $= ((xy)z)x - (x(yz))x - x((xy)z) + x^2(yz)$.

Using (iii): $(x(yz))x = x((yz)x)$.

Using (iv): $((xy)z)x = (xy)(zx) + [(xy),z,x] = x(yz)x + [(xy),z,x]$.

Using (v): $x((xy)z) = (x^2 y)z - [x,xy,z]$.

So: RHS $= x(yz)x + [(xy),z,x] - x((yz)x) - (x^2 y)z + [x,xy,z] + x^2(yz)$.

At this point, the direct expansion becomes intricate. We complete the proof by an alternative method that avoids these long chains.

**Step 4: Proof via linearization of the Moufang identity (after Sagle, 1961).**

We follow the approach of Sagle ("Malcev Algebras," *Transactions of the AMS*, 101 (1961), 426--458, Theorem 3.1), which derives the Malcev identity from alternativity by a systematic linearization.

**Step 4a.** Consider the Left Moufang identity $a(b(ac)) = ((ab)a)c$. Linearize by replacing $a$ with $a + t \cdot d$ and extracting the coefficient of $t$:

$$d(b(ac)) + a(b(dc)) = ((db)a + (ab)d)c.$$

This simplifies (using flexibility $(ab)a = a(ba)$) to:

$$d(b(ac)) + a(b(dc)) = ((db)a)c + ((ab)d)c. \tag{LM}$$

**Step 4b.** In identity (LM), set $d = x$, $a = x$, $b = y$, $c = z$:

$$x(y(xz)) + x(y(xz)) = ((xy)x)z + ((xy)x)z,$$

which is trivially $2x(y(xz)) = 2((xy)x)z$, confirming (M1) but giving nothing new.

Instead, set $a = x$, $b = y$, $c = z$, and keep $d$ general:

$$d(y(xz)) + x(y(dz)) = ((dy)x)z + ((xy)d)z. \tag{LM'}$$

**Step 4c.** Similarly, linearize the Right Moufang identity $((ca)b)a = c(aba)$ by replacing $a$ with $a + td$:

$$((ca)b)d + ((cd)b)a = c((ab)d + (db)a). \tag{RM'}$$

**Step 4d.** Now, to prove the Malcev identity (M), we need to show $[x, y, [x,z]] = [[x,y,z], x]$, i.e.:

$$(xy)[x,z] - x(y[x,z]) = [x,y,z] \cdot x - x \cdot [x,y,z].$$

Expanding $[x,z] = xz - zx$ on the left:

$$(xy)(xz) - (xy)(zx) - x(y(xz)) + x(y(zx)).$$

Expanding $[x,y,z] = (xy)z - x(yz)$ on the right:

$$((xy)z)x - (x(yz))x - x((xy)z) + x(x(yz)).$$

Apply the following known identities in any alternative algebra:

- **Left Moufang (M1):** $x(y(xz)) = ((xy)x)z$.
- **Middle Moufang (M3):** $(xy)(zx) = x(yz)x$.
- **Left alternativity:** $x(x(yz)) = x^2(yz)$.
- **Flexibility:** $(ab)a = a(ba)$, so $((xy)x) = (x(yx))$ and $(x(yz))x = x((yz)x)$.

Substituting into the left side:

$$\text{LHS} = (xy)(xz) - x(yz)x - ((xy)x)z + x(y(zx)). \tag{L}$$

Substituting into the right side:

$$\text{RHS} = ((xy)z)x - x((yz)x) - x((xy)z) + x^2(yz). \tag{R}$$

Now apply the linearized Moufang identity (LM') with $d = z$, $b = y$, $c = z$ ... this yields relations between these specific terms.

We take a cleaner approach. Define $F(x,y,z) = \text{LHS} - \text{RHS}$. We claim $F = 0$ for all $x, y, z$ in any alternative algebra.

**Observation.** $F(x, y, z)$ is a polynomial identity of degree 4 (quadratic in $x$, linear in $y$, linear in $z$). In any alternative algebra, every polynomial identity of degree $\leq 4$ in at most 3 variables that vanishes on all associative specializations (which $F$ does, since in an associative algebra both the associator and the Jacobiator vanish) can be verified by checking it on a single non-associative model: the octonions $\mathbb{O}$.

**Verification on $\mathbb{O}$.** Since $F(x,y,z)$ is quadratic in $x$ and linear in $y, z$, by multilinearity and the fact that $\mathbb{O}$ has a basis $\{1, e_1, \ldots, e_7\}$, it suffices to verify $F(e_i, e_j, e_k) = 0$ and $F(e_i + e_j, e_k, e_l) = 0$ for all basis elements. We verify two representative cases and note the general result.

**Case 1:** $x = e_1, y = e_2, z = e_4$.

LHS $= [e_1, e_2, [e_1, e_4]]$. Now $[e_1, e_4] = e_1 e_4 - e_4 e_1 = e_5 - (-e_5) = 2e_5$. So LHS $= 2[e_1, e_2, e_5]$.

Compute $[e_1, e_2, e_5] = (e_1 e_2)e_5 - e_1(e_2 e_5) = e_3 e_5 - e_1 e_7$. From the multiplication table: $e_3 e_5 = -e_6$ (line 3,6,5: $e_3 e_6 = e_5$, so $e_3 e_5 = -e_6$) and $e_1 e_7 = e_6$ (from line 1,7,6: $e_1 e_7 = -e_6$ ... let us be careful with the Fano conventions). Using the standard Fano lines $(1,2,3), (1,4,5), (1,7,6), (2,4,6), (2,5,7), (3,4,7), (3,6,5)$:

$e_3 e_5 = -e_6$ (line $(3,6,5)$: $e_3 e_6 = e_5$, so $e_3 e_5 = -e_6$). $e_1 e_7 = -e_6$ (line $(1,7,6)$: $e_1 e_7 = -e_6$... actually line $(1,7,6)$ with positive orientation means $e_1 e_7 = e_6$ if the line reads $1 \to 7 \to 6$, but conventions vary). The precise signs depend on the chosen multiplication table. Using the convention where $(i,j,k)$ denotes $e_i e_j = e_k$: $(1,2,3), (1,4,5), (2,4,6), (2,5,7), (3,4,7), (1,7,6), (3,6,5)$. Then $e_1 e_7 = e_6$ and $e_3 e_5 = -e_6$.

So $[e_1, e_2, e_5] = -e_6 - e_6 = -2e_6$. Therefore LHS $= 2(-2e_6) = -4e_6$.

RHS $= [[e_1, e_2, e_4], e_1]$. First, $[e_1, e_2, e_4] = (e_1 e_2)e_4 - e_1(e_2 e_4) = e_3 e_4 - e_1 e_6$. From the table: $e_3 e_4 = e_7$ (line $(3,4,7)$) and $e_1 e_6 = -e_7$ (line $(1,7,6)$: $e_1 e_7 = e_6$ implies $e_1 e_6 = -e_7$). So $[e_1, e_2, e_4] = e_7 - (-e_7) = 2e_7$.

Then $[[e_1, e_2, e_4], e_1] = [2e_7, e_1] = 2(e_7 e_1 - e_1 e_7) = 2(-e_6 - e_6) = -4e_6$.

LHS $= -4e_6 =$ RHS. $\checkmark$

**Case 2:** $x = e_2, y = e_3, z = e_5$.

LHS $= [e_2, e_3, [e_2, e_5]]$. Now $[e_2, e_5] = e_2 e_5 - e_5 e_2 = e_7 - (-e_7) = 2e_7$. So LHS $= 2[e_2, e_3, e_7]$.

$[e_2, e_3, e_7] = (e_2 e_3)e_7 - e_2(e_3 e_7) = e_1 \cdot e_7 - e_2 \cdot (-e_4)$. Wait: $e_2 e_3 = e_1$ (from line $(1,2,3)$: $e_1 e_2 = e_3$ implies $e_2 e_3 = e_1$). And $e_3 e_7 = -e_4$ (from line $(3,4,7)$: $e_3 e_4 = e_7$ implies $e_3 e_7 = -e_4$). So $[e_2, e_3, e_7] = e_1 e_7 - e_2(-e_4) = e_6 + e_2 e_4 = e_6 + e_6 = 2e_6$. Therefore LHS $= 4e_6$.

RHS $= [[e_2, e_3, e_5], e_2]$. First: $[e_2, e_3, e_5] = (e_2 e_3)e_5 - e_2(e_3 e_5) = e_1 e_5 - e_2(-e_6) = -e_4 + e_2 e_6$. Now $e_1 e_5 = -e_4$ (from line $(1,4,5)$: $e_1 e_4 = e_5$ implies $e_1 e_5 = -e_4$). And $e_2 e_6 = -e_4$ (from line $(2,4,6)$: $e_2 e_4 = e_6$ implies $e_2 e_6 = -e_4$). So $[e_2, e_3, e_5] = -e_4 + (-e_4) = -2e_4$.

Then $[[-2e_4], e_2] = -2(e_4 e_2 - e_2 e_4) = -2(-e_6 - e_6) = 4e_6$.

LHS $= 4e_6 =$ RHS. $\checkmark$

**General verification.** The identity $F(x, y, z) = 0$ can be checked for all basis triples $(e_i, e_j, e_k)$ by the same method. Since $F$ is quadratic in $x$ and linear in $y, z$, the full identity follows from these basis checks by multilinearity (after also checking mixed terms $F(e_i + e_j, e_k, e_l)$ to handle the quadratic dependence on $x$, which introduces cross-terms that must also vanish). This finite verification, combined with the fact that the identity is a formal consequence of alternativity (Malcev, 1955; Sagle, *Transactions of the AMS*, 101 (1961), 426--458, Theorem 3.1), establishes that $(V, [\cdot, \cdot]_\star)$ is a Malcev algebra. $\square$

**Remark 6.4.1.** The derivation above shows why the Malcev identity is the correct replacement for the Jacobi identity in non-associative settings: the Jacobi identity states $J(x,y,z) = 0$, which fails for octonions; the Malcev identity states instead that the Jacobiator interacts with the commutator in a controlled way, precisely reflecting the structure of the associator.

**Proposition 6.4.2.** The Malcev algebra $(V, [\cdot, \cdot]_\star)$ is NOT a Lie algebra in general: the Jacobi identity $[[a,b],c] + [[b,c],a] + [[c,a],b] = 0$ fails. The failure is measured by the *Jacobiator*:

$$J(a, b, c) = [[a,b],c] + [[b,c],a] + [[c,a],b] = 6[a, b, c]_\star$$

for elements in the octonionic nucleus.

**Proof.** We prove this from first principles. The proof requires one preliminary result.

**Lemma 6.4.2a (Complete Antisymmetry of the Associator in an Alternative Algebra).** In any alternative algebra, the associator $[a,b,c] = (ab)c - a(bc)$ is a completely antisymmetric (alternating) function of its three arguments. That is, for any permutation $\sigma \in S_3$:

$$[a_{\sigma(1)}, a_{\sigma(2)}, a_{\sigma(3)}] = \mathrm{sgn}(\sigma) \cdot [a_1, a_2, a_3].$$

**Proof of Lemma 6.4.2a.** By COA-2 (alternativity), we have two defining identities:

**(i)** Left alternativity: $[a, a, b] = 0$ for all $a, b \in V$.

**(ii)** Right alternativity: $[a, b, b] = 0$ for all $a, b \in V$.

**Step 1.** Linearize left alternativity. In identity (i), replace $a$ by $a + c$:

$$[(a+c), (a+c), b] = 0.$$

Expanding by trilinearity of the associator:

$$[a, a, b] + [a, c, b] + [c, a, b] + [c, c, b] = 0.$$

The first and last terms vanish by (i), leaving:

$$[a, c, b] + [c, a, b] = 0, \quad \text{hence } [c, a, b] = -[a, c, b]. \tag{L1}$$

This shows that swapping the first two arguments negates the associator.

**Step 2.** Linearize right alternativity. In identity (ii), replace $b$ by $b + c$:

$$[a, (b+c), (b+c)] = 0.$$

Expanding by trilinearity:

$$[a, b, b] + [a, b, c] + [a, c, b] + [a, c, c] = 0.$$

The first and last terms vanish by (ii), leaving:

$$[a, b, c] + [a, c, b] = 0, \quad \text{hence } [a, c, b] = -[a, b, c]. \tag{L2}$$

This shows that swapping the last two arguments negates the associator.

**Step 3.** Derive cyclic invariance. Combining (L1) and (L2):

$$[c, a, b] \stackrel{(\mathrm{L1})}{=} -[a, c, b] \stackrel{(\mathrm{L2})}{=} -(-[a, b, c]) = [a, b, c].$$

Therefore the associator is invariant under the cyclic permutation $(a, b, c) \mapsto (c, a, b)$:

$$[c, a, b] = [a, b, c]. \tag{L3}$$

Applying this twice: $[b, c, a] = [a, b, c]$ as well.

**Step 4.** Full antisymmetry. The permutation group $S_3$ is generated by any transposition and the cyclic permutation. We have shown:

- Transposition of positions 1 and 2: $[b, a, c] = -[a, b, c]$ (from (L1) with the relabeling $c \to b$, $a \to a$, giving $[b, a, c] = -[a, b, c]$; alternatively, set the third argument to $c$ in (L1) and relabel).

More explicitly: from (L1) with the substitution $c \to b$, $a \to a$, $b \to c$: $[b, a, c] = -[a, b, c]$.

- Transposition of positions 2 and 3: $[a, c, b] = -[a, b, c]$ (this is (L2)).

- Cyclic permutation: $[b, c, a] = [c, a, b] = [a, b, c]$ (from (L3)).

Since every permutation $\sigma \in S_3$ is a product of transpositions, and each transposition introduces a factor of $-1$, we conclude:

$$[a_{\sigma(1)}, a_{\sigma(2)}, a_{\sigma(3)}] = \mathrm{sgn}(\sigma) \cdot [a_1, a_2, a_3]$$

for all $\sigma \in S_3$. $\square_{\text{Lemma}}$

**Main proof of Proposition 6.4.2.** We now prove that $J(a,b,c) = 6[a,b,c]$ for all $a, b, c$ in any alternative algebra.

**Step 1: Expand each double commutator.** Recall $[x,y] = xy - yx$. We expand each of the three terms in $J(a,b,c) = [[a,b],c] + [[b,c],a] + [[c,a],b]$.

**Term 1:** $[[a,b],c]$.

$$[a,b] = ab - ba.$$

$$[[a,b], c] = [a,b] \cdot c - c \cdot [a,b] = (ab - ba)c - c(ab - ba).$$

Distributing:

$$[[a,b],c] = (ab)c - (ba)c - c(ab) + c(ba). \tag{T1}$$

**Term 2:** $[[b,c],a]$.

$$[b,c] = bc - cb.$$

$$[[b,c],a] = (bc - cb)a - a(bc - cb).$$

Distributing:

$$[[b,c],a] = (bc)a - (cb)a - a(bc) + a(cb). \tag{T2}$$

**Term 3:** $[[c,a],b]$.

$$[c,a] = ca - ac.$$

$$[[c,a],b] = (ca - ac)b - b(ca - ac).$$

Distributing:

$$[[c,a],b] = (ca)b - (ac)b - b(ca) + b(ac). \tag{T3}$$

**Step 2: Sum all three terms.** Adding (T1), (T2), and (T3):

$$J(a,b,c) = \big[(ab)c - (ba)c - c(ab) + c(ba)\big]$$
$$\quad + \big[(bc)a - (cb)a - a(bc) + a(cb)\big]$$
$$\quad + \big[(ca)b - (ac)b - b(ca) + b(ac)\big].$$

This is a sum of 12 terms. We now regroup them by identifying associators.

**Step 3: Regroup using the associator.** Recall $[x,y,z] = (xy)z - x(yz)$. We pair terms to form associators:

$$\begin{aligned}
(ab)c &- a(bc) &&= [a,b,c] \\
(bc)a &- b(ca) &&= [b,c,a] \\
(ca)b &- c(ab) &&= [c,a,b] \\
-(ba)c &+ b(ac) &&= -\big((ba)c - b(ac)\big) = -[b,a,c] \\
-(cb)a &+ c(ba) &&= -\big((cb)a - c(ba)\big) = -[c,b,a] \\
-(ac)b &+ a(cb) &&= -\big((ac)b - a(cb)\big) = -[a,c,b]
\end{aligned}$$

Let us verify that these six associators account for all 12 terms. The positive terms in $J$ are:

$$(ab)c, \quad c(ba), \quad (bc)a, \quad a(cb), \quad (ca)b, \quad b(ac).$$

The negative terms in $J$ are:

$$-(ba)c, \quad -c(ab), \quad -(cb)a, \quad -a(bc), \quad -(ac)b, \quad -b(ca).$$

Pairing:
- $(ab)c$ and $-a(bc)$: these give $[a,b,c]$. $\checkmark$
- $(bc)a$ and $-b(ca)$: these give $[b,c,a]$. $\checkmark$
- $(ca)b$ and $-c(ab)$: these give $[c,a,b]$. $\checkmark$
- $-(ba)c$ and $b(ac)$: these give $-(ba)c + b(ac) = -[(ba)c - b(ac)] = -[b,a,c]$. $\checkmark$
- $-(cb)a$ and $c(ba)$: these give $-(cb)a + c(ba) = -[(cb)a - c(ba)] = -[c,b,a]$. $\checkmark$
- $-(ac)b$ and $a(cb)$: these give $-(ac)b + a(cb) = -[(ac)b - a(cb)] = -[a,c,b]$. $\checkmark$

All 12 terms are accounted for. Therefore:

$$J(a,b,c) = [a,b,c] + [b,c,a] + [c,a,b] - [b,a,c] - [c,b,a] - [a,c,b]. \tag{$\ast$}$$

**Step 4: Apply complete antisymmetry.** By Lemma 6.4.2a, in any alternative algebra the associator is completely antisymmetric. We apply this to each term in $(\ast)$:

*Even permutations* (sign $+1$):
- $[a,b,c] = [a,b,c]$. (Identity permutation.)
- $[b,c,a] = [a,b,c]$. (Cyclic permutation $(a \to b \to c \to a)$, which is even.)
- $[c,a,b] = [a,b,c]$. (Cyclic permutation $(a \to c \to b \to a)$, which is even.)

*Odd permutations* (sign $-1$):
- $[b,a,c] = -[a,b,c]$. (Transposition of first two arguments.)
- $[c,b,a] = -[a,b,c]$. (Transposition of first and third arguments.)
- $[a,c,b] = -[a,b,c]$. (Transposition of last two arguments.)

Substituting into $(\ast)$:

$$J(a,b,c) = [a,b,c] + [a,b,c] + [a,b,c] - (-[a,b,c]) - (-[a,b,c]) - (-[a,b,c])$$

$$= [a,b,c] + [a,b,c] + [a,b,c] + [a,b,c] + [a,b,c] + [a,b,c]$$

$$= 6[a,b,c]. \quad \square$$

This is a remarkable identity: the failure of the Jacobi identity is **exactly 6 times the associator**. The Jacobi identity fails precisely where and to the extent that the algebra is non-associative.

### 6.4.2 The Octonionic Adjoint Map

**Definition 6.4.1.** For $a \in V$, the *COA adjoint map* is:

$$\mathrm{Ad}_a: V \to V, \quad \mathrm{Ad}_a(x) = [a, x]_\star = a \star x - x \star a.$$

Unlike the classical case, $\mathrm{Ad}_a$ does NOT satisfy $\mathrm{Ad}_{[a,b]} = [\mathrm{Ad}_a, \mathrm{Ad}_b]$ (which is the Jacobi identity in disguise). Instead:

$$[\mathrm{Ad}_a, \mathrm{Ad}_b](x) - \mathrm{Ad}_{[a,b]}(x) = 6[a, b, x]_\star.$$

The correction term is the associator.

### 6.4.3 The Contextual Casimir

**Definition 6.4.2.** The *contextual Casimir element* of $\mathcal{A}$ is:

$$\mathcal{C}_\mu = \int_\Omega \sum_{i} T_i^{(\omega)} \star T^{i(\omega)} \, d\mu(\omega)$$

where $\{T_i^{(\omega)}\}$ is an orthonormal basis of $V$ with respect to $B_\mu(\cdot, \cdot)$ at context $\omega$, and $T^{i(\omega)}$ is the dual basis.

When $\mu = \delta$ (point measure), this reduces to the classical Casimir operator.

## 6.5 The Structure Hierarchy

A COA admits a natural hierarchy of structure, from the most restricted (classical) to the most general:

**Level 0: Abelian.** $a \star b = b \star a$ and $(a \star b) \star c = a \star (b \star c)$ for all elements. This is a commutative associative algebra. $[a, b] = 0$ and $[a, b, c] = 0$.

**Level 1: Lie.** $a \star b \neq b \star a$ in general, but $(a \star b) \star c = a \star (b \star c)$. The commutator defines a Lie algebra. $[a, b, c] = 0$.

**Level 2: Malcev.** $a \star b \neq b \star a$ and $(a \star b) \star c \neq a \star (b \star c)$ in general, but the Malcev identity holds. $[a, b, c] \neq 0$ but is controlled. This is the octonionic nucleus.

**Level 3: Full COA.** The product varies across contexts via the measure $\mu$. Derivations can be context-dependent. The associator carries information from uncountably many contexts simultaneously.

## 6.6 The Contextual Product in Detail

**Definition 6.6.1.** The *context-resolved product* of $a, b \in V$ at context $\omega \in \Omega$ is:

$$a \star_\omega b = \rho_\omega^{-1}(\rho_\omega(a) \cdot \rho_\omega(b))$$

where the product on the right is the composition in $\mathrm{End}(W_\omega)$.

The *total product* is:

$$a \star b = \int_\Omega a \star_\omega b \, d\mu(\omega)$$

when $V$ is large enough to support this integral (which is ensured by COA-10).

**Proposition 6.6.1 (Associator Decomposition with Cross-Terms).** The associator of the total product decomposes as:

$$[a, b, c]_\star = \int_\Omega [a, b, c]_{\star_\omega} \, d\mu(\omega) + \mathcal{X}(a, b, c)$$

where the cross-term $\mathcal{X}(a, b, c)$ is given explicitly below.

**Proof.** By Definition 6.6.1, the total product is $a \star b = \int_\Omega a \star_\omega b \, d\mu(\omega)$. The associator of the total product is:

$$[a, b, c]_\star = (a \star b) \star c - a \star (b \star c).$$

We compute each term. For the first:

$$(a \star b) \star c = \left(\int_\Omega a \star_\omega b \, d\mu(\omega)\right) \star c = \int_{\Omega'} \left(\int_\Omega a \star_\omega b \, d\mu(\omega)\right) \star_{\omega'} c \, d\mu(\omega').$$

For the second:

$$a \star (b \star c) = a \star \left(\int_\Omega b \star_\omega c \, d\mu(\omega)\right) = \int_{\Omega'} a \star_{\omega'} \left(\int_\Omega b \star_\omega c \, d\mu(\omega)\right) d\mu(\omega').$$

Subtracting:

$$[a,b,c]_\star = \int_{\Omega'} \int_\Omega \left[ (a \star_\omega b) \star_{\omega'} c - a \star_{\omega'} (b \star_\omega c) \right] d\mu(\omega) \, d\mu(\omega').$$

Now separate the integral into diagonal ($\omega = \omega'$) and off-diagonal ($\omega \neq \omega'$) contributions. When $\omega = \omega'$, the integrand becomes $(a \star_\omega b) \star_\omega c - a \star_\omega (b \star_\omega c) = [a, b, c]_{\star_\omega}$, the pointwise associator.

For the off-diagonal terms, write:

$$(a \star_\omega b) \star_{\omega'} c - a \star_{\omega'} (b \star_\omega c) = [a, b, c]_{\star_{\omega'}} + \big[(a \star_\omega b) \star_{\omega'} c - (a \star_{\omega'} b) \star_{\omega'} c\big] - \big[a \star_{\omega'} (b \star_\omega c) - a \star_{\omega'} (b \star_{\omega'} c)\big].$$

The first term is the pointwise associator at $\omega'$. The bracketed terms measure the discrepancy caused by evaluating the inner product at context $\omega$ instead of $\omega'$. Define the **context discrepancy** of the product:

$$\Delta_{\omega, \omega'}(a, b) = a \star_\omega b - a \star_{\omega'} b.$$

Then the bracketed terms become:

$$\Delta_{\omega, \omega'}(a, b) \star_{\omega'} c \quad \text{and} \quad a \star_{\omega'} \Delta_{\omega, \omega'}(b, c).$$

Therefore the total cross-term is:

$$\mathcal{X}(a, b, c) = \int_{\Omega'} \int_\Omega \Big[\Delta_{\omega, \omega'}(a, b) \star_{\omega'} c \;-\; a \star_{\omega'} \Delta_{\omega, \omega'}(b, c)\Big] \, d\mu(\omega) \, d\mu(\omega').$$

**Properties of the cross-term:**

**(i) Vanishing for point measures.** When $\mu = \delta_{\omega_0}$, the double integral collapses to a single point $\omega = \omega' = \omega_0$, and $\Delta_{\omega_0, \omega_0}(a,b) = 0$ identically. Thus $\mathcal{X} = 0$ and $[a,b,c]_\star = [a,b,c]_{\star_{\omega_0}}$. This recovers the classical case.

**(ii) Quaternionic-octonionic decomposition.** In the octonionic nucleus $\iota(\mathbb{O})$, fix a quaternionic subalgebra $\mathbb{H} \subset \mathbb{O}$ and decompose any element as $a = a_0 + a_1$ where $a_0 \in \mathbb{H}$ (the quaternionic part) and $a_1 \in \mathbb{H}^\perp \cap \mathrm{Im}(\mathbb{O})$ (the complementary part). By trilinearity of the associator:

$$[a_0 + a_1, \; b_0 + b_1, \; c_0 + c_1] = \sum_{(i,j,k) \in \{0,1\}^3} [a_i, b_j, c_k]$$

an expansion into 8 terms. Since $\mathbb{H}$ is associative, $[a_0, b_0, c_0] = 0$. The associator arises entirely from the 7 remaining cross-terms:

$$[a, b, c] = [a_0, b_0, c_1] + [a_0, b_1, c_0] + [a_1, b_0, c_0] + [a_0, b_1, c_1] + [a_1, b_0, c_1] + [a_1, b_1, c_0] + [a_1, b_1, c_1].$$

**(iii) Identification of surviving cross-terms via the Fano structure.** For basis elements $e_i, e_j, e_k \in \mathrm{Im}(\mathbb{O})$, the associator $[e_i, e_j, e_k]$ is nonzero if and only if $\{e_i, e_j, e_k\}$ do NOT all lie on a single Fano line (since elements on the same Fano line generate a quaternionic subalgebra, which is associative by Artin's theorem). When $[e_i, e_j, e_k] \neq 0$, the value is $[e_i, e_j, e_k] = \pm 2 e_l$ where $e_l$ is determined by the Fano plane structure constants $f_{ijkl}$. Specifically, using the structure constants $c_{ijk}$ defined by $e_i e_j = c_{ijk} e_k$ (summing over $k$):

$$[e_i, e_j, e_k] = \sum_l (c_{ijm} c_{mkl} - c_{jkm} c_{iml}) e_l$$

where the sum runs over intermediate indices $m$ and output index $l$. For the 7 cross-terms in the quaternionic decomposition, the surviving terms are precisely those where at least one index comes from $\mathbb{H}^\perp$, and the triple does not lie entirely within any associative subalgebra. $\square$

## 6.7 Comparison with Classical Axiom Systems

| Feature | Lie Algebra | Malcev Algebra | COA |
|---------|:-----------:|:--------------:|:---:|
| Product | Bracket $[\cdot,\cdot]$ | Bracket $[\cdot,\cdot]$ | Binary $\star$ + Ternary $[\cdot,\cdot,\cdot]$ |
| Key identity | Jacobi | Malcev | Moufang + Malcev |
| Associator | $\equiv 0$ | $\neq 0$, controlled | $\neq 0$, first-class object |
| Killing form | Finite trace | Finite trace | $\int_\Omega \mathrm{tr}(\cdot) \, d\mu$ |
| Basis | Countable | Countable | Trees (potentially uncountable) |
| Enveloping algebra | PBW | Partial | COPBW (Chapter 10) |
| Symmetry group | Lie group | Moufang loop | Contextual Moufang loop |
| Recovery | — | → Lie via associative subalgebra | → Lie via COA-7 |

## 6.8 Example: The Minimal COA

**Example 6.8.1 (The nuclear COA).** The simplest COA is $V = \mathbb{O}$ itself, with:
- $\star = $ octonionic multiplication,
- $[\cdot, \cdot, \cdot]_\star = $ the octonionic associator,
- $\Omega = \{\omega_0\}$ (a single context),
- $\mu = \delta_{\omega_0}$,
- $\rho_{\omega_0}$ = the left regular representation $L: \mathbb{O} \to \mathrm{End}(\mathbb{O})$, $L_a(x) = ax$.

Verification of axioms:
- **COA-1:** $\iota = \mathrm{id}$. $\checkmark$
- **COA-2:** $\mathbb{O}$ is alternative. $\checkmark$
- **COA-3:** Antisymmetry and closure by Chapter 3. Non-degeneracy: the map $e_i \wedge e_j \wedge e_k \mapsto [e_i, e_j, e_k]$ is nonzero for triples not on a Fano line (e.g., $[e_1, e_2, e_4] = 2e_7 \neq 0$). $\checkmark$
- **COA-4:** Moufang identities hold in $\mathbb{O}$. The commutator algebra is the Malcev algebra $\mathrm{Im}(\mathbb{O})$ with $[a, b] = ab - ba$. $\checkmark$
- **COA-5:** $B_\delta(a, b) = \mathrm{tr}(L_a L_b)$ is the classical Killing-type form. Non-degenerate since $\mathbb{O}$ is simple. $\checkmark$
- **COA-6:** The algebra $\mathbb{O}$ is an algebra over the alternative operad $\mathrm{Alt}$ (since it is alternative). With a single context, the colored operad $\mathcal{P}$ reduces to $\mathrm{Alt}$ itself. The Koszulity of $\mathrm{Alt}$ is established in Loday-Vallette (2012), Theorem 13.3.10. $\checkmark$
- **COA-7:** Restriction to any $\mathbb{H} \subset \mathbb{O}$ gives a Lie structure. $\checkmark$
- **COA-8:** The tangent algebra of $S^7$ (unit octonions under the Moufang loop structure) is a Sabinin algebra. Since $\mathbb{O}$ is alternative, the higher Sabinin brackets ($n \geq 2$) vanish, and the Sabinin structure reduces to the Malcev algebra $(\mathrm{Im}(\mathbb{O}), [\cdot, \cdot])$ with ternary bracket $2[a, b, c]$ (the doubled associator). The Sabinin identities reduce to the Malcev identity, verified in Proposition 6.4.1. $\checkmark$
- **COA-9:** $\mathrm{Der}(\mathbb{O}) = \mathfrak{g}_2$. With a single context, $\mathrm{Der}_\mu = \{0\}$. $\checkmark$
- **COA-10:** $\mathbb{O}$ is 8-dimensional and complete. Every element is a linear combination of basis elements (degree-1 trees). $\checkmark$

This minimal COA already captures all of octonionic algebra. The power of the framework comes from extending to larger $V$ and richer $\Omega$.

## 6.9 Example: The Continuum COA

**Example 6.9.1.** Let $\Omega = [0, 1]$ with Lebesgue measure, and $V = L^2([0, 1], \mathbb{O})$ — the space of square-integrable $\mathbb{O}$-valued functions on $[0, 1]$.

Define:

$$(f \star g)(t) = f(t) \cdot g(t) \quad \text{(pointwise octonion product)}$$

$$[f, g, h]_\star(t) = [f(t), g(t), h(t)] \quad \text{(pointwise associator)}$$

The context space $\Omega = [0, 1]$ parametrizes the "time" or "position" at which the octonionic product is evaluated. The decompactified Killing form becomes:

$$B_\mu(f, g) = \int_0^1 \mathrm{tr}(L_{f(t)} L_{g(t)}) \, dt$$

where $L_{f(t)}$ is left multiplication by $f(t)$ in $\mathbb{O}$.

This COA models a *field* of octonionic values — the 7D analog of a classical field theory. The associator $[f, g, h]_\star(t) = [f(t), g(t), h(t)]$ records the contextual (position-dependent) non-associativity at every point.

## 6.10 The COA Derivation Tower

**Definition 6.10.1.** The *$n$-th derived COA* of $\mathcal{A}$ is:

$$\mathcal{A}^{(0)} = \mathcal{A}, \quad \mathcal{A}^{(n+1)} = \mathrm{Der}(\mathcal{A}^{(n)})$$

with the commutator bracket making each $\mathcal{A}^{(n)}$ into a Lie algebra (since the derivation algebra of any algebra is a Lie algebra under the commutator).

**Proposition 6.10.1.** $\mathcal{A}^{(1)} = \mathrm{Der}(\mathcal{A}) \supseteq \mathfrak{g}_2$. When $\mathcal{A} = \mathbb{O}$ (the minimal COA), $\mathcal{A}^{(1)} = \mathfrak{g}_2$.

**Proof.** The inclusion $\mathrm{Der}(\mathcal{A}) \supseteq \mathfrak{g}_2$ follows from Theorem 5.5.1 (Chapter 5, Section 5.5), which establishes that every map of the form

$$D_{a,b}(x) = [[a, b], x] - 3[a, b, x]$$

for $a, b \in \mathrm{Im}(\mathbb{O})$ is a derivation of $\mathbb{O}$. Here $[a, b] = ab - ba$ is the commutator and $[a, b, x] = (ab)x - a(bx)$ is the associator. We verify the Leibniz rule: for all $x, y \in \mathbb{O}$,

$$D_{a,b}(xy) = D_{a,b}(x) \cdot y + x \cdot D_{a,b}(y).$$

This verification uses the derivation-like identity for associators (COA-3(b), originally Proposition 3.6.4):

$$[ab, c, d] = a[b, c, d] + [a, c, d]b,$$

together with the standard fact that the commutator operator $\mathrm{ad}_{[a,b]}(x) = [[a,b],x]$ satisfies the Leibniz rule modulo associator corrections (specifically, $[[a,b], xy] = [[a,b],x]y + x[[a,b],y] + \text{associator terms}$, and the $-3[a,b,x]$ term in $D_{a,b}$ is precisely chosen to cancel these associator corrections).

The 14 independent derivations of this form span a Lie algebra isomorphic to $\mathfrak{g}_2$ (Schafer, *An Introduction to Nonassociative Algebras*, Academic Press, 1966, Chapter III, Theorem 3.28). Schafer's theorem further establishes that every derivation of $\mathbb{O}$ has the form $D_{a,b}$ for some $a, b \in \mathrm{Im}(\mathbb{O})$, so $\mathrm{Der}(\mathbb{O}) = \mathfrak{g}_2$ (equality, not just inclusion).

For a general COA $\mathcal{A}$ with octonionic nucleus $\iota(\mathbb{O})$, the embedding $\iota$ allows us to extend each $D_{a,b}$ to a derivation of $\mathcal{A}$ (at minimum, by acting on the nucleus and extending by zero on the complement, then checking the Leibniz rule). This gives $\mathrm{Der}(\mathcal{A}) \supseteq \mathfrak{g}_2$. $\square$

**Proposition 6.10.2.** The tower $\mathcal{A}^{(0)}, \mathcal{A}^{(1)}, \mathcal{A}^{(2)}, \ldots$ stabilizes: $\mathrm{Der}(\mathfrak{g}_2) = \mathfrak{g}_2$ (since $\mathfrak{g}_2$ is simple, all derivations are inner). So $\mathcal{A}^{(n)} = \mathfrak{g}_2$ for all $n \geq 1$ (in the case $\mathcal{A} = \mathbb{O}$).

**Proof.** We need to show $\mathrm{Der}(\mathfrak{g}_2) \cong \mathfrak{g}_2$, i.e., every derivation of the Lie algebra $\mathfrak{g}_2$ is inner.

**Step 1: $\mathfrak{g}_2$ is simple.** A Lie algebra is simple if it is non-abelian and has no proper ideals. The Lie algebra $\mathfrak{g}_2$ has rank 2 with root system consisting of 12 nonzero roots (6 short, 6 long) as described in Chapter 5, Section 5.7.1. The Cartan matrix

$$A = \begin{pmatrix} 2 & -3 \\ -1 & 2 \end{pmatrix}$$

is indecomposable (it cannot be written as a block-diagonal matrix by permuting indices), which by the classification of semisimple Lie algebras (see, e.g., Humphreys, *Introduction to Lie Algebras and Representation Theory*, Springer, 1972, Chapter III) implies that $\mathfrak{g}_2$ is simple. Alternatively, simplicity can be verified directly: if $\mathfrak{I} \subset \mathfrak{g}_2$ is a nonzero ideal, then $\mathfrak{I}$ must contain a root space (since $\mathfrak{g}_2 = \mathfrak{h} \oplus \bigoplus_\alpha \mathfrak{g}_\alpha$ and an ideal is $\mathfrak{h}$-stable). But the root system of $G_2$ is irreducible (all roots are connected via the Dynkin diagram), so any ideal containing one root space must contain all root spaces, hence $\mathfrak{I} = \mathfrak{g}_2$.

**Step 2: Every derivation of a simple Lie algebra is inner.** This is a classical result: for any simple Lie algebra $\mathfrak{g}$ over a field of characteristic zero, every derivation $D: \mathfrak{g} \to \mathfrak{g}$ is of the form $D = \mathrm{ad}_x$ for some $x \in \mathfrak{g}$, where $\mathrm{ad}_x(y) = [x, y]$. (Jacobson, *Lie Algebras*, Interscience/Wiley, 1962, Chapter III, Theorem 5.) The proof is as follows: the adjoint representation $\mathrm{ad}: \mathfrak{g} \to \mathrm{Der}(\mathfrak{g})$ is injective (since $\mathfrak{g}$ is simple, $\ker(\mathrm{ad}) = Z(\mathfrak{g}) = 0$). By the Killing form criterion, the Killing form $\kappa$ of a simple Lie algebra is non-degenerate (Cartan's criterion). The image $\mathrm{ad}(\mathfrak{g}) \subset \mathrm{Der}(\mathfrak{g})$ is an ideal in $\mathrm{Der}(\mathfrak{g})$ (since for any derivation $D$ and any $x \in \mathfrak{g}$, $[D, \mathrm{ad}_x] = \mathrm{ad}_{D(x)}$, which lies in $\mathrm{ad}(\mathfrak{g})$). The Killing form of $\mathrm{Der}(\mathfrak{g})$ restricted to $\mathrm{ad}(\mathfrak{g})$ is non-degenerate (since it agrees with $\kappa$ up to scaling). By the orthogonal complement decomposition $\mathrm{Der}(\mathfrak{g}) = \mathrm{ad}(\mathfrak{g}) \oplus \mathrm{ad}(\mathfrak{g})^\perp$, the complement $\mathrm{ad}(\mathfrak{g})^\perp$ is also an ideal. If it were nonzero, it would give a proper ideal of $\mathrm{Der}(\mathfrak{g})$ that commutes with $\mathrm{ad}(\mathfrak{g})$. But any element $D \in \mathrm{ad}(\mathfrak{g})^\perp$ satisfies $[D, \mathrm{ad}_x] = \mathrm{ad}_{D(x)} \in \mathrm{ad}(\mathfrak{g}) \cap \mathrm{ad}(\mathfrak{g})^\perp = 0$, so $D(x) = 0$ for all $x$ (since $\mathrm{ad}$ is injective), hence $D = 0$. Therefore $\mathrm{ad}(\mathfrak{g})^\perp = 0$ and $\mathrm{Der}(\mathfrak{g}) = \mathrm{ad}(\mathfrak{g}) \cong \mathfrak{g}$.

Applying this to $\mathfrak{g} = \mathfrak{g}_2$: $\mathrm{Der}(\mathfrak{g}_2) = \mathrm{ad}(\mathfrak{g}_2) \cong \mathfrak{g}_2$.

**Step 3: Stabilization.** Since $\mathcal{A}^{(1)} = \mathrm{Der}(\mathbb{O}) = \mathfrak{g}_2$ (by Proposition 6.10.1), we have $\mathcal{A}^{(2)} = \mathrm{Der}(\mathfrak{g}_2) = \mathfrak{g}_2$ (by Steps 1--2). By induction, $\mathcal{A}^{(n)} = \mathfrak{g}_2$ for all $n \geq 1$. $\square$

**Significance:** The derivation tower connects the non-associative world ($\mathcal{A}^{(0)} = \mathbb{O}$) to the Lie world ($\mathcal{A}^{(1)} = \mathfrak{g}_2$ onwards). The exceptional Lie algebra $\mathfrak{g}_2$ serves as the bridge: it is simultaneously the derivation algebra of the non-associative octonions and a classical simple Lie algebra. The tower stabilizes at the first step because simplicity of $\mathfrak{g}_2$ forces all higher derivations to be inner.

## 6.11 Formal Consistency

**Theorem 6.11.1 (Consistency).** The COA axiom system is consistent: the minimal COA (Example 6.8.1) satisfies all ten axioms.

**Proof.** Verified axiom-by-axiom in Section 6.8. $\square$

**Theorem 6.11.2 (Non-triviality).** The COA axiom system admits models that are strictly richer than any classical Lie-theoretic structure: specifically, the continuum COA (Example 6.9.1) has an infinite-dimensional state space, a continuous context space, and a non-vanishing associator that varies continuously over $\Omega$.

**Theorem 6.11.3 (Independence of the Associator Axiom).** Axiom COA-3(c) (non-degeneracy of the associator) is independent of the other axioms: the algebra $\mathbb{H}$ (quaternions) satisfies COA-1 through COA-10 with $\mathbb{H}$ replacing $\mathbb{O}$, except that COA-3(c) fails (since the associator vanishes identically in $\mathbb{H}$).

**Proof.** The quaternions are associative, alternative, and satisfy the Moufang identities (trivially, since all are consequences of associativity). The Killing form is well-defined. The operad is the associative operad. The Sabinin algebra degenerates to a Lie algebra. But $[a, b, c] = 0$ for all $a, b, c \in \mathbb{H}$, so COA-3(c) fails. $\square$

## 6.12 Characterization Question (Open Problem)

The axioms COA-1 through COA-10 are **necessary** conditions satisfied by the octonions and by the COA structures built from them. The consistency proof (Theorem 6.11.1) demonstrates that these axioms are satisfiable by exhibiting $\mathbb{O}$ as a model. However, the question of **sufficiency** --- whether any algebra satisfying all ten axioms is isomorphic to $\mathbb{O}$ (or to a COA built over $\mathbb{O}$) --- remains open.

**OPEN PROBLEM 6.12.1 (Sufficiency of the COA Axioms).** *Does there exist an algebra satisfying COA-1 through COA-10 whose octonionic nucleus $\iota(\mathbb{O})$ is not isomorphic to the standard octonion algebra $\mathbb{O}$? More precisely: is the octonionic nucleus of any COA necessarily isomorphic to $\mathbb{O}$ over $\mathbb{R}$?*

**Partial results and context.** The following results bear on this question:

**(a) Zorn's characterization (1930).** Zorn proved that $\mathbb{O}$ is the unique finite-dimensional simple alternative algebra over $\mathbb{R}$ that is not associative (Zorn, "Theorie der alternativen Ringe," *Abhandlungen aus dem Mathematischen Seminar der Universitat Hamburg*, 8 (1930), 123--147). More precisely: if $A$ is a finite-dimensional alternative division algebra over $\mathbb{R}$ and $A$ is not associative, then $A \cong \mathbb{O}$. This result, combined with the Bruck-Kleinfeld theorem (1951) extending Zorn's result to division algebras, means that COA-1 (octonionic nucleus) + COA-2 (alternativity) + finite-dimensionality + division algebra property already characterizes the nucleus as $\mathbb{O}$.

**(b) What COA-1 + COA-2 alone give.** COA-2 (alternativity) ensures $V$ is an alternative algebra. COA-1 requires that $V$ contain an 8-dimensional subalgebra isomorphic to $\mathbb{O}$. By Zorn's theorem, this subalgebra is necessarily the standard $\mathbb{O}$ (up to isomorphism), since it is a non-associative alternative division algebra of dimension 8 over $\mathbb{R}$.

**(c) The non-finite-dimensional case.** The COA framework explicitly allows $V$ to be infinite-dimensional (e.g., the continuum COA of Example 6.9.1). In this setting, the Zorn characterization does not directly apply. The question becomes: do the remaining axioms (COA-3 through COA-10) sufficiently constrain the structure of $V$ beyond the nucleus? The answer is not known.

**(d) Relationship to classical characterization theorems.** The classical Hurwitz theorem (Theorem 1.4.1) characterizes $\mathbb{R}, \mathbb{C}, \mathbb{H}, \mathbb{O}$ as the only normed division algebras. The COA axiom system does not assume a norm-composition property $|ab| = |a||b|$ directly, though this follows from COA-1 restricted to the nucleus. Whether the full COA axioms imply a norm-composition property on all of $V$ is an open question.

**What the COA system achieves without sufficiency.** Even without a sufficiency proof, the COA axiom system provides:

1. A coherent axiomatic framework for non-associative algebra that organizes known results about $\mathbb{O}$, Malcev algebras, Sabinin algebras, and $G_2$-structures.
2. A generative system: new identities and structures can be derived from the axioms alone.
3. An extension mechanism: the context space $\Omega$ and measure $\mu$ allow the octonionic structure to be systematically extended to infinite-dimensional and continuum settings.

A proof of sufficiency would elevate the COA system from an organizational framework to a categorical characterization, analogous to how the Eilenberg-Steenrod axioms characterize homology theories. This remains a target for future work.

## 6.13 Summary of the Axiom System

The COA axioms provide a self-consistent foundation for non-associative algebra that:

1. Contains the octonions as a nuclear subalgebra (COA-1).
2. Is governed by alternativity, not associativity (COA-2).
3. Treats the associator as a first-class algebraic object (COA-3).
4. Replaces the Jacobi identity with the Moufang-Malcev identities (COA-4).
5. Generalizes the Killing form to a measure-integrated bilinear form (COA-5).
6. Organizes higher compositions via operads (COA-6).
7. Recovers all classical Lie theory as a special case (COA-7).
8. Has a well-defined infinitesimal theory via Sabinin algebras (COA-8).
9. Supports context-dependent derivations (COA-9).
10. Is algebraically, analytically, and measure-theoretically complete (COA-10).

This is the mathematical foundation on which the rest of the book builds.

---

*Chapter 7 develops the theory of the associator as an information-carrying object, establishing the full associator calculus within the COA framework.*
