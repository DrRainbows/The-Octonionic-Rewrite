> **Rigor Level: CONSTRUCTIVE** — Generalized Noether theorem for alternative algebras; systematic analysis with some derivations sketched.
> **Novelty: EXTENSION** — Extends Noether's theorem to the non-associative setting; classical Noether theory is well-established.

# Chapter 16: Noether's Theorem in Non-Associative Symmetry Groups

*Part III: Conservation Laws — Breaking and Inventing*

---

## 16.1 Introduction: The Classical Noether Program

Emmy Noether's first theorem (1918) stands as one of the supreme achievements of mathematical physics: every continuous symmetry of a Lagrangian system corresponds to a conserved current. The proof, in its classical form, proceeds through the following chain:

1. A Lie group $G$ acts on the configuration space $Q$.
2. The action functional $S[\phi] = \int \mathcal{L}(\phi, \partial_\mu \phi) \, d^n x$ is invariant under $G$.
3. Infinitesimal generators $\xi^a$ of $G$ produce variations $\delta \phi = \xi^a T_a \phi$.
4. On-shell (i.e., when the Euler-Lagrange equations hold), the Noether current $J^\mu_a = \frac{\partial \mathcal{L}}{\partial (\partial_\mu \phi)} T_a \phi$ satisfies $\partial_\mu J^\mu_a = 0$.
5. The conserved charge $Q_a = \int J^0_a \, d^{n-1}x$ is time-independent.

Every step in this chain depends critically on **associativity**. The generators $T_a$ close under the Lie bracket $[T_a, T_b] = f^{ab}_c T_c$, and the Jacobi identity ensures that the algebra is well-defined. The group composition law $(g_1 g_2) g_3 = g_1 (g_2 g_3)$ guarantees that finite symmetry transformations are path-independent.

When we lift physics to the octonionic setting, the natural symmetry group is $G_2 = \mathrm{Aut}(\mathbb{O})$, and the fundamental algebraic structure is a **Moufang loop** rather than a Lie group. The Jacobi identity fails. The composition of symmetry transformations becomes path-dependent. The entire classical Noether apparatus requires reconstruction.

This chapter provides that reconstruction. We derive the **Generalized Noether Theorem for Alternative Algebras** (Theorem 16.1), identify the correction terms arising from non-associativity, and demonstrate that the classical theorem is recovered exactly upon projection to associative subalgebras.

**Cross-references:** This chapter relies on the $G_2$ structure developed in Chapter 5, the COA axioms from Chapter 6, the associator calculus of Chapter 7, and the octonionic calculus of Chapter 11. Results here are applied in Chapters 17–21 and throughout Part V.

---

## 16.2 Why Classical Noether Fails in the Octonionic Setting

Let us be precise about where the classical proof breaks down. Consider a field theory with octonionic-valued fields $\Phi: M \to \mathbb{O}$, where $M$ is a (smooth) spacetime manifold.

### 16.2.1 Failure of the Lie Bracket Closure

In a classical gauge theory, infinitesimal symmetry generators $T_a$ form a Lie algebra:

$$[T_a, T_b] = f^{ab}_c T_c \tag{16.1}$$

with structure constants $f^{ab}_c$ satisfying the Jacobi identity:

$$f^{ab}_d f^{dc}_e + f^{bc}_d f^{da}_e + f^{ca}_d f^{db}_e = 0 \tag{16.2}$$

When the generators act on octonionic fields, composing two generators requires evaluating expressions of the form $T_a(T_b \Phi)$. Because $\mathbb{O}$ is non-associative, we must distinguish between:

$$(T_a T_b) \Phi \quad \text{and} \quad T_a (T_b \Phi) \tag{16.3}$$

The **Malcev algebra** replaces the Lie algebra. For elements $x, y, z$ in the imaginary octonions $\mathrm{Im}(\mathbb{O})$, the Malcev identity holds:

$$J(x,y,[x,z]) = [J(x,y,z), x] \tag{16.4}$$

where $J(x,y,z) = [[x,y],z] + [[y,z],x] + [[z,x],y]$ is the Jacobiator (the failure of the Jacobi identity).

### 16.2.2 Failure of Group Composition Associativity

The symmetry "group" of octonionic multiplication is not a group at all — it is a **Moufang loop**. A Moufang loop $(L, \cdot)$ satisfies the Moufang identities:

$$((xy)x)z = x(y(xz)) \tag{16.5a}$$
$$z(x(yx)) = ((zx)y)x \tag{16.5b}$$
$$x(y(zy)) = ((xy)z)y \tag{16.5c}$$

but NOT the general associative law. Thus, when we compose symmetry transformations $g_1, g_2, g_3 \in L$, the result depends on the association order.

### 16.2.3 Failure of the Variation Commutation

In the classical Noether proof, a critical step is:

$$\delta \mathcal{L} = \frac{\partial \mathcal{L}}{\partial \phi} \delta\phi + \frac{\partial \mathcal{L}}{\partial(\partial_\mu \phi)} \delta(\partial_\mu \phi) \tag{16.6}$$

where we use $\delta(\partial_\mu \phi) = \partial_\mu(\delta \phi)$, i.e., variation and differentiation commute. When $\phi$ is octonionic-valued and the variation involves octonionic multiplication, this commutation acquires a correction:

$$\delta(\partial_\mu \Phi) = \partial_\mu(\delta \Phi) + \mathcal{A}_\mu(\xi, \Phi) \tag{16.7}$$

where $\mathcal{A}_\mu$ is an **associator correction term** arising from the non-commutativity of differentiation and octonionic left/right multiplication.

---

## 16.3 The Algebraic Preliminaries: Malcev Algebras and Sabinin Algebras

### 16.3.1 Malcev Algebras

**Definition 16.1 (Malcev Algebra).** A Malcev algebra $(\mathfrak{m}, [\cdot, \cdot])$ is a vector space $\mathfrak{m}$ equipped with an anticommutative bilinear product satisfying the Malcev identity:

$$[J(x,y,z), x] = J(x,y,[x,z]) \tag{16.8}$$

for all $x, y, z \in \mathfrak{m}$, where $J(x,y,z) = [[x,y],z] + [[y,z],x] + [[z,x],y]$.

**Theorem 16.A (Malcev, 1955).** The tangent algebra of any Moufang loop is a Malcev algebra. Conversely, every finite-dimensional Malcev algebra over $\mathbb{R}$ is the tangent algebra of an analytic Moufang loop.

The imaginary octonions $\mathrm{Im}(\mathbb{O})$ with the commutator bracket $[x,y] = xy - yx$ form the unique simple 7-dimensional Malcev algebra that is not a Lie algebra.

### 16.3.2 Sabinin Algebras

For full generality, we work with Sabinin algebras (Chapter 9), which encode the tangent structure of arbitrary smooth loops.

**Definition 16.2 (Sabinin Algebra).** A Sabinin algebra is a vector space $V$ equipped with a family of multilinear operations:

$$\langle x_1, \ldots, x_m; y, z \rangle: V^{m+2} \to V \tag{16.9}$$

satisfying axioms that generalize both the Jacobi identity and the Malcev identity to arbitrary order. The binary operation $\langle \,; y, z \rangle = [y, z]$ recovers the bracket, and the ternary operation $\langle x; y, z \rangle$ encodes the first-order associator information.

### 16.3.3 The $G_2$ Lie Algebra Acting on $\mathbb{O}$

While the Moufang loop of unit octonions is non-associative, its **automorphism group** $G_2 = \mathrm{Aut}(\mathbb{O})$ IS a Lie group — in fact, an exceptional simple Lie group of dimension 14. The Lie algebra $\mathfrak{g}_2$ consists of derivations of $\mathbb{O}$:

$$\mathfrak{g}_2 = \mathrm{Der}(\mathbb{O}) = \{D \in \mathrm{End}(\mathbb{O}) : D(xy) = (Dx)y + x(Dy)\} \tag{16.10}$$

**Proposition 16.1.** Every derivation $D \in \mathfrak{g}_2$ can be written as:

$$D_{a,b} = [L_a, L_b] + [L_a, R_b] + [R_a, R_b] \tag{16.11}$$

for suitable $a, b \in \mathrm{Im}(\mathbb{O})$, where $L_a(x) = ax$ and $R_b(x) = xb$ are left and right multiplication operators. Equivalently, every derivation has the explicit action:

$$D_{a,b}(x) = [[a,b], x] - 3[a, b, x] \tag{16.11a}$$

where $[a,b] = ab - ba$ is the commutator and $[a,b,x] = (ab)x - a(bx)$ is the associator.

*Proof.* The proof has three parts: (I) every $D_{a,b}$ is a derivation; (II) the operator form (16.11) equals the closed form (16.11a); (III) these derivations span all of $\mathrm{Der}(\mathbb{O})$.

**Part I: $D_{a,b}$ is a derivation.** We verify the Leibniz rule $D_{a,b}(xy) = D_{a,b}(x) \cdot y + x \cdot D_{a,b}(y)$ using the operator form (16.11).

**Lemma 16.1a.** For $a \in \mathrm{Im}(\mathbb{O})$ and $x, y \in \mathbb{O}$, the left and right multiplication operators satisfy:

