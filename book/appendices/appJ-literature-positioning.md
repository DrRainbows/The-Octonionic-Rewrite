> **Rigor Level: EXPOSITORY** — Systematic literature comparison with precise attribution; no new mathematical results claimed.
> **Novelty: EXPOSITORY** — The positioning itself is a new organizational contribution; all cited prior work is established.

# Appendix J: Literature Positioning — Prior Work vs This Framework

## J.1 Introduction: Why Literature Positioning Matters

A framework built on the octonions inherits a long and distinguished intellectual lineage. The octonions were discovered independently by John T. Graves (1843) and Arthur Cayley (1845). Their automorphism group $G_2$ was classified by Elie Cartan (1894). Their connection to particle physics was explored by Günaydin and Gürsey (1973). Their role in the Standard Model has been investigated by Dixon (1994), Furey (2016), and many others. The non-associative algebraic structures underlying the octonions — Malcev algebras, Sabinin algebras, alternative algebras — were developed by Zorn, Malcev, Moufang, Schafer, and Sabinin across the 20th century.

Any honest framework must answer two questions:

1. **What is prior work?** What does this framework inherit, use, and depend on?
2. **What is genuinely new?** What appears here for the first time?

Failure to answer these questions clearly exposes a framework to three legitimate criticisms: that it is derivative without acknowledgment, that it claims originality where none exists, and that it obscures the boundary between established and speculative. This appendix addresses all three.

The standard we apply is strict. If a concept, construction, or theorem appears in the published literature — even if our presentation, notation, or computational implementation differs — we cite it and label it as prior work. We claim novelty only for constructions, proofs, and predictions that we have been unable to find in the existing literature after extensive search. We welcome correction on any attribution.

---

## J.2 Master Comparison Table

The following table lists every major concept used in this book, its origin in the prior literature, the specific citation, and what (if anything) this framework adds beyond the cited work. Entries where the "What This Framework Adds" column says "Foundation only" or "Standard usage" indicate concepts used without modification. All other entries describe specific extensions.

