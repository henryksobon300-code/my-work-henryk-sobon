# NetworkX #8964 — review candidate: precision and partition invariants
Date: 2026-11-24. Status: **local review candidate, NOT merged or upstream-CI verified**.

## Scope
The reported false-negative spanning-arborescence exception (#8964) stems from a weight-shift heuristic that can prefer a non-spanning branching. Further checks revealed two distinct requirements that must not be silently lost:

1. **Numerical fidelity:** a transformed weight should not become non-invertible because of finite-precision addition/subtraction. This affects e.g. `1e308`, `-1e308`, and `1e-300`; original graph weights and return values must be preserved.
2. **Partition fidelity:** an edge tagged `EdgePartition.INCLUDED` must occur in the final tree, and `EXCLUDED` edges must not. Checking only `is_arborescence` and total weight is insufficient. A cycle contraction can otherwise replace an included edge with an outside entrance.

## Minimal regression — mandatory edge
```python
import networkx as nx
from fractions import Fraction

G = nx.DiGraph()
edges = [
    (0, 1, 1e-300), (0, 2, Fraction(1, 3)),
    (1, 0, -1), (1, 2, 12),
    (2, 1, 0), (2, 0, 12),
]
for u, v, w in edges:
    G.add_edge(
        u, v, weight=w,
        part=(nx.EdgePartition.INCLUDED if (u, v) == (0, 2)
              else nx.EdgePartition.OPEN),
    )
T = nx.maximum_spanning_arborescence(
    G, partition="part", preserve_attrs=True
)
assert nx.is_arborescence(T)
assert T.has_edge(0, 2)  # Mandatory edge
```

## Minimal regression — numerical fidelity
```python
import networkx as nx

def path(w):
    G = nx.DiGraph()
    G.add_weighted_edges_from([(0, 1, w), (1, 2, w)])
    return G

assert nx.is_arborescence(nx.minimum_spanning_arborescence(path(1e308)))
assert nx.is_arborescence(nx.maximum_spanning_arborescence(path(-1e308)))
G = path(1e-300)
T = nx.minimum_spanning_arborescence(G)
assert G[0][1]["weight"] == 1e-300
assert T[0][1]["weight"] == 1e-300
```

## Candidate method and evidence
A local candidate uses an exact `Fraction`-based cardinality-first objective on an input-graph copy, restores original weight values and types, and prevents a contracted cycle from dropping a mandatory edge. It is a proposal for review, not a guarantee of universal correctness.

Reproduced locally on NetworkX **3.6.1**, Python 3.13:
- 64/64 module tests passed (original plus added regression cases).
- 1,184 directed-graph partition checks: 902 feasible matched the independent exhaustive oracle; 282 infeasible were rejected.
- 2,400 multi-digraph min/max checks: no reported discrepancy against the independent brute-force oracle, including infeasible instances.
- 1,280 additional exclusion-only checks: 956 feasible, 324 correctly rejected.
- The proposed combined patch applies cleanly to a pristine NetworkX 3.6.1 copy; local patched files match the candidate byte-for-byte.

**Limitations:** no complete upstream `networkx/main` CI run, no maintainer acceptance or merge, and no claim of exhaustive correctness for arbitrary numeric objects. Applying the patch to the current upstream branch and an independent review are still needed.

Related public discussion: https://github.com/networkx/networkx/issues/8964 and https://github.com/networkx/networkx/pull/8979.

This note does **not** publish any private MathemaSpace implementation. It documents independent regression checks and constraints on a proposed NetworkX change.
