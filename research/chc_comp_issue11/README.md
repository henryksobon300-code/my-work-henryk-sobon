# CHC-COMP: eight `standard_init2`–`standard_init9` model records

**State of review: 31 October 2026 — open, no organizer validation recorded.**

This page is a focused technical evidence index for [CHC-COMP issue #11](https://github.com/chc-comp/chc-comp26-benchmarks/issues/11). The reported result is specific to eight `quic3/data/standard_init{2..9}_true-unreach-call_ground_000.smt2` benchmark files. A validator query returning `unsat` means the submitted model satisfies the relevant assertions; it is **not** a claim that the CHC task itself is UNSAT.

## Public reproducibility artifacts

- [Eight candidate models + SHA-256 hashes](CHC_COMP_8X_MODELS_ONLY_20261012.zip)
- [Standalone generator + expected hashes](CHC_COMP_8X_STANDALONE_REPRODUCER_20261012.zip)
- [Original discussion and Gidon's reproducibility request](https://github.com/chc-comp/chc-comp26-benchmarks/issues/11#issuecomment-6109149693)
- [Published instructions supplied on 12 October](https://github.com/chc-comp/chc-comp26-benchmarks/issues/11#issuecomment-6119161771)
- [Successful author-run GitHub Actions evidence](https://github.com/henryksobon300-code/Mathemaspace/actions/runs/36849827697)

Reported ZIP SHA-256:

- Models: `a5bda769f1410094612f090a5a0b4fc4bca79091fd4d14bed19a354595a0e457`.
- Standalone reproducer: `957ead6b5400fc8e4a281d147945c68191856a70bc08d5d324003007b02b757e`.

The reproducer publishes only the eight final models from the stated invariant family, **not** any private discovery/search engine.

## Reproduce the author-side result

1. Obtain the exact eight original `.smt2` benchmark files.
2. Extract the standalone reproducer and run `python3 generate_models.py --out models` from the documented working directory. Compare all eight model files against the frozen SHA-256 list.
3. Use [CHC-COMP 2025 model validator at pinned commit `674721f1f9e5afb97528fc14a02c2afc5354c409`](https://github.com/chc-comp/chc-comp25-scripts/blob/674721f1f9e5afb97528fc14a02c2afc5354c409/validate-model.py), with `z3-solver==4.13.3.0` and `ply==3.11`. For each benchmark, pipe a corresponding model to the validator and direct its output to an SMT-LIB validation query. Run the query with Z3 4.13.3.0. See the original issue comment for the exact example.
4. Reported results from the frozen replay: **8/8** complete candidate-model validation queries `unsat`, **8/8** deliberately corrupted models `sat`, **128/128** individual Horn-clause checks `unsat`.

These are **author-side** runs; a third-party reproduction using the organizer's preferred 2026 environment has not yet been recorded. This page does not claim to have freshly rerun the two ZIP packages.

## Why independent review remains open

- On **1 October**, Levente Bajczi reported running the [current-2026 validator](https://github.com/chc-comp/chc-comp-2026/blob/main/tools/validator/validate-model.py) with Z3 but getting no answer within his available time. He expressly noted he might not have invoked it correctly; this was **not a rejected model or a semantic counterexample**. The exact command, exact model and runtime configuration were not recorded in his email.
- On **6 October**, Levente said the **issues are sufficient**, that he intended to resolve them in a batch, and that opening a PR would not speed up review. Repository restructuring was also being considered.
- On **11 October**, Gidon Ernst requested exact reproduction instructions and a separate eight-model ZIP. Both were linked publicly by **12 October**. There is no later reviewer answer in issue #11 as of **31 October**.
- A source inspection of the 2025 and 2026 `validate-model.py` entry points found a change in their handling of input before the `sat` marker; it did **not** establish the reason for the different behavior with Z3.
- **2026 metadata:** the eight entries currently have `expected_verdict: true` together with `# placeholder verdict (auto-added)`. **2025 metadata:** the corresponding entries lack `expected_verdict`. Neither establishes that the eight submitted models have been officially replayed.

## Next externally actionable step

Request **one** exact 2026 reproduction command and environment (input file, model, Z3 version and timeout) from the CHC-COMP maintainers, or ask them to run the already attached smallest `standard_init2` case. If their run terminates, compare the generated validation query, solver result and hashes with the pinned author-side procedure. Do **not** submit a metadata-only PR changing 2026 placeholders to `true`—they already say `true`. Request the maintainer's preferred procedure for recording a verified 2025 post-competition verdict.

No new issue, PR or email is implied by this document; the original issue remains the single canonical discussion.
