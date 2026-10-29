# Finite certificates for 26 infinite families of BLR determinants

I am sharing a reproducible candidate partial result for the positivity problem studied by Bellemare, Langlois and Ransford, related to the Nyman–Báez-Duarte approach. The stated scope is **every integer j from 3 through 28, and every integer k >= j**. This is *not* a proof of the full positivity conjecture or of the Riemann hypothesis. I have not established worldwide priority, and the argument has not been externally refereed.

The work combines an analytical tail bound with exact finite certificates. The two implementations were designed to check the certificate separately; the recorded runs report **26/26 rows passing** and **4,129 finite checks**. These software checks do not replace a mathematical review of the reductions and assumptions.

## Read and reproduce

- [Mathematical argument and scope](NB_GENERAL_CERTIFICATE_PROOF.md)
- [The j=3 argument](NB_J3_PROOF.md) and [the j=4 argument](NB_J4_PROOF.md)
- [Frozen certificate (JSON)](INFINITE_ROWS_CERTIFICATE.json)
- [Primary certificate generator](certify_infinite_rows.py)
- [Separate checker](check_infinite_rows_independent.py), using [C++17 Gram-sum helper](independent_gram_sums.cpp)
- [Independent verification result](INFINITE_ROWS_INDEPENDENT_CHECK.json) and [recorded run](INDEPENDENT_ROWS.log)
- [Prior-work and novelty notes](NOVELTY_AND_SOURCES.json)
- [Where an attempted extension fails](EXTENSION_FAILURE_29_56.json)

From a checkout of this directory, run:

```sh
python3 certify_infinite_rows.py --max-j 28
python3 check_infinite_rows_independent.py
```

Requirements: Python 3 standard library, and a C++17 compiler (g++) for the separate checker. The scripts write output files in the current directory; use a fresh working copy if you want to preserve the frozen results.

**Requested review:** I would welcome identification of a previously published proof covering these same cases, or a counterexample to any particular lemma or certificate bound. Please distinguish the all-k claim from a finite enumeration and compare the exact quantified statement. This is a research contribution for inspection, not a claim of a globally new theorem.

The proprietary MathemaSpace engine and private correspondence are not included.
