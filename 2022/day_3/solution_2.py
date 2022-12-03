from pathlib import Path


def get_priority(x: str) -> int:
    return ord(x) - 38 if x.isupper() else ord(x) - 96


def find_shared(*chunks: str) -> str:
    chunk_set = set(chunks[0])
    for chunk in chunks[1:]:
        chunk_set.intersection_update(set(chunk))
    return chunk_set.pop()


def main():
    input_data = Path('input.txt').read_text().splitlines()
    chunked_data = [input_data[i:i+3] for i in range(0, len(input_data), 3)]
    answer = sum(
        get_priority(find_shared(*chunk)) for chunk in chunked_data
    )
    print(answer)


if __name__ == '__main__':
    main()
