#!/usr/bin/env python3
from functools import reduce

filename = "input"
groups = None
with open(filename) as f:
    groups = [[set(person) for person in group.split('\n')]
              for group in f.read().strip().split("\n\n")]

surveys = [reduce(lambda a, b: a & b, group)
           for group in groups]

print(sum([len(entry) for entry in surveys]))
