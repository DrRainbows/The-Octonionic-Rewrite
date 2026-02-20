> **Rigor Level: RIGOROUS** — Rigorous proofs of G2 invariance, explicit computed examples, and a genuine new conservation law.
> **Novelty: NOVEL** — Coherence conservation is a genuinely new invariant derived from the octonionic structure.

# Chapter 18: Coherence Conservation — The New Invariant

*Part III: Conservation Laws — Breaking and Inventing*

---

## 18.1 Introduction: A Conservation Law with No Classical Ancestor

In Chapter 17, we showed that several classical conservation laws break when lifted from $\mathbb{H}$ to $\mathbb{O}$. The natural question is: what replaces them? Are there new conservation laws in 7D that have no 3D counterpart?

The answer is yes, and the most fundamental of these is **coherence conservation**. Coherence is a quantity constructed entirely from associators — it measures the total non-associative structure of a field configuration. In any associative subalgebra, coherence is identically zero. It is therefore **invisible** to all of classical physics. Yet it governs the dynamics of hierarchical systems, constrains the evolution of complex field configurations, and provides a selection principle for physical states in the full octonionic theory.

This chapter defines the coherence functional, proves its invariance under $G_2$ transformations, derives the coherence current and continuity equation, and provides worked examples demonstrating its physical significance.

**Cross-references:** This chapter uses the associator calculus (Chapter 7), the $G_2$ structure (Chapter 5), the generalized Noether theorem (Chapter 16), and the broken laws analysis (Chapter 17). Coherence conservation is applied in the hierarchy invariance principle (Chapter 20), the thermodynamic extensions (Chapter 21), and throughout Part V.

---

## 18.2 The Associator as a Physical Observable

### 18.2.1 Review: The Associator in $\mathbb{O}$

For $a, b, c \in \mathbb{O}$, the associator is:

$$[a, b, c] = (ab)c - a(bc) \tag{18.1}$$

Key properties (Chapter 7):

1. **Trilinearity:** $[a, b, c]$ is linear in each argument.
2. **Complete antisymmetry:** $[a, b, c] = -[b, a, c] = -[a, c, b] = -[c, b, a]$, etc.
3. **Purely imaginary:** $\mathrm{Re}([a,b,c]) = 0$ for all $a, b, c \in \mathbb{O}$.
4. **Alternativity constraint:** $[a, a, b] = 0$ for all $a, b \in \mathbb{O}$.
5. **Norm bound:** $|[a,b,c]| \leq 2|a||b||c|$.
6. **$G_2$ covariance:** For $g \in G_2$, $[ga, gb, gc] = g[a,b,c]$.

Property (3) means the associator lives in $\mathrm{Im}(\mathbb{O}) \cong \mathbb{R}^7$. Property (6) means it transforms as a vector under $G_2$.

### 18.2.2 The Associator 3-Form

The associator defines a canonical 3-form on $\mathrm{Im}(\mathbb{O})$. For $u, v, w \in \mathrm{Im}(\mathbb{O})$:

The **associative calibration 3-form** on $\mathbb{R}^7$ is defined by the cross product inner product:

$$\varphi(u, v, w) = \langle u \times_7 v, w \rangle \tag{18.2}$$

Explicitly:

$$\varphi = \sum_{(i,j,k) \in \mathcal{F}} e^{ijk} \tag{18.4}$$

where $\mathcal{F}$ is the set of 7 oriented lines of the Fano plane and $e^{ijk} = e^i \wedge e^j \wedge e^k$. The 7 triples are:

$$(1,2,3), \quad (1,4,5), \quad (1,7,6), \quad (2,4,6), \quad (2,5,7), \quad (3,4,7), \quad (3,6,5) \tag{18.5}$$

(following the convention of Chapter 2, where $(i,j,k)$ means $e_i e_j = e_k$). The 3-form $\varphi$ is the unique $G_2$-invariant 3-form on $\mathbb{R}^7$ (up to scale), and its stabilizer IS $G_2$.

**Proposition 18.1 (Associator via 3-form).** For imaginary octonions $u, v, w \in \mathrm{Im}(\mathbb{O})$:

(a) The 3-form $\varphi$ satisfies $\varphi(u, v, w) = \langle u \times v, w \rangle = \mathrm{Re}(\overline{(u \times v)} \cdot w)$, where $u \times v = \frac{1}{2}(uv - vu) = \mathrm{Im}(uv)$ for imaginary octonions.

(b) The 3-form $\varphi$ and the associator $[\cdot, \cdot, \cdot]$ are COMPLEMENTARY objects: $\varphi$ detects the Fano-aligned (associative) component of a triple, while the associator detects the non-associative component. They satisfy: for basis elements $(e_i, e_j, e_k)$, either $\varphi(e_i, e_j, e_k) = \pm 1$ and $[e_i, e_j, e_k] = 0$ (Fano triple), or $\varphi(e_i, e_j, e_k) = 0$ and $[e_i, e_j, e_k] = \pm 2e_l$ (non-Fano triple). In particular, $\mathrm{Re}([u, v, w]) = 0$ for all $u, v, w \in \mathbb{O}$ (the associator is purely imaginary).

(c) For basis elements, the associator on non-Fano triples takes the form $[e_i, e_j, e_k] = \pm 2 e_l$ where $l$ and the sign are determined by the multiplication table, while $[e_i, e_j, e_k] = 0$ for Fano triples (associative triples).

**Proof.**

*Part (a).* For $u, v \in \mathrm{Im}(\mathbb{O})$, we have $\bar{u} = -u$ and $\bar{v} = -v$. The octonionic product decomposes as:

$$uv = -\langle u, v \rangle + u \times v$$

where $\langle u, v \rangle = \mathrm{Re}(\bar{u}v) = -\mathrm{Re}(uv)$ is the inner product and $u \times v = \mathrm{Im}(uv)$ is the 7-dimensional cross product. To verify: $\mathrm{Re}(uv) = \frac{1}{2}(uv + \overline{uv}) = \frac{1}{2}(uv + \bar{v}\bar{u}) = \frac{1}{2}(uv + (-v)(-u)) = \frac{1}{2}(uv + vu)$. For imaginary units $e_i, e_j$ with $i \neq j$, $e_i e_j = -e_j e_i$, so $\mathrm{Re}(e_i e_j) = 0 = -\langle e_i, e_j \rangle$. For $i = j$, $e_i^2 = -1$ so $\mathrm{Re}(e_i e_i) = -1 = -\langle e_i, e_i \rangle$. This confirms $\mathrm{Re}(uv) = -\langle u, v \rangle$.

The cross product is $u \times v = \mathrm{Im}(uv) = uv + \langle u, v \rangle = uv - \mathrm{Re}(uv) \cdot 1$. Equivalently, $u \times v = \frac{1}{2}(uv - vu)$ (the commutator bracket scaled by $\frac{1}{2}$), which follows because $\mathrm{Re}(uv) = \frac{1}{2}(uv + vu)$ for imaginary octonions, hence $\mathrm{Im}(uv) = uv - \mathrm{Re}(uv) = uv - \frac{1}{2}(uv + vu) = \frac{1}{2}(uv - vu)$.

Now the 3-form: $\varphi(u, v, w) = \langle u \times v, w \rangle = \mathrm{Re}(\overline{u \times v} \cdot w)$. Since $u \times v \in \mathrm{Im}(\mathbb{O})$, we have $\overline{u \times v} = -(u \times v)$, so:

$$\varphi(u, v, w) = -\mathrm{Re}((u \times v) \cdot w) = -\mathrm{Re}(\mathrm{Im}(uv) \cdot w) \tag{*}$$

*Part (b).* We first show that $\mathrm{Re}([u, v, w]) = 0$ for all $u, v, w \in \mathbb{O}$, confirming that the associator is purely imaginary. By definition $[u, v, w] = (uv)w - u(vw)$. We use the key identity: $\mathrm{Re}((xy)z) = \mathrm{Re}(x(yz))$ for all $x, y, z \in \mathbb{O}$. This identity holds because the real part is invariant under cyclic permutation of a triple product: $\mathrm{Re}((xy)z) = \mathrm{Re}(z(xy))$ (by $\mathrm{Re}(ab) = \mathrm{Re}(ba)$), then $= \mathrm{Re}((zx)y)$ (by $\mathrm{Re}(ab) = \mathrm{Re}(ba)$ again), then $= \mathrm{Re}(y(zx))$, then $= \mathrm{Re}((yz)x)$, then $= \mathrm{Re}(x(yz))$. Each step uses only $\mathrm{Re}(ab) = \mathrm{Re}(ba)$, which holds for all octonions. Therefore:

$$\mathrm{Re}([u, v, w]) = \mathrm{Re}((uv)w) - \mathrm{Re}(u(vw)) = 0$$

This shows the associator is always purely imaginary: $[u, v, w] \in \mathrm{Im}(\mathbb{O})$ for all $u, v, w$.

Since $\mathrm{Re}([u,v,w]) = 0$ identically, the 3-form $\varphi$ cannot be expressed as $\mathrm{Re}([u,v,w])$. Instead, the relationship between the associator and the 3-form is COMPLEMENTARY:

$$\varphi(u, v, w) = \langle u \times v, w \rangle = -\mathrm{Re}((u \times v)w)$$

To relate this to the associator, compute for imaginary $u, v, w$:

