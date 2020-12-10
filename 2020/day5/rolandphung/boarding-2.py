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
seat = None
start = 0
end = len(numbers) - 1

while seat is None:
    if end - start == 2:
        seat = numbers[start] + 1
    mid = int(start + (end - start) / 2)
    if numbers[mid] - numbers[start] != mid - start:
        end = mid
    elif numbers[end] - numbers[mid + 1] != end - mid - 1:
        start = mid + 1
    else:
        seat = numbers[mid] + 1
print(seat)
