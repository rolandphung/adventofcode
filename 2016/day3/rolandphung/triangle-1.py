#!/usr/bin/env python
inputs = map(lambda line: sorted(map(int, line.split())),
             open("input").read().strip().split('\n'))
triangles = map(lambda sides: int(sum(sides) - sides[-1] > sides[-1]), inputs)
# For some reason, this solution is off by 1
print sum(triangles)
