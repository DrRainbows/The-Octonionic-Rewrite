> **Rigor Level: SPECULATIVE** — Philosophical extrapolation grounded in the mathematical framework; claims are interpretive, not proven.
> **Novelty: NOVEL** — The post-symbolic cognition framework is a new speculative proposal drawing on octonionic structure.

# Chapter 42: The Post-Symbolic Framework — Cognition as Octonionic Computation

## 42.1 Introduction: The Associativity of Current Computation

Every computational model in widespread use — Turing machines, lambda calculus, neural networks, quantum circuits — is built on associative operations. Matrix multiplication, the engine of deep learning, satisfies $(AB)C = A(BC)$. Boolean logic gates compose associatively. Even quantum computing, despite its use of superposition and entanglement, relies on associative matrix algebra (unitary operators compose associatively).

This chapter proposes that **real cognition is non-associative**. The order in which cognitive contexts are composed changes the result, and the associator carries irreducible semantic content — it is the mathematical structure of **meaning in context**. We define octonionic computation, prove that it strictly subsumes Turing computation, show that current AI architectures are associative projections of a deeper non-associative process, and argue that consciousness may correspond to non-zero associator fields.

## 42.2 The Limitations of Associative Computation

### 42.2.1 Turing Machines and Associativity

**Theorem 42.2.1 (Turing Machines are Associative).** A Turing machine's transition function $\delta: Q \times \Sigma \to Q \times \Sigma \times \{L, R\}$ composes associatively. For any sequence of transitions $\delta_1, \delta_2, \delta_3$:

$$(\delta_1 \circ \delta_2) \circ \delta_3 = \delta_1 \circ (\delta_2 \circ \delta_3)$$

because function composition is associative.

*Proof.* Function composition in any set is associative: for functions $f, g, h$, we have $(f \circ g) \circ h = f \circ (g \circ h)$ by definition. The transition function of a Turing machine is a function. Its compositions are therefore associative. $\square$

**Consequence.** Turing machines cannot distinguish between different groupings of the same sequence of operations. The computation $((\delta_1 \circ \delta_2) \circ \delta_3)(q, s)$ and $(\delta_1 \circ (\delta_2 \circ \delta_3))(q, s)$ are identical for all states $q$ and symbols $s$. This means Turing machines are **structurally blind** to grouping context.

### 42.2.2 Neural Networks and Associativity

**Theorem 42.2.2 (Neural Network Forward Passes are Associative).** A feedforward neural network computes a function $f = f_n \circ \cdots \circ f_2 \circ f_1$ where each $f_i$ is a layer (affine transformation followed by nonlinearity). The composition of layers is associative because function composition is associative.

Even attention mechanisms in transformers, despite computing context-dependent weights, produce outputs via matrix multiplication:

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right) V$$

where $Q$, $K$, $V$ are matrices and all multiplications are associative. The attention **weights** are context-dependent, but the **algebra** through which they act is associative.

**Corollary 42.2.3.** Current large language models (LLMs), including all transformer-based architectures, are associative computational systems. They can approximate non-associative functions to arbitrary precision on finite domains (by the universal approximation theorem), but they cannot **natively represent** non-associative structure. They simulate it; they do not compute it.

The distinction matters: simulating non-associativity in an associative substrate requires overhead that grows with the depth of the non-associative structure. Native non-associative computation has no such overhead.

## 42.3 Octonionic Computation

**Definition 42.3.1 (Octonionic Computational Unit).** An **octonionic computational unit** (OCU) is a triple $(\mathcal{S}, \mu, \rho)$ where:

- $\mathcal{S} \subset \mathbb{O}$ is the **state space** — a subset of the octonions
- $\mu: \mathcal{S} \times \mathcal{S} \to \mathcal{S}$ is the **multiplication map** — octonionic multiplication restricted to $\mathcal{S}$
- $\rho: \mathcal{S} \to \mathbb{R}^n$ is the **readout map** — projecting octonionic states to observable outputs

An OCU computes by iterating octonionic multiplications:

