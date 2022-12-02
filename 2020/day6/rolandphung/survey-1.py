#!/usr/bin/env python3
filename = "input"
groups = None
with open(filename) as f:
    groups = f.read().strip().split("\n\n")

surveys = [set([q for q in entry if q != '\n'])
           for entry in groups]

print(sum([len(entry) for entry in surveys]))
