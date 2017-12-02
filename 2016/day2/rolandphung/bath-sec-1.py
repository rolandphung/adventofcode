#!/usr/bin/env python
# Day 2 Part 2
direction = { 'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0) }
keypad = { (-1, 1): 1, (0, 1): 2, (1, 1): 3,
           (-1, 0): 4, (0, 0): 5, (1, 0): 6,
           (-1, -1): 7, (0, -1): 8, (1, -1): 9 }

inputs = open("input").read().strip().split()
instructions = [[direction[c] for c in i]
                for i in inputs]

key = []
for movement in instructions:
    location = (0, 0)
    for x, y in movement:
        point = (location[0] + x, location[1] + y)
        if point in keypad:
            location = point
    print keypad[location],
print
