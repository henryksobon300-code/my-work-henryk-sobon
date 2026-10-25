# Research results index

**Henryk Soboń — public research portfolio**  
**Snapshot:** 25 October 2026 · [Website home](https://henryksobon300-code.github.io/my-work-henryk-sobon/) · [Browse results on the website](https://henryksobon300-code.github.io/my-work-henryk-sobon/projects.html) · [Evidence/status ledger](../RESEARCH_STATUS.md)

This is the **comprehensive index of identified public GitHub submissions**. It is deliberately not a ranking of scientific merit. In particular, **closed** does not always mean accepted, and a published GitHub issue is not a journal article or an official benchmark certificate. External review from private email is not reproduced here.

## A. Merged author pull requests (2)

| ID | Scope | Evidence | Result |
| --- | --- | --- | --- |
| A01 | qLDPC verifier: GF(2) CSS row-space intersection diagnostic | [My PR #2740](https://github.com/unitaryfoundation/qldpc-challenge/pull/2740) · [review](https://github.com/unitaryfoundation/qldpc-challenge/pull/2740#pullrequestreview-5405628122) · [case study](CASE_QEC_INTERSECTION.md) | **Merged 4 Oct 2026.** Applied known identity with tests. |
| A02 | Campaign 4: 5 exact-distance status transfers for permutation-equivalent CSS codes | [My PR #11](https://github.com/qiskit-community/qcode-discovery/pull/11) · [reviewer confirmation](https://github.com/qiskit-community/qcode-discovery/pull/11#issuecomment-6368684584) · [case study](CASE_QCODE_CAMPAIGN4.md) | **Merged 23 Oct 2026.** Independent review and merge. |

## B. Confirmed findings that led to maintainer changes (2 distinct issues)

| ID | Scope | Evidence | Result |
| --- | --- | --- | --- |
| B01 | 4 previously unresolved quantum code equivalence clusters | [My issue #2643](https://github.com/unitaryfoundation/qldpc-challenge/issues/2643) · [maintainer's PR #2702](https://github.com/unitaryfoundation/qldpc-challenge/pull/2702) · [case study](CASE_QEC_FOUR_CLUSTERS.md) | **Issue completed / maintainer PR merged 3 Oct 2026.** The PR is the maintainer's work, not mine. |
| B02 | 2 bit-vector CHC demo/06 instances O0/O2 have UNSAT certificates | [My issue #1](https://github.com/aaronbembenek/binary-chc-problems/issues/1) · [original public issue and evidence](https://github.com/aaronbembenek/binary-chc-problems/issues/1) | **Completed 12 Oct 2026.** Maintainer confirmed verdicts and corrected expected results. |

## C. Externally reproduced observational result, with scope restriction (1 issue)

| ID | Scope | Evidence | Result |
| --- | --- | --- | --- |
| C01 | Campaign 4: 10 reducible CSS bivariate-bicycle records in a 39-record set | [My issue #2942](https://github.com/unitaryfoundation/qldpc-challenge/issues/2942) | **Closed 17 Oct 2026.** Maintainer independently rebuilt and reproduced exactly 10 records. **Connectivity checks already existed in the upstream verifier**; not a new merged feature or a newly established exact distance. |

## D. Public submissions awaiting third-party acceptance or official validation (6 issues, 1 PR)

| ID | Scope | Evidence | Latest checked status |
| --- | --- | --- | --- |
| D01 | SAT benchmark `vdwb_k6_n400`: explicit satisfying assignment and proposed dataset status correction | [SAT Competition issue #2](https://github.com/satcompetition/2026/issues/2) · [GBD PR #3](https://github.com/Udopia/gbd-data/pull/3) | **Both open.** Assignment reported as satisfying 31,600/31,600 clauses; dataset change not merged. |
| D02 | CHC-COMP: 8 quic3 `standard_init2`–`standard_init9` models | [Benchmark issue #11](https://github.com/chc-comp/chc-comp26-benchmarks/issues/11) · [public models and standalone generator](chc_comp_issue11/README.md) | **Open.** Author-side validation, deliberately corrupted controls, source hashes and a public reproducer; not an official validated verdict. |
| D03 | CHC-COMP: `O3_sum_array` model | [Benchmark issue #10](https://github.com/chc-comp/chc-comp26-benchmarks/issues/10) | **Open.** Awaiting third-party confirmation. |
| D04 | CHC-COMP: `goal71` model | [Benchmark issue #9](https://github.com/chc-comp/chc-comp26-benchmarks/issues/9) | **Open.** Awaiting third-party confirmation. |
| D05 | VMT/CHC: two array initialization models | [Benchmark issue #1](https://github.com/chc-comp/vmt-chc-benchmarks/issues/1) | **Open.** Awaiting third-party confirmation. |
| D06 | SYNTCOMP parity-game witness and five-instance provenance | [Own issue #1](https://github.com/henryksobon300-code/my-work-henryk-sobon/issues/1) · [author-side research record](SYNTCOMP_2026_PARITY_PUBLIC_CONTRIBUTION_RECORD.md) | **Open (author archive).** No competition certification or ranking established. |

## E. Closed or withdrawn submissions not to count as accepted results

| ID | Evidence | Significance |
| --- | --- | --- |
| E01 | [qLDPC Challenge PR #3362](https://github.com/unitaryfoundation/qldpc-challenge/pull/3362) | **Closed without merge.** Maintainer identified overlap with existing functionality and packaging problems; retained as an internal lesson, not advertised as an accepted contribution. |
| E02 | [SAT Competition issue #3](https://github.com/satcompetition/2026/issues/3) | **Closed 24 Oct 2026.** Off-topic duplicate of the four-cluster quantum-code report; original supported result remains B01. Not a separate discovery. |
| E03 | [qcode-discovery issue #8](https://github.com/qiskit-community/qcode-discovery/issues/8) | **Closed 23 Oct 2026 after PR #11.** This is the original issue for A02; not a third result. |

**Inventory checksum:** 11 authored public issues (5 closed, 6 open), plus 4 authored PRs (2 merged, 1 open, 1 closed without merge), reviewed as of 24 Oct 2026. Parent projects may contain separate maintainer PRs that are not additional authored PRs.

## F. Other computational projects and research threads

These are **not automatically included in the merged-contribution count**. A more precise, version-separated catalogue is at [Experimental research — evidence register](EXPERIMENTAL_RESEARCH_INDEX.md).

| Research thread | Public status and limits |
| --- | --- |
| MathemaSpace research prototypes | Research code is maintained privately. Public descriptions here document only selected findings, with no claim of outside certification or a general-purpose system. |
| New CSS code equivalence pairs `10-2-3 / 10-2-3-b` and `12-2-4 / 12-2-4-b` | Reported author-side certificate package (22 Oct 2026); **not yet incorporated in external repository**. Private source and current public-package review should remain separate. |
| Baum–Sweet / TheoremDB P2422 Hankel calculation | Reported finite modular non-vanishing checks for orders 1–30,000 in two fields. **Not a proof for all orders; novelty and literature priority unconfirmed.** Do not call this problem solved. |
| MathemaSpace V18 / HAAL resetless state diagnosis | Reported responses for 71 public models. External technical feedback exposed flaws in the nonadaptive comparison and opportunities for belief-graph pruning; **not evidence of state-of-the-art superiority**. |
| Program Bridge / finite transition-system equivalence | Exhaustive finite-state certificates for specified test families; **not an EquiBench result** under its category semantics. |
| Rotor / stateful dynamic graph primitive | Patent-sensitive research and prototypes. The existence of correspondence or an application does not establish patentability, working hardware or independent novelty confirmation. **Keep technical private methods out of public GitHub** pending IP review. |
| Other historical experimental branches | Separately indexed in nonpublic research archives; no shared blanket performance or novelty claim. |

## G. External review and correspondence

A [public review summary](EXTERNAL_REVIEW.md) records **public** review milestones and category-level private feedback. For mail-only discussions, personal messages, attachments and quotations are kept out of the public repository. A private internal source inventory should retain message dates, links and validation notes.

## H. What each result's dedicated page should contain

1. Clear claim and exact problem/data version.
2. Original author contribution, and separately the maintainer's implementation.
3. Proof or witness, replay/checker and negative controls where applicable.
4. Independent validation with a direct **public** link or an explicitly private unquoted record.
5. Scope limits, known counterexamples, retractions and unresolved questions.
6. Status history and next required evidence.

An issue's **closed** badge alone must never be interpreted as peer-reviewed publication, acceptance of a proposed fix, or a citation count.
