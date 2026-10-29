"""Separate exact checker: convex arithmetic-class tails + interval elimination.

Requires Python standard library and a C++17 compiler, no network or packages.
It imports no code from certify_infinite_rows.py or any MathemaSpace engine.
"""
from pathlib import Path
from fractions import Fraction as Q
import json,math,subprocess,time,traceback,sys

ROOT=Path(__file__).resolve().parent
D=10**24
STOP=1000000

def ceildiv(a,b):return -((-a)//b)
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[1],a[1]-b[0]
def mul(a,b):
    vals=[x*y for x in a for y in b]
    return min(vals)//D,ceildiv(max(vals),D)
def div(a,b):
    assert b[0]>0 or b[1]<0,'interval division crosses zero'
    nums=[(x*D,y) for x in a for y in b]
    return min(x//y for x,y in nums),max(ceildiv(x,y) for x,y in nums)

def projection_interval(A,b):
    # Forward interval elimination and backward substitution. No midpoint
    # inverse, spectral norm bound, or supplied projection result is used.
    n=len(b);M=[list(row)+[rhs] for row,rhs in zip(A,b)]
    for p in range(n):
        assert M[p][p][0]>0,('nonpositive interval pivot',p)
        for r in range(p+1,n):
            factor=div(M[r][p],M[p][p])
            for c in range(p+1,n+1):M[r][c]=sub(M[r][c],mul(factor,M[p][c]))
            M[r][p]=(0,0)
    out=[None]*n
    for r in range(n-1,-1,-1):
        rhs=M[r][-1]
        for c in range(r+1,n):rhs=sub(rhs,mul(M[r][c],out[c]))
        out[r]=div(rhs,M[r][r])
    return out

def validated_fixed_point_box(A,b):
    # Independent alternative when dependency widens interval elimination.
    # A rational LU inverse proposes a preconditioner, but its correctness is
    # NOT trusted: interval bounds verify the fixed-point contraction and box.
    n=len(b);g0=[[(x[0]+x[1])//2 for x in row] for row in A]
    LU=[[Q(x,D) for x in row] for row in g0];perm=list(range(n))
    for p in range(n):
        pivot=max(range(p,n),key=lambda r:abs(LU[r][p]));assert LU[pivot][p]
        LU[p],LU[pivot]=LU[pivot],LU[p];perm[p],perm[pivot]=perm[pivot],perm[p]
        for r in range(p+1,n):
            LU[r][p]/=LU[p][p]
            for c in range(p+1,n):LU[r][c]-=LU[r][p]*LU[p][c]
    columns=[]
    for col in range(n):
        y=[]
        for r in range(n):y.append(Q(int(perm[r]==col))-sum(LU[r][c]*y[c] for c in range(r)))
        x=[Q(0)]*n
        for r in range(n-1,-1,-1):x[r]=(y[r]-sum(LU[r][c]*x[c] for c in range(r+1,n)))/LU[r][r]
        columns.append(x)
    R=[[int(columns[c][r]*D) for c in range(n)] for r in range(n)]
    E=[]
    for r in range(n):
        row=[]
        for c in range(n):
            v=(D*int(r==c),)*2
            for t in range(n):v=sub(v,mul((R[r][t],)*2,A[t][c]))
            row.append(v)
        E.append(row)
    eabs=[[max(map(abs,x)) for x in row] for row in E]
    q=max(sum(row) for row in eabs)
    assert q<D,'preconditioned map is not a verified contraction'
    b0=[(x[0]+x[1])//2 for x in b]
    c0=[sum(R[r][c]*b0[c] for c in range(n))//D for r in range(n)]
    f=[]
    for r in range(n):
        v=(-c0[r],)*2
        for c in range(n):
            v=add(v,mul((R[r][c],)*2,b[c]))
            v=add(v,mul(E[r][c],(c0[c],)*2))
        f.append(max(map(abs,v)))
    radius=[2*x+10 for x in f]
    for iteration in range(100):
        needed=[f[r]+sum(ceildiv(eabs[r][c]*radius[c],D) for c in range(n)) for r in range(n)]
        if all(a<=z for a,z in zip(needed,radius)):
            return [(x-z,x+z) for x,z in zip(c0,radius)],{'method':'verified interval fixed-point box','iterations':iteration+1,'contraction_q':str(Q(q,D))}
        radius=[max(old,2*new+1) for old,new in zip(radius,needed)]
    raise AssertionError('fixed-point box budget exhausted')

def gram_tail_box(a,b,partial):
    L=math.lcm(a,b);lo=partial;hi=partial+STOP
    for q in range(1,L+1):
        value=(q%a)*(q%b)
        if not value:continue
        r=STOP+1+((q-STOP-1)%L)
        W=2*r-L
        assert W>2
        # Convex trapezoid lower bound, with log(1+t)>=t-t^2/2.
        low_num=D*value*(2*r*r+(L+1)*r-1)
        low_den=a*b*2*L*r*r*(r+1)
        lo+=low_num//low_den
        # Convex centered-cell upper bound, with log(1+t)<=t-t^2/2+t^3/3.
        high_num=D*value*(6*W*W-6*W+8)
        high_den=a*b*3*L*W*W*W
        hi+=ceildiv(high_num,high_den)
    return lo,hi

def oscillation(i):
    mean=Q(i-1,2*i);prefix=Q(0);values=[prefix]
    for r in range(1,i+1):
        prefix+=Q(r%i,i)-mean;values.append(prefix)
    assert prefix==0
    return max(values)-min(values)

def main():
    started=time.monotonic()
    cert=json.loads((ROOT/'INFINITE_ROWS_CERTIFICATE.json').read_text())
    assert cert['status']=='PASS'
    rows=cert['rows'];J=max(row['j'] for row in rows)
    assert [x['j'] for x in rows]==list(range(3,J+1))
    if '--reuse-sums' in sys.argv:
        raw=(ROOT/'INDEPENDENT_GRAM_SUMS.txt').read_text()
    else:
        compiler=subprocess.run(['g++','-O3','-std=c++17',str(ROOT/'independent_gram_sums.cpp'),'-o',str(ROOT/'independent_gram_sums')],capture_output=True,text=True)
        (ROOT/'INDEPENDENT_COMPILE.log').write_text(compiler.stdout+compiler.stderr)
        assert compiler.returncode==0
        sums=subprocess.run([str(ROOT/'independent_gram_sums'),str(J),str(STOP)],capture_output=True,text=True)
        (ROOT/'INDEPENDENT_GRAM_SUMS.txt').write_text(sums.stdout)
        assert sums.returncode==0
        raw=sums.stdout
    boxes={}
    for line in raw.splitlines():
        a,b,v=map(int,line.split());boxes[a,b]=gram_tail_box(a,b,v)
    assert set(boxes)=={(a,b) for a in range(2,J+1) for b in range(a,J+1)}
    def get(a,b):return boxes[min(a,b),max(a,b)]
    total_finite=0;row_results=[]
    for row in rows:
        j=row['j'];inds=list(range(2,j));beta=list(map(Q,row['projection_certificate']['upper_coefficients']))
        assert len(beta)==len(inds)
        A=[[get(a,b) for b in inds] for a in inds];bvec=[get(a,j) for a in inds]
        ci=projection_interval(A,bvec)
        method={'method':'interval Gaussian elimination'}
        if not all(Q(c[1],D)<=b for c,b in zip(ci,beta)):
            ci,method=validated_fixed_point_box(A,bvec)
        for c,b in zip(ci,beta):assert Q(c[1],D)<=b,('projection upper not certified',j,str(Q(c[1],D)),str(b))
        mu=Q(j-1,2*j)-sum(b*Q(i-1,2*i) for i,b in zip(inds,beta))
        C=oscillation(j)+sum(abs(b)*oscillation(i) for i,b in zip(inds,beta))
        M=sum(max(b,Q(0))*Q(i-1,i) for i,b in zip(inds,beta))
        assert mu>0
        K=row['prefix_K']
        S=sum((Q(r%j,j)-sum(b*Q(r%i,i) for i,b in zip(inds,beta)))/Q(r+1) for r in range(1,K+1))
        s=S-C/Q(K+2);assert s>0
        T=max(j,K+1,(2*C/s).numerator//(2*C/s).denominator+1)
        assert T==row['infinite_k_threshold']
        cases=row['finite_k_certificates']
        assert [x['k'] for x in cases]==list(range(j,T))
        maxstop=max((2*x['sum_stop'] for x in cases),default=0)
        glow=[]
        for r in range(1,maxstop+1):
            v=D*(r%j)//j
            for i,b in zip(inds,beta):v-=ceildiv(D*b.numerator*(r%i),b.denominator*i)
            glow.append(v)
        for case in cases:
            k=case['k'];N=2*case['sum_stop']
            lo=sum(glow[r-1]*(r%k)//(k*r*(r+1)) for r in range(1,N+1))
            lower=Q(lo,D)-M/Q(N+1)
            assert lower>0,('finite inner product failed',j,k)
            total_finite+=1
        row_results.append({'j':j,'all_integer_k_from':j,'finite_checks':len(cases),
            'infinite_threshold':T,'projection_check':method,'status':'PASS'})
        print(json.dumps(row_results[-1]),flush=True)
    result={'status':'PASS','range_j':[3,J],'quantifier':'every integer k >= j',
        'independent_gram_stop':STOP,'gram_method':'integer C++ partial sums + convex arithmetic-class integral bounds',
        'projection_method':'interval Gaussian elimination; verified interval fixed-point boxes where needed',
        'reused_previous_cpp_partial_sums':'--reuse-sums' in sys.argv,
        'finite_inner_products_recomputed':total_finite,'rows':row_results,
        'independent_human_review':False,'formal_proof_assistant':False,
        'elapsed_seconds':time.monotonic()-started}
    (ROOT/'INFINITE_ROWS_INDEPENDENT_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'PASS','range_j':[3,J],'finite_checks':total_finite,'elapsed_seconds':result['elapsed_seconds']}))

if __name__=='__main__':
    try:main()
    except Exception as exc:
        (ROOT/'INFINITE_ROWS_INDEPENDENT_CHECK.json').write_text(json.dumps({'status':'FAIL','error':str(exc),'traceback':traceback.format_exc()},indent=2)+'\n')
        raise