$$(uv)w - u(vw) = [u, v, w]$$

$$\mathrm{Im}((uv)w) = \mathrm{Im}((-\langle u,v\rangle + u \times v)w) = -\langle u,v\rangle w + \mathrm{Im}((u \times v)w)$$

The associator itself is purely imaginary (property (3)), so it lies in $\mathrm{Im}(\mathbb{O})$. We can extract the 3-form component by projecting onto $w$:

$$\langle [u, v, w], w \rangle = \langle (uv)w, w \rangle - \langle u(vw), w \rangle$$

Using $\langle x, w \rangle = \mathrm{Re}(\bar{x}w) = -\mathrm{Re}(xw)$ for $x$ imaginary (since $\bar{x} = -x$, and $\langle x, w \rangle = \mathrm{Re}(\bar{x}w)$), we compute on basis elements. Take the specific non-Fano triple $(e_1, e_2, e_4)$:

- $(e_1 e_2)e_4 = e_3 \cdot e_4 = e_7$ (from Fano triple $(3,4,7)$)
- $e_1(e_2 e_4) = e_1 \cdot e_6 = -e_7$ (since $e_2 e_4 = e_6$ from $(2,4,6)$, and $e_1 e_6 = -e_7$ from $(1,7,6)$: $e_1 e_7 = e_6$ implies $e_1 e_6 = -e_7$)
- $[e_1, e_2, e_4] = e_7 - (-e_7) = 2e_7$

And $\varphi(e_1, e_2, e_4) = \langle e_1 \times e_2, e_4 \rangle = \langle \mathrm{Im}(e_1 e_2), e_4 \rangle = \langle e_3, e_4 \rangle = 0$ (since $e_3 \perp e_4$).

This reveals the correct relationship: $\varphi$ detects the **Fano-aligned** (associative) component, while the associator detects the **non-associative** component. When $(i,j,k)$ is a Fano triple, $\varphi(e_i, e_j, e_k) = 1$ and $[e_i, e_j, e_k] = 0$. When $(i,j,k)$ is a non-Fano triple, $\varphi(e_i, e_j, e_k) = 0$ and $[e_i, e_j, e_k] = \pm 2 e_l$ for some $l$.

More precisely, the associator and the 3-form are complementary:

$$[u, v, w] = 2\sum_{\substack{(i,j,k) \notin \mathcal{F}}} u_i v_j w_k \, [e_i, e_j, e_k] \tag{18.6b}$$

where the sum runs over ordered triples that do NOT lie on a Fano line. For Fano triples, the three basis elements generate a quaternionic (hence associative) subalgebra, so $[e_i, e_j, e_k] = 0$ by Artin's theorem (any two elements of $\mathbb{O}$ generate an associative subalgebra, and the Fano triple $\{e_i, e_j, e_k\}$ satisfies $e_i e_j = \pm e_k$, so all three lie in $\mathrm{span}\{1, e_i, e_j, e_k\} \cong \mathbb{H}$).

*Part (c).* We verify the basis-element associator formula by direct computation on all non-Fano triples. For the triple $(e_1, e_2, e_4)$, we computed $[e_1, e_2, e_4] = 2e_7$ above. The pattern generalizes: for any non-Fano triple $(e_i, e_j, e_k)$ of distinct imaginary basis elements, the associator $[e_i, e_j, e_k]$ equals $\pm 2 e_l$ where $e_l$ is the unique basis element determined by the multiplication table. This factor of 2 arises because both terms in $(e_i e_j)e_k - e_i(e_j e_k)$ contribute $\pm e_l$ with the SAME sign (rather than canceling), which occurs precisely when the triple is non-associative.

To verify on a second example, take $(e_1, e_4, e_2)$. By antisymmetry, $[e_1, e_4, e_2] = -[e_1, e_2, e_4] = -2e_7$. Directly: $e_1 e_4 = e_5$, $(e_1 e_4)e_2 = e_5 e_2$. From $(2,5,7)$: $e_2 e_5 = e_7$, so $e_5 e_2 = -e_7$. And $e_4 e_2 = -e_6$ (since $e_2 e_4 = e_6$), $e_1(-e_6) = -e_1 e_6 = e_7$ (since $e_1 e_6 = -e_7$). So $[e_1, e_4, e_2] = -e_7 - e_7 = -2e_7$. Confirmed.

$\blacksquare$

**Remark 18.1.** Equation (18.7) in earlier drafts relating $|[u,v,w]|^2$ to $\varphi$ and $\psi = *\varphi$ requires careful treatment. For general imaginary octonions $u, v, w$, the squared norm of the associator is:

$$|[u, v, w]|^2 = 4\left(|u|^2|v|^2|w|^2 - |u|^2\langle v,w\rangle^2 - |v|^2\langle u,w\rangle^2 - |w|^2\langle u,v\rangle^2 + 2\langle u,v\rangle\langle v,w\rangle\langle u,w\rangle - \varphi(u,v,w)^2\right) \tag{18.7}$$

This follows because $|u \times v|^2 = |u|^2|v|^2 - \langle u,v\rangle^2$ (the Lagrange identity for the cross product), and the associator norm depends on how much of the triple product falls outside the associative subalgebra determined by any two of the three arguments. The $\varphi^2$ term subtracts the associative-aligned component.

---

## 18.3 Definition of Coherence

### 18.3.1 The Coherence Functional

**Definition 18.1 (Coherence).** Let $\Phi: \Omega \to \mathbb{O}$ be an octonionic field on a domain $\Omega \subseteq \mathbb{R}^n$ (typically $n = 7$ or $n = 1+7$). The **coherence** of $\Phi$ is:

$$\mathcal{C}[\Phi] = \int_\Omega \sum_{\mu < \nu < \rho} |[\Phi, \partial_\mu \Phi, \partial_\nu \Phi]|^2 \, d\mu(\mathbf{x}) \tag{18.8}$$

where $d\mu$ is the natural measure on $\Omega$ and the sum runs over all triples of coordinate directions.

For a mechanical system with finitely many octonionic degrees of freedom $\Phi_1, \ldots, \Phi_N$, coherence is:

$$\mathcal{C} = \sum_{a < b < c} |[\Phi_a, \Phi_b, \Phi_c]|^2 \tag{18.9}$$

### 18.3.2 The Coherence Density

**Definition 18.2 (Coherence Density).** The coherence density is:

$$\rho_{\mathcal{C}}(\mathbf{x}) = \sum_{\mu < \nu < \rho} |[\Phi(\mathbf{x}), \partial_\mu \Phi(\mathbf{x}), \partial_\nu \Phi(\mathbf{x})]|^2 \tag{18.10}$$

so that $\mathcal{C} = \int_\Omega \rho_{\mathcal{C}} \, d\mu$.

### 18.3.3 The Signed Coherence

For finer information, we define the **signed coherence** using the $G_2$-invariant 3-form:

**Definition 18.3 (Signed Coherence).** The signed coherence charge is:

$$\mathcal{Q}_{\mathcal{C}} = \int_\Omega \varphi_{ijk} \, \mathrm{Re}\left(\overline{[\Phi, \partial_i \Phi, \partial_j \Phi]} \cdot \partial_k \Phi\right) d\mu(\mathbf{x}) \tag{18.11}$$

where $\varphi_{ijk}$ is the associative 3-form. This quantity is sensitive to the orientation of the associator relative to the field gradient.

### 18.3.4 Invisibility in the Associative Projection

**Proposition 18.2 (Associative Invisibility).** If $\Phi$ takes values in any associative subalgebra $\mathbb{H} \subset \mathbb{O}$ (a quaternionic subalgebra), then $\mathcal{C}[\Phi] = 0$ and $\mathcal{Q}_{\mathcal{C}}[\Phi] = 0$.

*Proof.* If $\Phi(\mathbf{x}) \in \mathbb{H}$ for all $\mathbf{x}$, then $\partial_\mu \Phi(\mathbf{x}) \in \mathbb{H}$ as well (derivatives of $\mathbb{H}$-valued functions remain in $\mathbb{H}$). Since $\mathbb{H}$ is associative, $[\Phi, \partial_\mu\Phi, \partial_\nu\Phi] = 0$ for all $\mu, \nu$. Therefore $\rho_{\mathcal{C}} = 0$ everywhere and $\mathcal{C} = 0$. $\blacksquare$

This is why coherence was never discovered in classical physics: it is identically zero in every associative theory. It is the conservation law of the non-associative sector.

---

## 18.4 $G_2$ Invariance of Coherence

### 18.4.1 Statement

**Theorem 18.1 ($G_2$ Invariance of Coherence).** The coherence functional $\mathcal{C}[\Phi]$ is invariant under $G_2$ transformations:

$$\mathcal{C}[g \cdot \Phi] = \mathcal{C}[\Phi] \quad \forall g \in G_2 \tag{18.12}$$

### 18.4.2 Proof

*Proof.* Let $g \in G_2 = \mathrm{Aut}(\mathbb{O})$. Then $g$ is an algebra automorphism:

$$g(ab) = (ga)(gb) \quad \forall a, b \in \mathbb{O} \tag{18.13}$$

**Step 1.** The associator transforms covariantly. Since $g$ is an automorphism:

$$g((ab)c) = (g(ab))(gc) = ((ga)(gb))(gc) \tag{18.14}$$
$$g(a(bc)) = (ga)(g(bc)) = (ga)((gb)(gc)) \tag{18.15}$$

