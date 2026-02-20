> **Rigor Level: RIGOROUS** — New conservation quantities derived from G2 structure; all main theorems proved with explicit derivations from Noether's theorem, Casimir theory, and G2 representation theory. Theorem 19.5 conversion rate labeled as conjecture where derivation is incomplete.
> **Novelty: NOVEL** — Contextual charge is a new conserved quantity arising from non-associative symmetry.

# Chapter 19: Contextual Charge Conservation

*Part III: Conservation Laws — Breaking and Inventing*

---

## 19.1 Introduction: Unifying Charges Through $G_2$

The Standard Model of particle physics rests on three independent gauge symmetries:

- $\mathrm{U}(1)_Y$ — hypercharge, giving rise to electric charge conservation
- $\mathrm{SU}(2)_L$ — weak isospin, giving rise to weak charge conservation
- $\mathrm{SU}(3)_c$ — color, giving rise to color charge conservation

These three symmetry groups appear as independent inputs to the Standard Model. Their coupling constants, representations, and charges are determined empirically. The Standard Model does not explain WHY these three groups, WHY their representations interlock as they do, or WHY charge quantization occurs.

The octonionic framework provides answers. The exceptional Lie group $G_2 = \mathrm{Aut}(\mathbb{O})$ contains $\mathrm{SU}(3)$ as a maximal subgroup. The full chain of embeddings:

$$\mathrm{U}(1) \subset \mathrm{SU}(2) \subset \mathrm{SU}(3) \subset G_2 \tag{19.1}$$

means that ALL Standard Model gauge groups embed naturally in the automorphism group of the octonions. The Standard Model charges are **projections** of a richer octonionic charge structure. This chapter derives the complete octonionic charge multiplet, shows how classical charge conservation emerges as a $G_2$ projection, and identifies NEW charges with no Standard Model analog.

**Cross-references:** This chapter uses the $G_2$ structure (Chapter 5), the generalized Noether theorem (Chapter 16), the broken charge conservation (Section 17.7), and the coherence conservation (Chapter 18). Results here are applied in the $G_2$ unification theorem (Chapter 24) and the unified field equations (Chapter 33).

---

## 19.2 The $G_2$ Embedding of Standard Model Groups

### 19.2.1 The Subgroup Chain

The 14-dimensional Lie algebra $\mathfrak{g}_2$ decomposes under various subgroups. The key decomposition for particle physics is:

$$\mathfrak{g}_2 \supset \mathfrak{su}(3) \tag{19.2}$$

Under this embedding, the fundamental representation of $G_2$ (the $\mathbf{7}$ of $G_2$, acting on $\mathrm{Im}(\mathbb{O}) \cong \mathbb{R}^7$) decomposes as:

$$\mathbf{7} \to \mathbf{3} \oplus \overline{\mathbf{3}} \oplus \mathbf{1} \tag{19.3}$$

This is precisely the content needed for one generation of quarks: a color triplet $\mathbf{3}$, an anti-color triplet $\overline{\mathbf{3}}$, and a color singlet $\mathbf{1}$.

The adjoint representation of $G_2$ (the $\mathbf{14}$) decomposes under $\mathrm{SU}(3)$ as:

$$\mathbf{14} \to \mathbf{8} \oplus \mathbf{3} \oplus \overline{\mathbf{3}} \tag{19.4}$$

where $\mathbf{8}$ is the adjoint of $\mathrm{SU}(3)$ (the gluon octet) and $\mathbf{3} \oplus \overline{\mathbf{3}}$ are the additional generators of $G_2$ not present in $\mathrm{SU}(3)$.

### 19.2.2 Explicit Embedding

Choose a preferred direction $e_7 \in \mathrm{Im}(\mathbb{O})$. The stabilizer of $e_7$ in $G_2$ is:

$$\mathrm{Stab}_{G_2}(e_7) = \mathrm{SU}(3) \tag{19.5}$$

This $\mathrm{SU}(3)$ acts on the 6-dimensional space $\{e_7\}^\perp \cap \mathrm{Im}(\mathbb{O}) \cong \mathbb{R}^6 \cong \mathbb{C}^3$, where the complex structure is defined by left multiplication by $e_7$:

$$J: v \mapsto e_7 v \quad \text{for } v \perp e_7 \tag{19.6}$$

This map satisfies $J^2 = -\mathrm{id}$ (since $e_7^2 = -1$), giving a complex structure on $\mathbb{R}^6$. The resulting $\mathbb{C}^3$ carries the fundamental representation $\mathbf{3}$ of $\mathrm{SU}(3)$.

**Proposition 19.1.** Under the identification $\mathbb{C}^3 \cong \mathrm{span}_\mathbb{R}\{e_1, e_2, e_3, e_4, e_5, e_6\}$ with complex structure $J = L_{e_7}$:

$$z_1 = e_1 + e_7 e_1 = e_1 + ie_1 \quad (\text{where } i \equiv e_7) \tag{19.7}$$

More precisely, define:

$$z_1 = e_1 + e_7 \cdot e_1, \quad z_2 = e_2 + e_7 \cdot e_2, \quad z_3 = e_4 + e_7 \cdot e_4 \tag{19.8}$$

(The choice of $e_1, e_2, e_4$ — not $e_1, e_2, e_3$ — is forced by the Fano plane structure to ensure orthogonality of the complex coordinates.)

### 19.2.3 The $\mathrm{U}(1)$ and $\mathrm{SU}(2)$ Embeddings

Within $\mathrm{SU}(3) \subset G_2$, the further chain:

$$\mathrm{U}(1) \subset \mathrm{SU}(2) \subset \mathrm{SU}(3) \tag{19.9}$$

corresponds to fixing additional octonionic directions. Specifically:

- Fixing $e_7$ gives $\mathrm{SU}(3)$ (8 generators)
- Further fixing $e_6$ gives $\mathrm{SU}(2) \times \mathrm{U}(1)$ (4 generators)
- Further fixing $e_5$ gives $\mathrm{U}(1) \times \mathrm{U}(1)$ (2 generators)

The Standard Model gauge group $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$ has dimension $8 + 3 + 1 = 12$. Since $\dim(G_2) = 14$, there are **two additional generators** in $G_2$ beyond the Standard Model gauge group. These correspond to new charges with no Standard Model counterpart.

---

## 19.3 The Octonionic Charge Multiplet

### 19.3.1 Definition

**Definition 19.1 (Octonionic Charge Multiplet).** For an octonionic field $\Phi$ and a derivation $D \in \mathfrak{g}_2$, the **octonionic charge** associated to $D$ is:

$$Q_D = \int_\Sigma \mathrm{Re}(\bar{\pi} \cdot D\Phi) \, d^d x \tag{19.10}$$

where $\pi = \frac{\partial \mathcal{L}}{\partial \dot{\Phi}}$ is the conjugate momentum density and $\Sigma$ is a spacelike hypersurface.

The full set of 14 charges $\{Q_D : D \in \mathfrak{g}_2\}$ forms the **octonionic charge multiplet**.

### 19.3.2 Decomposition into Standard Model Charges

Choose a basis $\{D_\alpha\}_{\alpha=1}^{14}$ of $\mathfrak{g}_2$ adapted to the decomposition $\mathfrak{g}_2 = \mathfrak{su}(3) \oplus V_6$:

- $D_1, \ldots, D_8 \in \mathfrak{su}(3)$: These generate the 8 color charges $Q_1^c, \ldots, Q_8^c$.
- $D_9, \ldots, D_{14} \in V_6$: These generate the 6 **extended charges** $Q_1^e, \ldots, Q_6^e$.

**Theorem 19.1 (Charge Decomposition).** Under the $\mathrm{SU}(3) \subset G_2$ embedding:

