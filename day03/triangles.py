#!/usr/bin/env/ python

from __future__ import print_function

def is_triangle(a, b, c):
    return a+b>c and b+c>a and a+c>b

def count_triangles(triangles):
    triangles_count = 0
    for triangle in triangles.split('\n'):
        sides = map(int, triangle.split())
        if is_triangle(*sides):
            triangles_count += 1
    return triangles_count
#return sum(is_triangle(*sides) for sides in map(int, triangle.split()) for triangle in triangles.split('\n'))

with open('input') as f:
    triangles = f.read()

print("There are", count_triangles(triangles), "in the input file.")
