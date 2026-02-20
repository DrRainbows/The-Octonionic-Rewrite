> **Rigor Level: CONSTRUCTIVE** — Mathematical structures defined and explored; some existence results sketched rather than fully proven.
> **Novelty: EXTENSION** — Measure-theoretic basis theory for non-associative algebras is a new development; measure theory foundations are classical.

# Chapter 14: Measure-Theoretic Bases

## 14.1 Introduction

Classical algebra is built on countable (usually finite) bases. A vector space $V$ has a basis $\{e_i\}_{i \in I}$, and every element is a *finite* linear combination $v = \sum_{i} c_i e_i$. An operad $\mathcal{P}$ has operations of finite arity $\mathcal{P}(n)$ for $n \in \mathbb{N}$. Universal enveloping algebras have PBW bases indexed by finite sequences.

This chapter removes the finiteness constraint. We define operads with **uncountable arity** via colimits over measure spaces, show how to perform algebra with **uncountable bases** by replacing finite summation with integration, and formalize the notion of **contextual arity** that underlies the decompactified Killing form of Chapter 8 and the COPBW construction of Chapter 10.

The core insight: when the "number of ways to compose" is not a natural number but a measurable set, the algebraic operations must be defined via integration rather than summation. This is not a metaphor—it is a precise mathematical framework.

---

## 14.2 Motivation: Why Uncountable Arity?

### 14.2.1 The Limitation of Finite Arity

In a classical operad $\mathcal{P}$, an operation $\theta \in \mathcal{P}(n)$ takes $n$ inputs and produces one output. The composition:
$$\gamma : \mathcal{P}(k) \times \mathcal{P}(n_1) \times \cdots \times \mathcal{P}(n_k) \to \mathcal{P}(n_1 + \cdots + n_k)$$
is parameterized by finite natural numbers $k, n_1, \ldots, n_k \in \mathbb{N}$.

This is adequate for algebraic operations (binary products, ternary brackets, etc.) but insufficient for:
1. **Continuous symmetry groups:** A rotation in $SO(7)$ is parameterized by 21 continuous parameters. The "arity" of the rotation operation is the uncountable set $SO(7)$.
2. **The decompactified Killing form:** $B_\mu(X, Y) = \int_\Omega \operatorname{tr}(\operatorname{ad}_X^{(\omega)} \circ \operatorname{ad}_Y^{(\omega)}) \, d\mu(\omega)$ involves integration over an uncountable context space $\Omega$.
3. **Contextual bases:** In the COPBW construction, the "contexts" $\omega \in \Omega$ each contribute a basis direction. An uncountable $\Omega$ requires uncountable bases.
4. **Physical fields:** A field $\phi(\mathbf{x})$ assigns a value to each point $\mathbf{x} \in \mathbb{R}^7$—an uncountable "basis" of spatial positions.

### 14.2.2 The Goal

We seek a framework where:
- Operations have **measurable sets** as arities (not just natural numbers).
- Composition involves **integration** over these sets.
- Classical finite-arity operads are recovered as the special case of counting measure on finite sets.
- The COPBW basis (Chapter 10) extends naturally to uncountable index sets.

---

## 14.3 Measure Spaces as Arity Sets

### 14.3.1 Definitions

**Definition 14.1 (Arity measure space).** An *arity measure space* is a triple $(\Omega, \Sigma, \mu)$ where:
- $\Omega$ is a set (the "arity set" or "context space").
- $\Sigma$ is a $\sigma$-algebra on $\Omega$.
- $\mu$ is a $\sigma$-finite measure on $(\Omega, \Sigma)$.

**Examples:**
1. **Finite discrete:** $\Omega = \{1, \ldots, n\}$, $\Sigma = 2^\Omega$, $\mu = $ counting measure. Arity $= n$.
2. **Countable discrete:** $\Omega = \mathbb{N}$, $\mu = $ counting measure. Arity $= \aleph_0$.
3. **Continuous compact:** $\Omega = S^6$ (the 6-sphere), $\mu = $ volume measure on $S^6$. Arity $= $ uncountable.
4. **Continuous non-compact:** $\Omega = \mathbb{R}^7$, $\mu = $ Lebesgue measure. Arity $= $ uncountable.
5. **Contextual:** $\Omega = G_2$ (the automorphism group of $\mathbb{O}$), $\mu = $ Haar measure. Arity $= $ uncountable, with group structure.

### 14.3.2 Measurable Operations

**Definition 14.2 (Measurable operation).** Let $V$ be a Banach space (or more generally, a topological $\mathbb{O}$-module). A *measurable operation of arity $(\Omega, \mu)$* is a measurable map:
$$\theta : V^{\Omega} \to V$$
where $V^{\Omega} = \{f : \Omega \to V \mid f \text{ is measurable}\}$ is the space of measurable $V$-valued functions on $\Omega$, and $\theta$ is expressed as:
$$\theta(f) = \int_{\Omega} K(\omega) f(\omega) \, d\mu(\omega)$$
for some measurable kernel $K : \Omega \to \operatorname{End}(V)$.

**Remark 14.3.** In the finite case ($\Omega = \{1, \ldots, n\}$, $\mu = $ counting measure), this reduces to:
$$\theta(v_1, \ldots, v_n) = \sum_{i=1}^{n} K_i v_i$$
which is a classical $n$-ary operation.

### 14.3.3 The Integral Replaces Summation

The fundamental principle:

