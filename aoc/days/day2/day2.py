# AOC 2022 Day 2
from aocd import get_data

OPPONENT_ACTIONS = {
    'A': 1, # rock
    'B': 2, # paper 
    'C': 3, # scissors
}
MY_ACTIONS = {
    'X': 1, # rock # lose
    'Y': 2, # paper # draw
    'Z': 3, # scissors # win
}


def get_next_reward(opponent, me):
    opponent_value = OPPONENT_ACTIONS[opponent]
    my_value = MY_ACTIONS[me]

    index = (my_value - opponent_value) % 3

    if index == 0:
        outcome = 3

    elif index == 1:
        outcome = 6 
    
    else:
        outcome = 0
    
    return outcome + my_value

def get_next_reward_2(opponent, me):
    opponent_value = OPPONENT_ACTIONS[opponent]
    my_value = MY_ACTIONS[me]

    if my_value == 1: # lose
        outcome = 0
        action = (opponent_value - 1 - 1) % 3 + 1

    elif my_value == 2:
        outcome = 3
        action = opponent_value

    else:
        outcome = 6 
        action = opponent_value % 3 + 1
    
    return outcome + action



def tournament(actions):
    total = 0
    for round in actions:
        total += get_next_reward(*round)

    return total

def tournament2(actions):
    total = 0
    for round in actions:
        total += get_next_reward_2(*round)

    return total

def format_input(input_str):
    return  [l.split(' ') for l in input_str.split('\n')]

def main():

    # test = 'A Y\nB X\nC Z\nA X\nA Z\nB Y\nB Z\nC X\nC Y'
    test = 'A Y\nB X\nC Z'
    test_inputs = format_input(test)
    reward1 = tournament(test_inputs)
    reward = tournament2(test_inputs)
    assert reward1 == 15
    assert reward == 12

    data = get_data(day=2, year=2022)
    inputs = format_input(data)
    reward = tournament(inputs)
    print(f'Total Reward: {reward}')
    reward2 = tournament2(inputs)
    print(f'Total Reward: {reward2}')



if __name__ == '__main__':
    main()