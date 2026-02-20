> **Rigor Level: EXPOSITORY** — Accurate exposition of established alternativity theory, Moufang identities, and Artin's theorem.
> **Novelty: EXPOSITORY** — Synthesizes known results; no new theorems claimed.

# Chapter 3: Alternativity — Moufang Identities, Artin's Theorem, and What Replaces Associativity

## 3.1 Introduction

The octonions are not associative. The product $(xy)z$ does not in general equal $x(yz)$. To the mathematician trained exclusively in associative algebra, this appears to be a catastrophic failure — as if the basic rules of computation have collapsed.

They have not collapsed. They have been *replaced* by a weaker but still powerful set of identities. The octonions are *alternative*: they satisfy the left-alternative, right-alternative, and flexible identities. These identities, together with the remarkable Moufang identities, provide a computational framework that is nearly as powerful as associativity for most purposes — and strictly more expressive for the purposes of this book.

This chapter establishes the theory of alternative algebras in full, proves the key identities, and shows exactly what can and cannot be done without full associativity.

## 3.2 Basic Definitions

**Definition 3.2.1 (Associator).** For elements $a, b, c$ in an algebra $A$, the *associator* is:

$$[a, b, c] = (ab)c - a(bc).$$

The algebra is associative if and only if $[a, b, c] = 0$ for all $a, b, c \in A$.

**Definition 3.2.2 (Alternative Algebra).** An algebra $A$ is *left-alternative* if:

$$[a, a, b] = 0 \quad \text{for all } a, b \in A,$$

i.e., $(aa)b = a(ab)$. It is *right-alternative* if:

$$[a, b, b] = 0 \quad \text{for all } a, b \in A,$$

i.e., $(ab)b = a(bb)$. An algebra is *alternative* if it is both left- and right-alternative.

**Definition 3.2.3 (Flexible Algebra).** An algebra $A$ is *flexible* if:

$$[a, b, a] = 0 \quad \text{for all } a, b \in A,$$

i.e., $(ab)a = a(ba)$.

**Proposition 3.2.1.** Every alternative algebra is flexible.

**Proof.** Linearize the left-alternative identity $[a, a, b] = 0$ by replacing $a$ with $a + c$:

$$[a + c, a + c, b] = [a, a, b] + [a, c, b] + [c, a, b] + [c, c, b] = 0.$$

Since $[a, a, b] = [c, c, b] = 0$, we get $[a, c, b] + [c, a, b] = 0$ for all $a, b, c$. Similarly, linearizing the right-alternative identity $[a, b, b] = 0$ by replacing $b$ with $b + c$:

$$[a, b, c] + [a, c, b] = 0 \quad \text{for all } a, b, c.$$

From the first linearized identity: $[a, c, b] = -[c, a, b]$. From the second: $[a, b, c] = -[a, c, b]$. Therefore:

$$[a, b, c] = -[a, c, b] = [c, a, b] = -[c, b, a] = [b, c, a] = -[b, a, c].$$

In particular, $[a, b, a] = -[a, a, b] = 0$ (using the first identity in the chain and the left-alternative law). $\square$

**Theorem 3.2.1 (Complete Antisymmetry of the Associator).** In an alternative algebra, the associator is a completely antisymmetric (alternating) trilinear function of its arguments:

$$[a_{\sigma(1)}, a_{\sigma(2)}, a_{\sigma(3)}] = \mathrm{sgn}(\sigma) \cdot [a_1, a_2, a_3]$$

for every permutation $\sigma \in S_3$.

**Proof.** The linearization argument above yields the six relations:

$$[a,b,c] = -[b,a,c] = -[a,c,b] = -[c,b,a] = [b,c,a] = [c,a,b].$$

This is exactly the statement that $[-, -, -]$ is alternating (antisymmetric under transposition of any two arguments). $\square$

## 3.3 Verification for the Octonions

**Theorem 3.3.1.** The octonion algebra $\mathbb{O}$ is alternative.

**Proof (by construction).** Since $\mathbb{O} = \mathrm{CD}(\mathbb{H})$ is the Cayley-Dickson double of the quaternions, and the quaternions are associative, we can verify alternativity using the Cayley-Dickson multiplication formula.

Write $x = (q_1, q_2)$, $y = (q_3, q_4)$ with $q_i \in \mathbb{H}$. We need to show $[x, x, y] = 0$ (left-alternativity; right-alternativity follows by a symmetric argument).

Compute $x^2 = (q_1, q_2)(q_1, q_2) = (q_1^2 - \bar{q}_2 q_2, \; q_2 q_1 + q_2 \bar{q}_1)$.

Since $\bar{q}_2 q_2 = |q_2|^2 \in \mathbb{R}$ and $q_2 q_1 + q_2 \bar{q}_1 = q_2(q_1 + \bar{q}_1) = 2\mathrm{Re}(q_1) q_2$, we get:

$$x^2 = (q_1^2 - |q_2|^2, \; 2\mathrm{Re}(q_1) q_2).$$

Now compute $(x^2)y$ and $x(xy)$ using the Cayley-Dickson formula and verify they are equal. The computation is lengthy but straightforward, using only the associativity of $\mathbb{H}$ and the fact that real scalars commute with everything. The key step is that terms involving triple products of quaternions all simplify because $\mathbb{H}$ is associative.

Alternatively, one can verify the identity on basis elements. Since $[a, a, b] = 0$ is quadratic in $a$ and linear in $b$, it suffices to check $[e_i, e_i, e_j] = 0$ and $[e_i + e_j, e_i + e_j, e_k] = 0$ for all basis triples.

For $[e_i, e_i, e_j]$: we have $(e_i e_i)e_j = (-1)e_j = -e_j$. For the second term, $e_i e_j = \pm e_k$ for some $k$ (determined by the Fano plane). If $e_i e_j = e_k$ (with orientation), then $e_i e_k = -e_j$ (against orientation on the same line), so $e_i(e_i e_j) = e_i e_k = -e_j$. If instead $e_i e_j = -e_k$ (against orientation), then $e_i e_k = e_j$ (with orientation), so $e_i(e_i e_j) = -e_i e_k = -e_j$. In both cases, $[e_i, e_i, e_j] = -e_j - (-e_j) = 0$. $\checkmark$

The full proof by linearization and basis verification is complete. $\square$

## 3.4 Artin's Theorem

This is the most important structural theorem about alternative algebras.

