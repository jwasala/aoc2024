from collections import Counter
import os


def parse(path: str) -> tuple[list[int], list[int]]:
    with open(path) as f:
        lines = f.read().splitlines()
    lines = [list(map(int, line.split("   "))) for line in lines]
    return list(map(list, zip(*lines)))


def part1(xs: list[int], ys: list[int]) -> int:
    return sum(map(lambda xy: abs(xy[0] - xy[1]), zip(sorted(xs), sorted(ys))))


def part2(xs: list[int], ys: list[int]) -> int:
    x_cn, y_cn = Counter(xs), Counter(ys)
    return sum(map(lambda kv: kv[1] * kv[0] * y_cn.get(kv[0], 0), x_cn.items()))


if __name__ == "__main__":
    input_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "day01.txt")
    xs, ys = parse(input_file)
    print(part1(xs, ys))
    print(part2(xs, ys))
