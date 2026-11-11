# Exact distance of the frozen [[1000,406,≤6]] lifted-product instance

Research date: 2026-10-28. The underlying code is due to **@hirobumii**, not to this investigation. The code and its weight-six witnesses were published in PR #3863, merged 2026-10-18. This note supplies the original explicit lower-bound argument for the fixed matrices. No claim of worldwide priority is made.

**Status update (30 October 2026):** @hirobumii independently checked Henryk Soboń's proof, formalized its CC-support analysis in Lean and merged a formal exact-distance certificate in [unitaryfoundation/qldpc-challenge PR #4226](https://github.com/unitaryfoundation/qldpc-challenge/pull/4226). The source code construction and formal PR belong to @hirobumii; Soboń is credited as the author of this original exact-distance proof. The following sections retain the original 28 October mathematical argument and replay procedure.

## 1. Fixed object and claim

Repository: `unitaryfoundation/qldpc-challenge`.

- Commit: `9587d1aa54e98aa49caacf4a2cb358424e70160e`.
- Path: `codes/1000-406-6.json`.
- Git blob: `1492412cf38995f2d0d9507ad0402a260a28b3fb`.
- SHA-256 of the exact 49,594-byte input: `fdc1e71bfd9a588b39f545882a93b5b316582ecdd157451bd03c7411219b842b`.

**Claim.** For these matrices, in the usual binary CSS stabilizer model, `d_X=d_Z=d=6`. This is an exact mathematical statement about the stored instance, not an estimate from random error samples. It does not establish circuit-level distance, a decoding threshold, or a new asymptotically good code family.

The stored file has 297 independent X rows and 297 independent Z rows on 1000 qubits. Both programs independently establish rank 297 in each sector, mutual orthogonality, and therefore `k=1000−297−297=406`.

## 2. Expanded construction and row-space identification

Let `G` consist of pairs `(i,j)∈Z_5×Z_20`, encoded as `i+5j`, with

\[
(i,j)(k,l)=(i+2^j k\pmod5,\;j+l\pmod{20}).
\]

This defines a group because `2^20=1 mod 5`. The phase map `π(i,j)=j` is a homomorphism to `Z_20`. Put

\[
(a_0,a_1,a_2)=((0,1),(1,1),(1,7)),\quad
(b_0,b_1,b_2)=((0,1),(1,3),(4,3)).
\]

With `[L_g]_{t,u}=1` iff `u=gt` and `[R_h]_{t,u}=1` iff `u=th`, use `A_k=I+L_{a_k}`, `B_j=I+R_{b_j}` over `F_2`.

There are nine VV qubit blocks `(k,j)`, each indexed by `u∈G`, followed by one CC block indexed by `u∈G`. The VV qubit index is `100(3k+j)+u`; the CC index is `900+u`.

The full X syndrome has three blocks `j`, with `A_k` on VV(k,j) and `B_j` on CC. The full Z syndrome has three blocks `k`, with `B_j^T` on VV(k,j) and `A_k^T` on CC. Each full matrix has 300 rows.

The adapter reconstructs the full matrices, selects the first independent rows in their original order, and obtains **exactly** the 297 stored rows in each sector, including row order. The independent checker instead constructs sparse columns and proves row-space inclusion in both directions using elimination with the opposite pivot convention. Thus deleting the three redundant rows preserves the kernel. The proof below is applied to the full 300-row presentation and therefore applies to the stored matrices.

## 3. A finite graph lemma

Consider any binary syndrome matrix partitioned into three syndrome blocks. Suppose its columns have the following structure:

1. Each VV column is the incidence vector of one edge in a simple undirected graph within a single syndrome block. Each of the three graphs has girth at least six. The VV columns correspond injectively to edges: there are no duplicate edge columns.
2. A CC column indexed by `u` has, in each block `r`, boundary `{u,P_r(u)}`, where `P_r` is a permutation whose every cycle has length greater than five.
3. For every `u`, the sum over the three blocks of the graph distances from `u` to `P_r(u)` is at least five.
4. No two-element set `T={u,v}` has `|T Δ P_r(T)|=2` simultaneously for all three blocks.

Then the kernel of this syndrome matrix contains no nonzero vector of Hamming weight at most five.

**Proof.** Let `T` be the selected CC coordinates, `t=|T|`, and let `s` be the number of selected VV columns. Suppose `s+t≤5` and the syndrome vanishes. In each block the VV edge set has boundary `T Δ P_r(T)`.

**Case t=0.** Every VV edge set has even degree at every vertex. If any selected edge exists, its finite even-degree subgraph contains a cycle. Simplicity and injectivity exclude loops and parallel-edge two-cycles; girth at least six then requires at least six selected edges. This contradicts `s≤5`.

**Case t=1.** Each of the three blocks has exactly two boundary vertices. A finite edge set with precisely these two odd-degree vertices contains a path connecting them. In block `r` at least `dist(u,P_r(u))` VV edges are therefore needed. The blocks use disjoint VV coordinates, so `s≥5`. Consequently `s+t≥6`, a contradiction.

