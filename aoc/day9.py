# AOC 2022 Day 9
from aocd import get_data


def format_input(input_str):
    commands = []
    for line in input_str.split('\n'):
        items = line.split(' ')
        commands.append((items[0], int(items[1])))

    return commands


class VisitTracker:
    def __init__(self, num_ropes):
        self.num_ropes = num_ropes
        self.locations_visited = []
        self.head_pos = (0, 0)
        self.tail_pos = [(0, 0) for _ in range(num_ropes)]

    @staticmethod
    def _coordinates_after_update(start, direction):
        if direction == 'U':
            return (start[0], start[1] + 1)
        if direction == 'D':
            return (start[0], start[1] - 1)
        if direction == 'R':
            return (start[0] + 1, start[1])
        if direction == 'L':
            return (start[0] - 1, start[1])

    def update_head(self, direction):
        self.head_pos = self._coordinates_after_update(self.head_pos, direction)

    def update_tail(self, tail_num=0):
        if not self._are_touching(tail_num):
            diff = self._head_to_tail(tail_num)
            diff = [x / max(abs(x), 1) for x in diff]
            self.tail_pos[tail_num] = (
                self.tail_pos[tail_num][0] + diff[0],
                self.tail_pos[tail_num][1] + diff[1],
            )

    def _head_to_tail(self, tail_num):
        if tail_num == 0:
            return (
                self.head_pos[0] - self.tail_pos[0][0],
                self.head_pos[1] - self.tail_pos[0][1],
            )
        else:
            return (
                self.tail_pos[tail_num - 1][0] - self.tail_pos[tail_num][0],
                self.tail_pos[tail_num - 1][1] - self.tail_pos[tail_num][1],
            )

    def _are_touching(self, tail_num):
        diff = self._head_to_tail(tail_num)
        return abs(diff[0]) <= 1 and abs(diff[1]) <= 1

    def update(self, direction, distance):
        for _ in range(distance):

            self.update_head(direction)
            for i in range(self.num_ropes):
                self.update_tail(i)

            # Track position of last tail
            self.track_visit(self.tail_pos[-1])

    def track_visit(self, visit):
        self.locations_visited.append(visit)

    def unique_locations(self):
        return set(self.locations_visited)


def part1(commands):

    visit_tracker = VisitTracker(num_ropes=1)

    for direction, distance in commands:
        visit_tracker.update(direction, distance)

    total_visited = len(visit_tracker.unique_locations())
    return total_visited


def part2(commands):

    visit_tracker = VisitTracker(num_ropes=9)

    for direction, distance in commands:
        visit_tracker.update(direction, distance)

    total_visited = len(visit_tracker.unique_locations())
    return total_visited


def main():
    test_data = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

    commands = format_input(test_data)
    total = part1(commands)
    print(f'Part 1: {total=}')
    total = part2(commands)
    print(f'Part 2: {total=}')

    data = get_data(day=9, year=2022)
    commands = format_input(data)
    total = part1(commands)
    print(f'Part 1: {total=}')
    total = part2(commands)
    print(f'Part 2: {total=}')


if __name__ == '__main__':
    main()
