import os
import re


def parse(path: str) -> list[list[tuple[int, int, bool]]]:
    with open(path) as f:
        lines = f.read().splitlines()
    out = []
    enabled = True
    for line in lines:
        groups = re.findall("(mul\((\d+),(\d+)\)|don't\(\)|do\(\))", line)
        for op, a, b in groups:
            if op == "do()":
                enabled = True
            elif op == "don't()":
                enabled = False
            else:
                out.append((int(a), int(b), enabled))
    return out


def product_sum(xys: list[tuple[int, int]]) -> int:
    return sum(map(lambda xy: xy[0] * xy[1], xys))


if __name__ == "__main__":
    input_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "day03.txt")

    xys1 = parse(input_file)
    xys2 = [xy for xy in xys1 if xy[2]]  # skip disabled
    print(product_sum(xys1))
    print(product_sum(xys2))
