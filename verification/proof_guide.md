# Proof guide

## Four sentences from the introduction

Mix the two copies of a vertex by a scalar rotation and differentiate the resulting constant-rank pencil to force a containment between the kernels and images of different copies. Joining those intersections produces the least projection over the edge that attains the analytic minimum. Finite index makes each vertex space finite-dimensional over the edge division ring, so the trace of a projection becomes the integral of the dimensions of its greatest maximizing subspaces. The identity-coset coefficient maps the source maximizers into the target maximizers, and the resulting pointwise bound attains equality almost everywhere, producing a rational space of exactly the required cost.

## Statements to check

| Statement | Main inference | Hypotheses and dependence |
| --- | --- | --- |
| Theorem B | The rotation gives the four-copy inclusion, which forces every row join plus every column join of the intersection modules to equal the join of all intersections. | One countable binary group amalgam. The two vertex matrices may be unbounded and rectangular. Only the two projections used in the tangent step need be bounded. The least optimizer depends on the pair of matrices. |
| Second proof of Theorem B | Enlarge both projections by the same small spectral projection in the support corner. The expected meet then has a bounded inverse, so the operator-valued atom theorem applies. | The trace of the enlargement tends to zero even if the original expectation has spectrum tending to zero. This argument uses the trace-preserving conditional expectation. |
| Lemma 4.1 | Right coset coordinates give finite free modules. The trace of each diagonal block after restriction is the original trace. | Restriction multiplies dimension by the index. Scalar extension preserves rational dimension. The two operations serve different purposes. The normal core is taken separately at each vertex. |
| Lemma 4.2 | Supermodularity and a finite set of possible dimensions force a greatest optimizer. The derivative of the upper envelope integrates its dimension. | The rational subspace depends on the projection and the penalty parameter. At every parameter its greatest choice is invariant under the vertex division ring. |
| Theorem 5.1 | A quotient on the source side injects into a quotient on the target side after extending the edge scalars. This rules out strict enlargement of the target optimizer under the comparison map. | Each threshold comparison uses edge dimensions on both sides. Right multiplication by inverse coset representatives recovers all the coordinates. An attaining parameter is chosen after the analytic optimizer and matrices. |
| Theorem A | After stable linearization the rational edge minimum gives an integer rank. A Schur complement tests nonzero elements in the division closure. The same minimum bounds ranks in every compatible skew field. | No assumption of a universal map from an abstract skew field into the affiliated ring enters the proof. Cohn supplies the universal field for the coproduct of vertex division rings. |
| Corollary 6.2 | The coproduct localization has vanishing first self-Tor. Expand the two affiliated modules in bases over its division field. | The comparison to Sánchez-Peralta's Conjecture 7.1 uses a conjugation-invariant coefficient field. |
| Corollary 7.1 | Apply the finite-index amalgam theorem to the published splittings of free groups. | The Rattaggi indices use the known finiteness of the edge indices as well as the free ranks. |
| Corollary 7.2 | Density in one local factor gives a single quotient edge. Adding its endpoint stabilizer to the compact open conditions takes one place out of the induction. | The subgroup is torsion-free and finite-index. For the base case, rational or imaginary quadratic coefficients yield discreteness in the complex Lie group. No global generator of the prime ideal is assumed. |
| Proposition 8.1 and Corollary 8.2 | A coefficient automorphism acts on the vertex fields, the coproduct, and its universal localization. A transcendental central eigenvalue would have an infinite orbit among at most n eigenvalues. | Requires coefficient-rank invariance at both vertices. It is available for free vertices. No wild automorphism is applied to an orthogonal projection. |

## What the code checks

The program exhausts all 125 triples of subspaces of a two-dimensional vector space over the field of two elements, using the weights 1/6, 1/3 and 1/2. It computes every breakpoint of the overlap scores, tests greatestness at the breakpoints and between them, and integrates the resulting dimensions exactly. This is a finite linear model of the optimization in Lemma 4.2.

It also checks an explicit rational cut, ranks in 19 finite dihedral quotients, powers of the displayed level-35 matrix modulo 5 and 7, and the two index calculations for Rattaggi's group. The finite dihedral ranks need not equal the rank in the infinite group at a fixed quotient. The manuscript proves the infinite-group value directly from square summability. All computations use integers or rational numbers.

The proofs of the general statements are in the manuscript. The code and this dependency guide are supplementary checks.

