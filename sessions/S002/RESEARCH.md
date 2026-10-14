# P001C-S002 — exponent-bridge binary kill gate (2026-10-14)

## Decision: NO — RETURN_PARENT / PAUSE

**NO NEW UNIFORM ALPHABET EXPONENT BOUND; ZERO CLAIMED NOVEL THEOREMS.** This session did not produce an independently proved, non-recycled mechanism saving `D^(-epsilon*n)` against Naslund–Sawin's `2n/3` support count for EVERY three-sunflower-free `A subset [D]^n` with unrestricted `D>=3,n>=1`. There is a proved *elementary* first-moment marginal inequality, a fully specified but **UNPROVED** density-sensitive auxiliary conjecture, precise deductions that such a conjecture would have, quantified stress against S001 constructions, and a new directly checked prior-art item. **No S003 is authorized; refer strategic choice to SUN-PARENT-S006 on separate owner invocation.**

### 1. Definitions and original quantifiers

For `D>=3,n>=1` and `A subset [D]^n` consisting of distinct words, a 3-sunflower is a triple of DISTINCT words such that every coordinate has multiplicity type `(3)` or `(1,1,1)`; a sunflower-free family has a `(2,1)` coordinate in every distinct triple. Define `U(D,n)` to be the maximum size of a sunflower-free family. The original quantitative target is `exists K<infinity, delta>0: forall integers D>=3,n>=1, U(D,n)<=(K*D^(2/3-delta))^n`. Fixed positive delta emphatically does NOT prove a D-independent C^n bound or Erdos–Rado (even for three petals).

Naslund–Sawin 2017 published Theorem 2, arXiv v1 Theorem 5, gives `U(D,n) <= (3*(D-1)^(2/3)/2^(2/3))^n`. The proof uses a character expansion with at most 2n nontrivial occurrences across 3 variable groups, at least one side <=2n/3. A 2026 triangular-tensor polynomial factor in the BOOLEAN set-family case does not alter that alphabet D exponent.

### 2. Exact, positive but insufficient collision-to-atom inequality (fully proved)

Let `m=|A|>=3`, and let `p_{i,a}=|{x in A:x_i=a}|/m`; set `p_*=max_{i,a} p_{i,a}`. For independent uniformly sampled `X,Y,Z in A`, the chance the three chosen *words* are pairwise distinct is
`q_m=(m-1)(m-2)/m^2`.
For each fixed coordinate `i`, the probability of exactly two equal symbols is
`b_i=3 sum_{a=1}^D p_{i,a}^2(1-p_{i,a}) <= 3 sum_a p_{i,a}^2 <= 3p_*`.
When X,Y,Z are distinct words, sunflower-freeness guarantees at least one bad (2,1) coordinate. The union bound therefore proves
`(m-1)(m-2)/m^2 <= sum_i b_i <= 3n p_*`,
so **`p_* >= (m-1)(m-2)/(3nm^2)`** for all D,n,m>=3, with NO near-extremal assumption.

If ALL one-coordinate marginals are uniform on D symbols, `p_{i,a}=1/D`, the exact bad-coordinate probability is `3(D-1)/D^2`, yielding the necessary condition
`n >= D^2 (m-1)(m-2) / (3(D-1)m^2)`,
which is asymptotically `n >= D/3` when both m and D are large (more precisely `~D^2/[3(D-1)]`). This independently checked elementary count does not give an n-uniform D-power saving. A desired atom of size `D^(-7/12)` follows from THIS inequality only in the limited regime `n <= (m-1)(m-2)D^(7/12)/(3m^2)`. The original theorem permits n arbitrarily larger than this. Do not declare a new theorem or originality.

### 3. ONE precise near-extremal auxiliary lemma: UNPROVED, and currently a repackaging

**Candidate L(16,2,5/8,7/12)** (NOT asserted true): for EVERY integer `D>=16`, EVERY integer `n>=1`, EVERY distinct, three-sunflower-free `A subset [D]^n`, IF
`|A| >= (2D^(5/8))^n`
then there exists a coordinate `1<=i<=n` and symbol `a in [D]` with
`|{x in A:x_i=a}|/|A| >= D^(-7/12)`.
All constants and quantifiers are explicit and its density premise is numeric, independent of the unknown U and independent of the desired *statement* (not involving U or an assumed target inequality). It is NOT a proved lemma and its truth/non-vacuity for arbitrarily large D,n is unknown.