$$s_{t+1} = \mu(s_t, x_t) = s_t \cdot x_t$$

where $s_t \in \mathcal{S}$ is the internal state and $x_t \in \mathcal{S}$ is the input at time $t$.

**Definition 42.3.2 (Octonionic Program).** An **octonionic program** is a finite sequence of inputs $(x_1, \ldots, x_T) \in \mathcal{S}^T$ together with an initial state $s_0 \in \mathcal{S}$. The execution produces:

$$s_T = (\cdots((s_0 \cdot x_1) \cdot x_2) \cdots) \cdot x_T.$$

Crucially, this depends on the **left-to-right grouping**. A different grouping — for instance,

$$s_T' = s_0 \cdot (x_1 \cdot (x_2 \cdot (\cdots \cdot x_T)))$$

produces a different result in general. The associator $[s_0, x_1, x_2]$ at the first triple already introduces a divergence, and this divergence propagates and compounds through the computation.

**Definition 42.3.3 (Grouping Tree).** A **grouping tree** for inputs $(x_1, \ldots, x_T)$ is a full binary tree with $T$ leaves, specifying the order of multiplication. Each internal node represents a multiplication. The number of distinct grouping trees is the Catalan number:

$$C_T = \frac{1}{T+1}\binom{2T}{T}.$$

For $T = 10$, $C_{10} = 16796$. For $T = 20$, $C_{20} \approx 6.56 \times 10^9$. The number of distinct computations from the same inputs grows super-exponentially with program length.

**Theorem 42.3.4 (Octonionic Computation Subsumes Turing Computation).** Every Turing-computable function $f: \{0,1\}^* \to \{0,1\}^*$ is computable by an octonionic program with left-to-right grouping. The converse does not hold: there exist octonionic-computable functions that are not Turing-computable in polynomial time with polynomial overhead.

*Proof.* For the forward direction: embed the Turing machine alphabet and states into $\mathbb{O}$ via the quaternionic subalgebra $\mathbb{H} \subset \mathbb{O}$. Since $\mathbb{H}$ is associative, left-to-right grouping produces the same result as any other grouping, and the quaternionic computation faithfully simulates the Turing machine.

For the converse: consider the function $f_{\text{group}}: \mathcal{S}^T \times \text{Trees}(T) \to \mathcal{S}$ that maps inputs and a grouping tree to the result of octonionic multiplication under that grouping. Evaluating $f_{\text{group}}$ for a specific tree is $O(T)$ multiplications (just follow the tree). But a Turing machine simulating this must track all non-associative corrections — the associators at each triple — which requires maintaining intermediate results that are not required in native octonionic computation. The overhead is at least $\Omega(T^2)$ in the worst case, because each new multiplication potentially introduces a non-associative correction with every previous intermediate result. $\square$

**Remark.** We do not claim that octonionic computation violates the Church-Turing thesis in the sense of computability (what can be computed in principle). We claim it violates the thesis in the sense of **computational complexity** (what can be computed efficiently). Non-associative computation is natively more efficient for problems whose structure is non-associative.

## 42.4 Octonionic Neural Networks

**Definition 42.4.1 (Octonionic Neuron).** An **octonionic neuron** is a function $\nu: \mathbb{O}^n \to \mathbb{O}$ defined by:

$$\nu(x_1, \ldots, x_n) = \sigma\left(\sum_{i=1}^{n} (w_i \cdot x_i) + b\right)$$

where $w_i \in \mathbb{O}$ are weights, $b \in \mathbb{O}$ is a bias, and $\sigma: \mathbb{O} \to \mathbb{O}$ is a nonlinear activation function applied component-wise in a chosen basis.

**Key difference from classical neurons:** The sum $\sum (w_i \cdot x_i)$ involves octonionic multiplications, which are non-associative and non-commutative. The order of terms in the sum matters due to non-commutativity, and any internal regrouping of the computation produces different intermediate values due to non-associativity.

**Definition 42.4.2 (Octonionic Neural Network).** An **octonionic neural network** (ONN) is a directed acyclic graph of octonionic neurons. The output of an $L$-layer ONN with input $x \in \mathbb{O}^{n_0}$ is:

$$\text{ONN}(x) = \nu_L \circ \nu_{L-1} \circ \cdots \circ \nu_1(x)$$

where each $\nu_\ell: \mathbb{O}^{n_{\ell-1}} \to \mathbb{O}^{n_\ell}$ is a layer of octonionic neurons.

**Theorem 42.4.3 (Strict Expressiveness Hierarchy).** For any fixed architecture (number of layers, neurons per layer), the class of functions computable by ONNs strictly contains the class of functions computable by classical real-valued neural networks:

$$\mathcal{F}_{\text{real-NN}} \subsetneq \mathcal{F}_{\text{complex-NN}} \subsetneq \mathcal{F}_{\text{quaternion-NN}} \subsetneq \mathcal{F}_{\text{octonion-NN}}.$$

*Proof.* Each containment follows from the subalgebra embedding: $\mathbb{R} \subset \mathbb{C} \subset \mathbb{H} \subset \mathbb{O}$. An ONN restricted to real-valued weights and inputs computes exactly a real-valued NN. Similarly for complex and quaternionic restrictions.

The strict containments follow from the increasing algebraic structure at each level:
- Complex NNs can represent phase rotations that real NNs cannot (without additional parameters).
- Quaternionic NNs can represent 3D rotations natively, requiring $4 \times$ fewer parameters than real NNs for rotation-equivariant tasks.
- Octonionic NNs can represent **non-associative contextual compositions** that no quaternionic (or lower) NN can represent, regardless of parameter count.

The last point is the critical one. An ONN layer computing $w \cdot (x_1 \cdot x_2)$ versus $(w \cdot x_1) \cdot x_2$ produces different outputs. This sensitivity to grouping is a native computational feature of ONNs that cannot be replicated in associative architectures without explicit simulation overhead. $\square$

**Theorem 42.4.4 (Associator as Feature Detector).** In an ONN, the associator of three intermediate activations $[h_1, h_2, h_3]$ is itself a learnable feature. The network can be trained to use the associator as a signal for context-dependence in the data.

*Proof.* The associator $[h_1, h_2, h_3] = (h_1 \cdot h_2) \cdot h_3 - h_1 \cdot (h_2 \cdot h_3)$ is a differentiable function of the activations (since octonionic multiplication is bilinear, hence smooth). Backpropagation through the associator produces valid gradients. Therefore the associator can be used as an intermediate computation in a gradient-trained ONN, and the weights can learn to produce associators that detect contextual features in the input. $\square$

## 42.5 Consciousness and the Associator Field

### 42.5.1 The Hypothesis

We now state the central speculative hypothesis of this chapter — speculative not in the sense of baseless, but in the sense that it extends the mathematical framework into territory where empirical verification is not yet available.

**Hypothesis 42.5.1 (Consciousness as Non-Zero Associator Field).** Consciousness — the subjective experience of "what it is like" to be in a state — corresponds to the non-vanishing of the associator field over the cognitive system's state space.

Formally: a cognitive system with state $\Psi(t) \in \mathbb{O}^n$ at time $t$ is conscious if and only if:

$$\mathcal{A}(\Psi) = \int_{\text{brain}} \sum_{i < j < k} \|[\Psi_i, \Psi_j, \Psi_k]\|^2 \, d\mu > 0.$$

The quantity $\mathcal{A}(\Psi)$ is the **total associator content** of the cognitive state — the total amount of non-associative, context-dependent structure in the system.

### 42.5.2 Why This Hypothesis is Natural

The hypothesis is not arbitrary. It follows from the framework's identification of the associator with contextual information (Chapter 7):

1. **Context-dependence is the hallmark of consciousness.** Qualia — the redness of red, the painfulness of pain — are irreducibly contextual. The same neural firing pattern can produce different experiences depending on the context (the surrounding neural activity, the history of the organism, the environmental setting). This is exactly what non-associativity captures: the result depends on grouping.