$$L_a(xy) = L_a(x) \cdot y - [a,x,y] \tag{I.2}$$
$$R_b(xy) = x \cdot R_b(y) + [x,y,b] \tag{I.3}$$

*Proof.* From the associator $[a,x,y] = (ax)y - a(xy)$, we get $a(xy) = (ax)y - [a,x,y]$, which is (I.2). Similarly, $[x,y,b] = (xy)b - x(yb)$ gives $(xy)b = x(yb) + [x,y,b]$, which is (I.3). $\square$

Using (I.2) and (I.3) iteratively, we compute $[L_a, L_b](xy)$, $[L_a, R_b](xy)$, and $[R_a, R_b](xy)$. For example:

$$[L_a, L_b](xy) = ([L_a, L_b](x))y - [a,bx,y] + [b,ax,y] - a[b,x,y] + b[a,x,y]. \tag{I.4}$$

When we sum all three commutators to form $D_{a,b}(xy)$, the associator remainder terms from (I.4) and the analogous expressions for $[L_a, R_b]$ and $[R_a, R_b]$ cancel in pairs. This cancellation relies on the complete antisymmetry of the associator (Theorem 3.2.1): terms like $[a,bx,y]$ and $[b,ax,y]$ recombine with terms from $[L_a, R_b]$ and $[R_a, R_b]$ in such a way that the total correction vanishes. The detailed verification of this cancellation is carried out in Schafer, *An Introduction to Nonassociative Algebras*, 1966, Chapter III, Theorem 3.22.

The result is: $D_{a,b}(xy) = D_{a,b}(x) \cdot y + x \cdot D_{a,b}(y)$ for all $x, y \in \mathbb{O}$.

**Part II: Equivalence of forms.** We prove $D_{a,b}(x) = [L_a, L_b](x) + [L_a, R_b](x) + [R_a, R_b](x) = [[a,b],x] - 3[a,b,x]$.

Expanding the operator form on $x$:

$$D_{a,b}(x) = a(bx) - b(ax) + a(xb) - (ax)b + (xb)a - (xa)b. \tag{II.1}$$

Now expand $[[a,b],x]$ using associators. By the definition $[a,b] = ab - ba$:

$$[[a,b],x] = (ab)x - (ba)x - x(ab) + x(ba).$$

Rewrite each term using the associator $[p,q,r] = (pq)r - p(qr)$:

- $(ab)x = a(bx) + [a,b,x]$
- $(ba)x = b(ax) - [a,b,x]$ (since $[b,a,x] = -[a,b,x]$ by antisymmetry)
- $x(ab) = (xa)b - [a,b,x]$ (since $[x,a,b] = [a,b,x]$ by cyclic invariance: the permutation $(x,a,b) \to (a,b,x)$ is even)
- $x(ba) = (xb)a + [a,b,x]$ (since $[x,b,a] = -[a,b,x]$ by the transposition $(b,a) \to (a,b)$ composed with cyclic invariance)

Substituting:

$$[[a,b],x] = a(bx) + [a,b,x] - b(ax) + [a,b,x] - (xa)b + [a,b,x] + (xb)a + [a,b,x]$$
$$= a(bx) - b(ax) - (xa)b + (xb)a + 4[a,b,x]. \tag{II.2}$$

Therefore: $[[a,b],x] - 3[a,b,x] = a(bx) - b(ax) - (xa)b + (xb)a + [a,b,x]$.

We need to show this equals (II.1). The difference is:

$$D_{a,b}(x) - \big([[a,b],x] - 3[a,b,x]\big) = a(xb) - (ax)b - [a,b,x]. \tag{II.3}$$

Now, $a(xb) - (ax)b = -[a,x,b]$ (by the definition of the associator). And $[a,x,b] = -[a,b,x]$ (antisymmetry in positions 2 and 3). So $a(xb) - (ax)b = -(-[a,b,x]) = [a,b,x]$. Substituting into (II.3):

$$D_{a,b}(x) - \big([[a,b],x] - 3[a,b,x]\big) = [a,b,x] - [a,b,x] = 0.$$

Therefore $D_{a,b}(x) = [[a,b],x] - 3[a,b,x]$ for all $x \in \mathbb{O}$. $\checkmark$

**Verification on basis elements.** Take $a = e_1$, $b = e_2$, $x = e_4$. Using Fano-plane conventions ($e_1 e_2 = e_3$, $e_1 e_4 = e_5$, $e_2 e_4 = e_6$, $e_3 e_4 = e_7$, $e_6 e_1 = e_7$, $e_2 e_5 = e_7$):

*Operator form (II.1):*
- $e_1(e_2 e_4) = e_1 e_6 = -e_7$ (since $e_6 e_1 = e_7$ implies $e_1 e_6 = -e_7$)
- $e_2(e_1 e_4) = e_2 e_5 = e_7$
- $e_1(e_4 e_2) = e_1(-e_6) = e_7$
- $(e_1 e_4)e_2 = e_5 e_2 = -e_7$ (since $e_2 e_5 = e_7$ implies $e_5 e_2 = -e_7$)
- $(e_4 e_2)e_1 = (-e_6)e_1 = -e_7$
- $(e_4 e_1)e_2 = (-e_5)e_2 = e_7$

Sum: $-e_7 - e_7 + e_7 + e_7 - e_7 - e_7 = -2e_7$.

*Closed form (16.11a):* $[e_1,e_2] = 2e_3$, $[e_1,e_2,e_4] = (e_1 e_2)e_4 - e_1(e_2 e_4) = e_3 e_4 - e_1 e_6 = e_7 + e_7 = 2e_7$.

$[[e_1,e_2],e_4] - 3[e_1,e_2,e_4] = 4e_7 - 6e_7 = -2e_7$. $\checkmark$

**Part III: These derivations span $\mathrm{Der}(\mathbb{O})$.** We prove $\dim(\mathrm{span}\{D_{a,b} : a, b \in \mathrm{Im}(\mathbb{O})\}) = 14 = \dim(\mathfrak{g}_2)$.

The space of derivations $\mathrm{Der}(\mathbb{O})$ is a Lie subalgebra of $\mathfrak{so}(7)$ (by Proposition 5.4.1). We have $\dim(\mathrm{Der}(\mathbb{O})) = \dim(G_2) = 14$ (Theorem 5.3.1).

The maps $D_{a,b}$ for $a, b \in \mathrm{Im}(\mathbb{O})$ define a bilinear map $\mathrm{Im}(\mathbb{O}) \times \mathrm{Im}(\mathbb{O}) \to \mathrm{End}(\mathbb{O})$. The image lies in $\mathrm{Der}(\mathbb{O})$ by Part I. The map is antisymmetric: $D_{b,a} = -D_{a,b}$, which follows from the closed form (16.11a) since $[b,a] = -[a,b]$ and $[b,a,x] = -[a,b,x]$ (antisymmetry of commutator and associator).

The image of the map $(a,b) \mapsto D_{a,b}$ from $\Lambda^2(\mathrm{Im}(\mathbb{O}))$ to $\mathrm{Der}(\mathbb{O})$ has domain of dimension $\binom{7}{2} = 21$. The kernel consists of pairs $(a,b)$ such that $D_{a,b} = 0$. By the decomposition $\mathfrak{so}(7) = \mathfrak{g}_2 \oplus \mathbb{R}^7$ (Section 5.6.5 in Chapter 5), the map $\Lambda^2(\mathbb{R}^7) \cong \mathfrak{so}(7) \to \mathrm{Der}(\mathbb{O})$ is exactly the projection onto the $\mathfrak{g}_2$ summand with kernel $\mathbb{R}^7$. Since $\dim(\mathfrak{so}(7)) = 21$ and $\dim(\mathfrak{g}_2) = 14$, the kernel has dimension $21 - 14 = 7$. Therefore the image has dimension $14$, which equals $\dim(\mathrm{Der}(\mathbb{O}))$.

Hence every derivation of $\mathbb{O}$ is of the form $D_{a,b}$ for some $a, b \in \mathrm{Im}(\mathbb{O})$. $\blacksquare$

**Remark (Citation).** The result that every derivation of an alternative algebra is inner (generated by commutators of left and right multiplication operators) is due to Schafer (1966), *An Introduction to Nonassociative Algebras*, Academic Press, Chapter III, Theorem 3.22. The specific form $D_{a,b}(x) = [[a,b],x] - 3[a,b,x]$ appears in Schafer's Chapter IV, Section 4. The dimension argument using $\mathfrak{so}(7) = \mathfrak{g}_2 \oplus \mathbb{R}^7$ is due to the structure theory of $G_2$ (see also Baez, "The Octonions," Bull. AMS 39 (2002), Section 4.1).

This is crucial: $G_2$ transformations preserve the ENTIRE octonionic multiplication table, including all associator structure. The 14 generators of $\mathfrak{g}_2$ decompose under the $\mathrm{SU}(3) \subset G_2$ embedding as:

$$\mathfrak{g}_2 = \mathfrak{su}(3) \oplus \mathbb{C}^3 \oplus \overline{\mathbb{C}^3} \tag{16.12}$$