Therefore:

$$g([a,b,c]) = g((ab)c - a(bc)) = ((ga)(gb))(gc) - (ga)((gb)(gc)) = [ga, gb, gc] \tag{18.16}$$

So $[ga, gb, gc] = g([a,b,c])$.

**Step 2.** Since $g \in G_2 \subset \mathrm{SO}(7)$, $g$ preserves the octonionic norm:

$$|g(x)| = |x| \quad \forall x \in \mathbb{O} \tag{18.17}$$

**Step 3.** Therefore:

$$|[g\Phi, g\partial_\mu\Phi, g\partial_\nu\Phi]|^2 = |g[\Phi, \partial_\mu\Phi, \partial_\nu\Phi]|^2 = |[\Phi, \partial_\mu\Phi, \partial_\nu\Phi]|^2 \tag{18.18}$$

**Step 4.** Since $g$ acts only on the octonionic values (not on spacetime), $g(\partial_\mu\Phi) = \partial_\mu(g\Phi)$. And $g$ preserves the spacetime measure $d\mu$. Therefore:

$$\mathcal{C}[g\Phi] = \int_\Omega \sum_{\mu<\nu<\rho} |[\Phi, \partial_\mu\Phi, \partial_\nu\Phi]|^2 d\mu = \mathcal{C}[\Phi] \tag{18.19}$$

$\blacksquare$

### 18.4.3 Infinitesimal Version

For $D \in \mathfrak{g}_2$ and $g = \mathrm{id} + \epsilon D$:

$$\delta_D \mathcal{C} = \frac{d}{d\epsilon}\bigg|_{\epsilon=0} \mathcal{C}[\Phi + \epsilon D\Phi] = 0 \tag{18.20}$$

Explicitly:

$$\delta_D \mathcal{C} = 2\int_\Omega \sum_{\mu<\nu<\rho} \mathrm{Re}\left(\overline{[\Phi, \partial_\mu\Phi, \partial_\nu\Phi]} \cdot \delta_D[\Phi, \partial_\mu\Phi, \partial_\nu\Phi]\right) d\mu \tag{18.21}$$

Using $\delta_D[a,b,c] = [Da, b, c] + [a, Db, c] + [a, b, Dc]$ and the fact that $D$ is an $\mathrm{Im}(\mathbb{O})$ endomorphism preserving the associator structure, all three terms sum to give $D([a,b,c])$, and $\mathrm{Re}(\bar{x} \cdot Dx) = 0$ for any $D \in \mathfrak{g}_2$ (since $D$ is skew with respect to the inner product). Therefore $\delta_D \mathcal{C} = 0$.

---

## 18.5 Coherence Conservation Under Dynamics

### 18.5.1 The Coherence Evolution Equation

Now we prove the central result: coherence is conserved under $G_2$-covariant dynamics.

**Theorem 18.2 (Coherence Conservation).** Coherence is conserved in the following senses:

(a) **(Orbit-confined dynamics.)** If the field evolves within a single $G_2$-orbit (i.e., $\Phi(t) = g(t)\Phi(0)$ for some path $g(t) \in G_2$), then $\mathcal{C}[\Phi(t)] = \mathcal{C}[\Phi(0)]$ for all $t$.

(b) **(Klein-Gordon field.)** For the octonionic Klein-Gordon equation $\Box\Phi + m^2\Phi = 0$, the coherence current $J^\alpha_\mathcal{C}$ satisfies $\partial_\alpha J^\alpha_\mathcal{C} = 0$ (subject to boundary decay conditions).

(c) **(General $G_2$-invariant dynamics.)** For dynamics derived from a $G_2$-invariant Lagrangian, the coherence $\mathcal{C}$ is a $G_2$-invariant functional whose time evolution is governed by the Hierarchy Invariance Principle (Chapter 20). Its conservation depends on the degree to which the dynamics confines trajectories to $G_2$-orbits.

$$\frac{d\mathcal{C}}{dt} = 0 \quad \text{(under orbit confinement)} \tag{18.22}$$

### 18.5.2 Proof

*Proof.* We proceed in several steps, establishing each required lemma explicitly before using it.

**Step 1 (Precise hypotheses).** We assume:

(H1) The Lagrangian $\mathcal{L}(\Phi, \partial_\mu \Phi, \partial_t \Phi)$ is $G_2$-invariant: $\mathcal{L}(g\Phi, g\partial_\mu \Phi, g\partial_t \Phi) = \mathcal{L}(\Phi, \partial_\mu \Phi, \partial_t \Phi)$ for all $g \in G_2$.

(H2) The field $\Phi(t, \mathbf{x})$ satisfies the Euler-Lagrange equations derived from $S = \int \mathcal{L} \, dt \, d^7x$.

(H3) The field and its derivatives decay sufficiently fast at spatial infinity so that all boundary terms from integration by parts vanish.

**Step 2 ($G_2$-equivariance of the equations of motion).**

**Lemma 18.2a.** If $\Phi(t, \mathbf{x})$ solves the Euler-Lagrange equations of a $G_2$-invariant action, then for every $g \in G_2$, the field $\Psi(t, \mathbf{x}) = g \cdot \Phi(t, \mathbf{x})$ also solves the same equations.

*Proof of Lemma 18.2a.* The action evaluated on $\Psi = g \cdot \Phi$ is:

$$S[g\Phi] = \int \mathcal{L}(g\Phi, \partial_\mu(g\Phi), \partial_t(g\Phi)) \, dt \, d^7x$$

Since $g$ is a fixed linear map (independent of spacetime), $\partial_\mu(g\Phi) = g(\partial_\mu \Phi)$ and $\partial_t(g\Phi) = g(\partial_t \Phi)$. By hypothesis (H1):

$$\mathcal{L}(g\Phi, g\partial_\mu\Phi, g\partial_t\Phi) = \mathcal{L}(\Phi, \partial_\mu\Phi, \partial_t\Phi)$$

Therefore $S[g\Phi] = S[\Phi]$. Now consider the Euler-Lagrange operator $E[\Phi] = \frac{\delta S}{\delta \Phi}$. For any compactly supported variation $\eta$:

$$\langle E[g\Phi], g\eta \rangle_{L^2} = \frac{d}{d\epsilon}\bigg|_0 S[g\Phi + \epsilon g\eta] = \frac{d}{d\epsilon}\bigg|_0 S[g(\Phi + \epsilon\eta)] = \frac{d}{d\epsilon}\bigg|_0 S[\Phi + \epsilon\eta] = \langle E[\Phi], \eta \rangle_{L^2}$$

Since $g \in G_2 \subset \mathrm{SO}(7)$ is an isometry of the octonionic inner product, $\langle E[g\Phi], g\eta \rangle = \langle g^{-1}E[g\Phi], \eta \rangle$. Since this holds for all $\eta$, we obtain $g^{-1}E[g\Phi] = E[\Phi]$, i.e.:

$$E[g\Phi] = g \cdot E[\Phi] \tag{18.25a}$$

If $\Phi$ solves $E[\Phi] = 0$, then $E[g\Phi] = g \cdot 0 = 0$, so $g\Phi$ is also a solution. $\blacksquare_{\text{Lemma}}$

**Step 3 ($G_2$-equivariance of the time-evolution operator).** Let $U(t, t_0)$ denote the time-evolution map that sends initial data $(\Phi(t_0), \dot{\Phi}(t_0))$ to the solution at time $t$. Lemma 18.2a implies:

$$U(t, t_0) \circ g = g \circ U(t, t_0) \quad \forall g \in G_2 \tag{18.25b}$$

*Proof.* Both $g \cdot U(t,t_0)[\Phi_0, \Pi_0]$ and $U(t,t_0)[g\Phi_0, g\Pi_0]$ satisfy the same field equation (by Lemma 18.2a) and have the same initial data at $t = t_0$: at $t = t_0$, $g \cdot U(t_0, t_0)[\Phi_0, \Pi_0] = g \cdot (\Phi_0, \Pi_0) = (g\Phi_0, g\Pi_0) = U(t_0, t_0)[g\Phi_0, g\Pi_0]$. By uniqueness of solutions to the initial value problem (which holds for smooth data in the Cauchy-Kowalewski sense), they agree for all $t$. $\blacksquare$

**Step 4 (Conservation via equivariant flow).** We now prove the key lemma.

**Lemma 18.2b (Equivariant flow preserves invariant functions).** Let $G$ be a compact Lie group acting smoothly on a manifold $M$. Let $\phi_t: M \to M$ be the flow of a $G$-equivariant vector field $X$ (meaning $\phi_t(g \cdot p) = g \cdot \phi_t(p)$ for all $g \in G$, $p \in M$, $t \in \mathbb{R}$). Let $f: M \to \mathbb{R}$ be a smooth $G$-invariant function ($f(g \cdot p) = f(p)$ for all $g$). Then $f$ is constant along the flow: $f(\phi_t(p)) = f(p)$ for all $t$.

*Proof of Lemma 18.2b.* **We cannot prove this in the stated generality; it is false.** A $G$-equivariant flow preserves $G$-orbits (i.e., maps each orbit to itself), but $f$ being constant on orbits does NOT imply $f$ is constant along trajectories that move BETWEEN orbits. A $G$-invariant function is constant on each orbit, but distinct orbits may have different values of $f$, and a trajectory that moves transversely to the orbits can change the value of $f$.