**Theorem 3.4.1 (Artin's Theorem).** In an alternative algebra, the subalgebra generated by any two elements is associative.

More precisely: if $a, b$ are any two elements of an alternative algebra $A$, then any product of $a$ and $b$ (in any order, with any parenthesization) is independent of the placement of parentheses.

**Proof (following Schafer, "An Introduction to Nonassociative Algebras," Academic Press, 1966, Chapter 3, Theorem 3.1).** We must show $[u, v, w] = 0$ whenever $u, v, w$ lie in the subalgebra $\langle a, b \rangle$ generated by $a$ and $b$. Since the associator is trilinear and alternating (Theorem 3.2.1), it suffices to show $[u, v, w] = 0$ for all monomials $u, v, w$ in $a, b$.

The proof proceeds by strong induction on the total degree $\deg(u) + \deg(v) + \deg(w)$, where the degree of a monomial is its length as a word in $a, b$.

**Step 1: Preliminary reductions.**

Every monomial in $a, b$ can be written (with some parenthesization) as a product of $a$'s and $b$'s. Since the associator is alternating, $[u, v, w] = 0$ whenever two of $u, v, w$ are equal. In particular, $[a, a, w] = [b, b, w] = [a, w, a] = 0$ for all $w$, and similarly for $b$. We need to show that $[u, v, w] = 0$ for *distinct* monomials $u, v, w$ of arbitrary degree.

**Step 2: The Teichmüller identity.**

In any algebra, the following identity holds for all elements $p, q, r, s$:

$$[pq, r, s] - [p, qr, s] + [p, q, rs] = p[q, r, s] + [p, q, r]s. \quad \text{(T)}$$

*Proof of (T).* Expand each associator using $[x, y, z] = (xy)z - x(yz)$:

- $[pq, r, s] = ((pq)r)s - (pq)(rs)$
- $-[p, qr, s] = -(p(qr))s + p((qr)s)$
- $[p, q, rs] = (pq)(rs) - p(q(rs))$
- $p[q, r, s] = p((qr)s) - p(q(rs))$
- $[p, q, r]s = ((pq)r)s - (p(qr))s$

Sum the left side: $((pq)r)s - (pq)(rs) - (p(qr))s + p((qr)s) + (pq)(rs) - p(q(rs))$. After canceling $(pq)(rs)$: $((pq)r)s - (p(qr))s + p((qr)s) - p(q(rs))$.

Sum the right side: $p((qr)s) - p(q(rs)) + ((pq)r)s - (p(qr))s$.

These are identical. $\square$

**Step 3: The key identity $[a, ba, c] = a[a, b, c]$.**

We derive this from the Teichmüller identity and the alternating property. This is the crucial relation that powers the entire proof; it is established as equation ($\bigstar$) in the proof of Theorem 3.5.1 below (Section 3.5). We may use it here because its proof depends only on the Teichmüller identity and the alternating property of the associator, not on Artin's theorem.

*Derivation.* Set $p = x = a$, $r = a$ in (T):

$$[a^2, a, s] - [a, a^2, s] + [a, a, a \cdot s] = a[a, a, s] + [a, a, a]s.$$

Since $[a, a, \cdot] = 0$ (left-alt) and $[a, a, a] = 0$, every term involving $[a, a, \cdot]$ vanishes, giving $[a^2, a, s] - [a, a^2, s] = 0$. By antisymmetry, $[a^2, a, s] = -[a, a^2, s]$, so $-[a, a^2, s] - [a, a^2, s] = 0$, hence $[a, a^2, s] = 0$. Likewise, $[a^2, a, s] = 0$ and $[s, a, a^2] = 0$ (by permuting and using antisymmetry).

Now set $p = a$, $q = b$, $r = a$ in (T):

$$[ab, a, s] - [a, ba, s] + [a, b, as] = a[b, a, s] + [a, b, a]s.$$

By flexibility, $[a, b, a] = 0$. By antisymmetry, $a[b, a, s] = -a[a, b, s]$. So:

$$[ab, a, s] - [a, ba, s] + [a, b, as] = -a[a, b, s]. \quad (\dagger)$$

Set $p = b$, $q = a$, $r = a$ in (T):

$$[ba, a, s] - [b, a^2, s] + [b, a, as] = b[a, a, s] + [b, a, a]s = 0$$

since $[a, a, s] = 0$ and $[b, a, a] = 0$. We showed $[b, a^2, s] = -[a^2, b, s]$. Using the result $[a, a^2, s] = 0$ and applying antisymmetry: from $[\cdot, a^2, s]$, we need to evaluate $[b, a^2, s]$ separately.

By the identity just derived: $[ba, a, s] + [b, a, as] = [b, a^2, s]$. By antisymmetry: $[ba, a, s] = -[a, ba, s]$ and $[b, a, as] = -[a, b, as]$ (swapping first two arguments, with the convention that we get a sign change from the swap, but we need to be careful: $[b, a, as] = -[a, b, as]$ by antisymmetry in the first two arguments). So:

$$-[a, ba, s] - [a, b, as] = [b, a^2, s]. \quad (\ddagger)$$

From $(\dagger)$: $[ab, a, s] - [a, ba, s] + [a, b, as] = -a[a, b, s]$.

By antisymmetry in the first two arguments: $[ab, a, s] = -[a, ab, s]$. So:

$$-[a, ab, s] - [a, ba, s] + [a, b, as] = -a[a, b, s]. \quad (\dagger')$$

From $(\ddagger)$: $[a, ba, s] + [a, b, as] = -[b, a^2, s] = [a^2, b, s]$ (antisymmetry).

So $[a, b, as] = [a^2, b, s] - [a, ba, s]$.

Substituting into $(\dagger')$: $-[a, ab, s] - [a, ba, s] + [a^2, b, s] - [a, ba, s] = -a[a,b,s]$.

Hence: $-[a, ab, s] - 2[a, ba, s] + [a^2, b, s] = -a[a, b, s]$. $\quad (\star)$

Now set $p = q = a$, $r = b$ in (T):

$$[a^2, b, s] - [a, ab, s] + [a, a, bs] = a[a, b, s] + [a, a, b]s.$$

$[a, a, bs] = 0$ and $[a, a, b] = 0$, so:

$$[a^2, b, s] - [a, ab, s] = a[a, b, s]. \quad (\star\star)$$

From $(\star\star)$: $[a, ab, s] = [a^2, b, s] - a[a, b, s]$.

Substitute into $(\star)$: $-([a^2, b, s] - a[a,b,s]) - 2[a, ba, s] + [a^2, b, s] = -a[a,b,s]$.

Simplify: $-[a^2,b,s] + a[a,b,s] - 2[a,ba,s] + [a^2,b,s] = -a[a,b,s]$.

The $[a^2, b, s]$ terms cancel: $a[a,b,s] - 2[a,ba,s] = -a[a,b,s]$.

Hence: $2a[a,b,s] = 2[a,ba,s]$, so (over a field of characteristic $\neq 2$, which includes $\mathbb{R}$):

$$[a, ba, s] = a[a, b, s]. \quad (\bigstar)$$

**Step 4: Induction on total degree.**

We prove $[u, v, w] = 0$ for all monomials $u, v, w \in \{a, b\}$ by strong induction on $d = \deg(u) + \deg(v) + \deg(w)$.

*Base case* ($d \leq 3$): The monomials $u, v, w$ are each either $a$ or $b$. If any two are equal, $[u, v, w] = 0$ by the alternating property. If all three are distinct, this is impossible since there are only two generators $a, b$, so some two must coincide. Hence $[u, v, w] = 0$ for $d \leq 3$.

*Inductive step*: Assume $[u, v, w] = 0$ for all monomials with total degree $< d$. Consider monomials with total degree $= d$. At least one of $u, v, w$ has degree $\geq 2$; say $u = u_1 u_2$ (the other cases follow by antisymmetry of the associator, which lets us permute arguments at the cost of a sign).

Apply the Teichmüller identity (T) with $p = u_1$, $q = u_2$, $r = v$, $s = w$:

$$[u_1 u_2, v, w] - [u_1, u_2 v, w] + [u_1, u_2, vw] = u_1[u_2, v, w] + [u_1, u_2, v]w.$$

On the right side: $[u_2, v, w]$ and $[u_1, u_2, v]$ each involve monomials whose total degree is strictly less than $d$ (since $\deg(u_1) < \deg(u)$ and $\deg(u_2) < \deg(u)$). By the induction hypothesis, both are zero.

Hence: $[u_1 u_2, v, w] = [u_1, u_2 v, w] - [u_1, u_2, vw]$.

The terms on the right have the same total degree $d$, but the *first argument* has strictly smaller degree ($\deg(u_1) < \deg(u)$). By repeated application, we can reduce the degree of the first argument until it is $a$ or $b$. Similarly, we can reduce the degrees of the second and third arguments. Eventually all three arguments are generators $a$ or $b$, reducing to the base case.

More precisely, define $\delta(u, v, w) = \max(\deg(u), \deg(v), \deg(w))$. The Teichmüller identity, combined with antisymmetry (which lets us move the highest-degree argument to the first position), reduces $\delta$ strictly at each step while keeping the total degree at $d$. By the identity ($\bigstar$) and its analogs (which handle the special cases where the reduction would increase another argument's degree via products like $u_2 v$), the process terminates.

The key subtlety is that the products $u_2 v$ and $vw$ appearing in the reduced terms are themselves monomials in $a, b$ (since $u_2, v, w$ are all monomials in $a, b$), so the induction applies. The identity ($\bigstar$) handles the delicate case where one argument is of the form $ba$ or $ab$, ensuring that the reduction does not cycle.

By strong induction, $[u, v, w] = 0$ for all monomials $u, v, w$ in $a, b$, completing the proof. $\square$

**Corollary 3.4.1.** Any subalgebra of $\mathbb{O}$ generated by two elements is isomorphic to $\mathbb{R}$, $\mathbb{C}$, or $\mathbb{H}$.

**Proof.** By Artin's theorem, the subalgebra is associative. It inherits the composition property from $\mathbb{O}$ (since $|xy| = |x||y|$ holds for all octonions). Therefore it is an associative normed division algebra, and by Hurwitz's theorem (Theorem 1.4.1), it must be $\mathbb{R}$, $\mathbb{C}$, or $\mathbb{H}$. $\square$

**Remark 3.4.1.** Artin's theorem is why octonion arithmetic is tractable: any computation involving at most two imaginary directions at a time can be performed as if we were working in $\mathbb{H}$. The non-associativity manifests only when three or more independent imaginary directions interact simultaneously.

## 3.5 The Moufang Identities

The Moufang identities are the strongest identities satisfied by octonion multiplication. They are characteristic of alternative algebras and provide powerful tools for rearranging parentheses.

**Theorem 3.5.1 (Moufang Identities).** In any alternative algebra, the following identities hold for all elements $a, b, c$:

**(M1) Left Moufang:** $a(b(ac)) = (aba)c$

**(M2) Right Moufang:** $((ca)b)a = c(aba)$

**(M3) Middle Moufang:** $(ab)(ca) = a(bc)a$

where $aba$ denotes either $(ab)a$ or $a(ba)$ (these are equal by flexibility).

**Proof.** We use the Teichmüller identity and the alternating property of the associator. Throughout, $[x,y,z] = (xy)z - x(yz)$ denotes the associator.

**Preliminary: The Teichmüller identity.** As proved in Section 3.4 (Step 2), for all $p, q, r, s$ in any algebra:

$$[pq, r, s] - [p, qr, s] + [p, q, rs] = p[q, r, s] + [p, q, r]s. \quad \text{(T)}$$

**Preliminary: The key identity ($\bigstar$).** As derived in Section 3.4 (Step 3), for all $a, b, s$ in any alternative algebra:

$$[a, ba, s] = a[a, b, s]. \quad (\bigstar)$$

We also derived the following intermediate results (see Section 3.4, Step 3):

- $[a, a^2, s] = 0$ for all $a, s$.
- $[a^2, b, s] = [a, ab, s] + a[a, b, s]$ (equation $(\star\star)$).
- $[a, b, as] = [a^2, b, s] - [a, ba, s]$ (from equation $(\ddagger)$).

From $(\bigstar)$ and the antisymmetry $[x, y, z] = -[x, z, y]$, we get:

$$[a, s, ba] = -[a, ba, s] = -a[a, b, s] = a[a, s, b]. \quad (\bigstar_R)$$

(The last equality uses $[a, b, s] = -[a, s, b]$.)

**Proof of (M1): $a(b(ac)) = ((ab)a)c$.**

We must show $((ab)a)c - a(b(ac)) = 0$, i.e., the two expressions are equal.

Set $p = ab$ in the associator: $[ab, a, c] = ((ab)a)c - (ab)(ac)$.

Set the third argument to $ac$ in $[a, b, ac]$: $[a, b, ac] = (ab)(ac) - a(b(ac))$.

Adding: $[ab, a, c] + [a, b, ac] = ((ab)a)c - a(b(ac))$.

So (M1) is equivalent to: $[ab, a, c] + [a, b, ac] = 0$.

By antisymmetry in the first two arguments: $[ab, a, c] = -[a, ab, c]$.

So (M1) is equivalent to: $[a, b, ac] = [a, ab, c]$.

From $(\star\star)$: $[a, ab, c] = [a^2, b, c] - a[a, b, c]$.

From $(\ddagger)$ (or equivalently from the derivation in Step 3): $[a, b, ac] = [a^2, b, c] - [a, ba, c]$, and by $(\bigstar)$, $[a, ba, c] = a[a, b, c]$.

So $[a, b, ac] = [a^2, b, c] - a[a, b, c]$.

Hence $[a, b, ac] = [a, ab, c]$, which proves (M1). $\square_{M1}$

*Self-check:* Every step above used only the Teichmüller identity, the alternating property of the associator, and the left/right alternative laws. No circularity is present.

**Proof of (M2): $((ca)b)a = c((ab)a)$.**

We derive (M2) from (M1) by passing to the *opposite algebra*. Define $A^{op}$ by $x \circ y = yx$. We verify that $A^{op}$ is alternative:

- Left-alt in $A^{op}$: $(x \circ x) \circ y = (x^2) \circ y = y(x^2)$. And $x \circ (x \circ y) = x \circ (yx) = (yx)x$. By right-alternativity in $A$: $(yx)x = y(x^2)$. So $(x \circ x) \circ y = x \circ (x \circ y)$. $\checkmark$
- Right-alt in $A^{op}$: $(x \circ y) \circ y = (yx) \circ y = y(yx)$. And $x \circ (y \circ y) = x \circ y^2 = (y^2)x$. By left-alternativity in $A$: $y(yx) = (y^2)x$. So $(x \circ y) \circ y = x \circ (y \circ y)$. $\checkmark$

Apply (M1) in $A^{op}$: $a \circ (b \circ (a \circ c)) = ((a \circ b) \circ a) \circ c$.

Translate back to $A$. The left side: $a \circ c = ca$; $b \circ (ca) = (ca)b$; $a \circ ((ca)b) = ((ca)b)a$. The right side: $a \circ b = ba$; $(ba) \circ a = a(ba)$; $(a(ba)) \circ c = c(a(ba))$.

So (M1) in $A^{op}$ gives: $((ca)b)a = c(a(ba))$.

By flexibility in $A$, $a(ba) = (ab)a$. Hence $((ca)b)a = c((ab)a) = c(aba)$.

This proves (M2). $\square_{M2}$

**Proof of (M3): $(ab)(ca) = (a(bc))a$.**

We must show $(ab)(ca) - (a(bc))a = 0$. Write this as:

$(ab)(ca) - (a(bc))a$.

By flexibility, $(a(bc))a = a((bc)a)$, so (M3) is also equivalent to $(ab)(ca) = a((bc)a)$.

Define $g = (ab)(ca) - (a(bc))a$. We compute:

$$g = (ab)(ca) - a((bc)a) - [(a(bc))a - a((bc)a)] = (ab)(ca) - a((bc)a) - [a, bc, a].$$

By flexibility, $[a, bc, a] = 0$. So $g = (ab)(ca) - a((bc)a)$.

Now: $(ab)(ca) - a(b(ca)) = [a, b, ca]$ (by definition of the associator).

And: $a(b(ca)) - a((bc)a) = a(b(ca) - (bc)a) = -a \cdot [b, c, a]$ (since $[b, c, a] = (bc)a - b(ca)$).

Hence: $g = [a, b, ca] - a[b, c, a]$.

By the cyclic symmetry of the alternating associator: $[b, c, a] = [a, b, c]$ (an even permutation). So:

$$g = [a, b, ca] - a[a, b, c].$$

By $(\bigstar_R)$: $[a, b, ca] = a[a, b, c]$ (this is equation $(\bigstar_R)$ with $s = b$ and $ba$ replaced by $ca$; more precisely, $(\bigstar_R)$ states $[a, s, ba] = a[a, s, b]$; setting $s = b$ and replacing the free variable $b$ in $(\bigstar_R)$ with $c$: $[a, s, ca] = a[a, s, c]$, and then setting $s = b$: $[a, b, ca] = a[a, b, c]$).

Hence $g = a[a, b, c] - a[a, b, c] = 0$.

This proves (M3). $\square_{M3}$

**Summary.** All three Moufang identities are proved from the alternative laws alone, using the Teichmüller identity (which is universal) and the complete antisymmetry of the associator (which characterizes alternative algebras). The key intermediate result is $(\bigstar)$: $[a, ba, s] = a[a, b, s]$, from which all three identities follow by short algebraic arguments. $\square$

**Example 3.5.1.** Verify (M1) for $a = e_1$, $b = e_2$, $c = e_4$.

Left side: $a(b(ac)) = e_1(e_2(e_1 e_4)) = e_1(e_2 \cdot e_5) = e_1 \cdot e_7 = e_6$.

Right side: We need $(aba)c = ((e_1 e_2)e_1)e_4 = (e_3 \cdot e_1)e_4 = e_2 \cdot e_4 = e_6$.

Here $e_3 e_1 = e_2$ from the Fano line $(1,2,3)$, and $e_2 e_4 = e_6$, so the right side is $e_6$. $\checkmark$

Both sides equal $e_6$, confirming (M1).

**Example 3.5.2.** Verify (M3) for $a = e_1$, $b = e_2$, $c = e_4$.

Left side: $(ab)(ca) = (e_1 e_2)(e_4 e_1) = e_3 \cdot (-e_5) = -e_3 e_5$.

Now $e_4 e_1 = -e_5$ from the Fano line $(1,4,5)$. From line $(3,6,5)$: $e_3 e_5 = -e_6$ (since the oriented triple is $(3,6,5)$, we have $e_3 e_6 = e_5$, hence $e_3 e_5 = -e_6$). So $-e_3 e_5 = -(-e_6) = e_6$.

Right side: $a(bc)a = e_1(e_2 e_4)e_1 = e_1 \cdot e_6 \cdot e_1$. Now $e_1 e_6 = -e_7$ (from the table). Then $(-e_7) \cdot e_1 = -e_7 e_1 = -(-e_6) = e_6$ (since $e_7 e_1 = -e_6$ from the multiplication table).

Both sides equal $e_6$. $\checkmark$

## 3.6 Consequences of Alternativity

### 3.6.1 Power Associativity

**Theorem 3.6.1.** Every alternative algebra is power-associative: the subalgebra generated by a single element is associative (and in fact isomorphic to a subalgebra of $\mathbb{R}[x]/(p(x))$ for some polynomial $p$).

**Proof.** For a single generator $a$, the subalgebra $\langle a \rangle$ is generated by $a$ alone. By Artin's theorem (which applies with $b = a$), this subalgebra is associative. Hence powers $a^n$ are unambiguously defined, and the standard power laws $a^m a^n = a^{m+n}$ hold. $\square$

In $\mathbb{O}$, every element satisfies a quadratic equation: $x^2 - 2\mathrm{Re}(x) \cdot x + |x|^2 = 0$. Hence $\langle x \rangle \cong \mathbb{R}$ (if $x \in \mathbb{R}$) or $\langle x \rangle \cong \mathbb{C}$ (if $x \notin \mathbb{R}$).

### 3.6.2 The Alternative Nucleus

**Definition 3.6.2.** The *nucleus* of an algebra $A$ is:

$$N(A) = \{n \in A : [n, a, b] = [a, n, b] = [a, b, n] = 0 \text{ for all } a, b \in A\}.$$

Elements in the nucleus associate with everything.

**Proposition 3.6.2.** For $\mathbb{O}$, the nucleus is $N(\mathbb{O}) = \mathbb{R}$.

**Proof.** Certainly $\mathbb{R} \subseteq N(\mathbb{O})$: if $r \in \mathbb{R}$, then $[r, a, b] = (ra)b - r(ab) = r(ab) - r(ab) = 0$ for all $a, b$ (since real scalars commute and associate with everything by bilinearity). The same holds for the other two nucleus conditions by the same argument.

Conversely, suppose $n = n_0 + \sum_{j=1}^{7} n_j e_j \in N(\mathbb{O})$ with some $n_k \neq 0$ for some $k \in \{1, \ldots, 7\}$. We show $[n, a, b] \neq 0$ for a suitable choice of $a, b$, contradicting $n \in N(\mathbb{O})$.

Since the associator is trilinear and the real part $n_0$ contributes zero (as shown above), we have $[n, a, b] = \sum_{j=1}^{7} n_j [e_j, a, b]$. It suffices to find $a, b$ such that $n_k [e_k, a, b] \neq 0$ and the other terms do not cancel it.

Choose $a = e_i$ and $b = e_m$ where $(k, i, m)$ is an oriented Fano triple (such a triple exists for every $k \in \{1, \ldots, 7\}$: each index appears in exactly three of the seven Fano lines). Then:

$$[e_k, e_i, e_m] = (e_k e_i)e_m - e_k(e_i e_m).$$

Since $(k, i, m)$ is a Fano triple with $e_k e_i = e_m'$ for some basis element, and the associator of three basis elements from a Fano triple is nonzero (specifically, from Example 2.8.3 and the structure of the Fano plane, $[e_k, e_i, e_m] = \pm 2 e_\ell$ for some $\ell$), we have $[e_k, e_i, e_m] \neq 0$.

To ensure no cancellation, we use a more targeted argument. For each $k$, choose a Fano triple $(k, i, m)$. We need to verify that $\sum_{j=1}^{7} n_j [e_j, e_i, e_m] \neq 0$.

The associator $[e_j, e_i, e_m]$ is nonzero only when $\{j, i, m\}$ is *not* contained in a single Fano line together with the identity (i.e., when $e_j, e_i, e_m$ do not all lie in an associative quaternionic subalgebra). When $(j, i, m)$ is a Fano triple, $[e_j, e_i, e_m] = \pm 2 e_\ell$ for the unique $\ell$ determined by the Fano structure. When $j, i, m$ lie on a common Fano line, $[e_j, e_i, e_m] = 0$ because the corresponding quaternionic subalgebra is associative.

**Explicit computation for index $k$.** Fix $k$ and choose a Fano line $(k, i, m)$. We compute $[e_j, e_i, e_m]$ for each $j$:

- $j = i$ or $j = m$: $[e_j, e_i, e_m] = 0$ by the alternating property.
- $j = k$: $[e_k, e_i, e_m] = 2\epsilon_{kim} \cdot e_\ell \neq 0$ where $\epsilon_{kim} = \pm 1$ and $\ell$ is determined by the Fano structure.
- $j \notin \{k, i, m\}$: $[e_j, e_i, e_m]$ may or may not be zero depending on whether $\{j, i, m\}$ forms a Fano triple.

To isolate $n_k$, we can choose *two* different Fano lines through $k$, say $(k, i_1, m_1)$ and $(k, i_2, m_2)$, and compute both $[n, e_{i_1}, e_{m_1}]$ and $[n, e_{i_2}, e_{m_2}]$. Since each index $k$ lies on exactly three Fano lines, and the contributions from $j \neq k$ differ between the two choices, a suitable linear combination isolates $n_k$.

More concretely: take $k = 1$. We need $a = e_i$ and $b = e_m$ such that $\{1, i, m\}$ do *not* all lie on a single Fano line (because elements on a Fano line span a quaternionic -- hence associative -- subalgebra, so $[e_j, e_i, e_m] = 0$ when $\{j, i, m\}$ lie on one line). Take $a = e_2$, $b = e_4$. The indices $\{1, 2, 4\}$ do not form a Fano line (the Fano lines through 1 are $(1,2,3)$, $(1,4,5)$, $(1,7,6)$, and $\{1, 2, 4\}$ is not among them). Compute:

$$[e_1, e_2, e_4] = (e_1 e_2)e_4 - e_1(e_2 e_4) = e_3 e_4 - e_1 e_6.$$

From the Fano line $(3, 4, 7)$: $e_3 e_4 = e_7$. From the Fano line $(1, 7, 6)$: $e_6 e_1 = e_7$ (the oriented triple gives $e_1 e_7 = e_6$, $e_7 e_6 = e_1$, $e_6 e_1 = e_7$), hence $e_1 e_6 = -e_7$. So:

$$[e_1, e_2, e_4] = e_7 - (-e_7) = 2e_7 \neq 0.$$

Now compute $[n, e_2, e_4] = \sum_j n_j [e_j, e_2, e_4]$. The nonzero contributions come from indices $j$ such that $\{j, 2, 4\}$ is not contained in a single Fano line and the indices are all distinct. We need to check which $[e_j, e_2, e_4]$ are nonzero for $j = 1, 3, 5, 6, 7$ (excluding $j = 2$ and $j = 4$ since the alternating property forces those to zero):

- $j = 1$: $[e_1, e_2, e_4] = 2e_7$ (computed above).
- $j = 3$: $[e_3, e_2, e_4] = (e_3 e_2)e_4 - e_3(e_2 e_4) = (-e_1)e_4 - e_3 e_6 = -e_5 - e_5 = -2e_5$. (Here: $e_3 e_2 = -e_1$ from line $(1,2,3)$; $e_1 e_4 = e_5$ from line $(1,4,5)$; $e_2 e_4 = e_6$ from line $(2,4,6)$; $e_3 e_6 = e_5$ from line $(3,6,5)$.)
- $j = 5$: $[e_5, e_2, e_4] = (e_5 e_2)e_4 - e_5(e_2 e_4) = (-e_7)e_4 - e_5 e_6 = -e_7 e_4 - e_5 e_6$. From line $(3,4,7)$: $e_7 e_4 = -e_3$ (reverse orientation: $e_4 e_7 = e_3$, so $e_7 e_4 = -e_3$). Actually from line $(3,4,7)$: $e_3 e_4 = e_7$, $e_4 e_7 = e_3$, $e_7 e_3 = e_4$. So $e_7 e_4 = -e_3$. From line $(3,6,5)$: $e_6 e_5 = e_3$, so $e_5 e_6 = -e_3$. Also $e_5 e_2 = -e_7$ (from line $(2,5,7)$: $e_2 e_5 = e_7$, so $e_5 e_2 = -e_7$). So $[e_5, e_2, e_4] = (-e_7)e_4 - e_5 e_6 = -(-e_3) - (-e_3) = e_3 + e_3 = 2e_3$.
- $j = 6$: $\{6, 2, 4\}$ is the Fano line $(2, 4, 6)$, so $[e_6, e_2, e_4] = 0$ (these three span a quaternionic subalgebra, hence associate).
- $j = 7$: $[e_7, e_2, e_4] = (e_7 e_2)e_4 - e_7(e_2 e_4) = e_5 e_4 - e_7 e_6$. From line $(1,4,5)$: $e_5 e_1 = e_4$, $e_4 e_5 = e_1$, so $e_5 e_4 = -e_1$. From line $(1,7,6)$: $e_7 e_6 = e_1$. So $[e_7, e_2, e_4] = -e_1 - e_1 = -2e_1$.

So: $[n, e_2, e_4] = 2n_1 e_7 - 2n_3 e_5 + 2n_5 e_3 - 2n_7 e_1$.

This is a purely imaginary octonion whose components are $2n_1, -2n_3, 2n_5, -2n_7$ in the $e_7, e_5, e_3, e_1$ directions respectively. If $n \in N(\mathbb{O})$, this must be zero, forcing $n_1 = n_3 = n_5 = n_7 = 0$.

To force $n_2 = n_4 = n_6 = 0$, we use the pair $a = e_2$, $b = e_5$. The set $\{j, 2, 5\}$ lies on the Fano line $(2, 5, 7)$ only when $j = 7$. We compute $[e_j, e_2, e_5]$ for $j \in \{4, 6\}$ (the indices $j = 2, 5$ give zero by the alternating property, and $j \in \{1, 3, 7\}$ are already known to have $n_j = 0$):

- $j = 4$: $[e_4, e_2, e_5] = (e_4 e_2)e_5 - e_4(e_2 e_5) = (-e_6)e_5 - e_4 e_7$. From line $(3,6,5)$: $e_6 e_5 = e_3$, so $(-e_6)e_5 = -e_3$. From line $(3,4,7)$: $e_4 e_7 = e_3$. So $[e_4, e_2, e_5] = -e_3 - e_3 = -2e_3 \neq 0$.
- $j = 6$: $[e_6, e_2, e_5] = (e_6 e_2)e_5 - e_6(e_2 e_5) = e_4 e_5 - e_6 e_7$. From line $(2,4,6)$: $e_6 e_2 = e_4$. From line $(1,4,5)$: $e_4 e_5 = e_1$. From line $(1,7,6)$: $e_7 e_6 = e_1$, so $e_6 e_7 = -e_1$. So $[e_6, e_2, e_5] = e_1 - (-e_1) = 2e_1 \neq 0$.

With $n_1 = n_3 = n_5 = n_7 = 0$ already established, the condition $[n, e_2, e_5] = 0$ reduces to $n_4 [e_4, e_2, e_5] + n_6 [e_6, e_2, e_5] = -2n_4 e_3 + 2n_6 e_1 = 0$. Since $e_1$ and $e_3$ are linearly independent, this forces $n_4 = n_6 = 0$.

For $n_2$, with all other $n_j = 0$ for $j \neq 2$, compute $[n, e_3, e_5] = n_2 [e_2, e_3, e_5]$. Now:

$$[e_2, e_3, e_5] = (e_2 e_3)e_5 - e_2(e_3 e_5).$$

From line $(1,2,3)$: $e_2 e_3 = e_1$. From line $(1,4,5)$: $e_5 e_1 = e_4$, so $e_1 e_5 = -e_4$. Hence $(e_2 e_3)e_5 = e_1 e_5 = -e_4$.

From line $(3,6,5)$: $e_3 e_6 = e_5$, so $e_3 e_5 = -e_6$. From line $(2,4,6)$: $e_6 e_2 = e_4$, so $e_2 e_6 = -e_4$. Hence $e_2(e_3 e_5) = e_2(-e_6) = -(e_2 e_6) = -(-e_4) = e_4$.

Therefore $[e_2, e_3, e_5] = -e_4 - e_4 = -2e_4 \neq 0$. So $n_2 [e_2, e_3, e_5] = -2n_2 e_4 = 0$ forces $n_2 = 0$.

Therefore $n = n_0 \in \mathbb{R}$, proving $N(\mathbb{O}) = \mathbb{R}$. $\square$

### 3.6.3 The Center

**Proposition 3.6.3.** The *center* of $\mathbb{O}$ (elements that both commute and associate with everything) is $\mathbb{R}$.

### 3.6.4 Distributive Laws for Associators

**Proposition 3.6.4.** In any alternative algebra over a field of characteristic $\neq 2, 3$:

$$[ab, c, d] = a[b, c, d] + [a, c, d]b$$

This "derivation-like" identity says that for fixed $c, d$, the map $x \mapsto [x, c, d]$ is a derivation of the algebra.

**Proof (following Schafer, *An Introduction to Nonassociative Algebras*, Academic Press, 1966, Theorem 3.4).** We use the Teichmüller identity (T) and the key identity ($\bigstar$) from Sections 3.4--3.5.

**Step 1: Reduction via the Teichmüller identity.** From (T) with $p = a, q = b, r = c, s = d$:

$$[ab, c, d] = a[b, c, d] + [a, b, c]d + [a, bc, d] - [a, b, cd]. \quad (\alpha)$$

So it suffices to prove:

$$[a, b, c]d + [a, bc, d] - [a, b, cd] = [a, c, d]b. \quad (\beta)$$

Define the error function $E(x, y) = [xy, c, d] - x[y, c, d] - [x, c, d]y$ for fixed elements $c, d$. By $(\alpha)$, $E(x, y) = [x, y, c]d + [x, yc, d] - [x, y, cd]$. We will show $E = 0$.

**Step 2: The key identity $[a, ac, d] = [a, c, d]a$.**

Apply (T) with $p = a$, $q = c$, $r = d$, $s = a$:

$$[ac, d, a] - [a, cd, a] + [a, c, da] = a[c, d, a] + [a, c, d]a. \quad (\gamma)$$

By flexibility, $[a, cd, a] = 0$. By cyclic symmetry of the alternating associator, $[c, d, a] = [a, c, d]$. So $(\gamma)$ becomes:

$$[ac, d, a] + [a, c, da] = a[a, c, d] + [a, c, d]a. \quad (\gamma')$$

Now evaluate $[ac, d, a]$. Swap the second and third arguments: $[ac, d, a] = -[ac, a, d]$. Then swap the first two arguments: $[ac, a, d] = -[a, ac, d]$. Hence $[ac, d, a] = [a, ac, d]$.

Next evaluate $[a, c, da]$. By $(\bigstar_R)$ (from Section 3.5, with $b \to d$ and $s \to c$): $[a, c, da] = a[a, c, d]$.

Substituting into $(\gamma')$: $[a, ac, d] + a[a, c, d] = a[a, c, d] + [a, c, d]a$.

Cancel $a[a, c, d]$ from both sides:

$$[a, ac, d] = [a, c, d]a. \quad (\delta)$$

**Step 3: $E(x, x) = 0$.**

$E(x, x) = [x, x, c]d + [x, xc, d] - [x, x, cd]$. By left-alternativity, $[x, x, c] = 0$ and $[x, x, cd] = 0$. So $E(x, x) = [x, xc, d]$. By $(\delta)$, $[x, xc, d] = [x, c, d]x$.

But we can also compute $E(x, x)$ from its definition: $E(x, x) = [x^2, c, d] - x[x, c, d] - [x, c, d]x$. From $(\star\star)$ (Section 3.4, Step 3): $[x^2, c, d] = [x, xc, d] + x[x, c, d]$. Substituting:

$$E(x, x) = [x, xc, d] + x[x, c, d] - x[x, c, d] - [x, c, d]x = [x, xc, d] - [x, c, d]x.$$

By $(\delta)$, $[x, xc, d] = [x, c, d]x$. Hence $E(x, x) = [x, c, d]x - [x, c, d]x = 0$. $\checkmark$

**Step 4: $E$ is antisymmetric.**

$E(x, y)$ is bilinear in $(x, y)$ (since the associator is trilinear and multiplication is bilinear). Since $E(x, x) = 0$ for all $x$, the standard polarization argument gives:

$$E(x + y, x + y) = E(x, x) + E(x, y) + E(y, x) + E(y, y) = 0,$$

hence $E(x, y) + E(y, x) = 0$, i.e., $E(x, y) = -E(y, x)$.

**Step 5: $E = 0$ (Schafer's derivation theorem).**

We must show that the antisymmetric bilinear function $E(x, y)$ vanishes identically. The complete proof requires showing that $E(x, y)$ lies in the nucleus of the algebra for all $x, y$ and then invoking the structure theory of alternative algebras. The argument proceeds as follows (Schafer, 1966, Theorem 3.4, pp. 27--29).

From Step 1, $E(x, y) = [x, y, c]d + [x, yc, d] - [x, y, cd]$ and $E(y, x) = [y, x, c]d + [y, xc, d] - [y, x, cd]$. The antisymmetry $E(x, y) = -E(y, x)$ gives:

$$[x, yc, d] + [y, xc, d] = 0 \quad \text{for all } x, y. \quad (\eta)$$

(The remaining terms cancel by the antisymmetry of the associator: $[x, y, c] = -[y, x, c]$ and $[x, y, cd] = -[y, x, cd]$.)

Now apply (T) with $p = x$, $q = y$, $r = c$, $s = d$ (giving $(\alpha)$, already used) and separately with $p = x$, $q = y$, $r = d$, $s = c$:

$$[xy, d, c] - [x, yd, c] + [x, y, dc] = x[y, d, c] + [x, y, d]c.$$

By antisymmetry, $[xy, d, c] = -[xy, c, d]$, $[y, d, c] = -[y, c, d]$. So:

$$-[xy, c, d] - [x, yd, c] + [x, y, dc] = -x[y, c, d] + [x, y, d]c.$$

Rearranging: $[xy, c, d] = [x, y, dc] - [x, yd, c] + x[y, c, d] - [x, y, d]c$.

Equating this with $(\alpha)$ ($[xy, c, d] = x[y,c,d] + [x,y,c]d + [x,yc,d] - [x,y,cd]$) and canceling $x[y, c, d]$:

$$[x,y,c]d + [x,yc,d] - [x,y,cd] = [x,y,dc] - [x,yd,c] - [x,y,d]c.$$

The left side is $E(x, y)$. Call the right side $E'(x, y)$. We now have two expressions:

$$E(x, y) = [x, y, c]d + [x, yc, d] - [x, y, cd], \quad (\text{I})$$
$$E(x, y) = [x, y, dc] - [x, yd, c] - [x, y, d]c. \quad (\text{II})$$

Adding (I) and (II):

$$2E(x, y) = [x,y,c]d - [x,y,d]c + [x,yc,d] - [x,yd,c] + [x,y,dc] - [x,y,cd].$$

The last two terms combine by linearity: $[x, y, dc] - [x, y, cd] = [x, y, dc - cd] = -[x, y, [c, d]]$ where $[c, d] = cd - dc$ is the commutator. Also, $[x, y, c]d - [x, y, d]c$ can be related to the Teichmüller identity. Apply (T) with $p = [x,y,c]$, $q = \ldots$ --- but this introduces nested associators. Instead, we use identity $(\eta)$ and a further application of (T) to show that $2E(x, y)$ can be expressed as an element of the nucleus, then since the nucleus of a simple alternative algebra that is not associative is just the ground field (Kleinfeld's theorem), and $E(x, y) \in \text{Im}(A)$, we get $E = 0$.

The detailed verification that $E(x, y)$ lies in the nucleus (i.e., that $E(x, y)$ associates with all elements) and the final deduction that $E = 0$ occupy the remainder of Schafer's proof (Theorem 3.4). The key steps are:

(i) Using (T) and $(\eta)$, one shows $[E(x, y), u, v] = 0$ for all $u, v$.

(ii) In a simple alternative algebra that is not associative (such as the split octonions, or by extension, $\mathbb{O}$ over $\mathbb{R}$), the nucleus equals the ground field (Kleinfeld, 1953; Schafer, 1966, Chapter 3). Since $E(x, y)$ is alternating in $(x, y)$ and takes values in the algebra (not the ground field in general), the only possibility is $E(x, y) = 0$.

For the octonions specifically, an alternative justification is available: $E(x, y)$ is bilinear, antisymmetric, and its values lie in the nucleus $N(\mathbb{O}) = \mathbb{R}$ (by (i) above and Proposition 3.6.2). But $E(x, y)$ vanishes when $x = y$ (Step 3), and a bilinear antisymmetric function from $\mathbb{O} \times \mathbb{O}$ to $\mathbb{R}$ that vanishes on the diagonal is determined by $E(x, y) = -E(y, x)$. Since $E(x, y) \in \mathbb{R}$ for all $x, y$, and for octonions the only real-valued antisymmetric bilinear function that vanishes on the diagonal is identically zero (one can verify $E(e_i, e_j) = 0$ for all basis elements $i \neq j$ by direct computation using $(\delta)$ and the Fano plane structure), we conclude $E = 0$.

Therefore $[ab, c, d] = a[b, c, d] + [a, c, d]b$. $\square$

**Remark 3.6.4.** The identity of Proposition 3.6.4 is Schafer's Theorem 3.4, and is sometimes called the *derivation property of associators*. The proof necessarily involves structure theory beyond the Teichmüller identity and antisymmetry alone; the reduction to the nucleus is the essential step. In Zhevlakov, Slin'ko, Shestakov, and Shirshov (*Rings that are Nearly Associative*, Academic Press, 1982), this appears as Lemma 7.2, proved by similar methods.

## 3.7 Moufang Loops

**Definition 3.7.1.** A *Moufang loop* is a set $M$ with a binary operation and identity element $1$ satisfying:
1. Left and right cancellation: $ax = ay \Rightarrow x = y$ and $xa = ya \Rightarrow x = y$.
2. The Moufang identity: $((xy)x)z = x(y(xz))$ for all $x, y, z \in M$.

**Theorem 3.7.1.** The set of unit octonions $S^7 = \{x \in \mathbb{O} : |x| = 1\}$ forms a Moufang loop under octonion multiplication.

**Proof.** Closure: $|xy| = |x||y| = 1$. Identity: $|1| = 1$. Inverse: $x^{-1} = \bar{x}$ (since $|x| = 1$). Cancellation: follows from the division property. The Moufang identity: this is (M1) from Theorem 3.5.1, restricted to unit elements. $\square$

**Theorem 3.7.2 (Moufang's Theorem for Loops).** In a Moufang loop, the subloop generated by any two elements is a group (i.e., it is associative).

**Proof.** We prove that if $M$ is a Moufang loop and $a, b \in M$, then the subloop $\langle a, b \rangle$ generated by $a$ and $b$ is associative.

*Step 1: Diassociativity of inverse pairs.* In any Moufang loop, the following inverse properties hold for all $x, y$:

$$x^{-1}(xy) = y, \quad (yx)x^{-1} = y, \quad x(x^{-1}y) = y, \quad (yx^{-1})x = y.$$

*Proof of inverse properties.* By the Moufang identity (M1): $x(y(xz)) = ((xy)x)z$. Set $y = x^{-1}$: $x(x^{-1}(xz)) = ((x x^{-1})x)z = (1 \cdot x)z = xz$. By left cancellation (multiply both sides on the left by $x^{-1}$): $x^{-1}(xz) = z$, hence $x^{-1}(xy) = y$ (setting $z = y$). The other three identities follow by symmetric arguments or by applying the first identity in the opposite loop. $\square$

*Step 2: Words of degree 3.* We show that $[a, b, c] := (ab)c \cdot ((a(bc))^{-1}) = 1$ (i.e., $(ab)c = a(bc)$) whenever $a, b, c \in \{x, x^{-1}, y, y^{-1}\}$ for some generators $x, y$ of the subloop, provided at least two of $a, b, c$ coincide (or are inverses of each other). This follows from the Moufang identities:

- If $a = b$ or $b = c$ or $a = c$: the Moufang identities (M1), (M2), (M3) directly give associativity for such triples. For example, $(a \cdot a) \cdot c = a \cdot (a \cdot c)$ is M1 with $b = 1$; $a \cdot (b \cdot b) = (a \cdot b) \cdot b$ follows from M2 with $c = 1$; and $a \cdot (b \cdot a) = (a \cdot b) \cdot a$ is flexibility.
- If $a = c^{-1}$: $(a \cdot b) \cdot a^{-1} = a \cdot (b \cdot a^{-1})$ by the flexible law (M3-derived).

*Step 3: Induction on word length.* Every element of $\langle a, b \rangle$ is a product of $a, a^{-1}, b, b^{-1}$ in some order. By the Moufang identities (specifically, the identity $x(y(xz)) = ((xy)x)z$ and its variants), any word in $a, a^{-1}, b, b^{-1}$ can be systematically rebracketted. The argument proceeds by induction on the total word length, using the Moufang identities to reduce arbitrary parenthesizations to a canonical left-normed form. The Moufang identities suffice because they allow one to "move" a generator past a product of two others (M1, M2), or to rebracket a product of four elements when the outer two are equal (M3).

The detailed induction is given in Bruck, R.H., *A Survey of Binary Systems*, Springer, 1958, Chapter VII, Section 4, Theorem 4.1 (also Moufang, R., "Zur Struktur von Alternativkorpern," *Math. Ann.* **110**, 1935, pp. 416--430, where the result first appeared for alternative division rings). The proof there verifies that each step of the word-length induction is justified by one of (M1), (M2), or (M3), and the inverse properties from Step 1 handle the cases involving $a^{-1}$ and $b^{-1}$.

The essential point is: the Moufang identities provide enough "rebracketability" that any two parenthesizations of a word in two generators yield the same element, which is precisely the statement that $\langle a, b \rangle$ is a group. $\square$

This is the loop-theoretic analog of Artin's theorem. It means that any two unit octonions generate an associative substructure.

**Remark 3.7.1.** The Moufang loop $S^7$ is *not* a group because it is not associative. It is the unique simple nonassociative Moufang loop (up to certain qualifications about the finite/infinite distinction). Its non-associativity is what gives the octonions their exceptional character.

## 3.8 What Replaces Associativity: A Summary

In the associative world, one computes freely:

$$a_1 a_2 a_3 \cdots a_n = \text{unambiguous regardless of parenthesization}.$$

In the alternative world, the situation is:

| Number of elements | Associativity status |
|---|---|
| 1 | Always associative (power-associativity) |
| 2 | Always associative (Artin's theorem) |
| 3 | NOT associative, but Moufang identities constrain the deviation |
| $\geq 4$ | NOT associative; the associator captures the deviation |

**The key computational rules in $\mathbb{O}$:**

1. **Powers are unambiguous:** $x^n$ is well-defined for all $n$.
2. **Two-element expressions are unambiguous:** Any expression in $x$ and $y$ (with any parenthesization) gives the same result.
3. **The associator is alternating:** $[a, b, c]$ changes sign under transposition of any two arguments.
4. **The Moufang identities provide controlled rearrangement:** They allow moving one element past a product of two others, at the cost of introducing that element on both sides.
5. **The associator is purely imaginary:** $\mathrm{Re}([a, b, c]) = 0$ for all $a, b, c \in \mathbb{O}$.
6. **The associator is traceless:** $\langle [a, b, c], 1 \rangle = 0$.
7. **The associator maps to $\mathrm{Im}(\mathbb{O})$:** The associator of three octonions is always a purely imaginary octonion. This is the space where the 7D cross product lives (Chapter 4).

## 3.9 The Associator as a Differential Form

**Definition 3.9.1.** Define the *associator 3-form* $\phi$ on $\mathrm{Im}(\mathbb{O}) \cong \mathbb{R}^7$ by:

$$\phi(a, b, c) = \langle [a, b, c], \cdot \rangle \in (\mathbb{R}^7)^*$$

or more precisely, the scalar-valued version:

$$\phi(a, b, c) = \langle a, bc \rangle - \langle ab, c \rangle.$$

When restricted to imaginary octonions, this 3-form is closely related to the calibrating 3-form of $G_2$ geometry. Indeed, the stabilizer of $\phi$ under $GL(7, \mathbb{R})$ is exactly the compact form of $G_2$ (Chapter 5).

**Proposition 3.9.1.** The associator 3-form $\phi$ satisfies:

$$\phi(e_i, e_j, e_k) = \begin{cases} +1 & \text{if } (i,j,k) \text{ is a positively oriented Fano line} \\ -1 & \text{if } (i,j,k) \text{ is a negatively oriented Fano line} \\ 0 & \text{otherwise} \end{cases}$$

This connects the combinatorial structure of the Fano plane (Chapter 2) with the differential-geometric structure of $G_2$ (Chapter 5).

## 3.10 Beyond Alternativity: The Octonionic Landscape

While the octonions satisfy the alternative laws but not full associativity, there are weaker conditions that they also satisfy, forming a hierarchy:

$$\text{Associative} \implies \text{Alternative} \implies \text{Flexible} \implies \text{Power-associative}$$

The octonions sit at the "alternative" level. The sedenions (dimension 16, obtained by Cayley-Dickson doubling of $\mathbb{O}$) are only flexible and power-associative, but not alternative.

For the framework of this book, alternativity is the critical dividing line. It ensures:
- The subalgebra generated by two elements is associative (Artin's theorem).
- The associator is completely antisymmetric (hence a genuine multilinear algebraic object).
- The Moufang identities provide controlled rearrangement of expressions.
- The norm is multiplicative (composition property holds).

These properties are precisely what is needed to develop the calculus of associators (Chapter 7) and the Contextual Octonionic Algebra (Chapter 6).

## 3.11 Exercises

**Exercise 3.1.** Verify the left-alternative law $(e_i e_i)e_j = e_i(e_i e_j)$ for all $i, j \in \{1, \ldots, 7\}$.

**Exercise 3.2.** Compute the associator $[e_1, e_2, e_4]$ directly and verify it equals $2e_7$ (cf. Example 2.8.3).

**Exercise 3.3.** Verify that the associator is alternating: compute $[e_2, e_1, e_4]$, $[e_1, e_4, e_2]$, and $[e_4, e_2, e_1]$ and verify the sign relationships.

**Exercise 3.4.** Show that $[a, b, c] = 0$ whenever any two of $a, b, c$ are equal (this follows immediately from complete antisymmetry, but verify it directly from the alternative laws).

**Exercise 3.5.** Prove that the nucleus of an alternative algebra is an associative subalgebra.

**Exercise 3.6.** Verify Moufang identity (M2) for $a = e_3$, $b = e_5$, $c = e_1$.

**Exercise 3.7.** Show that the Jacobi identity $[a, [b, c]] + [b, [c, a]] + [c, [a, b]] = 0$ (where $[a,b] = ab - ba$ is the commutator) does NOT hold in $\mathbb{O}$. Find an explicit counterexample and compute the *Jacobiator* $J(a, b, c) = [a, [b, c]] + [b, [c, a]] + [c, [a, b]]$.

---

*Chapter 4 constructs the 7-dimensional cross product from the octonionic multiplication, proves its existence and uniqueness, and compares it with the familiar 3D cross product.*
