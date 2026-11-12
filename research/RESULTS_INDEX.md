# Research results index

**Henryk Soboń — public research portfolio**  
**Catalogue updated:** 11 November 2026 (new qLDPC PR and selected issue/PR statuses rechecked; broader issue inventory last fully reviewed 24 October 2026) · [Website home](https://henryksobon300-code.github.io/my-work-henryk-sobon/) · [Browse results on the website](https://henryksobon300-code.github.io/my-work-henryk-sobon/projects.html) · [Evidence/status ledger](../RESEARCH_STATUS.md) · [Publication status / unhosted packages](PUBLICATION_STATUS.md)

**Documentation quality standard:** [Evidence, attribution, review scope and publication checklist](PORTFOLIO_REVIEW_STANDARD.md).

This is a **curated index of substantive public results and review requests**, not a catalogue of every unsuccessful or redundant experiment. A public issue is not a journal article or an official benchmark certificate. The original GitHub projects retain their own public histories; private email correspondence is not reproduced here.

## Merged author pull requests (2)

| ID | Scope | Evidence | Result |
| --- | --- | --- | --- |
| A01 | qLDPC verifier: GF(2) CSS row-space intersection diagnostic | [My PR #2740](https://github.com/unitaryfoundation/qldpc-challenge/pull/2740) · [review](https://github.com/unitaryfoundation/qldpc-challenge/pull/2740#pullrequestreview-5405628122) · [case study](CASE_QEC_INTERSECTION.md) | **Merged 4 Oct 2026.** Applied known identity with tests. |
| A02 | Campaign 4: 5 exact-distance status transfers for permutation-equivalent CSS codes | [My PR #11](https://github.com/qiskit-community/qcode-discovery/pull/11) · [reviewer confirmation](https://github.com/qiskit-community/qcode-discovery/pull/11#issuecomment-6368684584) · [case study](CASE_QCODE_CAMPAIGN4.md) | **Merged 23 Oct 2026.** Independent review and merge. |

## Maintainer-confirmed findings (3 distinct issues)

| ID | Scope | Evidence | Result |
| --- | --- | --- | --- |
| B01 | 4 previously unresolved quantum code equivalence clusters | [My issue #2643](https://github.com/unitaryfoundation/qldpc-challenge/issues/2643) · [maintainer's PR #2702](https://github.com/unitaryfoundation/qldpc-challenge/pull/2702) · [case study](CASE_QEC_FOUR_CLUSTERS.md) | **Issue completed / maintainer PR merged 3 Oct 2026.** The PR is the maintainer's work, not mine. |
| B02 | 2 bit-vector CHC demo/06 instances O0/O2 have UNSAT certificates | [My issue #1](https://github.com/aaronbembenek/binary-chc-problems/issues/1) · [original public issue and evidence](https://github.com/aaronbembenek/binary-chc-problems/issues/1) | **Completed 12 Oct 2026.** Maintainer confirmed verdicts and corrected expected results. |
| B03 | Structural decomposition of ten Campaign 4 CSS records | [My issue #2942](https://github.com/unitaryfoundation/qldpc-challenge/issues/2942) · [independent check](https://github.com/unitaryfoundation/qldpc-challenge/issues/2942#issuecomment-6124605835) | **Independently confirmed 12 Oct 2026.** Vincent Russo rebuilt all 39 records and confirmed exactly the ten reported decompositions. The verifier's connectedness checks already covered these cases. |

## Public evidence awaiting independent adoption or confirmation (six issues; one active PR and one PR closed without merge)

| ID | Scope | Evidence | Latest checked status |
| --- | --- | --- | --- |
| D01 | SAT benchmark `vdwb_k6_n400`: 400-variable SAT witness, proposed database verdict update | [Case study](CASE_SAT_VDWB_K6_N400.md) · [original evidence, SAT issue #2 (open)](https://github.com/satcompetition/2026/issues/2) · [GBD PR #3 (closed)](https://github.com/Udopia/gbd-data/pull/3) · [database diff](https://github.com/Udopia/gbd-data/pull/3/files) | **Author-side witness; GBD PR CLOSED WITHOUT MERGE on 11 Nov 2026.** Reported 31,600/31,600 clauses satisfied; negative control rejects clause 12,954. No recorded upstream approval; **not a merged result**. |
| D02 | CHC-COMP: 8 quic3 `standard_init2`–`standard_init9` models | [Benchmark issue #11](https://github.com/chc-comp/chc-comp26-benchmarks/issues/11) · [public models and standalone generator](chc_comp_issue11/README.md) | **Open (31 Oct review).** Author-side validation, corrupted controls, frozen model ZIP and [reproducer instructions](chc_comp_issue11/README.md) supplied; current-2026 validator nontermination needs independent resolution. 2026 metadata already contains `true` placeholders; not official independent model acceptance. |
| D03 | CHC-COMP: `O3_sum_array` model | [Benchmark issue #10](https://github.com/chc-comp/chc-comp26-benchmarks/issues/10) | **Open.** Awaiting third-party confirmation. |
| D04 | CHC-COMP: `goal71` model | [Benchmark issue #9](https://github.com/chc-comp/chc-comp26-benchmarks/issues/9) | **Open.** Awaiting third-party confirmation. |
| D05 | VMT/CHC: two array initialization models | [Benchmark issue #1](https://github.com/chc-comp/vmt-chc-benchmarks/issues/1) | **Open.** Awaiting third-party confirmation. |
| D06 | SYNTCOMP parity-game witness and five-instance provenance | [Own issue #1](https://github.com/henryksobon300-code/my-work-henryk-sobon/issues/1) · [author-side research record](SYNTCOMP_2026_PARITY_PUBLIC_CONTRIBUTION_RECORD.md) | **Open (author archive).** No competition certification or ranking established. |
| D07 | Two n=180 CSS code entries: proposed exact distance 14 in X and Z | [My PR #5336](https://github.com/unitaryfoundation/qldpc-challenge/pull/5336) · [public independent-solver reproduction](https://github.com/unitaryfoundation/qldpc-challenge/pull/5336/files) | **Draft, no review or merge (11 Nov 2026).** Eight completed searches reported by two public third-party solvers; certificate level `solver`, not proof-log or formal. Prose, lint, format and replay workflows passed. Full verify was cancelled. No code-construction claim and no private MathemaSpace source. |

## Other computational projects and research threads

These are **not automatically included in the merged-contribution count**. A more precise, version-separated catalogue is at [Experimental research — evidence register](EXPERIMENTAL_RESEARCH_INDEX.md).

| Research thread | Public status and limits |
| --- | --- |
| **CSS code `[[1000,406,6]]` distance certificate** | [Public proof argument](qldpc-1000-406-d6/PROOF.md) · [verifier archive](../MathemaSpace_D6_PUBLIC.zip) · [original author PR #3863](https://github.com/unitaryfoundation/qldpc-challenge/pull/3863). Original code and weight-six witnesses belong to @hirobumii; Henryk Soboń's additional proof was independently checked by the original code author, formalized in Lean and accepted as a [formal distance-6 certificate in merged PR #4226](https://github.com/unitaryfoundation/qldpc-challenge/pull/4226) on 30 Oct 2026. The formal certificate PR was authored by @hirobumii, not Soboń. |
| **QEC-09 — Two tighter Campaign 7 PBB distance bounds** | [Public certificates and verifier](qcode-distance-bounds/). Reproducible author-side upper bounds for the two catalogue records. |
| **QEC-10 — Weight-72 logical for `684-6-77`** | [Certificate and verifier](qldpc-684-distance-bound/). The explicit Z witness establishes `d≤72` on the existing code. |
| **QEC-11 — Lower leading decoding error at fixed `[[980,398,6]]` parameters** | [Proof, matrices and Python replay](qldpc-980-low-noise/). At small independent depolarizing noise with perfect syndrome measurement and ML recovery, the leading coefficient is 3.869% smaller than for the existing code in PR #3867. |
| **SciPy graph Laplacian integer overflow** | [Original issue #26549](https://github.com/scipy/scipy/issues/26549) · [proposed patch](scipy-26549/laplacian_dtype_promotion.patch). Local test evidence is reported; upstream acceptance/full CI are not claimed. |
| **BLR determinant positivity: 26 proposed infinite families** | [Public arguments, scripts and finite certificates](blr-positivity-26-families/). Proposed partial result requires independent mathematical review; not a proof of the full conjecture. |
| New CSS code equivalence pairs `10-2-3 / 10-2-3-b` and `12-2-4 / 12-2-4-b` | Reported author-side certificate package (22 Oct 2026); **not yet incorporated in external repository**. Private source and current public-package review should remain separate. |
| Baum–Sweet / TheoremDB P2422 Hankel calculation | Reported finite modular non-vanishing checks for orders 1–30,000 in two fields. **Not a proof for all orders; novelty and literature priority unconfirmed.** Do not call this problem solved. |

### Recorded material not yet hosted with full public replay files

The [publication and evidence-status register](PUBLICATION_STATUS.md) tracks **9 additional research records**, including Array-Generator and NetworkX cases and an unreviewed BLR range extension. Each record describes its evidence and review status.

Their source correspondence and local notebooks are **not equivalent to public GitHub proof packages**. No independent replay or acceptance is implied; private engine code remains unhosted.

## Status hygiene and withdrawn claims

- [My earlier qLDPC PR #3362](https://github.com/unitaryfoundation/qldpc-challenge/pull/3362) was **closed without merge on 13 October 2026**. The maintainer found the proposed components duplicated functionality already present upstream and objected to binary ZIP packaging. This is not counted as a merged contribution or a new result.

The main website lists only merged contributions, maintainer-confirmed findings, active public submissions and explicitly bounded public research. A proposal rejected as incorrect, superseded by prior work without an independent added contribution, or withdrawn after failed validation should be removed from the **active** catalogue after checking the original maintainer discussion. Preserve a dated historical record rather than deleting the original GitHub issue or rewriting the review history.

An open issue is not proof of acceptance, but it is also not proof of rejection. A closed issue may be fixed, declined, duplicated or merely administratively closed; review the actual resolution before changing status. An earlier discovery by another author must be attributed, and any incremental contribution described narrowly.

**Audit boundary (11 November 2026, selected statuses only):** current GitHub state was checked for qLDPC PR #2740, qcode-discovery PR #11, qLDPC certificate PR #4226, GBD PR #3, CHC-COMP issues #9–11, VMT/CHC issue #1, SAT Competition issue #2 and SciPy issue #26549. The three PRs #2740, #11 and #4226 are merged; GBD PR #3 was **closed without merge** on 11 Nov 2026 with no explanatory review; the original SAT Competition issue #2 remains open. The listed other benchmark/software issues remain open. The new PR #5336 was checked on 11 November: open Draft, prose and other completed checks passed, full verify cancelled, no review. This check is not a comprehensive historical audit of all email discussions, attachments or closed submissions.

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