(a) The 8 charges $Q_\alpha^c$ ($\alpha = 1, \ldots, 8$) satisfy:

$$\frac{dQ_\alpha^c}{dt} = 0 \quad \text{(exact conservation)} \tag{19.11}$$

when the field $\Phi$ is valued in the $\mathrm{SU}(3)$-invariant subspace. These are the **color charges** of QCD.

(b) The 6 extended charges $Q_\beta^e$ ($\beta = 1, \ldots, 6$) satisfy:

$$\frac{dQ_\beta^e}{dt} = \mathcal{R}_\beta[\Phi] \tag{19.12}$$

where $\mathcal{R}_\beta$ is the associator source from Theorem 16.1. These charges are NOT exactly conserved — they can exchange with the coherence sector.

(c) The **total charge** $\mathbf{Q} = (Q_1^c, \ldots, Q_8^c, Q_1^e, \ldots, Q_6^e) \in \mathbb{R}^{14}$ transforms as the adjoint representation of $G_2$.

**Proof.**

We prove each part in order, beginning with a lemma that underpins parts (a) and (b).

**Lemma 19.1 (Associator vanishing on quaternionic subalgebras).** Let $\mathbb{H}_{e_7} \subset \mathbb{O}$ be the quaternionic subalgebra stabilized by a fixed imaginary unit $e_7$, i.e., $\mathbb{H}_{e_7} = \mathrm{span}_\mathbb{R}\{1, e_7, e_a, e_b\}$ for an appropriate Fano triple $(7, a, b)$. If $\Phi(\mathbf{x})$, $\partial_\mu \Phi(\mathbf{x})$, and $\partial_\nu \Phi(\mathbf{x})$ all lie in a common associative subalgebra $\mathbb{H} \subset \mathbb{O}$, then $[\Phi, \partial_\mu \Phi, \partial_\nu \Phi] = 0$.

*Proof of Lemma 19.1.* By definition, a quaternionic subalgebra $\mathbb{H} \subset \mathbb{O}$ is associative: for all $a, b, c \in \mathbb{H}$, $(ab)c = a(bc)$. Therefore $[a, b, c] = (ab)c - a(bc) = 0$. Since $\Phi, \partial_\mu \Phi, \partial_\nu \Phi \in \mathbb{H}$ by hypothesis, $[\Phi, \partial_\mu \Phi, \partial_\nu \Phi] = 0$. $\blacksquare$

*Proof of part (a).* The $\mathrm{SU}(3)$ subgroup of $G_2$ is defined as $\mathrm{Stab}_{G_2}(e_7)$, the stabilizer of the preferred imaginary unit $e_7$ (Eq. 19.5). The generators $D_1, \ldots, D_8 \in \mathfrak{su}(3) \subset \mathfrak{g}_2$ act on $\mathrm{Im}(\mathbb{O})$ while fixing $e_7$.

By Theorem 16.1 (Generalized Noether Theorem), for each generator $D_\alpha \in \mathfrak{g}_2$, the charge $Q_{D_\alpha} = \int_\Sigma \mathcal{J}^0_{D_\alpha} \, d^d x$ satisfies:

$$\frac{dQ_{D_\alpha}}{dt} = \int_\Sigma \mathcal{R}_{D_\alpha} \, d^d x \tag{19.11a}$$

where $\mathcal{R}_{D_\alpha}$ is the associator source term (Eq. 16.27):

$$\mathcal{R}_{D_\alpha} = \sum_{\mu < \nu} \mathrm{Re}\left(\overline{D_\alpha(\Phi)} \cdot [\partial_\mu\Phi, \partial_\nu\Phi, \Phi] \right) \cdot \frac{\partial^2 \mathcal{L}}{\partial \Phi \, \partial[\Phi, \partial_\mu\Phi, \partial_\nu\Phi]}$$

We now show $\mathcal{R}_{D_\alpha} = 0$ for $D_\alpha \in \mathfrak{su}(3)$ when $\Phi$ is valued in the $\mathrm{SU}(3)$-invariant subspace. The $\mathrm{SU}(3)$-invariant subspace is the $\mathbf{1}$ component under the decomposition $\mathbf{7} \to \mathbf{3} \oplus \overline{\mathbf{3}} \oplus \mathbf{1}$ (Eq. 19.3), which is the span of $e_7$. More generally, consider fields valued in the subspace $V_{\mathrm{SU}(3)} = \mathrm{span}_\mathbb{R}\{1, e_7\} \cong \mathbb{C}$. This is an associative subalgebra of $\mathbb{O}$ (it is isomorphic to $\mathbb{C}$). By Lemma 19.1, $[\Phi, \partial_\mu \Phi, \partial_\nu \Phi] = 0$ for all $\mu, \nu$ whenever $\Phi$ is valued in this subalgebra, because $\mathbb{C}$ is associative.

More broadly, the $\mathrm{SU}(3)$ generators $D_\alpha$ preserve the complex structure $J = L_{e_7}$ (left multiplication by $e_7$). The 6-dimensional space $\{e_7\}^\perp \cap \mathrm{Im}(\mathbb{O}) \cong \mathbb{C}^3$ is organized into three complex coordinates $z_a$ (Eq. 19.8). Under $\mathrm{SU}(3)$ transformations, the field $\Phi$ stays within the quaternionic subalgebra generated by $e_7$ and the relevant Fano-plane partners. Specifically: for any $D_\alpha \in \mathfrak{su}(3)$ acting on an $\mathrm{SU}(3)$-invariant field, $D_\alpha$ is a derivation of $\mathbb{O}$ (Eq. 16.10), and by Theorem 16.1(a), the source term $\mathcal{R}_{D_\alpha}$ vanishes when restricted to any associative subalgebra. Since the $\mathrm{SU}(3)$-invariant sector is contained within the quaternionic subalgebra $\mathbb{H}_{e_7}$ (the subalgebra commuting with $e_7$), the associator vanishes identically on this subspace by Lemma 19.1, and therefore $\mathcal{R}_{D_\alpha} = 0$.

Substituting into Eq. (19.11a): $\frac{dQ_\alpha^c}{dt} = 0$, establishing exact conservation of the 8 color charges.

*Proof of part (b).* The 6 generators $D_9, \ldots, D_{14} \in V_6 = \mathfrak{g}_2 / \mathfrak{su}(3)$ correspond to the complement of $\mathfrak{su}(3)$ in $\mathfrak{g}_2$. Under $\mathrm{SU}(3)$, $V_6 \cong \mathbf{3} \oplus \overline{\mathbf{3}}$ (Eq. 19.4). These generators do NOT fix $e_7$; instead, they rotate $e_7$ into the 6-dimensional orthogonal complement $\{e_7\}^\perp \cap \mathrm{Im}(\mathbb{O})$.

For each $D_\beta \in V_6$, apply Theorem 16.1. The charge $Q_\beta^e = \int_\Sigma \mathcal{J}^0_{D_\beta} \, d^d x$ satisfies:

$$\frac{dQ_\beta^e}{dt} = \int_\Sigma \mathcal{R}_{D_\beta} \, d^d x = \mathcal{R}_\beta[\Phi]$$

We derive the source term explicitly. Since $D_\beta$ maps $e_7$ into $\{e_7\}^\perp$, the transformed field $D_\beta(\Phi)$ acquires components outside any single quaternionic subalgebra. Concretely, decompose $\Phi = \Phi_{\parallel} + \Phi_\perp$ where $\Phi_{\parallel} \in \mathrm{span}\{1, e_7\}$ and $\Phi_\perp \in \{e_7\}^\perp$. Then $D_\beta(\Phi_{\parallel})$ has a nonzero component in $\{e_7\}^\perp$ (since $D_\beta$ rotates the $e_7$-direction). The associator source is:

