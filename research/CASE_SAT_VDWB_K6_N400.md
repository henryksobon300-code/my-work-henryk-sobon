# SAT Competition 2026 — vdwb_k6_n400: SAT witness and upstream status

**Status checked: 11 November 2026.**  
**Contributor:** Henryk Soboń.  
[Back to results index](RESULTS_INDEX.md) · [Research website](https://henryksobon300-code.github.io/my-work-henryk-sobon/projects.html)

## The narrow result

The publicly submitted evidence concerns **one fixed benchmark**:

- Benchmark: `vdwb_k6_n400.sanitized.cnf.xz`.
- GBD benchmark ID: `0757e47d262b75171c0040987e6d20ce`.
- Original verdict in the report: `unknown`.
- Proposed verdict: `sat`.
- A complete assignment of **400 Boolean variables** was published in the original issue's evidence package.
- The author-supplied independent checker reports `PASS: 31600/31600 clauses satisfied` against the original sanitized instance.
- A negative control, flipping variable 2, reports `REJECT: clause 12954 is unsatisfied`.

A full satisfying assignment, if it independently checks against the correctly identified original CNF, is sufficient to prove **SAT for that specific instance**. It does not prove a new value of the van der Waerden number W(2,6) or establish that every leading solver previously failed.

## Inspect the original evidence

1. [SAT Competition issue #2 — original claim, public evidence ZIP, witness, checker, corrupted negative control and SHA-256](https://github.com/satcompetition/2026/issues/2).
2. [GBD PR #3 — proposed `unknown` → `sat` database correction and timeline](https://github.com/Udopia/gbd-data/pull/3).
3. [Exact PR file diff — a single `cnf/meta.db` metadata change](https://github.com/Udopia/gbd-data/pull/3/files).

The public ZIP checksum **reported in the source issue** is:
`c745abd9f5cd28de07d887fc42de10d3d0a53b217f7be8fefea17bb4148c2b87`.

## What happened on 11 November 2026?

The owner `Udopia` **closed PR #3 without merging it** at **08:07:56 UTC**. The automatic GitHub e-mail said `Closed #3`. The checked PR had no maintainer acceptance review and no explanatory comment; its changed file was a single database verdict.

**Therefore:**
- The recorded author-side SAT witness and negative control remain publicly available.
- The proposed change was **not merged**; this is **not an officially accepted database correction**.
- The SAT Competition original issue #2 was still **open** at this status check.
- The GitHub close event neither independently validates nor disproves the SAT witness.

## Reproducibility and claim boundary

The original issue links to the public input CNF, full assignment, independent verifier, negative control, replay script and provenance. These are the correct materials for third-party verification; the private search engine is not necessary for verifying a SAT witness.

**This portfolio status review did not independently rerun the attached proof ZIP** and does not certify its output. It records the existing public author-side result and the verifiable upstream status separately.

**Credit and scope:** Henryk Soboń reported the specific witness and submitted the proposed metadata change. No claim of an upstream merge, of a new general-purpose SAT algorithm, or of solving a broader open mathematical conjecture is made.
