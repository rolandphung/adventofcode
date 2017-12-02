#!/usr/bin/env python
# Day 1 Part 1

# 0 is North, 1 is East, 2 is South, 3 is West
direction = { 0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0) }
turns = { 'R': 1, 'L': -1 }

inputs = open("input").read().strip().split(", ")
instructions = map(lambda x: (turns[x[0]], int(x[1:])), inputs)

location = (0, 0)
visited = {location: True}
heading = 0
for turn, length in instructions:
    heading = (heading + turn) % 4
    for i in range(length):
        location = (location[0] + direction[heading][0],
                    location[1] + direction[heading][1])
        if location in visited:
            print abs(location[0]) + abs(location[1])
            exit
        visited[location] = True
