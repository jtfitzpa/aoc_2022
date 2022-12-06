# AOC 2022 Day 1
import argparse
from aocd import get_data


def read_file(input):
    cleaned_input = []
    input = input.split('\n')
    for line in input:
        if line:
            line = int(line)
        else:
            line = None
        cleaned_input.append(line)

    return cleaned_input


def group_items(input):
    totals = [0]
    for item in input:
        if item:
            totals[-1] += item
        else:
            totals.append(0)

    return totals


def main():

    test_data = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""
    input = read_file(test_data)
    result = group_items(input)
    max_food = sorted(result)

    print(f'Test Answer - Part 1: {max(max_food)}')
    print(f'Test Answer - Part 2: {sum(max_food[-3:])}')

    data = get_data(day=1, year=2022)
    input = read_file(data)
    result = group_items(input)
    max_food = sorted(result)

    print(f'Final Answer - Part 1: {max(max_food)}')
    print(f'Final Answer - Part 2: {sum(max_food[-3:])}')


if __name__ == '__main__':
    main()