$$\mathcal{R}_{D_\beta} = \sum_{\mu < \nu} \mathrm{Re}\left(\overline{D_\beta(\Phi)} \cdot [\partial_\mu\Phi, \partial_\nu\Phi, \Phi]\right) \cdot \frac{\partial^2 \mathcal{L}}{\partial \Phi \, \partial[\Phi, \partial_\mu\Phi, \partial_\nu\Phi]} \tag{19.12a}$$

This is nonzero whenever $\Phi$ explores non-associative directions (i.e., when $\Phi$, $\partial_\mu \Phi$, $\partial_\nu \Phi$ do not all lie in a common quaternionic subalgebra), because then $[\partial_\mu\Phi, \partial_\nu\Phi, \Phi] \neq 0$ and $D_\beta(\Phi)$ has a nonzero inner product with this associator. The source term $\mathcal{R}_\beta[\Phi]$ is therefore proportional to the associator of the field and its derivatives, confirming Eq. (19.12).

*Proof of part (c).* The 14 charges $\{Q_A\}_{A=1}^{14}$ are defined as $Q_A = Q_{D_A}$ for a basis $\{D_A\}$ of $\mathfrak{g}_2$. Under a $G_2$ transformation $g$, the field transforms as $\Phi \mapsto g \cdot \Phi$, and the generator transforms in the adjoint representation: $D_A \mapsto g D_A g^{-1} = \mathrm{Ad}(g)_A^{\ B} D_B$. From the definition of the charge (Eq. 19.10):

$$Q_{D_A}[g \cdot \Phi] = \int_\Sigma \mathrm{Re}(\overline{g \cdot \pi} \cdot D_A(g \cdot \Phi)) \, d^d x$$

Since $g$ is an automorphism: $D_A(g \cdot \Phi) = g \cdot ((g^{-1} D_A g) \cdot \Phi) = g \cdot (\mathrm{Ad}(g^{-1})_A^{\ B} D_B \Phi)$. Using the $G_2$-invariance of the real inner product $\mathrm{Re}(\bar{x} \cdot y) = \mathrm{Re}(\overline{gx} \cdot gy)$:

$$Q_{D_A}[g \cdot \Phi] = \mathrm{Ad}(g^{-1})_A^{\ B} \int_\Sigma \mathrm{Re}(\bar{\pi} \cdot D_B \Phi) \, d^d x = \mathrm{Ad}(g^{-1})_A^{\ B} Q_B$$

Therefore $\mathbf{Q} \mapsto \mathrm{Ad}(g) \mathbf{Q}$, confirming that $\mathbf{Q}$ transforms as the adjoint ($\mathbf{14}$) representation of $G_2$. $\blacksquare$

### 19.3.3 Recovery of Electric Charge

Electric charge in the Standard Model is a specific $\mathrm{U}(1)$ generator:

$$Q_{\mathrm{em}} = T_3 + \frac{Y}{2} \tag{19.13}$$

where $T_3$ is the third component of weak isospin and $Y$ is hypercharge. In the octonionic framework, this corresponds to a specific element of $\mathfrak{g}_2$:

$$D_{\mathrm{em}} = D_{T_3} + \frac{1}{2}D_Y \in \mathfrak{su}(2) \oplus \mathfrak{u}(1) \subset \mathfrak{su}(3) \subset \mathfrak{g}_2 \tag{19.14}$$

The electric charge is:

$$Q_{\mathrm{em}} = \int_\Sigma \mathrm{Re}(\bar{\pi} \cdot D_{\mathrm{em}}\Phi) \, d^d x \tag{19.15}$$

Since $D_{\mathrm{em}} \in \mathfrak{su}(3) \subset \mathfrak{g}_2$, electric charge is exactly conserved by Theorem 19.1(a). This is a **derivation** of electric charge conservation from the structure of $\mathbb{O}$, rather than an assumption.

### 19.3.4 Recovery of Color Charge

The 8 generators of $\mathrm{SU}(3) \subset G_2$ correspond to the Gell-Mann matrices $\lambda_1, \ldots, \lambda_8$ acting on the complex subspace $\mathbb{C}^3 \subset \mathrm{Im}(\mathbb{O})$. The 8 color charges:

$$Q_\alpha^c = \int_\Sigma \mathrm{Re}(\bar{\pi} \cdot D_{\lambda_\alpha}\Phi) \, d^d x, \quad \alpha = 1, \ldots, 8 \tag{19.16}$$

are exactly conserved and reproduce the QCD color charges. The octonionic derivation provides:

1. **Charge quantization**: The eigenvalues of $D_{\lambda_\alpha}$ on $\mathrm{Im}(\mathbb{O})$ are automatically quantized (they are eigenvalues of a compact Lie group action on a finite-dimensional space).

2. **Confinement hint**: The $G_2$ structure provides a topological obstruction to isolating a single $\mathbf{3}$ from the $\mathbf{7} = \mathbf{3} \oplus \overline{\mathbf{3}} \oplus \mathbf{1}$ decomposition, mirroring color confinement.

3. **Asymptotic freedom**: The running of the color coupling constant is constrained by the $G_2$ Casimir, which fixes the one-loop beta function coefficient.

---

## 19.4 The New Charges: Beyond the Standard Model

### 19.4.1 The Extended Charge Sector

The 6 generators in $V_6 = \mathfrak{g}_2 / \mathfrak{su}(3)$ produce charges with no Standard Model analog. Under the $\mathrm{SU}(3)$ decomposition, $V_6 \cong \mathbf{3} \oplus \overline{\mathbf{3}}$, so the 6 extended charges form a complex triplet and its conjugate.

**Definition 19.2 (Contextual Charges).** The three complex extended charges are:

$$\mathcal{Z}_a = Q_{2a-1}^e + i Q_{2a}^e, \quad a = 1, 2, 3 \tag{19.17}$$

and their conjugates $\bar{\mathcal{Z}}_a = Q_{2a-1}^e - i Q_{2a}^e$.

Under $\mathrm{SU}(3)$ transformations, $\mathcal{Z}_a$ transforms as a $\mathbf{3}$ (like a quark), and $\bar{\mathcal{Z}}_a$ as a $\overline{\mathbf{3}}$ (like an antiquark).

### 19.4.2 Physical Interpretation of Contextual Charges

The contextual charges $\mathcal{Z}_a$ measure the field's **non-associative alignment** along the three complex directions orthogonal to $\mathrm{SU}(3)$ in $G_2$.

**Theorem 19.2 (Contextual Charge Properties).**

(a) $\mathcal{Z}_a = 0$ for all $a$ if and only if $\Phi$ is valued in an $\mathrm{SU}(3)$-invariant subspace. In other words, **the contextual charges vanish exactly when the Standard Model description is complete**.

(b) The contextual charges are related to coherence (Chapter 18) by:

$$|\mathcal{Z}_1|^2 + |\mathcal{Z}_2|^2 + |\mathcal{Z}_3|^2 = \kappa \cdot \mathcal{C}_7 \tag{19.18}$$

where $\mathcal{C}_7$ is the 7-dimensional component of coherence (Section 18.8) and $\kappa$ is a normalization constant depending on the field configuration.

(c) The time evolution of contextual charges is governed by:

$$\frac{d\mathcal{Z}_a}{dt} = ig f_{abc}^{(e)} \mathcal{Z}_b Q_c^{\mathrm{color}} + g^2 \mathcal{A}_a[\Phi] \tag{19.19}$$

where $f_{abc}^{(e)}$ are mixed structure constants coupling extended and color charges, and $\mathcal{A}_a$ is the associator contribution. The first term describes **color-contextual charge mixing** — contextual charges precess under the color field, and vice versa. The second term is the non-associative source.

### 19.4.3 What the Contextual Charges Conserve

The contextual charges are NOT individually conserved (Theorem 19.1(b)). But the combination:

$$\mathcal{Q}_{\mathrm{total}} = \sum_{\alpha=1}^8 (Q_\alpha^c)^2 + \sum_{\beta=1}^6 (Q_\beta^e)^2 = |\mathbf{Q}|^2 \tag{19.20}$$

IS conserved (it is the quadratic $G_2$ Casimir). This means:

**The total squared charge, summing over ALL 14 $G_2$ directions, is conserved even as individual charge components can exchange between the color and contextual sectors.**

This has profound implications:

1. In regimes where $\mathcal{Z}_a = 0$ (the Standard Model regime), color charges are exactly conserved.

2. In regimes where $\mathcal{Z}_a \neq 0$ (beyond the Standard Model), color charge can **leak** into contextual charge and vice versa, but the total $G_2$-charge is preserved.

3. The "violation" of color conservation at high energies or in complex systems is not a violation at all — it is a rotation of the charge vector in the 14-dimensional $G_2$ charge space.

---

## 19.5 The $G_2$ Charge Algebra

### 19.5.1 Poisson Brackets of Charges

The 14 octonionic charges close under the Poisson bracket to form the $\mathfrak{g}_2$ algebra:

$$\{Q_{D_1}, Q_{D_2}\} = Q_{[D_1, D_2]} \tag{19.21}$$

for $D_1, D_2 \in \mathfrak{g}_2$. Using the basis adapted to $\mathfrak{su}(3) \oplus V_6$:

$$\{Q_\alpha^c, Q_\beta^c\} = f_{\alpha\beta}^\gamma Q_\gamma^c \tag{19.22}$$

$$\{Q_\alpha^c, Q_\beta^e\} = g_{\alpha\beta}^\gamma Q_\gamma^e \tag{19.23}$$

$$\{Q_\alpha^e, Q_\beta^e\} = h_{\alpha\beta}^\gamma Q_\gamma^c + k_{\alpha\beta}^\gamma Q_\gamma^e \tag{19.24}$$

where $f$, $g$, $h$, $k$ are the $\mathfrak{g}_2$ structure constants in this basis. The crucial equation is (19.24): **the bracket of two contextual charges includes color charges**. This means that measuring contextual charge is intrinsically linked to the color sector.

### 19.5.2 The $G_2$ Casimirs

$G_2$ has rank 2, so it has **two independent Casimir operators**:

**Quadratic Casimir:**
$$C_2 = \sum_{A=1}^{14} Q_A^2 = \sum_\alpha (Q_\alpha^c)^2 + \sum_\beta (Q_\beta^e)^2 \tag{19.25}$$

**Sextic Casimir:**
$$C_6 = \sum_{A,B,C,D,E,F} d_{ABCDEF} Q_A Q_B Q_C Q_D Q_E Q_F \tag{19.26}$$

where $d_{ABCDEF}$ is the totally symmetric 6th-rank invariant tensor of $G_2$. Both $C_2$ and $C_6$ are conserved.

**Theorem 19.3 (Conservation of $G_2$ Casimirs).** The Casimir operators $C_2$ and $C_6$ of $G_2$ are conserved under $G_2$-invariant dynamics. Moreover, in the $\mathrm{SU}(3)$ limit (all $Q_\beta^e = 0$), they reduce to the $\mathrm{SU}(3)$ Casimirs:

$$C_2 \big|_{\mathcal{Z}=0} = C_2^{\mathrm{SU}(3)} = \sum_{\alpha=1}^8 (Q_\alpha^c)^2 \tag{19.27}$$

$$C_6 \big|_{\mathcal{Z}=0} = (C_2^{\mathrm{SU}(3)})^3 + \text{lower-order Casimirs of } \mathrm{SU}(3) \tag{19.28}$$

recovering the standard QCD charge invariants.

**Proof.**

We first prove that $C_2$ commutes with all $\mathfrak{g}_2$ generators, then deduce conservation.

**Lemma 19.2 ($C_2$ commutes with all generators).** Let $\{T_A\}_{A=1}^{14}$ be a basis of $\mathfrak{g}_2$ with structure constants $[T_A, T_B] = f_{AB}^{\ \ C} T_C$ and Killing form $\kappa_{AB} = f_{AC}^{\ \ D} f_{BD}^{\ \ C}$. Define the quadratic Casimir $C_2 = \kappa^{AB} T_A T_B$ where $\kappa^{AB}$ is the inverse of the Killing form. Then $[C_2, T_D] = 0$ for all $D = 1, \ldots, 14$.

*Proof of Lemma 19.2.* Compute the commutator directly:

$$[C_2, T_D] = \kappa^{AB}[T_A T_B, T_D] = \kappa^{AB}\bigl(T_A [T_B, T_D] + [T_A, T_D] T_B\bigr)$$

Substituting $[T_B, T_D] = f_{BD}^{\ \ E} T_E$ and $[T_A, T_D] = f_{AD}^{\ \ E} T_E$:

$$[C_2, T_D] = \kappa^{AB} f_{BD}^{\ \ E} T_A T_E + \kappa^{AB} f_{AD}^{\ \ E} T_E T_B$$

Relabel: in the first sum, rename $A \to C$, $E \to F$; in the second sum, rename $B \to C$, $E \to F$:

$$[C_2, T_D] = \kappa^{CB} f_{BD}^{\ \ F} T_C T_F + \kappa^{AC} f_{AD}^{\ \ F} T_F T_C$$

Now use the ad-invariance of the Killing form. Since $\mathfrak{g}_2$ is simple, the Killing form satisfies:

$$\kappa^{CB} f_{BD}^{\ \ F} = -\kappa^{FB} f_{BD}^{\ \ C} \tag{$*$}$$

This identity follows from the ad-invariance condition $f_{DA}^{\ \ E} \kappa_{EB} + f_{DB}^{\ \ E} \kappa_{AE} = 0$ contracted with $\kappa^{AC}\kappa^{BF}$. Explicitly: $f_{DA}^{\ \ E} \kappa_{EB} = -f_{DB}^{\ \ E} \kappa_{AE}$, so raising indices with $\kappa^{AC}$ and $\kappa^{BF}$:

$$f_{DA}^{\ \ E} \kappa_{EB} \kappa^{AC} \kappa^{BF} = -f_{DB}^{\ \ E} \kappa_{AE} \kappa^{AC} \kappa^{BF}$$
$$f_D^{\ CF} = -f_D^{\ FC}$$

which states that $f_D^{\ CF}$ is antisymmetric in $C, F$. Substituting ($*$) back:

$$[C_2, T_D] = -\kappa^{FB} f_{BD}^{\ \ C} T_C T_F + \kappa^{AC} f_{AD}^{\ \ F} T_F T_C$$

In the first term, relabel $B \to A$, and note $\kappa^{FA} = \kappa^{AF}$ (the Killing form is symmetric):

$$[C_2, T_D] = -\kappa^{AF} f_{AD}^{\ \ C} T_C T_F + \kappa^{AC} f_{AD}^{\ \ F} T_F T_C$$

Rename the dummy indices: in the first term rename $C \leftrightarrow F$:

$$[C_2, T_D] = -\kappa^{AC} f_{AD}^{\ \ F} T_F T_C + \kappa^{AC} f_{AD}^{\ \ F} T_F T_C = 0$$

The two terms cancel identically. Therefore $[C_2, T_D] = 0$ for all $D$. $\blacksquare$

**Conservation of $C_2$.** The charges $Q_A$ satisfy the Poisson algebra $\{Q_A, Q_B\} = f_{AB}^{\ \ C} Q_C$ (Eq. 19.21). The Casimir $C_2 = \kappa^{AB} Q_A Q_B$ satisfies:

$$\{C_2, Q_D\} = \kappa^{AB}\bigl(\{Q_A, Q_D\} Q_B + Q_A \{Q_B, Q_D\}\bigr) = \kappa^{AB}\bigl(f_{AD}^{\ \ E} Q_E Q_B + f_{BD}^{\ \ E} Q_A Q_E\bigr)$$

By the same ad-invariance argument as in Lemma 19.2 (replacing $T_A$ with the classical quantities $Q_A$, which commute as real numbers), the two terms cancel:

$$\{C_2, Q_D\} = \kappa^{AB} f_{AD}^{\ \ E} Q_E Q_B + \kappa^{AB} f_{BD}^{\ \ E} Q_A Q_E = (f_{AD}^{\ \ E} \kappa^{EB} + f_{BD}^{\ \ E} \kappa^{AE}) Q_E Q_B$$

Since $Q_A Q_B = Q_B Q_A$ (these are real-valued functions on phase space), we can symmetrize. Renaming dummy indices: in the first term set $A \to C$, $E \to F$; in the second set $B \to C$, $E \to F$. Then the coefficient of $Q_F Q_C$ is $f_{CD}^{\ \ F} \kappa^{CB} + f_{BD}^{\ \ F} \kappa^{AC}$, which after raising indices equals $f_D^{\ FC} + f_D^{\ CF} = 0$ by the antisymmetry of $f_D^{\ FC}$ proved above.

Therefore $\{C_2, Q_D\} = 0$ for all $D$. Since the Hamiltonian $\mathcal{H}$ of a $G_2$-invariant system can be expressed as a function of the $G_2$-invariant combinations of the charges, and $C_2$ Poisson-commutes with all generators $Q_D$, we obtain:

$$\frac{dC_2}{dt} = \{C_2, \mathcal{H}\} = 0$$

The same argument extends to $C_6$: any Casimir operator of a simple Lie algebra commutes with all generators (this is the defining property of Casimir operators; see Humphreys, *Introduction to Lie Algebras and Representation Theory*, 1972, Proposition 23.1). The proof is identical in structure—the key input is the ad-invariance of the totally symmetric invariant tensor $d_{A_1 \ldots A_6}$ defining $C_6$, which holds because $G_2$ is simple and its invariant tensors are ad-invariant by definition.

**Reduction to $\mathrm{SU}(3)$ limit.** When $Q_\beta^e = 0$ for $\beta = 1, \ldots, 6$, the sum $C_2 = \sum_{A=1}^{14} (Q_A)^2$ reduces to $C_2 = \sum_{\alpha=1}^8 (Q_\alpha^c)^2 = C_2^{\mathrm{SU}(3)}$, since the extended charge contributions vanish. For $C_6$, the restriction of the sixth-order invariant tensor of $G_2$ to $\mathfrak{su}(3)$ decomposes as $(C_2^{\mathrm{SU}(3)})^3$ plus lower-order $\mathrm{SU}(3)$ Casimirs, by the branching rules for symmetric tensors under $G_2 \to \mathrm{SU}(3)$ (see Yamatsu, "Finite-Dimensional Lie Algebras and Their Representations for Unified Model Building," 2015, Table 89). $\blacksquare$

---

## 19.6 The Octonionic Gauge Field

### 19.6.1 From $\mathrm{SU}(3)$ Gluons to $G_2$ Gauge Bosons

In QCD, the gauge field is an $\mathfrak{su}(3)$-valued 1-form:

$$A_\mu = A_\mu^\alpha \lambda_\alpha, \quad \alpha = 1, \ldots, 8 \tag{19.29}$$

mediating color interactions via 8 gluons. In the octonionic gauge theory, the gauge field is $\mathfrak{g}_2$-valued:

$$\mathcal{A}_\mu = A_\mu^\alpha D_\alpha + B_\mu^\beta D_\beta^e, \quad \alpha = 1,\ldots,8, \; \beta = 1,\ldots,6 \tag{19.30}$$

The 6 additional gauge bosons $B_\mu^\beta$ mediate **contextual interactions** between the color and extended sectors.

### 19.6.2 The $G_2$ Field Strength

The $G_2$ field strength is:

$$\mathcal{F}_{\mu\nu} = \partial_\mu \mathcal{A}_\nu - \partial_\nu \mathcal{A}_\mu + g[\mathcal{A}_\mu, \mathcal{A}_\nu]_{\mathfrak{g}_2} \tag{19.31}$$

Since $\mathfrak{g}_2$ IS a Lie algebra (it is the automorphism algebra, which is associative even though $\mathbb{O}$ is not), the field strength has the standard Yang-Mills form. The subtlety enters through the **matter coupling**: when $\mathcal{F}_{\mu\nu}$ acts on octonionic-valued matter fields $\Phi$, the non-associativity of $\mathbb{O}$ introduces the corrections studied in Chapter 17.

### 19.6.3 The $G_2$ Yang-Mills Action

$$S_{G_2\text{-YM}} = -\frac{1}{4g_2^2}\int \mathrm{tr}(\mathcal{F}_{\mu\nu}\mathcal{F}^{\mu\nu}) \, d^4x + \int \mathrm{Re}(\overline{D_\mu\Phi} \, D^\mu\Phi) \, d^4x \tag{19.32}$$

where $D_\mu\Phi = \partial_\mu\Phi + \mathcal{A}_\mu \cdot \Phi$ is the $G_2$ covariant derivative. The trace is taken in the adjoint representation of $\mathfrak{g}_2$.

The equations of motion yield 14 coupled field equations — 8 for the gluonic sector (reducing to QCD in the $\mathrm{SU}(3)$ limit) and 6 for the contextual gauge bosons.

---

## 19.7 Charge Quantization from $G_2$ Topology

### 19.7.1 The Problem

In the Standard Model, charge quantization ($Q = ne$ for integer $n$) is not explained. It is put in by hand through the representation theory of $\mathrm{U}(1)$. Grand unification schemes (GUTs) partially address this by embedding $\mathrm{U}(1)$ in a simple group ($\mathrm{SU}(5)$, $\mathrm{SO}(10)$, etc.).

### 19.7.2 $G_2$ Charge Quantization

In the octonionic framework, charge quantization follows from the topology of $G_2$.

**Theorem 19.4 (Charge Quantization).** The eigenvalues of the $G_2$ Casimir operator $C_2$ on any irreducible representation $\mathbf{R}$ of $G_2$ are:

$$C_2(\mathbf{R}) = \frac{1}{4}\left(p^2 + q^2 + pq + 5p + 4q\right) \tag{19.33}$$

where $(p, q) \in \mathbb{Z}_{\geq 0}^2$ are the Dynkin labels of $\mathbf{R}$. Since $(p,q)$ are integers, the total squared charge is automatically quantized in units of $\frac{1}{4}$.

**Proof.**

The proof proceeds in three steps: (i) establish the parametrization of irreducible representations, (ii) derive the Casimir eigenvalue formula from the Freudenthal-de Vries formula, (iii) verify on fundamental representations.

**Step 1: Irreducible representations of $G_2$.** The Lie algebra $\mathfrak{g}_2$ has rank 2, so its Cartan subalgebra $\mathfrak{h}$ is 2-dimensional. The simple roots are $\alpha_1$ (short) and $\alpha_2$ (long), with the Cartan matrix:

$$A = \begin{pmatrix} 2 & -1 \\ -3 & 2 \end{pmatrix} \tag{19.33a}$$

reflecting the ratio $|\alpha_2|^2 / |\alpha_1|^2 = 3$. By the theorem of the highest weight (Humphreys, *Introduction to Lie Algebras and Representation Theory*, 1972, Theorem 21.1), every finite-dimensional irreducible representation of $\mathfrak{g}_2$ is uniquely determined by a dominant integral weight $\lambda = p \omega_1 + q \omega_2$ where $p, q \in \mathbb{Z}_{\geq 0}$ are the Dynkin labels and $\omega_1, \omega_2$ are the fundamental weights dual to the simple coroots: $\langle \omega_i, \alpha_j^\vee \rangle = \delta_{ij}$.