| # | Concept | Prior Work | Citation | What This Framework Adds |
|:---:|:---|:---|:---|:---|
| 1 | Octonion algebra | Graves (1843), Cayley (1845) | Standard; see Baez (2002) for modern survey | Foundation only. Used as given. |
| 2 | Cayley-Dickson construction | Dickson (1919) | L. E. Dickson, *Ann. of Math.* 20 | Foundation only. |
| 3 | Hurwitz's theorem ($\mathbb{R}, \mathbb{C}, \mathbb{H}, \mathbb{O}$ only) | Hurwitz (1898) | A. Hurwitz, *Nachr. Ges. Wiss. Göttingen* | Foundation only. |
| 4 | Alternativity and Moufang identities | Moufang (1933), Artin (1927) | R. Moufang, *Math. Ann.* 110; E. Artin, *Abh. Math. Sem. Hamburg* 5 | Fano orientation invariance theorem: the sign pattern of the associator is invariant under all 168 Fano-plane automorphisms (Ch. 4, `fano_invariance.py`). |
| 5 | Alternative algebras, Zorn's vector matrices | Zorn (1933) | M. Zorn, *Abh. Math. Sem. Hamburg* 9 | Standard usage in Ch. 3. |
| 6 | $G_2 = \mathrm{Aut}(\mathbb{O})$ | Cartan (1894) | E. Cartan, *Sur la structure des groupes de transformations finis et continus* | Decompactified Killing form $B_\mu$ extending the $\mathfrak{g}_2$ Killing form to a measure-integrated bilinear form over context spaces (Ch. 8, `context_integral.py`). |
| 7 | $G_2$ and particle physics | Günaydin-Gürsey (1973) | M. Günaydin, F. Gürsey, *Phys. Rev.* D8, 3851 | Explicit computation of $G_2 \to SU(3) \to SU(2) \times U(1)$ branching with $\sin^2\theta_W = 3/8$ derivation; computational verification code (`g2_unification.py`); identification of 6 coset gauge bosons with specific quantum numbers (Ch. 24). |
| 8 | Octonions and the Standard Model | Dixon (1994) | G. M. Dixon, *Division Algebras: Octonions, Quaternions, Complex Numbers and the Algebraic Design of Physics* | COA axiom system (6 axioms, Definition 6.3); deformation parameter $\varepsilon$ linking classical and octonionic regimes (Ch. 4, `deformation.py`). |
| 9 | Octonions and quark-lepton symmetry | Furey (2016) | C. Furey, PhD thesis, University of Cambridge; *Phys. Lett.* B785 (2018) | Three generations from $G_2$ Dynkin structure via quaternionic subalgebra enumeration (Ch. 24, Section 24.13). Independent derivation using Fano combinatorics rather than $\mathrm{Cl}(6)$. |
| 10 | Octonions and generations (Todorov-Drenska) | Todorov-Drenska (2018-2020) | I. Todorov, S. Drenska, *Adv. Appl. Clifford Algebr.* 28; *Springer Proc. Math. Stat.* 335 | Falsifiable numerical predictions (Appendix H); deformation parameter connecting speculative to established regimes. |
| 11 | Exceptional structures survey | Baez (2002) | J. C. Baez, *Bull. Amer. Math. Soc.* 39, 145-205 | Computational verification of all algebraic identities via the `octonion_algebra` Python package; automated test suite covering every identity cited. |
| 12 | Non-associative geometry | Albuquerque-Majid (1999) | H. Albuquerque, S. Majid, *J. Algebra* 220, 188-224 | COPBW basis construction with tree-monomial truncation; Catalan-number counting of basis elements (Ch. 9-10, 22, `copbw.py`). |
| 13 | PBW theorem | Poincaré (1900), Birkhoff (1937), Witt (1937) | Standard; see Humphreys, *Introduction to Lie Algebras* | Non-associative COPBW extension: tree monomials replace ordered monomials; termination and confluence proven for the octonionic case (Ch. 9-10, 22, `copbw.py`). |
| 14 | Sabinin algebras | Sabinin (1977-1999) | L. V. Sabinin, *Smooth Quasigroups and Loops* (Kluwer, 1999); earlier papers in *Dokl. Akad. Nauk SSSR* | Interderivability theorem across 7 algebraic structures within the COA framework (Ch. 27, `interderivability.py`). |
| 15 | Malcev algebras | Malcev (1955) | A. I. Malcev, *Mat. Sbornik* 36, 569-576 | Context-dependent adjoint representation using the decompactified Killing form; recovery of Malcev structure as a single-context projection (Ch. 8-9). |
| 16 | Akivis algebras | Akivis (1976) | M. A. Akivis, *Dokl. Akad. Nauk SSSR* 227 | Used as the tangent algebra framework in the COPBW construction; no modification claimed. |
| 17 | Non-associative universal enveloping algebras | Pérez-Izquierdo, Shestakov (2004) | J. M. Pérez-Izquierdo, I. P. Shestakov, *J. Algebra* 272, 379-393 | Explicit COPBW basis enumeration with computational verification; tree-monomial truncation algorithm (Ch. 10, 22, `copbw.py`, `truncation.py`). |
| 18 | $G_2$ holonomy manifolds | Joyce (1996) | D. Joyce, *J. Differential Geom.* 43, 291-328 | Connection to octonionic field equations; decompactified Killing form on $G_2$ manifolds; context integral construction (Ch. 31, `context_integral.py`). |
| 19 | $G_2$ holonomy in M-theory | Acharya (1998), Atiyah-Witten (2002) | B. Acharya, *hep-th/9812011*; M. Atiyah, E. Witten, *Adv. Theor. Math. Phys.* 6 | Standard background for Ch. 31; no modification claimed. |
| 20 | Noether's theorem | Noether (1918) | E. Noether, *Nachr. Ges. Wiss. Göttingen*, 235-257 | Non-associative Noether theorem with coherence charge: new conserved quantity from the squared norm of associator fields (Ch. 16, 18, `conservation.py`). |
| 21 | Klein-Gordon equation | Klein (1926), Gordon (1926) | Standard | Octonionic Klein-Gordon with well-posedness proof for the 7D extension; existence and uniqueness via energy methods (Ch. 12, `time_evolution.py`). |
| 22 | Schafer's non-associative algebra theory | Schafer (1966) | R. D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press) | Standard reference for Ch. 1-5, 9. Framework extends Schafer's treatment via the COA axiom system. |
| 23 | $G_2$ representations | Humphreys (1972), various | J. E. Humphreys, *Introduction to Lie Algebras and Representation Theory* | Branching rules used in Ch. 24 are standard; the explicit computation with code verification is new. |
| 24 | Octonions in string/M-theory | Various (1980s-2000s) | See Baez (2002) for overview; Duff (1998), *hep-th/9808060* | Standard background. This framework does not claim contributions to string/M-theory. |
| 25 | Composition algebras classification | Hurwitz (1898), Kaplansky (1953) | I. Kaplansky, *Proc. Amer. Math. Soc.* 4 | Foundation only. |
| 26 | Bars-Günaydin $G_2$ in physics | Bars, Günaydin (1978) | I. Bars, M. Günaydin, *Phys. Rev. Lett.* 45 | Explicit branching computation code; predictions table (Appendix H). |
| 27 | Ramond on exceptional structures | Ramond (2003) | P. Ramond, *hep-th/0301050* | Systematic COA axiomatization of the exceptional structures Ramond discusses. |
| 28 | Springer-Veldkamp octonions | Springer, Veldkamp (2000) | T. A. Springer, F. D. Veldkamp, *Octonions, Jordan Algebras and Exceptional Groups* (Springer) | Standard reference. Framework extends via COPBW and decompactified Killing form. |
| 29 | Exceptional Jordan algebra $J_3(\mathbb{O})$ | Jordan, von Neumann, Wigner (1934) | P. Jordan, J. von Neumann, E. Wigner, *Ann. of Math.* 35 | Used in Ch. 24 for three-generation arguments; no modification of the algebra itself. |
| 30 | Zhevlakov non-associative algebra | Zhevlakov et al. (1982) | K. A. Zhevlakov et al., *Rings That Are Nearly Associative* (Academic Press) | Standard reference for alternative and Malcev algebras. |
| 31 | Karigiannis $G_2$ geometry | Karigiannis (2009) | S. Karigiannis, *Notices AMS* 58; various papers | Standard background for Ch. 31. No modification of $G_2$ geometry itself. |
| 32 | Conway-Smith on quaternions/octonions | Conway, Smith (2003) | J. H. Conway, D. A. Smith, *On Quaternions and Octonions* (A K Peters) | Standard reference for Ch. 1-2. |

