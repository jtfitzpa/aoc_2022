# AOC 2022 Day 7
from aocd import get_data
import numpy as np


def format_input(input_str):
    return input_str.split('\n')


def parse_file_tree(input):
    current_stack = []
    file_tree = {}
    current_tree = file_tree

    for line in input:
        cmd = line.split(' ')

        if cmd[0] == '$':
            if cmd[1] == 'ls':
                pass
            elif cmd[1] == 'cd':
                dir_name = cmd[2]
                if dir_name == '/':
                    current_stack = []
                    current_tree = file_tree
                elif dir_name == '..':
                    current_stack.pop()

                    new_tree = file_tree
                    for item in current_stack:
                        new_tree = new_tree[item]
                    current_tree = new_tree
                else:
                    current_stack.append(dir_name)
                    current_tree = current_tree.get(dir_name, {})

        elif cmd[0] == 'dir':
            dir_name = cmd[1]
            current_tree[dir_name] = current_tree.get(dir_name, {})

        else:  # file size
            dir_name = cmd[1]
            current_tree[dir_name] = int(cmd[0])
    return file_tree


def compute_size_smaller(d, thresh=100000):

    thresh_list = []
    thresh_list = []
    total_list = []
    total = 0
    for k, v in d.items():
        if isinstance(v, dict):
            folder_size, _total_list, _thresh_list = compute_size_smaller(
                v, thresh=thresh
            )
            thresh_list += _thresh_list
            total_list += _total_list
            total += folder_size
            if folder_size <= thresh:
                thresh_list.append(k)
                total_list.append(folder_size)
        else:
            total += v

    return total, total_list, thresh_list


def compute_size_greater(d, thresh=100000):

    thresh_list = []
    thresh_list = []
    total_list = []
    big_thresh_list = []
    big_total_list = []
    total = 0
    for k, v in d.items():
        if isinstance(v, dict):
            (
                folder_size,
                _total_list,
                _thresh_list,
                _big_total_list,
                _big_thresh_list,
            ) = compute_size_greater(v, thresh=thresh)
            thresh_list += _thresh_list
            total_list += _total_list
            big_thresh_list += _big_thresh_list
            big_total_list += _big_total_list
            total += folder_size
            if folder_size < thresh:
                thresh_list.append(k)
                total_list.append(folder_size)
            else:
                big_thresh_list.append(k)
                big_total_list.append(folder_size)
        else:
            total += v

    return total, total_list, thresh_list, big_total_list, big_thresh_list


def part1(input):
    file_tree = parse_file_tree(input)
    return compute_size_smaller(file_tree)


def part2(input, thresh=30000000):
    file_tree = parse_file_tree(input)
    return compute_size_greater(file_tree, thresh=thresh)


def main():
    test_data = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

    total_space = 70000000
    space_needed = 30000000

    data_stream = format_input(test_data)
    size, folder_size, folders = part1(data_stream)
    print(f'Part 1: {size=} {sum(folder_size)=} {folders=}')
    thresh = space_needed - (total_space - size)
    size, _, _, big_folder_size, big_folders = part2(data_stream, thresh=thresh)
    print(f'Part 2: {size=} {big_folder_size=} {big_folders=}')

    data = get_data(day=7, year=2022)
    data_stream = format_input(data)
    size, folder_size, folders = part1(data_stream)
    print(f'Part 1: {size=} {sum(folder_size)=} {folders=}')
    thresh = space_needed - (total_space - size)
    size, _, _, big_folder_size, big_folders = part2(data_stream, thresh=thresh)

    idx = np.argmin(big_folder_size)
    print(f'Part 2: {size=} {big_folder_size[idx]=} {big_folders[idx]=}')


if __name__ == '__main__':
    main()
