#!/usr/bin/env python
# Day 1 Part 1
turns = { 'R': 1, 'L': -1 }
inputs = open("input").read().strip().split(", ")
instructions = map(lambda x: (turns[x[0]], int(x[1:])), inputs)

distance = { i: 0 for i in range(4) }
direction = 0
for turn, length in instructions:
    direction = (direction + turn) % 4
    distance[direction] += length
total = abs(distance[0] - distance[2]) + abs(distance[1] - distance[3])
print total
