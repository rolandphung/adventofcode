#!/usr/bin/env python3

filename = 'input'
grid = None
with open(filename) as f:
    grid = f.read().strip().split('\n')

index = 0
move = 3
trees = 0
for line in grid[1:]:
    index = (index + move) % len(line)
    if line[index] == '#':
        trees += 1

print(trees)
