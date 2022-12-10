# AOC 2022 Day 10
from aocd import get_data


def format_input(input_str):
    commands = []
    for line in input_str.split('\n'):
        items = line.split(' ')
        if len(items) == 1:
            commands.append((items[0], 0))
        else:
            commands.append((items[0], int(items[1])))

    return commands


def part1(commands):
    x_reg = 1
    cycles = 0
    signal_strength = [x_reg]
    for command, value in commands:
        if command == 'addx':
            signal_strength.append((cycles + 1) * x_reg)
            signal_strength.append((cycles + 2) * x_reg)
            cycles += 2
            x_reg += value
        elif command == 'noop':
            signal_strength.append((cycles + 1) * x_reg)
            cycles += 1

    total = 0
    for inds in range(20, 221, 40):
        total += signal_strength[inds]
    return total


def check_in_range(cycles, x_reg):
    if x_reg - 1 <= cycles <= x_reg + 1:
        return '#'
    else:
        return '.'


def part2(commands):
    rendered_pixels = []
    x_reg = 1
    cycles = 0
    for command, value in commands:
        if command == 'addx':
            symbol = check_in_range(cycles % 40, x_reg)
            rendered_pixels.append(symbol)
            symbol = check_in_range((cycles + 1) % 40, x_reg)
            rendered_pixels.append(symbol)
            cycles += 2
            x_reg += value
        elif command == 'noop':
            symbol = check_in_range(cycles % 40, x_reg)
            rendered_pixels.append(symbol)
            cycles += 1

    # print(np.array(rendered_pixels).reshape(6, 40))
    disp = ''
    for inds in range(0, 221, 40):
        disp += ''.join(rendered_pixels[inds : inds + 40]) + '\n'

    print(disp)


def main():
    test_data = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

    commands = format_input(test_data)
    total = part1(commands)
    print(f'Part 1: {total=}')
    part2(commands)

    data = get_data(day=10, year=2022)
    commands = format_input(data)
    total = part1(commands)
    print(f'Part 1: {total=}')
    part2(commands)


if __name__ == '__main__':
    main()