| Finite arity | Uncountable arity |
|-------------|-------------------|
| Sum $\sum_{i=1}^{n}$ | Integral $\int_\Omega d\mu(\omega)$ |
| Basis $\{e_i\}_{i=1}^n$ | Continuous basis $\{e_\omega\}_{\omega \in \Omega}$ |
| Coefficients $c_i \in \mathbb{K}$ | Coefficient function $c(\omega) \in L^2(\Omega, \mu)$ |
| Linear combination $\sum c_i e_i$ | Integral expansion $\int c(\omega) e_\omega \, d\mu(\omega)$ |
| Trace $\sum_{i} A_{ii}$ | Integral trace $\int_\Omega A(\omega, \omega) \, d\mu(\omega)$ |
| Kronecker delta $\delta_{ij}$ | Dirac distribution $\delta(\omega - \omega')$ |

---

## 14.4 Operads with Uncountable Arity

### 14.4.1 The Category of Measure Spaces

Let $\mathbf{Meas}$ denote the category whose objects are $\sigma$-finite measure spaces $(\Omega, \Sigma, \mu)$ and whose morphisms are measurable maps $f : \Omega_1 \to \Omega_2$ that are *measure-compatible* (either measure-preserving or absolutely continuous).

### 14.4.2 Definition of a Measure-Theoretic Operad

**Definition 14.4 (Measure-theoretic operad).** A *measure-theoretic operad* $\mathcal{P}$ consists of:

1. **Operation spaces.** For each $\sigma$-finite measure space $(\Omega, \mu)$, a Banach space (or topological vector space) $\mathcal{P}(\Omega, \mu)$ of "operations of arity $(\Omega, \mu)$."

2. **Composition.** For $\sigma$-finite measure spaces $(\Lambda, \nu)$ and $\{(\Omega_\lambda, \mu_\lambda)\}_{\lambda \in \Lambda}$, a continuous linear map:
$$\gamma : \mathcal{P}(\Lambda, \nu) \times \int_\Lambda^{\oplus} \mathcal{P}(\Omega_\lambda, \mu_\lambda) \, d\nu(\lambda) \to \mathcal{P}\left(\int_\Lambda \Omega_\lambda \, d\nu(\lambda), \, \tilde{\mu}\right)$$
where:
- $\int_\Lambda^{\oplus} \mathcal{P}(\Omega_\lambda, \mu_\lambda) \, d\nu(\lambda)$ is the *direct integral* of the operation spaces over $\Lambda$.
- $\int_\Lambda \Omega_\lambda \, d\nu(\lambda)$ is the *fibered measure space* with measure $\tilde{\mu}$ defined by $\tilde{\mu}(E) = \int_\Lambda \mu_\lambda(E \cap \Omega_\lambda) \, d\nu(\lambda)$.

3. **Unit.** An element $\operatorname{id} \in \mathcal{P}(\{*\}, \delta_*)$ (the identity operation on a single point with Dirac measure).

4. **Associativity.** The composition satisfies the analog of operad associativity, expressed as commutativity of the appropriate diagram involving iterated direct integrals.

5. **Equivariance.** For any measure-preserving isomorphism $\sigma : (\Omega_1, \mu_1) \to (\Omega_2, \mu_2)$, there is an isomorphism $\sigma^* : \mathcal{P}(\Omega_1, \mu_1) \to \mathcal{P}(\Omega_2, \mu_2)$ compatible with composition.

### 14.4.3 Recovery of Classical Operads

**Proposition 14.5.** Let $\mathcal{P}$ be a measure-theoretic operad. Restricting to finite sets $\Omega_n = \{1, \ldots, n\}$ with counting measure gives a classical operad $\mathcal{P}_{\text{fin}}$:
$$\mathcal{P}_{\text{fin}}(n) = \mathcal{P}(\Omega_n, \#)$$
with classical composition and symmetric group action (from permutations of $\Omega_n$).

*Proof.* The direct integral over a finite set with counting measure reduces to a finite direct sum. The fibered measure space reduces to a disjoint union. The composition, unit, associativity, and equivariance conditions reduce to the classical operad axioms. $\square$

### 14.4.4 The Endomorphism Operad

**Example 14.6.** For a Hilbert space $\mathcal{H}$, the *measure-theoretic endomorphism operad* is:
$$\mathcal{E}nd(\mathcal{H})(\Omega, \mu) = \mathcal{B}(L^2(\Omega, \mu; \mathcal{H}), \mathcal{H})$$
the space of bounded linear operators from $L^2(\Omega, \mu; \mathcal{H})$ (the Hilbert space of $\mathcal{H}$-valued $L^2$ functions on $\Omega$) to $\mathcal{H}$.

An element $\theta \in \mathcal{E}nd(\mathcal{H})(\Omega, \mu)$ acts as:
$$\theta(f) = \int_\Omega K(\omega) f(\omega) \, d\mu(\omega)$$
where $K : \Omega \to \mathcal{B}(\mathcal{H})$ is a measurable operator-valued kernel.

Composition:
$$(\gamma(\theta; \{\phi_\lambda\}_\lambda))(f) = \theta\left(\lambda \mapsto \phi_\lambda\left(\omega \mapsto f(\lambda, \omega)\right)\right)$$
which is a nested integral:
$$= \int_\Lambda K_\theta(\lambda) \left(\int_{\Omega_\lambda} K_{\phi_\lambda}(\omega) f(\lambda, \omega) \, d\mu_\lambda(\omega)\right) d\nu(\lambda)$$

This is the integral analog of the classical composition of multi-linear maps.

---

## 14.5 Algebras with Uncountable Bases

### 14.5.1 Continuous Bases

**Definition 14.7 (Continuous basis).** Let $\mathcal{H}$ be a Hilbert space and $(\Omega, \mu)$ a $\sigma$-finite measure space. A *continuous basis* (or *rigged basis*) of $\mathcal{H}$ indexed by $\Omega$ is a measurable map $e : \Omega \to \mathcal{H}'$ (the dual space or a distributional extension) such that:

1. **Resolution of identity:**
$$\int_\Omega |e_\omega\rangle\langle e_\omega| \, d\mu(\omega) = I$$
where $|e_\omega\rangle\langle e_\omega|$ is the rank-one operator $v \mapsto \langle e_\omega, v\rangle e_\omega$.

2. **Expansion:** Every $v \in \mathcal{H}$ can be written as:
$$v = \int_\Omega c(\omega) e_\omega \, d\mu(\omega)$$
where $c(\omega) = \langle e_\omega, v \rangle \in L^2(\Omega, \mu)$.

3. **Parseval identity:**
$$\|v\|^2 = \int_\Omega |c(\omega)|^2 \, d\mu(\omega)$$

**Example 14.8 (Fourier basis).** $\mathcal{H} = L^2(\mathbb{R})$, $\Omega = \mathbb{R}$, $\mu = $ Lebesgue measure, $e_\omega(x) = \frac{1}{\sqrt{2\pi}} e^{i\omega x}$. This is the Fourier transform: every $f \in L^2(\mathbb{R})$ expands as $f(x) = \int_{\mathbb{R}} \hat{f}(\omega) e^{i\omega x} \, d\omega$.

**Example 14.9 (Position basis in quantum mechanics).** $\mathcal{H} = L^2(\mathbb{R}^7)$, $\Omega = \mathbb{R}^7$, $\mu = $ Lebesgue measure, $e_{\mathbf{x}_0}(\mathbf{x}) = \delta(\mathbf{x} - \mathbf{x}_0)$. This is the "position basis" $|\mathbf{x}_0\rangle$.

### 14.5.2 Octonionic Continuous Bases

For the octonionic framework, we need continuous bases for $\mathbb{O}$-modules.

**Definition 14.10 (Octonionic continuous basis).** Let $M$ be an $\mathbb{O}$-module with an inner product $\langle \cdot, \cdot \rangle_{\mathbb{O}} : M \times M \to \mathbb{O}$ (taking values in $\mathbb{O}$, not $\mathbb{R}$). A *continuous $\mathbb{O}$-basis* indexed by $(\Omega, \mu)$ is a measurable map $e : \Omega \to M'$ such that:

$$v = \int_\Omega e_\omega \cdot c(\omega) \, d\mu(\omega)$$
where $c(\omega) = \langle e_\omega, v \rangle_{\mathbb{O}} \in \mathbb{O}$ and $e_\omega \cdot c(\omega)$ uses right $\mathbb{O}$-multiplication.

**Caution.** The resolution of identity becomes:
$$\int_\Omega |e_\omega\rangle \cdot \langle e_\omega| \, d\mu(\omega) = I$$
but the composition $|e_\omega\rangle \cdot \langle e_\omega|$ is the operator $v \mapsto e_\omega \cdot \langle e_\omega, v\rangle_{\mathbb{O}}$. Due to non-associativity:
$$e_\omega \cdot \langle e_\omega, \lambda v\rangle_{\mathbb{O}} \neq \lambda \cdot (e_\omega \cdot \langle e_\omega, v\rangle_{\mathbb{O}})$$
in general. The resolution of identity holds as a *real-linear* identity but NOT as an $\mathbb{O}$-linear identity.

### 14.5.3 Integration as Basis Expansion

The octonionic integral expansion:
$$v = \int_\Omega e_\omega \cdot c(\omega) \, d\mu(\omega)$$

replaces the finite sum $v = \sum_i e_i c_i$ of classical $\mathbb{O}$-module theory. The key differences:

1. **Convergence.** The integral converges in the $L^2$ sense: $\int_\Omega |c(\omega)|^2 d\mu(\omega) < \infty$.

2. **Coefficient function.** $c : \Omega \to \mathbb{O}$ is a measurable octonion-valued function. It lives in $L^2(\Omega, \mu; \mathbb{O})$.

3. **Non-associativity.** The product $e_\omega \cdot c(\omega)$ involves a non-associative product at each point $\omega$. Different parenthesizations of the integrand give different results:
$$\int_\Omega (e_\omega \cdot c(\omega)) \cdot f(\omega) \, d\mu(\omega) \neq \int_\Omega e_\omega \cdot (c(\omega) \cdot f(\omega)) \, d\mu(\omega)$$

The difference is:
$$\int_\Omega [e_\omega, c(\omega), f(\omega)] \, d\mu(\omega)$$

This is the **integrated associator**, a measure-theoretic analog of the algebraic associator. It vanishes when the integrand is alternative (e.g., when $c(\omega)$ and $f(\omega)$ are always parallel as octonions).

---

## 14.6 Colimit Construction

### 14.6.1 Directed Systems of Finite Approximations

The key idea for rigorous construction: define the measure-theoretic operad as a **colimit** of finite-arity operads over finer and finer partitions of the measure space.

**Definition 14.11.** Let $(\Omega, \mu)$ be a $\sigma$-finite measure space. A *measurable partition* of $\Omega$ is a countable family $\mathcal{P} = \{A_1, A_2, \ldots\}$ of disjoint measurable sets with $\Omega = \bigsqcup_i A_i$ and $0 < \mu(A_i) < \infty$ for all $i$.

The set of measurable partitions is a directed set under refinement: $\mathcal{P} \preceq \mathcal{Q}$ if $\mathcal{Q}$ refines $\mathcal{P}$ (every set in $\mathcal{Q}$ is contained in some set of $\mathcal{P}$).

**Definition 14.12 (Finite approximation).** Given a partition $\mathcal{P} = \{A_1, \ldots, A_n\}$ of $\Omega$ (using only finitely many sets of positive measure), define the *finite-arity approximation*:
$$\mathcal{P}_{\mathcal{P}}(n) = \mathcal{P}(\Omega_n, \#) \quad \text{(the classical operad at arity } n\text{)}$$

with the identification: the operation slot corresponding to $A_i$ represents "all inputs from context $\omega \in A_i$," and the measure $\mu(A_i)$ serves as a weight.

### 14.6.2 The Colimit

**Definition 14.13.** The *measure-theoretic operad* $\mathcal{P}(\Omega, \mu)$ is defined as the colimit:
$$\mathcal{P}(\Omega, \mu) = \varinjlim_{\mathcal{P}} \mathcal{P}_{\mathcal{P}}$$
over the directed system of finite partitions, with transition maps defined by refinement.

Concretely: an element $\theta \in \mathcal{P}(\Omega, \mu)$ is represented by a *compatible family* $\{\theta_{\mathcal{P}}\}_{\mathcal{P}}$ where $\theta_{\mathcal{P}} \in \mathcal{P}_{\mathcal{P}}(|\mathcal{P}|)$ and for any refinement $\mathcal{P} \preceq \mathcal{Q}$, $\theta_{\mathcal{Q}}$ restricts to $\theta_{\mathcal{P}}$ under the coarsening map.

**Theorem 14.14.** The colimit $\mathcal{P}(\Omega, \mu) = \varinjlim_{\mathcal{P}} \mathcal{P}_{\mathcal{P}}$ exists in the category of topological vector spaces and satisfies the measure-theoretic operad axioms (Definition 14.4). In particular, the induced composition is associative and unital.

*Proof.*

We establish existence, the operad structure (composition, associativity, unitality, equivariance), and the topology in order.

**Part 1: Existence of the colimit.**

The directed system is indexed by the directed set $(\mathfrak{Part}(\Omega, \mu), \preceq)$ of finite measurable partitions of $\Omega$ ordered by refinement. For each partition $\mathcal{P} = \{A_1, \ldots, A_n\}$, we have the finite-arity operad space $\mathcal{P}_{\mathcal{P}}(n) = \mathcal{P}(\Omega_n, \#)$.

For $\mathcal{P} \preceq \mathcal{Q}$ (i.e., $\mathcal{Q}$ refines $\mathcal{P}$), define the transition map $\phi_{\mathcal{P}\mathcal{Q}} : \mathcal{P}_{\mathcal{P}} \to \mathcal{P}_{\mathcal{Q}}$ as follows. If $\mathcal{P} = \{A_1, \ldots, A_n\}$ and each $A_i$ is partitioned in $\mathcal{Q}$ as $A_i = \bigsqcup_{j \in J_i} B_j$, then an operation $\theta_{\mathcal{P}} \in \mathcal{P}_{\mathcal{P}}(n)$ with kernel values $K_i$ (one per partition cell $A_i$) is sent to $\theta_{\mathcal{Q}} \in \mathcal{P}_{\mathcal{Q}}(|\mathcal{Q}|)$ with kernel value $K_j' = K_i \cdot \frac{\mu(B_j)}{\mu(A_i)}$ for each $B_j \subseteq A_i$. This ensures that the approximation to the integral is preserved:
$$\sum_{j \in J_i} K_j' \cdot f_j \cdot \mu(B_j) = K_i \cdot \sum_{j \in J_i} \frac{\mu(B_j)}{\mu(A_i)} f_j \cdot \mu(B_j)$$
which converges to $K_i \cdot \int_{A_i} f(\omega) \, d\mu(\omega)$ as the partition refines.

The transition maps satisfy the cocycle condition: for $\mathcal{P} \preceq \mathcal{Q} \preceq \mathcal{R}$, each cell $A_i$ of $\mathcal{P}$ is refined by $\mathcal{Q}$ into cells $\{B_j\}$, each of which is further refined by $\mathcal{R}$ into cells $\{C_k\}$. The composition $\phi_{\mathcal{Q}\mathcal{R}} \circ \phi_{\mathcal{P}\mathcal{Q}}$ assigns to $C_k \subseteq B_j \subseteq A_i$ the kernel value $K_i \cdot \frac{\mu(B_j)}{\mu(A_i)} \cdot \frac{\mu(C_k)}{\mu(B_j)} = K_i \cdot \frac{\mu(C_k)}{\mu(A_i)}$, which equals $\phi_{\mathcal{P}\mathcal{R}}(\theta_{\mathcal{P}})$ evaluated at $C_k$. So $\phi_{\mathcal{Q}\mathcal{R}} \circ \phi_{\mathcal{P}\mathcal{Q}} = \phi_{\mathcal{P}\mathcal{R}}$.

The colimit is the algebraic colimit in the category of vector spaces:
$$\mathcal{P}(\Omega, \mu) = \left(\bigsqcup_{\mathcal{P}} \mathcal{P}_{\mathcal{P}}\right) / \sim$$
where $\theta_{\mathcal{P}} \sim \theta_{\mathcal{Q}}'$ if there exists $\mathcal{R} \succeq \mathcal{P}, \mathcal{Q}$ with $\phi_{\mathcal{P}\mathcal{R}}(\theta_{\mathcal{P}}) = \phi_{\mathcal{Q}\mathcal{R}}(\theta_{\mathcal{Q}}')$. This is a standard colimit construction (see Mac Lane, *Categories for the Working Mathematician*, Springer GTM 5, 1971, Chapter III, Section 3, Theorem 1).

**Part 2: Composition in the colimit.**

We define composition on representatives and verify well-definedness. Let $[\theta] \in \mathcal{P}(\Lambda, \nu)$ and $[\phi_\lambda] \in \mathcal{P}(\Omega_\lambda, \mu_\lambda)$ for $\lambda \in \Lambda$. Choose representatives: $\theta$ is represented at some partition $\mathcal{P}_\Lambda$ of $\Lambda$, and each $\phi_\lambda$ is represented at some partition $\mathcal{P}_{\Omega_\lambda}$ of $\Omega_\lambda$.

For the finite partition $\mathcal{P}_\Lambda = \{\Lambda_1, \ldots, \Lambda_m\}$, choose a representative $\lambda_i \in \Lambda_i$ for each cell. The "inner" operation for cell $\Lambda_i$ is $\phi_{\lambda_i}$, represented at partition $\mathcal{P}_{\Omega_{\lambda_i}} = \{\Omega_{i,1}, \ldots, \Omega_{i,n_i}\}$.

The finite composition in the classical operad is:
$$\gamma_{\text{fin}}(\theta_{\mathcal{P}_\Lambda}; \phi_{\lambda_1, \mathcal{P}_1}, \ldots, \phi_{\lambda_m, \mathcal{P}_m}) \in \mathcal{P}_{\mathcal{R}}(n_1 + \cdots + n_m)$$
where $\mathcal{R}$ is the partition of $\int_\Lambda \Omega_\lambda \, d\nu(\lambda)$ into the cells $\{\Omega_{i,j}\}_{i=1,\ldots,m; \; j=1,\ldots,n_i}$.

**Well-definedness.** Suppose we choose a finer partition $\mathcal{Q}_\Lambda \succeq \mathcal{P}_\Lambda$, with each $\Lambda_i$ split into $\{\Lambda_{i,1}, \ldots, \Lambda_{i,s_i}\}$. The refined outer operation $\phi_{\mathcal{P}_\Lambda \mathcal{Q}_\Lambda}(\theta)$ has kernel values $K_i \cdot \frac{\mu(\Lambda_{i,r})}{\mu(\Lambda_i)}$ on each sub-cell $\Lambda_{i,r}$. The inner operations on the sub-cells $\Lambda_{i,r}$ are all refinements of $\phi_{\lambda_i}$ (since they arise from the same element of the colimit). The finite composition at the refined level factors through the coarser composition by the compatibility of the transition maps with the classical operad composition, because both the kernel weighting and the partition cell structure refine consistently. Therefore the equivalence class in the colimit is independent of the chosen representatives.

**Part 3: Associativity of composition.**

We must verify that for operations $\theta \in \mathcal{P}(\Lambda, \nu)$, $\{\phi_\lambda\}_{\lambda \in \Lambda}$ with $\phi_\lambda \in \mathcal{P}(\Gamma_\lambda, \rho_\lambda)$, and $\{\psi_{\lambda,\gamma}\}_{\gamma \in \Gamma_\lambda}$ with $\psi_{\lambda,\gamma} \in \mathcal{P}(\Omega_{\lambda,\gamma}, \mu_{\lambda,\gamma})$, the two ways of composing are equal:

$$\gamma(\gamma(\theta; \{\phi_\lambda\}); \{\psi_{\lambda,\gamma}\}) = \gamma(\theta; \{\gamma(\phi_\lambda; \{\psi_{\lambda,\gamma}\}_\gamma)\}_\lambda)$$

Choose partitions $\mathcal{P}_\Lambda$, $\mathcal{P}_{\Gamma_\lambda}$, and $\mathcal{P}_{\Omega_{\lambda,\gamma}}$ fine enough that all three operations $\theta$, $\phi_\lambda$, $\psi_{\lambda,\gamma}$ are represented. At the finite-partition level, both sides reduce to the iterated composition:

*Left side:* First compose $\theta$ with $\{\phi_\lambda\}$ in the finite operad (using partitions $\mathcal{P}_\Lambda$ and $\mathcal{P}_{\Gamma_\lambda}$), obtaining an operation at arity $\sum_i |\mathcal{P}_{\Gamma_{\lambda_i}}|$. Then compose this with the $\psi$'s at arity $\sum_{i,j} |\mathcal{P}_{\Omega_{\lambda_i, \gamma_j}}|$.

*Right side:* First compose each $\phi_\lambda$ with $\{\psi_{\lambda,\gamma}\}_\gamma$ in the finite operad, obtaining operations at arity $\sum_j |\mathcal{P}_{\Omega_{\lambda,\gamma_j}}|$. Then compose $\theta$ with these.

Both sides produce the same element of the finite-arity operad at the common refinement partition, because the classical (finite-arity) operad satisfies associativity (this is one of the operad axioms for $\mathcal{P}_{\text{fin}}$, see May, J.P., *The Geometry of Iterated Loop Spaces*, Lecture Notes in Mathematics 271, Springer, 1972, Definition 1.1). Since the colimit equivalence class depends only on the value at sufficiently fine partitions, the two sides represent the same element of $\mathcal{P}(\Omega, \mu)$.

**Part 4: Unitality.**

The unit is $\operatorname{id} \in \mathcal{P}(\{*\}, \delta_*)$, represented at the trivial partition $\{*\}$ of the single-point space. For any $\theta \in \mathcal{P}(\Omega, \mu)$ represented at partition $\mathcal{P} = \{A_1, \ldots, A_n\}$:

*Left unitality:* $\gamma(\theta; \operatorname{id}, \ldots, \operatorname{id})$ is the composition where each input slot $A_i$ receives the identity operation. At the finite level, the classical operad unit axiom gives $\gamma_{\text{fin}}(\theta_{\mathcal{P}}; \operatorname{id}, \ldots, \operatorname{id}) = \theta_{\mathcal{P}}$. Passing to the colimit preserves this equality.

*Right unitality:* $\gamma(\operatorname{id}; \theta)$ composes the identity on a single point with $\theta$. The fibered measure space $\int_{\{*\}} \Omega \, d\delta_*$ is canonically identified with $(\Omega, \mu)$, and the classical unit axiom gives $\gamma_{\text{fin}}(\operatorname{id}; \theta_{\mathcal{P}}) = \theta_{\mathcal{P}}$. Again, this passes to the colimit.

**Part 5: Equivariance.**

For a measure-preserving isomorphism $\sigma : (\Omega_1, \mu_1) \to (\Omega_2, \mu_2)$, $\sigma$ induces a bijection on finite measurable partitions ($\mathcal{P} \mapsto \sigma(\mathcal{P})$) preserving refinement and cell measures. The induced map $\sigma^* : \mathcal{P}_{\mathcal{P}} \to \mathcal{P}_{\sigma(\mathcal{P})}$ commutes with transition maps and hence passes to a well-defined isomorphism $\sigma^* : \mathcal{P}(\Omega_1, \mu_1) \to \mathcal{P}(\Omega_2, \mu_2)$. Compatibility with composition follows from the classical equivariance (symmetric group action) at each finite level.

**Part 6: Topology.**

Equip $\mathcal{P}(\Omega, \mu)$ with the inductive limit (colimit) topology: $U \subseteq \mathcal{P}(\Omega, \mu)$ is open if and only if $\phi_{\mathcal{P}}^{-1}(U)$ is open in $\mathcal{P}_{\mathcal{P}}$ for every partition $\mathcal{P}$, where $\phi_{\mathcal{P}} : \mathcal{P}_{\mathcal{P}} \to \mathcal{P}(\Omega, \mu)$ is the canonical map. The composition map is continuous in this topology because it is continuous at each finite level (being a multi-linear map of finite-dimensional vector spaces) and the colimit topology is the finest topology making all canonical maps continuous (Schaefer, H.H., *Topological Vector Spaces*, Springer GTM 3, 1971, Chapter II, Section 6). $\square$

### 14.6.3 Convergence

**Proposition 14.15.** For the endomorphism operad $\mathcal{E}nd(\mathcal{H})$, the colimit construction gives:
$$\mathcal{E}nd(\mathcal{H})(\Omega, \mu) = \mathcal{B}(L^2(\Omega, \mu; \mathcal{H}), \mathcal{H})$$

In other words, the colimit of finite-dimensional multi-linear maps converges to the space of bounded operators on the $L^2$ function space.

*Proof.* A compatible family $\{\theta_{\mathcal{P}}\}_{\mathcal{P}}$ defines, for each partition, a multi-linear map $\theta_{\mathcal{P}} : \mathcal{H}^{|\mathcal{P}|} \to \mathcal{H}$. As the partition refines, $\theta_{\mathcal{P}}$ approximates the integral operator:
$$\theta(f) = \lim_{|\mathcal{P}| \to \infty} \sum_{i=1}^{|\mathcal{P}|} K_i \cdot f_i \cdot \mu(A_i) = \int_\Omega K(\omega) f(\omega) \, d\mu(\omega)$$

The convergence is in the strong operator topology when the kernel $K(\omega)$ is strongly measurable. $\square$

---

## 14.7 The COPBW Basis with Uncountable Index

### 14.7.1 The Extended COPBW Basis

In Chapter 10, the COPBW basis is indexed by:
$$\mathcal{B} = \{a_{\alpha_0} \cdot L_k(a_{\alpha_1} x_{i_1}, \ldots, a_{\alpha_k} x_{i_k}) : k \geq 0, \, i_1 \leq \cdots \leq i_k, \, \alpha_j \in \Lambda\}$$

When the algebra $A$ has an uncountable continuous basis indexed by $(\Omega, \mu)$ (as in the decompactified Killing form setting), the COPBW basis becomes:

$$\mathcal{B}_\mu = \left\{ a(\omega_0) \cdot L_k(a(\omega_1) x(\omega_1), \ldots, a(\omega_k) x(\omega_k)) : k \geq 0, \, \omega_1 \preceq_\mu \cdots \preceq_\mu \omega_k \right\}$$

where:
- $x : \Omega \to A$ is the continuous basis of $A$.
- $a : \Omega \to \mathbb{O}$ is the octonionic coefficient function.
- $\omega_1 \preceq_\mu \cdots \preceq_\mu \omega_k$ is a measure-theoretic ordering (well-ordering on the support of $\mu$, defined up to $\mu$-null sets).

**Definition 14.16 (Continuous tree monomial).** A *continuous tree monomial* of weight $k$ is:
$$T_k[c] = \int_{\Omega^k} c(\omega_1, \ldots, \omega_k) \, L_k(x(\omega_1), \ldots, x(\omega_k)) \, d\mu^k(\omega_1, \ldots, \omega_k)$$

where $c \in L^2_{\text{sym}}(\Omega^k, \mu^k; \mathbb{O})$ is a symmetric (in the appropriate tree-ordered sense) octonionic coefficient function.

### 14.7.2 The Continuous COPBW Theorem

**Theorem 14.17 (Continuous COPBW).** Let $A$ be an $\mathbb{O}$-algebra with continuous basis indexed by $(\Omega, \mu)$. Then $U_{\mathbb{O}}(A)$ has a "basis" (in the $L^2$ sense) of continuous tree monomials:

$$U_{\mathbb{O}}(A) \cong \bigoplus_{k \geq 0} L^2_{\text{tree}}(\Omega^k, \mu^k; \mathbb{O})$$

where $L^2_{\text{tree}}$ denotes the $L^2$ functions on $\Omega^k$ that satisfy the tree-ordering condition (the continuous analog of weakly increasing indices) and the octonionic coefficient structure.

**More precisely:** the weight-$k$ component is:
$$U_{\mathbb{O}}(A)_k \cong L^2_{\text{sym}}(\Omega^k, \mu^k; \mathbb{O}) \otimes_{\text{alt}} \mathbb{R}[\mathcal{T}_k]$$

where $\mathbb{R}[\mathcal{T}_k]$ is the vector space spanned by tree shapes of weight $k$ (finitely many, by the Catalan numbers), and $\otimes_{\text{alt}}$ is the alternative tensor product.

*Proof.* The proof proceeds in four steps: finite approximation, colimit passage, completeness (spanning), and independence.

**Step 1: Finite approximation.** Let $\mathcal{P} = \{A_1, \ldots, A_n\}$ be a finite measurable partition of $\Omega$ with $0 < \mu(A_i) < \infty$ for each $i$. Define the averaged basis element for each cell:
$$x_{A_i} = \frac{1}{\mu(A_i)} \int_{A_i} x(\omega) \, d\mu(\omega) \in A$$

This gives a finite set of generators $\{x_{A_1}, \ldots, x_{A_n}\}$. By the COPBW theorem (Theorem 10.12), the enveloping algebra $U_{\mathbb{O}}(\operatorname{span}\{x_{A_i}\})$ has a hierarchical tree monomial basis:
$$\mathcal{B}_{\mathcal{P}} = \left\{ a_{\alpha_0} \cdot L_k(a_{\alpha_1} x_{A_{i_1}}, \ldots, a_{\alpha_k} x_{A_{i_k}}) : k \geq 0, \; i_1 \leq \cdots \leq i_k, \; \alpha_j \in \Lambda \right\}$$

The weight-$k$ component is $U_{\mathbb{O}}(\operatorname{span}\{x_{A_i}\})_k \cong \mathbb{O}^{|\Lambda|^{k+1}} \otimes \operatorname{Sym}^k_{\text{weak}}(\{A_1, \ldots, A_n\})$, where $\operatorname{Sym}^k_{\text{weak}}$ denotes weakly ordered $k$-tuples.

**Step 2: Colimit passage.** For a refinement $\mathcal{P} \preceq \mathcal{Q}$, the inclusion $\operatorname{span}\{x_{A_i}\} \hookrightarrow \operatorname{span}\{x_{B_j}\}$ (where $\{B_j\}$ are the cells of $\mathcal{Q}$) induces a map $U_{\mathbb{O}}(\operatorname{span}\{x_{A_i}\}) \to U_{\mathbb{O}}(\operatorname{span}\{x_{B_j}\})$ by the universal property (Theorem 10.10). Since $x_{A_i} = \sum_{B_j \subseteq A_i} \frac{\mu(B_j)}{\mu(A_i)} x_{B_j}$, this map is compatible with the transition maps of Theorem 14.14. Taking the colimit over all finite partitions and completing in the $L^2$ norm yields:

$$U_{\mathbb{O}}(A)_{\text{cont}} = \overline{\varinjlim_{\mathcal{P}} U_{\mathbb{O}}(\operatorname{span}\{x_{A_i}\}_{A_i \in \mathcal{P}})}^{\|\cdot\|_{L^2}}$$

**Step 3: Completeness (spanning).**

We must show that every element of $U_{\mathbb{O}}(A)$ can be approximated in $L^2$ norm by elements expressible as finite linear combinations of continuous tree monomials $T_k[c]$ (Definition 14.16).

**Lemma 14.17.1 (Density of step functions in $L^2_{\mathrm{tree}}$).** For each $k \geq 0$, the space of $\mathbb{O}$-valued step functions on $\Omega^k$ is dense in $L^2_{\mathrm{tree}}(\Omega^k, \mu^k; \mathbb{O})$.

*Proof of Lemma 14.17.1.* Since $(\Omega, \Sigma, \mu)$ is $\sigma$-finite, the product space $(\Omega^k, \Sigma^{\otimes k}, \mu^k)$ is also $\sigma$-finite. By the density of simple (step) functions in $L^2$ of a $\sigma$-finite measure space (Rudin, W., *Real and Complex Analysis*, 3rd ed., McGraw-Hill, 1987, Theorem 1.17 and Theorem 3.13), every $f \in L^2(\Omega^k, \mu^k; \mathbb{R})$ can be approximated arbitrarily closely in $L^2$ norm by simple functions of the form:
$$s(\omega_1, \ldots, \omega_k) = \sum_{\ell=1}^{N} c_\ell \cdot \mathbf{1}_{E_\ell}(\omega_1, \ldots, \omega_k)$$
where $c_\ell \in \mathbb{R}$ and $E_\ell \in \Sigma^{\otimes k}$ are measurable sets of finite measure.

For $\mathbb{O}$-valued functions $f \in L^2(\Omega^k, \mu^k; \mathbb{O})$, decompose $f = \sum_{p=0}^{7} f_p \cdot e_p$ where each $f_p : \Omega^k \to \mathbb{R}$ is real-valued and $\{e_0 = 1, e_1, \ldots, e_7\}$ is the standard octonion basis. Since $\|f\|_{L^2}^2 = \sum_p \|f_p\|_{L^2}^2$ (by orthogonality of the octonion basis units with respect to the real inner product), approximating each $f_p$ by step functions $s_p$ to within $\epsilon / \sqrt{8}$ in $L^2$ gives:
$$\left\| f - \sum_p s_p \cdot e_p \right\|_{L^2}^2 = \sum_p \|f_p - s_p\|_{L^2}^2 < 8 \cdot \frac{\epsilon^2}{8} = \epsilon^2$$

Each measurable rectangle $E_\ell \subseteq \Omega^k$ can be approximated by products of partition cells $A_{i_1} \times \cdots \times A_{i_k}$ for a sufficiently fine partition $\mathcal{P}$: given $E_\ell$ of finite measure and $\delta > 0$, the $\sigma$-algebra $\Sigma^{\otimes k}$ is generated by measurable rectangles, so $E_\ell$ can be approximated from within by finite unions of rectangles to within $\delta$ in symmetric difference measure. These rectangles can in turn be approximated by products of partition cells by choosing a partition fine enough that each factor set is approximated by unions of partition cells.

It remains to show that the tree-ordering condition $\omega_1 \preceq_\mu \cdots \preceq_\mu \omega_k$ is compatible with this density. The $L^2_{\mathrm{tree}}$ space consists of functions supported on the "ordered" region $\Delta_k = \{(\omega_1, \ldots, \omega_k) : \omega_1 \preceq_\mu \cdots \preceq_\mu \omega_k\}$. Since the ordering is defined $\mu$-a.e. and $\Delta_k$ is a measurable subset of $\Omega^k$ (it is defined by a well-ordering on the support of $\mu$, which is measurable by definition), the restriction to $\Delta_k$ preserves $L^2$ density: if $s_n \to f$ in $L^2(\Omega^k)$, then $s_n \cdot \mathbf{1}_{\Delta_k} \to f \cdot \mathbf{1}_{\Delta_k}$ in $L^2(\Delta_k)$. The step functions restricted to $\Delta_k$ remain step functions (intersecting with $\Delta_k$ gives weakly ordered index tuples $i_1 \leq \cdots \leq i_k$ at the partition level). $\square_{\text{Lemma}}$

Now, each step function on $\Delta_k$ with values in $\mathbb{O}$ corresponds to a finite linear combination of finite tree monomials (from Step 1) with octonionic coefficients. By Lemma 14.17.1, these approximate any element of $L^2_{\mathrm{tree}}(\Omega^k, \mu^k; \mathbb{O})$ arbitrarily closely. The continuous tree monomial $T_k[c] = \int_{\Omega^k} c(\omega_1, \ldots, \omega_k) L_k(x(\omega_1), \ldots, x(\omega_k)) \, d\mu^k$ is the $L^2$-limit of the finite tree monomial approximations (since the map $c \mapsto T_k[c]$ is a bounded linear operator on $L^2$, continuity gives convergence of the image). Therefore, continuous tree monomials span $U_{\mathbb{O}}(A)$ in the $L^2$ topology.

**Step 4: Independence.**

We must show that if $\sum_{k=0}^{K} T_k[c_k] = 0$ in $U_{\mathbb{O}}(A)$ for some $c_k \in L^2_{\mathrm{tree}}(\Omega^k, \mu^k; \mathbb{O}) \otimes_{\mathrm{alt}} \mathbb{R}[\mathcal{T}_k]$, then $c_k = 0$ for all $k$.

**Lemma 14.17.2 (Independence at each partition level).** For each finite partition $\mathcal{P}$ of $\Omega$, the finite COPBW basis elements at different weights are linearly independent.

*Proof of Lemma 14.17.2.* This is a direct consequence of Theorem 10.12 (COPBW linear independence). The basis $\mathcal{B}_{\mathcal{P}}$ is linearly independent in $U_{\mathbb{O}}(\operatorname{span}\{x_{A_i}\})$ because the Cayley module construction (Section 10.5.4) provides a faithful representation: distinct hierarchical tree monomials act differently on the Cayley module $\mathcal{C}(\operatorname{span}\{x_{A_i}\})$. In particular, weight-$k$ tree monomials map $\mathbf{1} \in \operatorname{Alt}^0$ to elements of $\operatorname{Alt}^k$, and elements of different weights land in different graded components, hence are automatically independent. Elements of the same weight $k$ but with different index tuples $(i_1, \ldots, i_k)$ or different octonionic coefficients $(\alpha_0, \ldots, \alpha_k)$ produce linearly independent elements of $\operatorname{Alt}^k$ by the independence proof in Theorem 10.12. $\square_{\text{Lemma}}$

**Lemma 14.17.3 (Independence passes to the colimit).** If $c_k \neq 0$ in $L^2_{\mathrm{tree}}(\Omega^k, \mu^k; \mathbb{O})$, then $T_k[c_k] \neq 0$ in $U_{\mathbb{O}}(A)$.

*Proof of Lemma 14.17.3.* Suppose $c_k \neq 0$. Then $\|c_k\|_{L^2} > 0$, so there exists $\epsilon > 0$ and a measurable set $S \subseteq \Delta_k$ with $\mu^k(S) > 0$ such that $|c_k(\omega_1, \ldots, \omega_k)| > \epsilon$ for $(\omega_1, \ldots, \omega_k) \in S$.

Choose a finite partition $\mathcal{P}$ fine enough that the step-function approximation $c_k^{\mathcal{P}}$ of $c_k$ satisfies $\|c_k - c_k^{\mathcal{P}}\|_{L^2} < \frac{\epsilon \sqrt{\mu^k(S)}}{2}$. The coefficient function $c_k^{\mathcal{P}}$ is a step function, so $T_k[c_k^{\mathcal{P}}]$ is a finite linear combination of COPBW basis elements at weight $k$ with coefficients determined by $c_k^{\mathcal{P}}$.

Since $c_k^{\mathcal{P}}$ is not identically zero (because $\|c_k^{\mathcal{P}}\|_{L^2} \geq \|c_k\|_{L^2} - \frac{\epsilon \sqrt{\mu^k(S)}}{2} > 0$ by the triangle inequality and the choice of $\epsilon$), Lemma 14.17.2 gives $T_k[c_k^{\mathcal{P}}] \neq 0$ in $U_{\mathbb{O}}(\operatorname{span}\{x_{A_i}\})$. Since the canonical map $U_{\mathbb{O}}(\operatorname{span}\{x_{A_i}\}) \to U_{\mathbb{O}}(A)$ is injective (it is induced by the inclusion of generators, and the COPBW linear independence at each level means no new relations are imposed by passing to a finer partition), $T_k[c_k^{\mathcal{P}}] \neq 0$ in $U_{\mathbb{O}}(A)$.

Since $T_k[\cdot]$ is a bounded linear map, $T_k[c_k]$ is the $L^2$-limit of the nonzero elements $T_k[c_k^{\mathcal{P}}]$. The norms satisfy $\|T_k[c_k^{\mathcal{P}}]\| \geq \delta > 0$ uniformly for all sufficiently fine $\mathcal{P}$ (because the Cayley module representation provides a lower bound: the image of $T_k[c_k^{\mathcal{P}}]$ acting on $\mathbf{1}$ has norm at least $\|c_k^{\mathcal{P}}\|_{L^2} \cdot m$, where $m > 0$ depends only on the basis $\{x(\omega)\}$ and is independent of $\mathcal{P}$). By continuity of the norm, $\|T_k[c_k]\| \geq \delta > 0$, so $T_k[c_k] \neq 0$. $\square_{\text{Lemma}}$

Finally, suppose $\sum_{k=0}^{K} T_k[c_k] = 0$. The weight filtration (Theorem 10.12, part 3) gives a grading on the associated graded algebra: $\operatorname{gr}_k(U_{\mathbb{O}}(A)) = F_k / F_{k-1}$. The image of $T_k[c_k]$ in $\operatorname{gr}_k$ depends only on $c_k$ (the lower-weight components project to zero). If $c_K \neq 0$, then $T_K[c_K]$ has nonzero image in $\operatorname{gr}_K$ by Lemma 14.17.3, but $\sum_{k=0}^{K} T_k[c_k] = 0$ implies the image of $T_K[c_K]$ in $\operatorname{gr}_K$ is zero — a contradiction. By downward induction on $K$, all $c_k = 0$.

This establishes the isomorphism $U_{\mathbb{O}}(A) \cong \bigoplus_{k \geq 0} L^2_{\mathrm{tree}}(\Omega^k, \mu^k; \mathbb{O}) \otimes_{\mathrm{alt}} \mathbb{R}[\mathcal{T}_k]$, understood in the $L^2$ sense (continuous frame). $\square$

---

## 14.8 Contextual Arity

### 14.8.1 Definition

**Definition 14.18 (Contextual arity).** An operation $\theta$ has *contextual arity* $(\Omega, \mu)$ if its arity depends on the context: in context $\omega$, the operation has a specific "local arity" $n(\omega)$, and the total arity is:
$$\text{total arity} = \int_\Omega n(\omega) \, d\mu(\omega)$$

When $n(\omega) = 1$ for all $\omega$ (each context contributes one input), the total arity is $\mu(\Omega)$.

### 14.8.2 The Adjoint Action with Contextual Arity

The decompactified adjoint action (Chapter 8):
$$\operatorname{ad}_X^{(\mu)}(Y) = \int_\Omega [X^{(\omega)}, Y^{(\omega)}] \, d\mu(\omega)$$

is an operation of contextual arity $(\Omega, \mu)$: it takes two inputs ($X$ and $Y$), but each input is evaluated in uncountably many contexts $\omega \in \Omega$, and the results are integrated.

The arity of $\operatorname{ad}_X^{(\mu)}$ as a measurable operation is:
- Input arity: $(\Omega \times \{1, 2\}, \mu \times \#_2)$ (two inputs, each spread over $\Omega$).
- Output arity: a single element of $A$.

### 14.8.3 The Contextual Killing Form

The decompactified Killing form:
$$B_\mu(X, Y) = \int_\Omega \operatorname{tr}(\operatorname{ad}_X^{(\omega)} \circ \operatorname{ad}_Y^{(\omega)}) \, d\mu(\omega)$$

is a bilinear form of contextual arity $(\Omega, \mu)$. Its kernel and image depend on the measure $\mu$:

**Proposition 14.19.**
1. If $\mu = \delta_{\omega_0}$ (point mass), $B_\mu$ reduces to the classical Killing form at context $\omega_0$.
2. If $\mu$ is absolutely continuous with respect to Lebesgue measure, $B_\mu$ is "maximally decompactified" and detects all contextual information.
3. If $\mu$ is supported on a discrete set $\{\omega_1, \omega_2, \ldots\}$ with weights $w_i$, then $B_\mu = \sum_i w_i B_{\omega_i}$ is a weighted average of classical Killing forms.

---

## 14.9 The Integration-Summation Correspondence

### 14.9.1 Formal Statement

**Theorem 14.20 (Integration-summation correspondence).** Let $V$ be a finite-dimensional $\mathbb{O}$-module with basis $\{e_1, \ldots, e_n\}$, and let $V_\mu$ be the corresponding continuous module with basis $\{e_\omega\}_{\omega \in \Omega}$ and measure $\mu$. Then:

1. **Basis expansion:**
$$v = \sum_{i=1}^{n} c_i e_i \quad \longleftrightarrow \quad v_\mu = \int_\Omega c(\omega) e_\omega \, d\mu(\omega)$$

2. **Inner product:**
$$\langle v, w \rangle = \sum_i \bar{c}_i d_i \quad \longleftrightarrow \quad \langle v_\mu, w_\mu \rangle = \int_\Omega \overline{c(\omega)} d(\omega) \, d\mu(\omega)$$

3. **Operator action:**
$$Av = \sum_{i,j} A_{ij} c_j e_i \quad \longleftrightarrow \quad A_\mu v_\mu = \int_{\Omega \times \Omega} K(\omega, \omega') c(\omega') e_\omega \, d\mu(\omega) d\mu(\omega')$$

4. **Trace:**
$$\operatorname{tr}(A) = \sum_i A_{ii} \quad \longleftrightarrow \quad \operatorname{tr}(A_\mu) = \int_\Omega K(\omega, \omega) \, d\mu(\omega)$$

5. **Associator:**
$$[e_i, e_j, e_k] \quad \longleftrightarrow \quad \int_{\Omega^3} [e_{\omega_1}, e_{\omega_2}, e_{\omega_3}] \, d\mu^3(\omega_1, \omega_2, \omega_3)$$

### 14.9.2 Non-Associativity in the Continuous Setting

The associator of continuous basis elements introduces a **three-point correlation function**:
$$\mathcal{A}(\omega_1, \omega_2, \omega_3) = [e_{\omega_1}, e_{\omega_2}, e_{\omega_3}]$$

**Proposition 14.21a (Measurability of the associator function).** Let $e : \Omega \to M'$ be a continuous $\mathbb{O}$-basis of an $\mathbb{O}$-module $M$ indexed by a $\sigma$-finite measure space $(\Omega, \Sigma, \mu)$ (Definition 14.10). Then the associator function $\mathcal{A} : \Omega^3 \to \mathbb{O}$ defined by $\mathcal{A}(\omega_1, \omega_2, \omega_3) = [e_{\omega_1}, e_{\omega_2}, e_{\omega_3}]$ is measurable with respect to the product $\sigma$-algebra $\Sigma^{\otimes 3}$ and the Borel $\sigma$-algebra on $\mathbb{O} \cong \mathbb{R}^8$. Moreover, if $e$ is square-integrable (i.e., $\int_\Omega \|e_\omega\|^2 \, d\mu(\omega) < \infty$), then $\mathcal{A} \in L^1(\Omega^3, \mu^3; \mathbb{O})$.

*Proof.* The associator is defined as $[a, b, c] = (ab)c - a(bc)$ for $a, b, c \in \mathbb{O}$. Octonion multiplication $\mathbb{O} \times \mathbb{O} \to \mathbb{O}$ is a bilinear map (hence continuous, hence Borel measurable). The map $(\omega_1, \omega_2, \omega_3) \mapsto (e_{\omega_1}, e_{\omega_2}, e_{\omega_3})$ is measurable from $(\Omega^3, \Sigma^{\otimes 3})$ to $(\mathbb{O}^3, \mathcal{B}(\mathbb{O})^{\otimes 3})$ because each component $\omega \mapsto e_\omega$ is measurable by hypothesis (Definition 14.10 requires $e$ to be a measurable map).

The composition of measurable maps is measurable. The map $(a, b, c) \mapsto (ab)c$ is the composition of $(a, b) \mapsto ab$ (bilinear, hence measurable) followed by $(d, c) \mapsto dc$ (again bilinear, hence measurable). Similarly $(a, b, c) \mapsto a(bc)$. Their difference is a continuous (hence measurable) function. Therefore $\mathcal{A} = [(a,b,c) \mapsto (ab)c - a(bc)] \circ [({\omega_1, \omega_2, \omega_3}) \mapsto (e_{\omega_1}, e_{\omega_2}, e_{\omega_3})]$ is measurable as the composition of measurable maps.

For the integrability claim: if $\int_\Omega \|e_\omega\|^2 \, d\mu(\omega) < \infty$, then by the Cauchy-Schwarz inequality and the fact that the octonionic product satisfies $\|ab\| \leq \|a\| \cdot \|b\|$ (the octonions are a normed division algebra, so equality holds, but the inequality suffices):
$$\|\mathcal{A}(\omega_1, \omega_2, \omega_3)\| = \|[e_{\omega_1}, e_{\omega_2}, e_{\omega_3}]\| \leq \|(e_{\omega_1} e_{\omega_2}) e_{\omega_3}\| + \|e_{\omega_1} (e_{\omega_2} e_{\omega_3})\| \leq 2\|e_{\omega_1}\| \cdot \|e_{\omega_2}\| \cdot \|e_{\omega_3}\|$$

Therefore:
$$\int_{\Omega^3} \|\mathcal{A}(\omega_1, \omega_2, \omega_3)\| \, d\mu^3 \leq 2 \int_{\Omega^3} \|e_{\omega_1}\| \cdot \|e_{\omega_2}\| \cdot \|e_{\omega_3}\| \, d\mu^3 = 2 \left(\int_\Omega \|e_\omega\| \, d\mu(\omega)\right)^3$$

The last factor is finite because $\int_\Omega \|e_\omega\| \, d\mu \leq \left(\int_\Omega 1 \, d\mu\right)^{1/2} \left(\int_\Omega \|e_\omega\|^2 \, d\mu\right)^{1/2} < \infty$ when $\mu(\Omega) < \infty$, or more generally by the $\sigma$-finiteness of $\mu$ and the square-integrability hypothesis applied on each set of a countable decomposition. (When $\mu(\Omega) = \infty$ but $\mu$ is $\sigma$-finite, the integrability of $\|e_\omega\|$ follows from the resolution of identity: $\int_\Omega \|e_\omega\|^2 \, d\mu(\omega) = \operatorname{tr}(I) = \dim(M) < \infty$ for a finite-dimensional module $M$, so $\|e_\omega\| \in L^2(\Omega, \mu) \subseteq L^1_{\text{loc}}(\Omega, \mu)$.) $\square$

The integral:
$$\int_{\Omega^3} \mathcal{A}(\omega_1, \omega_2, \omega_3) \, d\mu^3$$

is the **total associator content** of the continuous module — a single octonion that measures the "total non-associativity" of the system.

**Definition 14.21b ($\mu$-almost-associativity).** A continuous $\mathbb{O}$-module $M$ with basis $\{e_\omega\}_{\omega \in \Omega}$ is *$\mu$-almost-associative* if for all $v, w, u \in M$ expressed as $v = \int c_v(\omega) e_\omega \, d\mu$, $w = \int c_w(\omega) e_\omega \, d\mu$, $u = \int c_u(\omega) e_\omega \, d\mu$:
$$\int_{\Omega^3} c_v(\omega_1) c_w(\omega_2) c_u(\omega_3) [e_{\omega_1}, e_{\omega_2}, e_{\omega_3}] \, d\mu^3(\omega_1, \omega_2, \omega_3) = 0$$

That is, the *weighted* associator vanishes for every choice of coefficient functions.

**Proposition 14.21.** The following are equivalent:

(i) The module is $\mu$-almost-associative.

(ii) The associator function $\mathcal{A}(\omega_1, \omega_2, \omega_3) = [e_{\omega_1}, e_{\omega_2}, e_{\omega_3}] = 0$ for $\mu^3$-almost every $(\omega_1, \omega_2, \omega_3) \in \Omega^3$.

*Proof.*

$(ii) \Rightarrow (i)$: If $\mathcal{A} = 0$ $\mu^3$-a.e., then for any coefficient functions $c_v, c_w, c_u \in L^2(\Omega, \mu; \mathbb{O})$, the integrand $c_v(\omega_1) c_w(\omega_2) c_u(\omega_3) \mathcal{A}(\omega_1, \omega_2, \omega_3) = 0$ $\mu^3$-a.e., so the integral vanishes.

$(i) \Rightarrow (ii)$: Suppose $\mathcal{A} \neq 0$ on a set $S \subseteq \Omega^3$ with $\mu^3(S) > 0$. We construct coefficient functions for which the weighted associator integral is nonzero.

Decompose $\mathcal{A} = \sum_{p=0}^{7} \mathcal{A}_p \cdot e_p$ into real components. Since $\mathcal{A} \neq 0$ on $S$, at least one component $\mathcal{A}_p$ is nonzero on a subset $S_p \subseteq S$ with $\mu^3(S_p) > 0$.

By Fubini's theorem ($\mu^3$ is $\sigma$-finite), if $\mu^3(S_p) > 0$, there exist measurable sets $E_1, E_2, E_3 \subseteq \Omega$ with $\mu(E_i) > 0$ such that $\mathcal{A}_p$ is nonzero on a subset of $E_1 \times E_2 \times E_3$ having positive $\mu^3$-measure. (This is the contrapositive of Fubini: if for $\mu$-a.e. $\omega_1$, the slice $\{(\omega_2, \omega_3) : \mathcal{A}_p(\omega_1, \omega_2, \omega_3) \neq 0\}$ had $\mu^2$-measure zero, then $\mu^3(S_p) = 0$.)

Choose $c_v = \mathbf{1}_{E_1}$, $c_w = \mathbf{1}_{E_2}$, $c_u = \mathbf{1}_{E_3}$ (indicator functions, which lie in $L^2$ when $\mu(E_i) < \infty$; since $\mu$ is $\sigma$-finite, we can choose $E_i$ to have finite measure). Then:
$$\int_{\Omega^3} c_v c_w c_u \cdot \mathcal{A}_p \, d\mu^3 = \int_{E_1 \times E_2 \times E_3} \mathcal{A}_p \, d\mu^3 \neq 0$$

(This integral is nonzero because $\mathcal{A}_p$ has a definite sign on a subset of $E_1 \times E_2 \times E_3$ of positive measure — we may further restrict to a subset where $\mathcal{A}_p > 0$ or $\mathcal{A}_p < 0$, each of which must have positive measure for at least one sign.) Therefore the $e_p$-component of the weighted associator integral is nonzero, contradicting $\mu$-almost-associativity.

**Remark.** The vanishing of the *total* associator content $\int_{\Omega^3} \mathcal{A} \, d\mu^3 = 0$ (a single octonionic equation) is a *necessary* condition for $\mu$-almost-associativity (it is the special case $c_v = c_w = c_u = 1$), but it is NOT sufficient. The full condition (ii) requires the pointwise-a.e. vanishing of the associator, which is strictly stronger. This provides a **measure-theoretic criterion for associativity**: the module is effectively associative if and only if the basis elements are pairwise associative $\mu$-almost everywhere. $\square$

---

## 14.10 Examples

### 14.10.1 The Fourier-Octonionic Basis

Let $\Omega = S^6$ (the unit sphere in $\operatorname{Im}(\mathbb{O})$) with the standard round measure $d\sigma$. Define:
$$e_{\hat{n}}(\mathbf{x}) = \exp(\hat{n} \cdot (\hat{n} \cdot \mathbf{x}))$$
for $\hat{n} \in S^6$ and $\mathbf{x} \in \mathbb{R}^7$.

This gives a continuous basis of octonionic "plane waves" parameterized by the direction $\hat{n}$ on $S^6$. The expansion:
$$f(\mathbf{x}) = \int_{S^6} c(\hat{n}) \exp(\hat{n} \cdot (\hat{n} \cdot \mathbf{x})) \, d\sigma(\hat{n})$$

is the *octonionic Fourier transform* on $S^6$. The coefficient function $c : S^6 \to \mathbb{O}$ is determined by the Funk–Hecke formula:
$$c(\hat{n}) = \int_{\mathbb{R}^7} f(\mathbf{x}) \overline{\exp(\hat{n} \cdot (\hat{n} \cdot \mathbf{x}))} \, dV_7(\mathbf{x})$$

### 14.10.2 The $G_2$ Contextual Basis

Let $\Omega = G_2$ with Haar measure $\mu_{G_2}$. For each $g \in G_2$, define:
$$e_g = g \cdot e_1$$
(the image of $e_1$ under the automorphism $g$). Since $G_2$ acts transitively on $S^6$, this gives a continuous basis of $\operatorname{Im}(\mathbb{O})$ parameterized by $G_2$.

The expansion:
$$\mathbf{v} = \int_{G_2} c(g) \, g \cdot e_1 \, d\mu_{G_2}(g)$$

expresses any imaginary octonion as an integral over $G_2$-rotated basis elements. The stabilizer of $e_1$ in $G_2$ is $SU(3)$, so the effective parameter space is $G_2/SU(3) \cong S^6$, recovering the previous example.

### 14.10.3 The Killing Form on the $G_2$ Basis

Using the $G_2$ contextual basis, the decompactified Killing form becomes:
$$B_{\mu_{G_2}}(X, Y) = \int_{G_2} \operatorname{tr}(\operatorname{ad}_{g \cdot X} \circ \operatorname{ad}_{g \cdot Y}) \, d\mu_{G_2}(g)$$

By the invariance of the Haar measure:
$$= \operatorname{tr}(\operatorname{ad}_X \circ \operatorname{ad}_Y) \cdot \mu_{G_2}(G_2)$$

So the $G_2$-averaged Killing form is proportional to the classical Killing form. The decompactification becomes nontrivial only when we use a *non-$G_2$-invariant* measure, breaking the full symmetry and selecting specific "contexts."

---

## 14.11 Connection to the Decompactified Killing Form

The decompactified Killing form (Chapter 8) is:
$$B_\mu(X, Y) = \int_\Omega \operatorname{tr}(\operatorname{ad}_X^{(\omega)} \circ \operatorname{ad}_Y^{(\omega)}) \, d\mu(\omega)$$

In the language of this chapter:
- $(\Omega, \mu)$ is the arity measure space for the "context" of the Killing form.
- $\operatorname{ad}_X^{(\omega)}$ is the adjoint operator of $X$ in context $\omega$, which is a measurable operation of contextual arity.
- The trace $\operatorname{tr}(\cdot)$ is the continuous trace of an operator on a potentially infinite-dimensional representation space.
- The integral replaces the finite sum over adjoint representation indices.

**Theorem 14.22 (Nondegeneracy criterion).** The decompactified Killing form $B_\mu$ is nondegenerate if and only if the measure $\mu$ separates contexts:
$$\forall X \neq 0, \; \exists \omega \in \operatorname{supp}(\mu) \text{ such that } \operatorname{ad}_X^{(\omega)} \neq 0$$

In other words, $B_\mu$ is nondegenerate when every nonzero element $X$ has a nontrivial adjoint action in *some* context $\omega$ that is seen by the measure $\mu$.

*Proof.* $B_\mu(X, Y) = 0$ for all $Y$ implies $\int_\Omega \operatorname{tr}(\operatorname{ad}_X^{(\omega)} \circ \operatorname{ad}_Y^{(\omega)}) \, d\mu(\omega) = 0$ for all $Y$. This gives $\operatorname{ad}_X^{(\omega)} = 0$ for $\mu$-almost every $\omega$. If $\mu$ separates contexts, this forces $X = 0$. $\square$

---

## 14.12 Recovery of Finite-Dimensional Theory

**Theorem 14.23 (Finite recovery).** When $(\Omega, \mu) = (\{1, \ldots, n\}, \#)$ (finite set with counting measure):

1. The continuous COPBW basis reduces to the finite COPBW basis (Theorem 10.12).
2. The integration-summation correspondence becomes the identity.
3. The contextual arity is the ordinary arity $n$.
4. The decompactified Killing form reduces to $B(X, Y) = \sum_{i=1}^{n} \operatorname{tr}(\operatorname{ad}_X^{(i)} \circ \operatorname{ad}_Y^{(i)})$.
5. When $n = 1$ and the algebra is a Lie algebra over $\mathbb{H}$, everything reduces to classical Lie theory.

This is the essential consistency check: the measure-theoretic framework contains the finite-dimensional theory as a special case, with no information lost.

---

## 14.13 Summary

This chapter establishes the measure-theoretic foundations for uncountable-arity algebra:

1. **Measure spaces as arities.** The arity of an operation is a $\sigma$-finite measure space $(\Omega, \mu)$, generalizing the natural number $n$.

2. **Measure-theoretic operads.** Defined via composition maps involving direct integrals, they extend classical operads to uncountable settings.

3. **Colimit construction.** The measure-theoretic operad is the colimit of finite-arity operads over refinements of partitions.

4. **Continuous bases.** Replace discrete bases; integration replaces summation.

5. **Contextual arity.** Operations whose arity depends on a context parameter $\omega \in \Omega$, with total arity given by $\mu(\Omega)$.

6. **Continuous COPBW.** The COPBW basis extends to continuous index sets, with coefficients in $L^2(\Omega^k, \mu^k; \mathbb{O})$.

7. **Integration-summation correspondence.** Every algebraic identity with finite sums has an integral analog, with the associator becoming a three-point correlation function.

8. **Recovery.** The finite-dimensional theory is recovered exactly when $(\Omega, \mu)$ is a finite set with counting measure.

---

*Next: Chapter 15 proves the quaternionic slice theorem, rigorously recovering all classical 3D mathematics from the 7D octonionic framework.*
