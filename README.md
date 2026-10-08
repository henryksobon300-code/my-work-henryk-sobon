# Henryk Soboń — Quantum Computing, Quantum Codes & Formal Verification

**qLDPC • Quantum Error Correction • SAT • CHC • Formal Verification • Computational Discovery • Machine-Checkable Proofs**

Independent work on quantum error-correcting codes, qLDPC, SAT/CHC verification, program equivalence, structural equivalence and machine-checkable computational results.

## Public contributions

### Merged contribution — qLDPC Challenge

**CSS row-space intersection dimension invariant**

I contributed the exact GF(2) diagnostic

`dim(row(H_X) ∩ row(H_Z)) = rank(H_X) + rank(H_Z) - rank([H_X; H_Z])`

to the public qLDPC Challenge verifier.

- Pull request: https://github.com/unitaryfoundation/qldpc-challenge/pull/2740
- Status: **MERGED**
- Merge commit: `6535af57ee494f77dfe9f4c22f737b5486fbb7b4`

### Result adopted by maintainers — qLDPC code equivalence

I found explicit physical-qubit permutations resolving four previously unresolved equivalence clusters in the qLDPC Challenge.

- Original issue and certificates: https://github.com/unitaryfoundation/qldpc-challenge/issues/2643
- Maintainer implementation: https://github.com/unitaryfoundation/qldpc-challenge/pull/2702
- Status: **MERGED**

The maintainer PR explicitly closes my issue and removes the four duplicate code entries after independent re-verification.

## Current public work

### Quantum codes — Campaign 4 exact-distance transfer

Five qLDPC Campaign 4 records are shown to be permutation-equivalent to an already exact `[[288,12,12]]` representative. The PR transfers exact distance using the repository's existing colored-BLISS equivalence machinery and explicit qubit maps.

- Pull request: https://github.com/qiskit-community/qcode-discovery/pull/11
- Status: **OPEN / under review**
- Full Campaign 4 audit: 39 rows, 29 equivalence classes
- Exact reference class: 6 records
- Transfers verified: 5/5

### SAT / Global Benchmark Database

For SAT Competition benchmark `vdwb_k6_n400.sanitized.cnf.xz`, I produced a complete 400-variable satisfying assignment verified against all 31,600 clauses, together with a negative control.

- Public evidence: https://github.com/satcompetition/2026/issues/2
- GBD correction PR: https://github.com/Udopia/gbd-data/pull/3
- Proposed metadata change: `unknown → sat`
- Status: **OPEN / awaiting maintainer review**

## Research areas

- Quantum computing and quantum error correction
- qLDPC and CSS quantum codes
- Exact code equivalence and structural invariants
- SAT and CHC benchmark verification
- Formal verification and machine-checkable certificates
- Program and state-space equivalence
- Computational discovery of structural relations

## Principle

Results listed here are linked to public repositories, explicit witnesses, verifiers, merged changes or reviewable pull requests whenever possible.
