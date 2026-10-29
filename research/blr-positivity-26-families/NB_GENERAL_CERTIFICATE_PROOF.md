# Finite certificates for infinite columns of the NB positivity problem

27 October 2026. Candidate partial contribution; no global priority or external
referee review is established. Read this proof together with the executable
certificate and its independent checker. All computational inequalities use
outward enclosures and exact integers/rationals.

## Result and exact limitation

With f_k and P_jk as defined in NB_J3_PROOF.md, the completed certificates prove
the Bellemare–Langlois–Ransford determinant inequality for each fixed integer
j=3,...,28 and **every** integer k>=j. The elementary j=2 case is already known.
This is a finite range in j, an infinite range in k. It proves neither the full
positivity conjecture nor the Riemann hypothesis.

The attempt was fixed to j<=30. Its original certificate construction failed
at (j,k)=(29,56), where a sufficient lower certificate did not become positive
within the declared direct-summation budget. That is UNKNOWN for this
construction, not a counterexample to the original conjecture. No missing rows
are silently replaced by easier instances.

The primary problem is Conjectures 2/9 in Bellemare, Langlois and Ransford,
[arXiv:2011.02847](https://arxiv.org/abs/2011.02847), published in the Monthly
in 2019. Its Theorem 12 already describes a conditional eventual-positivity
strategy. The present procedure supplies explicit, checkable constants and
finite checks for the stated rows. General domination, Abel summation,
periodicity, projection and perturbation bounds are known methods; their use
here is not evidence that those methods are new.

## 1. Reduction to a rational comparison function

Put u_i(r)=(r mod i)/i, and use weights w_r=1/[r(r+1)]. For fixed j, let

\[
 h_j=u_j-\sum_{i=2}^{j-1}c_i u_i
\]

be the residual of the orthogonal projection onto u_2,...,u_{j-1}. The
coefficient vector solves Gc=b, where G=(P_il) for 2<=i,l<j and b=(P_ij).
If rational numbers beta_i satisfy beta_i>=c_i, define

\[
 g=u_j-\sum_{i=2}^{j-1}\beta_i u_i.
\]

Since every u_i is nonnegative, h_j>=g pointwise. Therefore proving
<g,u_k>_w>0 suffices for <h_j,u_k>_w>0. Normalizing h_j preserves its sign.
The required Gram determinant has the same sign: taking the Schur complement
of G gives det(G)*<h_j,u_k>_w.

For completeness, all finite collections u_2,...,u_j are linearly independent.
Indeed, if a linear combination vanishes for every r, its first difference is
sum_i a_i/i - sum_{i|r}a_i=0. At r=1 the first sum must be zero. At r=2,3,...,j
the remaining divisibility equations then imply a_r=0 successively. Thus G is
positive definite and h_j is nonzero.

## 2. A uniform bound on centered partial sums

The mean of u_i over one period is m_i=(i-1)/(2i). Its centered prefix values,
for a remainder t in {0,...,i-1}, are

\[
 A_i(t)=\frac{t(t-i+2)}{2i}.
\]

Their range is C_i=floor(i^2/4)/(2i). A sum of centered u_i over any integer
interval is a difference of two prefix values, so its absolute value is at
most C_i, independent of the interval's length and starting residue.

Set

\[
 \mu=m_j-\sum_i\beta_i m_i,\qquad
 C=C_j+\sum_i|\beta_i|C_i.
\]

Then the sum of g(r)-mu over every finite integer interval has absolute value
at most C. The certificate explicitly verifies mu>0.

## 3. A harmonic-prefix barrier valid for every subsequent index

Let S_N=sum_{r=1}^N g(r)/(r+1). Choose a finite K and compute S_K exactly.
Abel summation, using the centered partial-sum bound in section 2 and the
decreasing weights 1/(r+1), gives, for every N>=K,

\[
 S_N\ge S_K-\frac{C}{K+2}=:s.
\]

The mean contribution from K+1 to N is nonnegative. For the centered part,
write its running sums as H_t with |H_t|<=C. In the finite Abel identity the
absolute sum of the coefficients of H_t is exactly the first weight
1/(K+2); hence its lower bound is -C/(K+2). This also covers N=K directly.
The certificate requires s>0.

## 4. The exact tail is bounded by a constant times 1/k^2

For r<k, u_k(r)w_r=1/[k(r+1)]. For r>=k, split into blocks r=mk+a,
m>=1, a=1,...,k-1; the omitted multiples of k contribute zero. Define

\[
 v_a=\frac{a}{k(mk+a)(mk+a+1)}.
\]

These v_a increase with a. Their consecutive difference has the sign of
mk-a, which is positive throughout each block. Apply finite Abel summation to
(g-mu)*v_a in a block. Because every centered prefix is bounded in absolute
value by C, its contribution is at least -2C*v_{k-1}. The mu contribution
is nonnegative. Moreover,

\[
 v_{k-1}\le\frac{1}{m(m+1)k^2},\qquad
 \sum_{m\ge1}\frac1{m(m+1)}=1.
\]

The full series converges absolutely. Summing these bounds proves

\[
 \langle g,u_k\rangle_w
 \ge \frac{S_{k-1}}{k}-\frac{2C}{k^2}.
\]

Consequently every k>=K+1 with k>2C/s has positive inner product.
The integer threshold stored in the certificate is

\[
 T=\max\{j,K+1,\lfloor2C/s\rfloor+1\}.
\]

Only k=j,...,T-1 remain to be checked separately. This is the finite-to-infinite
implication; a successful finite search alone would not establish it.

## 5. Rigorous Gram enclosures in the certificate generator

For a,b fixed, u_a(r)u_b(r) is nonnegative and periodic with period L=lcm(a,b).
Compute its exact finite-period mean m and the range B of its centered prefix
sums. Its infinite weighted tail after N satisfies

\[
 \left|\sum_{r>N}\frac{u_a(r)u_b(r)}{r(r+1)}-\frac{m}{N+1}\right|
 \le\frac{B}{(N+1)(N+2)}.
\]

This follows from Abel summation with decreasing weights and the same
interval-prefix bound as above. The retained N terms are rounded outward with
integers at scale 10^40. All rounding errors are included in the stored bounds.

Let G0,b0 be the midpoints of the Gram boxes and let R=G0^{-1}, computed using
exact rational elimination. Put c0=Rb0. If each Gram entry has error at most
epsilon_G and each right-hand-side entry has error at most epsilon_b, then

\[
 q=\|R\|_\infty (j-2)\epsilon_G<1
\]

implies, by the Neumann-series inverse bound,

\[
 \|c-c_0\|_\infty\le
 \frac{\|R\|_\infty(\epsilon_b+\epsilon_G\|c_0\|_1)}{1-q}=\delta.
\]

Thus rounding c0_i+delta upwards to the chosen rational grid supplies valid
beta_i. Neither floating-point linear algebra nor an approximate inverse is
trusted in this acceptance decision.

## 6. Finite k checks and the independent implementation

If M=sum_i max(beta_i,0)*(i-1)/i, then g>=-M. The direct series for
<g,u_k> has omitted tail at least -M/(N+1). Its finite sum is rounded
downwards using integer division, including for negative numerators. A strictly
positive resulting lower bound proves that finite case. No unverified decimal
signs are used.

`check_infinite_rows_independent.py` uses a separately written C++ integer
summation kernel and another Gram-tail enclosure. For a residue class starting
at r0>N, convexity of f(t)=1/[t(t+1)] gives

\[
 \frac12f(r_0)+\int_0^\infty f(r_0+Lx)\,dx
 \le\sum_{m\ge0}f(r_0+mL)
 \le\int_{-1/2}^\infty f(r_0+Lx)\,dx.
\]

The integrals are log(1+1/r0)/L and log(1+1/(r0-L/2))/L. Alternating-series
two-term lower and three-term upper bounds enclose these logarithms by
rationals. The checker then uses interval Gaussian elimination to validate
projection bounds. At j=26,...,28, dependency makes that first enclosure too
wide; a verified interval fixed-point box completes the check. Its proposed
rational LU preconditioner is accepted only after checking a strict contraction
and an invariant box. The proposed inverse is never trusted on its own. This
is distinct from the generator's global perturbation bound. The checker
recomputes every finite-case sign and each infinite-tail threshold.

This is independent implementation checking by programs written in this
session, not independent human review and not a Lean/Isabelle formalization.
The exact assumptions and analytical lemmas remain available for review here.