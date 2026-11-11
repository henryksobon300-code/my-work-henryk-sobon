# Research publication and evidence status

**Henryk Soboń · Public-facing inventory · originally reviewed 31 October 2026; selected GitHub additions checked 11 November 2026**

[Home](../README.md) · [Research website](https://henryksobon300-code.github.io/my-work-henryk-sobon/) · [Browse results](https://henryksobon300-code.github.io/my-work-henryk-sobon/projects.html) · [Public PR and issue index](RESULTS_INDEX.md) · [Experimental work](EXPERIMENTAL_RESEARCH_INDEX.md) · [External review](EXTERNAL_REVIEW.md)

## How to interpret this record

This inventory distinguishes **accepted external contributions** from **maintainer-confirmed findings**, **publicly inspectable author-side evidence**, and **research records whose reproducible package is not yet published here**. It is a research archive, **not** a list of established discoveries of worldwide novelty. A recorded verification claim is not a fresh independent replay by the website editor. "Merged" refers to a particular code change, not independent confirmation of a new theorem.

**PUBLIC CODE/PACKAGE AVAILABLE** means the linked artifact can be downloaded from this repository. **DOCUMENTED / PACKAGE NOT YET HOSTED** means the source report or experiment exists in the project archive but its original replay package is not accessible on this public site. Such records are presented as publication work in progress, never as independently certified results. No original private correspondence, engines, patents, or restricted research packages are hosted here.

## Externally accepted contributions and corrections

| ID | Result | Public record | Independent status |
| --- | --- | --- | --- |
| EXT-01 | CSS GF(2) row-space intersection diagnostic | [qLDPC PR #2740](https://github.com/unitaryfoundation/qldpc-challenge/pull/2740) · [case study](CASE_QEC_INTERSECTION.md) | **Merged**, 4 Oct 2026; known identity integrated with tests. |
| EXT-02 | Exact-distance metadata transferred for five permutation-equivalent Campaign 4 codes | [qcode-discovery PR #11](https://github.com/qiskit-community/qcode-discovery/pull/11) · [case study](CASE_QCODE_CAMPAIGN4.md) | **Merged**, 23 Oct 2026; not five newly discovered codes. |
| EXT-03 | Four duplicate qLDPC code clusters | [Issue #2643](https://github.com/unitaryfoundation/qldpc-challenge/issues/2643) · [maintainer PR #2702](https://github.com/unitaryfoundation/qldpc-challenge/pull/2702) | Independently checked; maintainer removed four redundant records. |
| EXT-04 | Two binary CHC UNSAT benchmark corrections | [Original issue](https://github.com/aaronbembenek/binary-chc-problems/issues/1) | Maintainer confirmed and changed the expected results. |

Other substantive public outcomes are indexed in [RESULTS_INDEX.md](RESULTS_INDEX.md). Do not double-count an issue and the PR that resolves the same work.

## Publicly hosted technical artifacts

| ID | Result | Files / source | Boundary |
| --- | --- | --- | --- |
| PUB-01 | Proposed exact-distance certificate for CSS code `[[1000,406,6]]` | [Proof](qldpc-1000-406-d6/PROOF.md) · [public verifier ZIP](../MathemaSpace_D6_PUBLIC.zip) · [original code PR #3863](https://github.com/unitaryfoundation/qldpc-challenge/pull/3863) | Source construction and weight-six witnesses belong to @hirobumii; the exact-distance proof by Henryk Soboń was independently verified by the code author and formalized in Lean; the [formal certificate, PR #4226](https://github.com/unitaryfoundation/qldpc-challenge/pull/4226), was merged on 30 October 2026. The original code and the certificate PR are authored by @hirobumii, not Soboń. |
| PUB-02 | SciPy graph-Laplacian integer overflow correction | [Public patch](scipy-26549/laplacian_dtype_promotion.patch) · [SciPy issue #26549](https://github.com/scipy/scipy/issues/26549) | Author-side tests; patch has **not** been shown accepted upstream or through full official CI. |
| PUB-03 | Positive determinants in 26 proposed BLR families (`j=3..28`, `k≥j`) | [Proof drafts, scripts, certificates](blr-positivity-26-families/) | Author-side arguments and checks, **not independently peer-reviewed**. Not a full conjecture or Riemann-hypothesis proof. |
| PUB-04 | Eight quic3 SAT model reports and controls | [Public CHC-COMP package](chc_comp_issue11/README.md) · [original issue](https://github.com/chc-comp/chc-comp26-benchmarks/issues/11) | Awaiting external benchmark acceptance. |
| PUB-05 | SYNTCOMP bounded parity witness record | [Public record](SYNTCOMP_2026_PARITY_PUBLIC_CONTRIBUTION_RECORD.md) · [original issue](https://github.com/henryksobon300-code/my-work-henryk-sobon/issues/1) | Author-side and native-verifier checks; no official competition ranking. |
| PUB-SAT | `vdwb_k6_n400`: reported witness for one CNF previously marked UNKNOWN | [Original public assignment and verifier](https://github.com/satcompetition/2026/issues/2) · [case study](CASE_SAT_VDWB_K6_N400.md) · [GBD PR #3](https://github.com/Udopia/gbd-data/pull/3) | **Public author-side evidence; GBD PR closed without merge on 11 Nov 2026**. No independent upstream SAT verdict adoption recorded. |
| PUB-06 | Two existing n=180 CSS entries: proposed `d_X=d_Z=d=14` | [Author PR #5336](https://github.com/unitaryfoundation/qldpc-challenge/pull/5336) · [public replay, third-party solvers and proposed certificates](https://github.com/unitaryfoundation/qldpc-challenge/pull/5336/files) | **Draft, not accepted (checked 11 Nov 2026).** Both public third-party programs `exactA` and `exactB` returned completed searches for X/Z of both entries, 8/8 runs; proposed `solver`-level certificates, not formal proofs. GitHub CI passed; maintainer approval and official exact status remain pending. No original private research engine is submitted. |

## Research records awaiting full public replay packages

The rows below record specific **reported** findings recovered from project summaries and research correspondence. Their existence in the archive does **not** establish that all code, original matrices, negative controls, hashes, or official reviewer acknowledgements have been audited for public release. In particular, **no email attachment is silently treated as a published GitHub artifact**.

| ID | Date (2026) | Recorded result | Public evidence state and necessary next check |
| --- | --- | --- | --- |
| QUEUE-01 | 29 Oct | New quantum CSS candidate `[[980,398,6]]`: report compares 19,110 vs 20,027 minimum-weight Pauli operators and gives a model-specific 3.869% reduction in an idealized ML error coefficient. | **PACKAGE NOT YET HOSTED.** Public-designated archive and notebook exist in project records. Need fresh replay of matrices, ranks, commutation, distance and both counters before a proof/benchmark claim is published here. No general decoder or hardware-performance claim. |
| QUEUE-02 | 17 Oct | For the previously known 684-qubit code `684-6-77`, a reported explicit witness tightens the upper bound from 77 to **`d≤72`**. | **PACKAGE NOT YET HOSTED.** A public-designated witness/reproducer was prepared; its exact source matrix and certificate must be checked before publication. This is an upper bound, not proof that `d=72`. Credit the original code constructor. |
| QUEUE-03 | 27 Oct | Two reported quantum-code upper-bound witnesses: `[[360,10]]` **`d≤16`** (from 22) and `[[180,6]]` **`d≤14`** (from 20). | **PACKAGE NOT YET HOSTED.** Public-math-only notebook and checker reportedly prepared. Check fixed input identity and decode witnesses; neither is an exact-distance claim. |
| QUEUE-04 | 23 Oct | Array-Generator rejects a valid interaction-test set when `t=k`; reported four configurations cover all six interaction-fault pairs. | **PACKAGE NOT YET HOSTED.** Public bug-report bundle includes a reproducer, checker and a proposed fix; upstream review or acceptance has not been established. |
| QUEUE-05 | 30 Oct | NetworkX graph-case adapter: 16,984 local checks reported, including an independent enumerating checker on the main case. | **EXPERIMENTAL NOTE, NO PUBLIC PACKAGE.** One notebook was archived; no claim of a merged NetworkX patch. Historical V12–V14 were not run in that experiment. |
| QUEUE-06 | 22 Oct | Baum–Sweet / [TheoremDB P2422](https://theoremdb.org/statements/P2422/) finite Hankel nonvanishing computations for orders 1–30,000 in two prime fields. | **DOCUMENTED, FULL PACKAGE NOT HOSTED.** Source archive reports two computational approaches. Not a proof of the infinite statement, and originality remains unconfirmed. |
| QUEUE-07 | 22 Oct | Two reported quantum-code data equivalences: `10-2-3 ≃ 10-2-3-b`; `12-2-4 ≃ 12-2-4-b`. | **DOCUMENTED, FULL CERTIFICATES NOT HOSTED.** Public-designated GF(2) row-space/permutation checkers were prepared. Not new codes; independent upstream adoption unknown. |
| QUEUE-08 | 27 Oct | Extension of the proposed BLR determinant argument from `j=3..28` to `j=3..40` for `k≥j`. | **EXTENSION NOT PUBLISHED HERE.** Only the earlier `j=3..28` public package is hosted. Separate public-only extraction, analytic review and novelty review needed; do not silently upgrade the earlier claim. |
| QUEUE-09 | 15 Oct | qLDPC helper-function counterexample on two 12-qubit CSS codes: same helper classification but distinct reported X/Z intersection dimensions 1 and 2. | **PACKAGE NOT YET HOSTED.** Check exact function/version and negative controls before publicly identifying a software defect. Not a demonstrated failure of the complete qLDPC submission verifier. |
| QUEUE-10 | 15 Oct | toqito SDP formulation / test expectation investigation, including a numerical model reduction and an exact test-value counterexample. | **PACKAGE NOT YET HOSTED.** Check comparison with optimized baseline, solver warnings and upstream reproduction. Some historical runs terminated at a time limit; no generic speedup claim. |
| QUEUE-11 | 17 Oct | qLDPC Challenge #3427 prototype: 32/32 controlled trials; six transformed 144-qubit code variants mapped by a new adapter. | **AUTHOR-SIDE EXPERIMENT, NO PUBLIC PACKAGE.** Check frozen data and baseline; not proof that the general challenge has been solved. |
| QUEUE-12 | 26 Oct | GF(2) / bivariate-bicycle symbolic family observation: reported weight `4r` versus baseline `4r+2` in specified cases `r≥5`. | **PRIVATE-ARCHIVE CANDIDATE.** No worldwide priority, global optimality or exact quantum-code distance established. Do not publish implementation or private research history. |

## Requirements for publishing further evidence

A queued item can be reclassified as **publicly reproducible** only after the published record has a specific frozen source/commit/dataset, an exact and limited claim, a shareable public artifact with its own content hash, a replay command and verification output, appropriate negative tests and baselines, attribution, and a precise statement about independent review. A code witness for an **upper** bound must not be labeled an **exact** distance without a separately proved lower bound.

**Current audit boundary:** Public GitHub inventory plus identified archive notes through 31 October 2026. This is an expanded inventory, **not an exhaustive replay of every historic mailbox attachment or notebook**. Items in the queue are not presented as peer-reviewed publications or as independently confirmed novel discoveries.
