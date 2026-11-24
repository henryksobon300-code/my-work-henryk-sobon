# SciPy PR #26747 — local source-level before/after replay (2026-11-24)

**Status:** author-side regression evidence only. **Not** a SciPy maintainer approval, full Meson build, or a claim that all upstream CI passes.

Issue: https://github.com/scipy/scipy/issues/26549  
PR: https://github.com/scipy/scipy/pull/26747

## Exact sources under test

These SHA-1 values are **Git blob hashes**, independently checked against the files exposed by GitHub (not arbitrary local filenames):

| Version | Git commit | File | Git blob SHA-1 |
|---|---|---|---|
| Base | `866295b15d5e74cc93e5409c89d845068a055aa2` | `scipy/sparse/csgraph/_laplacian.py` | `762158e0d86ff92293a9f181b1ad444bd02706c9` |
| PR head | `75de827187fd48874ee2e5d9519fdd2ed9f79fd1` | `scipy/sparse/csgraph/_laplacian.py` | `697927a5773331288a303564da9eee903b992a87` |
| PR head | same | `scipy/sparse/csgraph/tests/test_graph_laplacian.py` | `749dd0e37636e84b64789d11073b8111f93e924c` |

The regression test source and both implementation versions were matched by SHA-1 to these exact blobs. The test file is already part of the PR, not a newly proposed test module.

## Results reproduced in this audit

Python 3.13.5; NumPy 2.3.5; installed SciPy 1.17.0 helper/runtime modules; pytest 9.0.2. Exact GitHub `_laplacian.py` source loaded with `importlib` and injected as `scipy.sparse.csgraph.laplacian` while running tests from the exact PR test file.

| Run | Pass | Fail | Other |
|---|---:|---:|---|
| 67 targeted regression cases using **base** source | 18 | **49** | 1,126 pre-existing cases deselected |
| Same 67 cases using **PR head** source | **67** | 0 | targeted selection |
| Entire current PR `test_graph_laplacian.py`, using **PR head** source | **1,193** | 0 | local source-level test, not full project CI |

### Minimal failure and its fix

```python
import numpy as np
from scipy.sparse.csgraph import laplacian

graph = np.array([[0, 100, 100], [100, 0, 0], [100, 0, 0]], dtype=np.int8)
print(laplacian(graph, dtype=np.int64)[0, 0])
```

The **base** implementation returns `-56` due to an `int8` intermediate overflow; the PR implementation returns the correct `200`. Both outputs were reproduced directly using the corresponding GitHub-source implementation. The PR promotes the graph's working dtype **before** arithmetic when the requested dtype can safely represent all input values.

### How to reproduce

1. Obtain `_laplacian.py` from the **base commit** and the **PR-head commit**, and `test_graph_laplacian.py` from the PR head; check their Git blob SHA-1 hashes against the table above.
2. In a Python environment with SciPy and pytest available, load the chosen source using `importlib.util.spec_from_file_location` and temporarily set `scipy.sparse.csgraph.laplacian = loaded_module.laplacian`.
3. Run `python -m pytest test_graph_laplacian.py -q` with the PR-head implementation (1,193 passing in this local replay).
4. Run `python -m pytest test_graph_laplacian.py -q -k 'requested_wide_dtype or wide_dtype_product or normalized_unsigned or copy_false_preserves'` with the base source; compare its 49 failures to the zero targeted failures from the PR-head source.

All three sources were verified with `git hash-object` before the local run. Full upstream `spin test` and human reviewer verification remain separate outstanding steps. No private MathemaSpace implementation or unpublished research materials are included.

**AI assistance disclosure:** ChatGPT assisted with reproducing the source-level check and writing this record. The upstream pull request remains an open **draft** requiring human review.