---

## J.3 Division Algebras Tradition

### J.3.1 Prior Work

The four normed division algebras $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$, $\mathbb{O}$ have been studied since the 19th century:

- **Real numbers**: Foundational. No attribution needed.
- **Complex numbers** ($\mathbb{C}$): Formalized by Wessel (1799), Argand (1806), Gauss, and Hamilton.
- **Quaternions** ($\mathbb{H}$): Discovered by Hamilton (1843). The non-commutative multiplication table was published in Hamilton's *Lectures on Quaternions* (1853).
- **Octonions** ($\mathbb{O}$): Discovered by Graves in a letter to Hamilton (December 1843), published by Cayley (1845). The modern treatment via the Cayley-Dickson construction follows Dickson (1919).
- **Hurwitz's theorem** (1898): Only $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$, $\mathbb{O}$ are normed division algebras.

The key modern survey is Baez (2002), which provides an accessible account of the octonions and their connections to geometry, physics, and exceptional structures. Conway and Smith (2003) provide a complementary treatment emphasizing integer forms and lattices.

### J.3.2 What This Framework Adds

Chapters 1-2 of this book are **expository**. They present the normed division algebras following the sources above. The novelty begins in Chapter 3 (alternativity and Moufang identities), where the associator is reframed as an information-carrying object rather than an error term. This reframing is conceptual, not algebraic — the identities themselves are Moufang's (1933).

The specific new contributions built on this foundation are:

- **COA axiom system** (Ch. 6): A formal axiom system that organizes the octonionic algebra, its automorphisms, and its non-associative structure into a unified framework with 6 axioms. Definition 6.3 is new.
- **Deformation parameter $\varepsilon$** (Ch. 4): A continuous parameter that interpolates between the classical ($\varepsilon = 0$, associative) and octonionic ($\varepsilon = 1$, non-associative) regimes. The deformation is implemented in `deformation.py`.

---

## J.4 $G_2$ in Physics

### J.4.1 Prior Work

The connection between $G_2$ and particle physics has a substantial history:

- **Günaydin-Gürsey (1973)**: The foundational paper relating the octonions to quark structure via $G_2 = \mathrm{Aut}(\mathbb{O})$ and the embedding $SU(3) \subset G_2$. They observed that the fundamental $\mathbf{7}$ of $G_2$ decomposes as $\mathbf{3} \oplus \bar{\mathbf{3}} \oplus \mathbf{1}$ under $SU(3)$, providing a natural home for quarks and antiquarks.

- **Bars-Günaydin (1978)**: Extended the $G_2$ framework to include electroweak structure, exploring the full chain $G_2 \supset SU(3) \supset SU(2) \times U(1)$.

- **Ramond (2003)**: Situated the octonionic structures within the broader context of exceptional Lie algebras ($F_4$, $E_6$, $E_7$, $E_8$) and their potential role in fundamental physics.

- **Various string/M-theory applications** (1990s-2000s): $G_2$ holonomy manifolds appear in M-theory compactifications yielding $\mathcal{N} = 1$ supersymmetry in 4D. Key contributors include Acharya, Atiyah, Witten, and others.

### J.4.2 What This Framework Adds

The $G_2$ group itself and its embeddings are entirely standard. This framework does not claim to have discovered $G_2$, the embedding $SU(3) \subset G_2$, or the decomposition of the fundamental representation. What is new:

1. **Explicit branching computation with code** (Ch. 24, `g2_unification.py`): A complete, runnable computation of the chain $G_2 \to SU(3) \to SU(2) \times U(1)$ with explicit matrix representations of all generators, branching coefficients, and embedding indices. Prior work states the branching rules; this framework provides a verifiable computational implementation.

2. **$\sin^2\theta_W = 3/8$ derivation within the COA** (Ch. 24, Appendix H Prediction 1): The tree-level Weinberg angle prediction $3/8$ is shared with $SU(5)$ and $SO(10)$ GUTs. The new content is the derivation within the $G_2$ context specifically, showing that a rank-2 group achieves the same prediction as rank-4 and rank-5 groups, with fewer free parameters.

3. **Identification of 6 coset gauge bosons** (Ch. 24): Specific quantum numbers and collider signatures for the $G_2/SU(3)$ coset generators, which would constitute new gauge bosons beyond the Standard Model.

---

## J.5 Octonions and the Standard Model

### J.5.1 Prior Work

The program of deriving the Standard Model from division algebras has been pursued by several groups:

