#!/usr/bin/env python3
from itertools import tee

filename = "input"
data = None
with open(filename) as f:
    data = f.read()

numbers = set([int(i) for i in data.split()])
pairs = {}
it = iter(numbers)
i = next(it)
while i is not None:
    it, nit = tee(it)
    for j in nit:
        if i + j < 2020:
            pairs[i + j] = (i, j)
    try:
        i = next(it)
    except StopIteration:
        i = None

for k, (a, b) in iter(pairs.items()):
    c = 2020 - k
    if c in numbers:
        print(a, b, c)
        print(a * b * c)
