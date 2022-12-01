# AOC 2022 Day 1
import argparse


def read_file(filename):
    with open(filename, 'r', encoding='UTF-8') as f:
        input = f.readlines()
    cleaned_input = []
    for line in input:
        no_return = line.rstrip('\n')
        if no_return:
            no_return = int(no_return)
        else:
            no_return = None
        cleaned_input.append(no_return)

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
    ap = argparse.ArgumentParser()
    ap.add_argument('file', type=str)
    args = ap.parse_args()


    input = read_file(args.file)
    result = group_items(input)
    max_food = sorted(result)

    print(f'Final Answer - Part 1: {max(max_food)}')
    print(f'Final Answer - Part 2: {sum(max_food[-3:])}')


if __name__ == '__main__':
    main()