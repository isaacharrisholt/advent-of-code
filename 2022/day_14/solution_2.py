import copy
from pathlib import Path

Position = tuple[int, int]


def parse_input() -> list[list[Position]]:
    return [
        [
            (int(l.split(',')[0]), int(l.split(',')[1]))
            for l in line.split(' -> ')
        ]
        for line in Path('input.txt').read_text().splitlines()
    ]


def interpolate(p1: Position, p2: Position) -> set[Position]:
    x1, y1 = p1
    x2, y2 = p2

    if x1 == x2:
        return {(x1, y) for y in range(min(y1, y2), max(y1, y2) + 1)}
    elif y1 == y2:
        return {(x, y1) for x in range(min(x1, x2), max(x1, x2) + 1)}
    else:
        raise ValueError(f'Points {p1} and {p2} are not aligned')


def get_walls(paths: list[list[Position]]) -> set[Position]:
    walls = set()
    for path in paths:
        for i in range(len(path) - 1):
            walls |= interpolate(path[i], path[i + 1])
    return walls


def generate_grid(x_size: int, y_size: int) -> list[list[str]]:
    grid = [['.' for _ in range(x_size)] for _ in range(y_size)]
    grid[-1] = ['#' for _ in range(x_size)]
    return grid


def fill_grid(grid: list[list[str]], walls: set[Position]) -> list[list[str]]:
    grid = copy.deepcopy(grid)
    for x, y in walls:
        grid[y][x] = '#'
    return grid


def print_grid(grid: list[list[str]]) -> None:
    for line in grid:
        print(''.join(line))


def run_sand_sim(grid: list[list[str]], start: Position) -> int:
    count = 0
    start_x, start_y = start
    while grid[start_y][start_x] == '+':
        x, y = start

        while True:
            if grid[y + 1][x] == '.':
                y += 1
                continue

            potential_floors = [
                (x - 1, y),
                (x, y),
                (x + 1, y),
            ]

            if all(grid[y1][x1] != '.' for x1, y1 in potential_floors):
                # Sand has landed
                grid[y][x] = 'o'
                count += 1
                break

            if grid[y + 1][x] != '.':
                # Object below
                if grid[y + 1][x - 1] == '.':
                    x -= 1
                    y += 1
                    continue
                elif grid[y + 1][x + 1] == '.':
                    x += 1
                    y += 1
                    continue
                else:
                    # Sand has landed
                    grid[y][x] = 'o'
                    count += 1
                    break

    return count


def main():
    input_data = parse_input()

    walls = get_walls(input_data)

    max_y = max(y for _, y in walls)

    y_size = max_y + 3
    x_size = 2 * y_size + 20  # Sand piles can be 2x as wide as they are tall

    # (500, 0) is the starting position, and should lie in the middle of the
    # grid
    min_x = 500 - x_size // 2

    adjusted_points = {(x - min_x, y) for x, y in walls}
    adjusted_start = (500 - min_x, 0)

    grid = generate_grid(x_size, y_size)
    grid = fill_grid(grid, adjusted_points)
    grid[adjusted_start[1]][adjusted_start[0]] = '+'

    print_grid(grid)

    count = run_sand_sim(grid, adjusted_start)

    print_grid(grid)
    print(count)


if __name__ == '__main__':
    main()