- **Dixon (1994)**: Proposed that the full algebraic structure $\mathbb{R} \otimes \mathbb{C} \otimes \mathbb{H} \otimes \mathbb{O}$ encodes the Standard Model. His book *Division Algebras* remains a foundational reference.

- **Furey (2012-2018)**: Showed that a single generation of Standard Model fermions (with correct quantum numbers) can be obtained from the algebra $\mathbb{C} \otimes \mathbb{H} \cong \mathrm{Cl}(6)$ acting on a minimal left ideal. Extended this to the full $\mathbb{C} \otimes \mathbb{O}$ in later work.

- **Todorov-Drenska (2018-2020)**: Explored the connection between the exceptional Jordan algebra $J_3(\mathbb{O})$ and the three generations of fermions, providing representation-theoretic arguments for the generation structure.

- **Boyle (2020)**: Proposed that the algebra $\mathbb{C} \otimes \mathbb{H} \otimes \mathbb{O}$ (the "Dixon algebra") encodes the Standard Model with three generations through its ideal structure.

- **Stoica (2018)**: Investigated the relationship between octonions and the Standard Model using Clifford algebra techniques.

### J.5.2 What This Framework Adds

The prior work establishes that the octonions *can* accommodate the Standard Model. What remains open — and what motivates the extensions in this book — is the question of *why* the octonions, and whether the accommodation leads to falsifiable predictions. The new contributions are:

1. **COA axiom system** (Ch. 6, Definition 6.3): A formal axiom system that goes beyond the octonion algebra itself to include the context space, the decompactified Killing form, and the projection principle. None of the prior work cited above provides an axiomatic framework at this level of generality.

2. **Deformation parameter $\varepsilon$** (Ch. 4, `deformation.py`): A continuous parameter that controls the degree of non-associativity. At $\varepsilon = 0$ the framework reduces to classical (associative) physics; at $\varepsilon = 1$ it gives the full octonionic structure. This parameter makes the framework falsifiable: if experiments bound $\varepsilon < \varepsilon_0$ for some threshold, specific predictions are ruled out.

3. **Falsifiable numerical predictions** (Appendix H): Ten concrete, computable predictions with explicit falsification criteria. Prior work in octonionic physics is largely structural ("the groups fit together"); this framework commits to numbers.

4. **Computational verification package** (`octonion_algebra/`): A complete Python implementation allowing independent verification of every algebraic identity and numerical prediction. No prior octonionic physics framework that we are aware of ships with a computational verification suite of this scope.

---

## J.6 Non-Associative Algebra

### J.6.1 Prior Work

The algebraic structures underlying the octonionic framework have deep roots:

- **Alternative algebras**: Systematically studied by Zorn (1933), who introduced vector matrix representations, and later by Schafer (1966) in his definitive textbook.

- **Malcev algebras**: Introduced by Malcev (1955) as the tangent algebras of Moufang loops, generalizing Lie algebras. The imaginary octonions $\mathrm{Im}(\mathbb{O})$ with the commutator bracket form the prototypical Malcev algebra.

- **Akivis algebras**: Introduced by Akivis (1976) as the tangent algebras of general local analytic loops, further generalizing Malcev algebras.

- **Sabinin algebras**: The most general tangent algebra construction, due to Sabinin (1977-1999). Sabinin algebras have multilinear operations of all arities and are the tangent algebras of arbitrary smooth loops.

- **Non-associative universal enveloping algebras**: Constructed by Pérez-Izquierdo and Shestakov (2004), extending the PBW theorem to Malcev algebras and, conditionally, to Sabinin algebras.

- **Zhevlakov et al. (1982)**: The comprehensive reference *Rings That Are Nearly Associative* covers alternative, Jordan, and Lie-admissible algebras systematically.

### J.6.2 What This Framework Adds

The algebraic structures listed above are used as given. The new contributions are:

1. **COPBW basis with Catalan counting** (Ch. 9-10, 22, `copbw.py`): The existence of a PBW-type basis for non-associative enveloping algebras was proven by Pérez-Izquierdo and Shestakov. This framework provides an explicit *construction* using tree monomials, with the basis elements enumerated by Catalan numbers $C_n$. The termination and confluence of the reduction algorithm are proven for the octonionic case, with explicit computational verification for up to 3 generators.

2. **Tree-monomial truncation algorithm** (Ch. 10, `truncation.py`): A practical algorithm for truncating infinite COPBW expansions to finite computations, with error bounds. This is a computational contribution with no direct analog in the prior literature.

3. **Interderivability theorem** (Ch. 27, `interderivability.py`): A new structural result proving that any well-formed expression in the COA can be transformed into any other sharing a common factor, through a finite sequence of octonionic operations. The proof uses $G_2$ transitivity on $S^6$ and the composition algebra property.

4. **Fano orientation invariance** (Ch. 4, `fano_invariance.py`): The proof that the sign pattern of octonionic associators is invariant under the full automorphism group $\mathrm{PSL}(2, \mathbb{F}_7) \cong \mathrm{GL}(3, \mathbb{F}_2)$ of the Fano plane (order 168). This is a combinatorial result about the interaction between the Fano plane's symmetry group and the associator structure.