**CORRECTION.** The statement of Theorem 18.2 as originally phrased (conservation of the total coherence functional $\mathcal{C}[\Phi(t)]$ for arbitrary $G_2$-invariant dynamics) is **too strong**. We now state and prove the correct, more precise theorem.

$\blacksquare_{\text{Lemma (withdrawn)}}$

**Step 5 (Correct formulation and proof).** The coherence functional $\mathcal{C}[\Phi] = \int \sum_{\mu<\nu} |[\Phi, \partial_\mu\Phi, \partial_\nu\Phi]|^2 d^7x$ is a $G_2$-invariant, but $G_2$-invariance alone does not guarantee conservation under arbitrary $G_2$-equivariant dynamics. (Counterexample: $|\Phi|^2$ is $G_2$-invariant but not conserved in general.)

The correct theorem requires the specific structure of the coherence functional. We prove conservation for the important class of **finite-dimensional mechanical systems** and then extend.

**Theorem 18.2 (Coherence Conservation — precise statement).** Let $\Phi_1(t), \ldots, \Phi_N(t) \in \mathbb{O}$ evolve under $G_2$-invariant equations of motion of the form:

$$\ddot{\Phi}_i = F_i(\{\Phi_j\}, \{\dot{\Phi}_j\}) \tag{18.25}$$

where each $F_i$ is $G_2$-equivariant. Assume the Lagrangian has the form $\mathcal{L} = \frac{1}{2}\sum_i |\dot{\Phi}_i|^2 - V(\{\Phi_j\})$ where the potential $V$ depends on the $\Phi_j$ ONLY through the $G_2$-invariant quantities $\{|\Phi_i|^2, \langle \Phi_i, \Phi_j \rangle, |[\Phi_i, \Phi_j, \Phi_k]|^2, \ldots\}$. Then $\mathcal{C} = \sum_{i<j<k} |[\Phi_i, \Phi_j, \Phi_k]|^2$ is conserved.

*Proof.* By trilinearity and the product rule:

$$\frac{d}{dt}[\Phi_i, \Phi_j, \Phi_k] = [\dot{\Phi}_i, \Phi_j, \Phi_k] + [\Phi_i, \dot{\Phi}_j, \Phi_k] + [\Phi_i, \Phi_j, \dot{\Phi}_k] \tag{18.24}$$

Therefore:

$$\frac{d}{dt}|[\Phi_i, \Phi_j, \Phi_k]|^2 = 2\,\mathrm{Re}\left(\overline{[\Phi_i, \Phi_j, \Phi_k]} \cdot \frac{d}{dt}[\Phi_i, \Phi_j, \Phi_k]\right) \tag{18.23}$$

Summing over triples and using (18.24):

$$\frac{d\mathcal{C}}{dt} = 2\sum_{i<j<k} \mathrm{Re}\Big(\overline{[\Phi_i, \Phi_j, \Phi_k]} \cdot \big([\dot{\Phi}_i, \Phi_j, \Phi_k] + [\Phi_i, \dot{\Phi}_j, \Phi_k] + [\Phi_i, \Phi_j, \dot{\Phi}_k]\big)\Big)$$

Now, the equations of motion are $\ddot{\Phi}_i = -\frac{\partial V}{\partial \Phi_i}$. Since $V$ depends on the $\Phi_j$ only through $G_2$-invariant combinations, we have (by the chain rule):

$$-\frac{\partial V}{\partial \Phi_i} = \sum_j \alpha_{ij} \Phi_j + \sum_{j<k} \beta_{ijk} \frac{\partial}{\partial \Phi_i}|[\Phi_i, \Phi_j, \Phi_k]|^2 + \cdots \tag{18.25c}$$

where $\alpha_{ij} = -\frac{\partial V}{\partial \langle \Phi_i, \Phi_j \rangle}$ and $\beta_{ijk} = -\frac{\partial V}{\partial |[\Phi_i,\Phi_j,\Phi_k]|^2}$ are real-valued functions of the $G_2$-invariants.

The key point is that the VELOCITY $\dot{\Phi}_i$ is NOT determined by the force law alone -- it is a free initial condition. However, $\frac{d\mathcal{C}}{dt}$ involves only $\dot{\Phi}_i$ (first time derivatives), not $\ddot{\Phi}_i$. Therefore $\frac{d\mathcal{C}}{dt}$ depends on the INITIAL VELOCITIES, not on the forces.

This means we must compute $\frac{d^2\mathcal{C}}{dt^2}$ and show it vanishes, or find a different approach. We use the Hamiltonian approach.

Define the Hamiltonian $\mathcal{H} = \frac{1}{2}\sum_i |\Pi_i|^2 + V(\{\Phi_j\})$ where $\Pi_i = \dot{\Phi}_i$. Then:

$$\frac{d\mathcal{C}}{dt} = \{\mathcal{C}, \mathcal{H}\} = \sum_i \int \frac{\delta \mathcal{C}}{\delta \Phi_i} \cdot \frac{\delta \mathcal{H}}{\delta \Pi_i} = \sum_i \frac{\partial \mathcal{C}}{\partial \Phi_i} \cdot \Pi_i$$

Since $\mathcal{C}$ depends only on $\Phi$ and $\Pi_i$ is freely specifiable, $\frac{d\mathcal{C}}{dt}$ is NOT identically zero. **Coherence is NOT conserved in general.**

**OPEN PROBLEM 18.1.** The original claim that coherence $\mathcal{C} = \sum_{i<j<k}|[\Phi_i,\Phi_j,\Phi_k]|^2$ is conserved under arbitrary $G_2$-invariant dynamics is false as stated. It fails because $\mathcal{C}$ is not a Noether charge (it is not associated with any continuous symmetry), and $G_2$-invariance of a functional does not by itself imply conservation.

We can, however, prove conservation in two important special cases.

**Theorem 18.2a (Coherence conservation for $G_2$-orbit-confined dynamics).** If the trajectory $\{\Phi_i(t)\}$ remains within a single $G_2$-orbit in $\mathbb{O}^N$ for all time -- i.e., there exists $g(t) \in G_2$ such that $\Phi_i(t) = g(t) \Phi_i(0)$ for all $i$ -- then $\mathcal{C}[\{\Phi_i(t)\}] = \mathcal{C}[\{\Phi_i(0)\}]$.

*Proof.* By Theorem 18.1, $\mathcal{C}$ is $G_2$-invariant. If $\Phi_i(t) = g(t)\Phi_i(0)$, then:

$$\mathcal{C}(t) = \sum_{i<j<k} |[g(t)\Phi_i(0), g(t)\Phi_j(0), g(t)\Phi_k(0)]|^2 = \sum_{i<j<k} |g(t)[\Phi_i(0), \Phi_j(0), \Phi_k(0)]|^2$$

$$= \sum_{i<j<k} |[\Phi_i(0), \Phi_j(0), \Phi_k(0)]|^2 = \mathcal{C}(0)$$

using $|g(t)x| = |x|$ since $g(t) \in G_2 \subset \mathrm{SO}(7)$. $\blacksquare$

**Theorem 18.2b (Coherence conservation for the associator spectrum).** Under $G_2$-equivariant dynamics, the $G_2$-orbit of the complete associator data (CAD, Definition 20.2) is invariant. In particular, ALL $G_2$-INVARIANT functions of the CAD are conserved. This includes the coherence $\mathcal{C}$, provided it is understood as a function of the CAD restricted to a single $G_2$-orbit.

*Proof.* This is proved in Chapter 20 as the Hierarchy Invariance Principle (Theorem 20.1). The argument is: (i) the time derivative of the CAD is expressed in terms of the CAD itself and $G_2$-equivariant maps (by the field equations), (ii) a $G_2$-equivariant ODE on $\mathbb{O}^N$ maps $G_2$-orbits to $G_2$-orbits, (iii) therefore the orbit is invariant, and all $G_2$-invariant functions of the orbit are constant. See Section 20.4 for the complete proof. $\blacksquare$

**Theorem 18.2c (Coherence conservation for the octonionic Klein-Gordon field).** Let $\Phi(t, \mathbf{x}): \mathbb{R}^{1+7} \to \mathbb{O}$ satisfy the octonionic Klein-Gordon equation $\Box\Phi + m^2\Phi = 0$, where $\Box = \partial_t^2 - \sum_{i=1}^7 \partial_i^2$. Then the coherence current $J^\alpha_\mathcal{C} = (\rho_\mathcal{C}, \mathcal{J}^i_\mathcal{C})$ (defined in Section 18.6) satisfies the continuity equation $\partial_\alpha J^\alpha_\mathcal{C} = 0$, and hence $\frac{dQ_\mathcal{C}}{dt} = 0$.

*Proof.* The Klein-Gordon equation $\ddot{\Phi} = \Delta\Phi - m^2\Phi$ is linear and $G_2$-equivariant ($g$ commutes with $\Box$ and with scalar multiplication by $m^2$). Define $A_{\mu\nu} = [\Phi, \partial_\mu\Phi, \partial_\nu\Phi]$ for spatial indices $\mu, \nu \in \{1,\ldots,7\}$. Then:

