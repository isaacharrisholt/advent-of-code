import copy
from pathlib import Path

Num = int | float


def parse_input() -> list[tuple[list, list]]:
    data = Path('input.txt').read_text()

    pairs = data.split('\n\n')

    return [(eval(a), eval(b)) for a, b in (pair.split('\n') for pair in pairs)]


def compare_lists(left: list, right: list) -> bool | None:
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
                return True
            elif left_val > right_val:
                return False
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
        return False
    elif right:
        return True
    else:
        return None


def main():
    input_data = parse_input()

    results = []

    for i, (left, right) in enumerate(input_data):
        result = compare_lists(left, right)
        results.append((i + 1, result))

    print(sum(result[0] for result in results if result[1]))


if __name__ == '__main__':
    main()