**If L were independently proved**, minimal-n induction immediately proves `U(D,n)<=(2D^(5/8))^n` for all D>=16: if at minimal n a family exceeded `M_n=(2D^(5/8))^n`, choose the heavy fibre; it is sunflower-free of length n−1 and has size `>D^(-7/12)M_n=2D^(1/24)M_{n-1}>M_{n-1}`, contradiction. At n=1, the fibre is of size <=1, also contradicting the displayed inequality (define `M_0=1`). For 3<=D<16 use the trivial `U(D,n)<=D^n<=(3D^(5/8))^n` since `D^(3/8)<16^(3/8)<3`. Thus L *would imply* `U(D,n)<=(3D^(2/3-1/24))^n` for ALL D>=3,n>=1, with **K=3, delta=1/24**.

**Crucial noncircularity failure:** Since this same argument forces the absence of ANY counterexample above `M_n`, presenting L without an independent argument is not a substantive bridge; it is effectively another formulation of the desired D-power improvement. A true mechanism would have to derive L from independently verified local/multi-coordinate information on near-extremal A, not define its conclusion to match the goal. The elementary first-moment inequality in §2 cannot supply it for unrestricted n. For a threshold at the *old* 2/3 exponent, by contrast, fibre iteration can at most eliminate families at that old-exponent scale, not yield a fixed delta. Hence NO decision.

### 4. Falsification and quantification: do NOT confuse sparse examples with near-extremal refutations

To quantify nearness, define the exact alphabet exponent `alpha_D(A)=log(|A|)/(n log D)`, for any `|A|>=1`. This is NOT the as-yet-unproved optimal rate, just the observed exponent of an explicit family.

* **S001 balanced perfect-matching family**: for all D>=3, `A_D subset [D]^N`, `N=binom(2D,2)=D(2D-1)`, `|A_D|=2D`, every symbol occupies exactly 2 of the 2D words at each coordinate. This witnesses `p_*=1/D`; `alpha_D(A_D^t)=log_D(2D)/[D(2D-1)] -> 0` as D grows, for every product exponent t. Thus not a counterexample to L; it fails its density hypothesis for all sufficiently large D. Its n is on order D^2, comfortably above the elementary n >=~D/3 condition. Independent finite enumeration (D=3,4,5,6) verified the matching construction and all triples.
* **One-hot family** `H_m={0,e_1,...,e_m} subset {0,1}^m` for every m>=3, with `H_m^t` of size `(m+1)^t`, length mt, and `alpha_D=log_D(m+1)/m <=log_D(2)` since m+1<=2^m. Each coordinate has Bernoulli mass `1/(m+1)` on the rare 1. The (2,1) probability is `3m/(m+1)^2` per coordinate, becoming arbitrarily small as m grows; explicit distinct triples of products have b/n=3/m. The family is sparse, not a refutation of L, but kills all-family type-density claims.
* **Binary cubes and binary-block products**: `{0,1}^n` is sunflower-free with `|A|=2^n`; `alpha_D=log_D2 ->0` for growing D. All families using only TWO symbols in every coordinate have size <=2^n. Their restricted character space can collapse drastically; this is not evidence of uniform cancellation on near-extremal A.
* **D=3 six-word balanced S001 example**: n=3,m=6, all marginals 1/3, exactly sunflower-free. Its exponent is `log_3(6)/3=0.543643251...<2/3` and it does not form a varying-D counterexample.
* **Products of the above**: log-size and length add. Hence the rate of a coordinate-concatenation product is a length-weighted average of the block rates (same D) and cannot generate a growing-D rate near 2/3 from building blocks whose rates all tend to zero. A product may preserve marginal balance or rare type coordinates while still missing L's near-extremal hypothesis.

Numerical cross-checks: D=3 matching N=15,m=6, alpha=0.10872865; D=4 N=28,m=8, alpha=0.05357143; D=5 N=45,m=10, alpha=0.03179281; D=6 N=66,m=12, alpha=0.02101292. One-hot bad-type probabilities m=3:0.5625, m=5:0.4166667, m=10:0.2479339, m=20:0.1360544. These are diagnostics, NOT a proof beyond exact formulas.

For L specifically, at large D all cited constructions have `alpha_D <5/8` so cannot falsify the near-extremal hypothesis `|A| >= (2D^(5/8))^n`. No construction at the required size was found. Equally, no proof that such large sunflower-free sets cannot exist was found. Do not count a vacuous potential lemma as progress.

### 5. Balanced XY/YZ/ZX Fourier support — sharp monomial barrier and global-cancellation gap

