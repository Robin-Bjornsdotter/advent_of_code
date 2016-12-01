#!/usr/bin/env python

init_dir = 'N'
init_pos = (0, 0)

dir_mapping = {
    'N': (0, 1),
    'E': (1, 0),
    'W': (-1, 0),
    'S': (0, -1)
}

turns_mapping = {
    'N': {'L': 'W', 'R': 'E'},
    'E': {'L': 'N', 'R': 'S'},
    'W': {'L': 'S', 'R': 'N'},
    'S': {'L': 'E', 'R': 'W'}
}

def make_turn(direction, turn):
    return turns_mapping[direction][turn]

def taxicab_distance(init_pos, end_pos):
    return abs(end_pos[0] - init_pos[0]) + abs(end_pos[1] - init_pos[1])

def solve(moves):
    curr_dir = init_dir
    curr_pos = init_pos
    
    visited = set()
    visited.add(curr_pos)
    
    for move in moves.split(', '):
        turn, steps = move[0], int(move[1:])
        curr_dir = make_turn(curr_dir, turn)
        next_step = dir_mapping[curr_dir]
        
        for step in range(steps):
            curr_pos = (curr_pos[0] + next_step[0], curr_pos[1] + next_step[1])
            print curr_pos
            
            if curr_pos in visited:
               return taxicab_distance(init_pos, curr_pos)
            visited.add(curr_pos)

assert solve("R2, R1, R1, R1") == 1

with open('input') as f:
    moves = f.read()

print "Easter bunny HQ is", solve(moves), "blocks away"
