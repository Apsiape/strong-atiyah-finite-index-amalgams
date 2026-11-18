# The strong Atiyah conjecture for finite-index amalgams

Nidhal Mghirbi and Seth Douglas. Preprint, version 1.0.0, November 2026. [Archive DOI](https://doi.org/10.5281/zenodo.24356021) (all versions); version 1.0.0: [10.5281/zenodo.24356022](https://doi.org/10.5281/zenodo.24356022)

## Abstract

Let G = A *_E B, where E has finite index in both vertex groups. We prove that the torsion-free strong Atiyah conjecture over a subfield of ℂ passes from A and B to G. The division closure of the group algebra is the universal field of fractions of the coproduct of the vertex division rings over the edge division ring. The proof starts with an analytic formula for the rank of a product of vertex matrices, valid for arbitrary group amalgams. At finite index we show that a subspace over the edge division ring attains the minimum in that formula. Applications include torsion-free finite-index subgroups of SL₂ over rings of S-integers in ℚ and in imaginary quadratic fields, and the simple lattices in products of trees constructed by Burger and Mozes. For these lattices, the point eigenvalues of matrices over Q̄[G] in the regular representation are algebraic.

## Results

Theorem and corollary numbers refer to `paper/main.pdf`.

- **Theorem A.** Let G = A *_E B be a countable amalgam with E of finite index in A and in B, and let K be a subfield of ℂ. If the division closures D_K(A) and D_K(B) are division rings, then every matrix over K[G] has integral von Neumann rank, and D_K(G) is the universal field of fractions of the coproduct D_K(A) *_{D_K(E)} D_K(B).
- **Theorem B.** For any countable group amalgam, the rank of a product XY of vertex matrices equals the minimum, over projections w in the edge von Neumann algebra, of rk(Xw) + rk((1 − w)Y), and there is a least minimizing projection. Theorem 5.1 shows that at finite index a subspace over the edge division ring attains the minimum.
- **Corollary 6.2.** Tor₁ of the affiliated ring over the vertex coproduct vanishes, giving the conclusion of Sánchez-Peralta's Conjecture 7.1 for these amalgams.
- **Corollary 7.1.** The simple groups of Burger and Mozes and Rattaggi's finitely presented torsion-free simple group satisfy the strong Atiyah conjecture over ℂ.
- **Corollary 7.2.** Every torsion-free finite-index subgroup of SL₂ over the S-integers of ℚ or of an imaginary quadratic field satisfies the strong Atiyah conjecture over ℂ.
- **Corollary 8.2.** Under coefficient-rank invariance at both vertices, point eigenvalues of matrices over K[G] in the regular representation are algebraic over K; this applies to the simple groups of Corollary 7.1.

Prior work, as the paper credits it: Sánchez-Peralta proved the conjecture for graphs of groups with finite edge groups; Fisher and Sánchez-Peralta embedded these group algebras in division rings abstractly, which already gives Kaplansky's zero-divisor and idempotent conjectures for the groups of Corollary 7.1; Theorem B also follows from the operator-valued atom theorem of Belinschi, Bercovici and Liu; congruence-type cases of Corollary 7.2 follow from Farkas and Linnell with Jaikin-Zapirain's base change.

## Archive contents

- `paper/` contains the manuscript PDF (14 pages), its LaTeX source with the bibliography inline, the plain-text abstract and build instructions.
- `verification/` contains a standard-library Python program that checks finite examples (a finite linear model of Lemma 4.2, a rational cut, finite dihedral ranks, the level-35 matrix modulo 5 and 7, and the two index calculations for Rattaggi's group), its expected output, and a statement-by-statement proof guide. The proofs of the general statements are in the manuscript.
- The root contains citation metadata, licensing information and `SHA256SUMS`, the SHA-256 digest of every distributed file except the checksum list itself. Verify it from the archive root with `sha256sum -c SHA256SUMS`.

## Build and check

From `paper/`, run pdfLaTeX three times without shell escape. From the archive root, run `python3 verification/check_examples.py` and compare its output with `verification/expected_output.txt`. The tested engine is MiKTeX-pdfTeX 4.23 (MiKTeX 25.12).

## Citation and license

Mghirbi, Nidhal, and Seth Douglas (2026). *The strong Atiyah conjecture for finite-index amalgams*. Version 1.0.0. [Archive DOI](https://doi.org/10.5281/zenodo.24356021) · [Citation metadata](CITATION.cff)

Paper and documentation are licensed under CC BY 4.0; the verification script under MIT or Apache 2.0, at your option. [Licensing details](RIGHTS.md)
