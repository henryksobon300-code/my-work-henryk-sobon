# Case study — Campaign 4 exact-distance status transfer

**Author:** Henryk Soboń  
**Project:** [qiskit-community/qcode-discovery](https://github.com/qiskit-community/qcode-discovery)  
**Record:** [My merged PR #11](https://github.com/qiskit-community/qcode-discovery/pull/11) · merged 23 October 2026  
**Status:** Accepted data/code change; independent maintainer replay and approval  
**Back to:** [Research index](RESULTS_INDEX.md) · [Portfolio](../README.md)

## Problem
Several entries in Campaign 4 had `d_is_exact = false` even though an exact `[[288,12,12]]` reference represented the same code up to a physical-qubit permutation. The dataset needed narrow, verifiable propagation of exact-distance metadata rather than repeated independent distance calculations for equivalent representatives.

## Method
An explicit bijective permutation of physical-qubit coordinates preserves Pauli weight. If both X and Z stabilizer row spaces match after that permutation, the code's minimum distance is the same. The report checked both row spaces and retained maps that can be independently replayed.

## Contribution
- Audited 39 Campaign 4 records and organized them into 29 equivalence classes.
- Identified an exact-distance reference class with six entries.
- Transferred existing exact distance `d=12` to five corresponding records with explicit permutation certificates and verification tooling.
- Kept the change scoped to dataset metadata and a replayable script.

## Independent review
The qcode-discovery reviewer **independently checked the changes and confirmed the results agreed** before approving PR #11. The PR was merged on 23 October 2026.

## Public evidence
- [Merged PR #11, code, verifier, review and acceptance](https://github.com/qiskit-community/qcode-discovery/pull/11)
- [Direct link to independent reviewer verification](https://github.com/qiskit-community/qcode-discovery/pull/11#issuecomment-6368684584)
- [Original issue #8 and initial public certificate](https://github.com/qiskit-community/qcode-discovery/issues/8)
- Merge commit: `da9178fd65ffc2eec3dab46089f9879eb02d4b23`.

## Limits
This work **did not discover a new `[[288,12,12]]` quantum code** and did **not** independently calculate the reference code's minimum distance from scratch. It made five existing records' exactness information consistent with a verified equivalence class. Its contribution is the traceable, accepted data correction.
