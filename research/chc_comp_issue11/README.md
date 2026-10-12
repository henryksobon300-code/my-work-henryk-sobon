# CHC-COMP issue #11 — eight quic3 SAT models

This directory is a narrow reproducibility supplement for:
https://github.com/chc-comp/chc-comp26-benchmarks/issues/11

It contains two public, benchmark-specific archives:

- `CHC_COMP_8X_MODELS_ONLY_20261012.zip` — the eight candidate SMT-LIB model files plus SHA-256 hashes.
- `CHC_COMP_8X_STANDALONE_REPRODUCER_20261012.zip` — a small script that regenerates those eight final model files from the already stated invariant family, plus expected hashes and a byte-for-byte comparison receipt.

The standalone reproducer is not the private MathemaSpace search/discovery engine. It only regenerates the final models for this one benchmark family.

Archive SHA-256:

- models-only: `a5bda769f1410094612f090a5a0b4fc4bca79091fd4d14bed19a354595a0e457`
- standalone reproducer: `957ead6b5400fc8e4a281d147945c68191856a70bc08d5d324003007b02b757e`

Pinned validation route used in the successful replay:

- `chc-comp/chc-comp25-scripts@674721f1f9e5afb97528fc14a02c2afc5354c409`
- `z3-solver==4.13.3.0`
- `ply==3.11`

Expected validation result for each of the eight candidate models: `unsat`.
Deliberately corrupted final-value controls: `sat`.

The separate current-validator hang reported by Levente is still a distinct reproducibility question; this supplement does not claim to explain it.