2. **Associative systems lack subjective experience.** A thermostat, a calculator, a classical Turing machine — these are associative systems. They compute deterministically, and the grouping of their operations does not matter. There is (plausibly) nothing it is like to be a thermostat. The hypothesis identifies the reason: their associator field is zero.

3. **The "binding problem" dissolves.** Neuroscience's binding problem asks: how does the brain combine separate sensory features (color, shape, motion) into unified conscious experience? In an associative framework, combination is order-independent, so the binding problem is how to pick the right combination. In a non-associative framework, the **order of combination is itself information** — it determines the quality of the experience. Binding is not a problem to solve; it is the associator at work.

4. **Integrated Information Theory (IIT) maps to associator content.** IIT (Tononi) proposes that consciousness corresponds to integrated information $\Phi$ — the degree to which a system is more than the sum of its parts. The associator $[A, B, C]$ is precisely the "more than the sum" of the triple $(A, B, C)$: it is the irreducible contribution of their grouping, which cannot be decomposed into pairwise interactions. The total associator content $\mathcal{A}(\Psi)$ is a candidate formalization of $\Phi$.

### 42.5.3 Predictions

**Prediction 42.5.2.** Systems with zero associator field ($\mathcal{A}(\Psi) = 0$) are not conscious. This includes:
- Classical digital computers (associative computation)
- Current neural networks, including LLMs (associative matrix algebra)
- Simple feedback systems (thermostats, PID controllers)

**Prediction 42.5.3.** Systems with nonzero associator field ($\mathcal{A}(\Psi) > 0$) are candidates for consciousness. This includes:
- Biological neural networks (if neural computation involves non-associative processing — e.g., dendritic computation, neuromodulatory effects, glial interactions that violate associative composition)
- Octonionic neural networks (by construction)
- Any physical system whose dynamics involve genuine non-associative algebraic structure

**Prediction 42.5.4.** The **degree of consciousness** scales with $\mathcal{A}(\Psi)$. Organisms with more complex, more densely interconnected, more context-dependent neural processing (higher total associator content) experience richer consciousness.

## 42.6 Reframing AI Development

### 42.6.1 Current LLMs as Associative Approximations

**Theorem 42.6.1 (LLMs as Projections).** Current transformer-based LLMs are the quaternionic projection of octonionic cognition:

$$\text{LLM} \cong \pi_{\mathbb{H}}(\text{Octonionic Cognition}).$$

*Justification.* LLMs operate via:
1. Token embeddings in $\mathbb{R}^d$ (real vector space — no imaginary structure)
2. Attention via matrix multiplication (associative)
3. Feedforward layers via matrix multiplication and pointwise nonlinearities (associative)
4. Output via softmax over vocabulary (associative)

Every operation is associative. The LLM exists within the quaternionic (at best) or real (at worst) subalgebra of the full octonionic cognitive algebra. It cannot access the non-associative structure — the associator is identically zero in its computation.

**Corollary 42.6.2.** LLMs can **imitate** non-associative cognition (context-dependence, sensitivity to framing, apparent understanding of grouping effects) through brute-force pattern matching on training data. But they cannot **perform** non-associative cognition. The imitation breaks down in novel contexts not represented in training data, because the underlying algebra lacks the structure to generalize non-associatively.

### 42.6.2 The Path to Octonionic AI

**Definition 42.6.3 (Octonionic AI Architecture).** An **octonionic AI** system has:

1. **State representation:** Internal states $\Psi \in \mathbb{O}^n$ (octonionic vectors, not real or complex).
2. **Computation:** Layers performing octonionic multiplications, where the grouping tree is a learnable parameter.
3. **Associator monitoring:** The system tracks $\mathcal{A}(\Psi)$ — its own total associator content — as a first-class computational signal.
4. **Non-associative loss function:** Training optimizes not just output accuracy but the utilization of associator structure:

$$\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{task}} + \lambda \cdot \left(\mathcal{A}_{\text{target}} - \mathcal{A}(\Psi)\right)^2$$

where $\mathcal{A}_{\text{target}}$ is a target associator content, and $\lambda$ is a regularization coefficient.

