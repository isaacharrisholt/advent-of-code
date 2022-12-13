import copy
import functools
from pathlib import Path

Num = int | float


def parse_input() -> list:
    data = Path('input.txt').read_text()

    pairs = data.split('\n')

    return [eval(line.strip()) for line in pairs if line.strip()]


def compare_lists(left: list, right: list) -> int | None:
    left = copy.deepcopy(left)
    right = copy.deepcopy(right)

    while left and right:
        left_val = left.pop(0)
        right_val = right.pop(0)

        if isinstance(left_val, list) and isinstance(right_val, list):
            result = compare_lists(left_val, right_val)
            if result is not None:
                return result
            continue

        if isinstance(left_val, Num) and isinstance(right_val, Num):
            if left_val < right_val:
                return -1
            elif left_val > right_val:
                return 1
            continue

        if isinstance(left_val, Num) and isinstance(right_val, list):
            result = compare_lists([left_val], right_val)
            if result is not None:
                return result
            continue

        if isinstance(left_val, list) and isinstance(right_val, Num):
            result = compare_lists(left_val, [right_val])
            if result is not None:
                return result
            continue

    if left:
        return 1
    elif right:
        return -1
    else:
        return None


def main():
    input_data = parse_input()

    input_data.extend(
        [
            [[2]],
            [[6]],
        ],
    )

    sorted_lines = sorted(input_data, key=functools.cmp_to_key(compare_lists))

    idx_div_1 = sorted_lines.index([[2]]) + 1
    idx_div_2 = sorted_lines.index([[6]]) + 1

    print(idx_div_1 * idx_div_2)


if __name__ == '__main__':
    main()
