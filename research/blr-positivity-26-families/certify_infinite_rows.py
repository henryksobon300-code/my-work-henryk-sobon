"""Exact certificates for finite rows and ALL columns of the NB Gram problem.

All accept/reject decisions use integers or Fraction. A small midpoint inverse
is used with a rigorous Neumann perturbation bound, not as a floating oracle.
The analytical propagation lemmas are in NB_GENERAL_CERTIFICATE_PROOF.md.
"""
from pathlib import Path
from fractions import Fraction as Q
import argparse, json, math, time, functools

ROOT=Path(__file__).resolve().parent
D=10**40
GRAM_STOP=10000

def ceilq(x): return -(-x.numerator//x.denominator)
def floorq(x): return x.numerator//x.denominator

@functools.lru_cache(None)
def gram_interval(a,b):
    if a>b:return gram_interval(b,a)
    period=math.lcm(a,b)
    vals=[(r%a)*(r%b) for r in range(1,period+1)]
    total=sum(vals)
    running=0; least=0; greatest=0
    for t,v in enumerate(vals,1):
        running+=v
        centered=period*running-total*t
        least=min(least,centered);greatest=max(greatest,centered)
    mean=Q(total,period*a*b)
    oscillation=Q(greatest-least,period*a*b)
    low=sum(D*(r%a)*(r%b)//(a*b*r*(r+1)) for r in range(1,GRAM_STOP+1))
    tail=mean/(GRAM_STOP+1)
    error=oscillation/((GRAM_STOP+1)*(GRAM_STOP+2))
    lo=low+floorq(D*(tail-error))
    hi=low+GRAM_STOP+ceilq(D*(tail+error))
    return Q(lo,D),Q(hi,D)

def inverse(A):
    n=len(A)
    M=[list(row)+[Q(int(i==j)) for j in range(n)] for i,row in enumerate(A)]
    for col in range(n):
        pivot=next(i for i in range(col,n) if M[i][col])
        M[col],M[pivot]=M[pivot],M[col]
        den=M[col][col]
        M[col]=[x/den for x in M[col]]
        for i in range(n):
            if i==col:continue
            m=M[i][col]
            if m:M[i]=[x-m*y for x,y in zip(M[i],M[col])]
    assert all(M[i][j]==int(i==j) for i in range(n) for j in range(n))
    return [row[n:] for row in M]

def projection_box(j):
    inds=list(range(2,j));m=len(inds)
    boxes=[[gram_interval(a,b) for b in inds] for a in inds]
    rhs=[gram_interval(a,j) for a in inds]
    mid=[[(l+h)/2 for l,h in row] for row in boxes]
    midrhs=[(l+h)/2 for l,h in rhs]
    R=inverse(mid)
    c0=[sum(R[i][t]*midrhs[t] for t in range(m)) for i in range(m)]
    norm=max(sum(abs(x) for x in row) for row in R)
    epsG=max((h-l)/2 for row in boxes for l,h in row)
    epsb=max((h-l)/2 for l,h in rhs)
    q=norm*m*epsG
    assert q<1,('perturbation bound failed',j)
    delta=norm*(epsb+epsG*sum(map(abs,c0)))/(1-q)
    # A rational grid coarser than the certified uncertainty; rounding is up.
    upper=[Q(ceilq((x+delta)*10**6),10**6) for x in c0]
    return upper,{'midpoint_coefficients':list(map(str,c0)),
        'common_absolute_error_bound':str(delta),'neumann_q':str(q),
        'inverse_infinity_norm':str(norm),'max_gram_entry_error':str(epsG),
        'max_rhs_entry_error':str(epsb),
        'upper_coefficients':list(map(str,upper))}

def sawtooth_oscillation(i):
    # Exact range of prefix sums of (r mod i)/i-(i-1)/(2i).
    return Q((i*i)//4,2*i)

def make_surrogate(j,upper):
    den=math.lcm(j,*[x.denominator*i for i,x in zip(range(2,j),upper)])
    terms=[(j,den//j)]+[(i,-x.numerator*(den//(x.denominator*i)))
                          for i,x in zip(range(2,j),upper)]
    def numerator(r):return sum(c*(r%i) for i,c in terms)
    mean=Q(j-1,2*j)-sum(x*Q(i-1,2*i) for i,x in zip(range(2,j),upper))
    oscillation=sawtooth_oscillation(j)+sum(abs(x)*sawtooth_oscillation(i)
                              for i,x in zip(range(2,j),upper))
    negative_bound=sum(max(Q(0),x)*Q(i-1,i) for i,x in zip(range(2,j),upper))
    assert mean>0,('nonpositive surrogate mean',j)
    return den,numerator,mean,oscillation,negative_bound

def certify_row(j):
    upper,projection=projection_box(j)
    den,num,mean,C,M=make_surrogate(j,upper)
    candidates=[]
    for K in [12,24,36,50,100,200,500,1000,2000]:
        S=sum(Q(num(r),den*(r+1)) for r in range(1,K+1))
        s=S-C/Q(K+2)
        if s>0:
            threshold=max(K+1,floorq(2*C/s)+1,j)
            candidates.append((threshold,K,S,s))
    assert candidates,('no positive harmonic barrier in budget',j)
    T,K,S,s=min(candidates)
    assert T<=20000,('finite certificate budget exceeded',j,T)
    finite=[]
    cache={}
    for k in range(j,T):
        stop=1000
        while True:
            if stop not in cache:cache[stop]=[num(r) for r in range(1,stop+1)]
            low=sum(D*v*(r%k)//(den*k*r*(r+1)) for r,v in enumerate(cache[stop],1))
            lower=Q(low,D)-M/Q(stop+1)
            if lower>0:break
            stop*=2
            assert stop<=1024000,('finite k certificate failed in budget',j,k)
        finite.append({'k':k,'sum_stop':stop,'strict_positive_lower_bound':str(lower)})
    return {'j':j,'status':'CERTIFIED','quantifier':f'every integer k >= {j}',
        'projection_certificate':projection,'surrogate_mean':str(mean),
        'centered_partial_sum_bound_C':str(C),'negative_value_bound_M':str(M),
        'surrogate_common_denominator':str(den),'prefix_K':K,
        'prefix_S_K':str(S),'harmonic_barrier_s':str(s),
        'infinite_k_threshold':T,'strict_tail_criterion':'k > 2*C/s',
        'finite_k_certificates':finite}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--max-j',type=int,default=10)
    args=ap.parse_args();start=time.monotonic();rows=[]
    for j in range(3,args.max_j+1):
        row=certify_row(j);rows.append(row)
        print(json.dumps({'j':j,'status':row['status'],'all_k_from':j,
            'infinite_k_threshold':row['infinite_k_threshold'],
            'finite_cases':len(row['finite_k_certificates'])}),flush=True)
        (ROOT/'INFINITE_ROWS_CERTIFICATE.json').write_text(json.dumps({
            'status':'IN_PROGRESS','rows_completed':rows},indent=2)+'\n')
    boxdata={f'{a},{b}':list(map(str,gram_interval(a,b)))
                 for a in range(2,args.max_j+1) for b in range(a,args.max_j+1)}
    result={'status':'PASS','rows':rows,'original_weight':'1/[r(r+1)]',
        'all_k':True,'quantification_in_j':{'lower':3,'upper':args.max_j},
        'gram_sum_stop':GRAM_STOP,'gram_intervals':boxdata,
        'decision_arithmetic':'integers and exact rational numbers only',
        'analytical_lemmas_required':'NB_GENERAL_CERTIFICATE_PROOF.md',
        'not_claimed':['all j','Riemann hypothesis','formal proof-assistant check','global priority'],
        'elapsed_seconds':time.monotonic()-start}
    (ROOT/'INFINITE_ROWS_CERTIFICATE.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'PASS','max_j':args.max_j,'elapsed_seconds':result['elapsed_seconds']}))

if __name__=='__main__':main()
