#!/usr/bin/env/ python

def is_a_triangle(triangles):
    triangles_count = 0
    for triangle in triangles.split('\n'):
        sides =  triangle.split()
        a = int(sides[0])
        b = int(sides[1])
        c = int(sides[2])
        if a+b>c and b+c>a and a+c>b:
            triangles_count += 1
    return triangles_count


with open('input') as f:
    triangles = f.read()

print "There are", is_a_triangle(triangles), "in the input file."