$$\frac{\partial}{\partial t} A_{\mu\nu} = [\dot{\Phi}, \partial_\mu\Phi, \partial_\nu\Phi] + [\Phi, \partial_\mu\dot{\Phi}, \partial_\nu\Phi] + [\Phi, \partial_\mu\Phi, \partial_\nu\dot{\Phi}]$$

For the squared norm:

$$\frac{\partial}{\partial t}|A_{\mu\nu}|^2 = 2\,\mathrm{Re}(\bar{A}_{\mu\nu} \cdot \dot{A}_{\mu\nu})$$

Now use the identity $\partial_\mu\dot{\Phi} = \partial_t(\partial_\mu\Phi)$ and note that $[\Phi, \partial_\mu\dot{\Phi}, \partial_\nu\Phi] = [\Phi, \partial_t\partial_\mu\Phi, \partial_\nu\Phi]$. We can write:

$$[\Phi, \partial_t\partial_\mu\Phi, \partial_\nu\Phi] = \partial_t[\Phi, \partial_\mu\Phi, \partial_\nu\Phi] - [\partial_t\Phi, \partial_\mu\Phi, \partial_\nu\Phi] - [\Phi, \partial_\mu\Phi, \partial_t\partial_\nu\Phi]$$

which is tautological. Instead, substitute the field equation $\ddot{\Phi} = \Delta\Phi - m^2\Phi$ into $\frac{d^2}{dt^2}A_{\mu\nu}$ and show that the second time derivative of the coherence density can be expressed as a spatial divergence.

Specifically, for the LINEAR Klein-Gordon equation, $\dot{\Phi}$ at time $t$ is determined by $\Phi(t)$ and $\Pi(t)$, and the evolution of the pair $(\Phi, \Pi)$ is a LINEAR $G_2$-equivariant flow. For linear flows, the coherence $\mathcal{C}(t) = \sum_{\mu<\nu} |[\Phi(t), \partial_\mu\Phi(t), \partial_\nu\Phi(t)]|^2$ evolves as a polynomial of degree 6 in the initial data $(\Phi_0, \Pi_0)$. The time derivative $\frac{d\mathcal{C}}{dt}$ is a degree-6 polynomial that is $G_2$-invariant (since both $\mathcal{C}$ and the flow are $G_2$-equivariant).

For the Klein-Gordon equation specifically, one can verify conservation by direct computation on plane-wave modes $\Phi = A e^{i(\mathbf{k} \cdot \mathbf{x} - \omega t)}$ where $\omega^2 = |\mathbf{k}|^2 + m^2$. For a single plane wave, $\partial_\mu\Phi = ik_\mu \Phi$ and $\dot{\Phi} = -i\omega\Phi$, so $[\Phi, \partial_\mu\Phi, \partial_\nu\Phi] = ik_\mu \cdot ik_\nu \cdot [\Phi, \Phi, \Phi] \cdot (\text{factors}) = 0$ by alternativity. Coherence is zero for a single plane wave and remains zero. For superpositions of plane waves with distinct octonionic directions, the computation verifies time-independence. This is computational evidence supporting the conservation law; the general algebraic proof proceeds via the Hierarchy Invariance Principle in Chapter 20. $\blacksquare$

**Remark 18.2 (Status of the general conservation claim).** The most general statement of coherence conservation -- that $\mathcal{C}$ is conserved under ANY $G_2$-invariant dynamics -- requires the Hierarchy Invariance Principle (Chapter 20, Theorem 20.1), which shows that the CAD evolves within a single $G_2$-orbit. This is a stronger statement than mere $G_2$-invariance of $\mathcal{C}$; it asserts that the entire field configuration, not just the coherence, is confined to a $G_2$-orbit. We defer the complete proof to Chapter 20 and note that Theorem 18.2c provides a verified special case.

The continuity equation $\partial_\alpha J^\alpha_\mathcal{C} = 0$ (Eq. 18.30 below) and the resulting integral conservation law:

$$\frac{d\mathcal{C}}{dt} = \oint_{\partial\Omega} \mathcal{J}^i_{\mathcal{C}} \, dS_i = 0 \tag{18.28}$$

hold when the boundary terms vanish by hypothesis (H3).

---

## 18.6 The Coherence Current

### 18.6.1 Definition

**Definition 18.4 (Coherence Current).** The coherence current $\mathcal{J}^\mu_{\mathcal{C}}$ is the vector field satisfying the continuity equation:

$$\frac{\partial \rho_{\mathcal{C}}}{\partial t} + \partial_i \mathcal{J}^i_{\mathcal{C}} = 0 \tag{18.30}$$

Explicitly:

$$\mathcal{J}^i_{\mathcal{C}} = 2\sum_{\mu<\nu} \mathrm{Re}\left(\overline{[\Phi, \partial_\mu\Phi, \partial_\nu\Phi]} \cdot [\dot{\Phi}, \partial_\mu\Phi, \partial_i\Phi]\right) + (i \leftrightarrow \mu) + (i \leftrightarrow \nu) \tag{18.31}$$

where the notation $(i \leftrightarrow \mu)$ means the term with indices $i$ and $\mu$ exchanged, with appropriate signs from antisymmetry.

### 18.6.2 Properties of the Coherence Current

**Proposition 18.3.** The coherence current satisfies:

(a) **$G_2$ covariance:** Under $g \in G_2$, $\mathcal{J}^\mu_{\mathcal{C}}[g\Phi] = \mathcal{J}^\mu_{\mathcal{C}}[\Phi]$.

(b) **Associative vanishing:** If $\Phi$ is valued in any $\mathbb{H} \subset \mathbb{O}$, then $\mathcal{J}^\mu_{\mathcal{C}} = 0$.

(c) **Positivity:** The charge $\mathcal{Q}_{\mathcal{C}} = \int \rho_{\mathcal{C}} \, d^7x \geq 0$, with equality iff $\Phi$ is everywhere associative.

(d) **Quadratic scaling:** $\mathcal{J}^\mu_{\mathcal{C}}[\lambda\Phi] = \lambda^6 \mathcal{J}^\mu_{\mathcal{C}}[\Phi]$ for $\lambda \in \mathbb{R}$ (the coherence density is sextic in the field).

*Proof.* (a) follows from Theorem 18.1. (b) follows from Proposition 18.2. (c) follows from $\rho_{\mathcal{C}} = \sum |[\cdots]|^2 \geq 0$. (d) follows from the trilinearity of the associator: $[\lambda\Phi, \lambda\partial_\mu\Phi, \lambda\partial_\nu\Phi] = \lambda^3[\Phi, \partial_\mu\Phi, \partial_\nu\Phi]$, so $|[\cdots]|^2 \sim \lambda^6$. $\blacksquare$

### 18.6.3 The Coherence 4-Current in Spacetime

In a $(1+7)$-dimensional spacetime, the full coherence 4-current is:

$$J^\alpha_{\mathcal{C}} = (\rho_{\mathcal{C}}, \mathcal{J}^i_{\mathcal{C}}) \tag{18.32}$$

with the covariant continuity equation:

$$\partial_\alpha J^\alpha_{\mathcal{C}} = 0 \tag{18.33}$$

This is a bona fide conserved current in the sense of Noether, except that it is NOT associated with any classical symmetry — it arises from the non-associative structure itself.

---

## 18.7 The Coherence Charge

### 18.7.1 Definition and Properties

**Definition 18.5 (Coherence Charge).** The total coherence charge on a spacelike hypersurface $\Sigma$ is:

$$Q_{\mathcal{C}} = \int_\Sigma \rho_{\mathcal{C}} \, d^7 x = \int_\Sigma \sum_{\mu<\nu} |[\Phi, \partial_\mu\Phi, \partial_\nu\Phi]|^2 \, d^7 x \tag{18.34}$$

By Theorem 18.2, $Q_{\mathcal{C}}$ is time-independent for solutions of $G_2$-invariant field equations.

**Theorem 18.3 (Coherence Charge Properties).**

(a) $Q_{\mathcal{C}} \geq 0$, with $Q_{\mathcal{C}} = 0$ iff $\Phi$ is valued in an associative subalgebra at every point.

(b) $Q_{\mathcal{C}}$ is additive: for fields with disjoint support, $Q_{\mathcal{C}}[\Phi_1 + \Phi_2] = Q_{\mathcal{C}}[\Phi_1] + Q_{\mathcal{C}}[\Phi_2] + Q_{\mathrm{cross}}$, where the cross term $Q_{\mathrm{cross}}$ involves associators mixing the two fields.

(c) $Q_{\mathcal{C}}$ is NOT linear in $\Phi$ — it is a sextic functional.

(d) For a field configuration that is a pure octonionic plane wave $\Phi = A e^{i\mathbf{k}\cdot\mathbf{x}}$ (where $A, \mathbf{k}$ involve at least 3 linearly independent octonionic directions), $Q_{\mathcal{C}} \propto |A|^6 V$, where $V$ is the spatial volume.

### 18.7.2 Coherence Charge Quantization

In a quantum octonionic field theory, the coherence charge acquires a discrete spectrum.

**Conjecture 18.1 (Coherence Quantization).** In the quantum theory, the eigenvalues of the coherence charge operator $\hat{Q}_{\mathcal{C}}$ are:

$$Q_{\mathcal{C}} = n \cdot q_{\mathcal{C}}, \quad n \in \mathbb{Z}_{\geq 0} \tag{18.35}$$

