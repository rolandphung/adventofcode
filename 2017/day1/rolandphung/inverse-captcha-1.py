#!/usr/bin/env python
# Part 1
digits = [int(i) for i in open("input").read().strip()]
values = [digits[i] 
          for i in range(-1, len(digits) - 1)
          if digits[i] == digits[i + 1]]
print sum(values)
