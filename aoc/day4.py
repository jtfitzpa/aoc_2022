# AOC 2022 Day 4
from aocd import get_data


def convert_item_to_priority(item: str):
    if item.islower():
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27


def format_input(input_str):
    return input_str.split('\n')


def split_into_paired_ranges(inputs):
    paired_ranges = []
    for line in inputs:
        ranges = line.split(',')
        ranges = [r.split('-') for r in ranges]
        paired_range = [set(range(int(u), int(l) + 1)) for u, l in ranges]
        paired_ranges.append(paired_range)
    return paired_ranges


def is_subset(a: set, b: set):
    return a.union(b) == b


def any_overlap(a: set, b: set):
    return len(a.intersection(b)) > 0


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
    paired_ranges = split_into_paired_ranges(inputs)
    count = 0
    for left, right in paired_ranges:
        if is_subset(left, right) or is_subset(right, left):
            count += 1
    return count


def part2(inputs):
    paired_ranges = split_into_paired_ranges(inputs)
    count = 0
    for left, right in paired_ranges:
        if any_overlap(left, right):
            count += 1
    return count


def main():

    test_data = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

    test_inputs = format_input(test_data)
    count = part1(test_inputs)
    count2 = part2(test_inputs)
    print(f'Test Part 1: {count=}')
    print(f'Test Part 2: {count2=}')

    data = get_data(day=4, year=2022)
    inputs = format_input(data)
    count = part1(inputs)
    count2 = part2(inputs)
    print(f'Part 1: {count=}')
    print(f'Part 2: {count2=}')


if __name__ == '__main__':
    main()
