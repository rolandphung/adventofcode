#!/usr/bin/env python
digits = [int(i) for i in open("input").read().strip()]
length = len(digits)
half = length / 2
values = [digits[i] if digits[i] == digits[(i + half) % length] else 0
          for i in range(len(digits))]
print sum(values)
