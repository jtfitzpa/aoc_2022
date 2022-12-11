# AOC 2022 Day 11
from aocd import get_data
from collections import defaultdict

from tqdm.auto import tqdm
from typing import List, Dict


class Monkey:
    def __init__(
        self,
        id: int,
        starting_items: List[int],
        operation: str,
        test_val: int,
        test_true: int,
        test_false: int,
    ):
        self.norm_val = 1
        self.id = id
        self.starting_items = starting_items
        self._operation = operation
        self.test_val = test_val
        self.test_true = test_true
        self.test_false = test_false
        self.num_inspections = 0

    def inspect(self) -> Dict[int, List[int]]:
        throw_dict = defaultdict(list)
        while self.starting_items:
            item = self.starting_items.pop(0)
            self.num_inspections += 1
            item = self.operation(item)
            # item //= 3
            next_monkey = self.test(item)
            item %= self.norm_val
            throw_dict[next_monkey].append(item)
        return throw_dict

    def operation(self, old: int) -> int:
        return eval(self._operation)

    def test(self, x: int) -> int:

        if x % self.test_val == 0:
            return self.test_true
        else:
            return self.test_false

    def catch(self, items: List[int]) -> None:
        self.starting_items.extend(items)


def format_input(input_str: str) -> Dict[int, Monkey]:
    monkeys = {}
    lines = input_str.split('\n')
    all_test_vals = 1
    for i in range(0, len(lines), 7):
        line_chunk = lines[i : i + 7]
        id = int(line_chunk[0].strip(':').split(' ')[1])
        starting_items = line_chunk[1].split(':')[1].split(',')
        operation = line_chunk[2].split('=')[1]
        test_val = int(line_chunk[3].split(' ')[-1])
        all_test_vals *= test_val
        starting_items = [int(item) for item in starting_items]
        test_true = int(line_chunk[4].split(' ')[-1])
        test_false = int(line_chunk[5].split(' ')[-1])

        monkey = Monkey(id, starting_items, operation, test_val, test_true, test_false)
        monkeys[id] = monkey
    for monkey in monkeys.values():
        monkey.norm_val = all_test_vals

    return monkeys


class Barrel:
    def __init__(self, monkeys: Dict[int, Monkey]) -> None:
        self.monkeys = monkeys

    def round(self) -> None:
        for id, monkey in self.monkeys.items():
            throw_dict = monkey.inspect()
            for monkey_id, items in throw_dict.items():
                self.monkeys[monkey_id].catch(items)


def part1(monkeys: List[Monkey]) -> int:
    barrel = Barrel(monkeys=monkeys)

    for i in tqdm(range(10000)):
        barrel.round()
        if i + 1 in [
            1,
            20,
            1000,
            2000,
            3000,
            4000,
            5000,
            6000,
            7000,
            8000,
            9000,
            10000,
        ]:

            inspect = [monkey.num_inspections for monkey in barrel.monkeys.values()]
            print(f'round: {i+1}')
            print(inspect)

    inspect = [monkey.num_inspections for monkey in barrel.monkeys.values()]
    print(inspect)
    inspect = sorted(inspect)
    monkey_business = inspect[-2] * inspect[-1]
    return monkey_business


def main():
    test_data = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

    monkeys = format_input(test_data)
    total = part1(monkeys)
    print(f'Part 2: {total=}')

    data = get_data(day=11, year=2022)
    commands = format_input(data)
    total = part1(commands)
    print(f'Part 2: {total=}')


if __name__ == '__main__':
    main()