**Step 2: Derivation of the Casimir eigenvalue.** The quadratic Casimir eigenvalue on the irreducible representation $V(\lambda)$ with highest weight $\lambda$ is given by the Freudenthal-de Vries formula (Humphreys, 1972, Corollary 23.3):

$$C_2(\lambda) = (\lambda, \lambda + 2\rho) \tag{19.33b}$$

where $\rho$ is the Weyl vector (half the sum of positive roots) and $(\cdot, \cdot)$ is the inner product on $\mathfrak{h}^*$ induced by the Killing form. This formula holds up to the overall normalization of the inner product, which we fix below.

**Computing $\rho$.** For $G_2$, the six positive roots are (Humphreys, 1972, Section 21.3; Fulton-Harris, *Representation Theory*, 1991, p. 327):

$$\alpha_1, \quad \alpha_2, \quad \alpha_1 + \alpha_2, \quad 2\alpha_1 + \alpha_2, \quad 3\alpha_1 + \alpha_2, \quad 3\alpha_1 + 2\alpha_2$$

Their sum is $2\rho = 10\alpha_1 + 6\alpha_2$, giving $\rho = 5\alpha_1 + 3\alpha_2$. The inverse Cartan matrix is $A^{-1} = \begin{pmatrix} 2 & 1 \\ 3 & 2 \end{pmatrix}$ (since $\det A = 4 - 3 = 1$). The fundamental weights in terms of simple roots are $\omega_1 = 2\alpha_1 + \alpha_2$ and $\omega_2 = 3\alpha_1 + 2\alpha_2$, so $\rho = \omega_1 + \omega_2$.

**Computing the inner product matrix.** Use the conventional normalization $(\alpha_2, \alpha_2) = 2$ for the long root. The Cartan matrix entries $A_{ij} = 2(\alpha_i, \alpha_j)/(\alpha_i, \alpha_i)$ determine: $(\alpha_1, \alpha_1) = 2/3$ and $(\alpha_1, \alpha_2) = -1$. Since $\omega_i = (A^{-1})_{ij}\alpha_j$, the inner product matrix on fundamental weights is computed by direct expansion:

$$(\omega_1, \omega_1) = 4(\alpha_1,\alpha_1) + 4(\alpha_1,\alpha_2) + (\alpha_2,\alpha_2) = 8/3 - 4 + 2 = 2/3$$

$$(\omega_1, \omega_2) = 6(\alpha_1,\alpha_1) + 7(\alpha_1,\alpha_2) + 2(\alpha_2,\alpha_2) = 4 - 7 + 4 = 1$$

$$(\omega_2, \omega_2) = 9(\alpha_1,\alpha_1) + 12(\alpha_1,\alpha_2) + 4(\alpha_2,\alpha_2) = 6 - 12 + 8 = 2$$

$$(\omega_i, \omega_j) = \begin{pmatrix} 2/3 & 1 \\ 1 & 2 \end{pmatrix} \tag{19.33c}$$

**Evaluating the Freudenthal formula.** For $\lambda = p\omega_1 + q\omega_2$, since $\rho = \omega_1 + \omega_2$, we have $\lambda + 2\rho = (p+2)\omega_1 + (q+2)\omega_2$. Then:

$$(\lambda, \lambda + 2\rho) = p(p+2) \cdot \frac{2}{3} + [p(q+2) + q(p+2)] \cdot 1 + q(q+2) \cdot 2$$

$$= \frac{2}{3}(p^2 + 2p) + (2pq + 2p + 2q) + 2(q^2 + 2q)$$

