#!/usr/bin/env python
inputs = open("input").read().strip().split('\n')
numbers = map(lambda number: sorted(map(int, number.split())), inputs)
checksum = map(lambda n: n[-1] - n[0], numbers)
print sum(checksum)
