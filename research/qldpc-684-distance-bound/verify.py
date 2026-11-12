"""Verify the QEC-10 weight-72 Z witness with Python 3.10 or newer."""

import argparse
import hashlib
import json
from pathlib import Path
from urllib.request import urlopen

SOURCE_URL = "https://raw.githubusercontent.com/unitaryfoundation/qldpc-challenge/15e58eea2bba862eb49a8a162fa801f81d027f5a/codes/684-6-77.json"
SOURCE_SHA256 = "f22859a38a45ddd13ede68b9a5540c0d59d4722eaa85e5306e1a3b26e10351fd"

Z_WITNESS = (
    365, 373, 374, 375, 384, 392, 393, 394, 396, 404, 405, 406, 421, 429,
    430, 431, 435, 443, 444, 445, 451, 459, 460, 461, 469, 470, 471, 479,
    486, 494, 502, 503, 507, 508, 509, 517, 526, 534, 535, 536, 547, 548,
    549, 557, 560, 568, 569, 570, 576, 577, 578, 586, 596, 597, 598, 606,
    618, 619, 620, 628, 630, 631, 639, 647, 653, 654, 655, 663, 670, 671,
    672, 680,
)
X_PARTNER = (
    358, 361, 362, 365, 368, 370, 372, 378, 379, 382, 384, 389, 390, 392,
    394, 395, 398, 399, 401, 402, 403, 404, 405, 408, 409, 410, 411, 412,
    413, 416, 417, 420, 422, 423, 424, 425, 426, 427, 428, 430, 431, 433,
    434, 439, 444, 447, 448, 450, 455, 456, 458, 461, 462, 463, 464, 466,
    468, 469, 470, 471, 473, 475, 484, 485, 487, 489, 490, 493, 494, 496,
    497, 498, 500, 505, 508, 511, 512, 513, 514, 515, 516, 518, 519, 522,
    523, 531, 532, 534, 537, 538, 540, 544, 545, 550, 552, 555, 556, 557,
    558, 561, 562, 563, 568, 569, 570, 571, 573, 578, 580, 581, 589, 590,
    593, 594, 595, 598, 601, 602, 603, 606, 612, 613, 617, 618, 619, 623,
    626, 627, 630, 631, 632, 634, 635, 637, 640, 641, 643, 645, 647, 648,
    649, 654, 655, 656, 660, 661, 662, 663, 664, 667, 668, 669, 671, 673,
    675, 678, 679, 680, 681, 683,
)


def mask(support, n):
    if any(type(q) is not int or not 0 <= q < n for q in support):
        raise ValueError("support index outside the code")
    if len(set(support)) != len(support):
        raise ValueError("repeated support index")
    return sum(1 << q for q in support)


def rank(rows):
    pivots = {}
    for row in rows:
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    return len(pivots)


def verify(code, z_support=Z_WITNESS, x_support=X_PARTNER):
    n = code["n"]
    if n != 684 or code["k"] != 6:
        raise ValueError("unexpected code parameters")
    hx = [mask(row, n) for row in code["checks"]["X"]]
    hz = [mask(row, n) for row in code["checks"]["Z"]]
    if any((x & z).bit_count() % 2 for x in hx for z in hz):
        raise ValueError("CSS checks do not commute")

    z = mask(z_support, n)
    x = mask(x_support, n)
    if z.bit_count() != 72:
        raise ValueError("expected a weight-72 witness")
    if any((z & row).bit_count() % 2 for row in hx):
        raise ValueError("Z witness has nonzero X syndrome")
    if any((x & row).bit_count() % 2 for row in hz):
        raise ValueError("X partner has nonzero Z syndrome")
    if (z & x).bit_count() % 2 != 1:
        raise ValueError("Z witness and X partner do not anticommute")

    rank_x, rank_z = rank(hx), rank(hz)
    if n - rank_x - rank_z != 6 or rank(hz + [z]) != rank_z + 1:
        raise ValueError("rank check failed")
    return rank_x, rank_z


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, help="local copy of the pinned source JSON")
    args = parser.parse_args()
    try:
        if args.source is None:
            with urlopen(SOURCE_URL, timeout=20) as response:
                raw = response.read()
        else:
            raw = args.source.read_bytes()
        if hashlib.sha256(raw).hexdigest() != SOURCE_SHA256:
            raise ValueError("source SHA-256 does not match the pinned matrix")
        rank_x, rank_z = verify(json.loads(raw))
    except (OSError, ValueError, KeyError) as error:
        parser.exit(1, f"FAIL: {error}\n")
    print("PASS: n=684 k=6 Z logical weight=72; d_Z <= 72 and d <= 72")
    print(f"Ranks H_X/H_Z/H_Z with witness: {rank_x}/{rank_z}/{rank_z + 1}")


if __name__ == "__main__":
    main()
