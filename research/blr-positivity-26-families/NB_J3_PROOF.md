# A weighted comparison proving the j = 3 positivity case

Date: 27 October 2026. Status: analytical proof with separate computational checks;
candidate partial contribution, global priority not established. No external
mathematician or formal proof assistant has reviewed this note.

## Precise scope and source

Bellemare, Langlois and Ransford, *A positivity conjecture related to the Riemann
zeta function*, American Mathematical Monthly 126 (2019), 891–904;
[author preprint](https://arxiv.org/abs/2011.02847), Conjectures 2 and 9,
ask for positivity of certain Gram minors, equivalently of the coefficients
obtained by Gram–Schmidt in the natural integer order. The definitions below
are theirs. The weighted comparison and matching proof below were derived in
this investigation. A literature search did not locate this specific argument;
that does not prove it has never appeared elsewhere.

This note proves the case j = 3 for every integer k >= 3. It does not settle
the cases j >= 4, the whole positivity conjecture, or the Riemann hypothesis.
The source paper itself does not assert that its positivity conjecture implies
the Riemann hypothesis.

## Definitions

For k >= 2 set

\[
 f_k(x)=\frac1k\lfloor1/x\rfloor-\lfloor1/(kx)\rfloor,
 \qquad 0<x\le1.
\]

On the interval (1/(r+1),1/r] this is (r mod k)/k. Consequently

\[
 P_{jk}=\langle f_j,f_k\rangle
 =\sum_{r\ge1}\frac{(r\bmod j)(r\bmod k)}{jk\,r(r+1)}.
\]

Write u_k(r)=(r mod k)/k. For any strictly decreasing positive summable
sequence w=(w_r), define

\[
 P^w_{jk}=\sum_{r\ge1}w_r u_j(r)u_k(r),
 \qquad g(r)=u_3(r)-\tfrac23u_2(r).
\]

All series used below converge absolutely because the u_k and g are bounded.
The original inner product corresponds to w_r=1/[r(r+1)].

## Lemma 1: a comparison for all k >= 3 and all such weights

\[
 \sum_{r\ge1} w_r g(r)u_k(r)>0.
\]

In fact it is at least (4w_2-3w_3)/(3k), a strictly positive quantity.

**Proof.** In residue order 0,1,2,3,4,5 modulo 6, the values of g are

\[
 (0,\ 0,\ 2/3,\ -1/3,\ 1/3,\ 1/3).
\]

Thus a negative summand can occur only at r=6q+3. Put a=r mod k.

* If a=0, that summand is zero.
* If a>=2, assign to it the earlier positive index s=r-1. Its remainder
  is a-1 and g(s)=2/3. The positive term minus the magnitude of the negative
  term equals
  \[
   \frac{2(a-1)w_{r-1}-a w_r}{3k}>0,
  \]
  since 2(a-1)>=a and w_{r-1}>w_r.
* If a=1, necessarily k>=4: every negative index r is divisible by 3, so
  k=3 cannot occur in this case. Also r cannot be 3, because 3 mod k is
  either 0 or 3 for k>=3; hence r>=9. Assign s=r-4>=5. Then s is 5 modulo
  6, g(s)=1/3, and s mod k=k-3>=1. The positive term minus the negative
  magnitude equals
  \[
   \frac{(k-3)w_{r-4}-w_r}{3k}>0.
  \]

The assignments never reuse a positive term: indices of the first type are
2 modulo 6, indices of the second type are 5 modulo 6, and each assignment
is injective within its type. All unassigned terms are nonnegative. Therefore
the regrouping proves nonnegativity and is legitimate by absolute convergence.

For k>=4 the pair r=3, s=2 alone contributes
(4w_2-3w_3)/(3k)>0. For k=3 the negative term at r=3 vanishes and the
unassigned term r=2 contributes 4w_2/9, which exceeds the stated bound
(4w_2-3w_3)/9. This proves both strictness and the quantitative bound. QED.

## Lemma 2: the projection coefficient is below 2/3

Let a_w=P^w_{23}/P^w_{22}. Then a_w<2/3. Indeed, only odd r contribute
to the inner product of g with u_2, so

\[
 \langle g,u_2\rangle_w
 =\tfrac16\sum_{q\ge0}(w_{6q+5}-w_{6q+3})<0.
\]

Also P^w_{22}>0. More explicitly,
delta_w=(2/3)P^w_{22}-P^w_{23}>(w_3-w_5)/6>0,
because the q=0 contribution already gives (w_3-w_5)/6 and all later
contributions are positive.

## Theorem: the whole second nontrivial Gram–Schmidt column is positive

For every integer k>=3,

\[
 D^w_{3k}:=P^w_{22}P^w_{3k}-P^w_{23}P^w_{2k}>0.
\]

**Proof.** The unnormalized third Gram–Schmidt vector is
h_3=u_3-a_w u_2. It is nonzero (its values at r=1 and r=2 cannot both
vanish). Since a_w<2/3,

\[
 \langle h_3,u_k\rangle_w
 =\langle g,u_k\rangle_w+(2/3-a_w)P^w_{2k}>0.
\]

Both P^w_{22} and the norm of h_3 are positive. Multiplication by the former
gives D^w_{3k}>0; division by the latter gives the positive normalized
Gram–Schmidt coefficient. QED.

For the original weights, P_22=(log 2)/4, the comparison in Lemma 1 is
at least 5/(36k), and delta>1/120. As P_2k>=1/(4k), the proof also gives

\[
 D_{3k}>\frac{5\log2}{144k}+\frac1{480k}>0,
 \qquad k\ge3.
\]

This is an infinite-family statement, rather than verification up to a finite
cutoff. Its claimed generality is exactly the quantified assumptions above.

## Independent validation and reproducibility

Run `python3 verify_positivity_independent.py` using only the Python standard
library. It does not import this matching construction. It checks nonnegative
prefix sums directly over a complete period for each k in 3..2000 (thereby
covering every prefix length for those k), and encloses selected infinite Gram
series with integer arithmetic and a proved tail bound. It also rejects the
false extension of the comparison to k=2. These are independent computational
checks, not a second human proof or a formal proof-assistant certificate.

The period check uses 3*g(r)=(r mod 3)-(r mod 2). The direct Gram check computes
the defining nonnegative series and bounds its omitted tail by 1/(N+1), with
outward rounding accounted for exactly. The universal analytical proof is
separate from these finite-k checks.

## How the representation was selected

The target was converted from Gram determinants to a sign question for a
projection residual. Replacing its real projection coefficient by the rational
comparison 2/3 produces a six-residue sign pattern. Negative residue classes can
be injected into earlier positive classes while preserving the remainder
constraints of u_k. This is an application of domination/monotone-weight
reasoning. It does not require discarding the weights: their monotonicity and
summability are essential assumptions.

The six-state residue description is a finite representation audit. It does
not itself establish the quantified matching for arbitrary k. The universal
claim depends on the explicit analytical argument above.