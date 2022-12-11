from pathlib import Path
from dataclasses import dataclass


@dataclass
class Instruction:
    length_in_cycles: int
    value: int
    cycles_completed: int = 0


def parse_instructions():
    """Return instructions in the format (cycles, V)"""
    input_data = Path('input.txt').read_text().splitlines()
    split = [x.split() for x in input_data]
    results = []

    for line in split:
        if line[0] == 'noop':
            results.append((1, 0))
        elif line[0] == 'addx':
            results.append((2, int(line[1])))
        else:
            raise ValueError(f'Unknown instruction: {line[0]}')

    return results


def main():
    instructions = parse_instructions()
    cycles_completed = 0
    current_idx = 0
    curr_ins = Instruction(
        length_in_cycles=instructions[current_idx][0],
        value=instructions[current_idx][1],
    )
    register = 1

    pixel = -1
    line = 0

    screen = ['.' * 40 for _ in range(6)]

    while True:
        if pixel in {register - 1, register, register + 1}:
            screen[line] = screen[line][:pixel] + '#' + screen[line][pixel + 1:]
        else:
            screen[line] = screen[line][:pixel] + '.' + screen[line][pixel + 1:]

        if curr_ins.cycles_completed == curr_ins.length_in_cycles:
            register += curr_ins.value
            current_idx += 1
            if current_idx == len(instructions):
                break
            curr_ins = Instruction(
                length_in_cycles=instructions[current_idx][0],
                value=instructions[current_idx][1],
            )
        cycles_completed += 1
        curr_ins.cycles_completed += 1

        pixel += 1
        if pixel == 40:
            pixel = 0
            line += 1
        if line == 6:
            line = 0

    for l in screen:
        print(l)


if __name__ == '__main__':
    main()
