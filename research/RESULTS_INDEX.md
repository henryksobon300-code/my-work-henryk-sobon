# Research results index

**Henryk Soboń — public research portfolio**  
**Catalogue updated:** 31 October 2026 (issue/PR inventory last fully reviewed 24 October 2026) · [Website home](https://henryksobon300-code.github.io/my-work-henryk-sobon/) · [Browse results on the website](https://henryksobon300-code.github.io/my-work-henryk-sobon/projects.html) · [Evidence/status ledger](../RESEARCH_STATUS.md) · [Publication status / unhosted packages](PUBLICATION_STATUS.md)

This is a **curated index of substantive public results and review requests**, not a catalogue of every unsuccessful or redundant experiment. A public issue is not a journal article or an official benchmark certificate. The original GitHub projects retain their own public histories; private email correspondence is not reproduced here.

## Merged author pull requests (2)

| ID | Scope | Evidence | Result |
| --- | --- | --- | --- |
| A01 | qLDPC verifier: GF(2) CSS row-space intersection diagnostic | [My PR #2740](https://github.com/unitaryfoundation/qldpc-challenge/pull/2740) · [review](https://github.com/unitaryfoundation/qldpc-challenge/pull/2740#pullrequestreview-5405628122) · [case study](CASE_QEC_INTERSECTION.md) | **Merged 4 Oct 2026.** Applied known identity with tests. |
| A02 | Campaign 4: 5 exact-distance status transfers for permutation-equivalent CSS codes | [My PR #11](https://github.com/qiskit-community/qcode-discovery/pull/11) · [reviewer confirmation](https://github.com/qiskit-community/qcode-discovery/pull/11#issuecomment-6368684584) · [case study](CASE_QCODE_CAMPAIGN4.md) | **Merged 23 Oct 2026.** Independent review and merge. |

## Confirmed findings that led to maintainer changes (2 distinct issues)

| ID | Scope | Evidence | Result |
| --- | --- | --- | --- |
| B01 | 4 previously unresolved quantum code equivalence clusters | [My issue #2643](https://github.com/unitaryfoundation/qldpc-challenge/issues/2643) · [maintainer's PR #2702](https://github.com/unitaryfoundation/qldpc-challenge/pull/2702) · [case study](CASE_QEC_FOUR_CLUSTERS.md) | **Issue completed / maintainer PR merged 3 Oct 2026.** The PR is the maintainer's work, not mine. |
| B02 | 2 bit-vector CHC demo/06 instances O0/O2 have UNSAT certificates | [My issue #1](https://github.com/aaronbembenek/binary-chc-problems/issues/1) · [original public issue and evidence](https://github.com/aaronbembenek/binary-chc-problems/issues/1) | **Completed 12 Oct 2026.** Maintainer confirmed verdicts and corrected expected results. |

## Pending public submissions awaiting third-party acceptance or official validation (6 issues, 1 PR)

| ID | Scope | Evidence | Latest checked status |
| --- | --- | --- | --- |
| D01 | SAT benchmark `vdwb_k6_n400`: explicit satisfying assignment and proposed dataset status correction | [SAT Competition issue #2](https://github.com/satcompetition/2026/issues/2) · [GBD PR #3](https://github.com/Udopia/gbd-data/pull/3) | **Both open.** Assignment reported as satisfying 31,600/31,600 clauses; dataset change not merged. |
| D02 | CHC-COMP: 8 quic3 `standard_init2`–`standard_init9` models | [Benchmark issue #11](https://github.com/chc-comp/chc-comp26-benchmarks/issues/11) · [public models and standalone generator](chc_comp_issue11/README.md) | **Open (31 Oct review).** Author-side validation, corrupted controls, frozen model ZIP and [reproducer instructions](chc_comp_issue11/README.md) supplied; current-2026 validator nontermination needs independent resolution. 2026 metadata already contains `true` placeholders; not official independent model acceptance. |
| D03 | CHC-COMP: `O3_sum_array` model | [Benchmark issue #10](https://github.com/chc-comp/chc-comp26-benchmarks/issues/10) | **Open.** Awaiting third-party confirmation. |
| D04 | CHC-COMP: `goal71` model | [Benchmark issue #9](https://github.com/chc-comp/chc-comp26-benchmarks/issues/9) | **Open.** Awaiting third-party confirmation. |
| D05 | VMT/CHC: two array initialization models | [Benchmark issue #1](https://github.com/chc-comp/vmt-chc-benchmarks/issues/1) | **Open.** Awaiting third-party confirmation. |
| D06 | SYNTCOMP parity-game witness and five-instance provenance | [Own issue #1](https://github.com/henryksobon300-code/my-work-henryk-sobon/issues/1) · [author-side research record](SYNTCOMP_2026_PARITY_PUBLIC_CONTRIBUTION_RECORD.md) | **Open (author archive).** No competition certification or ranking established. |

## Other computational projects and research threads

These are **not automatically included in the merged-contribution count**. A more precise, version-separated catalogue is at [Experimental research — evidence register](EXPERIMENTAL_RESEARCH_INDEX.md).

| Research thread | Public status and limits |
| --- | --- |
| **CSS code `[[1000,406,6]]` distance certificate** | [Public proof argument](qldpc-1000-406-d6/PROOF.md) · [verifier archive](../MathemaSpace_D6_PUBLIC.zip) · [original author PR #3863](https://github.com/unitaryfoundation/qldpc-challenge/pull/3863). Original code and weight-six witnesses belong to @hirobumii; Henryk Soboń's additional proof was independently checked by the original code author, formalized in Lean and accepted as a [formal distance-6 certificate in merged PR #4226](https://github.com/unitaryfoundation/qldpc-challenge/pull/4226) on 30 Oct 2026. The formal certificate PR was authored by @hirobumii, not Soboń. |
| **SciPy graph Laplacian integer overflow** | [Original issue #26549](https://github.com/scipy/scipy/issues/26549) · [proposed patch](scipy-26549/laplacian_dtype_promotion.patch). Local test evidence is reported; upstream acceptance/full CI are not claimed. |
| **BLR determinant positivity: 26 proposed infinite families** | [Public arguments, scripts and finite certificates](blr-positivity-26-families/). Proposed partial result requires independent mathematical review; not a proof of the full conjecture. |
| New CSS code equivalence pairs `10-2-3 / 10-2-3-b` and `12-2-4 / 12-2-4-b` | Reported author-side certificate package (22 Oct 2026); **not yet incorporated in external repository**. Private source and current public-package review should remain separate. |
| Baum–Sweet / TheoremDB P2422 Hankel calculation | Reported finite modular non-vanishing checks for orders 1–30,000 in two fields. **Not a proof for all orders; novelty and literature priority unconfirmed.** Do not call this problem solved. |

### Recorded material not yet hosted with full public replay files

The [publication and evidence-status register](PUBLICATION_STATUS.md) tracks **12 additional research records** and the checks required to release or verify them. This is a separate queue, not twelve accepted new discoveries. It includes the `[[980,398,6]]` candidate, an upper-bound witness `d≤72` for the existing 684-qubit code, two further upper-bound witnesses for `[[360,10]]` and `[[180,6]]`, Array-Generator and NetworkX cases, and an unreviewed BLR range extension. Other mathematical and software experiments are listed with their precise limitations.

Their source correspondence and local notebooks are **not equivalent to public GitHub proof packages**. No independent replay or acceptance is implied; private engine code remains unhosted.

## External review and correspondence

A [public review summary](EXTERNAL_REVIEW.md) records **public** review milestones and category-level private feedback. For mail-only discussions, personal messages, attachments and quotations are kept out of the public repository. A private internal source inventory should retain message dates, links and validation notes.

## What each result's dedicated page should contain

1. Clear claim and exact problem/data version.
2. Original author contribution, and separately the maintainer's implementation.
3. Proof or witness, replay/checker and negative controls where applicable.
4. Independent validation with a direct **public** link or an explicitly private unquoted record.
5. Scope limits, known counterexamples, retractions and unresolved questions.
6. Status history and next required evidence.

An issue's **closed** badge alone must never be interpreted as peer-reviewed publication, acceptance of a proposed fix, or a citation count.
