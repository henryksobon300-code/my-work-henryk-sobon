# A distinct [[980,398,6]] code with a smaller exact low-noise ML coefficient

Henryk Soboń · 29 October 2026

This computer-assisted proof covers two specific codes. Two implementations
reproduce the distance, logical-operator counts and decoding coefficient.
External review is pending.

## Object and attribution

The baseline is **@hirobumii's** `codes/980-398-6.json`, Git blob
`202238a380652df23d2b3b6c64265d9b1b2b0463`, from
`unitaryfoundation/qldpc-challenge` commit
`6ad5382fb23173ac91171fe472cba8aedfce74f3`.
It was merged in [PR #3867](https://github.com/unitaryfoundation/qldpc-challenge/pull/3867).
The [current catalogue certificate](https://github.com/unitaryfoundation/qldpc-challenge/blob/30953fadd41e29f83d1186976d95cddc87cfb4dd/certs/980-398-6.json) independently records the baseline distance.

The new instance is `results/candidate_980_398_6.json` in the replay package. It uses the
lifted-product construction with a different explicit choice of group actions.
The two instances have matching parameters and maximum check weight. They
differ in minimum-weight Pauli count and in the leading decoding error coefficient.

Let G = C7 semidirect C14 with inversion action. Encode (i,j) as i+7j and set

$$
(i,j)(k,l)=(i+6^j k\pmod7,\ j+l\pmod{14}).
$$

Choose A=(7,22,40) and B=(7,23,38), i.e.
A=((0,1),(1,3),(5,5)) and B=((0,1),(2,3),(3,5)).
Define L_g[t,u]=1 iff u=g*t and R_h[t,u]=1 iff u=t*h.
Set A_k=I+L_{a_k}, B_j=I+R_{b_j}, over GF(2).
There are nine VV(k,j) qubit blocks, indexed 3k+j, followed by one CC block;
each block has 98 coordinates. X-check block j has A_k on VV(k,j) and B_j
on CC. Z-check block k has B_j transposed on VV(k,j) and A_k transposed on CC.
Keep the first independent natural rows. There are 291 rows on each side.

Left and right actions commute, giving H_X H_Z^T=0. Both programs additionally
check this entry by entry, the ranks 291+291, k=980-582=398, and check weight 8.

## Finite graph conditions checked directly from the stored matrices

For BOTH codes, restore the last dependent row in each 97-row block as the
XOR of that block's rows. This gives 294 rows per side with exactly the same
row spaces as the stored matrices. The checker verifies row-space equality
and weight 8 of all restored rows; it does not assume an untested restoration.

In either syndrome sector, the 882 VV columns are edges of three separate
simple, connected, six-regular graphs on 98 vertices. Each has girth exactly 6.
A CC coordinate u has endpoints u and P_r(u) in block r. Each P_r is a
permutation consisting of seven cycles of length 14. The three permutations'
undirected edge sets are pairwise disjoint. These facts are extracted from
matrix columns, without knowing the group law or either generator triple.

The total shortest VV path cost of one CC coordinate, summed over the three
blocks, has minimum **5 for the baseline** in both sectors and **7 for the new
code** in both sectors. Its maximum is 9 in all four cases. Every vertex's
cost is computed using all-pairs breadth-first graph distances.

## Complete classification through weight six

Consider a nonzero zero-syndrome binary support. Let t be its CC size and s its
VV size, with t+s<=6. In block r its VV edges must have boundary
T symmetric_difference P_r(T), where T is the selected CC set.

For 1<=t<=6 this boundary cannot be empty: an invariant nonempty set for a
permutation with 14-cycles has size at least 14. Therefore every block needs
at least one VV edge.

* t=0: an even nonempty edge subgraph contains a cycle. Girth 6 means s>=6;
  equality is exactly one simple VV six-cycle in one block.
* t=1: the total VV cost is at least 5 (baseline) or 7 (new code). Thus there
  is no total weight below 6. In the baseline, weight 6 is possible precisely
  at coordinates of cost 5, using a shortest endpoint path in each block.
  With total s=5 and at least one edge in each block, no path is longer than
  3; there is no room for any extra cycle. Enumerating all three-path products
  exhausts this family. The new code has no member of this family.
* t=2: s<=4 across three nonempty blocks, so at least two blocks have one
  VV edge. Boundary size 2 implies |T intersection P_r(T)|=1. The two points
  of T must therefore be an undirected P_r edge for each such block, contrary
  to pairwise disjointness of the action edge sets.
* t=3: s<=3 forces one VV edge in all three blocks. Boundary size 2 implies
  |T intersection P_r(T)|=2. Since no permutation has a cycle of size <=6,
  these are two distinct undirected action edges on T. Two such permutations
  already require four disjoint edges on three vertices, which have only
  three possible pairs. Contradiction.
* t=4 or 5: s<=2 while all three blocks require an edge. Contradiction.
* t=6: s=0 would require a nonempty invariant six-point set. Contradiction.

This exhausts all supports of weight at most six, not a random sample.
In particular no nonzero kernel word of weight <=5 exists. At weight 6 the
only possibilities are VV six-cycles and the specified one-CC family.

Both programs enumerate these supports and check every one is outside its
own stabilizer row space, using opposite GF(2) pivot conventions. The counts:

| Code/sector | VV six-cycles | One-CC supports | Total pure logical supports |
|---|---:|---:|---:|
| Baseline X | 9555 | 21 | 9576 |
| Baseline Z | 10437 | 14 | 10451 |
| New X | 9555 | 0 | 9555 |
| New Z | 9555 | 0 | 9555 |

The X and Z six-support sets have empty intersection in each code. A mixed
Pauli of physical weight <=6 would have two nonzero binary components in the
respective kernels. Each component has weight >=6, so at physical weight 6
both would have the same six-support, contrary to that intersection check.
Thus all minimum Paulis are pure, and there is no nonidentity stabilizer of
physical weight <=6. In particular **d_X=d_Z=d=6 exactly** for both inputs.

The total numbers of minimum nontrivial Pauli operators (ignoring phase, not
quotienting their supports into logical cosets) are **20027 and 19110**.
A product of single-qubit Clifford transformations and a qubit permutation
preserves Pauli weight and maps the centralizer and stabilizer bijectively.
It preserves this count. Its inequality proves the new code is inequivalent
to the baseline under this equivalence, including permutations and X/Z swap.

## Exact ambiguity counts and the noise statement

Use independent depolarizing noise: every qubit is I with probability 1-p and
each of X,Y,Z with probability p/3. Syndrome measurements are perfect, with
one code block and optimal syndrome-based Pauli recovery modulo stabilizers.

Two distinct weight-three errors with equal syndrome differ by a nonzero
centralizing Pauli of weight <=6. The classification forces physical weight
6 and a pure X or pure Z logical. Their supports are disjoint, so both errors
are pure of that same type and are complementary three-subsets of a listed
six-support. This proves the half-support enumeration covers every ambiguity,
including mixed-Pauli triples by exclusion, and not merely selected examples.
No two such errors are stabilizer-equivalent, since there is no nonidentity
stabilizer through weight six. No weight-three error competes with a weight
<=2 error, because the difference would be a nonzero kernel element of
weight <=5.

Group all halves by their ACTUAL stored-check syndrome. A class of size r
has r equally probable, distinct logical alternatives, so every decoder loses
at least r-1. Counting pairs r(r-1)/2 would be incorrect for classes above 2.

| Class size r | Baseline X classes | Baseline Z classes | New X classes | New Z classes |
|---:|---:|---:|---:|---:|
| 2 | 67074 | 74060 | 66885 | 66885 |
| 3 | 3521 | 1771 | 3528 | 3528 |
| 4 | 2653 | 3087 | 2646 | 2646 |
| 6 | 147 | 441 | 147 | 147 |
| Ambiguous patterns | 156205 | 168427 | 155820 | 155820 |
| Ambiguous syndromes | 73395 | 79359 | 73206 | 73206 |
| Unavoidable failures | 82810 | 89068 | 82614 | 82614 |

The X and Z classes cannot overlap in full Pauli syndrome: their opposite
components vanish, and an overlap would imply a weight-three kernel word.
Therefore the total unavoidable weight-three counts are 171878 and 165228.
For this fixed finite code the optimal block failure probabilities satisfy

$$
P_{\rm old}(p)=\frac{171878}{27}p^3+O(p^4),\qquad
P_{\rm new}(p)=\frac{165228}{27}p^3+O(p^4).
$$

The relative leading-coefficient reduction is exactly

$$
\frac{171878-165228}{171878}=\frac{475}{12277}
\approx 3.869023377\%.
$$

For every p in [0,1], every syndrome decoder also has the finite-p lower
bound F*(p/3)^3*(1-p)^977, with F=171878 or 165228 respectively. This bound
counts unavoidable failures, not a fixed list of error patterns that defeat
every possible decoder. The asymptotic coefficient follows because ML can
correct one leading logical alternative per syndrome, and higher-weight
events contribute O(p^4). A smaller leading coefficient implies an improvement
for sufficiently small positive p, but gives no numerical crossover p here.
There is no claim of improvement at all p, of a threshold, of circuit-level
performance, or of a practical decoder's performance.

## Reproducibility and error correction during the investigation

The producer builds the new matrices from G,A,B and enumerates cycles by DFS.
For one-CC words it enumerates all simple paths of lengths up to 3 and retains
products of total length 5. It groups all resulting half-support syndromes.

The independent checker imports neither the producer nor an engine nor its
cycle lists. It reads only the two stored check matrices. It uses low-pivot
elimination, pairs length-three paths to enumerate six-cycles, and obtains
one-CC words from all shortest paths using distance-decreasing recursion.
It additionally enumerates **all 4192244 three-edge subsets** of a representative
graph in each of four sectors, totaling **16768976** subsets. All three copies
of each graph are checked equal. This cross-check recovers the pure-cycle
histograms without using cycle halves; the separately classified one-CC
family is then included and every collision is verified to be a listed logical.

The first cycle-only comparison omitted the baseline's 35 one-CC supports
and gave F=171549, with 19992 operators. That was an incomplete comparison,
not the final result. The independent checker rejected its stronger one-CC
assumption; both implementations were corrected to include the missing
family. The obsolete reduction 3.68466% must not be used. The corrected
values are F=171878 and 20027 operators, agreeing in both implementations.

To reproduce the comparison, run `python3 replay.py` after extracting the public replay ZIP.
Python 3.10 or later and the standard library suffice. The replay rejects a
modified check support, a wrong dimension and a forged failure count.

## Prior work and novelty boundary

Established ingredients include lifted products and nonabelian constructions
([Panteleev–Kalachev](https://arxiv.org/abs/2111.03654)); group-algebra products
and distance bounds ([Bhardwaj et al., Appendix G](https://arxiv.org/html/2607.28795v2));
and analytical use of low-weight multiplicities and ML error estimates.
[Mahdavifar](https://arxiv.org/abs/2609.01181) discusses low-weight logical
multiplicities and ML expressions for erasure in FDPC-based codes. This
comparison uses independent depolarizing noise and perfect syndrome readout.
Its inequivalence and error claims concern the two specified matrices.
