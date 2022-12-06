# AOC 2022 Day 5
from aocd import get_data
from collections import defaultdict


def format_input(input_str):
    lines = input_str.split('\n')
    split_idx = lines.index('')
    return lines[:split_idx], lines[split_idx + 1 :]


def clean_stacks(stacks):

    all_lines = []
    for line in stacks:
        splits = line.split(' ')
        out_splits = []
        while splits:
            if splits[0] == '':
                out_splits.append(splits[0])
                splits = splits[4:]
            else:
                out_splits.append(splits[0])
                splits = splits[1:]

        all_lines.append(out_splits)
    return all_lines


def create_stacks(inputs):
    stack_ids = [int(i) for i in inputs[-1].split(' ') if i]

    stack_lines = clean_stacks(inputs[-2::-1])

    stacks = defaultdict(list)
    for line in stack_lines:
        cols = line
        for i, col in enumerate(cols):
            if cols[i]:
                _, val, _ = col
                stacks[stack_ids[i]].append(val.strip('[').strip(']'))

    return stacks


def parse_instructions(inputs):
    instructions = []
    for line in inputs:
        _, count, _, start, _, end = line.split(' ')
        instructions.append((int(count), int(start), int(end)))
    return instructions


def get_common_items(*args):
    total = set(args[0])
    if len(args) == 1:
        return total
    for arg in args[1:]:
        total &= set(arg)
    return list(total)


def part1(stack, instructions):

    stacks = create_stacks(stack)
    instructions = parse_instructions(instructions)

    for instruction in instructions:
        (count, start, stop) = instruction
        for _ in range(count):
            stacks[stop].append(stacks[start].pop())

    letters = ''
    for stack in stacks.values():
        if len(stack):
            letters += stack.pop()
    return letters


def part2(stack, instructions):

    stacks = create_stacks(stack)
    instructions = parse_instructions(instructions)

    for instruction in instructions:
        (count, start, stop) = instruction
        new_stack = []
        for _ in range(count):
            new_stack.insert(0, stacks[start].pop())
        stacks[stop].extend(new_stack)

    letters = ''
    for stack in stacks.values():
        if len(stack):
            letters += stack.pop()
    return letters


def main():

    test_data = """    [D] 
[N] [C]
[Z] [M] [P]
 1 2 3  

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

    stack, instruction = format_input(test_data)
    name = part1(stack, instruction)
    name2 = part2(stack, instruction)
    print(f'Test Part 1: {name=}')
    print(f'Test Part 2: {name2=}')

    data = get_data(day=5, year=2022)
    stack, instruction = format_input(data)
    name = part1(stack, instruction)
    name2 = part2(stack, instruction)
    print(f'Part 1: {name=}')
    print(f'Part 2: {name2=}')


if __name__ == '__main__':
    main()
