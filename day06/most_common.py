#!/usr/bin/env python

from __future__ import print_function
from collections import Counter
from operator import itemgetter

with open('test_input') as f:
    test_jammed = f.read()
    
with open('input') as f:
    jammed_inpt = f.read()

jammed = jammed_inpt.split('\n')
lines_count = len(jammed)
len_line = len(jammed[0])
    
def get_chars(jammed, idx):
    letter = ''
    for i in range(lines_count):
        letter += jammed[i][idx]
    return ''.join(letter)

def decrypt():
    decrypted = ''
    for i in range(len_line):
        most_common = Counter(get_chars(jammed, i)).items()
        most_common = sorted(most_common, key=itemgetter(1)) # for first part need to add reverse=True
        decrypted += str(most_common[0][0])
    return decrypted
    
#assert decrypt() == 'advent' # for first task there's "easter"
print("The original message is:", decrypt())