---

## J.7 Exceptional Geometry

### J.7.1 Prior Work

The geometry of $G_2$-structures and $G_2$-holonomy manifolds is a substantial field:

- **Joyce (1996)**: Constructed the first compact 7-manifolds with $G_2$ holonomy, proving a conjecture of Berger's. These "Joyce manifolds" are foundational to $G_2$ geometry.

- **Karigiannis (2009 and later)**: Provided accessible treatments of $G_2$ geometry including flows of $G_2$-structures, calibrated submanifolds, and connections to physics.

- **Kovalev (2003)**: Constructed $G_2$-holonomy manifolds via twisted connected sums, greatly expanding the known examples.

- **Corti-Haskins-Nordström-Pacini (2015)**: Systematized the twisted connected sum construction, producing millions of topological types of compact $G_2$-manifolds.

- **Associative and coassociative calibrations**: The associative 3-form $\phi$ and coassociative 4-form $*\phi$ on a $G_2$-structure manifold calibrate 3- and 4-dimensional submanifolds, respectively. This is standard $G_2$ geometry following Harvey and Lawson (1982).

### J.7.2 What This Framework Adds

The $G_2$ geometry itself is used as given. The new contributions are:

1. **Decompactified Killing form $B_\mu$** (Ch. 8, `context_integral.py`): The classical Killing form $B(X,Y) = \mathrm{tr}(\mathrm{ad}_X \circ \mathrm{ad}_Y)$ is a finite trace. The decompactified form $B_\mu(X,Y) = \int_\Omega \mathrm{tr}(\mathrm{ad}_X^{(\omega)} \circ \mathrm{ad}_Y^{(\omega)}) d\mu(\omega)$ replaces this with an integral over a measure space of contexts. This construction has no direct analog in the cited $G_2$ geometry literature.

2. **Context integral on $G_2$ manifolds** (Ch. 31, `context_integral.py`): Application of the decompactified Killing form to $G_2$-holonomy manifolds, producing a new invariant that depends on the measure structure of the context space.

3. **Connection to octonionic field equations** (Ch. 31, 33): The octonionic Einstein equations, Yang-Mills equations, and Klein-Gordon equation are formulated on $G_2$-structure manifolds. While the individual equations have precedent in the physics literature, the systematic derivation from the COA axiom system is new.

---

## J.8 What Is Genuinely New in This Framework

This section collects every construction in this book that we believe to be new, with precise chapter and code references. Each entry states what the construction is, why we believe it is new, and how it can be independently verified.

### J.8.1 The COA Axiom System (Ch. 6, Definition 6.3)

**What it is.** A formal axiom system consisting of 6 axioms (COA-1 through COA-6) that provides the logical foundation for all derived results. The axioms specify: an octonionic nucleus (COA-1), the associator functional (COA-2), the decompactified Killing form (COA-3), the projection principle (COA-4), coherence conservation (COA-5), and the COPBW property (COA-6).

**Why we believe it is new.** Prior work on octonionic physics (Dixon, Furey, Todorov-Drenska) operates within the octonion algebra directly, without a formal axiomatic superstructure. The COA axioms organize the algebra, its automorphisms, and its applications into a single deductive system. We have found no comparable axiomatization in the published literature.

**Verification.** `axiom_verification.py` checks each axiom computationally for the standard octonion model.

### J.8.2 The Deformation Parameter $\varepsilon$ (Ch. 4, `deformation.py`)

**What it is.** A continuous parameter $\varepsilon \in [0, 1]$ such that at $\varepsilon = 0$ all associators vanish (recovering associative algebra) and at $\varepsilon = 1$ the full octonionic structure is present. The deformation is smooth and preserves alternativity for all $\varepsilon$.

**Why we believe it is new.** Deformation theory of algebras is well-established (Gerstenhaber, 1964). However, the specific one-parameter deformation that continuously interpolates between an associative algebra and the octonions while preserving alternativity at every stage appears to be new. The key constraint is that alternativity (not just the algebra product) must be preserved throughout the deformation.

**Verification.** `deformation.py` implements the deformation and verifies alternativity at 100 sample values of $\varepsilon$.

### J.8.3 The Decompactified Killing Form $B_\mu$ (Ch. 8, `context_integral.py`)

**What it is.** The extension of the Killing form from a finite trace to an integral over a measure space:
$$B_\mu(X, Y) = \int_\Omega \mathrm{tr}\left(\mathrm{ad}_X^{(\omega)} \circ \mathrm{ad}_Y^{(\omega)}\right) d\mu(\omega)$$

**Why we believe it is new.** The Killing form is a standard object (Cartan, 1894; Killing, 1888). Extensions to infinite-dimensional Lie algebras exist (Kac-Moody algebras have Killing forms). But the specific construction of integrating the trace of context-dependent adjoint representations over a measure space, and applying this to a non-associative (Malcev/Sabinin) algebra, appears to be new. The closest prior work is the theory of continuous fields of C*-algebras (Dixmier, 1977), but that theory is restricted to associative algebras and does not involve the Killing form construction.

