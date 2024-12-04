from itertools import chain
import os
import re


def parse(path: str) -> list[str]:
    with open(path) as f:
        return f.read().splitlines()


def part1(xs: list[str]):
    h, w = len(xs), len(xs[0])
    horizontal = sum(x.count(word) for x in xs for word in ("XMAS", "SAMX"))
    vertical = sum(
        x.count(word) for x in map("".join, list(zip(*xs))) for word in ("XMAS", "SAMX")
    )
    diag = sum(
        "".join(
            ord[i0 + i][j0 + i] for i in range(max(w, h)) if i0 + i < h and j0 + i < w
        ).count(word)
        for ord in (xs, [list(reversed(x)) for x in xs])
        for (i0, j0) in chain(zip(range(h), [0] * h), zip([0] * (w - 1), range(1, w)))
        for word in ("XMAS", "SAMX")
    )
    return horizontal + vertical + diag


def part2(xs: list[str]):
    patterns = [
        "M.S.A.M.S",
        "M.M.A.S.S",
        "S.S.A.M.M",
        "S.M.A.S.M",
    ]
    out = 0
    for i in range(len(xs) - 2):
        for j in range(len(xs[0]) - 2):
            window = "".join(map(lambda x: x[j : j + 3], xs[i : i + 3]))
            if any(re.match(pattern, window) for pattern in patterns):
                out += 1
    return out


if __name__ == "__main__":
    input_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "day04.txt")

    xs = parse(input_file)
    print(part1(xs))
    print(part2(xs))
