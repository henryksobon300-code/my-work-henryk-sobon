# SYNTCOMP 2026 — parity-realizability: public contribution record

**Author:** Henryk Soboń (GitHub: @henryksobon300-code)  
**Record created:** 2026-10-10  
**Status:** Author-reported computational results; independent competition evaluation pending.  
**Scope:** Evidence and attribution record only. **No private solver source, private container, or unpublished algorithm is released here.**

## What was investigated

The 2026 parity-realizability track included a frozen 483-instance set. In the author's archived analysis, the union of published configurations had recorded outcomes for 478 instances, leaving five without a recorded virtual-best verdict:

| Benchmark | Author-reported verdict |
| --- | --- |
| `aut3` | UNREALIZABLE |
| `aut3.2` | UNREALIZABLE |
| `aut4` | UNREALIZABLE |
| `steadygame_pb_12_pe_` | UNREALIZABLE |
| `test3` | UNREALIZABLE |

The author reported five successful independent certificate replays for these five instances. Four intentionally damaged certificate controls were reported rejected. These counts describe the author's test artifacts, **not an official SYNTCOMP result**.

## Independently checkable witness work

For `steadygame_pb_12_pe_`, the author prepared a nine-state environment-forced-cycle argument, checked an original eHOA witness against controller choices, and used Knor/Oink for an additional parity-game validation path. The organizer acknowledged learning the status of this benchmark in correspondence dated 2026-09-29. This acknowledgement should **not** be interpreted as an official solver ranking, competition submission acceptance, or validation of every other benchmark.

## Full-solver submission context

In correspondence on 2026-09-30, the author reported a general parity-realizability solver V6, including an author-side frozen-set run of 458/483 decided instances (296 REALIZABLE, 162 UNREALIZABLE, 25 abstentions), and a private Docker image for potential organizer testing. Separate later author-side runs and five-instance certificates were also reported. These runs have different scopes and should not be combined into a single competition score.

The organizer indicated willingness to test a solver when resources allow. **No independently run competition score or official acceptance is claimed here.** The private image identifier, credentials, source code, and proprietary engine details are intentionally omitted.

## Evidence boundaries and next steps

- Original benchmark names and reported verdicts are recorded above for precise attribution.
- The full original certificate bundles, replay logs, versioned source artifacts, and SHA-256 manifests should be attached or linked only after an artifact-by-artifact privacy and integrity review.
- The author-side reports are not equivalent to an independently verified official competition outcome.
- This page records *public disclosure of these claims* on 2026-10-10; it does not establish that the underlying methods are novel, patentable, or exclusive.
- No request is made here for maintainers or organizers to change results without independent checks.

**Related project:** SYNTCOMP 2026 parity-realizability.  
**Author contact:** via this GitHub account.

---
This record is deliberately separated from the private `Mathemaspace` repository and contains no private solver implementation.
