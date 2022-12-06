# AOC 2022 Day 3
from aocd import get_data


def convert_item_to_priority(item: str):
    if item.islower():
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27


def format_input(input_str):
    return input_str.split('\n')


def split_rucksack_into_compartments(rucksacks):
    return [
        (list(rucksack[: len(rucksack) // 2]), list(rucksack[len(rucksack) // 2 :]))
        for rucksack in rucksacks
    ]


def split_groups(rucksacks):
    groups = []
    for i in range(0, len(rucksacks), 3):
        group = []
        for bag in rucksacks[i : i + 3]:
            group.append(bag)
        groups.append(group)
    return groups


def get_common_items(*args):
    total = set(args[0])
    if len(args) == 1:
        return total
    for arg in args[1:]:
        total &= set(arg)
    return list(total)


def part1(inputs):
    split_rucksack = split_rucksack_into_compartments(inputs)
    total = 0
    for left, right in split_rucksack:
        items = get_common_items(left, right)
        assert len(items) == 1
        priority = convert_item_to_priority(items[0])
        total += priority
    print(f'{total=}')


def part2(inputs):
    split_items = split_groups(inputs)
    total = 0
    for a, b, c in split_items:
        items = get_common_items(a, b, c)
        assert len(items) == 1
        priority = convert_item_to_priority(items[0])
        total += priority
    print(f'{total=}')


def main():

    test_data = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

    test_inputs = format_input(test_data)
    part1(test_inputs)
    part2(test_inputs)

    data = get_data(day=3, year=2022)
    inputs = format_input(data)
    part1(inputs)
    part2(inputs)

    #### Part 2 ####


if __name__ == '__main__':
    main()
