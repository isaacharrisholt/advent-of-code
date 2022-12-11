import math
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


# move_tail moves the tail to follow the head
def move_tail(
    head: tuple[int, int],
    tail: tuple[int, int],
    direction: str,
) -> tuple[int, int]:
    x_head, y_head = head
    x_tail, y_tail = tail
    dist = math.sqrt((x_head - x_tail) ** 2 + (y_head - y_tail) ** 2)

    if dist in {0, 1, math.sqrt(2)}:  # Tail overlaps head or is touching
        return tail

    if dist == 2:  # Straight line between head and tail
        return move_unit(tail, direction)

    # Tail is diagonal to head, move tail to be 'behind' head's last movement
    match direction:
        case 'U':
            return x_head, y_head - 1
        case 'D':
            return x_head, y_head + 1
        case 'L':
            return x_head + 1, y_head
        case 'R':
            return x_head - 1, y_head


def move(
    head: tuple[int, int],
    tail: tuple[int, int],
    direction: str,
    distance: int,
    visited: set[tuple[int, int]],
) -> tuple[tuple[int, int], tuple[int, int]]:
    for _ in range(distance):
        head = move_unit(head, direction)
        tail = move_tail(head, tail, direction)
        visited.add(tail)
    return head, tail


def main():
    instructions = parse_instructions()

    # Initial positions
    head = (0, 0)
    tail = (0, 0)

    # Positions visited
    visited = {tail}

    for instruction in instructions:
        direction, distance = instruction
        head, tail = move(head, tail, direction, distance, visited)

    print(f'Visited {len(visited)} positions')


if __name__ == '__main__':
    main()