**Verification.** `context_integral.py` computes $B_\mu$ numerically for several measure spaces and verifies non-degeneracy and $G_2$-invariance.

### J.8.4 The COPBW Basis with Catalan Counting (Ch. 9-10, 22, `copbw.py`)

**What it is.** An explicit basis for the non-associative universal enveloping algebra $U_\mathbb{O}(S)$ consisting of tree monomials — planar rooted binary trees with generator-labeled leaves — where the number of tree shapes at degree $n$ is the Catalan number $C_{n-1}$. The reduction algorithm has proven termination and confluence for the octonionic case.

**Why we believe it is new.** Pérez-Izquierdo and Shestakov (2004) proved the existence of a PBW-type theorem for non-associative enveloping algebras. Their proof is abstract (using a filtration argument). The explicit construction via tree monomials, the connection to Catalan numbers, and the computational reduction algorithm appear to be new. The computational verification for up to 3 generators via `copbw.py` provides concrete evidence beyond the existence proof.

**Verification.** `copbw.py` enumerates tree monomials, verifies linear independence by explicit computation, and checks the Catalan count.

### J.8.5 Fano Orientation Invariance Theorem (Ch. 4, `fano_invariance.py`)

**What it is.** The theorem that the sign pattern of octonionic associators — specifically, the map $(i, j, k) \mapsto \mathrm{sgn}([e_i, e_j, e_k])$ for Fano triples — is invariant under all 168 automorphisms of the Fano plane $\mathbb{F}_2P^2$.

**Why we believe it is new.** The automorphism group of the Fano plane ($\mathrm{PSL}(2, \mathbb{F}_7) \cong \mathrm{GL}(3, \mathbb{F}_2)$, order 168) and its action on the octonion multiplication table are well-studied. The specific statement that the associator sign pattern is invariant appears to be a new observation, albeit one that follows from known facts about the interaction between Fano automorphisms and $G_2$.

**Verification.** `fano_invariance.py` checks all 168 automorphisms against all 7 Fano triples, verifying sign invariance exhaustively.

### J.8.6 Falsifiable Numerical Predictions (Appendix H, `predictions.py`)

**What they are.** Ten concrete numerical predictions derived from the octonionic framework, each with: the computed value, the code that produces it, the automated test that verifies it, and the experimental measurement that would falsify it.

**Why we believe they are new.** Individual predictions (such as $\sin^2\theta_W = 3/8$) are shared with other GUT frameworks. The collection of 10 predictions specifically derived from the $G_2$/octonionic structure, presented with computational verification and explicit falsification criteria, appears to be new as a systematic program.

**Verification.** `pytest tests/test_predictions.py -v` runs all prediction tests.

### J.8.7 Non-Associative Noether Theorem with Coherence Charge (Ch. 16, 18, `conservation.py`)

**What it is.** An extension of Noether's theorem to systems with non-associative symmetry (Moufang loop symmetry rather than Lie group symmetry). The key new result is the identification of a new conserved quantity — the *coherence integral* $\int \|[a, b, c]\|^2 d\mu$ — that is invisible in any associative projection (it projects to zero on quaternionic subalgebras).

**Why we believe it is new.** Extensions of Noether's theorem to non-standard settings exist: supersymmetric Noether theorems, Noether theorems for discrete symmetries (via Noether's second theorem), and Noether theorems in non-commutative geometry. However, a Noether theorem for Moufang loop symmetry, with the specific conserved quantity being the squared-norm integral of the associator, appears to be new.

**Verification.** `conservation.py` numerically verifies coherence conservation under random $G_2$ transformations. `tests/test_predictions.py` includes automated tests.

### J.8.8 Interderivability Theorem (Ch. 27, `interderivability.py`)

**What it is.** The theorem that any two well-formed expressions in the COA sharing a common octonionic factor can be connected by a finite sequence of COA operations. The proof is constructive, using $G_2$ transitivity on $S^6 \subset \mathrm{Im}(\mathbb{O})$.

**Why we believe it is new.** This is a structural theorem about the COA specifically. It has no direct analog in classical Lie theory (where the analogous statement would be trivial, since associative enveloping algebras are connected by construction). The non-triviality arises from non-associativity: in a non-associative algebra, it is not obvious that every expression can be reached from every other.

**Verification.** `interderivability.py` implements the constructive transformation algorithm and verifies it on random expression pairs.

### J.8.9 Octonionic Time Evolution Well-Posedness (Ch. 12, `time_evolution.py`)

**What it is.** A proof of existence, uniqueness, and continuous dependence on initial data for the octonionic differential equation $\dot{x}(t) = f(x(t))$ where $x(t) \in \mathbb{O}$ and $f: \mathbb{O} \to \mathbb{O}$ is Lipschitz. The proof adapts the Picard-Lindelöf theorem to the non-associative setting, with the key difficulty being that the Picard iteration $x_{n+1}(t) = x_0 + \int_0^t f(x_n(s)) ds$ involves octonionic-valued integrals where the integration does not commute with multiplication.

