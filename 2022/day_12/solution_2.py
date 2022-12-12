from pathlib import Path

Position = tuple[int, int]


def parse_input() -> (list[list[str]], set[Position], Position):
    data = [
        list(line) for line in
        Path("input.txt").read_text().splitlines()
    ]
    starts = set()
    end = None
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if char in ("S", "a"):
                starts.add((i, j))
            elif char == "E":
                end = (i, j)
    return data, starts, end


def walk_path(
    data: list[list[str]],
    start: Position,
    end: Position,
):
    points_to_visit = [start]
    came_from = {start: None}

    point = start

    while points_to_visit:
        point = points_to_visit.pop(0)
        if point == end:
            break

        y, x = point
        val = data[y][x]

        val_ord = ord(val)
        if val == 'S':
            val_ord = ord('a')

        for direction in (
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ):
            new_point = (point[0] + direction[0], point[1] + direction[1])
            new_y, new_x = new_point

            if new_point in came_from:
                continue

            if new_y < 0 or new_y >= len(data):
                continue

            if new_x < 0 or new_x >= len(data[0]):
                continue

            new_val = data[new_y][new_x]
            new_ord = ord(new_val)

            if new_val == 'S':
                new_ord = ord('a')
            elif new_val == 'E':
                new_ord = ord('z')

            if new_ord - val_ord <= 1:
                came_from[new_point] = point
                points_to_visit.append(new_point)

    if point != end:
        return None

    current = end
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]

    return path


def main():
    data, starts, end = parse_input()

    shortest_path = None

    for start in starts:
        path = walk_path(data, start, end)
        if path is None:
            continue

        if shortest_path is None or len(path) < len(shortest_path):
            shortest_path = path

    print(len(shortest_path))


if __name__ == '__main__':
    main()
