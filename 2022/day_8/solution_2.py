from pathlib import Path
import copy


def parse_input() -> list[list[int]]:
    """Create a 2x2 matrix of the input data."""
    return [
        [int(i) for i in line]
        for line in Path('input.txt').read_text().splitlines()
    ]


def count_visible_in_column(
    matrix: list[list[int]],
    row: int,
    column: int,
    reverse: bool = False,
) -> int:
    """Count the number of visible elements above the given element."""
    count = 0
    tree_height = matrix[row][column]
    gen = range(row - 1, -1, -1) if reverse else range(row + 1, len(matrix))
    for i in gen:
        count += 1

        if matrix[i][column] >= tree_height:
            break
    return count


def count_visible_in_row(
    matrix: list[list[int]],
    row: int,
    column: int,
    reverse: bool = False,
) -> int:
    """Count the number of visible elements above the given element."""
    count = 0
    tree_height = matrix[row][column]
    gen = (
        range(column - 1, -1, -1) if reverse
        else range(column + 1, len(matrix[0]))
    )

    for i in gen:
        count += 1

        if matrix[row][i] >= tree_height:
            break
    return count


def main():
    grid = parse_input()

    scores = copy.deepcopy(grid)

    for y, row in enumerate(grid):
        for x, height in enumerate(row):
            # Count above
            above = count_visible_in_column(grid, y, x, reverse=True)

            # Count below
            below = count_visible_in_column(grid, y, x)

            # Count left
            left = count_visible_in_row(grid, y, x, reverse=True)

            # Count right
            right = count_visible_in_row(grid, y, x)

            score = above * below * left * right
            scores[y][x] = score

    # Max score
    print(max(max(row) for row in scores))


if __name__ == '__main__':
    main()
