#!/usr/bin/env python

init_key = '5'
init_coordinates = (0, -2)

instructions_mapping = {
    'U': (1, 0),
    'D': (-1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

key_mapping = {
    '1': (2, 0),
    '2': (1, -1), '3': (1, 0), '4': (1, 1),
    '5': (0, -2), '6': (0, -1), '7': (0, 0), '8': (0, 1), '9': (0, 2),
    'A': (-1, -1),'B': (-1, 0), 'C': (-1, 1),
    'D': (-2, 0)
}

forbidden = {'U': '12459', 'D': '59ACD', 'L': '125AD', 'R': '149CD'}

def is_valid_move(move, curr_key):
    return curr_key not in forbidden[move]

def solve(moves):
    curr_key = init_key
    curr_coordinates = init_coordinates
    keys = ""
    
    for key in moves.split('\n'):
        for move in key:
            next_move = instructions_mapping[move]
            if is_valid_move(move, curr_key):
                curr_coordinates = (curr_coordinates[0] + next_move[0], curr_coordinates[1] + next_move[1])
                curr_key = key_mapping.keys()[key_mapping.values().index(curr_coordinates)]
        keys += curr_key
    return keys
        
with open('test_input') as f:
   test_moves = f.read()
assert solve(test_moves) == "5DB3"


with open('input') as f:
    moves = f.read()
print "The bathroom code is:", solve(moves)
