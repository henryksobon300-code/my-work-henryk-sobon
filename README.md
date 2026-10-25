# Henryk Soboń — Independent Research & Technical Contributions

<img src="Screenshot_20261008-214406~2.jpg" alt="Portrait of Henryk Soboń" width="225" align="right">

**Quantum error correction · qLDPC codes · formal verification · reproducible computational research**

Independent researcher working with exact structural checks, program and graph representations, SAT/CHC benchmarks and machine-checkable certificates.

I try to make each public claim inspectable: a specific problem, evidence, a verifier where possible, the external review status, and the limits of the result. These are technical contributions and research experiments, not a claim of formal academic affiliation or a comprehensive new theory.

[Research website](https://henryksobon300-code.github.io/my-work-henryk-sobon/) · **[Website projects & public discussions](https://henryksobon300-code.github.io/my-work-henryk-sobon/projects.html)** · [Full GitHub source register](research/RESULTS_INDEX.md) · [Evidence and status register](RESEARCH_STATUS.md) · [Experimental research catalogue](research/EXPERIMENTAL_RESEARCH_INDEX.md) · [External review record](research/EXTERNAL_REVIEW.md)

## Merged pull requests authored by me

### 1. qLDPC Challenge — CSS row-space intersection diagnostic

- **Merged 4 October 2026** — [unitaryfoundation/qldpc-challenge PR #2740](https://github.com/unitaryfoundation/qldpc-challenge/pull/2740)
- Added a computed GF(2) row-space intersection dimension diagnostic with regression tests to the trusted verifier.
- `dim(row(H_X) ∩ row(H_Z)) = rank(H_X) + rank(H_Z) − rank([H_X; H_Z])`.
- The identity is established mathematics; the contribution was its integration and verification in this codebase. [Read case study](research/CASE_QEC_INTERSECTION.md).

### 2. qcode-discovery — exact-distance status transfer, Campaign 4

- **Merged 23 October 2026** — [qiskit-community/qcode-discovery PR #11](https://github.com/qiskit-community/qcode-discovery/pull/11)
- Certified five records as permutation-equivalent to an already exact `[[288,12,12]]` representative using explicit qubit maps, exact row-space checks and a replay verifier.
- The audit covered 39 records in 29 equivalence classes. The change transfers exactness; it does not claim a newly discovered quantum code. [Read case study](research/CASE_QCODE_CAMPAIGN4.md).

## Findings confirmed and acted on by maintainers

### Four duplicate qLDPC code clusters

- [My issue #2643](https://github.com/unitaryfoundation/qldpc-challenge/issues/2643) provided explicit qubit permutations and row-space comparisons.
- The maintainer independently verified the result and merged [their PR #2702](https://github.com/unitaryfoundation/qldpc-challenge/pull/2702) removing four duplicate entries on 3 October 2026.
- **This was the maintainer's PR, not an additional PR authored by me.** [Read case study](research/CASE_QEC_FOUR_CLUSTERS.md).

### Two bit-vector CHC benchmark verdicts

- [My issue #1](https://github.com/aaronbembenek/binary-chc-problems/issues/1) supplied exact UNSAT certificates for `demo/06` O0 and O2 with an independent checker and a corrupted negative control.
- The project maintainer confirmed both UNSAT results, updated the expected-results table and closed the issue in October 2026.
- This establishes the verdicts for two exact test instances, not a general solver.

## Ongoing external review

- [CHC-COMP: eight quic3 SAT models — issue #11](https://github.com/chc-comp/chc-comp26-benchmarks/issues/11): **open**, with author-side validation and negative controls; awaiting external adoption.
- [Additional CHC-COMP and VMT models](RESEARCH_STATUS.md): submitted for review; no organizer certification claimed.
- [GBD SAT correction — PR #3](https://github.com/Udopia/gbd-data/pull/3): **open**; `vdwb_k6_n400` satisfying assignment and proposed metadata correction.
- [SYNTCOMP parity witness](https://github.com/henryksobon300-code/my-work-henryk-sobon/issues/1): independently checkable author-side evidence, without claiming a competition result.

## Experimental methods and MathemaSpace

I also conduct experimental research under the **MathemaSpace** name. Specific results are documented separately from any proprietary implementation. This public portfolio does not describe the underlying engine architecture.

The research engine and its source packages are kept in a private repository. This README does not provide public access to them or imply outside certification.

A [Campaign 4 decomposition report](https://github.com/unitaryfoundation/qldpc-challenge/issues/2942) was independently reproduced by a maintainer: ten of 39 entries decomposed. Related connectivity gates already existed upstream; I therefore do **not** present it as a newly implemented feature.

Additional results are catalogued in the [experimental research register](research/EXPERIMENTAL_RESEARCH_INDEX.md), with distinct evidence status and limitations. Unreleased internal methods and implementation details are excluded.

## Research practice

I distinguish: **(1)** code merged into a third-party repository, **(2)** findings independently confirmed and acted on by maintainers, **(3)** reproducible author-side calculations and certificates, and **(4)** hypotheses or prototypes still requiring validation.

For technical details, rejected proposals, known limitations and the current status of outstanding reports, see the [evidence register](RESEARCH_STATUS.md). The [complete public outcomes index](research/RESULTS_INDEX.md) tracks **all 11 authored issues and 4 PRs identified in the 24 October 2026 audit** and separately indexes experimental research. The [external review summary](research/EXTERNAL_REVIEW.md) links publicly inspectable review; private emails are not published.

*Last status review: 25 October 2026.*
