# Public exact-distance certificate

The known @hirobumii code previously recorded as `[[1000,406,≤6]]` has
`d_X=d_Z=d=6` for the fixed matrices bundled here.

1. Read [`PROOF.md`](PROOF.md) for the proposed graph lemma and lower-bound argument.
2. Download the [public ZIP archive](../../MathemaSpace_D6_PUBLIC.zip). The executable verifier, frozen matrices and `results/` outputs are **inside the ZIP**, not separately present in this GitHub folder.
3. Extract the ZIP, locate `independent_check.py`, and run `python3 independent_check.py --math-only` with Python 3.10 or later from the extracted package. Review its run instructions and all dependency/input paths before use.
4. Compare `results/independent_check.json` with the frozen input SHA-256 and the claims in the proof. Independent third-party replay of this package has not been established here.

No internet, additional private software, email, Drive or Colab access is intended to be needed for the packaged verification steps. This public package deliberately contains the independent
mathematical check rather than the private engine implementation.

The source quantum code and its weight-six logical operators are credited to
@hirobumii, PR #3863 in `unitaryfoundation/qldpc-challenge`.
The contribution here is an explicit lower certificate. Worldwide novelty,
external peer review and a board-earned exact tier are not established.

`MACHINE_HANDOFF.json` explains the representations and proof dependencies.
`WYNIK_I_PROCEDURA.md` gives the Polish report; references to full/private
reproduction files there describe the separate PRIVATE_FULL package.

This public archive is intended to exclude private research implementation and correspondence.
Keep the included Apache license and attributions with the public source input.