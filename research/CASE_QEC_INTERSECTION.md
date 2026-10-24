# Case study — CSS row-space intersection diagnostic

**Author:** Henryk Soboń  
**Project:** [Unitary Foundation qLDPC Challenge](https://github.com/unitaryfoundation/qldpc-challenge)  
**Record:** [My merged PR #2740](https://github.com/unitaryfoundation/qldpc-challenge/pull/2740) · merged 4 October 2026  
**Status:** Accepted software contribution, independently reviewed  
**Back to:** [Research index](RESULTS_INDEX.md) · [Portfolio](../README.md)

## Problem
When candidate CSS stabilizer-code records have similar superficial signatures, one needs cheap, exact invariants that can distinguish inequivalent pairs before attempting expensive equivalence searches. The dimension of the intersection between X- and Z-stabilizer row spaces is such an invariant.

## Method
For binary check matrices `H_X` and `H_Z`, use the well-known GF(2) identity:

```text
dim(row(H_X) ∩ row(H_Z))
    = rank(H_X) + rank(H_Z) - rank([H_X; H_Z])
```

Row operations do not change these spaces, and simultaneous physical-qubit permutations and a global X/Z swap preserve the dimension. A difference is therefore a certificate of non-equivalence **under that defined equivalence group**.

## Contribution
The pull request incorporated the stacked-matrix rank computation into the qLDPC Challenge verifier's diagnostic output and added regression tests. It was reviewed by the project maintainer and merged. The mathematics itself was **not** claimed as a new theorem.

## Evidence
- [Merged original code and review discussion — PR #2740](https://github.com/unitaryfoundation/qldpc-challenge/pull/2740)
- [First independent maintainer review](https://github.com/unitaryfoundation/qldpc-challenge/pull/2740#pullrequestreview-5405628122)
- [Second pass verifying the requested fixes](https://github.com/unitaryfoundation/qldpc-challenge/pull/2740#pullrequestreview-5408209621)
- [Original motivating reviewer discussion — 510-qubit candidate pair](https://github.com/unitaryfoundation/qldpc-challenge/issues/2643) (the four-cluster issue is a separate earlier result)
- Merge commit: `6535af57ee494f77dfe9f4c22f737b5486fbb7b4`.

## Limitations
This diagnostic can refute equivalence under the stated operations when the dimensions differ. Equal values are **not sufficient** to establish equivalence. It does not compute or improve a quantum code's exact distance, and it does not independently solve the general code-equivalence problem.
