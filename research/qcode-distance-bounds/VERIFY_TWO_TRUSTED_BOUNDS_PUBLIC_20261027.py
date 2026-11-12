# PUBLIC MATH-ONLY PROOF: TWO TRUSTED-CATALOGUE UPPER BOUNDS
# Public source: qiskit-community/qcode-discovery, commit da9178fd65ffc2eec3dab46089f9879eb02d4b23.
# Contains public polynomial parameters, explicit Pauli witnesses and an independently
# implemented verifier. No original MathemaSpace engine, emails, GOLD or search heuristics.
# Upper bounds only. Repository novelty is a candidate status; global priority is not proved.
"""Standalone exact PBB Pauli-pair verifier. Python standard library only.

Does not import the finder, its GF2 basis routines, or saved matrices.
Builds rows directly as sets of (X/Z, block, x, y) and checks commutation.
An anticommuting pair in the centralizer proves both are non-stabilizers.
"""
from pathlib import Path
import json,copy,hashlib

if not __debug__: raise RuntimeError('Run without -O')
SOURCE_RECORDS_JSON='[\n  {\n    "ell": 30,\n    "m": 6,\n    "A_terms": [\n      [\n        14,\n        1\n      ],\n      [\n        21,\n        4\n      ],\n      [\n        28,\n        4\n      ]\n    ],\n    "B_terms": [\n      [\n        0,\n        0\n      ],\n      [\n        5,\n        1\n      ],\n      [\n        28,\n        5\n      ]\n    ],\n    "C_terms": [\n      [\n        14,\n        4\n      ],\n      [\n        21,\n        4\n      ]\n    ],\n    "D_terms": [\n      [\n        14,\n        5\n      ],\n      [\n        21,\n        2\n      ]\n    ],\n    "n": 360,\n    "k": 10,\n    "d": 22,\n    "bliss_hash": "f0fdaa4514a87ad2"\n  },\n  {\n    "ell": 15,\n    "m": 6,\n    "A_terms": [\n      [\n        8,\n        1\n      ],\n      [\n        12,\n        4\n      ],\n      [\n        1,\n        4\n      ]\n    ],\n    "B_terms": [\n      [\n        0,\n        0\n      ],\n      [\n        5,\n        1\n      ],\n      [\n        1,\n        5\n      ]\n    ],\n    "C_terms": [\n      [\n        8,\n        1\n      ],\n      [\n        12,\n        4\n      ]\n    ],\n    "D_terms": [\n      [\n        8,\n        2\n      ],\n      [\n        12,\n        5\n      ]\n    ],\n    "n": 180,\n    "k": 6,\n    "d": 20,\n    "bliss_hash": "331facaa1752ec16"\n  }\n]\n'
CERTIFICATES_JSON='[\n  {\n    "id": "f0fdaa4514a87ad2",\n    "status": "CERTIFIED_UPPER_BOUND",\n    "n": 360,\n    "k": 10,\n    "catalogue_d": 22,\n    "upper_bound": 16,\n    "strictly_smaller": true,\n    "x_support": [],\n    "z_support": [\n      20,\n      30,\n      32,\n      62,\n      73,\n      77,\n      107,\n      115,\n      158,\n      160,\n      170,\n      202,\n      215,\n      253,\n      255,\n      298\n    ],\n    "anticommuting_partner": {\n      "x_support": [\n        1,\n        4,\n        6,\n        9,\n        19,\n        22,\n        24,\n        27,\n        37,\n        40,\n        42,\n        45,\n        55,\n        58,\n        60,\n        63,\n        73,\n        76,\n        78,\n        81,\n        91,\n        94,\n        96,\n        99,\n        109,\n        112,\n        114,\n        117,\n        127,\n        130,\n        132,\n        135,\n        145,\n        148,\n        150,\n        153,\n        163,\n        166,\n        168,\n        171\n      ],\n      "z_support": [\n        194,\n        197,\n        198,\n        199,\n        201,\n        202,\n        204,\n        207,\n        211,\n        212,\n        214,\n        215,\n        230,\n        233,\n        234,\n        235,\n        237,\n        238,\n        240,\n        243,\n        247,\n        248,\n        250,\n        251,\n        266,\n        269,\n        270,\n        271,\n        273,\n        274,\n        276,\n        279,\n        283,\n        284,\n        286,\n        287,\n        302,\n        305,\n        306,\n        307,\n        309,\n        310,\n        312,\n        315,\n        319,\n        320,\n        322,\n        323,\n        338,\n        341,\n        342,\n        343,\n        345,\n        346,\n        348,\n        351,\n        355,\n        356,\n        358,\n        359\n      ]\n    },\n    "syndrome_nonzero_count": 0,\n    "partner_syndrome_nonzero_count": 0,\n    "symplectic_pairing": 1,\n    "coordinate_convention": "index=block*(ell*m)+x*m+y; zero based",\n    "transfer": {\n      "representative": "f0fdaa4514a87ad2",\n      "x_multiplier": 1\n    },\n    "exact_distance": false,\n    "certificate_argument": "Both commute with every stabilizer, but anticommute with one another; therefore neither is a stabilizer."\n  },\n  {\n    "id": "331facaa1752ec16",\n    "status": "CERTIFIED_UPPER_BOUND",\n    "n": 180,\n    "k": 6,\n    "catalogue_d": 20,\n    "upper_bound": 14,\n    "strictly_smaller": true,\n    "x_support": [],\n    "z_support": [\n      12,\n      22,\n      28,\n      46,\n      57,\n      67,\n      91,\n      102,\n      117,\n      122,\n      128,\n      143,\n      154,\n      159\n    ],\n    "anticommuting_partner": {\n      "x_support": [\n        1,\n        4,\n        6,\n        9,\n        19,\n        22,\n        24,\n        27,\n        37,\n        40,\n        42,\n        45,\n        55,\n        58,\n        60,\n        63,\n        73,\n        76,\n        78,\n        81\n      ],\n      "z_support": [\n        93,\n        99,\n        101,\n        107,\n        111,\n        117,\n        119,\n        125,\n        129,\n        135,\n        137,\n        143,\n        147,\n        153,\n        155,\n        161,\n        165,\n        171,\n        173,\n        179\n      ]\n    },\n    "syndrome_nonzero_count": 0,\n    "partner_syndrome_nonzero_count": 0,\n    "symplectic_pairing": 1,\n    "coordinate_convention": "index=block*(ell*m)+x*m+y; zero based",\n    "transfer": {\n      "representative": "331facaa1752ec16",\n      "x_multiplier": 1\n    },\n    "exact_distance": false,\n    "certificate_argument": "Both commute with every stabilizer, but anticommute with one another; therefore neither is a stabilizer."\n  }\n]\n'

