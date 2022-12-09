# AOC 2022 Day 7
from aocd import get_data
import numpy as np


def format_input(input_str):
    return np.array([list(line) for line in input_str.split('\n')], dtype=np.int32)


def part1(tree_grid):

    visible_mask = np.ones_like(tree_grid)
    visible_mask[1:-1, 1:-1] = 0
    for i in range(1, tree_grid.shape[0] - 1):
        for j in range(1, tree_grid.shape[1] - 1):
            if np.all(tree_grid[i, j] > tree_grid[:i, j]):
                visible_mask[i, j] = 1
            if np.all(tree_grid[i, j] > tree_grid[i + 1 :, j]):
                visible_mask[i, j] = 1
            if np.all(tree_grid[i, j] > tree_grid[i, :j]):
                visible_mask[i, j] = 1
            if np.all(tree_grid[i, j] > tree_grid[i, j + 1 :]):
                visible_mask[i, j] = 1

    return np.sum(visible_mask)


def part2(tree_grid):
    view_dist = np.ones_like(tree_grid)
    for i in range(1, tree_grid.shape[0] - 1):
        for j in range(1, tree_grid.shape[1] - 1):

            view = 1
            comps = tree_grid[i, j] > tree_grid[:i, j]
            if not np.all(comps):
                view *= np.argmin(comps[::-1]) + 1
            else:
                view *= len(comps)

            comps = tree_grid[i, j] > tree_grid[i + 1 :, j]
            if not np.all(comps):
                view *= np.argmin(comps) + 1
            else:
                view *= len(comps)

            comps = tree_grid[i, j] > tree_grid[i, :j]
            if not np.all(comps):
                view *= np.argmin(comps[::-1]) + 1
            else:
                view *= len(comps)
            comps = tree_grid[i, j] > tree_grid[i, j + 1 :]
            if not np.all(comps):
                view *= np.argmin(comps) + 1
            else:
                view *= len(comps)

            view_dist[i, j] = view
    return np.max(view_dist)


def main():
    test_data = """30373
25512
65332
33549
35390"""

    tree_grid = format_input(test_data)
    visible_trees = part1(tree_grid)
    print(f'Part 1: {visible_trees=}')
    view_score = part2(tree_grid)
    print(f'Part 2: {view_score=}')

    data = get_data(day=8, year=2022)
    tree_grid = format_input(data)
    visible_trees = part1(tree_grid)
    print(f'Part 1: {visible_trees=}')
    view_score = part2(tree_grid)
    print(f'Part 2: {view_score=}')


if __name__ == '__main__':
    main()
