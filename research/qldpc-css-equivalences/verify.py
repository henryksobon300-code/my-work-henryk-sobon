"""Verify two qLDPC Challenge CSS catalogue equivalences."""

import argparse
import hashlib
import json
from pathlib import Path
from urllib.request import urlopen

SOURCE = "https://raw.githubusercontent.com/unitaryfoundation/qldpc-challenge/30953fadd41e29f83d1186976d95cddc87cfb4dd/codes"
PAIRS = (
    (
        ("10-2-3", "bfa38290a2077146d7277adc4dd626a96da47ec45be49e11e54602393e661b12"),
        ("10-2-3-b", "6fbd5fdf9f75bf50d482541bb6524d4373cb709f3c7079bb470c33723028bd46"),
        (0, 6, 4, 2, 8, 5, 9, 3, 1, 7),
        16,
    ),
    (
        ("12-2-4", "3c7b1a79d820d4dd783b602f78703de361b36927fc55b6458d57b85b61a8b3ae"),
        ("12-2-4-b", "d59ebef380cfd442d0a4c5d5091bd1b8bae1859466397d4f8b97bbe0bb744d6d"),
        (0, 1, 4, 5, 8, 9, 3, 2, 7, 6, 11, 10),
        32,
    ),
)


def load_code(source, folder):
    slug, digest = source
    name = f"{slug}.json"
    if folder is None:
        with urlopen(f"{SOURCE}/{name}", timeout=20) as response:
            data = response.read()
    else:
        data = (folder / name).read_bytes()
    if hashlib.sha256(data).hexdigest() != digest:
        raise ValueError(f"{name} differs from the pinned catalogue file")
    return json.loads(data)


def span(rows, permutation):
    vectors = {0}
    for support in rows:
        word = sum(1 << permutation[i] for i in support)
        vectors |= {vector ^ word for vector in vectors}
    return vectors


def check_pair(first, second, permutation, expected_size):
    identity = tuple(range(second["n"]))
    if first["n"] != second["n"] or sorted(permutation) != list(identity):
        raise ValueError("Invalid qubit permutation")
    if first["code_type"] != "CSS" or second["code_type"] != "CSS":
        raise ValueError("Both inputs must be CSS codes")

    wrong = (permutation[1], permutation[0], *permutation[2:])
    for side in ("X", "Z"):
        source = first["checks"][side]
        target_span = span(second["checks"][side], identity)
        if len(target_span) != expected_size or span(source, permutation) != target_span:
            raise ValueError(f"{side} row spaces do not match")
        if span(source, wrong) == target_span:
            raise ValueError(f"The {side} negative control unexpectedly passed")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", type=Path, help="directory with the four pinned JSON files")
    args = parser.parse_args()
    for source, target, permutation, expected_size in PAIRS:
        first = load_code(source, args.source_dir)
        second = load_code(target, args.source_dir)
        check_pair(first, second, permutation, expected_size)
        print(f"{source[0]} -> {target[0]}: PASS, X and Z spans of size {expected_size}")
        print("Negative control rejected in both sectors")


if __name__ == "__main__":
    main()