**Case t=2.** A set invariant under a permutation is a union of its cycles. All permutation cycles have length greater than five, so the nonempty two-element set is not invariant in any block. Each block has nonzero boundary and needs at least one VV edge. Since `s≤3`, exactly one VV edge must occur in each block. The boundary of one edge has exactly two vertices. This would give `|T Δ P_r(T)|=2` in all three blocks, excluded by assumption 4.

**Cases t=3,4,5.** The same cycle-length argument shows that no such nonempty `T` is invariant under any `P_r`. All three blocks need a VV edge. Hence `s+t≥3+t≥6`, again a contradiction. These cases exhaust all nonzero supports of total weight at most five. QED.

Notice that this lemma excludes *all* small kernel vectors, not just small nontrivial logical operators. No stabilizer-equivalence approximation is used for the lower bound.

## 4. Verification of the lemma's hypotheses

For the X-check syndrome, a VV column `(k,j,u)` has endpoints `u,a_k^{-1}u` in block `j`; a CC column `u` has endpoints `u,ub_j^{-1}` in block `j`.

For the Z-check syndrome, a VV column `(k,j,u)` has endpoints `u,ub_j` in block `k`; a CC column `u` has endpoints `u,a_ku` in block `k`.

All six group elements `a_k,b_j` have order 20. Their left and right actions are free, so every CC permutation consists of five cycles of length 20. This proves hypothesis 2 and the noninvariance fact used in cases `t≥2`.

In either VV graph, the six signed generators are distinct and none is the identity. There are therefore no duplicate edges across generator labels and no loops. The graphs are six-regular. The producer computes their girth by BFS from every vertex and obtains six. The independent checker derives all six block graphs directly from the sparse columns, verifies bipartiteness, and verifies that distinct vertices have at most one common neighbor. These two conditions exclude all cycles of lengths three, four, and five. They establish hypothesis 1 without relying on the producer's BFS routine. The graphs here are **VV incidence graphs on 100 vertices**, not the full CSS Tanner graphs; the latter have reported girth four. These are different graphs, so there is no contradiction.

For hypothesis 4 one can reason algebraically: `|{u,v} Δ P_r({u,v})|=2` means that `u` and `v` are adjacent along that permutation's 20-cycle. Simultaneous adjacency for all three distinct signed generators is impossible. Independently, the checker exhausts all `binom(100,2)=4950` CC pairs in each sector and finds zero pairs satisfying all three size-two conditions.

### Independent one-CC graph-distance check

For the one-CC case, the lower bound can be established using only the publicly specified finite graphs. The independent checker builds the 100-vertex VV incidence graphs from the sparse check matrices and computes all-pairs shortest-path distances. For the possible CC displacements, its reported minimum required VV path-cost sum is seven in each sector, exceeding the budget available to an operator of total weight at most five.

This finite graph-distance check is sufficient for hypothesis 3 and does not depend on any proprietary research engine, abstraction implementation or private intermediate state. The public result concerns this fixed mathematical instance; it makes no claim about the novelty, generality, speed or necessity of the research tooling used during its discovery.

## 5. From the lower bound to exact quantum distance

The lemma applies to both full check matrices, hence neither kernel has a nonzero vector of weight at most five. A Pauli operator of physical support at most five has binary X and Z components each of weight at most five. To commute with all stabilizers these components must belong to the relevant kernels; both must therefore be zero. This proves `d_X,d_Z≥6`.

The frozen input supplies:

- X logical support `{0,5,95,110,195,213}`.
- Z logical support `{0,5,7,10,301,310}`.

Both implementations verify that each has weight six, has zero syndrome against the opposite check sector, and lies outside its own stabilizer row space. These are valid logical operators and prove `d_X,d_Z≤6`. Combining the bounds gives **`d_X=d_Z=d=6`**.

## 6. Reproduction and trust boundary

Private/full package:

```sh
python3 reproduce.py
python3 independent_check.py
```

Public mathematical package, which contains no original MathemaSpace engine source:

```sh
python3 independent_check.py --math-only
```

Use Python 3.10 or later. There are no pip packages, credentials, network calls, stochastic seeds, time limits, or solvers in these computations. Run the adapter normally, without Python's `-O` option, because its checks use assertions. The independent checker uses explicit exceptions and also runs with `python3 -O`.

The finite programs check all hypotheses of the lemma and the linear algebra. The four-case proof above was originally written as a human-readable mathematical argument, not as a Lean/Coq proof object. The independent implementation within this original package was written in the same investigation. Subsequent independent checking and Lean formalization are documented in PR #4226. Corrupting a bridge transition or replacing a CC permutation by the identity is rejected by the included negative controls.

**Historical note:** On 28 October this result had no board-earned exact tier. That status changed on 30 October with merged [formal certificate PR #4226](https://github.com/unitaryfoundation/qldpc-challenge/pull/4226). The result does not supply a new quantum code, a new Pareto point, or a solution to every question raised by issue #4162.