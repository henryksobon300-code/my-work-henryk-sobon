# External review — public record and claim boundaries

**Selected review records updated: 26 November 2026** · [Research results index](RESULTS_INDEX.md)

This page records review that a visitor can independently inspect in **public primary sources**. Private correspondence is indexed separately and is **not posted or quoted without permission**. Technical correspondence is not equivalent to formal peer review.

## Public independent checks and accepted changes

### Campaign 4 — qcode-discovery

[PR #11](https://github.com/qiskit-community/qcode-discovery/pull/11) ([direct reviewer confirmation](https://github.com/qiskit-community/qcode-discovery/pull/11#issuecomment-6368684584)) contains a public independent review of the five proposed exact-distance transfers and the eventual merge into the repository. The accepted claim concerns five records proven permutation-equivalent to an existing exact reference.

### CSS invariant in the qLDPC verifier

[PR #2740](https://github.com/unitaryfoundation/qldpc-challenge/pull/2740) ([direct independent review](https://github.com/unitaryfoundation/qldpc-challenge/pull/2740#pullrequestreview-5405628122)) records the public discussion, requested fixes and accepted implementation of an established GF(2) rank invariant in the verifier.

### Four quantum-code equivalence clusters

[Original report #2643](https://github.com/unitaryfoundation/qldpc-challenge/issues/2643) and the separate [maintainer PR #2702](https://github.com/unitaryfoundation/qldpc-challenge/pull/2702) document an independently reviewed finding that resulted in removal of four duplicate entries. The maintainer authored the corrective PR.

### Two binary-CHC benchmark corrections

[Original report #1](https://github.com/aaronbembenek/binary-chc-problems/issues/1) includes the submitted evidence and the completed maintainer correction of two specific `demo/06` verdicts.

### Ten decomposable Campaign 4 CSS records

I reported ten Campaign 4 CSS records that split into smaller code blocks. Vincent Russo rebuilt all 39 inputs and independently confirmed exactly those ten decompositions. The qLDPC Challenge verifier already checks connectedness.

- [Original issue #2942](https://github.com/unitaryfoundation/qldpc-challenge/issues/2942)
- [Vincent Russo's independent verification](https://github.com/unitaryfoundation/qldpc-challenge/issues/2942#issuecomment-6124605835)

### 684-qubit weight-72 witness — independently checked and adopted

Vincent Russo [rechecked the witness against the existing catalogue matrices](https://github.com/unitaryfoundation/qldpc-challenge/pull/5591#issuecomment-6979095564). [PR #5591](https://github.com/unitaryfoundation/qldpc-challenge/pull/5591) merged 18 November; the correctly formatted [catalogue revision #6789](https://github.com/unitaryfoundation/qldpc-challenge/pull/6789) merged 19 November. This establishes an upper bound of 72, not exact distance, and the two PRs concern the same witness.

### Exact distance six — formal certificate by the original code author

[PR #4226](https://github.com/unitaryfoundation/qldpc-challenge/pull/4226), authored by @hirobumii, merged 30 October 2026. It credits Henryk Soboń's supplied proof and records the Lean formalization and replay for the unchanged `[[1000,406,6]]` code. The code construction and formal-certificate PR belong to @hirobumii.

### Two n=180 codes — research note accepted

[Author PR #5336](https://github.com/unitaryfoundation/qldpc-challenge/pull/5336) merged 18 November 2026 as a preliminary research record. The merge does not certify exact distance 14 or change official distance-confidence values.

### NetworkX — concrete regression acknowledged by the PR author

Reported a concrete extreme-float regression in another contributor's spanning-arborescence PR. The PR author acknowledged the cancellation bug, committed a correction and added two regression tests. The PR remains open and unmerged; this confirmation covers the reported regression, not the separate local candidate or all numeric and partition cases.

[My report](https://github.com/networkx/networkx/pull/8979#issuecomment-7143906292) · [PR-author acknowledgement and correction](https://github.com/networkx/networkx/pull/8979#issuecomment-7184429671). The correction was committed in revision `5f71f10925dd1e3b96e4f30164df2024d6ed332e`. The author's report of 221 passing tests is attributed to that author; this audit does not claim a fresh independent test run.

### SymPy — revised implementation still awaiting review

[PR #31142](https://github.com/sympy/sympy/pull/31142): Open and unmerged. Automated checks on commit `64c30bc967b018df6af8d918702f7f0a47887235` passed; the revised implementation awaits maintainer review. Earlier feedback on an older implementation is not approval of the current revision. Public comments on the earlier implementation include requests for reuse of existing cycle logic and a reported regression; they are not final approval.

## Other expert conversations — restricted to private records

There have also been technical conversations about:

- Unpublished mathematical/engineering concepts (technical questions about possible applications; no implementation details disclosed).
- Competition-grade parity-game witnesses and CHC model validation (reproducibility questions and outstanding official validation).
- Possible modular-system applications for an adaptive graph concept (early interest only, no funding or signed collaboration).

These exchanges helped refine scope and experimental design. **They are not presented as official endorsement, collaboration, funded work or independent validation of the entire research platform.** The internal private archive stores source correspondence and follow-up decisions.

## Policy for acknowledgements and quotations

Publicly thank a contributor for a specific form of assistance, such as identifying a missing baseline or performing an independent replay, only when appropriate. Never manufacture testimonials. For direct extracts from private email or name-and-quote displays, obtain explicit permission from the correspondent and preserve their context.

[Portfolio](../README.md) · [Complete public issue/PR index](RESULTS_INDEX.md) · [Publication status](PUBLICATION_STATUS.md)
