#!/usr/bin/env python3


filename = "input"
data = None
with open(filename) as f:
    data = f.read()

numbers = set([int(i) for i in data.split()])
mirror = [(2020 - i) for i in numbers]

for i in mirror:
    if i in numbers:
        print((2020 - i) * i)
        break


