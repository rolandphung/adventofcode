#!/usr/bin/env python3
import re

filename = "input"
regex = re.compile("(\d+)-(\d+) ([a-z]): (\w+)")

data = None
with open(filename) as f:
    data = f.read().split("\n")

def validate(first, second, letter, pwd):
    if len(pwd) < second:
        return False
    char1 = pwd[first]
    char2 = pwd[second]

    return (char1 == letter or char2 == letter) and char1 != char2

count = 0
for line in data:
    if not line:
        continue
    m = regex.match(line)
    first, second, letter, pwd = m.groups()
    first = int(first) - 1
    second = int(second) - 1
    if validate(first, second, letter, pwd):
        count += 1

print(count)