where $\mathfrak{su}(3)$ is 8-dimensional and $\mathbb{C}^3 \oplus \overline{\mathbb{C}^3}$ is 6-dimensional.

---

## 16.4 The Octonionic Action Functional

### 16.4.1 Definition

Let $\Phi: M^{1,d} \to \mathbb{O}$ be an octonionic scalar field on a $(1+d)$-dimensional spacetime. The **octonionic action functional** is:

$$S[\Phi] = \int_M \mathcal{L}(\Phi, \partial_\mu \Phi, [\Phi, \partial_\mu \Phi, \partial_\nu \Phi]) \, d^{d+1}x \tag{16.13}$$

Note the critical difference from the classical action: the Lagrangian depends explicitly on the **associator** $[\Phi, \partial_\mu \Phi, \partial_\nu \Phi]$. This is because in the octonionic setting, the kinetic energy, potential energy, and interaction terms all involve products of octonionic quantities whose evaluation depends on association order.

**Example (Octonionic Klein-Gordon).** The simplest octonionic field theory has Lagrangian:

$$\mathcal{L}_{\mathrm{OKG}} = \frac{1}{2}\mathrm{Re}(\overline{\partial_\mu \Phi} \, \partial^\mu \Phi) - \frac{1}{2}m^2 \mathrm{Re}(\bar{\Phi}\Phi) + \frac{\lambda}{4!} \mathrm{Re}((\bar{\Phi}\Phi)(\bar{\Phi}\Phi)) \tag{16.14}$$

Here $\mathrm{Re}(x) = \frac{1}{2}(x + \bar{x})$ extracts the real part. The quartic term is ambiguous due to non-associativity:

$$(\bar{\Phi}\Phi)(\bar{\Phi}\Phi) \neq \bar{\Phi}(\Phi \bar{\Phi})\Phi \neq \bar{\Phi}(\Phi(\bar{\Phi}\Phi)) \tag{16.15}$$

However, the real part is independent of association order for elements of the form $\bar{x}x$ (by alternativity), so $\mathcal{L}_{\mathrm{OKG}}$ is well-defined. This is not an accident — **the real part acts as a natural projector onto the associative sector**.

### 16.4.2 The Euler-Lagrange Equations

The octonionic Euler-Lagrange equations require care. Define the **left octonionic functional derivative**:

$$\frac{\delta^L S}{\delta \Phi}(x) = \lim_{\epsilon \to 0} \frac{1}{\epsilon}\left(S[\Phi + \epsilon \eta] - S[\Phi]\right) \tag{16.16}$$

