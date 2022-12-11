import re
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Monkey:
    items: list[int]
    operation: str
    test_divisor: int
    true_recipient: int
    false_recipient: int
    inspected_items: int = 0

    def inspect(self) -> tuple[int, int]:
        self.inspected_items += 1
        old = self.items.pop(0)
        new = eval(self.operation) // 3

        if new % self.test_divisor == 0:
            return new, self.true_recipient
        else:
            return new, self.false_recipient


def parse_monkey(lines: list[str]) -> Monkey:
    items = [
        int(item)
        for item in lines[0].replace('Starting items:', '').strip().split(', ')
    ]
    operation = lines[1].replace('Operation: new =', '').strip()
    test_divisor = int(re.search(r'\d+', lines[2]).group(0))
    true_recipient = int(re.search(r'\d+', lines[3]).group(0))
    false_recipient = int(re.search(r'\d+', lines[4]).group(0))

    return Monkey(
        items,
        operation,
        test_divisor,
        true_recipient,
        false_recipient,
    )


def parse_input() -> dict[int, Monkey]:
    input_data = Path('input.txt').read_text()

    monkeys = {}

    for monkey in input_data.split('\n\n'):
        lines = monkey.splitlines()
        monkey_id = int(re.search(r'\d+', lines[0]).group(0))
        monkey_data = parse_monkey(lines[1:])
        monkeys[monkey_id] = monkey_data

    return monkeys


def main():
    monkeys = parse_input()

    for _ in range(20):
        for monkey_id, monkey in monkeys.items():
            for _ in range(len(monkey.items)):
                item, recipient = monkey.inspect()
                monkeys[recipient].items.append(item)

    ranked_monkeys = sorted(
        monkeys.values(),
        key=lambda x: x.inspected_items,
        reverse=True,
    )
    monkey_business = (
        ranked_monkeys[0].inspected_items * ranked_monkeys[1].inspected_items
    )
    print(monkey_business)


if __name__ == '__main__':
    main()
