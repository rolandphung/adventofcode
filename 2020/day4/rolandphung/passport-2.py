#!/usr/bin/env python3
import re

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

year_re = re.compile(r'^\d{4}$')
height_re = re.compile(r'^\d+(?:in|cm)$')
hair_re = re.compile(r'^#[0-9a-f]{6}$')
pid_re = re.compile(r'^\d{9}$')

def validate_year(value, low, high):
    if not year_re.match(value):
        return False
    year = int(value)
    return year >= low and year <= high

def validate_height(value):
    if not height_re.match(value):
        return False
    height = int(value[:-2])
    unit = value[-2:]
    if unit == 'in':
        return height >= 59 and height <= 76
    if unit == 'cm':
        return height >= 150 and height <= 193

fields = frozenset(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
eye_colors = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')

count = 0
for passport in passports:
    keys = frozenset(passport.keys())
    if not (keys >= fields):
        continue

    if not validate_year(passport['byr'], 1920, 2002):
        continue

    if not validate_year(passport['iyr'], 2010, 2020):
        continue

    if not validate_year(passport['eyr'], 2020, 2030):
        continue

    if not validate_height(passport['hgt']):
        continue

    if not hair_re.match(passport['hcl']):
        continue

    if passport['ecl'] not in eye_colors:
        continue

    if not pid_re.match(passport['pid']):
        continue

    count += 1

print(count)
