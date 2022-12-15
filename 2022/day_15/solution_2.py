import re
from pathlib import Path

import numpy as np

Position = tuple[int, int]


def parse_input() -> list[tuple[Position, Position]]:
    input_data = Path('input.txt').read_text().splitlines()

    results = []

    for line in input_data:
        digits = re.findall(r'-?\d+', line)
        results.append(
            (
                (int(digits[0]), int(digits[1])),
                (int(digits[2]), int(digits[3])),
            )
        )

    return results


def get_taxicab_distance(a: Position, b: Position) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def walk_perimeter(sensor: Position, distance: int) -> set[Position]:
    s_x, s_y = sensor
    x = s_x - distance - 1
    y = s_y

    positions = set()

    while x < s_x:
        positions.add((x, y))
        x += 1
        y += 1

    while y > s_y:
        positions.add((x, y))
        x += 1
        y -= 1

    while x > s_x:
        positions.add((x, y))
        x -= 1
        y += 1

    while y < s_y:
        positions.add((x, y))
        x -= 1
        y -= 1

    return positions


def main():
    input_data = parse_input()

    input_data_with_taxicab_distances = [
        (sensor, beacon, get_taxicab_distance(sensor, beacon))
        for sensor, beacon in input_data
    ]

    point = None

    for i, (sensor, _, taxicab_distance) in enumerate(
        input_data_with_taxicab_distances
    ):
        print(f'{i+1}/{len(input_data_with_taxicab_distances)}')
        perimeter = walk_perimeter(sensor, taxicab_distance)
        hidden = False

        for p in perimeter:
            x, y = p
            hidden = True
            if 0 <= x <= 4_000_000 and 0 <= y <= 4_000_000:
                for s, _, d in input_data_with_taxicab_distances:
                    if get_taxicab_distance(s, p) <= d:
                        hidden = False
                        break
                if hidden:
                    point = p
                    break
        if hidden:
            break

    freq = 4_000_000 * point[0] + point[1]
    print(point)
    print(freq)


if __name__ == '__main__':
    main()
