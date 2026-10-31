# Research contributions — evidence and status

**Henryk Soboń** · Last reviewed: 24 October 2026

For the expanded inventory of research experiments and pending full public proof packages, see the [publication-status register](research/PUBLICATION_STATUS.md). A recorded test or draft does not upgrade its prior independent-review status.

This ledger separates contributions merged into external repositories, maintainer-confirmed corrections and author-side results awaiting external verification. A merged PR is evidence that a *specific change* was accepted; it does not by itself establish a new mathematical theorem.

## Accepted contributions and corrections

| Record | Contribution | External evidence | Status |
| --- | --- | --- | --- |
| QEC-01 | CSS row-space intersection dimension diagnostic for the qLDPC Challenge verifier | [Author PR #2740](https://github.com/unitaryfoundation/qldpc-challenge/pull/2740) | **Merged, 4 Oct 2026.** Applied the established GF(2) rank identity as a tested verifier diagnostic. |
| QEC-02 | Exact-distance status transfer to five permutation-equivalent Campaign 4 records | [Author PR #11](https://github.com/qiskit-community/qcode-discovery/pull/11) · [issue #8](https://github.com/qiskit-community/qcode-discovery/issues/8) | **Merged, 23 Oct 2026.** Exact `[[288,12,12]]` reference; explicit permutations and replay verifier. 39 source records, 29 equivalence classes, five status transfers. |
| QEC-03 | Explicit qubit permutations for four duplicate-code clusters | [Author issue #2643](https://github.com/unitaryfoundation/qldpc-challenge/issues/2643) · [maintainer PR #2702](https://github.com/unitaryfoundation/qldpc-challenge/pull/2702) | **Maintainer correction merged, 3 Oct 2026.** Four mappings independently re-derived by the maintainer; duplicate entries removed. PR #2702 was written by the maintainer, not by me. |
| CHC-01 | Exact UNSAT certificates for two `demo/06` O0/O2 bit-vector CHC instances | [Author issue #1](https://github.com/aaronbembenek/binary-chc-problems/issues/1) | **Maintainer confirmed and benchmark results updated, 12 Oct 2026.** Scope is limited to those two exact benchmark files. |

## Public submissions pending external adoption or certification

| Record | Evidence | Status / claim boundary |
| --- | --- | --- |
| SAT-01 | [SAT Competition issue #2](https://github.com/satcompetition/2026/issues/2) · [GBD PR #3](https://github.com/Udopia/gbd-data/pull/3) | **GBD PR open, checked 24 Oct 2026.** Author-side 400-variable assignment reports all 31,600 clauses satisfied. Proposed database change `unknown` → `sat` is not yet merged. |
| CHC-02 | [Eight quic3 benchmarks, CHC-COMP issue #11](https://github.com/chc-comp/chc-comp26-benchmarks/issues/11) | **Open, checked 31 Oct 2026.** Public model ZIP, exact generator, hashes and 8/8 author-side checks are linked in [issue #11 reproduction guide](research/chc_comp_issue11/README.md). Current-organizer validator previously failed to return a result in the reviewer’s time window; no exact reproduction command was provided. The 2026 YAML files already say `expected_verdict: true` only as auto-added placeholders, whereas the 2025 metadata lacks the verdict. No official model replay or final correction is claimed. |
| CHC-03 | [O3 array benchmark, CHC-COMP issue #10](https://github.com/chc-comp/chc-comp26-benchmarks/issues/10) | **Open, checked 24 Oct 2026.** Author-side validation claim; external acceptance pending. |
| CHC-04 | [ADTRem/clam/goal71, CHC-COMP issue #9](https://github.com/chc-comp/chc-comp26-benchmarks/issues/9) | **Open, checked 24 Oct 2026.** Author-side model; external acceptance pending. |
| CHC-05 | [Two VMT/CHC array cases, issue #1](https://github.com/chc-comp/vmt-chc-benchmarks/issues/1) | **Open, checked 24 Oct 2026.** Author-side models; external acceptance pending. |
| SYNT-01 | [Parity-realizability witness record](https://github.com/henryksobon300-code/my-work-henryk-sobon/issues/1) | Author-side replayable environment counterstrategy for `steadygame_pb_12_pe_`; no official SYNTCOMP certificate or competition ranking claimed. |

## Additional public research records — individual verification states

These records have publicly accessible technical artifacts with different levels of outside adoption. A formal-certificate PR by the original code author credits the separate proof by Soboń; it is not an additional PR authored or merged by Soboń.

| Record | Public evidence | Claim boundary and next check |
| --- | --- | --- |
| QEC-06 | [`[[1000,406,6]]` proof argument](research/qldpc-1000-406-d6/PROOF.md) · [public verifier archive](MathemaSpace_D6_PUBLIC.zip) · [source code PR #3863](https://github.com/unitaryfoundation/qldpc-challenge/pull/3863) | A lower-bound certificate is proposed for a code due to @hirobumii. The original code author independently verified Henryk Soboń's distance-6 proof and formalized it in Lean. The [formal-tier certificate was merged in PR #4226](https://github.com/unitaryfoundation/qldpc-challenge/pull/4226) on 30 Oct 2026. Do not attribute the code construction or PR authorship to Soboń. |
| SCIPY-01 | [Issue #26549](https://github.com/scipy/scipy/issues/26549) · [public patch](research/scipy-26549/laplacian_dtype_promotion.patch) | Author-side local regression tests reported. No full upstream SciPy CI or maintainer acceptance demonstrated here. |
| MATH-01 | [BLR 26-family proof/certificate package](research/blr-positivity-26-families/) | An all-`k` partial-positivity argument is proposed for `j=3,…,28`; checks and scripts are public, but a mathematical review and prior-work comparison are needed. Not a proof of the full positivity conjecture. |

External statuses for the first section were reviewed on 24 October 2026. Adding this section on 31 October does not retrospectively recertify those submissions.

## Documentation principles

- Link to primary source records and distinguish **my PRs** from **maintainer PRs prompted by my issues**.
- Preserve unsuccessful reviews, counterexamples, scope limits and pending verification.
- Separate computational verification of a concrete instance from proof of an unlimited general claim.
- Do not publish private engines, research correspondence or patent-sensitive material in this public repository.
- Dates and statuses are a checked snapshot, not continuously updated claims.

Contact and source contributions are available through [my GitHub profile](https://github.com/henryksobon300-code).
