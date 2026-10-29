# A transparent special certificate for j = 4

Use the definitions in NB_J3_PROOF.md. This is a second derivation for one row
also covered by the general certificate generator.

The exact outward Gram enclosures computed by `verify_j4_certificate.py`
prove that the projection residual is

\[
 h_4=f_4-u f_3-v f_2,\qquad u<9/20,\quad v<21/50.
\]

Take g=f_4-(9/20)f_3-(21/50)f_2. In residue order 0,...,11 its values,
multiplied by 100, are

\[
 (0,-11,20,54,-15,-26,50,39,-30,4,35,24).
\]

Write S_N=sum_{r<=N}g(r)/(r+1). Direct rational summation gives
S_35=971006025493703/2888071057872000 and
S_37=962645819799863/2888071057872000, both greater than 3/10.
Also S_36=S_35. For every later prefix, assign the negative residues 4 and 5
to the earlier positive residue 3 in the same period (54>15+26), residue 8 to
the earlier residue 7 (39>30), and residue 1 to residue 11 of the previous
period (24>11). The harmonic weights decrease, and no positive source is
reused. Starting after r=37, each negative term is covered by an earlier
positive term of at least its magnitude; every remaining term is nonnegative.
It follows that S_N>=min(S_35,S_37)>3/10 for every N>=35.

For k>=36, the r<k contribution to <g,f_k> is S_(k-1)/k. Since g>=-3/10,
the remaining tail is at least -3/(10k). Hence <g,f_k>>0 for all k>=36.
The executable certificate independently encloses the defining signed series
for each k=4,...,35 and obtains a strictly positive lower endpoint, with the
tail and rounding included. Thus <g,f_k>>0 for every k>=4.

Finally h_4-g=(9/20-u)f_3+(21/50-v)f_2 is nonnegative, so
<h_4,f_k>>0. Its norm is positive by linear independence. This proves the
j=4 Gram-minor/normalized Gram–Schmidt assertion for every k>=4.

The first trial incorrectly guessed that the harmonic barrier already exceeded
3/10 at N=11. An exact assertion rejected that guess. The valid cutoff above
uses N=35,37; the failed guess is retained in the procedural log. It never
became an accepted result.