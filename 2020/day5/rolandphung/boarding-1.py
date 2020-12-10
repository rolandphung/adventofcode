#!/usr/bin/env python3


filename = 'input'
passes = []
with open(filename) as f:
    passes = f.read().strip().split('\n')

def convert(entry):
    number = 0
    for bit in entry:
        number *= 2
        if bit == 'B' or bit == 'R':
            number += 1
    return number
    
numbers = sorted([convert(entry) for entry in passes])
print(max(numbers))
