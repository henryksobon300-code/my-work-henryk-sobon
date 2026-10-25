# MathemaSpace and related research — experimental work register

**Henryk Soboń** · Public summary reviewed: 25 October 2026  
[Main site](https://henryksobon300-code.github.io/my-work-henryk-sobon/) · [Verified contributions and reports](https://henryksobon300-code.github.io/my-work-henryk-sobon/projects.html) · [Evidence ledger](../RESEARCH_STATUS.md)

## Purpose and status vocabulary

This index addresses research that would be lost if the portfolio included **only merged GitHub PRs**. It is a map of distinguishable workstreams, not a claim that every workstream produced a novel peer-reviewed discovery.

- **Externally reproduced:** a named outside reviewer or maintainer independently checked a particular computation. The exact scope remains narrow.
- **Public author-side evidence:** a public repository/issue contains the author's replay or witness, but upstream reviewers have not adopted its conclusion.
- **Private/archived author-side evidence:** test packages exist in the private research correspondence; those experiments have not been re-run for this portfolio and are not openly reproducible from this page.
- **Research concept/IP:** exploratory implementation or engineering proposal, not certified theoretical novelty or commercial deployment.

A private scientific email discussing an idea is not equivalent to independent validation, and no correspondence is quoted here without permission.

## 1. Public independently inspected findings that are not another merged author PR

### QEC-OBS-01 — Ten decomposable BB/CSS records, Campaign 4

**Status:** externally reproduced observation, not a new merged verifier feature.

- The public [original issue #2942](https://github.com/unitaryfoundation/qldpc-challenge/issues/2942) reports ten reducible entries among 39 Campaign 4 records.
- In a [public technical reply](https://github.com/unitaryfoundation/qldpc-challenge/issues/2942#issuecomment-6124605835), the maintainer independently reconstructed the source records and reproduced the ten classifications.
- **Critical limit:** the repository already had relevant connectivity checks; this was not a newly discovered missing check that I subsequently merged.
- Count it once as a checked dataset observation; do not count as a new code or an additional merged PR.

### SYN-2026 — Parity-realizability certificates

**Status:** publicly recorded author-side certification with a competition-organizer discussion; **not** an official solver ranking.

- [Public attribution and scope record](SYNTCOMP_2026_PARITY_PUBLIC_CONTRIBUTION_RECORD.md) · [original issue](https://github.com/henryksobon300-code/my-work-henryk-sobon/issues/1).
- For `steadygame_pb_12_pe_`, the author reported a 9-state environment cycle, exhaustive controller checks, and subsequent native game export/verification with Knor and Oink. A deliberately altered certificate was reported rejected.
- Five historically no-verdict cases and a separate experimental solver run were reported, but these are **distinct experiments** and not one official benchmark score.
- **Missing:** a full public replay bundle linked here and an official organizer evaluation or certificate. The publicly available description must not be called a competition win.
- The organizer's private feedback is not published here or used as a personal endorsement.

## 2. Author-side exact, finite, or reproducible experiments requiring broader review

### QEC-DATA-02 — Two CSS stabilizer-code equivalence pairs

**Status:** archived author-side certificates; not upstream merged and not independently reviewed for this register.

- Reported pairs: `10-2-3` versus `10-2-3-b`, and `12-2-4` versus `12-2-4-b`.
- The 22 October 2026 PUBLIC/PRIVATE-separated handoff describes coordinate permutations and X/Z row-space checks with corrupted controls.
- **Limit:** this is equivalence of specific database entries, not discovery of new `[[n,k,d]]` code parameters or a new theorem.
- The public-ready package has not been uploaded as a verified accessible artifact through this page. Private provenance and algorithmic history remain unpublished.

### MATH-FIN-01 — Baum–Sweet / TheoremDB P2422

**Status:** finite modular computation reported in archived tests; not a proof of the open infinite statement.

- The October 22 evidence package reports nonvanishing finite Hankel determinants for orders **1 through 30,000**, using separate C++17 approaches in GF(100000007) and GF(1000003), with tables and checks.
- [Problem statement P2422](https://theoremdb.org/statements/P2422/).
- **Limit:** nonzero determinants mod a prime for specific finite orders are evidence only for those orders. This is **not** a proof for all n. World novelty and priority were not established.
- Reproduction and primary source availability should be checked before publicly asserting the package's stronger reproducibility guarantees.

### HAAL-V18 — Resetless model/state diagnosis

**Status:** author-reported bounded study with substantive external methodological criticism, not proven state-of-the-art performance.

- V18 reported a yes/no answer on **71 public HAAL protocol models** for an adaptive distinguishing-sequence existence question.
- A technical reviewer pointed out that a preset distinguishing sequence cannot exist where an adaptive one does not, so the attempted PDS-versus-ADS comparison was not well balanced. Further pruning and baseline issues were identified.
- **Limit:** a `71/71` response count is **not** a superiority score, a complete active-automata-learning solution, or a scientific novelty proof.
- Full experiment replay and corrected baseline evaluation remain separate work.

### PROG-BRIDGE — Exact finite transition-system equivalence

**Status:** reported finite-state certificates; external feedback established a semantic mismatch with a published benchmark.

- Experimental cases use state and command bijections and test commuting transitions under `P(T_A(c,s)) = T_B(C(c),P(s))` on a finite state space.
- The original experiment included three holdouts of `4096 × 8` transition checks, followed by larger author-side positive and negative controls.
- **Limit:** this is not an accepted EquiBench score, because EquiBench's language/category-specific notion of correspondence is different. The methodology needs a separate semantic adapter and blinded evaluation before that stronger claim.

### CORE-013 — Bounded structural engine experiment

**Status:** public executable research artifact with limited claim scope.

- [Original Mathemaspace repository](https://github.com/henryksobon300-code/Mathemaspace).
- Read its source README for the exact tasks, test provenance and frozen boundary. It is one component, **not** a proven general-purpose system able to solve arbitrary research problems.

## 3. Other distinct experimental and engineering branches

The following threads have been recorded in project history but are not certified independently within this portfolio. They must remain distinct rather than be pooled into a single reported success rate.

| Track | What it studies | Limit/status |
| --- | --- | --- |
| MathemaSpace Genesis / V12 | Distinguishability and sufficiency of a representation | Archived prototypes; method and baseline versions must be matched before retesting |
| MathemaSpace V13 | Preserving behaviour/cost while quotienting or merging states | Different task from V12; archived, externally unconfirmed |
| MathemaSpace V14 | Choosing informative observations or discriminating tests | Different task from V12/V13; archived, externally unconfirmed |
| ABC-RLE / MRS / ABC SBC-2 | Historical relational and compressed-structure engines | Multiple distinct implementations and protocols; no blanket claim of superiority |
| V19–V23 | Selected finite algebraic/quantum-code checks and construction attempts | Small-scale/synthetic tests and known mathematical mechanisms; exact version and checker required |
| NASA ADAPT experiments | Reduction of observation channels while preserving distinguishability on selected scenarios | Archived author-side tests; source/version/negative controls needed for public confirmation |
| Laurent-model GF(2) work | Reported example/counterexample structures | Needs an unambiguous problem definition and independent verification before a new claim |
| MH370 drift-compatibility model | Model sensitivity of candidate debris-transport corridors | Hypothesis under assumptions, **not** identification of wreck location |
| OMEGA / machine pattern studies | Numerical and structural research prototypes | Author-side experiments, not externally certified scientific discovery |
| Rotor / stateful dynamic network | A patent-sensitive computational/engineering concept | Do not disclose private algorithm, claims or unreleased implementation without IP review |

## 4. How these projects should be assessed

To promote a row to **verified public achievement**, retain original dataset identity, frozen code version, exact claim, independent or orthogonal checker, positive and negative controls, baseline/limitations, and review/adoption source. An independent critic identifying an invalid baseline is a useful part of research history, **not** evidence that the original claim passed.

### What is not claimed

No general AGI capability, all-domain scientific superiority, novel mathematical theorem, established patent novelty, accredited solver certification, formal academic title, or blanket independent endorsement is claimed.

### Evidence and disclosure

This is a **public descriptive index**, not an archive of source code or unconsented third-party messages. Original PRIVATE engines, mail transcripts, legal correspondence, unreleased patent material and any private container references remain excluded.

Last scope check: Gmail's relevant research and reviewer threads plus public GitHub records were re-examined on 25 October 2026. An exhaustive replay of every archived test, notebook and email attachment was **not** performed in this update.
