#!/usr/bin/env python

init_key = '5'
init_coordinates = (0, 0)

instructions_mapping = {
    'U': (1, 0),
    'D': (-1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

key_mapping = {
    '1': (1, -1), '2': (1, 0), '3': (1,1),
    '4': (0, -1), '5': (0, 0), '6': (0,1),
    '7': (-1, -1), '8': (-1, 0), '9': (-1, 1)
}

forbidden = {'U': '123', 'D': '789', 'L': '147', 'R': '369'}

def check_overflow(move, curr_key):
    return curr_key in forbidden[move]      

def solve(moves):
    curr_key = init_key
    curr_coordinates = init_coordinates
    keys = ""
    
    for key in moves.split('\n'):
        for move in key:
            next_move = instructions_mapping[move] #U = 1, 0
            if not check_overflow(move, curr_key):
                curr_coordinates = (curr_coordinates[0] + next_move[0], curr_coordinates[1] + next_move[1])
                curr_key = key_mapping.keys()[key_mapping.values().index(curr_coordinates)]
        keys += curr_key
    return keys
        
with open('test_input') as f:
   test_moves = f.read()
assert solve(test_moves) == "1985"


with open('input') as f:
    moves = f.read()
print "The bathroom code is:", solve(moves)

