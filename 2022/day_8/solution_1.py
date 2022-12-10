from pathlib import Path


def parse_input() -> list[list[tuple[int, bool]]]:
    """Create a 2x2 matrix of the input data, where each datum becomes a tuple
    of (height, visible) where visible is initially False."""
    return [
        [
            (int(num), False)
            for num in group
        ]
        for group in Path('input.txt').read_text().splitlines()
    ]


def update_row_visibility(
    row: list[tuple[int, bool]],
    reverse: bool = False,
) -> list[tuple[int, bool]]:
    row = row.copy()
    heights = []

    gen = enumerate(row) if not reverse else reversed(list(enumerate(row)))

    for i, (height, visible) in gen:
        if not heights:
            # The first and last elements are always visible
            row[i] = (height, True)
            heights.append(height)
            continue

        if height > max(heights):
            # If the current element is taller than the previous element, it is
            # visible
            row[i] = (height, True)
        heights.append(height)

    return row


def update_column_visibility(
    matrix: list[list[tuple[int, bool]]],
    column: int,
) -> list[list[tuple[int, bool]]]:
    """Update the visibility of a column in the matrix."""
    matrix = [row.copy() for row in matrix]
    heights = []
    for i, row in enumerate(matrix):
        if not heights:
            # The first and last elements are always visible
            matrix[i][column] = (row[column][0], True)
            heights.append(row[column][0])
            continue

        if row[column][0] > max(heights):
            # If the current element is taller than the previous element, it is
            # visible
            matrix[i][column] = (row[column][0], True)
        heights.append(row[column][0])

    return matrix


def main():
    grid = parse_input()
    for i, row in enumerate(grid):
        row = update_row_visibility(row)
        row = update_row_visibility(row, reverse=True)
        grid[i] = row

    for i in range(len(grid[0])):
        grid = update_column_visibility(grid, i)
        grid = update_column_visibility(grid[::-1], i)[::-1]

    # Count the number of visible elements
    print(sum(visible for _, visible in sum(grid, [])))


if __name__ == '__main__':
    main()