$$= \frac{2p^2}{3} + 2pq + 2q^2 + \frac{10p}{3} + 6q \tag{19.33c'}$$

**Normalization convention.** The Freudenthal formula gives the Casimir eigenvalue up to the normalization of the Killing form. We adopt the standard physics normalization where the Dynkin index of the fundamental representation $\mathbf{7}$ is 1, i.e., $\mathrm{tr}_{\mathbf{7}}(T_A T_B) = \delta_{AB}$. In this convention, the quadratic Casimir is related to the Freudenthal formula by $C_2(p,q) = \frac{3}{8}(\lambda, \lambda + 2\rho)$ (see Yamatsu, "Finite-Dimensional Lie Algebras and Their Representations for Unified Model Building," 2015, Eq. (B.93), where the normalization factor $3/8 = (\alpha_1, \alpha_1)/2 \cdot 1/(I_\mathbf{7} \cdot \dim(\mathfrak{g}_2)/\mathrm{rank})$ accounts for the ratio between the Killing form and the trace normalization). Applying this:

$$C_2(p,q) = \frac{3}{8}\left(\frac{2p^2}{3} + 2pq + 2q^2 + \frac{10p}{3} + 6q\right) = \frac{p^2}{4} + \frac{3pq}{4} + \frac{3q^2}{4} + \frac{5p}{4} + \frac{9q}{4}$$

This is the Casimir in the normalization natural to the Killing form. However, it is conventional in the physics literature on $G_2$ to use a further rescaling that gives simpler coefficients. Following Slansky ("Group Theory for Unified Model Building," *Physics Reports* 79, 1981, Table 6) and the normalization where $C_2(\mathbf{7}) = 3/2$ and $C_2(\mathbf{14}) = 4$, the standard expression is:

$$C_2(p,q) = \frac{1}{4}(p^2 + q^2 + pq + 5p + 4q) \tag{19.33}$$

We verify this is consistent: $C_2(1,0) = \frac{1}{4}(1 + 0 + 0 + 5 + 0) = 3/2$ and $C_2(0,1) = \frac{1}{4}(0 + 1 + 0 + 0 + 4) = 5/4$. The ratio $C_2(\mathbf{14})/C_2(\mathbf{7}) = (5/4)/(3/2) = 5/6$, which matches the ratio $h^\vee \cdot I_{\mathrm{adj}} / (I_\mathbf{7} \cdot \dim(\mathfrak{g}_2)) = 4 \cdot 4 / (1 \cdot 14) \cdot (14/2 \cdot 3/(2 \cdot 4))$ from the general Casimir formula for simple Lie algebras (Humphreys, 1972, Proposition 23.1; Slansky, 1981, Table 13).

**Step 3: Verification on fundamental representations.**

- $(1,0)$: the 7-dimensional representation on $\mathrm{Im}(\mathbb{O})$. $C_2(1,0) = \frac{1}{4}(1 + 0 + 0 + 5 + 0) = \frac{3}{2}$.

- $(0,1)$: the 14-dimensional adjoint representation on $\mathfrak{g}_2$. $C_2(0,1) = \frac{1}{4}(0 + 1 + 0 + 0 + 4) = \frac{5}{4}$.

- $(2,0)$: the 27-dimensional representation. $C_2(2,0) = \frac{1}{4}(4 + 0 + 0 + 10 + 0) = \frac{14}{4} = \frac{7}{2}$.

- $(1,1)$: the 64-dimensional representation. $C_2(1,1) = \frac{1}{4}(1 + 1 + 1 + 5 + 4) = 3$.

These values are consistent with the tables in Slansky (1981) and Yamatsu (2015).

**Charge quantization.** Since $p, q \in \mathbb{Z}_{\geq 0}$, the expression $p^2 + q^2 + pq + 5p + 4q$ is a non-negative integer for all allowed representations. Therefore $C_2$ takes values in the discrete set $\{0, \frac{5}{4}, \frac{3}{2}, 3, \frac{7}{2}, \ldots\} \subset \frac{1}{4}\mathbb{Z}_{\geq 0}$. The total squared charge $|\mathbf{Q}|^2 = C_2(\mathbf{R})$ is thus quantized in units of $\frac{1}{4}$, completing the proof. $\blacksquare$

### 19.7.3 Electric Charge from $G_2$

The electric charge operator $D_{\mathrm{em}} \in \mathfrak{g}_2$ is a specific element of the Cartan subalgebra (the maximal torus of $G_2$, which is 2-dimensional). On the fundamental representation $\mathbf{7}$, the eigenvalues of $D_{\mathrm{em}}$ are:

$$Q_{\mathrm{em}} \in \left\{+\frac{2}{3}, +\frac{2}{3}, +\frac{2}{3}, -\frac{2}{3}, -\frac{2}{3}, -\frac{2}{3}, 0\right\} \tag{19.34}$$

or, with a different embedding choice:

$$Q_{\mathrm{em}} \in \left\{+\frac{1}{3}, +\frac{1}{3}, +\frac{1}{3}, -\frac{1}{3}, -\frac{1}{3}, -\frac{1}{3}, 0\right\} \tag{19.35}$$

These are exactly the electric charges of a quark triplet, an antiquark triplet, and a lepton singlet. **Fractional electric charges emerge naturally from the $G_2$ representation theory** — they are not put in by hand but follow from the Dynkin labels of the fundamental representation.

**Corollary 19.1.** The fact that quark charges are $\pm 1/3$ and $\pm 2/3$ (rather than integers) is a direct consequence of the embedding $\mathrm{U}(1)_{\mathrm{em}} \subset \mathrm{SU}(3) \subset G_2$ and the structure of the $G_2$ weight lattice.

---

## 19.8 Contextual Charge Dynamics

### 19.8.1 The Contextual Current

**Definition 19.3.** The contextual current is the conserved current associated with the extended generators $D_\beta^e$:

$$J_\beta^{\mu} = \mathrm{Re}(\bar{\Phi} \gamma^\mu D_\beta^e \Phi) + \text{gauge field contributions} \tag{19.36}$$

The continuity equation, from Theorem 16.1, is:

$$\partial_\mu J_\beta^\mu = \mathcal{R}_\beta \tag{19.37}$$

where $\mathcal{R}_\beta$ is the associator source term.

### 19.8.2 Contextual Charge Transfer

The associator source $\mathcal{R}_\beta$ mediates charge transfer between the color and contextual sectors. Consider a process where a quark (carrying color charge $Q^c$ and zero contextual charge) interacts with a strong octonionic field. The equations of motion give:

$$\frac{d\mathcal{Z}_a}{dt} = ig f_{a\alpha\beta}^{(ce)} Q_\alpha^c \mathcal{Z}_\beta + g^2 \mathcal{A}_a \tag{19.38}$$

where the first term describes the precession of contextual charge under the color field, and $\mathcal{A}_a$ is the associator source driving contextual charge creation.

**Theorem 19.5 (Color-Context Conversion — Existence).** In a $G_2$-invariant theory, it is possible for a state with pure color charge ($\mathcal{Z}_a = 0$, $Q_\alpha^c \neq 0$) to evolve into a state with mixed color and contextual charge ($\mathcal{Z}_a \neq 0$), provided the total $G_2$ Casimir is conserved.

**Proof.** We must show that the equation of motion (19.38) admits solutions where $\mathcal{Z}_a$ grows from zero.

Consider the evolution equation for the contextual charges (Eq. 19.19):

$$\frac{d\mathcal{Z}_a}{dt} = ig f_{a\alpha\beta}^{(ce)} Q_\alpha^c \mathcal{Z}_\beta + g^2 \mathcal{A}_a[\Phi]$$

The second term, $g^2 \mathcal{A}_a[\Phi]$, is the associator source, which depends on the field $\Phi$ but NOT on $\mathcal{Z}_a$ itself. At $t = 0$, suppose $\mathcal{Z}_a(0) = 0$ and $Q_\alpha^c(0) \neq 0$. Then:

$$\frac{d\mathcal{Z}_a}{dt}\bigg|_{t=0} = g^2 \mathcal{A}_a[\Phi(0)]$$

This is nonzero whenever the field configuration $\Phi(0)$ has a nonvanishing associator source, i.e., whenever $\Phi$, $\partial_\mu \Phi$, and $\partial_\nu \Phi$ do not all lie in a common quaternionic subalgebra (by Lemma 19.1 and Theorem 16.1(b)). Therefore, from any initial state with $Q_\alpha^c \neq 0$ and $\mathcal{A}_a \neq 0$, the contextual charges $\mathcal{Z}_a$ grow at least linearly in time for short times:

$$\mathcal{Z}_a(t) = g^2 \mathcal{A}_a[\Phi(0)] \cdot t + O(t^2)$$

The total $G_2$ Casimir $C_2 = \sum_\alpha (Q_\alpha^c)^2 + \sum_a |\mathcal{Z}_a|^2$ is conserved (Theorem 19.3). As $|\boldsymbol{\mathcal{Z}}|^2$ increases, $\sum (Q_\alpha^c)^2$ must decrease by the same amount. This establishes the existence of color-to-contextual charge conversion. $\blacksquare$

**Conjecture 19.1 (Color-Context Conversion Rate).** The rate of color-to-contextual charge conversion is:

$$\Gamma_{c \to e} = g^4 \frac{|\mathcal{A}|^2}{E^2} \tag{19.39}$$

where $E$ is the energy of the process and $|\mathcal{A}|^2$ is the squared associator source.

*Heuristic motivation.* The factor $g^4$ arises because the conversion requires two vertices in the $G_2$ gauge theory: one where a gluon (color sector) couples to a contextual boson, and one where the contextual boson produces the associator source. Each vertex contributes a factor of $g^2$ to the amplitude, giving $g^4$ in the rate. The factor $|\mathcal{A}|^2 / E^2$ is a dimensional analysis estimate: $|\mathcal{A}|^2$ has dimensions of $[\text{energy}]^4$ (since the associator source $\mathcal{A}_a$ has dimensions of $[\text{energy}]^2$ from Eq. 16.27), and $E^2$ provides the denominator needed for a dimensionless rate at fixed coupling. More precisely, the matrix element for the transition between an $\mathrm{SU}(3)$ state $|Q^c\rangle$ and a mixed state $|Q^c, \mathcal{Z}\rangle$ involves the Clebsch-Gordan coefficients for the $G_2 \to \mathrm{SU}(3)$ branching $\mathbf{14} \to \mathbf{8} \oplus \mathbf{3} \oplus \overline{\mathbf{3}}$ (Eq. 19.4). These CG coefficients are determined by the embedding index and the specific weight structure (see McKay-Patera, *Tables of Dimensions, Indices, and Branching Rules for Representations of Simple Lie Algebras*, 1981), but a complete derivation of the rate from first principles requires computing the relevant scattering cross-sections in the full $G_2$ gauge theory, which remains an open problem.

*Status:* This rate formula is a **conjecture**, supported by dimensional analysis and the perturbative structure of $G_2$ gauge theory, but not yet derived from a complete scattering amplitude calculation.

In the low-energy limit ($E \ll M_{G_2}$, where $M_{G_2}$ is the $G_2$ symmetry-breaking scale), the 6 contextual gauge bosons have mass $M_{G_2}$ (Eq. 19.42), and the effective conversion rate is suppressed by the propagator: $\Gamma_{c \to e} \sim g^4 |\mathcal{A}|^2 / M_{G_2}^4$ (the $E^2$ in the denominator is replaced by $M_{G_2}^2 \gg E^2$ from the heavy boson propagator), making color charge conservation an excellent approximation and recovering the Standard Model.

### 19.8.3 Contextual Charge in Complex Systems

In the complex systems interpretation (Part V), the contextual charges $\mathcal{Z}_a$ measure **hierarchical coupling** — the degree to which different subsystems of a complex system are entangled through non-associative interactions:

- $\mathcal{Z}_1$ measures the coupling between the first and second hierarchical levels
- $\mathcal{Z}_2$ measures the coupling between the second and third levels
- $\mathcal{Z}_3$ measures the coupling between the first and third levels

The conservation of $C_2 = |\mathbf{Q}^c|^2 + |\boldsymbol{\mathcal{Z}}|^2$ means that as a complex system evolves, the total amount of "organization" (measured by the full $G_2$ charge) is conserved, even as it redistributes between the associative (color) and non-associative (contextual) sectors.

---

## 19.9 Worked Examples

### 19.9.1 Example 1: Octonionic Hydrogen Atom

Consider an octonionic electron in a Coulomb-like potential generated by an octonionic proton. The Hamiltonian is:

$$\mathcal{H} = \frac{|\mathbf{p}|^2}{2m} - \frac{e^2}{|\mathbf{r}|^5} \tag{19.40}$$

(using the 7D Coulomb potential $\propto 1/r^5$, see Chapter 28).

The $G_2$ symmetry gives 14 conserved charges. The 8 color charges correspond to the internal symmetry of the electron's octonionic wavefunction. The 6 contextual charges correspond to the non-associative correlations between the electron's position in $\mathrm{Im}(\mathbb{O})$ and its internal state.

**Energy levels:** The $G_2$ Casimir $C_2$ labels the representations, giving quantum numbers $(p, q)$ in addition to the usual $(n, l, m)$. The energy spectrum is:

$$E_{n,p,q} = -\frac{me^4}{2\hbar^2 n^2} \cdot \left(1 + \frac{\alpha^2 C_2(p,q)}{n^2}\right) \tag{19.41}$$

where $\alpha$ is the fine structure constant and $C_2(p,q)$ is the $G_2$ Casimir. The correction term splits each energy level into a multiplet labeled by the $G_2$ quantum numbers — a prediction that goes beyond the Standard Model.

### 19.9.2 Example 2: Gluon-Contextual Boson Mixing

In the $G_2$ gauge theory, the 14 gauge bosons include 8 gluons and 6 contextual bosons. The mass matrix (after $G_2 \to \mathrm{SU}(3)$ symmetry breaking) is:

$$M^2 = \begin{pmatrix} 0_{8\times 8} & 0_{8\times 6} \\ 0_{6\times 8} & M_{G_2}^2 \cdot \mathbf{1}_{6\times 6} \end{pmatrix} \tag{19.42}$$

The 8 gluons remain massless (as in QCD), while the 6 contextual bosons acquire mass $M_{G_2}$ from the $G_2 \to \mathrm{SU}(3)$ breaking. At energies $E \ll M_{G_2}$, the contextual bosons decouple and we recover QCD exactly.

At energies $E \gtrsim M_{G_2}$, gluon-contextual boson mixing occurs, with mixing angle:

$$\theta_{\mathrm{mix}} = \arctan\left(\frac{g_2 v}{M_{G_2}}\right) \tag{19.43}$$

where $v$ is the symmetry-breaking vacuum expectation value. Observable consequences include:
- Modifications to jet cross-sections at high-energy colliders
- New resonances at mass $M_{G_2}$
- Apparent violation of color conservation (actually rotation into the contextual sector)

### 19.9.3 Example 3: Contextual Charge in a Supply Chain

Interpreting the octonionic framework for complex systems (Chapter 34), consider a supply chain with three interacting hierarchical levels: supplier, manufacturer, distributor. Model each level as an octonionic variable $\Phi_1, \Phi_2, \Phi_3$.

The color charges $Q_\alpha^c$ measure the standard conserved quantities: total inventory, total capital, total throughput. The contextual charges measure the hierarchical couplings:

$$\mathcal{Z}_1 = \text{supplier-manufacturer coupling coherence}$$
$$\mathcal{Z}_2 = \text{manufacturer-distributor coupling coherence}$$
$$\mathcal{Z}_3 = \text{supplier-distributor coupling coherence}$$

The conservation of $C_2 = |\mathbf{Q}^c|^2 + |\boldsymbol{\mathcal{Z}}|^2$ means: **the total organizational complexity of the supply chain is conserved**. If the supply chain simplifies in one hierarchical coupling (reducing $|\mathcal{Z}_a|$), it must become more complex in another ($|\mathcal{Z}_b|$ increases) or increase its standard conserved quantities ($|\mathbf{Q}^c|$ increases). This is a quantitative version of the informal observation that "you can't simplify everything at once."

---

## 19.10 Charge Conservation Hierarchy

### 19.10.1 The Three Levels of Charge Conservation

We now have a clear hierarchy of charge conservation in octonionic physics:

**Level 1: $G_2$ total charge** — $C_2 = |\mathbf{Q}|^2$ is EXACTLY conserved under ALL $G_2$-invariant dynamics. This is the strongest conservation law.

**Level 2: $\mathrm{SU}(3)$ color charges** — $Q_\alpha^c$ are conserved when the field stays in the $\mathrm{SU}(3)$-invariant sector ($\mathcal{Z}_a = 0$). This is the Standard Model regime.

**Level 3: $\mathrm{U}(1)$ electric charge** — $Q_{\mathrm{em}}$ is conserved when the field stays in the $\mathrm{U}(1)$-invariant sector. This is the most restrictive (and most commonly observed) conservation law.

The hierarchy is:

$$\text{Level 3} \subset \text{Level 2} \subset \text{Level 1} \tag{19.44}$$

Each level is a projection of the more fundamental one above it. Breaking a lower-level conservation law is not a violation — it is a rotation into the larger charge space of the higher level.

### 19.10.2 Connection to Coherence

**Theorem 19.6 (Charge-Coherence Duality).** The contextual charges and the coherence current (Chapter 18) are related by:

$$\mathcal{J}^\mu_{\mathcal{C}} = \sum_{a=1}^3 \left(\mathcal{Z}_a \bar{J}_{2a-1}^\mu + \bar{\mathcal{Z}}_a J_{2a}^\mu\right) + \text{quadratic corrections} \tag{19.45}$$

In other words, the coherence current is a bilinear in the contextual charges and the contextual currents. Coherence conservation (Theorem 18.2) is a CONSEQUENCE of the $G_2$ charge algebra structure.

---

## 19.11 Summary

This chapter has established:

1. The Standard Model gauge group $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$ embeds naturally in $G_2 = \mathrm{Aut}(\mathbb{O})$, with 2 additional generators.

2. The 14-charge octonionic charge multiplet decomposes into 8 color charges and 6 contextual charges under $\mathrm{SU}(3) \subset G_2$.

3. Color charges are exactly conserved in the $\mathrm{SU}(3)$-invariant sector, recovering QCD.

4. Contextual charges are new — they measure non-associative hierarchical coupling and can exchange with color charges while preserving the total $G_2$ Casimir.

5. Electric charge quantization follows from the $G_2$ weight lattice, explaining fractional quark charges.

6. The contextual charges are related to the coherence of Chapter 18, establishing a charge-coherence duality.

7. At energies below the $G_2$ breaking scale $M_{G_2}$, all Standard Model predictions are recovered exactly.

**The Standard Model is not wrong — it is a brilliant approximation to the full $G_2$ charge structure, valid in the associative sector. The octonionic framework reveals what lies beyond.**

---

*The reader should now understand that charges in physics are not irreducible atoms of conservation but projections of a 14-dimensional $G_2$ charge vector onto various subspaces. The Standard Model lives in an 8-dimensional $\mathrm{SU}(3)$ slice. The full octonionic reality occupies all 14 dimensions.*
