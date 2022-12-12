from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

Position = tuple[int, int]


def parse_input() -> (list[list[str]], Position):
    data = [
        list(line) for line in
        Path("input.txt").read_text().splitlines()
    ]
    start = None
    end = None
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if char == "S":
                start = (i, j)
            elif char == "E":
                end = (i, j)
    return data, start, end


@dataclass
class Node:
    pos: Position
    parent: Node | None = None
    f: int = 0
    g: int = 0
    h: int = 0

    def __eq__(self, other: Node) -> bool:
        return self.pos == other.pos


def a_star(
    data: list[list[str]],
    start: Position,
    end: Position,
) -> list[Position]:
    start_node = Node(pos=start, parent=None)
    end_node = Node(pos=end, parent=None)

    open_list = [start_node]
    closed_list = []

    while open_list:
        curr_node = open_list[0]
        curr_index = 0

        for i, item in enumerate(open_list):
            if item.f < curr_node.f:
                curr_node = item
                curr_index = i

        open_list.pop(curr_index)
        closed_list.append(curr_node)

        if curr_node == end_node:
            path = []
            curr = curr_node
            while curr is not None:
                path.append(curr.pos)
                curr = curr.parent
            return path[::-1]

        y, x = curr_node.pos
        curr_val = data[y][x]
        curr_ord = ord(curr_val)
        if curr_val == "S":
            curr_ord = ord('a')

        children = []
        # 4 possible directions
        for direction in [
            (0, -1),
            (0, 1),
            (-1, 0),
            (1, 0),
        ]:
            new_pos = (y + direction[0], x + direction[1])
            new_y, new_x = new_pos

            try:
                new_val = data[new_y][new_x]
            except IndexError:
                # Out of bounds
                continue

            new_ord = ord(new_val)
            if new_val == "S":
                new_ord = ord('a')
            elif new_val == "E":
                new_ord = ord('z')

            # Check if allowed move
            if new_ord - curr_ord > 1:
                continue

            new_node = Node(pos=new_pos, parent=curr_node)
            children.append(new_node)

        for child in children:
            if child in closed_list:
                continue

            child.g = curr_node.g + 1
            child.h = (
                (child.pos[0] - end_node.pos[0]) ** 2
                + (child.pos[1] - end_node.pos[1]) ** 2
            )
            child.f = child.g + child.h

            if child in open_list:
                continue

            open_list.append(child)


def main():
    data, start, end = parse_input()

    path = a_star(data, start, end)

    for pos in path:
        y, x = pos
        data[y][x] = ' '

    for line in data:
        print(''.join(line))

    print(path)
    print(len(path) - 1)  # Num steps


if __name__ == '__main__':
    main()