Let `e(a,b,c)=1[a=b]+1[b=c]+1[c=a]-1` on the full D-ary cube and `T(x,y,z)=prod_{i=1}^n e(x_i,y_i,z_i)`. Let `n=3t`. Partition coordinates into blocks I_XY,I_YZ,I_ZX of t indices each. On each coordinate choose a nontrivial character chi, and respectively choose the Fourier mode `chi(x_i) conj(chi(y_i))`, `chi(y_i) conj(chi(z_i))`, `chi(z_i) conj(chi(x_i))`. Each chosen mode has coefficient exactly `1/D` in the FULL-CUBE Fourier expansion of e; the combined mode is UNIQUE as a full Fourier-frequency tuple because at a coordinate its pair of nontrivial supports identifies XY, YZ or ZX. Hence the product tensor has that full-cube Fourier coefficient exactly `D^(-n) !=0`. All THREE sides have exactly `2t=2n/3` nontrivial coordinate positions, with no side of support `<(2/3)n`. There are `binom(3t;t,t,t)(D-1)^(3t)` such full-cube modes as a family before restricting to A.

This is a rigorous falsification of an improved **termwise/pointwise character-support** bound. It is NOT a lower bound on slice rank of `T|A^3`: restricting Fourier characters to an arbitrary A can create linear dependencies and cancellations between large numbers of terms. No global estimate `D^(-epsilon n)` on the effective dimension of that restriction was established. Conversely, a cancellation observed on the binary cube does NOT scale to near-extremal A. This was precisely the missing quantitative bridge, not established in S002.

### 6. Prior art and scope

* Alon–Shpilka–Umans (2013) Theorem 2.6: only a D-independent base `b_3`, not a positive change of D exponent, implies classical 3-petal bound `c_3=e b_3`. Their Theorem 2.7 also makes the old 2/3 exponent already a weak `D^(1-epsilon)` phenomenon; don't misattribute this project.
* Naslund–Sawin (2017) Forum of Mathematics, Sigma 5 e15, **published Theorem 2**, primary PDF pp.4,8–9; arXiv 1606.09575v1 calls alphabet statement Theorem 5. Precisely matches the Fourier formula above.
* Ahmadi–Norouzi (2026) arXiv:2606.30593v1 Theorem 1.4: polynomial prefactor `O(n^(1/6)(3/2^(2/3))^n)` for `F subset 2^[n]`, NOT a D-uniform 2/3 exponent saving.
* Additional S002 discovery: Gabor Hegedus, *About sunflowers*, arXiv:1804.10050v2, primary PDF checked, Theorem 1.7 supplies a bound uniform in D but **factorial/superexponential in n**, `K(alpha)n! ((log log log n)^2/(alpha log log n))^n` (asymptotic n range, alpha>1); it is not `C^n`. Theorem 1.8 is a bound for k-uniform set systems with union-size dependency, built using Naslund–Sawin. These results cannot be repackaged as the desired uniform strict exponent saving.

Targeted source checks were performed on 2026-10-14, including the actual PDFs of ASU, NS, Hegedus, and Ahmadi–Norouzi abstract + accessible full text. This is **NOT worldwide priority clearance**. No claimed new results or publication entitlement.

### 7. Discrepancies, unresolved obligations and final action

1. **Mechanism obligation UNSATISFIED**: no independent proof of L, no quantitative restricted-character rank/cancellation theorem uniform D,n, and no near-extremal witness/refutation. The positive first-moment estimate has unavoidable n dependence and does not solve this.
2. **Density gap**: all explicit counterexamples are sparse at D^(2n/3) scale, so they invalidate unconditional lemmas only; L is unproved, NOT refuted.
3. **Fourier distinction**: nonzero balanced full-cube mode coefficient D^(-n) is a termwise obstruction, NOT a proof that restricted tensor cannot cancel; the sought D-exponent leverage remains absent.
4. **Prior art expanded**: Hegedus 2018 uniform-in-D factorial bound must be registered, but does not resolve a fixed-base or D-exponent improvement.
5. **Repository vs mathematics**: PR checks and push CI provide provenance/integrity only; they do not certify mathematical novelty or peer review. Parent main remains at its previous S005 state and must not be edited during this child session.

**Binary verdict NO**. Set child state **RETURN_PARENT_PAUSE_NO_D_EXPONENT_MECHANISM**, do not queue S003, stop here. Next requested action is owner-separate **SUN-PARENT-S006** portfolio judgment; do not secretly execute it. No theorem formalisation, Palomar, manuscript, arXiv, email, journal or outreach.