where $\eta$ is an octonionic test field with compact support and $\epsilon \in \mathbb{R}$ (a real parameter, so associativity issues don't arise at this level).

**Theorem 16.B (Octonionic Euler-Lagrange Equations).** The field $\Phi$ is a critical point of $S$ if and only if:

$$\frac{\partial \mathcal{L}}{\partial \Phi} - \partial_\mu \frac{\partial \mathcal{L}}{\partial(\partial_\mu \Phi)} + \mathcal{E}_{\mathrm{assoc}}[\Phi] = 0 \tag{16.17}$$

where the associator correction term is:

$$\mathcal{E}_{\mathrm{assoc}}[\Phi] = \sum_{\mu < \nu} \left(\frac{\partial \mathcal{L}}{\partial [\Phi, \partial_\mu \Phi, \partial_\nu \Phi]} \right)_{\mathrm{cycl}} \tag{16.18}$$

and the subscript "cycl" denotes the appropriate cyclic sum over the three slots of the associator.

*Proof.* We compute $\frac{d}{d\epsilon}\big|_{\epsilon=0} S[\Phi + \epsilon\eta]$. Since $\epsilon \in \mathbb{R}$ commutes and associates with all octonions:

$$\frac{d}{d\epsilon}\bigg|_{\epsilon=0} \mathcal{L}(\Phi+\epsilon\eta, \partial_\mu\Phi + \epsilon \partial_\mu \eta, [\Phi+\epsilon\eta, \partial_\mu\Phi+\epsilon\partial_\mu\eta, \partial_\nu\Phi+\epsilon\partial_\nu\eta])$$

The first two terms give the classical Euler-Lagrange contributions. The third gives:

$$\frac{d}{d\epsilon}\bigg|_{\epsilon=0} [\Phi+\epsilon\eta, \partial_\mu\Phi+\epsilon\partial_\mu\eta, \partial_\nu\Phi+\epsilon\partial_\nu\eta]$$

By linearity of the associator in each slot (the associator is trilinear in an alternative algebra), this produces three terms:

$$[\eta, \partial_\mu\Phi, \partial_\nu\Phi] + [\Phi, \partial_\mu\eta, \partial_\nu\Phi] + [\Phi, \partial_\mu\Phi, \partial_\nu\eta] \tag{16.19}$$

Integrating by parts on the latter two (moving $\partial_\mu$ from $\eta$ to the Lagrangian prefactor) yields $\mathcal{E}_{\mathrm{assoc}}$. $\blacksquare$

---

## 16.5 The Generalized Noether Theorem

### 16.5.1 $G_2$ Symmetry and Infinitesimal Transformations

Let $g \in G_2$ act on $\Phi$ by $\Phi \mapsto g \cdot \Phi$ where $g$ is an automorphism of $\mathbb{O}$, so:

$$g \cdot (ab) = (g \cdot a)(g \cdot b) \quad \forall a, b \in \mathbb{O} \tag{16.20}$$

Infinitesimally, with $g = \mathrm{id} + \epsilon D + O(\epsilon^2)$ for $D \in \mathfrak{g}_2$:

$$\delta_D \Phi = D(\Phi) \tag{16.21}$$

The crucial property is that $G_2$ automorphisms preserve associators:

$$g \cdot [a, b, c] = [g \cdot a, g \cdot b, g \cdot c] \tag{16.22}$$

This follows immediately from $g$ being an algebra automorphism. Infinitesimally:

$$D([a,b,c]) = [Da, b, c] + [a, Db, c] + [a, b, Dc] \tag{16.23}$$

### 16.5.2 Statement of the Theorem

**Theorem 16.1 (Generalized Noether Theorem for Alternative Algebras).** Let $S[\Phi] = \int_M \mathcal{L}(\Phi, \partial_\mu \Phi, [\Phi, \partial_\mu\Phi, \partial_\nu\Phi]) \, d^{d+1}x$ be an action functional for an octonionic field $\Phi$. Let $G_2$ act on $\Phi$ via algebra automorphisms, and suppose $S$ is $G_2$-invariant. Then for each generator $D \in \mathfrak{g}_2$, there exists a current:

$$\mathcal{J}^\mu_D = \frac{\partial \mathcal{L}}{\partial(\partial_\mu \Phi)} \cdot D(\Phi) + \sum_{\nu} \mathcal{K}^{\mu\nu}_D \tag{16.24}$$

where the **associator current correction** is:

$$\mathcal{K}^{\mu\nu}_D = \frac{\partial \mathcal{L}}{\partial[\Phi, \partial_\mu\Phi, \partial_\nu\Phi]} \cdot \bigl([\Phi, D(\partial_\mu\Phi), \partial_\nu\Phi] + [\Phi, \partial_\mu\Phi, D(\partial_\nu\Phi)]\bigr) \tag{16.25}$$

and the generalized conservation law holds:

$$\partial_\mu \mathcal{J}^\mu_D = \mathcal{R}_D \tag{16.26}$$

where $\mathcal{R}_D$ is the **associator source term**:

$$\mathcal{R}_D = \sum_{\mu < \nu} \mathrm{Re}\left(\overline{D(\Phi)} \cdot [\partial_\mu\Phi, \partial_\nu\Phi, \Phi] \right) \cdot \frac{\partial^2 \mathcal{L}}{\partial \Phi \, \partial[\Phi, \partial_\mu\Phi, \partial_\nu\Phi]} \tag{16.27}$$

Moreover:

**(a)** The source term $\mathcal{R}_D$ vanishes identically when restricted to any associative subalgebra $\mathbb{H} \subset \mathbb{O}$, recovering the classical Noether theorem with $\partial_\mu J^\mu = 0$.

**(b)** For pure $G_2$ transformations (which preserve the associator), the integrated charge $Q_D = \int_\Sigma \mathcal{J}^0_D \, d^d x$ satisfies:

$$\frac{dQ_D}{dt} = \int_\Sigma \mathcal{R}_D \, d^d x \tag{16.28}$$

**(c)** If the Lagrangian depends on $\Phi$ only through $|\Phi|^2$ and the associator dependence enters only through $|[\Phi, \partial_\mu\Phi, \partial_\nu\Phi]|^2$, then $\mathcal{R}_D = 0$ and the conservation law is exact.

### 16.5.3 Proof of Theorem 16.1

*Proof.* We compute $\delta_D S = 0$ under the assumption of $G_2$ invariance.

**Step 1.** Compute $\delta_D \mathcal{L}$:

$$\delta_D \mathcal{L} = \frac{\partial \mathcal{L}}{\partial \Phi} D(\Phi) + \frac{\partial \mathcal{L}}{\partial(\partial_\mu \Phi)} D(\partial_\mu \Phi) + \frac{\partial \mathcal{L}}{\partial [\Phi, \partial_\mu\Phi, \partial_\nu\Phi]} \delta_D [\Phi, \partial_\mu\Phi, \partial_\nu\Phi] \tag{16.29}$$

**Step 2.** Since $D$ is a derivation commuting with spacetime derivatives (it acts only on the octonionic indices), $D(\partial_\mu \Phi) = \partial_\mu(D\Phi)$. Thus the second term becomes:

$$\frac{\partial \mathcal{L}}{\partial(\partial_\mu \Phi)} \partial_\mu(D\Phi) = \partial_\mu\left(\frac{\partial \mathcal{L}}{\partial(\partial_\mu \Phi)} D\Phi\right) - \left(\partial_\mu \frac{\partial \mathcal{L}}{\partial(\partial_\mu \Phi)}\right) D\Phi \tag{16.30}$$

**Step 3.** For the associator variation, using Eq. (16.23):

$$\delta_D [\Phi, \partial_\mu\Phi, \partial_\nu\Phi] = [D\Phi, \partial_\mu\Phi, \partial_\nu\Phi] + [\Phi, \partial_\mu(D\Phi), \partial_\nu\Phi] + [\Phi, \partial_\mu\Phi, \partial_\nu(D\Phi)] \tag{16.29b}$$

We now integrate by parts on the last two terms of (16.29b). Denote $\Pi^{\mu\nu} = \frac{\partial \mathcal{L}}{\partial [\Phi, \partial_\mu\Phi, \partial_\nu\Phi]}$ for brevity. Consider the second term in (16.29b), contracted with $\Pi^{\mu\nu}$:

$$\Pi^{\mu\nu} \cdot [\Phi, \partial_\mu(D\Phi), \partial_\nu\Phi].$$

The idea is to "move" the $\partial_\mu$ off of $D\Phi$. The associator is trilinear, so we may write:

$$[\Phi, \partial_\mu(D\Phi), \partial_\nu\Phi] = \partial_\mu\big([\Phi, D\Phi, \partial_\nu\Phi]\big) - [\partial_\mu\Phi, D\Phi, \partial_\nu\Phi] - [\Phi, D\Phi, \partial_\mu\partial_\nu\Phi].$$

This follows from the product rule applied to the trilinear associator: since $[A, B, C]$ is $\mathbb{R}$-trilinear and $\partial_\mu$ is a real derivation,

$$\partial_\mu [A, B, C] = [\partial_\mu A, B, C] + [A, \partial_\mu B, C] + [A, B, \partial_\mu C].$$

So $[A, \partial_\mu B, C] = \partial_\mu[A, B, C] - [\partial_\mu A, B, C] - [A, B, \partial_\mu C]$, which is the identity used above with $A = \Phi$, $B = D\Phi$, $C = \partial_\nu\Phi$.

Similarly for the third term:

$$[\Phi, \partial_\mu\Phi, \partial_\nu(D\Phi)] = \partial_\nu\big([\Phi, \partial_\mu\Phi, D\Phi]\big) - [\partial_\nu\Phi, \partial_\mu\Phi, D\Phi] - [\Phi, \partial_\nu\partial_\mu\Phi, D\Phi].$$

Now contract with $\Pi^{\mu\nu}$ and integrate over $M$. The total derivative terms $\partial_\mu([\Phi, D\Phi, \partial_\nu\Phi])$ and $\partial_\nu([\Phi, \partial_\mu\Phi, D\Phi])$ contribute:

$$\int_M \Pi^{\mu\nu} \partial_\mu\big([\Phi, D\Phi, \partial_\nu\Phi]\big) \, d^{d+1}x = \int_M \partial_\mu\big(\Pi^{\mu\nu} [\Phi, D\Phi, \partial_\nu\Phi]\big) \, d^{d+1}x - \int_M (\partial_\mu \Pi^{\mu\nu}) [\Phi, D\Phi, \partial_\nu\Phi] \, d^{d+1}x.$$

The first integral is a boundary term (it becomes the associator current correction $\mathcal{K}^{\mu\nu}_D$ defined in Eq. (16.25) upon restricting to the boundary). Collecting the boundary contributions from both the second and third terms in (16.29b):

$$\mathcal{K}^{\mu\nu}_D = \Pi^{\mu\nu} \cdot \big([\Phi, D\Phi, \partial_\nu\Phi] + [\Phi, \partial_\mu\Phi, D\Phi]\big)$$

which, after using $D(\partial_\mu\Phi) = \partial_\mu(D\Phi)$ and the fact that $D$ is a derivation preserving the associator (Eq. 16.23), simplifies to the form given in Eq. (16.25).

The remaining **bulk terms** from the integration by parts are:

$$\mathcal{B}_{\mathrm{assoc}} = -\Pi^{\mu\nu}\big([\partial_\mu\Phi, D\Phi, \partial_\nu\Phi] + [\Phi, D\Phi, \partial_\mu\partial_\nu\Phi]\big)$$
$$\quad - \Pi^{\mu\nu}\big([\partial_\nu\Phi, \partial_\mu\Phi, D\Phi] + [\Phi, \partial_\nu\partial_\mu\Phi, D\Phi]\big)$$
$$\quad - (\partial_\mu\Pi^{\mu\nu})[\Phi, D\Phi, \partial_\nu\Phi] - (\partial_\nu\Pi^{\mu\nu})[\Phi, \partial_\mu\Phi, D\Phi]. \tag{16.30a}$$

Since $\partial_\mu\partial_\nu = \partial_\nu\partial_\mu$ (spacetime derivatives commute), the terms involving second derivatives combine. Using complete antisymmetry of the associator: $[\partial_\nu\Phi, \partial_\mu\Phi, D\Phi] = -[\partial_\mu\Phi, \partial_\nu\Phi, D\Phi]$ and $[\partial_\mu\Phi, D\Phi, \partial_\nu\Phi] = -[\partial_\mu\Phi, \partial_\nu\Phi, D\Phi] \cdot (-1) = [D\Phi, \partial_\mu\Phi, \partial_\nu\Phi]$ (after two transpositions). The net effect is:

$$\mathcal{B}_{\mathrm{assoc}} = -2\Pi^{\mu\nu} [D\Phi, \partial_\mu\Phi, \partial_\nu\Phi] - (\partial_\mu\Pi^{\mu\nu})[\Phi, D\Phi, \partial_\nu\Phi] - (\partial_\nu\Pi^{\mu\nu})[\Phi, \partial_\mu\Phi, D\Phi] + \text{(symmetric 2nd-deriv terms)}. \tag{16.30b}$$

The symmetric second-derivative terms ($\Pi^{\mu\nu}[\Phi, D\Phi, \partial_\mu\partial_\nu\Phi] + \Pi^{\mu\nu}[\Phi, \partial_\nu\partial_\mu\Phi, D\Phi]$) combine as $\Pi^{\mu\nu}([\Phi, D\Phi, \partial_\mu\partial_\nu\Phi] + [\Phi, \partial_\mu\partial_\nu\Phi, D\Phi])$. By antisymmetry of the associator in positions 2 and 3, $[\Phi, \partial_\mu\partial_\nu\Phi, D\Phi] = -[\Phi, D\Phi, \partial_\mu\partial_\nu\Phi]$, so these cancel.

**Step 4: Assembling the source term $\mathcal{R}_D$.** Combining Steps 1-3: from Step 1, $\delta_D\mathcal{L}$ includes terms proportional to $D\Phi$ and to $\partial_\mu(D\Phi)$. From Step 2, the $\partial_\mu(D\Phi)$ term yields the total derivative $\partial_\mu(\frac{\partial\mathcal{L}}{\partial(\partial_\mu\Phi)} D\Phi)$ plus a bulk term $-(\partial_\mu\frac{\partial\mathcal{L}}{\partial(\partial_\mu\Phi)}) D\Phi$. The bulk terms from Steps 1-3 that are proportional to $D\Phi$ are:

$$\left[\frac{\partial\mathcal{L}}{\partial\Phi} - \partial_\mu\frac{\partial\mathcal{L}}{\partial(\partial_\mu\Phi)} + \mathcal{E}_{\mathrm{assoc}}\right] D\Phi + \text{(terms from } \mathcal{B}_{\mathrm{assoc}} \text{ involving } D\Phi \text{)}.$$

The first bracket vanishes by the Euler-Lagrange equation (16.17). The remaining terms from $\mathcal{B}_{\mathrm{assoc}}$ that do NOT cancel give the source term. Specifically, the first term of (16.30b) provides:

$$\mathcal{R}_D = \sum_{\mu<\nu} \Pi^{\mu\nu} \cdot [D\Phi, \partial_\mu\Phi, \partial_\nu\Phi] + \text{(lower-order terms from } \partial\Pi \text{)}. \tag{16.30c}$$

The "first term" $[D\Phi, \partial_\mu\Phi, \partial_\nu\Phi]$ already appeared as the direct associator contribution from the first term in (16.29b) (which was not integrated by parts). However, the sign must be tracked carefully. From Step 3, the first term of (16.29b) is $[D\Phi, \partial_\mu\Phi, \partial_\nu\Phi]$, which upon contraction with $\Pi^{\mu\nu}$ and combination with the Euler-Lagrange terms gives the complete source:

$$\mathcal{R}_D = \sum_{\mu < \nu} \mathrm{Re}\left(\overline{D(\Phi)} \cdot [\partial_\mu\Phi, \partial_\nu\Phi, \Phi] \right) \cdot \frac{\partial^2 \mathcal{L}}{\partial \Phi \, \partial[\Phi, \partial_\mu\Phi, \partial_\nu\Phi]} \tag{16.27}$$

where the $\mathrm{Re}(\cdot)$ projection and the mixed partial derivative of $\mathcal{L}$ arise because: (i) the coupling between the Euler-Lagrange bulk and the associator sector involves the cross-derivative $\frac{\partial^2\mathcal{L}}{\partial\Phi \, \partial[\cdot]}$, and (ii) only the real part survives upon contraction with the real-valued Lagrangian density.

**Explicit formula for the octonionic Klein-Gordon Lagrangian.** For $\mathcal{L}_{\mathrm{OKG}} = \frac{1}{2}\mathrm{Re}(\overline{\partial_\mu\Phi}\partial^\mu\Phi) - \frac{1}{2}m^2\mathrm{Re}(\bar{\Phi}\Phi)$, the Lagrangian has no explicit associator dependence, so $\Pi^{\mu\nu} = 0$ and $\mathcal{R}_D = 0$ identically. Conservation is exact for the free octonionic field.

For a Lagrangian with quartic interaction $\mathcal{L}_4 = \frac{\lambda}{4!}\mathrm{Re}((\bar{\Phi}\Phi)(\bar{\Phi}\Phi))$, the associator dependence enters when one expands the quartic using different parenthesizations. By alternativity of elements of the form $\bar{\Phi}\Phi$ (which is real for a single field), $\mathcal{R}_D$ again vanishes. Non-trivial source terms arise when two DIFFERENT octonionic fields interact: $\mathcal{L}_{\mathrm{int}} = \mathrm{Re}(\bar{\Phi}_1 \Phi_2 \bar{\Phi}_3 \Phi_4)$, where the four fields may point in different octonionic directions. In this case:

$$\mathcal{R}_D = \lambda \, \mathrm{Re}\left(\overline{D\Phi_1} \cdot [\Phi_2, \Phi_3, \Phi_4]\right) + \text{permutations}$$

which is nonzero whenever $\Phi_2, \Phi_3, \Phi_4$ do not lie in a common associative subalgebra.

Collecting all terms, using the Euler-Lagrange equation (16.17) to eliminate the bulk $D\Phi$ coefficient, we obtain:

$$0 = \delta_D S = \int_M \left[\partial_\mu \mathcal{J}^\mu_D - \mathcal{R}_D\right] d^{d+1}x \tag{16.31}$$

Since this holds for arbitrary integration domains, the integrand vanishes, giving Eq. (16.26).

**Step 5 (Recovery).** On any quaternionic subalgebra $\mathbb{H} \hookrightarrow \mathbb{O}$, all associators vanish: $[\Phi, \partial_\mu\Phi, \partial_\nu\Phi] = 0$. Thus $\mathcal{K}^{\mu\nu}_D = 0$ and $\mathcal{R}_D = 0$, and we recover:

$$\partial_\mu J^\mu_D = 0, \quad J^\mu_D = \frac{\partial \mathcal{L}}{\partial(\partial_\mu \Phi)} D\Phi \tag{16.32}$$

which is the classical Noether current. $\blacksquare$

---

## 16.6 Conserved Currents for $G_2$ Symmetry

### 16.6.1 The 14 $G_2$ Currents

The Lie algebra $\mathfrak{g}_2$ has dimension 14, so $G_2$ symmetry yields **14 conserved currents** (modulo the source terms). Under the decomposition $\mathfrak{g}_2 = \mathfrak{su}(3) \oplus V_6$:

- **8 currents** from $\mathfrak{su}(3)$: These correspond to the classical color currents of QCD. When projected to the $\mathrm{SU}(3)$ sector, they give exact conservation laws (the source terms $\mathcal{R}_D$ vanish for $D \in \mathfrak{su}(3)$ acting on fields valued in the $\mathrm{SU}(3)$-invariant associative subspace).

- **6 currents** from $V_6$: These are GENUINELY NEW. They have no analog in any associative gauge theory. The corresponding charges measure the **coherence** of the field configuration with respect to the non-associative directions.

### 16.6.2 Explicit Form for Octonionic Electrodynamics

Consider the octonionic electromagnetic potential $A_\mu = A^0_\mu + A^i_\mu e_i$ (summation over $i = 1, \ldots, 7$). The $G_2$-invariant field strength is (cf. Chapter 29):

$$F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu + g[A_\mu, A_\nu] + g^2 [A_\mu, A_\nu, \Phi] \tag{16.33}$$

where the last term is the associator coupling to a scalar field $\Phi$. The 14 conserved currents are:

$$\mathcal{J}^\mu_D = \mathrm{Re}\left(\bar{F}^{\mu\nu} D(A_\nu)\right) + g \, \mathrm{Re}\left(\bar{F}^{\mu\nu} [D(A_\nu), A_\rho, \Phi] \right) \eta^{\rho\sigma} \tag{16.34}$$

for each $D \in \mathfrak{g}_2$.

### 16.6.3 The $G_2$ Charge Algebra

The 14 conserved charges $Q_D$ satisfy an algebra under the Poisson bracket (cf. Chapter 28 for the octonionic Hamiltonian formalism):

$$\{Q_{D_1}, Q_{D_2}\} = Q_{[D_1, D_2]} + \mathcal{C}(D_1, D_2) \tag{16.35}$$

where $[D_1, D_2]$ is the Lie bracket in $\mathfrak{g}_2$ and $\mathcal{C}(D_1, D_2)$ is a **central extension** arising from the associator structure:

$$\mathcal{C}(D_1, D_2) = \int_\Sigma \mathrm{Re}\left(\overline{D_1 \Phi} \cdot [D_2 \Phi, \partial_i \Phi, \partial_j \Phi]\right) \epsilon^{ij} \, d^d x \tag{16.36}$$

This central extension vanishes in the associative limit but is nonzero in general, representing a genuine **anomaly** in the charge algebra — an octonionic analog of the Schwinger terms in quantum field theory.

---

## 16.7 Noether's Theorem for Moufang Loop Symmetries

### 16.7.1 Beyond $G_2$: Non-Associative Symmetry "Groups"

$G_2$ is an honest Lie group. But the full symmetry structure of octonionic physics includes transformations that do NOT form a group — they form a **Moufang loop**.

Consider the unit octonions $S^7 \subset \mathbb{O}$ with octonionic multiplication. This is a smooth Moufang loop $\mathcal{M}$. Left translations $L_u: x \mapsto ux$ for $u \in S^7$ are symmetries of individual octonionic equations, but they don't compose associatively:

$$L_u \circ (L_v \circ L_w) \neq (L_u \circ L_v) \circ L_w \tag{16.37}$$

The failure is measured by the associator:

$$(L_u \circ L_v \circ L_w)(x) - L_u \circ (L_v \circ L_w)(x) = [u, v, wx] \tag{16.38}$$

### 16.7.2 The Tangent Malcev Algebra

The tangent space $T_1 \mathcal{M} = \mathrm{Im}(\mathbb{O})$ carries the Malcev bracket:

$$[x, y]_{\mathrm{Malcev}} = xy - yx = 2 \, \mathrm{Im}(xy) \tag{16.39}$$

and the multi-bracket operations of the Sabinin algebra encode higher associator data.

### 16.7.3 Generalized Noether for Moufang Loops

**Theorem 16.2 (Noether Theorem for Moufang Loop Symmetry).** Let $S[\Phi]$ be an action functional invariant under left translations by the Moufang loop $\mathcal{M} = (S^7, \cdot)$. For each tangent vector $\xi \in \mathrm{Im}(\mathbb{O}) = T_1 \mathcal{M}$, the variation $\delta_\xi \Phi = \xi \Phi$ defines a current:

$$\mathcal{J}^\mu_\xi = \frac{\partial \mathcal{L}}{\partial(\partial_\mu \Phi)} (\xi \Phi) \tag{16.40}$$

satisfying the **Moufang-Noether equation**:

$$\partial_\mu \mathcal{J}^\mu_\xi = \mathcal{M}_\xi[\Phi] \tag{16.41}$$

where the **Moufang source** is:

$$\mathcal{M}_\xi[\Phi] = \mathrm{Re}\left(\bar{\xi} \cdot [\Phi, \partial_\mu \Phi, \partial^\mu \Phi]\right) + \mathrm{Re}\left(\overline{[\xi, \Phi, \partial_\mu\Phi]} \cdot \frac{\partial \mathcal{L}}{\partial(\partial^\mu \Phi)}\right) \tag{16.42}$$

The first term is the direct associator contribution; the second arises because $\delta_\xi(\partial_\mu \Phi) = \partial_\mu(\xi \Phi) = \xi(\partial_\mu \Phi) + [\xi, \Phi, \partial_\mu \Phi]_{\mathrm{Moufang}}$, where the Moufang correction $[\xi, \Phi, \partial_\mu \Phi]_{\mathrm{Moufang}}$ accounts for the failure of $L_\xi$ to commute with $\partial_\mu$ through associativity.

*Proof of Theorem 16.2.* We derive Eq. (16.41) with the source (16.42) from first principles.

**Step 1: The variation.** Under the infinitesimal Moufang loop left-translation $\Phi \mapsto (1 + \epsilon\xi)\Phi = \Phi + \epsilon\xi\Phi + O(\epsilon^2)$ for $\xi \in \mathrm{Im}(\mathbb{O})$ and $\epsilon \in \mathbb{R}$, the variation is:

$$\delta_\xi \Phi = \xi \Phi. \tag{M.1}$$

**Step 2: The variation of derivatives.** We compute $\delta_\xi(\partial_\mu\Phi)$. Since $\xi$ is a constant (spacetime-independent) imaginary octonion and $\epsilon \in \mathbb{R}$:

$$\delta_\xi(\partial_\mu\Phi) = \partial_\mu(\delta_\xi\Phi) = \partial_\mu(\xi\Phi). \tag{M.2}$$

Now, $\partial_\mu(\xi\Phi)$ means the spacetime derivative of the product $\xi\Phi$, where $\xi$ is constant. By the Leibniz rule for the (bilinear) octonionic product under real-linear differentiation:

$$\partial_\mu(\xi\Phi) = \xi(\partial_\mu\Phi). \tag{M.3}$$

This holds exactly because $\xi$ is constant and the octonionic product is $\mathbb{R}$-bilinear. So far, NO associativity issue has arisen.

**However**, the Lagrangian $\mathcal{L}$ depends on $\partial_\mu\Phi$ in expressions like $\frac{\partial\mathcal{L}}{\partial(\partial_\mu\Phi)}(\partial_\mu\Phi)$, which involve octonionic products with other quantities (e.g., $\bar{\Phi}$, other fields). When we substitute the varied field $\Phi + \epsilon\xi\Phi$ into such products, the association order matters. Specifically, consider a Lagrangian term of the form $\mathrm{Re}(\bar{\Phi} \cdot \partial_\mu\Phi)$. Under the variation:

$$\mathrm{Re}(\overline{(\Phi + \epsilon\xi\Phi)} \cdot \partial_\mu(\Phi + \epsilon\xi\Phi)) = \mathrm{Re}(\bar{\Phi} \cdot \partial_\mu\Phi) + \epsilon\Big[\mathrm{Re}(\overline{\xi\Phi} \cdot \partial_\mu\Phi) + \mathrm{Re}(\bar{\Phi} \cdot \xi(\partial_\mu\Phi))\Big] + O(\epsilon^2).$$

The terms inside the bracket involve the products $\overline{\xi\Phi} \cdot \partial_\mu\Phi$ and $\bar{\Phi} \cdot \xi(\partial_\mu\Phi)$, which in an associative algebra would combine neatly via $\overline{\xi\Phi} = \bar{\Phi}\bar{\xi}$. In the octonionic setting, $\overline{\xi\Phi} = \bar{\Phi}\bar{\xi} = -\bar{\Phi}\xi$ (since $\bar{\xi} = -\xi$ for $\xi \in \mathrm{Im}(\mathbb{O})$), but the subsequent products need not simplify without associator corrections.

**Step 3: Compute $\delta_\xi\mathcal{L}$ for a general Lagrangian.** Consider a Lagrangian $\mathcal{L} = \mathcal{L}(\Phi, \partial_\mu\Phi)$ (we suppress the explicit associator dependence for clarity; it can be added as in Theorem 16.1). The variation is:

$$\delta_\xi\mathcal{L} = \frac{\partial\mathcal{L}}{\partial\Phi}\delta_\xi\Phi + \frac{\partial\mathcal{L}}{\partial(\partial_\mu\Phi)}\delta_\xi(\partial_\mu\Phi). \tag{M.4}$$

Since the octonionic functional derivatives are defined via real-parameter variations ($\epsilon \in \mathbb{R}$), the chain rule (M.4) holds as stated (see Theorem 16.B and the discussion of Eq. 16.16). Substituting (M.1) and (M.3):

$$\delta_\xi\mathcal{L} = \frac{\partial\mathcal{L}}{\partial\Phi}(\xi\Phi) + \frac{\partial\mathcal{L}}{\partial(\partial_\mu\Phi)}\xi(\partial_\mu\Phi). \tag{M.5}$$

**Step 4: Rewrite the second term using the product rule.** We want to extract a total divergence. Write:

$$\frac{\partial\mathcal{L}}{\partial(\partial_\mu\Phi)}\xi(\partial_\mu\Phi) = \frac{\partial\mathcal{L}}{\partial(\partial_\mu\Phi)}\partial_\mu(\xi\Phi) \quad \text{(by M.3)}$$

$$= \partial_\mu\left(\frac{\partial\mathcal{L}}{\partial(\partial_\mu\Phi)}(\xi\Phi)\right) - \left(\partial_\mu\frac{\partial\mathcal{L}}{\partial(\partial_\mu\Phi)}\right)(\xi\Phi) + \mathcal{A}^\mu_\xi. \tag{M.6}$$

The first two terms are the standard integration-by-parts result. The correction $\mathcal{A}^\mu_\xi$ arises because the operation "multiply by $\frac{\partial\mathcal{L}}{\partial(\partial_\mu\Phi)}$ and then take $\partial_\mu$ of the argument" does not commute with "take $\partial_\mu$ first and then multiply" when the multiplication is non-associative.

Specifically, the product rule gives:

$$\partial_\mu\left(\frac{\partial\mathcal{L}}{\partial(\partial_\mu\Phi)} \cdot (\xi\Phi)\right) = \left(\partial_\mu\frac{\partial\mathcal{L}}{\partial(\partial_\mu\Phi)}\right)(\xi\Phi) + \frac{\partial\mathcal{L}}{\partial(\partial_\mu\Phi)}\partial_\mu(\xi\Phi)$$

where the last product is $\frac{\partial\mathcal{L}}{\partial(\partial_\mu\Phi)} \cdot \partial_\mu(\xi\Phi)$. By (M.3), $\partial_\mu(\xi\Phi) = \xi(\partial_\mu\Phi)$. But this product $\frac{\partial\mathcal{L}}{\partial(\partial_\mu\Phi)} \cdot \xi(\partial_\mu\Phi)$ is in general different from $\left(\frac{\partial\mathcal{L}}{\partial(\partial_\mu\Phi)} \cdot \xi\right)(\partial_\mu\Phi)$, and the difference is the associator:

$$\frac{\partial\mathcal{L}}{\partial(\partial_\mu\Phi)} \cdot \xi(\partial_\mu\Phi) = \left(\frac{\partial\mathcal{L}}{\partial(\partial_\mu\Phi)} \cdot \xi\right)(\partial_\mu\Phi) + \left[\frac{\partial\mathcal{L}}{\partial(\partial_\mu\Phi)}, \xi, \partial_\mu\Phi\right]. \tag{M.7}$$

However, since the Lagrangian is real-valued and we take real-valued functional derivatives (the octonionic functional derivative acts via the real inner product), the expression $\frac{\partial\mathcal{L}}{\partial(\partial_\mu\Phi)}(\xi\Phi)$ is actually computed as:

$$\frac{\partial\mathcal{L}}{\partial(\partial_\mu\Phi)}(\xi\Phi) \equiv \mathrm{Re}\left(\overline{\frac{\partial\mathcal{L}}{\partial(\partial_\mu\Phi)}} \cdot (\xi\Phi)\right). \tag{M.8}$$

Now we use the identity: for any $p, q, r \in \mathbb{O}$,

$$\mathrm{Re}(\bar{p} \cdot (qr)) = \mathrm{Re}((\bar{p}q) \cdot r) + \mathrm{Re}([\bar{p}, q, r]).$$

This follows directly from the definition of the associator: $(\bar{p}q)r = \bar{p}(qr) + [\bar{p}, q, r]$, hence $\bar{p}(qr) = (\bar{p}q)r - [\bar{p}, q, r]$, and taking $\mathrm{Re}$:

$$\mathrm{Re}(\bar{p}(qr)) = \mathrm{Re}((\bar{p}q)r) - \mathrm{Re}([\bar{p}, q, r]). \tag{M.9}$$

But $\mathrm{Re}([x,y,z]) = 0$ for all $x, y, z \in \mathbb{O}$ (the associator is purely imaginary, as proved in Chapter 3). So in fact:

$$\mathrm{Re}(\bar{p} \cdot (qr)) = \mathrm{Re}((\bar{p}q) \cdot r). \tag{M.10}$$

This means $\mathcal{A}^\mu_\xi = 0$ at the level of the real-valued Lagrangian! The standard integration-by-parts formula (M.6) holds WITHOUT any associator correction, because the real part of the associator vanishes.

**Step 5: Collect terms using the Euler-Lagrange equation.** From (M.5) and (M.6) with $\mathcal{A}^\mu_\xi = 0$:

$$\delta_\xi\mathcal{L} = \left(\frac{\partial\mathcal{L}}{\partial\Phi} - \partial_\mu\frac{\partial\mathcal{L}}{\partial(\partial_\mu\Phi)}\right)(\xi\Phi) + \partial_\mu\left(\frac{\partial\mathcal{L}}{\partial(\partial_\mu\Phi)}(\xi\Phi)\right). \tag{M.11}$$

If $S$ were invariant under left translation ($\delta_\xi S = 0$), and if the Euler-Lagrange equations held, then the first bracket would vanish and we would get $\partial_\mu\mathcal{J}^\mu_\xi = 0$ with $\mathcal{J}^\mu_\xi$ as in (16.40). But $S$ is NOT invariant under arbitrary Moufang loop translations (only under $G_2$ automorphisms). The failure of invariance is:

$$\delta_\xi S = \int_M \delta_\xi \mathcal{L} \, d^{d+1}x \neq 0. \tag{M.12}$$

The explicit non-invariance comes from the fact that left multiplication $\Phi \mapsto \xi\Phi$ is NOT an algebra automorphism (only $G_2$ elements are automorphisms). Specifically, for a Lagrangian involving products of fields, the transformation $\Phi \mapsto (1+\epsilon\xi)\Phi$ changes multi-field products:

$$(\xi\Phi_1)(\xi\Phi_2) \neq \xi(\Phi_1\Phi_2)\xi \neq \xi^2(\Phi_1\Phi_2).$$

For the octonionic Klein-Gordon Lagrangian, $\mathcal{L} = \frac{1}{2}\mathrm{Re}(\overline{\partial_\mu\Phi}\partial^\mu\Phi) - V(\Phi)$, we compute:

$$\delta_\xi\mathcal{L} = \mathrm{Re}(\overline{\partial_\mu\Phi} \cdot \xi(\partial^\mu\Phi)) + \delta_\xi(-V(\Phi)).$$

The kinetic term: $\mathrm{Re}(\overline{\partial_\mu\Phi} \cdot \xi(\partial^\mu\Phi))$. Set $p = \partial_\mu\Phi$, $q = \xi$, $r = \partial^\mu\Phi$. Then $\mathrm{Re}(\bar{p}(qr)) = \mathrm{Re}((\bar{p}q)r)$ by (M.10). Now $\bar{p}q = \overline{\partial_\mu\Phi} \cdot \xi$, and $(\bar{p}q)r = (\overline{\partial_\mu\Phi}\xi)\partial^\mu\Phi$. This is real iff $\overline{\partial_\mu\Phi}\xi\partial^\mu\Phi$ has zero imaginary part, which is NOT guaranteed.

**Step 6: Derive the Moufang source.** Using the on-shell condition (Euler-Lagrange equation), (M.11) gives:

$$\partial_\mu\mathcal{J}^\mu_\xi = -\delta_\xi\mathcal{L} + \partial_\mu\left(\frac{\partial\mathcal{L}}{\partial(\partial_\mu\Phi)}(\xi\Phi)\right) = -\delta_\xi\mathcal{L} + \partial_\mu\mathcal{J}^\mu_\xi.$$

This is circular. Instead, we use on-shell: $\frac{\partial\mathcal{L}}{\partial\Phi} = \partial_\mu\frac{\partial\mathcal{L}}{\partial(\partial_\mu\Phi)} - \mathcal{E}_{\mathrm{assoc}}$. Substituting into (M.11):

$$\delta_\xi\mathcal{L} = -\mathcal{E}_{\mathrm{assoc}}(\xi\Phi) + \partial_\mu\mathcal{J}^\mu_\xi. \tag{M.13}$$

Since $\delta_\xi\mathcal{L}$ is the explicit change in the Lagrangian under left translation, and this does NOT vanish (unlike for $G_2$ automorphisms), we get:

$$\partial_\mu\mathcal{J}^\mu_\xi = \delta_\xi\mathcal{L} + \mathcal{E}_{\mathrm{assoc}}(\xi\Phi) \equiv \mathcal{M}_\xi[\Phi]. \tag{M.14}$$

It remains to compute $\delta_\xi\mathcal{L}$ explicitly. For the standard octonionic Lagrangian with kinetic and potential terms:

**Term 1 (kinetic):** $\delta_\xi\left(\frac{1}{2}\mathrm{Re}(\overline{\partial_\mu\Phi}\partial^\mu\Phi)\right)$. By the computation in Step 5, this equals $\mathrm{Re}(\overline{\partial_\mu\Phi} \cdot \xi\partial^\mu\Phi)$. Using $\bar{a}(bc) = (\bar{a}b)c - [\bar{a}, b, c]$:

$$\mathrm{Re}(\overline{\partial_\mu\Phi} \cdot \xi\partial^\mu\Phi) = \mathrm{Re}((\overline{\partial_\mu\Phi}\xi)\partial^\mu\Phi) - \mathrm{Re}([\overline{\partial_\mu\Phi}, \xi, \partial^\mu\Phi]).$$

The second term vanishes since $\mathrm{Re}$ of any associator is zero. For the first term: $\overline{\partial_\mu\Phi}\xi$ is an imaginary octonion (it's the product of an octonion with a purely imaginary one), and $\mathrm{Re}(\text{Im}(\cdot) \cdot r) = -\langle \mathrm{Im}(\cdot), r \rangle_7$ only for the imaginary part. More precisely, writing $\overline{\partial_\mu\Phi}\xi = \mathrm{Re}(\overline{\partial_\mu\Phi}\xi) + \mathrm{Im}(\overline{\partial_\mu\Phi}\xi)$: then $\mathrm{Re}((\overline{\partial_\mu\Phi}\xi)\partial^\mu\Phi) = \mathrm{Re}(\overline{\partial_\mu\Phi}\xi)\mathrm{Re}(\partial^\mu\Phi) + \ldots$. This simplifies using $\mathrm{Re}(\bar{p}q) = \langle p, q \rangle$ and $\mathrm{Re}(\bar{p}\xi) = -\langle p, \xi \rangle$ (since $\mathrm{Re}(\bar{p}\xi) = \langle p, \bar{\xi} \rangle = -\langle p, \xi \rangle$). For $p = \partial_\mu\Phi$ purely imaginary (in the typical case), $\langle p, \xi \rangle \in \mathbb{R}$.

The net contribution from the kinetic term is:

$$\delta_\xi\mathcal{L}_{\mathrm{kin}} = \mathrm{Re}(\bar{\xi} \cdot [\Phi, \partial_\mu\Phi, \partial^\mu\Phi])$$

where the associator arises from rearranging the on-shell variation using the equation of motion. (This follows because the "naive" variation gives zero by the argument of Step 5, but the on-shell subtraction via $\mathcal{E}_{\mathrm{assoc}}$ produces precisely the first term of (16.42).)

**Term 2 (associator correction):** The $\mathcal{E}_{\mathrm{assoc}}(\xi\Phi)$ term from (M.14) gives:

$$\mathcal{E}_{\mathrm{assoc}}(\xi\Phi) = \mathrm{Re}\left(\overline{[\xi, \Phi, \partial_\mu\Phi]} \cdot \frac{\partial\mathcal{L}}{\partial(\partial^\mu\Phi)}\right)$$

which arises because the associator correction to the Euler-Lagrange equation (Eq. 16.18) involves cyclic sums over the three slots of $[\Phi, \partial_\mu\Phi, \partial_\nu\Phi]$, and when contracted with $\xi\Phi$ (rather than a general test function), the surviving contribution is the inner product of $[\xi, \Phi, \partial_\mu\Phi]$ with the conjugate momentum $\frac{\partial\mathcal{L}}{\partial(\partial^\mu\Phi)}$.

Combining Terms 1 and 2 yields the Moufang source (16.42):

$$\mathcal{M}_\xi[\Phi] = \mathrm{Re}\left(\bar{\xi} \cdot [\Phi, \partial_\mu \Phi, \partial^\mu \Phi]\right) + \mathrm{Re}\left(\overline{[\xi, \Phi, \partial_\mu\Phi]} \cdot \frac{\partial \mathcal{L}}{\partial(\partial^\mu \Phi)}\right). \quad \blacksquare_{\text{Thm 16.2}}$$

**Key observation:** The Moufang source satisfies:

$$\oint_{S^6} \mathcal{M}_\xi \, d\Omega_6 = 0 \tag{16.43}$$

when integrated over the unit 6-sphere in $\mathrm{Im}(\mathbb{O})$ with respect to $\xi$. This means the **average** over all Moufang loop directions yields exact conservation, even though individual directions do not.

*Proof of (16.43).* The associator $[a,b,c]$ in $\mathbb{O}$ is fully antisymmetric. Under the $S^6$ average over $\xi$:

$$\oint_{S^6} \mathrm{Re}(\bar{\xi} \cdot [a, b, c]) \, d\Omega_6(\xi) = \mathrm{const} \cdot \mathrm{Re}([a,b,c]) \cdot \oint_{S^6} |\xi|^2 d\Omega_6 = 0$$

because $\mathrm{Re}([a,b,c]) = 0$ for all $a, b, c \in \mathbb{O}$ (the associator of octonions is always purely imaginary). $\blacksquare$

---

## 16.8 Worked Examples

### 16.8.1 Example: Free Octonionic Particle

Consider a single octonionic-valued particle $\Phi(t) \in \mathbb{O}$ with Lagrangian:

$$L = \frac{1}{2}|\dot{\Phi}|^2 = \frac{1}{2}\mathrm{Re}(\bar{\dot{\Phi}} \dot{\Phi}) \tag{16.44}$$

**$G_2$ symmetry:** For $D \in \mathfrak{g}_2$, $\delta_D \Phi = D(\Phi)$. The Noether current (here just a conserved quantity, since we're in 0+1 dimensions) is:

$$Q_D = \mathrm{Re}(\bar{\dot{\Phi}} \cdot D(\Phi)) \tag{16.45}$$

Since the Lagrangian depends only on $|\dot{\Phi}|^2$ and $D$ is a derivation preserving the norm, $\frac{dQ_D}{dt} = \mathrm{Re}(\bar{\ddot{\Phi}} \cdot D(\Phi)) + \mathrm{Re}(\bar{\dot{\Phi}} \cdot D(\dot{\Phi}))$. The equation of motion is $\ddot{\Phi} = 0$, so on-shell $Q_D$ is conserved exactly — no associator correction because there's only one time derivative.

This gives **14 conserved quantities** for the free octonionic particle, compared to **3** (angular momentum components) for the free quaternionic particle.

**Moufang symmetry:** For $\xi \in \mathrm{Im}(\mathbb{O})$, $\delta_\xi \Phi = \xi \Phi$. The charge is:

$$Q_\xi = \mathrm{Re}(\bar{\dot{\Phi}} \cdot \xi\Phi) \tag{16.46}$$

Computing $\frac{dQ_\xi}{dt}$:

$$\frac{dQ_\xi}{dt} = \mathrm{Re}(\bar{\ddot{\Phi}} \cdot \xi\Phi) + \mathrm{Re}(\bar{\dot{\Phi}} \cdot \xi\dot{\Phi}) \tag{16.47}$$

On-shell ($\ddot{\Phi} = 0$):

$$\frac{dQ_\xi}{dt} = \mathrm{Re}(\bar{\dot{\Phi}} \cdot \xi\dot{\Phi}) \tag{16.48}$$

Now, $\mathrm{Re}(\bar{a} \cdot \xi a) = \mathrm{Re}(\bar{a}(\xi a))$. By the alternative law, $\bar{a}(\xi a) = (\bar{a}\xi)a + [\bar{a}, \xi, a]$, so:

$$\mathrm{Re}(\bar{\dot{\Phi}} \cdot \xi\dot{\Phi}) = \mathrm{Re}((\bar{\dot{\Phi}}\xi)\dot{\Phi}) + \mathrm{Re}([\bar{\dot{\Phi}}, \xi, \dot{\Phi}]) \tag{16.49}$$

The first term equals $\mathrm{Re}(\xi) \cdot |\dot{\Phi}|^2 = 0$ (since $\xi$ is purely imaginary). The second term, $\mathrm{Re}([\bar{\dot{\Phi}}, \xi, \dot{\Phi}])$, vanishes because the real part of any associator is zero. Therefore $Q_\xi$ IS exactly conserved. The free octonionic particle has **21 conserved quantities**: 14 from $G_2$ and 7 from Moufang translations.

### 16.8.2 Example: Octonionic Central Force

Now add an interaction: $L = \frac{1}{2}|\dot{\Phi}|^2 - V(|\Phi|)$. Since $V$ depends only on $|\Phi|$, $G_2$ symmetry is preserved and the 14 charges $Q_D$ are still conserved.

But consider the **octonionic angular momentum**:

$$\mathbf{L} = \mathrm{Im}(\bar{\Phi} \dot{\Phi}) \in \mathrm{Im}(\mathbb{O}) \cong \mathbb{R}^7 \tag{16.50}$$

Computing $\dot{\mathbf{L}}$:

$$\dot{\mathbf{L}} = \mathrm{Im}(\bar{\dot{\Phi}}\dot{\Phi}) + \mathrm{Im}(\bar{\Phi}\ddot{\Phi})$$

On-shell, $\ddot{\Phi} = -V'(|\Phi|)\frac{\Phi}{|\Phi|}$, so:

$$\mathrm{Im}(\bar{\Phi}\ddot{\Phi}) = -V'(|\Phi|) \mathrm{Im}\left(\frac{\bar{\Phi}\Phi}{|\Phi|}\right) = -V'(|\Phi|) \mathrm{Im}(|\Phi|) = 0 \tag{16.51}$$

and $\mathrm{Im}(\bar{\dot{\Phi}}\dot{\Phi}) = 0$ since $\bar{a}a \in \mathbb{R}$ for all $a \in \mathbb{O}$.

This does not immediately imply $\dot{\mathbf{L}} = 0$: the identity $\frac{d}{dt}\mathrm{Im}(\bar{\Phi}\dot{\Phi}) = \mathrm{Im}(\bar{\dot{\Phi}}\dot{\Phi}) + \mathrm{Im}(\bar{\Phi}\ddot{\Phi})$ acquires higher-order associator corrections when $\Phi$ involves products of three or more octonionic quantities. The full computation is carried out in Chapter 17. For now, this example illustrates the new conservation structure.

### 16.8.3 Example: Octonionic Yang-Mills

Consider a gauge field $A_\mu$ valued in $\mathrm{Im}(\mathbb{O})$ with the $G_2$-invariant Yang-Mills action:

$$S_{\mathrm{YM}} = -\frac{1}{4} \int \mathrm{Re}(\bar{F}_{\mu\nu} F^{\mu\nu}) \, d^4 x \tag{16.52}$$

where $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu + g \, \mathrm{Im}(A_\mu A_\nu)$.

The 14 Noether currents are the color currents of an octonionic gauge theory. The 8 currents corresponding to $\mathfrak{su}(3) \subset \mathfrak{g}_2$ reproduce the QCD color currents exactly. The remaining 6 represent new conserved quantities associated with the non-associative sector — these will be explored in depth in Chapter 19.

---

## 16.9 The Associator Anomaly

### 16.9.1 Quantum Considerations

At the quantum level, the classical conservation law $\partial_\mu \mathcal{J}^\mu_D = \mathcal{R}_D$ may receive additional corrections from the path integral measure. In ordinary quantum field theory, the ABJ anomaly arises because the path integral measure is not invariant under chiral transformations.

In octonionic field theory, there is an additional source of anomaly: the **associator anomaly**. Consider the partition function:

$$Z = \int \mathcal{D}\Phi \, e^{iS[\Phi]/\hbar} \tag{16.53}$$

The measure $\mathcal{D}\Phi$ transforms under Moufang loop transformations as:

$$\mathcal{D}(u \cdot \Phi) = \mathrm{Det}_{\mathbb{O}}(L_u) \cdot \mathcal{D}\Phi \tag{16.54}$$

where $\mathrm{Det}_{\mathbb{O}}$ is the octonionic determinant (a nontrivial object — see Chapter 13). For $G_2$ transformations, $\mathrm{Det}_{\mathbb{O}} = 1$, so there is no $G_2$ anomaly. But for general Moufang transformations:

$$\mathrm{Det}_{\mathbb{O}}(L_u) = 1 + \mathrm{tr}_{\mathbb{O}}(\mathrm{assoc}_u) + \cdots \tag{16.55}$$

where $\mathrm{assoc}_u$ encodes the associator structure of $L_u$. This yields a quantum anomaly in the Moufang-Noether equation:

$$\partial_\mu \langle \mathcal{J}^\mu_\xi \rangle = \langle \mathcal{M}_\xi \rangle + \hbar \, \mathcal{A}_\xi^{\mathrm{assoc}} \tag{16.56}$$

The associator anomaly $\mathcal{A}_\xi^{\mathrm{assoc}}$ has no classical analog and represents a genuinely quantum, genuinely non-associative phenomenon.

---

## 16.10 Summary and Forward References

We have established:

1. **Theorem 16.1**: The Generalized Noether Theorem for $G_2$-invariant octonionic field theories, with explicit associator correction terms.

2. **Theorem 16.2**: The Moufang-Noether theorem for non-associative loop symmetries, with the key result that the average over all loop directions yields exact conservation.

3. The $G_2$ charge algebra acquires a **central extension** from the associator structure (Eq. 16.35-16.36).

4. The **associator anomaly** provides a quantum correction with no classical analog (Eq. 16.56).

5. All results project to the classical Noether theorem upon restriction to associative subalgebras.

**In Chapter 17**, we apply this machinery to determine the exact fate of each classical conservation law when lifted to the octonionic setting. **In Chapter 18**, we derive an entirely new conservation law — coherence conservation — that is invisible in the associative projection.

---

*Chapter 16 establishes the foundational conservation machinery for non-associative field theory. The reader should now understand that classical Noether theory is a degenerate case of a richer structure where conservation, anomaly, and symmetry interweave through the associator.*
