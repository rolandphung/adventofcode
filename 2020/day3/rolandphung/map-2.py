#!/usr/bin/env python3

filename = 'input'
grid = None
with open(filename) as f:
    grid = f.read().strip().split('\n')

moves = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
answer = 1
for x, y in moves:
    index = 0
    trees = 0
    for lineno, line in enumerate(grid[y:]):
        if lineno % y == 0:
            index = (index + x) % len(line)
            if line[index] == '#':
                trees += 1
    answer *= trees

print(answer)
