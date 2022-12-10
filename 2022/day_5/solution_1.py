import re
from pathlib import Path


def get_input() -> list[str]:
    return Path('input.txt').read_text().splitlines()


def create_stacks(input_lines) -> list[list[str]]:
    input_data = [
        line for line in input_lines
        if '[' in line
    ]

    # Split into individual characters
    split_data = [
        [line[i] for i in range(1, len(line), 4)]
        for line in input_data
    ]

    # Transpose and reverse the list of lists to create the stacks
    return [
        [row[i] for row in reversed(split_data) if row[i] != ' ']
        for i in range(len(split_data[0]))
    ]


def parse_instructions(input_lines) -> list[tuple[int, int, int]]:
    # Extract three numbers from each line
    instructions = [
        re.findall(r'\d+', line)
        for line in input_lines
        if line.startswith('move')
    ]

    return [
        (int(i[0]), int(i[1]) - 1, int(i[2]) - 1)  # Sub 1 to make 0-indexed
        for i in instructions
    ]


def main():
    input_data = get_input()
    stacks = create_stacks(input_data)
    instructions = parse_instructions(input_data)

    for instruction in instructions:
        # Move the top X crates from stack A to stack B
        for _ in range(instruction[0]):
            stacks[instruction[2]].append(stacks[instruction[1]].pop())

    print(''.join(stack[-1] for stack in stacks))


if __name__ == '__main__':
    main()
