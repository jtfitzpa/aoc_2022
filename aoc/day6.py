# AOC 2022 Day 6
from aocd import get_data

def format_input(input_str):
    return input_str.strip('\n')

def part1(input, sync_len=4):
    for i in range(sync_len, len(input)):
        if len(set(input[i-sync_len:i])) == sync_len:
            return i
    return len(input)

        
def part2(input):

    pass



def main():
    test_data1 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
    data_stream = format_input(test_data1)
    marker = part1(data_stream, sync_len=4)
    assert marker == 7, marker
    marker = part1(data_stream, sync_len=14)
    assert marker == 19, marker

    test_data2 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
    data_stream = format_input(test_data2)
    marker = part1(data_stream, sync_len=4)
    assert marker == 5, marker
    marker = part1(data_stream, sync_len=14)
    assert marker == 23, marker

    test_data3 = "nppdvjthqldpwncqszvftbrmjlhg"
    data_stream = format_input(test_data3)
    marker = part1(data_stream, sync_len=4)
    assert marker == 6, marker
    marker = part1(data_stream, sync_len=14)
    assert marker == 23, marker

    test_data4 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
    data_stream = format_input(test_data4)
    marker = part1(data_stream, sync_len=4)
    assert marker == 10, marker
    marker = part1(data_stream, sync_len=14)
    assert marker == 29, marker
    
    test_data5 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
    data_stream = format_input(test_data5)
    marker = part1(data_stream, sync_len=4)
    assert marker == 11, marker
    marker = part1(data_stream, sync_len=14)
    assert marker == 26, marker
    
    data = get_data(day=6, year=2022)
    data_stream = format_input(data)
    marker = part1(data_stream, sync_len=4)
    print(f'Part 1: {marker=}')
    marker = part1(data_stream, sync_len=14)
    print(f'Part 2: {marker=}')


if __name__ == '__main__':
    main()