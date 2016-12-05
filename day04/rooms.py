#!/usr/bin/env python

from __future__ import print_function
from collections import Counter
from string import ascii_lowercase

def parse(line):
    last_dash_index = line.rindex('-')
    bracket_index = line.index('[')

    return {
        'room_name': line[:last_dash_index],
        'sector_id': line[last_dash_index+1:bracket_index],
        'room_checksum': line[bracket_index+1:-1]
    }

def is_valid_checksum(room_name, room_checksum):
    most_common = Counter(room_name.replace('-', '')).items()
    most_common = sorted(most_common, key=lambda k: (-k[1], k[0]))
    checksum = ''.join(i[0] for i in most_common[:5])
    if checksum == room_checksum:
        return True

def decrypt_name(room_name, sector_id):
    return ''.join(ascii_lowercase[(ascii_lowercase.index(i) + int(sector_id)) % len(ascii_lowercase)] if i != '-' else ' 'for i in room_name)
    
def solve_first(rooms):
    return sum(int(room['sector_id']) for room in map(parse, rooms.splitlines()) if is_valid_checksum(room['room_name'], room['room_checksum']))


def solve_second(rooms):
    for room in map(parse, rooms.splitlines()):
        name = decrypt_name(room['room_name'], room['sector_id'])
        if 'north' in name:
            print(name, room)
        
    

with open('test_input') as f:
    test = f.read()    
assert solve_first(test) == 1514

with open('input') as f:
    rooms = f.read()
print("Sum of sector ID's of the real rooms is:", solve_first(rooms))

print("Room ID is:", solve_second(rooms))

assert decrypt_name('qzmt-zixmtkozy-ivhz', 343) == 'very encrypted name'