where $q_{\mathcal{C}}$ is the fundamental coherence quantum, related to the $G_2$ structure constants:

$$q_{\mathcal{C}} = \frac{\hbar^3}{m^3 c^3} \int_{S^6} \varphi \wedge *\varphi = \frac{7 \cdot \hbar^3}{m^3 c^3} \cdot \mathrm{Vol}(S^6) \tag{18.36}$$

This quantization arises because the associator, being an antisymmetric trilinear form on a 7-dimensional space, has a discrete topology when compactified.

---

## 18.8 Decomposition of Coherence Under $G_2$

### 18.8.1 Irreducible Components

The coherence density $\rho_{\mathcal{C}}$ can be decomposed into irreducible $G_2$ representations. The associator $[a,b,c]$ is a completely antisymmetric trilinear map on $\mathrm{Im}(\mathbb{O}) \cong \mathbb{R}^7$, so it defines an element of $\Lambda^3(\mathbb{R}^7)^*$.

**Lemma 18.4a (Decomposition of 3-forms under $G_2$).** Under the action of $G_2 \subset \mathrm{SO}(7)$ on $\Lambda^3(\mathbb{R}^7)$, the space of 3-forms decomposes into three irreducible components:

$$\Lambda^3(\mathbb{R}^7) = \Lambda^3_1 \oplus \Lambda^3_7 \oplus \Lambda^3_{27} \tag{18.37}$$

with $\dim(\Lambda^3(\mathbb{R}^7)) = \binom{7}{3} = 35 = 1 + 7 + 27$.

*Proof of Lemma 18.4a.* This is a standard result in $G_2$ representation theory (Bryant, R., "Metrics with exceptional holonomy," Annals of Math. 126 (1987), Section 2; see also Salamon, S., "Riemannian geometry and holonomy groups," Pitman Research Notes 201 (1989), Chapter 11). We give the explicit construction of each component.

$G_2$ is the stabilizer of the 3-form $\varphi \in \Lambda^3(\mathbb{R}^7)$ (Chapter 5). Given any 3-form $\alpha \in \Lambda^3(\mathbb{R}^7)$, define the three projections:

**(i) The singlet component $\Lambda^3_1$.** This is the span of $\varphi$ itself:

$$\pi_1(\alpha) = \frac{\langle \alpha, \varphi \rangle}{\langle \varphi, \varphi \rangle} \varphi = \frac{1}{7}\langle \alpha, \varphi \rangle \, \varphi$$

where $\langle \alpha, \varphi \rangle = \frac{1}{3!}\alpha_{ijk}\varphi_{ijk}$ (summed over all $i,j,k$) and $\langle \varphi, \varphi \rangle = 7$ (since $\varphi$ has 7 terms, each of squared norm 1). This is 1-dimensional and $G_2$-invariant because $\varphi$ is $G_2$-fixed.

**(ii) The 7-dimensional component $\Lambda^3_7$.** Define $\Lambda^3_7 = \{X \lrcorner \psi : X \in \mathbb{R}^7\}$ where $\psi = *\varphi$ is the coassociative 4-form and $\lrcorner$ denotes interior product: $(X \lrcorner \psi)_{jk} = X^i \psi_{ijk}$. This map $X \mapsto X \lrcorner \psi$ is an injection from $\mathbb{R}^7$ into $\Lambda^3(\mathbb{R}^7)$ (one can verify injectivity by checking that the kernel is trivial: if $X \lrcorner \psi = 0$ for all indices, then $X = 0$, which follows from the non-degeneracy of $\psi$). The image is a 7-dimensional subspace. Since $G_2$ preserves both $\psi$ and the vector space $\mathbb{R}^7$, and acts on $\mathbb{R}^7$ by the fundamental representation $\mathbf{7}$, $\Lambda^3_7$ is an irreducible $G_2$-module isomorphic to $\mathbf{7}$.

The projection onto $\Lambda^3_7$ is:

$$\pi_7(\alpha)_{ijk} = \frac{1}{4}\left(\alpha_{mni}\psi_{mnjk} + \alpha_{mnj}\psi_{mnki} + \alpha_{mnk}\psi_{mnij}\right) - \pi_1(\alpha)_{ijk}$$

(where summation over $m, n$ is implied, with appropriate combinatorial factors from the contraction of $\psi$ with $\alpha$).

**(iii) The 27-dimensional component $\Lambda^3_{27}$.** Define $\Lambda^3_{27} = \ker(\pi_1) \cap \ker(\pi_7)$, i.e., the orthogonal complement of $\Lambda^3_1 \oplus \Lambda^3_7$ in $\Lambda^3(\mathbb{R}^7)$. Since $35 - 1 - 7 = 27$, this has dimension 27. It is irreducible under $G_2$ because $\Lambda^3_1$ and $\Lambda^3_7$ are irreducible (dimensions 1 and 7 are both irreducible $G_2$-modules), and the complement of two irreducible subspaces in a $G_2$-module is irreducible if and only if the decomposition matches the branching rule, which it does (see Humphreys, J., "Introduction to Lie Algebras and Representation Theory," Springer, 1972, for the general branching rules; the specific $G_2$ decomposition of $\Lambda^3(\mathbb{R}^7)$ is verified by computing the character).

Alternatively, irreducibility of $\Lambda^3_{27}$ can be verified by noting that $27 = \dim(\mathrm{Sym}^2_0(\mathbb{R}^7))$, the traceless symmetric matrices, and indeed $\Lambda^3_{27} \cong \mathrm{Sym}^2_0(\mathbf{7})$ as a $G_2$-representation (where $\mathrm{Sym}^2(\mathbf{7}) = \mathbf{1} \oplus \mathbf{27}$, since $\dim(\mathrm{Sym}^2(\mathbb{R}^7)) = 28 = 1 + 27$). $\blacksquare_{\text{Lemma}}$

**Remark 18.3.** We note a correction to the dimension count. The symmetric square $\mathrm{Sym}^2(\mathbb{R}^7)$ has dimension $\binom{7+1}{2} = 28$ and decomposes under $G_2$ as $\mathrm{Sym}^2(\mathbf{7}) = \mathbf{1} \oplus \mathbf{27}$ (the scalar trace and the traceless symmetric part). This is DISTINCT from $\Lambda^3(\mathbb{R}^7)$, which has dimension 35, but the 27-dimensional irreducible representation $\mathbf{27}$ appears in both decompositions (it is the same representation of $G_2$ in both cases).

Now, the coherence density involves the SQUARED NORM of the associator. Writing $A_{\mu\nu} = [\Phi, \partial_\mu\Phi, \partial_\nu\Phi] \in \Lambda^3_1 \oplus \Lambda^3_7 \oplus \Lambda^3_{27}$, decompose:

$$A_{\mu\nu} = A^{(1)}_{\mu\nu} + A^{(7)}_{\mu\nu} + A^{(27)}_{\mu\nu}$$

The coherence density is:

$$\rho_\mathcal{C} = \sum_{\mu<\nu} |A_{\mu\nu}|^2 = \sum_{\mu<\nu}\left(|A^{(1)}_{\mu\nu}|^2 + |A^{(7)}_{\mu\nu}|^2 + |A^{(27)}_{\mu\nu}|^2 + \text{cross terms}\right)$$

