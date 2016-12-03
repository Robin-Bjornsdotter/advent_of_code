#!/usr/bin/env/ python

def is_triangle(a, b, c):
    if a+b>c and b+c>a and a+c>b:
        return True
    return False

def count_triangles(triangles):
    triangles_count = 0
    for triangle in triangles.split('\n'):
        sides =  triangle.split()
        a = int(sides[0])
        b = int(sides[1])
        c = int(sides[2])
        if is_triangle(a, b, c):
            triangles_count += 1
    return triangles_count


with open('input') as f:
    triangles = f.read()

print "There are", count_triangles(triangles), "in the input file."