**Why we believe it is new.** The Picard-Lindelöf theorem is standard for real and complex ODEs. Extensions to quaternionic ODEs exist. The octonionic case requires handling the additional complication that the integral $\int f(x) dx$ is not associative with respect to external multiplication. The specific well-posedness proof for the octonionic case, with explicit energy estimates, appears to be new.

**Verification.** `time_evolution.py` implements numerical octonionic time evolution and verifies convergence and stability.

---

## J.9 Honest Assessment: What Remains Speculative

Intellectual honesty requires acknowledging not only what is new but what is uncertain. The following aspects of this framework range from constructive-but-incomplete to genuinely speculative.

### J.9.1 Established (Rigorously Proven or Computationally Verified)

These results are either mathematically proven or verified by exhaustive computation:

- All algebraic identities in Chapters 1-5 (these are established mathematics, verified computationally).
- The COA axiom system is self-consistent for the standard octonion model (Ch. 6, verified by `axiom_verification.py`).
- The COPBW basis construction terminates and is confluent for up to 3 generators (Ch. 22, verified by `copbw.py`).
- Coherence conservation holds under $G_2$ transformations (Ch. 18, verified by `conservation.py`).
- Non-gameable alignment for team sizes $m = 3, 4$ (Ch. 26, verified by `alignment.py`).
- The Fano orientation invariance theorem (Ch. 4, verified exhaustively by `fano_invariance.py`).
- All 10 numerical predictions in Appendix H are internally consistent and computationally verified.

### J.9.2 Constructive but Incomplete

These results have rigorous mathematical structure but contain gaps that are explicitly identified:

- The COPBW confluence proof for arbitrary (not just octonionic) Sabinin algebras is conditional on Sabinin coherence (Ch. 22, Section 22.8).
- The non-gameable alignment theorem for team sizes $m \geq 5$ is proven generically (with probability 1 under Haar measure) but not for every specific configuration (Ch. 26, Section 26.7).
- The three-generation derivation from $G_2$ Dynkin structure (Ch. 24, Section 24.13) presents five independent arguments, each suggestive but none constituting a complete proof. This is flagged as Appendix F, Problem 36.
- The non-associative Noether theorem (Ch. 16) is derived for alternative algebras; extension to general Sabinin algebras is conjectured.

### J.9.3 Speculative

These aspects of the framework are interesting proposals that have not been empirically validated:

- The claim that the octonionic framework describes nature (as opposed to being a consistent mathematical structure that *could* describe nature). This is an empirical question, addressed by the falsifiable predictions in Appendix H.
- Applications to fluid dynamics (Ch. 32), economics (Ch. 37), political science (Ch. 35), and biology (Ch. 36). These chapters contain valid mathematical constructions (the equations are correctly derived) alongside interpretive claims that are speculative.
- The philosophical arguments in Part VI (Ch. 38-42). These are conceptual proposals grounded in the framework, not mathematical proofs.
- The connection between the deformation parameter $\varepsilon$ and observable physics. The parameter is mathematically well-defined, but its physical interpretation (if any) is speculative.

### J.9.4 The Central Open Question

The deepest question this framework poses is whether non-associativity is a feature of nature or merely of our mathematics. If nature is non-associative — if the associator carries genuine physical information — then the octonionic framework makes predictions that differ from any associative theory. These predictions are collected in Appendix H. If all such predictions are falsified, the framework fails as physics (while remaining valid as mathematics).

We do not know the answer. We have tried to make the question precise enough to be answerable.

---

## J.10 Citation Index

For convenience, the full citations for all works referenced in this appendix, ordered alphabetically by first author:

1. Acharya, B. (1998). M-theory, Joyce orbifolds and super Yang-Mills. *Adv. Theor. Math. Phys.* 3, 227-248. arXiv: hep-th/9812011.
2. Akivis, M. A. (1976). Local algebras of a multidimensional three-web. *Dokl. Akad. Nauk SSSR* 227, 1273-1276.
3. Albuquerque, H., Majid, S. (1999). Quasialgebra structure of the octonions. *J. Algebra* 220, 188-224.
4. Artin, E. (1927). Zur Theorie der hyperkomplexen Zahlen. *Abh. Math. Sem. Hamburg* 5, 251-260.
5. Atiyah, M., Witten, E. (2002). M-theory dynamics on a manifold of $G_2$ holonomy. *Adv. Theor. Math. Phys.* 6, 1-106.
6. Baez, J. C. (2002). The octonions. *Bull. Amer. Math. Soc.* 39, 145-205.
7. Bars, I., Günaydin, M. (1978). Construction of Lie algebras and Lie superalgebras from ternary algebras. *J. Math. Phys.* 20, 1977-1985.
8. Boyle, L. (2020). The standard model, the exceptional Jordan algebra, and triality. arXiv: 2006.16265.
9. Cartan, E. (1894). *Sur la structure des groupes de transformations finis et continus.* Thesis, Paris.
10. Conway, J. H., Smith, D. A. (2003). *On Quaternions and Octonions.* A K Peters, Natick, MA.
11. Corti, A., Haskins, M., Nordström, J., Pacini, T. (2015). $G_2$-manifolds and associative submanifolds via semi-Fano 3-folds. *Duke Math. J.* 164, 1971-2092.
12. Dickson, L. E. (1919). On quaternions and their generalization and the history of the eight square theorem. *Ann. of Math.* 20, 155-171.
13. Dixon, G. M. (1994). *Division Algebras: Octonions, Quaternions, Complex Numbers and the Algebraic Design of Physics.* Kluwer Academic Publishers.
14. Duff, M. J. (1998). Anti-de Sitter space, branes, singletons, superconformal field theories and all that. *Int. J. Mod. Phys.* A14, 815-844.
15. Furey, C. (2016). *Standard model physics from an algebra?* PhD thesis, University of Cambridge.
16. Furey, C. (2018). Three generations, two unbroken gauge symmetries, and one eight-dimensional algebra. *Phys. Lett.* B785, 84-89.
17. Gerstenhaber, M. (1964). On the deformation of rings and algebras. *Ann. of Math.* 79, 59-103.
18. Gordon, W. (1926). Der Comptoneffekt nach der Schrödingerschen Theorie. *Z. Phys.* 40, 117-133.
19. Graves, J. T. (1843). Letter to W. R. Hamilton, December 26, 1843. Published in Hamilton's collected works.
20. Günaydin, M., Gürsey, F. (1973). Quark structure and octonions. *J. Math. Phys.* 14, 1651-1667. (Also *Phys. Rev.* D8, 3851.)
21. Hamilton, W. R. (1843). On a new species of imaginary quantities connected with a theory of quaternions. *Proc. Royal Irish Acad.* 2, 424-434.
22. Harvey, R., Lawson, H. B. (1982). Calibrated geometries. *Acta Math.* 148, 47-157.
23. Humphreys, J. E. (1972). *Introduction to Lie Algebras and Representation Theory.* Springer, New York.
24. Hurwitz, A. (1898). Über die Composition der quadratischen Formen von beliebig vielen Variablen. *Nachr. Ges. Wiss. Göttingen*, 309-316.
25. Jordan, P., von Neumann, J., Wigner, E. (1934). On an algebraic generalization of the quantum mechanical formalism. *Ann. of Math.* 35, 29-64.
26. Joyce, D. (1996). Compact Riemannian 7-manifolds with holonomy $G_2$. I, II. *J. Differential Geom.* 43, 291-328 and 329-375.
27. Kaplansky, I. (1953). Infinite-dimensional quadratic forms permitting composition. *Proc. Amer. Math. Soc.* 4, 956-960.
28. Karigiannis, S. (2009). What is... a $G_2$-manifold? *Notices Amer. Math. Soc.* 58, 580-581.
29. Klein, O. (1926). Quantentheorie und fünfdimensionale Relativitätstheorie. *Z. Phys.* 37, 895-906.
30. Kovalev, A. (2003). Twisted connected sums and special Riemannian holonomy. *J. Reine Angew. Math.* 565, 125-160.
31. Malcev, A. I. (1955). Analytic loops. *Mat. Sbornik* 36, 569-576. (In Russian.)
32. Moufang, R. (1933). Alternativkörper und der Satz vom vollständigen Vierseit. *Abh. Math. Sem. Hamburg* 9, 207-222.
33. Noether, E. (1918). Invariante Variationsprobleme. *Nachr. Ges. Wiss. Göttingen*, 235-257.
34. Pérez-Izquierdo, J. M., Shestakov, I. P. (2004). An envelope for Malcev algebras. *J. Algebra* 272, 379-393.
35. Ramond, P. (2003). Exceptional groups and physics. arXiv: hep-th/0301050.
36. Sabinin, L. V. (1999). *Smooth Quasigroups and Loops.* Kluwer Academic Publishers.
37. Schafer, R. D. (1966). *An Introduction to Nonassociative Algebras.* Academic Press, New York.
38. Springer, T. A., Veldkamp, F. D. (2000). *Octonions, Jordan Algebras and Exceptional Groups.* Springer, Berlin.
39. Stoica, O. C. (2018). The Standard Model algebra — leptons, quarks, and gauge from the complex Clifford algebra $\mathrm{Cl}_6$. *Adv. Appl. Clifford Algebr.* 28, 52.
40. Todorov, I., Drenska, S. (2018). Octonions, exceptional Jordan algebra and the role of the group $F_4$ in particle physics. *Adv. Appl. Clifford Algebr.* 28, 82.
41. Zhevlakov, K. A., Slin'ko, A. M., Shestakov, I. P., Shirshov, A. I. (1982). *Rings That Are Nearly Associative.* Academic Press, New York.
42. Zorn, M. (1933). Alternativkörper und quadratische Systeme. *Abh. Math. Sem. Hamburg* 9, 395-402.

---

*This appendix is intended as a living document. If any attribution is incorrect or incomplete, or if prior work has been overlooked, we welcome correction. The goal is honest positioning, not priority claims. For the open problems that arise from this framework, see Appendix F. For the concrete numerical predictions, see Appendix H.*
