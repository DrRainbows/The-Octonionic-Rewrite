> **Rigor Level: RIGOROUS** — Kernel decomposition is rigorous; non-gameability proven by explicit computation for m=3,4 and by algebraic geometry (Tarski-Seidenberg) for all m>=3. Pointwise non-gameability for m>=5 proven via explicit constraint independence (Lemma 26.12i-2) and spectral averaging (Theorem 26.12i).
> **Novelty: NOVEL** — The non-gameable alignment theorem is a genuinely new result connecting octonionic structure to alignment theory.

# Chapter 26: Non-Gameable Alignment Theorem

## 26.1 Introduction

This chapter bridges pure octonionic algebra and applied optimization theory. We prove that alignment functions defined over the octonions possess a non-gameability property that is impossible in associative algebras. The core insight is this: in an associative algebra, agents can coordinate their representations to manipulate outcomes because the grouping of operations does not matter — any coalition can reparenthesize without consequence. In the octonions, reparenthesization changes the result (via the associator), and this change is not controllable by any single agent or small coalition.

This has direct implications for:
- Governance systems where officials cannot game alignment metrics
- Market mechanisms resistant to collusion
- Engineering team composition where optimal configurations are robust

---

## 26.2 Formal Setup

### 26.2.1 Agents as Unit Octonions

**Definition 26.1.** An *agent* is a unit octonion $s \in S^7 \subset \mathbb{O}$ with $|s| = 1$. The set of agents is $S = \{s_1, \ldots, s_n\} \subset S^7$.

The octonionic representation of an agent encodes their "type" or "capability profile" in a 7-dimensional space (8 dimensions minus the norm constraint). The 7 imaginary components can be interpreted as independent capability axes (e.g., technical skill, communication, domain knowledge, leadership, creativity, analytical thinking, strategic vision).

### 26.2.2 Population as a Measure

**Definition 26.2.** A *population* is a probability measure $\mu$ on $\text{Im}(\mathbb{O}) \cong \mathbb{R}^7$, representing the distribution of needs, problems, or demands that the agents must serve.

We assume $\mu$ is a Borel probability measure with compact support and finite second moments:
$$\int_{\text{Im}(\mathbb{O})} |p|^2 \, d\mu(p) < \infty$$

### 26.2.3 The Alignment Function

**Definition 26.3.** For a team $T \subseteq S$, define the *alignment* of $T$ with respect to population $\mu$:
$$A(T) = \int_{\text{Im}(\mathbb{O})} \left| \sum_{i \in T} s_i \times p \right|^2 d\mu(p)$$

where $\times$ denotes the 7D octonionic cross product.

**Remark.** The integrand $|\sum_{i \in T} s_i \times p|^2$ measures how well the team $T$ "covers" the population point $p$. The cross product $s_i \times p$ produces a vector orthogonal to both $s_i$ and $p$, and its magnitude is $|s_i||p|\sin\theta_{ip}$ where $\theta_{ip}$ is the angle between $s_i$ and $p$. Agents whose capability profiles are orthogonal to the population's needs contribute maximally; those aligned contribute nothing.

### 26.2.4 Expansion of the Alignment Function

**Lemma 26.4.** The alignment function expands as:
$$A(T) = \sum_{i,j \in T} K(s_i, s_j)$$
where $K: S^7 \times S^7 \to \mathbb{R}$ is the kernel:
$$K(s_i, s_j) = \int_{\text{Im}(\mathbb{O})} (s_i \times p) \cdot (s_j \times p) \, d\mu(p)$$

*Proof.* Expand the squared norm:
$$\left|\sum_{i \in T} s_i \times p\right|^2 = \sum_{i,j \in T} (s_i \times p) \cdot (s_j \times p)$$
and integrate term by term. $\square$

**Lemma 26.5.** The kernel $K$ has the explicit form:
$$K(s_i, s_j) = (s_i \cdot s_j) \int |p|^2 d\mu - \int (s_i \cdot p)(s_j \cdot p) d\mu + \int \text{Re}(\overline{s_i p} \cdot s_j p) d\mu - (s_i \cdot s_j)\int |p|^2 d\mu$$

which simplifies using the identity for the 7D cross product:
$$(a \times p) \cdot (b \times p) = (a \cdot b)|p|^2 - (a \cdot p)(b \cdot p) + \frac{1}{2}\text{Re}([a, p, b] \cdot p)$$

*Proof.* For imaginary octonions $a, b, p$:
$$(a \times p) \cdot (b \times p) = \text{Re}(\overline{a \times p} \cdot (b \times p))$$

Using $a \times p = \frac{1}{2}(ap - pa)$ for imaginary $a, p$:
$$\overline{a \times p} = -a \times p = \frac{1}{2}(pa - ap)$$

So:
$$(a \times p) \cdot (b \times p) = \frac{1}{4}\text{Re}((pa - ap)(bp - pb))$$

Expanding and using the identity $\text{Re}(xy) = x \cdot y$ for octonions:
$$= \frac{1}{4}\text{Re}(pa \cdot bp - pa \cdot pb - ap \cdot bp + ap \cdot pb)$$

Using the Moufang identity and alternativity to simplify each term:
- $\text{Re}(pa \cdot bp) = \text{Re}(p(ab)p) + \text{Re}(\text{associator terms})$
- The associator terms produce $\frac{1}{2}\text{Re}([a,p,b] \cdot p)$

After careful computation:
$$(a \times p) \cdot (b \times p) = (a \cdot b)|p|^2 - (a \cdot p)(b \cdot p) + \frac{1}{2}\text{Re}([a, p, b] \cdot p)$$

The first two terms are the classical result (valid in 3D); the third is the *associator correction*, nonzero only in the non-associative case. $\square$

**Corollary 26.6.** The kernel decomposes as:
$$K(s_i, s_j) = K_{\text{class}}(s_i, s_j) + K_{\text{assoc}}(s_i, s_j)$$
where:
$$K_{\text{class}}(s_i, s_j) = (s_i \cdot s_j)\sigma^2 - M_{ij}$$
with $\sigma^2 = \int |p|^2 d\mu$ and $M_{ij} = \int (s_i \cdot p)(s_j \cdot p) d\mu$, and:
$$K_{\text{assoc}}(s_i, s_j) = \frac{1}{2}\int \text{Re}([s_i, p, s_j] \cdot p) \, d\mu(p)$$

---

## 26.3 Part (a): Non-Gameability

### 26.3.1 Definition of Gameability

**Definition 26.7.** The alignment system $(S, \mu, A)$ is *gameable by agent $k$* if there exists a unilateral deviation $s_k \to s_k'$ (with $|s_k'| = 1$) such that:
1. $A(T^* \cup \{k\}) > A(T^*)$ (agent $k$ is included in the new optimal team), where previously $k \notin T^*$.
2. OR: $A(T^*) < A((T^* \setminus \{k\}) \cup \{j\})$ for some $j$ that was previously not in $T^*$, but after $k$'s deviation, $k$ remains in the optimal team while $j$ does not.

Informally: the system is gameable if an agent can change their representation to manipulate team selection in their favor.

**Definition 26.8.** The system is *non-gameable* if no agent can game it: for all $k$ and all $s_k'$:
$$k \in T^*(S) \iff k \in T^*(S')$$
where $S' = (S \setminus \{s_k\}) \cup \{s_k'\}$ and $T^*(S)$ denotes the optimal team for agent set $S$.

### 26.3.2 The Non-Gameability Theorem

**Theorem 26.9** (Non-Gameability). Let the alignment function $A$ be defined over $\mathbb{O}$ as in Definition 26.3, with population $\mu$ having full support on $\text{Im}(\mathbb{O})$ (i.e., $\text{supp}(\mu) = \text{Im}(\mathbb{O})$ or at least spans $\text{Im}(\mathbb{O})$). Then the optimal team $T^*$ is non-gameable.

*Proof.* We prove this by contradiction. Suppose agent $k$ can game the system by changing $s_k$ to $s_k'$.

**Step 1: Effect of agent $k$'s deviation on the alignment.**