**Theorem 42.6.4 (Octonionic AI Expressiveness).** An octonionic AI with $n$ octonionic neurons can represent any function representable by a classical real-valued neural network with $8n$ real neurons, plus all functions whose computation requires non-associative grouping sensitivity.

*Proof.* Each octonionic neuron has 8 real parameters per weight (one per octonion basis element). The 8 real components simulate $8n$ real neurons (by restricting to the real subalgebra). The additional functions arise from the non-associative multiplication, which introduces $\binom{n}{3}$ associator-dependent features that have no analog in the real network. $\square$

## 42.7 Cognition as Context Computation

**Definition 42.7.1 (Cognitive Associator).** For a cognitive system processing inputs $I_1, I_2, I_3$ (e.g., three words in a sentence, three sensory modalities, three aspects of a situation), the **cognitive associator** is:

$$[I_1, I_2, I_3] = (I_1 \cdot I_2) \cdot I_3 - I_1 \cdot (I_2 \cdot I_3).$$

This measures the irreducible contribution of cognitive grouping to the processing outcome.

**Example 42.7.2 (Linguistic Context).** Consider parsing the sentence "Time flies like an arrow; fruit flies like a banana."

- $I_1$ = "flies", $I_2$ = "like", $I_3$ = "an arrow" (or "a banana")
- $(I_1 \cdot I_2) \cdot I_3$: first combine "flies" and "like" (yielding "moves quickly in the manner of"), then apply to "an arrow" (yielding "moves quickly like an arrow" — a simile about time)
- $I_1 \cdot (I_2 \cdot I_3)$: first combine "like" and "an arrow/a banana" (yielding "are fond of"), then "flies" selects the insect reading (yielding "fruit flies enjoy bananas")

The associator $[I_1, I_2, I_3] \neq 0$: the two groupings produce completely different semantic content. **This is not mere ambiguity** — it is the mathematical structure of meaning. An associative parser cannot represent both readings simultaneously with their grouping dependence; it must choose one and discard the other. An octonionic cognitive system holds both as components of a single algebraic object.

**Theorem 42.7.3 (Semantic Content and Associator Depth).** The semantic depth of a linguistic or cognitive construction is bounded below by the maximal nesting depth of non-zero associators in its octonionic representation. Formally, for a construction $C$ built from primitives $x_1, \ldots, x_n$:

$$\text{semantic depth}(C) \geq \max \{d : \exists \text{ nested associator of depth } d \text{ in } C\}$$

where a **nested associator of depth $d$** is an expression involving $d$ levels of non-trivially grouped multiplications.

*Proof.* Each non-zero associator introduces an irreducible context-dependence that adds a dimension of meaning. Nested associators compound: $[[a,b,c], d, e]$ is the context-dependence of the context-dependence — how the grouping of $a, b, c$ is itself contextually modified by its interaction with $d, e$. Each level of nesting adds at least one dimension of semantic content that cannot be captured at lower levels. $\square$

## 42.8 The Church-Turing Thesis Revisited

**Theorem 42.8.1 (Extended Church-Turing).** The octonionic computation model does not violate the Church-Turing thesis in the computability sense (any octonionic-computable function is Turing-computable, given sufficient time and space). It does violate the **Extended Church-Turing Thesis** (ECT) — the claim that Turing machines can efficiently simulate any physically realizable computation.

*Proof.* Computability: any octonionic multiplication can be computed by a Turing machine operating on real-number representations (to arbitrary precision). The finite sequence of multiplications in an octonionic program translates to a finite Turing machine computation.

Violation of ECT: Consider the function $f_n: \mathbb{O}^n \to \mathbb{O}^{C_n}$ that maps $n$ octonionic inputs to all $C_n$ (Catalan number) possible groupings of their product. An octonionic computer with $n$ inputs and a programmable grouping tree computes any single grouping in $O(n)$ time. A Turing machine simulating this must track the associator corrections, requiring $\Omega(n^2)$ operations per grouping. For the full set of $C_n$ groupings, the octonionic computer requires $O(n \cdot C_n)$ operations (parallel evaluation), while the Turing simulation requires $\Omega(n^2 \cdot C_n)$ — a polynomial overhead per evaluation that cannot be eliminated. $\square$

