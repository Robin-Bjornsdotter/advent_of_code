#!/usr/bin/env python
from __future__ import print_function
import hashlib

def first():
    input = "reyedfim"
    password = []
    index = 0
    while len(password) < 8:
        hash = hashlib.md5(input+str(index)).hexdigest()
           
        if hash.startswith("00000"):
            password.append(hash[5])
        input += 1
    return ''.join(password)

    
def second():
    input = "reyedfim"
    password = ['.', '.', '.', '.', '.', '.', '.', '.']
    index = 0
    
    while '.' in password:
        hash = hashlib.md5(input+str(index)).hexdigest()
                
        if hash.startswith("00000"):
            if hash[5].isdigit():
                password_index = int(hash[5])
                if password_index < 8 and password[password_index] == ".":
                    password[password_index] = hash[6]
        index += 1
    return ''.join(password)

print(First part password:", first())
print("Second part password:", second())
