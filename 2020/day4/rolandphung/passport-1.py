#!/usr/bin/env python3

filename = 'input'
passports = []
with open(filename) as f:
    data = f.read().strip().split('\n\n')
    for entry in data:
        passport = {}
        for field in entry.strip().split():
            if field:
                key, value = field.split(':')
                passport[key] = value
        passports.append(passport)

fields = frozenset(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
count = 0
for passport in passports:
    keys = frozenset(passport.keys())
    if keys >= fields:
        count += 1

print(count)
