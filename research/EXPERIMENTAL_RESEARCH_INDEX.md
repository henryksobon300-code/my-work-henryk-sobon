# Experimental research — results and evidence register

**Henryk Soboń** · Public summary reviewed: 25 October 2026  
[Main site](https://henryksobon300-code.github.io/my-work-henryk-sobon/) · [Verified contributions and reports](https://henryksobon300-code.github.io/my-work-henryk-sobon/projects.html) · [Evidence ledger](../RESEARCH_STATUS.md) · [Publication queue](PUBLICATION_STATUS.md)

## Purpose and status vocabulary

This index preserves bounded computational research that has a meaningful mathematical result or testable certificate. It is not a claim that every experiment produced a novel peer-reviewed discovery.

- **Externally reproduced:** a named outside reviewer or maintainer independently checked a particular computation. The exact scope remains narrow.
- **Public author-side evidence:** a public repository/issue contains the author's replay or witness, but upstream reviewers have not adopted its conclusion.
- **Private/archived author-side evidence:** test packages exist in the private research correspondence; those experiments have not been re-run for this portfolio and are not openly reproducible from this page.

A private scientific email discussing an idea is not equivalent to independent validation, and no correspondence is quoted here without permission.

## Public author-side research certificates

### SYN-2026 — Parity-realizability certificates

**Status:** publicly recorded author-side certification with a competition-organizer discussion; **not** an official solver ranking.

- [Public attribution and scope record](SYNTCOMP_2026_PARITY_PUBLIC_CONTRIBUTION_RECORD.md) · [original issue](https://github.com/henryksobon300-code/my-work-henryk-sobon/issues/1).
- For `steadygame_pb_12_pe_`, the author reported a 9-state environment cycle, exhaustive controller checks, and subsequent native game export/verification with Knor and Oink. A deliberately altered certificate was reported rejected.
- Five historically no-verdict cases and a separate experimental solver run were reported, but these are **distinct experiments** and not one official benchmark score.
- **Missing:** a full public replay bundle linked here and an official organizer evaluation or certificate. The publicly available description must not be called a competition win.
- The organizer's private feedback is not published here or used as a personal endorsement.

## Finite calculations and code-equivalence investigations

### QEC-DATA-02 — Two CSS catalogue equivalences (QEC-12)

The [public permutations and verifier](qldpc-css-equivalences/) cover `10-2-3` / `10-2-3-b` and `12-2-4` / `12-2-4-b`. The Challenge verifier and full row-space enumeration both confirm the equivalences on the pinned catalogue data. External review is pending.

### MATH-FIN-01 — Baum–Sweet / TheoremDB P2422

**Status:** finite modular computation reported in archived tests; not a proof of the open infinite statement.

- The October 22 evidence package reports nonvanishing finite Hankel determinants for orders **1 through 30,000**, using separate C++17 approaches in GF(100000007) and GF(1000003), with tables and checks.
- [Problem statement P2422](https://theoremdb.org/statements/P2422/).
- **Limit:** nonzero determinants mod a prime for specific finite orders are evidence only for those orders. This is **not** a proof for all n. World novelty and priority were not established.
- Reproduction and primary source availability should be checked before publicly asserting the package's stronger reproducibility guarantees.

## Publication queue and additional records

The [publication-status register](PUBLICATION_STATUS.md) distinguishes **complete public proof files already hosted** from archived results **whose full replay material is not released here**. It covers the `[[980,398,6]]` candidate, additional quantum-code upper bounds, Array-Generator and NetworkX, a BLR extension, finite Baum–Sweet computation, CSS data-equivalence pairs and further qLDPC/SDP tests. The cross-reference preserves the record without presenting historical reports as merged contributions or externally reviewed discoveries.

## Evidence requirements

To promote a row to **verified public achievement**, retain original dataset identity, frozen code version, exact claim, independent or orthogonal checker, positive and negative controls, baseline/limitations, and review/adoption source. An independent critic identifying an invalid baseline is a useful part of research history, **not** evidence that the original claim passed.

### What is not claimed

No general AGI capability, all-domain scientific superiority, novel mathematical theorem, established patent novelty, accredited solver certification, formal academic title, or blanket independent endorsement is claimed.

### Evidence and disclosure

This is a **public descriptive index**, not an archive of source code or unconsented third-party messages. Unreleased software, mail transcripts, legal correspondence, patent-sensitive material and private file references remain excluded.

Last scope check: Gmail's relevant research and reviewer threads plus public GitHub records were re-examined on 25 October 2026. An exhaustive replay of every archived test, notebook and email attachment was **not** performed in this update.
