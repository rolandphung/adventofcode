#!/usr/bin/env python
# Day 2 Part 2
direction = { 'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0) }
keypad = { (0, 2): 1,
           (-1, 1): 2, (0, 1): 3, (1, 1): 4,
           (-2, 0): 5, (-1, 0): 6, (0, 0): 7, (1, 0): 8, (2, 0): 9,
           (-1, -1): 'A', (0, -1): 'B', (1, -1): 'C',
           (0, -2): 'D' }

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
