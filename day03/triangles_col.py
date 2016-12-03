#!/usr/bin/env/ python

def get_triangle(row, n):
    return (row[i:i+n] for i in xrange(0, len(row), n))

def is_a_triangle(triangles):
    triangles_count = 0
    for triangle in get_triangle(triangles, 3):
        a = int(triangle[0])
        b = int(triangle[1])
        c = int(triangle[2])
        if a+b>c and b+c>a and a+c>b:
            triangles_count += 1
    return triangles_count

def solve(triangles):
    triangles_count = 0
    col_0 = []
    col_1 = []
    col_2 = []
    
    for triangle in triangles.split('\n'):
        vals =  triangle.split()
        col_0.append(vals[0])
        col_1.append(vals[1])
        col_2.append(vals[2])
        
    for column in (col_0, col_1, col_2):
        triangles_count += is_a_triangle(column)
    return triangles_count

with open('test_input') as f:
    triangles = f.read()
assert solve(triangles) == 9

with open('input') as f:
    triangles = f.read()
print "COL: There are", solve(triangles), "triangles in the input file."
