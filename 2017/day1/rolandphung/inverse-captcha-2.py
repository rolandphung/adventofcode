#!/usr/bin/env python
# Day 2 Part 2
digits = [int(i) for i in open("input").read().strip()]
length = len(digits)
half = length / 2
values = [digits[i] for i in range(len(digits))
          if digits[i] == digits[(i + half) % length]]
print sum(values)
