# Self-contained verifier for five new Qiskit qcode-discovery issue #13 candidates.
# Only Python 3 standard library. Bit i = qubit i (zero-based).
import json
records=json.loads('''[{"id":"6f76d175b6c3996b","ell":30,"m":6,"A":[[7,2],[28,3],[28,4]],"B":[[0,0],[7,5],[5,4]],"C":[[7,4],[28,2]],"D":[[7,0],[28,4]],"old":32,"upper":20,"zx":"0","zz":"100090090040000000004000000002200200201100000004000002000000001200020000000000000000008004","px":"73bfe0e0073bfe0e0073bfe0e0073bfe0e0073bfe0e","pz":"93f4bf00093f4bf00093f4bf00093f4bf00093f4bf000000000000000000000000000000000000000000000000"},{"id":"ca906ef77eaee0ed","ell":30,"m":6,"A":[[7,2],[28,3],[28,4]],"B":[[0,0],[7,5],[5,4]],"C":[[7,5],[28,1]],"D":[[7,1],[28,3]],"old":30,"upper":20,"zx":"0","zz":"100090090040000000004000000002200200201100000004000002000000001200020000000000000000008004","px":"73bfe0e0073bfe0e0073bfe0e0073bfe0e0073bfe0e","pz":"93f4bf00093f4bf00093f4bf00093f4bf00093f4bf000000000000000000000000000000000000000000000000"},{"id":"3d5510c528b2e841","ell":30,"m":6,"A":[[29,2],[26,3],[26,4]],"B":[[0,0],[29,5],[25,4]],"C":[[26,4],[29,1]],"D":[[26,2],[29,2]],"old":30,"upper":20,"zx":"0","zz":"200000200010102010000000100000081000080204040020004000000000202000000000000000001008000004","px":"4409102004409102004409102004409102004409102","pz":"480900000480900000480900000480900000480900000000000000000000000000000000000000000000000000"},{"id":"67c015a84425ea3a","ell":30,"m":6,"A":[[1,2],[4,3],[4,4]],"B":[[0,0],[1,5],[5,4]],"C":[[4,0]],"D":[[1,1],[4,3]],"old":30,"upper":20,"zx":"0","zz":"44200080001080000100000010002110000200000200000008001000000000000000002200000000004020004","px":"73bfe0e0073bfe0e0073bfe0e0073bfe0e0073bfe0e","pz":"abfe3f27f3801e4d92ab61dbfd2c4055bfffc491ff000900000000000000000000000000000000000000000000"},{"id":"70c03e15fe2839e4","ell":15,"m":6,"A":[[4,1],[6,4],[8,4]],"B":[[0,0],[10,1],[8,5]],"C":[[8,1]],"D":[[4,5],[6,2]],"old":21,"upper":14,"zx":"0","zz":"80000008402120040100000200000000008800001108","px":"264009900264009900264","pz":"110004400110004400110000000000000000000000000"}]''')
def pos(T,x,y,l,m,b,rev=False):
 s=-1 if rev else 1
 return {b*l*m+((x+s*a)%l)*m+(y+s*c)%m for a,c in T}
def comm(p,q):return (len(p[0]&q[1])+len(p[1]&q[0]))%2
def bits(h,n):
 v=int(h,16); assert v.bit_length()<=n
 return {i for i in range(n) if v>>i&1}
def rank(rows,n):
 B={}
 for x,z in rows:
  v=sum(1<<i for i in x)|sum(1<<(n+i) for i in z)
  while v:
   pivot=v.bit_length()-1
   if pivot not in B:B[pivot]=v;break
   v^=B[pivot]
 return len(B)
for R in records:
 l,m=R['ell'],R['m'];n=2*l*m;A,B,C,D=(R[q] for q in 'ABCD')
 rows=[]
 for x in range(l):
  for y in range(m):
   rows.append((pos(A,x,y,l,m,0)|pos(B,x,y,l,m,1),pos(C,x,y,l,m,0)|pos(D,x,y,l,m,1)))
 for x in range(l):
  for y in range(m):rows.append((set(),pos(B,x,y,l,m,0,True)|pos(A,x,y,l,m,1,True)))
 low=(bits(R['zx'],n),bits(R['zz'],n))
 partner=(bits(R['px'],n),bits(R['pz'],n))
 assert all(comm(a,b)==0 for a in rows for b in rows)
 rnk=rank(rows,n);assert n-rnk==(10 if n==360 else 6)
 assert len(low[0]|low[1])==R['upper']
 assert all(comm(low,g)==0 and comm(partner,g)==0 for g in rows)
 assert comm(low,partner)==1
 damaged=(set(low[0]),low[1]^{0})
 assert any(comm(damaged,g) for g in rows)
 assert R['upper']<R['old']
 print('PASS',R['id'],'n',n,'k',n-rnk,'d<=',R['upper'],'prior',R['old'])
print('PASS 5/5: upper bounds only; not exact distances')