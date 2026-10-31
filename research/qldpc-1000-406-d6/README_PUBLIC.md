# Public exact-distance certificate

The known @hirobumii code previously recorded as `[[1000,406,≤6]]` has
`d_X=d_Z=d=6` for the fixed matrices bundled here.

1. Read [`PROOF.md`](PROOF.md) for the proposed graph lemma and lower-bound argument.
2. Download the [public ZIP archive](../../MathemaSpace_D6_PUBLIC.zip). The executable verifier, frozen matrices and `results/` outputs are **inside the ZIP**, not separately present in this GitHub folder.
3. Extract the ZIP, locate `independent_check.py`, and run `python3 independent_check.py --math-only` with Python 3.10 or later from the extracted package. Review its run instructions and all dependency/input paths before use.
4. Compare `results/independent_check.json` with the frozen input SHA-256 and the claims in the proof. This package is the original author-side replay. Subsequently @hirobumii independently checked the mathematical proof, implemented its core CC-support argument in Lean and merged a formal-tier certificate in [PR #4226](https://github.com/unitaryfoundation/qldpc-challenge/pull/4226) on 30 October 2026.

No internet, additional private software, email, Drive or Colab access is intended to be needed for the packaged verification steps. This public package deliberately contains the independent
mathematical check rather than the private engine implementation.

The source quantum code and its weight-six logical operators are credited to
@hirobumii, PR #3863 in `unitaryfoundation/qldpc-challenge`.
The contribution here is the original exact-distance lower-bound proof by Henryk Soboń. The formal Lean adaptation and merged cert were authored by @hirobumii with explicit credit to Soboń for the original proof. Do not attribute the code construction or the certificate PR to Soboń, and do not claim a new code or a new worldwide mathematical theorem.

`MACHINE_HANDOFF.json` explains the representations and proof dependencies.
`WYNIK_I_PROCEDURA.md` gives the Polish report; references to full/private
reproduction files there describe the separate PRIVATE_FULL package.

This public archive is intended to exclude private research implementation and correspondence.
Keep the included Apache license and attributions with the public source input.