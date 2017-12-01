#!/usr/bin/env python
digits = [int(i) for i in open("input").read().strip()]
values = [digits[i] if digits[i] == digits[i + 1] else 0
          for i in range(-1, len(digits) - 1)]
print sum(values)
