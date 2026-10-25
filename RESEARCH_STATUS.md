# Research contributions — evidence and status

**Henryk Soboń** · Last reviewed: 24 October 2026

This ledger separates contributions merged into external repositories, maintainer-confirmed corrections, independently reviewed observations, and author-side results awaiting external verification. A merged PR is evidence that a *specific change* was accepted; it does not by itself establish a new mathematical theorem.

## Accepted contributions and corrections

| Record | Contribution | External evidence | Status |
| --- | --- | --- | --- |
| QEC-01 | CSS row-space intersection dimension diagnostic for the qLDPC Challenge verifier | [Author PR #2740](https://github.com/unitaryfoundation/qldpc-challenge/pull/2740) | **Merged, 4 Oct 2026.** Applied the established GF(2) rank identity as a tested verifier diagnostic. |
| QEC-02 | Exact-distance status transfer to five permutation-equivalent Campaign 4 records | [Author PR #11](https://github.com/qiskit-community/qcode-discovery/pull/11) · [issue #8](https://github.com/qiskit-community/qcode-discovery/issues/8) | **Merged, 23 Oct 2026.** Exact `[[288,12,12]]` reference; explicit permutations and replay verifier. 39 source records, 29 equivalence classes, five status transfers. |
| QEC-03 | Explicit qubit permutations for four duplicate-code clusters | [Author issue #2643](https://github.com/unitaryfoundation/qldpc-challenge/issues/2643) · [maintainer PR #2702](https://github.com/unitaryfoundation/qldpc-challenge/pull/2702) | **Maintainer correction merged, 3 Oct 2026.** Four mappings independently re-derived by the maintainer; duplicate entries removed. PR #2702 was written by the maintainer, not by me. |
| CHC-01 | Exact UNSAT certificates for two `demo/06` O0/O2 bit-vector CHC instances | [Author issue #1](https://github.com/aaronbembenek/binary-chc-problems/issues/1) | **Maintainer confirmed and benchmark results updated, 12 Oct 2026.** Scope is limited to those two exact benchmark files. |

## Independently examined, with important qualifications

| Record | Evidence | What it does—and does not—establish |
| --- | --- | --- |
| QEC-04 | [Campaign 4 decomposition report, issue #2942](https://github.com/unitaryfoundation/qldpc-challenge/issues/2942) | Maintainer independently reproduced the finding that ten of 39 records decompose. **The relevant verifier connectivity gates already existed upstream.** This is a useful dataset analysis, not a new verifier feature. Issue closed 17 Oct 2026. |
| QEC-05 | [Quantum-library reference package, PR #3362](https://github.com/unitaryfoundation/qldpc-challenge/pull/3362) | **Closed without merge, 13 Oct 2026.** Review identified overlap with existing upstream components and packaging problems. Not an accepted contribution. |

## Public submissions pending external adoption or certification

| Record | Evidence | Status / claim boundary |
| --- | --- | --- |
| SAT-01 | [SAT Competition issue #2](https://github.com/satcompetition/2026/issues/2) · [GBD PR #3](https://github.com/Udopia/gbd-data/pull/3) | **GBD PR open, checked 24 Oct 2026.** Author-side 400-variable assignment reports all 31,600 clauses satisfied. Proposed database change `unknown` → `sat` is not yet merged. |
| CHC-02 | [Eight quic3 benchmarks, CHC-COMP issue #11](https://github.com/chc-comp/chc-comp26-benchmarks/issues/11) | **Open, checked 24 Oct 2026.** Author reports validated SAT models for `standard_init2`–`standard_init9`, with corrupted-model controls. No organizer acceptance or updated official verdict is claimed. |
| CHC-03 | [O3 array benchmark, CHC-COMP issue #10](https://github.com/chc-comp/chc-comp26-benchmarks/issues/10) | **Open, checked 24 Oct 2026.** Author-side validation claim; external acceptance pending. |
| CHC-04 | [ADTRem/clam/goal71, CHC-COMP issue #9](https://github.com/chc-comp/chc-comp26-benchmarks/issues/9) | **Open, checked 24 Oct 2026.** Author-side model; external acceptance pending. |
| CHC-05 | [Two VMT/CHC array cases, issue #1](https://github.com/chc-comp/vmt-chc-benchmarks/issues/1) | **Open, checked 24 Oct 2026.** Author-side models; external acceptance pending. |
| SYNT-01 | [Parity-realizability witness record](https://github.com/henryksobon300-code/my-work-henryk-sobon/issues/1) | Author-side replayable environment counterstrategy for `steadygame_pb_12_pe_`; no official SYNTCOMP certificate or competition ranking claimed. |

## Experimental research — not externally certified

**MathemaSpace** is an ongoing research program with separate experimental branches. Internal architecture and unreleased implementations are not disclosed here. Experimental results require original code versions, frozen inputs, baselines, negative controls, independent replay and an explicit novelty/literature review before broader scientific claims can be made.

The MathemaSpace research engine and implementation remain in a private repository. Their code is not distributed through this public site, and no institutional certification or general AI claim is made here.

## Documentation principles

- Link to primary source records and distinguish **my PRs** from **maintainer PRs prompted by my issues**.
- Preserve unsuccessful reviews, counterexamples, scope limits and pending verification.
- Separate computational verification of a concrete instance from proof of an unlimited general claim.
- Do not publish private engines, research correspondence or patent-sensitive material in this public repository.
- Dates and statuses are a checked snapshot, not continuously updated claims.

Contact and source contributions are available through [my GitHub profile](https://github.com/henryksobon300-code).
