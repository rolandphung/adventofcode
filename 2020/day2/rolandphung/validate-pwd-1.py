#!/usr/bin/env python3
import re

filename = "input"
regex = re.compile("(\d+)-(\d+) ([a-z]): (\w+)")

data = None
with open(filename) as f:
    data = f.read().split("\n")

def validate(low, high, letter, pwd):
    count = 0
    for char in pwd:
        if letter == char:
            count += 1
    return low <= count and high >= count

count = 0
for line in data:
    if not line:
        continue
    m = regex.match(line)
    low, high, letter, pwd = m.groups()
    low = int(low)
    high = int(high)
    if validate(low, high, letter, pwd):
        count += 1

print(count)