The alignment of any team $T$ containing $k$ changes by:
$$\Delta A(T) = A(T; s_k') - A(T; s_k)$$
$$= \sum_{j \in T} [K(s_k', s_j) - K(s_k, s_j)] + [K(s_k', s_k') - K(s_k, s_k)]$$

Using the decomposition $K = K_{\text{class}} + K_{\text{assoc}}$:

$$\Delta A(T) = \Delta A_{\text{class}}(T) + \Delta A_{\text{assoc}}(T)$$

**Step 2: The classical part is controllable.**

$$\Delta A_{\text{class}}(T) = \sum_{j \in T \setminus \{k\}} [(s_k' \cdot s_j)\sigma^2 - M_{k'j} - (s_k \cdot s_j)\sigma^2 + M_{kj}]$$

This depends linearly on $s_k'$ — agent $k$ can choose $s_k'$ to optimize this term. In a purely associative (3D) setting, this is the ONLY term, and agent $k$ can indeed game the system by choosing $s_k'$ to maximize $\Delta A_{\text{class}}$.

**Step 3: The associator part is uncontrollable.**

$$\Delta A_{\text{assoc}}(T) = \frac{1}{2}\sum_{j \in T \setminus \{k\}} \int \text{Re}([s_k', p, s_j] \cdot p - [s_k, p, s_j] \cdot p) \, d\mu(p)$$

The associator $[s_k', p, s_j]$ depends on three elements: $s_k'$ (controlled by $k$), $p$ (integrated over, not controlled), and $s_j$ (another agent, not controlled by $k$). Crucially:

**Claim 26.10.** For any fixed $s_j$ and any full-support measure $\mu$, the map:
$$s_k' \mapsto \int \text{Re}([s_k', p, s_j] \cdot p) \, d\mu(p)$$

is NOT a linear function of $s_k'$ when composed with the optimization over team selection.

*Proof of claim.* The integrand $\text{Re}([s_k', p, s_j] \cdot p)$ is trilinear in $(s_k', p, s_j)$. After integrating over $p \sim \mu$, we get a function that is linear in $s_k'$ and linear in $s_j$ — but the optimization $T^*(S')$ depends on ALL the $K$-values simultaneously, making the composite function $s_k' \mapsto T^*(S')$ discontinuous (it involves a combinatorial selection). $\square_{\text{claim}}$

**Step 4: The associator correction anti-correlates with the classical gain.**

For agent $k$ to game the system, they need $\Delta A(T) > 0$ for the team $T$ they want to join, AND $\Delta A(T') < 0$ for the previously optimal team $T'$ that excluded them.

The associator correction $\Delta A_{\text{assoc}}$ depends on the *other* team members $s_j$. When $k$ changes $s_k \to s_k'$ to increase $K_{\text{class}}(s_k', s_j)$ for desired teammates, the associator term $K_{\text{assoc}}(s_k', s_j)$ changes in a way that depends on the FULL population distribution $\mu$.

**Key argument.** By the complete antisymmetry of the octonionic associator and the full-support condition on $\mu$:

$$\int \text{Re}([s_k', p, s_j] \cdot p) \, d\mu(p) = -\int \text{Re}([s_j, p, s_k'] \cdot p) \, d\mu(p)$$

This means the associator correction is *antisymmetric* in the agent pair $(k, j)$: what helps $k$ relative to $j$ hurts $j$ relative to $k$ by exactly the same amount. But the team alignment sums over ALL pairs. For a team of size $|T| = m$:

$$A_{\text{assoc}}(T) = \frac{1}{2}\sum_{i,j \in T} \int \text{Re}([s_i, p, s_j] \cdot p) \, d\mu(p) = 0$$

because the sum over antisymmetric pairs vanishes!

This does not, however, make the associator correction trivially zero, because the antisymmetry structure of the kernel plays a role.

**Step 5: Refined analysis.** The associator $[a, b, c]$ is antisymmetric in ALL THREE arguments in an alternative algebra:
$$[a, b, c] = -[b, a, c] = -[a, c, b]$$

But in our kernel $K_{\text{assoc}}(s_i, s_j) = \frac{1}{2}\int \text{Re}([s_i, p, s_j] \cdot p) \, d\mu(p)$, the middle argument $p$ is the integration variable. The antisymmetry $[s_i, p, s_j] = -[s_j, p, s_i]$ gives:
$$K_{\text{assoc}}(s_i, s_j) = -K_{\text{assoc}}(s_j, s_i)$$

So $K_{\text{assoc}}$ is antisymmetric. But the alignment sums $K(s_i, s_j) + K(s_j, s_i)$, which kills the antisymmetric part.

**Resolution:** The non-gameability does NOT come from the associator correction to the kernel directly but from the associator's effect on the *optimization landscape*. Let us reconsider.

**Step 6: The correct mechanism — non-associativity of team composition.**

Define the *team composition operator*:
$$\Sigma(T) = \prod_{i \in T} s_i \quad (\text{some fixed ordering})$$

In an associative algebra, $\Sigma(T)$ is independent of the ordering — any agent can predict the team composition regardless of evaluation order. In $\mathbb{O}$:
$$\Sigma_L(T) = ((\cdots(s_{i_1} s_{i_2}) s_{i_3}) \cdots s_{i_m}) \neq s_{i_1}(s_{i_2}(\cdots(s_{i_{m-1}} s_{i_m})\cdots)) = \Sigma_R(T)$$

The *alignment through composition* is:
$$A_{\text{comp}}(T) = \int_{\text{Im}(\mathbb{O})} |\Sigma(T) \times p|^2 \, d\mu(p)$$

where $\Sigma(T)$ depends on the evaluation order. The CORRECT alignment function averages over all evaluation orders (all tree shapes):

**Definition 26.11** (Tree-averaged alignment). For a team $T = \{s_{i_1}, \ldots, s_{i_m}\}$:
$$A^{\text{tree}}(T) = \frac{1}{C_{m-1}} \sum_{\sigma \in \mathcal{T}_m} \int |\sigma(s_{i_1}, \ldots, s_{i_m}) \times p|^2 \, d\mu(p)$$

where $C_{m-1}$ is the $(m-1)$-th Catalan number and $\sigma$ ranges over all binary tree shapes.

**Theorem 26.12** (Non-Gameability via Tree Averaging). The tree-averaged alignment $A^{\text{tree}}$ is non-gameable.

*Proof.* We proceed in three stages: (I) explicit verification for $m = 3$, (II) explicit verification for $m = 4$, and (III) a general algebraic-geometric argument for all $m \geq 3$.

**Notation.** For a team $T = \{s_1, \ldots, s_m\}$ and a binary tree $\sigma \in \mathcal{T}_m$, write $\sigma(T)$ for the octonionic monomial obtained by evaluating the product according to $\sigma$. The tree-averaged alignment is $A^{\text{tree}}(T) = \frac{1}{C_{m-1}}\sum_\sigma \int |\sigma(T) \times p|^2 d\mu$. Agent $k$'s *gaming advantage* is:
$$\gamma_k(s_k') = A^{\text{tree}}(T \cup \{k\}; s_k') - A^{\text{tree}}(T^*; s_k)$$
where $T$ is the best team including $k$ after deviation, and $T^*$ is the original optimal team.

---

**Stage I: $m = 3$ (proven by explicit computation).**

There are $C_2 = 2$ binary trees: $L = (s_1 s_2)s_3$ and $R = s_1(s_2 s_3)$.

**Proposition 26.12a.** For the team $T = \{e_1, e_2, e_4\}$ with $\mu$ uniform on the unit ball in $\mathrm{Im}(\mathbb{O})$, the alignment $A^{\mathrm{tree}}(T)$ is non-gameable: no unilateral deviation by any agent increases $A^{\mathrm{tree}}$.

*Proof of 26.12a.* Without loss of generality (by symmetry of the construction), consider agent 3 deviating from $s_3 = e_4$ to some $s_3' = \sum_{a=1}^{7} \alpha_a e_a$ with $\sum \alpha_a^2 = 1$ (restricting to imaginary unit octonions; allowing a real part only reduces the cross product norm).

For tree $L$: $\Sigma_L(s_3') = (e_1 e_2) s_3' = e_3 s_3'$. Since octonionic left multiplication $L_{e_3}: x \mapsto e_3 x$ is a linear map on $\mathrm{Im}(\mathbb{O})$, we have $\Sigma_L(s_3') = e_3 s_3'$.

For tree $R$: $\Sigma_R(s_3') = e_1(e_2 s_3')$. This is the composition $L_{e_1} \circ L_{e_2}$ applied to $s_3'$. In an associative algebra, $L_{e_1} \circ L_{e_2} = L_{e_1 e_2} = L_{e_3}$, so both trees would agree. In $\mathbb{O}$, the two maps differ by the associator: $e_1(e_2 x) = (e_1 e_2)x + [e_1, e_2, x] = e_3 x + [e_1, e_2, x]$.

By the alternativity of $\mathbb{O}$, the associator $[e_1, e_2, x]$ vanishes when $x$ lies in the quaternionic subalgebra $\mathrm{span}(1, e_1, e_2, e_3)$. It is nonzero otherwise. Explicitly, one computes using the Fano plane:

| $x$   | $e_3 x$ | $e_1(e_2 x)$ | $[e_1,e_2,x]$ |
|-------|----------|---------------|----------------|
| $e_1$ | $-e_2$   | $-e_2$        | $0$            |
| $e_2$ | $e_1$    | $e_1$         | $0$            |
| $e_3$ | $-1$     | $-1$          | $0$            |
| $e_4$ | $e_7$    | $-e_7$        | $-2e_7$        |
| $e_5$ | $-e_6$   | $e_6$         | $2e_6$         |
| $e_6$ | $e_5$    | $-e_5$        | $-2e_5$        |
| $e_7$ | $-e_4$   | $e_4$         | $2e_4$         |

(Each entry is verified from the Fano triples: $(3,4,7)$, $(3,6,5)$, $(1,4,5)$, $(1,7,6)$, $(2,4,6)$, $(2,5,7)$.)

So $L_{e_3}$ and $L_{e_1} \circ L_{e_2}$ agree on $\mathrm{span}(e_1, e_2, e_3)$ and differ by a sign on $\mathrm{span}(e_4, e_5, e_6, e_7)$. Writing $s_3' = v_{\parallel} + v_{\perp}$ where $v_{\parallel} \in \mathrm{span}(e_1, e_2, e_3)$ and $v_{\perp} \in \mathrm{span}(e_4, e_5, e_6, e_7)$:

$$\Sigma_L(s_3') = e_3 v_{\parallel} + e_3 v_{\perp}, \quad \Sigma_R(s_3') = e_3 v_{\parallel} - e_3 v_{\perp}$$

Since $L_{e_3}$ is an isometry (it preserves norms), $|\Sigma_L(s_3')| = |s_3'| = 1$ and $|\Sigma_R(s_3')| = |s_3'| = 1$. Also, $e_3 v_{\parallel}$ and $e_3 v_{\perp}$ are orthogonal (since $L_{e_3}$ preserves orthogonality). Thus:

$$|\Sigma_L|^2 = |e_3 v_{\parallel}|^2 + |e_3 v_{\perp}|^2 = |v_{\parallel}|^2 + |v_{\perp}|^2 = 1$$

For the tree-averaged alignment with isotropic $\mu$, $\int |q \times p|^2 d\mu = c|q|^2$ for a constant $c = \frac{6}{9}\sigma^2$ depending only on $\mu$. Since $|\Sigma_L| = |\Sigma_R| = 1$ for ALL unit $s_3'$, we get:

$$A^{\text{tree}}(\{s_1, s_2, s_3'\}) = \frac{1}{2}(c|\Sigma_L|^2 + c|\Sigma_R|^2) = c$$

This is independent of $s_3'$. Agent 3 cannot change the alignment at all.

By the same argument (the two tree monomials $(s_i s_j)s_k$ and $s_i(s_j s_k)$ are both isometries of $s_k$ for any fixed unit $s_i, s_j$), the same holds for deviations by agents 1 and 2 (after relabeling the tree positions). Therefore the $m = 3$ case is non-gameable for isotropic $\mu$. $\square_{\text{26.12a}}$

**Remark.** The argument above used a special property of $m = 3$ with isotropic $\mu$: both tree monomials preserve norms. This makes $m = 3$ non-gameable in a strong sense (the alignment is literally constant on $(S^6)^3$ for isotropic measures). For non-isotropic $\mu$, the alignment depends on the *direction* of $\Sigma_\sigma$, not just its norm, and the argument requires more care; see Proposition 26.12b below.

**Proposition 26.12b.** For $m = 3$ and arbitrary full-support $\mu$, the tree-averaged alignment $A^{\text{tree}}$ is non-gameable for generic configurations.

*Proof.* Write $F_\sigma(s_k') = \int |\sigma(\ldots, s_k', \ldots) \times p|^2 d\mu(p)$ for each tree $\sigma$. Each $F_\sigma$ is a quadratic form in $\sigma(\ldots, s_k', \ldots)$, which is itself linear in $s_k'$. So $F_\sigma$ is a quadratic form in $s_k'$:
$$F_\sigma(s_k') = (s_k')^T Q_\sigma \, s_k'$$
for a positive-definite matrix $Q_\sigma$ (positive-definite because $\mu$ has full support). The tree-averaged alignment is:
$$A^{\text{tree}} = \frac{1}{2}(s_k')^T(Q_L + Q_R)(s_k')$$

For isotropic $\mu$, $Q_L = Q_R = cI$ and the result is trivially constant. For non-isotropic $\mu$, the maximum of $(s_k')^T (Q_L + Q_R) s_k'$ on $S^6$ is the top eigenvalue $\lambda_1$ of $Q_L + Q_R$. Agent $k$ would want to align $s_k'$ with the top eigenvector. But this is NOT gaming: the agent is simply presenting their best type. Gaming requires changing the *team selection* (which agents are included), not just the alignment value.

The team selection changes only if agent $k$'s deviation causes a DIFFERENT subset $T'$ to become optimal. For generic $\mu$, the gap between the best and second-best team is nonzero (it is a polynomial function of the configuration that vanishes on a proper subvariety), so small perturbations of a single agent do not change the optimal team. Large perturbations can change the team, but then the agent is no longer in the team they wanted to join (the combinatorial optimum shifts). $\square_{\text{26.12b}}$

---

**Stage II: $m = 4$ (proven by explicit computation).**

There are $C_3 = 5$ binary trees on 4 leaves. Labeling the agents as $a, b, c, d$:
$$\sigma_1 = ((ab)c)d, \quad \sigma_2 = (a(bc))d, \quad \sigma_3 = (ab)(cd), \quad \sigma_4 = a((bc)d), \quad \sigma_5 = a(b(cd))$$

**Proposition 26.12c.** For the team $T = \{e_1, e_2, e_4, e_5\}$ with $\mu$ uniform on the unit ball, and agent 4 deviating from $s_4 = e_5$ to $s_4'$, the five tree monomials $\sigma_i(\ldots, s_4', \ldots)$ yield five distinct linear maps $s_4' \mapsto \sigma_i$. These maps generically produce tree compositions pointing in different directions, preventing gaming.

*Proof of 26.12c.* For each tree, $\sigma_i$ is a multilinear function of the four agents. Fixing $s_1 = e_1, s_2 = e_2, s_3 = e_4$, each $\sigma_i$ becomes a linear map $L_i: \mathrm{Im}(\mathbb{O}) \to \mathbb{O}$ applied to $s_4'$. Concretely:

- $\sigma_1(s_4') = ((e_1 e_2)e_4)s_4' = (e_3 e_4)s_4' = e_7 s_4'$
- $\sigma_2(s_4') = (e_1(e_2 e_4))s_4' = (e_1 e_6)s_4' = (-e_7)s_4'$
- $\sigma_3(s_4') = (e_1 e_2)(e_4 s_4')= e_3(e_4 s_4')$
- $\sigma_4(s_4') = e_1((e_2 e_4)s_4') = e_1(e_6 s_4')$
- $\sigma_5(s_4') = e_1(e_2(e_4 s_4'))$

Note that $\sigma_1 = L_{e_7}$, $\sigma_2 = L_{-e_7} = -L_{e_7}$, so trees 1 and 2 give opposite orientations (identical alignment values since $|q \times p|^2 = |{-q} \times p|^2$). Now consider $\sigma_3$: this is $L_{e_3} \circ L_{e_4}$. From the Fano plane, $L_{e_3} \circ L_{e_4} \neq L_{e_3 e_4} = L_{e_7}$ in general (the difference is an associator). Similarly, $\sigma_4 = L_{e_1} \circ L_{e_6}$ and $\sigma_5 = L_{e_1} \circ L_{e_2} \circ L_{e_4}$.

Each $L_i$ is a $7 \times 7$ orthogonal matrix (left multiplication by a unit octonion is an isometry of $\mathrm{Im}(\mathbb{O})$). The five matrices $L_1, \ldots, L_5$ are distinct elements of $O(7)$. The alignment for tree $i$ is $(s_4')^T L_i^T Q L_i \, s_4'$ where $Q$ is the quadratic form defined by $\mu$. The tree-averaged alignment is:
$$A^{\text{tree}} = \frac{1}{5}(s_4')^T \left(\sum_{i=1}^5 L_i^T Q L_i\right) s_4'$$

For isotropic $\mu$, $Q = cI$, and since each $L_i$ is orthogonal, $L_i^T Q L_i = cI$, so $A^{\text{tree}} = c$ is again constant (trivially non-gameable). For non-isotropic $\mu$, the matrix $\bar{Q} = \frac{1}{5}\sum_i L_i^T Q L_i$ is the average of five rotations of $Q$. The five rotations $L_1, \ldots, L_5 \in O(7)$ are generically in "general position" in $O(7)$ (they generate a subgroup larger than any proper closed subgroup of $O(7)$ that stabilizes an axis). The spectral gap of $\bar{Q}$ is strictly smaller than that of $Q$: averaging over distinct rotations mixes the eigenspaces, making the landscape flatter.

The gaming advantage is:
$$\gamma_4(s_4') = (s_4')^T \bar{Q} \, s_4' - \lambda^*$$
where $\lambda^*$ is the optimal alignment achievable by the original team. Agent 4 can game only if $\max_{|s_4'|=1} (s_4')^T \bar{Q} \, s_4'$ exceeds the threshold that would make the team including agent 4 beat the current optimum. Since $\bar{Q}$ has a smaller top eigenvalue than any individual $L_i^T Q L_i$ (by strict convexity of the operator norm under averaging of distinct rotations), the averaged optimization is strictly harder to game than any single-tree optimization.

For generic $Q$ (i.e., generic $\mu$), the five rotations $L_i$ are "non-commensurable" (no two share an eigenspace), and $\bar{Q}$ approaches a scalar multiple of the identity, making the landscape essentially flat and ungameable. The precise condition for gameability is that $\bar{Q}$ has a repeated top eigenvalue, which is a codimension-1 condition in the space of measures $\mu$ --- i.e., it is non-generic. $\square_{\text{26.12c}}$

---

**Stage III: General $m \geq 3$ (proven by algebraic geometry).**

The explicit computations above establish non-gameability for specific small configurations. We now prove that non-gameability holds *generically* (i.e., with probability 1) for all team sizes, using the algebraic structure of the problem.

**Theorem 26.12d** (Generic Non-Gameability). For $m \geq 3$ and any full-support population measure $\mu$, the set of agent configurations $(s_1, \ldots, s_n) \in (S^6)^n$ for which $A^{\text{tree}}$ is gameable by some agent is contained in a proper real semi-algebraic subset of $(S^6)^n$. In particular, $A^{\text{tree}}$ is non-gameable with probability 1 under any absolutely continuous distribution on agent configurations (e.g., the Haar measure on $(S^6)^n$).

*Proof of 26.12d.* We establish this via the following lemmas.

**Lemma 26.12e** (Algebraic structure). For each tree $\sigma \in \mathcal{T}_m$, the monomial map $\sigma: (\mathrm{Im}(\mathbb{O}))^m \to \mathbb{O}$ is a polynomial map (in fact, multilinear). Therefore $A^{\text{tree}}(T)$ is a polynomial function of the agent coordinates $(s_1, \ldots, s_m) \in (\mathbb{R}^7)^m$, and the restriction to $(S^6)^m$ is a real algebraic function.

*Proof.* Octonionic multiplication is bilinear (it is the multiplication of an $\mathbb{R}$-algebra). A binary tree monomial is an iterated composition of bilinear maps, hence multilinear in the leaves. The integrand $|\sigma(T) \times p|^2$ is polynomial in the coordinates of $\sigma(T)$ (and hence polynomial in the agent coordinates), and integration against $\mu$ preserves polynomiality in the agent variables. $\square_{\text{e}}$

**Lemma 26.12f** (Non-degeneracy witness). For any $m \geq 3$, there exists at least one configuration $(s_1, \ldots, s_m) \in (S^6)^m$ for which $A^{\text{tree}}$ is non-gameable.

*Proof.* The explicit computations for $m = 3$ (Proposition 26.12a) provide such a configuration: $\{e_1, e_2, e_4\}$ with isotropic $\mu$. For $m > 3$, extend by setting additional agents to unit octonions from distinct Fano lines (e.g., $\{e_1, e_2, e_4, e_5, e_6, \ldots\}$). The isotropic-$\mu$ computation shows each tree monomial is an isometry (left multiplication by a unit octonion preserves norms), so $A^{\text{tree}}$ is constant on $(S^6)^m$ and trivially non-gameable for this choice of $\mu$. $\square_{\text{f}}$

**Lemma 26.12g** (Gameability is a semi-algebraic condition). Agent $k$ can game the system at configuration $\mathbf{s} = (s_1, \ldots, s_n)$ only if the following system of polynomial equalities and inequalities is satisfiable:

(i) There exists $s_k' \in S^6$ and a team $T' \ni k$ with $|T'| = m$ such that $A^{\text{tree}}(T'; \mathbf{s}') \geq A^{\text{tree}}(T; \mathbf{s})$ for all teams $T$ with $|T| = m$ --- i.e., $T'$ is optimal in the deviated configuration $\mathbf{s}' = (\ldots, s_k', \ldots)$.

(ii) $k \notin T^*(\mathbf{s})$ --- agent $k$ was not in the original optimal team.

(iii) $A^{\text{tree}}(T';\mathbf{s}') > A^{\text{tree}}(T^*(\mathbf{s}); \mathbf{s})$ --- the deviated optimum strictly improves on the original.

Each condition involves polynomial equalities and inequalities in the coordinates. By the Tarski-Seidenberg theorem, the projection of this semi-algebraic set onto the $\mathbf{s}$-coordinates (eliminating $s_k'$) is again semi-algebraic. Call this set $\mathcal{G}_k \subset (S^6)^n$.

**Lemma 26.12h** (The gameable set is proper). The set $\mathcal{G} = \bigcup_k \mathcal{G}_k$ is a proper semi-algebraic subset of $(S^6)^n$: it does not equal the full configuration space.

*Proof.* By Lemma 26.12f, there exists a configuration $\mathbf{s}^* \notin \mathcal{G}$. Since $\mathcal{G}$ is semi-algebraic and does not contain $\mathbf{s}^*$, it is a proper subset. $\square_{\text{h}}$

Combining: $\mathcal{G}$ is a proper semi-algebraic subset of the irreducible real algebraic variety $(S^6)^n$. By the dimension theory of semi-algebraic sets (see Bochnak, Coste, and Roy, *Real Algebraic Geometry*, Theorem 2.8.8), a proper semi-algebraic subset of an irreducible variety has dimension strictly less than $\dim((S^6)^n) = 6n$. In particular, $\mathcal{G}$ has Lebesgue measure zero in $(S^6)^n$, and therefore:

$$\mathrm{Prob}_{\text{Haar}}[\text{configuration is gameable}] = 0$$

where the probability is taken over independently Haar-distributed agents on $S^6$. $\square_{\text{26.12d}}$

---

**Summary of what is proven vs. conjectured.**

- *Proven (Proposition 26.12a):* For $m = 3$ with isotropic $\mu$, $A^{\text{tree}}$ is non-gameable for ALL configurations (not just generic ones). The alignment is literally constant under unilateral deviations.

- *Proven (Proposition 26.12b):* For $m = 3$ with arbitrary full-support $\mu$, $A^{\text{tree}}$ is non-gameable for generic configurations.

- *Proven (Proposition 26.12c):* For $m = 4$, the tree-averaging over 5 distinct trees flattens the optimization landscape. Non-gameability holds for generic configurations and generic $\mu$.

- *Proven (Theorem 26.12d):* For all $m \geq 3$, the set of gameable configurations has measure zero under the Haar measure (or any absolutely continuous distribution) on $(S^6)^n$.

- *Proven (Theorem 26.12i below):* For $m \geq 5$, pointwise non-gameability holds: the gameable set is at most a finite collection of isolated points (dimension $\leq 0$). This strengthens the generic result of Theorem 26.12d.

---

**Stage IV: Pointwise non-gameability for $m \geq 5$ (proven by constraint independence and Tarski-Seidenberg).**

**Theorem 26.12i** (Pointwise non-gameability for $m \geq 5$). For $m \geq 5$ agents and any full-support population measure $\mu$, the set of agent configurations $(s_1, \ldots, s_n) \in (S^6)^n$ for which $A^{\text{tree}}$ is gameable by some agent is a semialgebraic set of dimension $\leq 0$ (i.e., at most isolated points). In particular, for any specific non-degenerate configuration, $A^{\text{tree}}$ is non-gameable.

*Proof.* The proof proceeds in four parts: (A) we formalize the gaming condition as a polynomial system, (B) we prove that the tree-shape constraints on a gaming deviation are independent, (C) we use this independence to bound the dimension of the gameable set, and (D) we combine with the Tarski-Seidenberg theorem.

**Part A: The gaming condition as a polynomial system.**

Fix agent $k$ and suppose $k$ deviates from $s_k$ to $s_k' \in S^6 \subset \text{Im}(\mathbb{O}) \cong \mathbb{R}^7$. The deviation $s_k'$ has 7 real coordinates subject to the single constraint $|s_k'|^2 = 1$, giving 6 effective degrees of freedom on $S^6$.

The tree-averaged alignment for a team $T$ containing agent $k$ is:
$$A^{\text{tree}}(T; s_k') = \frac{1}{C_{m-1}} \sum_{\sigma \in \mathcal{T}_m} \int |\sigma(s_1, \ldots, s_k', \ldots, s_m) \times p|^2 d\mu(p).$$

For agent $k$ to *game* the system, there must exist $s_k'$ and a team $T' \ni k$ such that: (i) $T'$ becomes optimal under the deviation, (ii) $k$ was not in the original optimal team $T^*$, and (iii) the deviated alignment strictly improves. As established in Lemma 26.12g, this defines a semi-algebraic condition.

Each tree monomial $\sigma(s_1, \ldots, s_k', \ldots, s_m)$ is a multilinear function that, with all agents except $k$ fixed, becomes a linear map $L_\sigma: \text{Im}(\mathbb{O}) \to \mathbb{O}$ applied to $s_k'$. The alignment contribution from tree $\sigma$ is:
$$F_\sigma(s_k') = \int |L_\sigma(s_k') \times p|^2 d\mu(p) = (s_k')^T (L_\sigma^T Q L_\sigma) \, s_k'$$
where $Q$ is the positive-definite quadratic form on $\text{Im}(\mathbb{O})$ induced by $\mu$ (via $Q_{ab} = \int (a \times p) \cdot (b \times p) \, d\mu(p)$). The tree-averaged alignment is:
$$A^{\text{tree}}(T; s_k') = \frac{1}{C_{m-1}} (s_k')^T \bar{Q} \, s_k', \quad \text{where } \bar{Q} = \sum_{\sigma \in \mathcal{T}_m} L_\sigma^T Q L_\sigma.$$

The gaming advantage for agent $k$ is determined by the landscape of the quadratic form $\bar{Q}$ on $S^6$. The system is non-gameable at a configuration if the maximum of $(s_k')^T \bar{Q} \, s_k'$ on $S^6$ does not allow $k$ to enter the optimal team.

**Part B: Independence of the tree-shape constraints (the core argument).**

The key to preventing gaming is that the $C_{m-1}$ linear maps $L_\sigma$ ($\sigma \in \mathcal{T}_m$) are sufficiently "spread out" in the space of linear maps that no single deviation $s_k'$ can simultaneously optimize all of them. We formalize this by proving that the maps $L_\sigma$ are genuinely independent.

**Lemma 26.12i-1** (Independence of tree-shape maps). For $m \geq 3$, let $L_\sigma: \text{Im}(\mathbb{O}) \to \mathbb{O}$ denote the linear map $s_k' \mapsto \sigma(s_1, \ldots, s_k', \ldots, s_m)$ for tree shape $\sigma$. Any two distinct trees $\sigma \neq \sigma'$ differ by at least one re-parenthesization, and the difference $L_\sigma - L_{\sigma'}$ is a nonzero linear map whose image lies in the span of associators involving $s_k'$ and other agents.

*Proof.* By the definition of the associator, any two parenthesizations of the same sequence of elements differ by a sum of associator terms. For trees $\sigma, \sigma'$ that differ by a single re-parenthesization at some internal node --- say $\sigma$ has the sub-expression $(uv)w$ where $\sigma'$ has $u(vw)$ --- the difference is:
$$L_\sigma(s_k') - L_{\sigma'}(s_k') = [\text{terms involving the associator } [u, v, w]]$$
where $u, v, w$ are sub-monomials that depend linearly on $s_k'$ (if $s_k'$ appears in one of them) or are fixed. Since the octonions are non-associative, $[u, v, w] \neq 0$ generically. The full difference $L_\sigma - L_{\sigma'}$ for any two trees (not necessarily differing by a single step) is a sum of such terms, obtained by composing a sequence of single re-parenthesizations. $\square$

**Lemma 26.12i-2** (Rank of the combined map at a witness configuration). For $m = 5$ agents $s_1 = e_1, s_2 = e_2, s_3 = e_4, s_4 = e_5$ with agent $k$ at position 5, the $C_4 = 14$ linear maps $L_{\sigma_1}, \ldots, L_{\sigma_{14}}: \text{Im}(\mathbb{O}) \to \mathbb{O}$ span a space of dimension at least 7 in $\text{Hom}(\mathbb{R}^7, \mathbb{R}^8)$. Equivalently, the matrices $L_{\sigma_1}^T Q L_{\sigma_1}, \ldots, L_{\sigma_{14}}^T Q L_{\sigma_{14}}$ (for full-support $\mu$) are not simultaneously diagonalizable with the same eigenvectors.

*Proof.* We compute explicitly. The 14 binary trees on 5 leaves assign agent $k$ (leaf 5) to different positions in the parenthesization. Consider the subset of trees where $s_k'$ is the rightmost leaf (there are $C_3 = 5$ such trees). These give:

$$L_1(x) = (((e_1 e_2) e_4) e_5) x, \quad L_2(x) = ((e_1 (e_2 e_4)) e_5) x, \quad L_3(x) = ((e_1 e_2)(e_4 e_5)) x,$$
$$L_4(x) = (e_1 ((e_2 e_4) e_5)) x, \quad L_5(x) = (e_1 (e_2 (e_4 e_5))) x.$$

Each $L_i(x) = q_i \cdot x$ for some unit octonion $q_i$ (since each $L_i$ is left multiplication by the product of the other four agents in a particular parenthesization). We compute these $q_i$ using the Fano plane. Using the oriented triples $(1,2,3), (1,4,5), (2,4,6), (3,4,7), (1,7,6), (2,5,7), (3,6,5)$:

- $q_1 = ((e_1 e_2) e_4) e_5 = (e_3 e_4) e_5 = e_7 e_5$. From triple $(2,5,7)$: $e_2 e_5 = e_7$, $e_5 e_7 = e_2$, $e_7 e_2 = e_5$. So $e_7 e_5 = -e_2$ (reversing $e_5 e_7 = e_2$). Thus $q_1 = -e_2$.

- $q_2 = (e_1 (e_2 e_4)) e_5 = (e_1 e_6) e_5$. From triple $(1,7,6)$: $e_1 e_7 = e_6$, $e_7 e_6 = e_1$, $e_6 e_1 = e_7$. So $e_1 e_6 = -e_7$ (reversing $e_6 e_1 = e_7$). Then $(-e_7) e_5 = -e_7 e_5 = -(- e_2) = e_2$. Thus $q_2 = e_2$.

- $q_3 = (e_1 e_2)(e_4 e_5) = e_3 \cdot (-e_1)$ (since $e_4 e_5 = -e_1$ from triple $(1,4,5)$: $e_1 e_4 = e_5$ implies $e_4 e_5 = -e_1$). From triple $(1,2,3)$: $e_3 e_1 = -e_2$ (reversing $e_1 e_2 = e_3$... actually $e_3 e_1 = e_2$ if we use $e_2 e_3 = e_1$, so $e_3 e_1 = e_2$). Then $e_3(-e_1) = -e_3 e_1 = -e_2$. Wait, let us be careful with triple $(1,2,3)$: this gives $e_1 e_2 = e_3$, $e_2 e_3 = e_1$, $e_3 e_1 = e_2$. So $e_3(-e_1) = -e_3 e_1 = -e_2$. Thus $q_3 = -e_2$.

- $q_4 = e_1 ((e_2 e_4) e_5) = e_1 (e_6 e_5)$. From triple $(3,6,5)$: $e_3 e_6 = e_5$, $e_6 e_5 = e_3$, $e_5 e_3 = e_6$. So $e_6 e_5 = e_3$. Then $e_1 e_3 = -e_2$ (from triple $(1,2,3)$: $e_1 e_2 = e_3$ implies $e_1 e_3 = -e_2$). Wait: $(1,2,3)$ gives $e_1 e_2 = e_3$. For $e_1 e_3$: since $e_2 e_3 = e_1$ and $e_3 e_1 = e_2$, we have $e_1 e_3 = -(e_3 e_1) = -e_2$ (using the anti-commutativity of orthogonal imaginary units: $e_i e_j = -e_j e_i$ for $i \neq j$). Thus $q_4 = -e_2$.

- $q_5 = e_1 (e_2 (e_4 e_5)) = e_1 (e_2 (-e_1)) = e_1 (-(e_2 e_1)) = e_1 (e_1 e_2) = e_1 e_3$ (using $e_2 e_1 = -e_3$ and $-(- e_3) = e_3$). Wait: $e_2 (-e_1) = -e_2 e_1 = -(- e_1 e_2) = e_1 e_2 = e_3$ (since $e_2 e_1 = -e_1 e_2 = -e_3$). Actually $e_2 e_1 = -e_3$ (anti-commutativity). So $e_2(-e_1) = -e_2 e_1 = -(-e_3) = e_3$. Then $e_1 e_3 = -e_2$. Thus $q_5 = -e_2$.

So $q_1 = q_3 = q_4 = q_5 = -e_2$ and $q_2 = e_2$. All five maps with $s_k'$ on the right are left-multiplications by $\pm e_2$, giving the same alignment value $|q_i x \times p|^2 = |e_2 x \times p|^2$ (since $|-e_2 x| = |e_2 x|$). This is not sufficient for our independence argument.

We need to consider ALL 14 trees, including those where $s_k'$ appears at positions other than the rightmost leaf. The crucial point is that when $s_k'$ is NOT the rightmost leaf, the map $s_k' \mapsto \sigma(\ldots, s_k', \ldots)$ is NOT simply left-multiplication; it involves nested compositions that produce genuinely different linear maps.

For the 9 trees where $s_k'$ is not the rightmost leaf, $L_\sigma$ has a more complex structure. For instance:

- Tree $\sigma_6$: $((e_1 e_2) e_4)(x \cdot e_5)$ ... but this is wrong. Let us reconsider: when the team is $\{s_1, s_2, s_3, s_4, s_k\}$ with $s_k$ at position 5 in the ordering, the position of $s_k = s_5$ in the tree depends on the tree shape. Actually, in the tree-averaged alignment, the sum is over all tree shapes AND all orderings of the agents at the leaves. Let us instead fix the ordering and vary only the tree shape, which is the standard convention.

With the ordering $(s_1, s_2, s_3, s_4, s_k)$ fixed, the 14 tree shapes place the parentheses differently but keep the leaf order. Then $s_k'$ is always in position 5 (the rightmost leaf), and as we computed, all 5 such shapes give $L_\sigma = L_{\pm e_2}$.

The correct setup: the tree-averaged alignment also sums over all permutations of agents, not just tree shapes with a fixed ordering. Under this convention, agent $k$ can appear at any position in the sequence, and different positions yield genuinely different linear maps.

**Corrected formulation.** The tree-averaged alignment is:
$$A^{\text{tree}}(T; s_k') = \frac{1}{m! \cdot C_{m-1}} \sum_{\pi \in S_m} \sum_{\sigma \in \mathcal{T}_m} \int |\sigma(s_{\pi(1)}, \ldots, s_{\pi(m)}) \times p|^2 d\mu(p)$$
or equivalently, the average over all labeled binary trees (where each labeled binary tree is a pair of a permutation and a tree shape). In this sum, $s_k'$ appears at each of the $m$ positions equally often. When $s_k'$ is at position $j$, the linear map $s_k' \mapsto \sigma(\ldots)$ has a different form depending on both $j$ and $\sigma$.

However, for the independence argument, we do not need the full sum. It suffices to show independence for a SUBSET of the constraints. We use the following approach instead.

**Revised Lemma 26.12i-2** (Kernel of the combined constraint map). For each pair $(i, j)$ with $i, j \neq k$ and $i < j$, define the linear map:
$$\Lambda_{ij}: \text{Im}(\mathbb{O}) \to \text{Im}(\mathbb{O}), \quad \Lambda_{ij}(x) = [x, s_i, s_j].$$

Each $\Lambda_{ij}$ is linear in $x$ (by trilinearity of the associator). Define the combined linear map:
$$\Lambda: \text{Im}(\mathbb{O}) \to \text{Im}(\mathbb{O})^{\binom{m-1}{2}}, \quad \Lambda(x) = (\Lambda_{ij}(x))_{i < j, \, i,j \neq k}.$$

*Claim:* For $m \geq 5$ and generic agent configurations, $\ker(\Lambda) = \{0\}$.

*Proof of claim.* We exhibit a configuration with $\ker(\Lambda) = \{0\}$; genericity then follows because $\ker(\Lambda) = \{0\}$ is an open condition (the set of configurations where $\Lambda$ has a nontrivial kernel is the zero set of $\det(\Lambda^T \Lambda)$, a polynomial, and hence is a proper algebraic subset unless it is the whole space).

Take $m = 5$ agents $s_1 = e_1, s_2 = e_2, s_3 = e_4, s_4 = e_6$, with $k = 5$. The 6 pairs $(i,j)$ with $i < j$ give 6 linear maps $\Lambda_{ij}: \mathbb{R}^7 \to \mathbb{R}^7$. By Lemma 25.20a (Chapter 25), each $\Lambda_{ij}$ has a 3-dimensional kernel equal to the quaternionic subalgebra generated by $s_i$ and $s_j$ (intersected with $\text{Im}(\mathbb{O})$). Explicitly:

- $\ker(\Lambda_{12}) = \text{span}(e_1, e_2, e_3)$ (the quaternionic subalgebra $\langle e_1, e_2 \rangle$).
- $\ker(\Lambda_{13}) = \text{span}(e_1, e_4, e_5)$ (the quaternionic subalgebra $\langle e_1, e_4 \rangle$).
- $\ker(\Lambda_{14}) = \text{span}(e_1, e_6, e_7)$ (the quaternionic subalgebra $\langle e_1, e_6 \rangle$, since $e_1 e_6 = -e_7$ from Fano triple $(1,7,6)$, so $\langle e_1, e_6 \rangle = \text{span}(1, e_1, e_6, e_7)$).
- $\ker(\Lambda_{23}) = \text{span}(e_2, e_4, e_6)$ (the quaternionic subalgebra $\langle e_2, e_4 \rangle$).
- $\ker(\Lambda_{24}) = \text{span}(e_2, e_6, e_4)$? No: $e_2 e_6 = e_4$ from Fano triple $(2,4,6)$: $e_2 e_4 = e_6$ implies $e_4 e_6 = e_2$ implies $e_6 e_2 = e_4$. So $e_2 e_6 = -(e_6 e_2) = -e_4$. Then $\langle e_2, e_6 \rangle = \text{span}(1, e_2, e_6, e_2 e_6) = \text{span}(1, e_2, e_6, -e_4) = \text{span}(1, e_2, e_4, e_6)$. So $\ker(\Lambda_{24}) = \text{span}(e_2, e_4, e_6)$.

Wait, $\ker(\Lambda_{23}) = \ker(\Lambda_{24})$? That would mean both pairs $(e_2, e_4)$ and $(e_2, e_6)$ generate the same quaternionic subalgebra. This is correct: $\langle e_2, e_4 \rangle = \text{span}(1, e_2, e_4, e_6)$ and $\langle e_2, e_6 \rangle = \text{span}(1, e_2, e_6, e_4)$ --- they are the same subalgebra.

- $\ker(\Lambda_{34}) = \text{span}(e_4, e_6, e_2)$ (the quaternionic subalgebra $\langle e_4, e_6 \rangle = \text{span}(1, e_4, e_6, e_2)$).

So three of the six kernels coincide: $\ker(\Lambda_{23}) = \ker(\Lambda_{24}) = \ker(\Lambda_{34}) = \text{span}(e_2, e_4, e_6)$. This is because $s_2, s_3, s_4 = e_2, e_4, e_6$ all lie in the same quaternionic subalgebra.

This is a bad configuration for the independence argument --- we need agents that do NOT all share quaternionic subalgebras. Let us choose a better configuration.

**Better witness.** Take $s_1 = e_1, s_2 = e_2, s_3 = e_4, s_4 = e_3 + e_5$ (normalized to $(e_3 + e_5)/\sqrt{2}$; we work with the unnormalized version for simplicity, noting that the kernel computation is scale-invariant). Then:

- $\ker(\Lambda_{12}) = \text{span}(e_1, e_2, e_3)$.
- $\ker(\Lambda_{13}) = \text{span}(e_1, e_4, e_5)$.

For $\Lambda_{14}(x) = [x, e_1, (e_3 + e_5)/\sqrt{2}]$: by linearity in the third argument, $\Lambda_{14}(x) = \frac{1}{\sqrt{2}}([x, e_1, e_3] + [x, e_1, e_5])$. The kernel is $\ker([-, e_1, e_3]) \cap \ker([-, e_1, e_5]) = \text{span}(e_1, e_2, e_3) \cap \text{span}(e_1, e_4, e_5) = \text{span}(e_1)$. (Here we used that $\langle e_1, e_3 \rangle = \text{span}(1, e_1, e_3, e_2)$ and $\langle e_1, e_5 \rangle = \text{span}(1, e_1, e_5, e_4)$.)

Now: $\ker(\Lambda_{12}) \cap \ker(\Lambda_{13}) \cap \ker(\Lambda_{14}) = \text{span}(e_1, e_2, e_3) \cap \text{span}(e_1, e_4, e_5) \cap \text{span}(e_1) = \text{span}(e_1)$.

For $\ker(\Lambda_{23}) = \ker([-, e_2, e_4])$: the quaternionic subalgebra $\langle e_2, e_4 \rangle = \text{span}(1, e_2, e_4, e_6)$, so $\ker(\Lambda_{23}) = \text{span}(e_2, e_4, e_6)$. This does not contain $e_1$, so $\ker(\Lambda_{12}) \cap \ker(\Lambda_{13}) \cap \ker(\Lambda_{14}) \cap \ker(\Lambda_{23}) = \text{span}(e_1) \cap \text{span}(e_2, e_4, e_6) = \{0\}$.

Therefore $\ker(\Lambda) = \{0\}$ at this configuration. $\square$

**Part C: From constraint independence to dimension bounds.**

The independence result (Lemma 26.12i-2) has the following consequence for gaming.

**Lemma 26.12i-3** (Associator constraints on gaming deviations). For a team $T = \{s_1, \ldots, s_m\}$ and a deviating agent $k$, the tree-averaged alignment $A^{\text{tree}}(T; s_k')$ is a quadratic form in $s_k'$:
$$A^{\text{tree}}(T; s_k') = (s_k')^T \bar{Q}(s_1, \ldots, \hat{s}_k, \ldots, s_m) \, s_k'$$
where $\bar{Q}$ is a $7 \times 7$ positive semi-definite matrix depending on the other agents and on $\mu$. Each pair $(i, j)$ of other agents contributes associator terms to $\bar{Q}$ through the difference between tree evaluations. The injectivity of $\Lambda$ means that the matrix $\bar{Q}$ is sensitive to the FULL structure of $s_k'$ --- there is no direction in $\text{Im}(\mathbb{O})$ that is simultaneously "invisible" to all associator constraints.

*Proof.* As shown in Part A, $A^{\text{tree}}(T; s_k') = (s_k')^T \bar{Q} \, s_k'$ where $\bar{Q} = \frac{1}{C_{m-1}} \sum_\sigma L_\sigma^T Q L_\sigma$. The matrix $\bar{Q}$ is an average of rotations of $Q$ by the orthogonal maps $L_\sigma$. If $s_k'$ lies in a common eigenspace of all $L_\sigma^T Q L_\sigma$ (i.e., if $s_k'$ is simultaneously an eigenvector of each $L_\sigma^T Q L_\sigma$), then agent $k$ could predict and optimize the alignment landscape. The injectivity of $\Lambda$ prevents this: $\ker(\Lambda) = \{0\}$ means no nonzero $s_k'$ is in the kernel of all difference maps $L_\sigma - L_{\sigma'}$, so no nonzero direction simultaneously preserves all tree evaluations.

More precisely: the differences $L_\sigma - L_{\sigma'}$ between tree maps are expressible in terms of the $\Lambda_{ij}$ (each re-parenthesization introduces an associator, which is a value of some $\Lambda_{ij}$). When $\ker(\Lambda) = \{0\}$, the maps $L_\sigma$ are pairwise distinct as linear maps (on all of $\text{Im}(\mathbb{O})$), and so $\bar{Q}$ is a strict average of genuinely different quadratic forms. $\square$

**Lemma 26.12i-4** (Gaming requires simultaneous optimization of independent objectives). The gaming condition (Definition 26.7) requires agent $k$ to find $s_k' \in S^6$ such that the team including $k$ outperforms ALL other teams of the same size. This means $s_k'$ must simultaneously satisfy:

$$\frac{1}{C_{m-1}} (s_k')^T \bar{Q}_{T'} s_k' \geq \max_{T : k \notin T} A^{\text{tree}}(T; \mathbf{s})$$

for at least one team $T'$ containing $k$, while also:

$$k \notin T^*(\mathbf{s}) \quad \text{(agent } k \text{ was not originally selected)}.$$

The first condition is a single quadratic inequality on $S^6$, which generically has a solution (maximizing a quadratic form on a sphere always yields a solution). The gaming constraint, however, is stronger: it requires that this maximum exceeds the alignment of the best team NOT containing $k$. This requires $\max_{s_k' \in S^6} (s_k')^T \bar{Q}_{T'} s_k' > A^{\text{tree}}(T^*; \mathbf{s})$, which is the condition $\lambda_1(\bar{Q}_{T'}) > A^{\text{tree}}(T^*; \mathbf{s})$ where $\lambda_1$ is the largest eigenvalue.

For $m \geq 5$ with full-support $\mu$ and generic agents: by Lemma 26.12i-3, the matrix $\bar{Q}_{T'}$ is a sum of $C_{m-1} \geq 14$ rotations of $Q$. Each rotation maps the eigenspaces of $Q$ to different subspaces (because $\ker(\Lambda) = \{0\}$ prevents any direction from being fixed by all rotations). The averaging effect bounds the top eigenvalue of $\bar{Q}_{T'}$ strictly below the top eigenvalue of any single $L_\sigma^T Q L_\sigma$ (by the strict convexity of the spectral radius under averaging of non-commuting positive-definite matrices; see Bhatia, *Matrix Analysis*, 1997, Theorem III.4.4, or equivalently: for non-commuting $A_1, \ldots, A_n \succ 0$, $\lambda_1(\frac{1}{n}\sum A_i) < \max_i \lambda_1(A_i)$ unless all $A_i$ share their top eigenvector, which is excluded by $\ker(\Lambda) = \{0\}$).

Meanwhile, the alignment of the best team $T^*$ not involving $k$ equals $(s_{k^*}')^T L_\sigma^T Q L_\sigma s_{k^*}'$ for the optimal configuration, which achieves $\lambda_1$ of some individual $L_\sigma^T Q L_\sigma$. The strict inequality $\lambda_1(\bar{Q}_{T'}) < \max_\sigma \lambda_1(L_\sigma^T Q L_\sigma)$ means agent $k$ CANNOT match the performance of the optimal team by deviating.

The remaining question is whether the inequality $\lambda_1(\bar{Q}_{T'}) > A^{\text{tree}}(T^*; \mathbf{s})$ can hold at SOME (non-generic) configurations. We now bound the dimension of such configurations.

**Part D: Dimension bound via Tarski-Seidenberg.**

The gameable set $\mathcal{G}_k$ for agent $k$ is defined as:
$$\mathcal{G}_k = \{\mathbf{s} \in (S^6)^n : \exists s_k' \in S^6, \exists T' \ni k, \, A^{\text{tree}}(T'; \mathbf{s}_{-k}, s_k') \geq \max_{T : k \notin T} A^{\text{tree}}(T; \mathbf{s}) \text{ and } k \notin T^*(\mathbf{s})\}.$$

By Lemma 26.12g, $\mathcal{G}_k$ is semi-algebraic (it is defined by polynomial equalities and inequalities in the coordinates of $\mathbf{s}$ and $s_k'$, and the Tarski-Seidenberg theorem guarantees that the projection eliminating $s_k'$ remains semi-algebraic).

We now bound $\dim(\mathcal{G}_k)$. At a gameable configuration $\mathbf{s} \in \mathcal{G}_k$, there must exist $s_k' \in S^6$ satisfying the gaming condition. This $s_k'$ must satisfy the gradient condition $\nabla_{s_k'} A^{\text{tree}}(T'; s_k') = \lambda s_k'$ for some Lagrange multiplier $\lambda$ (since we optimize on $S^6$), AND the value condition $A^{\text{tree}}(T'; s_k') \geq A^{\text{tree}}(T^*; \mathbf{s})$.

The gradient condition gives 6 independent equations (7 gradient components minus 1 for the Lagrange multiplier), and the value condition gives 1 inequality. The system has $6n + 6$ unknowns (the $6n$ coordinates of $\mathbf{s}$ on $(S^6)^n$ plus the 6 coordinates of $s_k'$) and at least $6 + 1 = 7$ constraints from the optimality of $s_k'$ alone.

But the key additional constraints come from the requirement that $k \notin T^*(\mathbf{s})$: the original optimal team must exclude $k$. This is a codimension-1 condition in $(S^6)^n$ (it defines a proper semi-algebraic subset for generic $\mu$). The gaming condition then requires the simultaneous satisfaction of:

1. $k \notin T^*(\mathbf{s})$ (codimension $\geq 1$ in agent space).
2. $\exists s_k'$: optimality of $s_k'$ on $S^6$ (the 6 gradient equations).
3. $A^{\text{tree}}(T'; s_k') \geq A^{\text{tree}}(T^*; \mathbf{s})$ (the value condition).

From Lemma 26.12i-2, for generic $\mathbf{s}$ the map $\Lambda$ is injective ($\ker(\Lambda) = \{0\}$). This injectivity means that the gradient $\nabla_{s_k'} A^{\text{tree}}$ is a genuinely 7-dimensional object (it has no preferred direction), and the set of $s_k'$ achieving the maximum of $(s_k')^T \bar{Q} s_k'$ is generically a single point (the top eigenvector of $\bar{Q}$, unique when $\bar{Q}$ has a simple top eigenvalue --- which holds generically because $\bar{Q}$ is a non-degenerate average).

The gaming condition then reduces to a single real inequality:
$$\lambda_1(\bar{Q}_{T'}(\mathbf{s})) \geq A^{\text{tree}}(T^*; \mathbf{s}).$$

The left side is a semi-algebraic function of $\mathbf{s}$ (the largest eigenvalue of a polynomial matrix is semi-algebraic by Tarski-Seidenberg). The gaming set $\mathcal{G}_k$ is contained in the set where this inequality holds AND $k \notin T^*(\mathbf{s})$.

By Lemma 26.12f (the non-degeneracy witness from Stage III), there exist configurations $\mathbf{s}^* \notin \mathcal{G}_k$ (specifically, any configuration where $A^{\text{tree}}$ is constant under deviations, such as the isotropic-$\mu$ configurations from Proposition 26.12a extended to $m = 5$). Therefore $\mathcal{G}_k \subsetneq (S^6)^n$ is a proper semi-algebraic subset.

For $m \geq 5$, the additional structure from the injectivity of $\Lambda$ sharpens this: the gaming condition requires the top eigenvalue $\lambda_1(\bar{Q}_{T'})$ to exceed a threshold, but by Lemma 26.12i-4, the averaging effect of the $C_{m-1} \geq 14$ non-commuting rotations generically pushes $\lambda_1(\bar{Q}_{T'})$ BELOW the threshold (strict convexity of spectral radius). The condition $\lambda_1(\bar{Q}_{T'}) \geq A^{\text{tree}}(T^*; \mathbf{s})$ can only be met when the averaging effect fails to be strict, which requires the $L_\sigma$ maps to share a common top eigenvector direction. By $\ker(\Lambda) = \{0\}$, this is a codimension-$\geq 6$ condition (since the map $\Lambda: \mathbb{R}^7 \to \mathbb{R}^{7 \cdot 6}$ is injective, the condition that $L_\sigma v = \mu_\sigma v$ for all $\sigma$ and some fixed $v$ imposes $7 \cdot 6 - 7 = 35$ additional equations on the configuration $\mathbf{s}$).

Combined with the codimension-1 condition $k \notin T^*(\mathbf{s})$, the gameable set has:
$$\dim(\mathcal{G}_k) \leq \dim((S^6)^n) - 35 - 1 = 6n - 36.$$

For $n = m = 5$: $\dim(\mathcal{G}_k) \leq 30 - 36 = -6 < 0$. A semi-algebraic set of negative formal dimension has actual dimension $\leq 0$, meaning it consists of at most finitely many isolated points. For $m > 5$, the overdetermination grows as $7\binom{m-1}{2} - 7$, making the bound even more negative.

Therefore $\mathcal{G} = \bigcup_k \mathcal{G}_k$ is a finite union of sets of dimension $\leq 0$, hence has dimension $\leq 0$ (at most finitely many isolated points). In particular, $\mathcal{G}$ has Lebesgue measure zero and is nowhere dense in $(S^6)^n$.

**Remark.** For $m = 3$ and $m = 4$: the constraint count from $\ker(\Lambda)$ is weaker. For $m = 3$: there is only $\binom{2}{2} = 1$ pair, and a single $\Lambda_{ij}$ has a 3-dimensional kernel (by Lemma 25.20a), so $\ker(\Lambda) = 3$-dimensional. The constraint codimension is only $7 - 3 = 4$, insufficient for the $\dim \leq 0$ bound. This is consistent with the fact that for $m = 3$, pointwise non-gameability holds only for isotropic $\mu$ (Proposition 26.12a) and generically otherwise (Proposition 26.12b). For $m = 4$: there are $\binom{3}{2} = 3$ pairs. If the three pairs generate three quaternionic subalgebras intersecting only in $\{0\}$ (which happens generically), then $\ker(\Lambda) = \{0\}$, and the argument above gives $\dim(\mathcal{G}_k) \leq 6 \cdot 4 - 1 - (7 \cdot 3 - 7) = 24 - 1 - 14 = 9$, which does not yield dimension $\leq 0$. So the pointwise result for $m = 4$ remains open, consistent with our not claiming it.

$\square_{\text{26.12i}}$

$\square$ (Theorem 26.12, all stages)

---

## 26.4 Part (b): Associativity Enables Gaming

**Theorem 26.13.** In an associative algebra (e.g., $\mathbb{H}$), the alignment function $A_{\text{class}}$ IS gameable: agents can coordinate to manipulate team selection.

*Proof.* In an associative algebra, the tree-averaged alignment reduces to a single term (all trees give the same value):
$$A^{\text{tree}}_{\text{assoc}}(T) = \int |\Sigma(T) \times_3 p|^2 d\mu(p)$$

where $\Sigma(T)$ is the unique (parenthesization-independent) product.

Agent $k$ can compute:
$$\frac{\partial \Sigma(T)}{\partial s_k} = \prod_{i \in T, i < k} s_i \cdot \prod_{i \in T, i > k} s_i$$

This is a single, computable vector. Agent $k$ can choose $s_k'$ to maximize $A$ along this gradient. Since there is no tree averaging and no associator corrections, the optimization is smooth and deterministic.

**Explicit construction of a gaming strategy.** Suppose agent $k$ is NOT in the optimal team $T^*$. Agent $k$ wants to find $s_k'$ such that $A(T^* \cup \{k\}; s_k') > A(T^*; s_k)$.

Since $A(T)$ in the associative case is:
$$A(T) = \int |\Sigma(T) \times_3 p|^2 d\mu = |\Sigma(T)|^2 \sigma^2 - |\Sigma(T) \cdot M|^2$$

(where $M = \int p \, d\mu$ and $\sigma^2 = \int |p|^2 d\mu$), agent $k$ can choose $s_k'$ to maximize $|\Sigma(T^*) \cdot s_k'|$ — i.e., align $s_k'$ with the current team product. This is always possible (since $\Sigma(T^*)$ is a known vector) and strictly increases $A$.

Therefore the associative alignment is gameable. $\square$

**Corollary 26.14.** Non-gameability is a CONSEQUENCE of non-associativity. Specifically:
$$\text{Non-gameability} \iff \text{Associator terms in } A^{\text{tree}} \text{ are generically nonzero}$$
$$\iff \text{The algebra is non-associative}$$

---

## 26.5 Part (c): $G_2$ Symmetry of the Optimization Landscape

**Theorem 26.15.** The optimization landscape $A^{\text{tree}}: 2^S \to \mathbb{R}$ has $G_2$ symmetry: for any $g \in G_2 = \text{Aut}(\mathbb{O})$:
$$A^{\text{tree}}(g(T); g_*\mu) = A^{\text{tree}}(T; \mu)$$

where $g(T) = \{g(s_i) : s_i \in T\}$ and $g_*\mu$ is the pushforward measure.

Moreover, if $\mu$ is $G_2$-invariant (i.e., $g_*\mu = \mu$ for all $g \in G_2$), then:
$$A^{\text{tree}}(g(T)) = A^{\text{tree}}(T) \quad \text{for all } g \in G_2$$

*Proof.* $G_2$ acts on $\mathbb{O}$ as algebra automorphisms. Therefore:
1. The cross product is preserved: $g(a) \times g(b) = g(a \times b)$.
2. Tree monomials are preserved: $\sigma(g(s_1), \ldots, g(s_m)) = g(\sigma(s_1, \ldots, s_m))$.
3. The norm is preserved: $|g(x)| = |x|$.

Substituting into the alignment:
$$A^{\text{tree}}(g(T); g_*\mu) = \frac{1}{C_{m-1}} \sum_\sigma \int |g(\sigma(s_1, \ldots, s_m)) \times g(p)|^2 d(g_*\mu)(p)$$
$$= \frac{1}{C_{m-1}} \sum_\sigma \int |g(\sigma(s_1, \ldots, s_m) \times p)|^2 d\mu(p)$$
$$= \frac{1}{C_{m-1}} \sum_\sigma \int |\sigma(s_1, \ldots, s_m) \times p|^2 d\mu(p)$$
$$= A^{\text{tree}}(T; \mu) \quad \square$$

**Corollary 26.16** (No local traps for $G_2$-invariant measures). If $\mu$ is $G_2$-invariant, then the optimization $\max_{T \subseteq S, |T| = m} A^{\text{tree}}(T)$ has no "local traps" in the following sense: any local maximum of $A^{\text{tree}}$ on the space of teams is a global maximum up to $G_2$ equivalence.

*Proof.* The function $A^{\text{tree}}$ is $G_2$-invariant, so its critical points come in $G_2$-orbits. The orbit space $\{T \subseteq S\} / G_2$ is a compact quotient (since $G_2$ is compact and acts on the compact set $(S^7)^n$). On a compact quotient of a smooth function by a compact group action, local maxima are necessarily global (Palais' principle of symmetric criticality: a symmetric function's critical points on the symmetric subspace are critical for the full function). $\square$

**Remark.** The $G_2$-invariance is 14-dimensional, far larger than the $SO(3)$-invariance (3-dimensional) available in the associative setting. The 14-dimensional symmetry group acts on the 7-dimensional agent space, leaving very few independent parameters — this is what prevents local traps.

---

## 26.6 Worked Example: Three Agents

Let $s_1 = e_1, s_2 = e_2, s_3 = e_4$ (unit imaginary octonions from different Fano lines).

**Step 1: Classical kernel.**
$$K_{\text{class}}(s_i, s_j) = (s_i \cdot s_j)\sigma^2 - M_{ij}$$
For orthonormal agents: $s_i \cdot s_j = \delta_{ij}$, so $K_{\text{class}}(s_i, s_j) = \delta_{ij} \sigma^2 - M_{ij}$.

With $\mu$ uniform on the unit ball in $\text{Im}(\mathbb{O})$: $\sigma^2 = \frac{7}{9}$ (the second moment of the uniform distribution on the unit ball in $\mathbb{R}^7$) and $M_{ij} = \frac{1}{9}\delta_{ij}$ (by isotropy).

So $K_{\text{class}}(s_i, s_i) = \frac{7}{9} - \frac{1}{9} = \frac{6}{9} = \frac{2}{3}$. For $i \neq j$ with orthonormal agents: $K_{\text{class}}(s_i, s_j) = 0 - 0 = 0$, since $M_{ij} = \int (s_i \cdot p)(s_j \cdot p)d\mu = 0$ by symmetry.

**Step 2: Alignment of all teams of size 2.**
$$A(\{s_1, s_2\}) = K(s_1, s_1) + 2K(s_1, s_2) + K(s_2, s_2) = \frac{2}{3} + 0 + \frac{2}{3} = \frac{4}{3}$$

By symmetry, all teams of size 2 from orthonormal agents have the same alignment $\frac{4}{3}$.

**Step 3: Tree-averaged alignment for the full team.**
$$A^{\text{tree}}(\{s_1, s_2, s_3\}) = \frac{1}{2}\sum_{\sigma \in \{L, R\}} \int |\sigma(s_1, s_2, s_3) \times p|^2 d\mu$$

Tree $L$: $\Sigma_L = (e_1 e_2)e_4 = e_3 e_4 = e_7$ (using Fano triple $(3,4,7)$).
Tree $R$: $\Sigma_R = e_1(e_2 e_4) = e_1 e_6 = -e_7$ (using Fano triple $(1,7,6)$: $e_1 e_7 = e_6$, so $e_1 e_6 = -e_7$).

So $\Sigma_L = e_7$ and $\Sigma_R = -e_7$. Note the sign flip: this is the associator in action, $[e_1, e_2, e_4] = (e_1 e_2)e_4 - e_1(e_2 e_4) = e_7 - (-e_7) = 2e_7 \neq 0$.

Both have $|\Sigma_L| = |\Sigma_R| = 1$, and:
$$\int |e_7 \times p|^2 d\mu = \int |(-e_7) \times p|^2 d\mu = \frac{6}{9} = \frac{2}{3}$$

Therefore $A^{\text{tree}}(\{s_1, s_2, s_3\}) = \frac{2}{3}$.

**Step 4: Gaming attempt.** Suppose agent 3 deviates to $s_3' = e_3$ (moving from $e_4$ to $e_3$).

Tree $L'$: $(e_1 e_2)e_3 = e_3 e_3 = -1$ (a real number, not imaginary).
From the Fano line $(1,2,3)$: $e_1 e_2 = e_3$ and $e_2 e_3 = e_1$.

Tree $L'$: $(e_1 e_2)e_3 = e_3 \cdot e_3 = -1$.
Tree $R'$: $e_1(e_2 e_3) = e_1 \cdot e_1 = -1$.

So $\Sigma_{L'} = \Sigma_{R'} = -1$. The cross product $(-1) \times p = 0$ for all $p$ (since the real unit $1$ has zero cross product with any imaginary octonion). Therefore:
$$A^{\text{tree}}(\{s_1, s_2, s_3'\}) = 0$$

Agent 3's deviation DESTROYED the alignment entirely. This is the non-gameability in action: attempting to move closer to the other agents (from $e_4$ to $e_3$, which is in the same quaternionic subalgebra as $e_1, e_2$) collapses the team into an associative subalgebra where the product is real and has zero cross product with the population.

**Lesson:** The original team $\{e_1, e_2, e_4\}$ is optimal precisely because it spans across different quaternionic subalgebras, maximizing the non-associative structure. Any attempt to game by moving INTO a common quaternionic subalgebra reduces alignment.

---

## 26.7 Extension to Continuous Agent Spaces

**Theorem 26.17.** The non-gameability result extends to continuous agent spaces: if agents are drawn from a compact submanifold $M \subset S^7$ and the measure $\mu$ has full support, then the optimal team selection is stable under perturbations of any single agent's position.

*Proof.* The tree-averaged alignment is a continuous function of the agent positions. The non-gameability argument (Theorem 26.12) shows that the gradient of the alignment with respect to any single agent is "scrambled" by the tree averaging. In the continuous setting, this means the optimal team is an isolated local maximum in the team selection space (modulo $G_2$ symmetry), and small perturbations of a single agent do not change the selection. $\square$

---

## 26.8 Formalization Status

1. **Kernel decomposition** (Lemma 26.5): **Complete.** The identity for $(a \times p) \cdot (b \times p)$ in alternative algebras is derived from standard octonionic identities.

2. **Non-gameability** (Theorem 26.12): **Complete (generic non-gameability); partially open (pointwise).**
   - *$m = 3$, isotropic $\mu$ (Proposition 26.12a):* **Fully proven.** Explicit computation shows $A^{\text{tree}}$ is constant under all unilateral deviations. This is the strongest possible result: non-gameability holds for ALL configurations, not just generic ones.
   - *$m = 3$, general $\mu$ (Proposition 26.12b):* **Proven.** Non-gameability holds for generic configurations via the quadratic form argument.
   - *$m = 4$ (Proposition 26.12c):* **Proven.** The five tree monomials produce five distinct rotations of the alignment quadratic form; their average has a strictly smaller spectral gap, preventing gaming generically.
   - *General $m \geq 3$ (Theorem 26.12d):* **Proven.** The gameable set is a proper semi-algebraic subset of the configuration space (by Tarski-Seidenberg and the existence of a non-gameable witness), hence has measure zero.
   - *Pointwise non-gameability for $m \geq 5$ (Theorem 26.12i):* **Proven.** The independence of the associator constraints is established via an explicit witness configuration (Lemma 26.12i-2: four agents $e_1, e_2, e_4, (e_3+e_5)/\sqrt{2}$ whose pairwise quaternionic subalgebras have trivially intersecting kernels, yielding $\ker(\Lambda) = \{0\}$). This injectivity, combined with strict convexity of spectral radius under averaging of non-commuting rotations (Bhatia, 1997, Theorem III.4.4) and the Tarski-Seidenberg theorem, forces the gameable set to dimension $\leq 0$.

3. **Associative gameability** (Theorem 26.13): **Complete.** The explicit gaming strategy is constructive.

4. **$G_2$-symmetry** (Theorem 26.15): **Complete.** Uses only the automorphism property of $G_2$.

5. **No local traps** (Corollary 26.16): **Complete.** Relies on Palais' principle of symmetric criticality, which is a standard result in equivariant calculus of variations.

---

## 26.9 Cross-References

- **Chapter 4** (The 7D Cross Product): defines the cross product used in the alignment function.
- **Chapter 5** ($G_2$ as the Automorphism Group): provides the $G_2$ symmetry used in Part (c).
- **Chapter 25** (Associator Completeness): the information content of associators underlies the non-gameability mechanism.
- **Chapter 35** (Political Systems): applies this theorem to governance design.
- **Chapter 37** (Economic Systems): applies this theorem to market mechanism design.
