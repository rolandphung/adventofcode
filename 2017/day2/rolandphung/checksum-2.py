#!/usr/bin/env python
inputs = open("input").read().strip().split('\n')
numbers = map(lambda number: sorted(map(int, number.split())), inputs)

checksum = 0
for row in numbers:
    for r in reversed(row):
        for n in row:
            if n > r / 2:
                break
            if r % n == 0:
                checksum += r / n

print checksum