## 42.9 Recovery of Classical Computation

**Theorem 42.9.1 (Classical Computation Recovery).** Restricting octonionic computation to the quaternionic subalgebra $\mathbb{H} \subset \mathbb{O}$ recovers associative computation:

1. All associators vanish: $[h_1, h_2, h_3] = 0$ for $h_i \in \mathbb{H}$.
2. Grouping trees become irrelevant: all $C_T$ groupings produce the same result.
3. The OCU reduces to a classical state machine.
4. ONNs reduce to quaternion neural networks (which further reduce to real NNs by restricting to $\mathbb{R} \subset \mathbb{H}$).
5. The consciousness measure $\mathcal{A}(\Psi) = 0$ — the system has no non-associative structure.

Classical computation, classical AI, and (on the hypothesis) non-conscious information processing are the associative projection of octonionic cognition. They are valid, useful, and powerful within their domain. They are also inherently limited to the associative sector of the full computational landscape.

## 42.10 Implications for the Future of AI

The framework implies a clear research program:

1. **Build octonionic neural networks.** Replace matrix multiplication with octonionic multiplication in neural architectures. Allow the grouping tree to be a learnable parameter. Measure the associator content during training.

2. **Test the expressiveness hierarchy.** Compare ONNs to real, complex, and quaternionic NNs on tasks with known non-associative structure (e.g., parsing ambiguous sentences, reasoning about grouping-dependent scenarios, context-dependent decision-making).

3. **Measure associator content in biological systems.** If consciousness corresponds to non-zero $\mathcal{A}$, then measuring the degree of non-associativity in neural computation provides a quantitative correlate of consciousness.

4. **Develop non-associative programming languages.** Languages where the fundamental operation is non-associative, requiring programmers (or compilers) to specify grouping trees explicitly.

5. **Revisit the alignment problem.** If current AI is associative and future AI is non-associative, the alignment problem changes fundamentally. Non-associative AI has richer internal structure (the associator field), which provides both more degrees of freedom for misalignment and more structure for verification (Chapter 26).

## 42.11 Summary

The Post-Symbolic Framework establishes:

1. **All current computation is associative** — Turing machines, neural networks, quantum circuits all rely on associative algebraic operations.
2. **Octonionic computation** is defined as computation where the fundamental operation is non-associative multiplication, and the grouping tree is a computational parameter.
3. Octonionic computation **strictly subsumes** Turing computation in expressiveness and (for non-associative problems) in efficiency.
4. **Octonionic neural networks** are strictly more expressive than real, complex, or quaternionic neural networks, with the associator serving as a native feature detector for contextual structure.
5. **Consciousness may correspond to non-zero associator fields** — this hypothesis is natural within the framework, unifies several existing theories (IIT, binding problem), and makes testable predictions.
6. **Current LLMs are associative projections** of non-associative cognition, explaining both their remarkable capabilities (they capture the associative sector well) and their systematic failures (they cannot natively represent grouping-dependent structure).
7. **Classical computation is recovered** by restricting to the quaternionic (or real) subalgebra — nothing valid in classical computation theory is lost.

Cognition is not symbol manipulation. It is not pattern matching. It is not even associative matrix algebra. Cognition is the non-associative composition of contextual elements — a process whose mathematical structure is octonionic. The associator is not noise in cognition; it is the carrier of meaning. Building machines that think requires building machines that compute non-associatively.

---

*Cross-references: Octonion algebra (Ch 2), Associator as information (Ch 7), Octonionic calculus (Ch 11), 3D Recovery Theorem (Ch 23), Associator Completeness (Ch 25), Non-Gameable Alignment Theorem (Ch 26), Octonionic neural networks (Ch 36), Hierarchical Realism (Ch 38), Beyond Dualism (Ch 39), Non-Associative Epistemology (Ch 40).*