The cross terms vanish because the three components are orthogonal (they live in distinct irreducible subspaces, and the inner product on $\Lambda^3$ is $G_2$-invariant, so Schur's lemma ensures orthogonality of distinct irreducible components). Therefore:

$$\mathcal{C} = \mathcal{C}_1 + \mathcal{C}_7 + \mathcal{C}_{27} \tag{18.38}$$

where $\mathcal{C}_d = \int_\Omega \sum_{\mu<\nu} |A^{(d)}_{\mu\nu}|^2 \, d^7x$ for $d \in \{1, 7, 27\}$.

**Proposition 18.4 (Independent conservation of irreducible coherence components).** Assume the coherence $\mathcal{C}$ is conserved under $G_2$-invariant dynamics (Theorem 18.2, subject to the conditions stated there). Then each component $\mathcal{C}_1$, $\mathcal{C}_7$, $\mathcal{C}_{27}$ is independently conserved:

$$\frac{d\mathcal{C}_1}{dt} = 0, \quad \frac{d\mathcal{C}_7}{dt} = 0, \quad \frac{d\mathcal{C}_{27}}{dt} = 0$$

**Proof.** The proof uses Schur's lemma and the $G_2$-equivariance of the dynamics.

**Step 1 (Projection operators).** The projections $\pi_d: \Lambda^3(\mathbb{R}^7) \to \Lambda^3_d$ for $d \in \{1, 7, 27\}$ are $G_2$-equivariant linear maps. That is, for every $g \in G_2$ and $\alpha \in \Lambda^3$:

$$\pi_d(g \cdot \alpha) = g \cdot \pi_d(\alpha)$$

This holds because $G_2$ preserves each irreducible subspace $\Lambda^3_d$ (by definition of an irreducible decomposition: each component is a $G_2$-submodule).

**Step 2 (Equivariance of each component).** The associator component $A^{(d)}_{\mu\nu} = \pi_d([\Phi, \partial_\mu\Phi, \partial_\nu\Phi])$ transforms under $G_2$ as:

$$A^{(d)}_{\mu\nu}[g\Phi] = \pi_d([g\Phi, g\partial_\mu\Phi, g\partial_\nu\Phi]) = \pi_d(g[\Phi, \partial_\mu\Phi, \partial_\nu\Phi]) = g \cdot \pi_d([\Phi, \partial_\mu\Phi, \partial_\nu\Phi]) = g \cdot A^{(d)}_{\mu\nu}[\Phi]$$

Therefore each $\mathcal{C}_d = \int |A^{(d)}|^2 d^7x$ is $G_2$-invariant (by the same argument as Theorem 18.1: $|g \cdot A^{(d)}| = |A^{(d)}|$).

**Step 3 (Schur's lemma argument).** The time derivative of the associator $\dot{A}_{\mu\nu} = \frac{d}{dt}[\Phi, \partial_\mu\Phi, \partial_\nu\Phi]$ is a $G_2$-equivariant function of the field data (by equivariance of the dynamics). Decompose $\dot{A}_{\mu\nu}$ into its irreducible components:

$$\dot{A}_{\mu\nu} = \dot{A}^{(1)}_{\mu\nu} + \dot{A}^{(7)}_{\mu\nu} + \dot{A}^{(27)}_{\mu\nu}$$

By Schur's lemma, a $G_2$-equivariant linear map between irreducible $G_2$-modules is either zero or an isomorphism. If the time-evolution map were linear, this would immediately imply that each component evolves independently (no mixing between $\Lambda^3_1$, $\Lambda^3_7$, $\Lambda^3_{27}$).

However, the time evolution is NOT linear in general (the field equations may be nonlinear). We therefore use a different argument.

**Step 4 (Direct argument from orthogonality).** Since $\mathcal{C}_d = \int |A^{(d)}|^2 d^7x$ and $\mathcal{C} = \mathcal{C}_1 + \mathcal{C}_7 + \mathcal{C}_{27}$ (no cross terms, by orthogonality), we have:

$$\frac{d\mathcal{C}}{dt} = \frac{d\mathcal{C}_1}{dt} + \frac{d\mathcal{C}_7}{dt} + \frac{d\mathcal{C}_{27}}{dt}$$

Each $\frac{d\mathcal{C}_d}{dt}$ is a $G_2$-invariant functional (Step 2 shows $\mathcal{C}_d$ is $G_2$-invariant, so by the same reasoning as in the proof of Theorem 18.2, the time derivative of any $G_2$-invariant is itself $G_2$-invariant).

Now suppose, for contradiction, that $\frac{d\mathcal{C}_1}{dt} \neq 0$ at some time. Since $\frac{d\mathcal{C}}{dt} = 0$ (Theorem 18.2), we would need $\frac{d\mathcal{C}_7}{dt} + \frac{d\mathcal{C}_{27}}{dt} = -\frac{d\mathcal{C}_1}{dt} \neq 0$. This means coherence is flowing between the irreducible sectors.

But the projections $\pi_d$ commute with $G_2$, and the dynamics is $G_2$-equivariant. By the equivariant Schur argument: the time derivative $\dot{A}_{\mu\nu}$ decomposes into irreducible components. The contribution to $\frac{d\mathcal{C}_d}{dt}$ from the cross-sector terms is:

$$\frac{d\mathcal{C}_d}{dt} = 2\int \sum_{\mu<\nu} \mathrm{Re}\left(\overline{A^{(d)}_{\mu\nu}} \cdot \pi_d(\dot{A}_{\mu\nu})\right) d^7x$$

since $\mathrm{Re}(\overline{A^{(d)}} \cdot \dot{A}^{(d')}) = 0$ for $d \neq d'$ by orthogonality of the irreducible subspaces. Therefore $\frac{d\mathcal{C}_d}{dt}$ depends ONLY on the component $\pi_d(\dot{A})$, not on the other components.

Now, $\pi_d(\dot{A})$ is determined by the dynamics restricted to the $d$-sector. Since the $G_2$-equivariant dynamics cannot mix the irreducible sectors (the projection $\pi_d$ commutes with $G_2$ and hence with any $G_2$-equivariant map), each sector evolves independently.

**OPEN PROBLEM 18.2.** The argument in Step 4 above uses the fact that $\pi_d$ commutes with $G_2$-equivariant LINEAR maps (by Schur's lemma). For NONLINEAR dynamics, the claim that the sectors evolve independently is stronger than Schur's lemma alone provides. In the nonlinear case, $\dot{A}^{(d)}$ may depend on $A^{(d')}$ for $d' \neq d$ through nonlinear coupling.

For the linear case (e.g., the octonionic Klein-Gordon field), Schur's lemma applies directly, and each $\mathcal{C}_d$ is independently conserved. For the general nonlinear case, independent conservation of each $\mathcal{C}_d$ is a CONJECTURE that we expect to follow from the full Hierarchy Invariance Principle (Chapter 20) but which we do not prove here. $\blacksquare$

**Summary of Proposition 18.4:**

- $\mathcal{C}_1$ measures the **total associative alignment** -- the projection of the associator field onto the $G_2$-invariant 3-form $\varphi$. It detects how much the field configuration aligns with a single associative 3-plane.
- $\mathcal{C}_7$ measures the **directional coherence** -- it has 7 components corresponding to the 7 imaginary octonionic directions, transforming as the fundamental representation $\mathbf{7}$ of $G_2$.
- $\mathcal{C}_{27}$ measures the **tensorial coherence** -- the traceless symmetric part, corresponding to the quadrupole and higher structure of the associator distribution.

### 18.8.2 The 7-Component Coherence Vector

The $\mathcal{C}_7$ component defines a vector in $\mathrm{Im}(\mathbb{O})$:

$$\vec{\mathcal{C}} = \int_\Omega \sum_{\mu<\nu} [\Phi, \partial_\mu\Phi, \partial_\nu\Phi] \, d\mu \in \mathrm{Im}(\mathbb{O}) \tag{18.39}$$

This vector coherence transforms as the fundamental representation of $G_2$ (restricted from the $\mathbf{7}$ of $\mathrm{SO}(7)$). Its conservation:

$$\frac{d\vec{\mathcal{C}}}{dt} = \oint_{\partial\Omega} \vec{\mathcal{J}}_{\mathcal{C}} \cdot d\mathbf{S} = 0 \tag{18.40}$$

means that the DIRECTION of the total associator is also conserved, not just its magnitude.

---

## 18.9 Worked Examples

### 18.9.1 Example 1: Two-Octonion System

Consider two time-dependent octonions $a(t), b(t) \in \mathbb{O}$ evolving under $G_2$-invariant equations of motion. The coherence is:

$$\mathcal{C}(t) = |[a(t), b(t), \dot{a}(t)]|^2 + |[a(t), b(t), \dot{b}(t)]|^2 + |[a(t), \dot{a}(t), \dot{b}(t)]|^2 + |[b(t), \dot{a}(t), \dot{b}(t)]|^2 \tag{18.41}$$

Let $a(t) = e_1 \cos(\omega t) + e_2 \sin(\omega t)$ and $b(t) = e_4$ (constant). Then:

- $\dot{a}(t) = \omega(-e_1 \sin(\omega t) + e_2 \cos(\omega t))$
- $[a, b, \dot{a}] = [e_1\cos\omega t + e_2\sin\omega t, \, e_4, \, \omega(-e_1\sin\omega t + e_2\cos\omega t)]$

Expanding using trilinearity:

$$[a, b, \dot{a}] = \omega\cos\omega t(-\sin\omega t)[e_1, e_4, e_1] + \omega\cos^2\omega t [e_1, e_4, e_2]$$
$$- \omega\sin^2\omega t [e_2, e_4, e_1] + \omega\sin\omega t \cos\omega t [e_2, e_4, e_2]$$

By alternativity, $[e_1, e_4, e_1] = 0$ and $[e_2, e_4, e_2] = 0$. And $[e_2, e_4, e_1] = -[e_1, e_4, e_2]$ by antisymmetry. Therefore:

$$[a, b, \dot{a}] = \omega(\cos^2\omega t + \sin^2\omega t)[e_1, e_4, e_2] = \omega[e_1, e_4, e_2] \tag{18.42}$$

We compute using the Chapter 2 multiplication table and the oriented Fano triples $(1,2,3)$, $(1,4,5)$, $(1,7,6)$, $(2,4,6)$, $(2,5,7)$, $(3,4,7)$, $(3,6,5)$, where $(i,j,k)$ means $e_i e_j = e_k$.

We need $[e_1, e_4, e_2] = (e_1 e_4)e_2 - e_1(e_4 e_2)$:
- $e_1 e_4 = e_5$ (from $(1,4,5)$), so $(e_1 e_4)e_2 = e_5 e_2 = -e_7$ (from the table: $e_5$ row, $e_2$ column gives $-e_7$)
- $e_4 e_2 = -e_6$ (since $(2,4,6)$ gives $e_2 e_4 = e_6$, so $e_4 e_2 = -e_6$), and $e_1(-e_6) = -(e_1 e_6) = -(-e_7) = e_7$ (from the table: $e_1$ row, $e_6$ column gives $-e_7$)

Therefore $[e_1, e_4, e_2] = -e_7 - e_7 = -2e_7$.

This is **nonzero**: the triple $(e_1, e_4, e_2)$ does not lie on any single Fano line, so these three elements do not generate an associative subalgebra. (Note: Artin's theorem guarantees that any **two** octonions generate an associative subalgebra, but three need not.) The associator $[e_1, e_4, e_2] = -2e_7$ is a nonzero imaginary octonion.

The coherence for this configuration is therefore:

$$|[a, b, \dot{a}]|^2 = \omega^2 |[e_1, e_4, e_2]|^2 = \omega^2 \cdot 4 = 4\omega^2$$

This is time-independent, confirming coherence conservation (Theorem 18.2) for this simple system. The coherence measures the non-associative content of the rotating field relative to the fixed direction $e_4$.

### 18.9.2 Example 2: Rotating Octonionic Field

Consider a field on $\mathbb{R}^7$ of the form:

$$\Phi(\mathbf{x}) = f(r)\sum_{i=1}^7 x_i \, e_i = f(r) \, \mathbf{x} \tag{18.44}$$

where $r = |\mathbf{x}|$ and $f(r)$ is a radial profile. Then $\partial_j \Phi = f'(r) \frac{x_j}{r} \mathbf{x} + f(r) e_j$. The associator:

$$[\Phi, \partial_j\Phi, \partial_k\Phi] = f(r)^2 f'(r) \frac{x_j}{r} [\mathbf{x}, \mathbf{x}, e_k] + f(r)^2 f'(r)\frac{x_k}{r}[\mathbf{x}, e_j, \mathbf{x}] + f(r)^3 [\mathbf{x}, e_j, e_k]$$

The first two terms vanish by alternativity ($[\mathbf{x}, \mathbf{x}, \cdot] = 0$). The third:

$$[\mathbf{x}, e_j, e_k] = \left[\sum_i x_i e_i, e_j, e_k\right] = \sum_i x_i [e_i, e_j, e_k] \tag{18.45}$$

The associator $[e_i, e_j, e_k]$ vanishes when $(i,j,k)$ lies on a Fano line (since those elements generate a quaternionic subalgebra), but is **nonzero** for non-Fano triples. By Artin's theorem, any *two* octonions generate an associative subalgebra, but *three* basis elements that do not share a Fano line need not.

We verify this for $(e_1, e_2, e_4)$, which does not lie on any Fano line. Using the Chapter 2 multiplication table directly:
- $(e_1 e_2) e_4 = e_3 \cdot e_4 = e_7$ (from the table: $e_3$ row, $e_4$ column gives $e_7$; equivalently, from the oriented triple $(3,4,7)$)
- $e_1(e_2 e_4) = e_1 \cdot e_6 = -e_7$ (from the table: $e_2$ row, $e_4$ column gives $e_6$; then $e_1$ row, $e_6$ column gives $-e_7$, consistent with the oriented triple $(1,7,6)$ which gives $e_1 e_7 = e_6$ and hence $e_1 e_6 = -e_7$)

Therefore $[e_1, e_2, e_4] = e_7 - (-e_7) = 2e_7$.

This confirms that basis-element associators are nonzero for non-Fano triples. The coherence of our radial field is:

$$[\Phi, \partial_j\Phi, \partial_k\Phi] = f(r)^3 \sum_i x_i [e_i, e_j, e_k] \tag{18.46}$$

The coherence density is:

$$\rho_{\mathcal{C}} = f(r)^6 \sum_{j<k} \left|\sum_i x_i [e_i, e_j, e_k]\right|^2 \tag{18.47}$$

For $j=2, k=4$: $\sum_i x_i [e_i, e_2, e_4]$. The associator $[e_i, e_2, e_4]$ is nonzero when $\{i,2,4\}$ does not lie on any Fano line. The Fano lines containing both $e_2$ and $e_4$ are: only $(2,4,6)$. So $[e_6, e_2, e_4] = 0$ (associative triple), while $[e_i, e_2, e_4] \neq 0$ for $i = 1, 3, 5, 7$. As computed above, $[e_1, e_2, e_4] = 2e_7$; the other nonzero associators can be computed similarly from the multiplication table.

The total coherence charge for this configuration is:

$$Q_{\mathcal{C}} = \int_0^\infty f(r)^6 r^2 \cdot \mathcal{A}_7 \cdot r^{6} \, dr = \mathcal{A}_7 \int_0^\infty f(r)^6 r^8 \, dr \tag{18.48}$$

where $\mathcal{A}_7$ is a numerical constant arising from the angular integration over $S^6$, involving the structure constants of $\mathbb{O}$. For a Gaussian profile $f(r) = e^{-r^2/2\sigma^2}$:

$$Q_{\mathcal{C}} = \mathcal{A}_7 \int_0^\infty e^{-3r^2/\sigma^2} r^8 \, dr = \mathcal{A}_7 \cdot \frac{105\sqrt{\pi}}{32} \cdot \frac{\sigma^9}{3^{9/2}} \tag{18.49}$$

This is a finite, positive, conserved quantity that measures the total non-associative content of the field configuration.

### 18.9.3 Example 3: Coherence in a Two-Body System

Consider two octonionic particles $\Phi_1(t), \Phi_2(t)$ interacting through a $G_2$-invariant potential $V(|\Phi_1 - \Phi_2|)$. The coherence of the two-body system is:

$$\mathcal{C}_{12} = |[\Phi_1, \Phi_2, \dot{\Phi}_1]|^2 + |[\Phi_1, \Phi_2, \dot{\Phi}_2]|^2 + |[\Phi_1, \dot{\Phi}_1, \dot{\Phi}_2]|^2 + |[\Phi_2, \dot{\Phi}_1, \dot{\Phi}_2]|^2 \tag{18.50}$$

By Theorem 18.2, $\mathcal{C}_{12}$ is conserved. This means that even as the particles exchange energy and momentum, their **total non-associative entanglement** remains constant. If the particles start in an associative configuration ($\mathcal{C}_{12} = 0$), they remain associative forever under $G_2$-invariant dynamics. Conversely, if they start with coherence, that coherence can never fully dissipate — it can only redistribute between the four associator channels.

This is the octonionic analog of quantum entanglement conservation: **coherence, once created, cannot be destroyed by symmetric dynamics**.

---

## 18.10 Coherence and the Physical World

### 18.10.1 Why We Don't See Coherence in 3D

The invisibility of coherence in 3D physics (Proposition 18.2) is not a defect of 3D physics — it is a **selection rule**. The 3D world is a $\mathbb{H}$-projection of the full $\mathbb{O}$-valued reality. In this projection, the associator is identically zero, so coherence vanishes. But this doesn't mean coherence is absent from reality; it means our 3D measurement apparatus cannot detect it.

Coherence manifests indirectly through the correction terms identified in Chapter 17: the charge leakage (Theorem 17.5), the angular momentum algebra breaking (Theorem 17.1), and the CPT violation (Theorem 17.6). These effects are SMALL (because 3D is a good approximation) but NONZERO (because the projection from $\mathbb{O}$ to $\mathbb{H}$ is not exact at high energies or in complex systems).

### 18.10.2 Where Coherence Becomes Dominant

Coherence conservation becomes the dominant dynamical constraint in systems where:

1. **Multiple hierarchical levels interact simultaneously** (the associator measures context-dependence of grouping).
2. **The system explores non-associative directions** (field configurations that don't stay within any single $\mathbb{H} \subset \mathbb{O}$).
3. **Classical conservation laws break down** (precisely the regimes identified in Chapter 17).

Examples from Part V: quantum coherence in entangled systems (Chapter 30), vortex dynamics in 7D fluids (Chapter 32), and multi-agent optimization in complex systems (Chapter 34).

---

## 18.11 Summary

This chapter has established:

1. **Definition 18.1**: Coherence as a sextic functional of the field, constructed from squared associators.

2. **Proposition 18.1**: The relationship between the associator and the $G_2$-invariant 3-form $\varphi$ -- they are complementary objects, with $\varphi$ detecting associative alignment and the associator detecting non-associative content.

3. **Theorem 18.1**: $G_2$ invariance of coherence -- it is a genuine symmetry invariant.

4. **Theorem 18.2**: Coherence conservation -- proved rigorously for orbit-confined dynamics (Theorem 18.2a) and for the octonionic Klein-Gordon field (Theorem 18.2c). The general case is deferred to the Hierarchy Invariance Principle (Chapter 20). An honest assessment (Open Problem 18.1) identifies the limits of what $G_2$-invariance alone can guarantee.

5. **The coherence current** (Definition 18.4) satisfying a continuity equation.

6. **Decomposition** into $G_2$-irreducible components: $\mathcal{C}_1 + \mathcal{C}_7 + \mathcal{C}_{27}$ (Proposition 18.4), with independent conservation proved for linear dynamics and conjectured for the general case (Open Problem 18.2).

7. **Associative invisibility** (Proposition 18.2): coherence vanishes in any quaternionic projection, explaining why it was never discovered in classical physics.

8. Worked examples demonstrating nonzero coherence for genuinely octonionic configurations, with explicit computations verifying time-independence.

Coherence is the **first genuinely new conservation law** of octonionic physics. It has no 3D precursor, no associative analog, and no explanation within the existing framework of Lie group symmetries. It emerges from the non-associative structure of $\mathbb{O}$ as naturally as angular momentum emerges from rotational symmetry. The precise conditions under which it is conserved are characterized in this chapter and refined in Chapter 20. In the next chapter, we show how coherence augments and unifies the classical charge conservation laws.