def translated(terms,x,y,ell,m,block,reverse=False):
    sign=-1 if reverse else 1;N=ell*m
    return {block*N+((x+sign*a)%ell)*m+(y+sign*b)%m for a,b in terms}

def stabilizers(record):
    ell,m=record['ell'],record['m'];rows=[]
    for x in range(ell):
        for y in range(m):
            xs=translated(record['A_terms'],x,y,ell,m,0)|translated(record['B_terms'],x,y,ell,m,1)
            zs=translated(record['C_terms'],x,y,ell,m,0)|translated(record['D_terms'],x,y,ell,m,1)
            rows.append((xs,zs))
    for x in range(ell):
        for y in range(m):
            zs=translated(record['B_terms'],x,y,ell,m,0,True)|translated(record['A_terms'],x,y,ell,m,1,True)
            rows.append((set(),zs))
    return rows

def form(a,b):return (len(a[0]&b[1])+len(a[1]&b[0]))%2

def rank(rows,n):
    basis={}
    for x,z in rows:
        row=set(x)|{n+i for i in z}
        while row:
            p=min(row)
            if p not in basis:basis[p]=row;break
            row.symmetric_difference_update(basis[p])
    return len(basis)

def verify(record,certificate,rows=None):
    n=2*record['ell']*record['m'];rows=rows if rows is not None else stabilizers(record)
    sx=certificate['x_support'];sz=certificate['z_support'];partner=certificate['anticommuting_partner']
    for seq in [sx,sz,partner['x_support'],partner['z_support']]:
        if len(seq)!=len(set(seq)) or any(not isinstance(i,int) or not 0<=i<n for i in seq):return False,'invalid support'
    word=(set(sx),set(sz));other=(set(partner['x_support']),set(partner['z_support']))
    if len(word[0]|word[1])!=certificate['upper_bound']:return False,'wrong weight'
    if any(form(word,g) for g in rows):return False,'nonzero syndrome'
    if any(form(other,g) for g in rows):return False,'partner outside centralizer'
    if form(word,other)!=1:return False,'anticommuting partner missing'
    return True,'centralizer pair with symplectic product one'

if __name__=='__main__':
    records=json.loads(SOURCE_RECORDS_JSON);certs=json.loads(CERTIFICATES_JSON);output=[]
    for cert in certs:
        if cert['status']!='CERTIFIED_UPPER_BOUND':raise ValueError('uncertified target '+cert['id'])
        rec=next(r for r in records if r['bliss_hash']==cert['id']);rows=stabilizers(rec);n=rec['n']
        assert all(form(a,b)==0 for a in rows for b in rows)
        rr=rank(rows,n);assert n-rr==rec['k']
        ok,why=verify(rec,cert,rows);assert ok,(cert['id'],why)
        controls={}
        damaged=copy.deepcopy(cert);s=set(damaged['z_support']);s.symmetric_difference_update({0});damaged['z_support']=sorted(s);damaged['upper_bound']=len(s)
        controls['single_qubit_damage_rejected']=not verify(rec,damaged,rows)[0]
        bad_weight=copy.deepcopy(cert);bad_weight['upper_bound']+=1
        controls['wrong_weight_rejected']=not verify(rec,bad_weight,rows)[0]
        stab=copy.deepcopy(cert);stab['x_support']=sorted(rows[-1][0]);stab['z_support']=sorted(rows[-1][1]);stab['upper_bound']=len(rows[-1][0]|rows[-1][1])
        controls['stabilizer_as_logical_rejected']=not verify(rec,stab,rows)[0]
        assert all(controls.values())
        output.append(dict(id=cert['id'],status='PASS',n=n,k=n-rr,stabilizer_rank=rr,upper_bound=cert['upper_bound'],
                           previous_catalogue=cert['catalogue_d'],controls=controls,
                           certificate='explicit anticommuting centralizer pair',shared_finder_code=False))
    result=dict(status='PASS',verified=output,input_records_sha256=hashlib.sha256(SOURCE_RECORDS_JSON.encode('utf-8')).hexdigest(),
                certificates_sha256=hashlib.sha256(CERTIFICATES_JSON.encode('utf-8')).hexdigest(),
                bound_type='upper only; exact minimum and optimality are not claimed')
    print(json.dumps(result,indent=2))
