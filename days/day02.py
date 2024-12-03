import os


def parse(path: str) -> list[list[int]]:
    with open(path) as f:
        lines = f.read().splitlines()
    lines = [list(map(int, line.split(" "))) for line in lines]
    return lines


def _is_safe(xs: list[int]) -> bool:
    return all(map(lambda xy: 0 < abs(xy[0] - xy[1]) < 4, zip(xs, xs[1:]))) and all(
        map(
            lambda xyz: xyz[0] < xyz[1] < xyz[2] or xyz[0] > xyz[1] > xyz[2],
            zip(xs, xs[1:], xs[2:]),
        )
    )


def part1(xss: list[list[int]]) -> int:
    return sum(map(_is_safe, xss))


def part2(xss: list[list[int]]) -> int:
    return sum(
        map(
            lambda xs: _is_safe(xs)
            or any(_is_safe(xs[:i] + xs[i + 1 :]) for i in range(len(xs))),
            xss,
        )
    )


if __name__ == "__main__":
    input_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "day02.txt")
    xss = parse(input_file)
    print(part1(xss))
    print(part2(xss))
