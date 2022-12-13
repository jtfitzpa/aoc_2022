# AOC 2022 Day 12
from aocd import get_data

import numpy as np
from collections import defaultdict
from tqdm.auto import tqdm
from typing import List, Dict, Tuple
from typing_extensions import Self
import random
from dataclasses import dataclass


def format_input(input_str: str, part: int = 1) -> np.ndarray:
    start = (0, 0)
    end = (0, 0)
    lines = input_str.split('\n')
    surface_map = []
    starts = []
    for i, line in enumerate(lines):
        surface_line = []
        for j, char in enumerate(line):
            if char == 'S':
                value = ord('a')
                start = (i, j)
                if part == 2:
                    starts.append(start)
            elif char == 'E':
                end = (i, j)
                value = ord('z')
            elif part == 2 and char == 'a':
                starts.append((i, j))
                value = ord(char)
            else:
                value = ord(char)
            surface_line.append(value)
        surface_map.append(surface_line)

    surface = np.array(surface_map)

    if part == 2:
        return surface, starts, end
    return surface, start, end


@dataclass
class Node:
    location: Tuple[int, int] = (0, 0)
    value: int = 0
    parent: Self = None
    steps: int = 0


class Graph:
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def add_edge(self, u, v):
        self.graph[u].append(v)


def create_graph(surface):

    graph = Graph()
    visited = {}
    h, w = surface.shape
    for i in range(h):
        for j in range(w):
            pos = (i, j)
            visited[pos] = False
            for offset in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                next_pos = (
                    min(max(pos[0] + offset[0], 0), h - 1),
                    min(max(pos[1] + offset[1], 0), w - 1),
                )
                if next_pos[0] == pos[0] and next_pos[1] == pos[1]:
                    continue
                if abs(next_pos[0] - pos[0]) + abs(next_pos[1] - pos[1]) > 1:
                    continue
                if surface[next_pos] - surface[pos] > 1:
                    continue
                graph.add_edge(pos, next_pos)

    return graph, visited


def part1(surface, start, end) -> int:
    graph, visited = create_graph(surface)
    pos = start
    root = Node(
        location=pos,
        value=surface[pos],
    )
    locations = [root]
    while locations:
        node = locations.pop(0)
        pos = node.location

        if pos[0] == end[0] and pos[1] == end[1]:
            n_steps = 0
            while node.parent is not None:
                n_steps += 1
                node = node.parent

            return n_steps

        for location in graph.graph[pos]:
            if not visited[location]:
                child = Node(location=location, value=surface[location], parent=node)
                locations.append(child)
                visited[location] = True


def part2(surface, starts, end):
    all_steps = []
    for start in tqdm(starts):
        total_steps = part1(surface, start, end)
        if total_steps:
            all_steps.append(total_steps)

    return min(all_steps)


def main():
    test_data = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

    surface, start, end = format_input(test_data, part=1)
    total_steps = part1(surface, start, end)
    print(f'Part 1: {total_steps=}')
    surface, starts, end = format_input(test_data, part=2)
    total_steps = part2(surface, starts, end)
    print(f'Part 2: {total_steps=}')

    data = get_data(day=12, year=2022)
    surface, start, end = format_input(data, part=1)
    total_steps = part1(surface, start, end)
    print(f'Part 1: {total_steps=}')
    surface, starts, end = format_input(data, part=2)
    total_steps = part2(surface, starts, end)
    print(f'Part 2: {total_steps=}')


if __name__ == '__main__':
    main()
