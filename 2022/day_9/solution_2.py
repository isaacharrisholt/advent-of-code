import math
import sys
from pathlib import Path


def parse_instructions() -> list[tuple[str, int]]:
    input_data = Path("input.txt").read_text().splitlines()
    return [(x.split()[0], int(x.split()[1])) for x in input_data]


def move_unit(
    start: tuple[int, int],
    direction: str,
) -> tuple[int, int]:
    x, y = start
    match direction:
        case 'U':
            y += 1
        case 'D':
            y -= 1
        case 'L':
            x -= 1
        case 'R':
            x += 1
    return x, y


def move_knot(
    prev: tuple[int, int],
    curr: tuple[int, int],
    direction: str,
) -> tuple[int, int]:
    x_prev, y_prev = prev
    x_curr, y_curr = curr
    dist = math.sqrt((x_prev - x_curr) ** 2 + (y_prev - y_curr) ** 2)

    if dist in {0, 1, math.sqrt(2)}:  # Curr overlaps prev or is touching
        return curr

    # Diagonal line between prev and curr
    if dist == math.sqrt(5):  # e.g. right 2, up 1
        x_diff = x_prev - x_curr
        y_diff = y_prev - y_curr
        x_new = int(
            x_prev +
            (0 if abs(x_diff) == 1 else -1 * (x_diff / abs(x_diff)))
        )
        y_new = int(
            y_prev +
            (0 if abs(y_diff) == 1 else -1 * (y_diff / abs(y_diff)))
        )
        return x_new, y_new

    # Move one unit in direction of prev
    x_diff = x_prev - x_curr
    y_diff = y_prev - y_curr
    return x_curr + x_diff // 2, y_curr + y_diff // 2


def draw_grid(size: int, knots, offset: int):
    grid = [['.' for _ in range(size)] for _ in range(size)]
    grid[size - offset - 1][offset] = 's'
    for i, knot in reversed(list(enumerate(knots))):
        if not i:
            i = 'H'
        x, y = knot
        grid[size - (y + offset) - 1][x + offset] = str(i)
    for row in grid:
        print(''.join(row))


def move(
    knots: list[tuple[int, int]],
    direction: str,
    distance: int,
    visited: set[tuple[int, int]],
    debug: bool = False,
) -> list[tuple[int, int]]:
    for j in range(distance):
        knots[0] = move_unit(knots[0], direction)
        if debug:
            print(f'{direction} {distance}: {j+1}/{distance}')
        for i in range(1, len(knots)):
            knots[i] = move_knot(knots[i - 1], knots[i], direction)
            # print(f'{knots[i]} Knot {i}')

        if debug:
            draw_grid(30, knots, 15)
            print()
            breakpoint()
        visited.add(knots[-1])
    return knots


def main():
    debug = False
    if '--debug' in sys.argv:
        debug = True
    instructions = parse_instructions()

    # Initial positions
    knots = [(0, 0) for _ in range(10)]

    # Positions visited
    visited = {knots[-1]}

    for instruction in instructions:
        direction, distance = instruction
        knots = move(knots, direction, distance, visited, debug)

    print(f'Visited {len(visited)} positions')


if __name__ == '__main__':
    main()
