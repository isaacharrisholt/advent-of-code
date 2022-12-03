from pathlib import Path


def get_priority(x: str) -> int:
    return ord(x) - 38 if x.isupper() else ord(x) - 96


def find_shared(line: str) -> str:
    return set(line[:len(line) // 2]).intersection(
        set(line[len(line) // 2:])
    ).pop()


def main():
    input_data = Path('input.txt').read_text().splitlines()
    print(sum(get_priority(find_shared(line)) for line in input_data))


if __name__ == '__main__':
    main()
