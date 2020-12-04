#!/usr/bin/env python3
"""
Day 4: Passport Processing

https://adventofcode.com/2020/day/4
"""

import string
from typing import Set, Dict

def load_input(filename: str) -> [[(str, str)]]:
    with open(filename) as f:
        text = f.read()
        return [
            {
                x.split(':')[0]: x.split(':')[1]
                for x in passport.split()
            }
            for passport in text.split("\n\n")
        ]

def check_keys(passport: Dict[str, str]) -> bool:
    required_keys = set(("byr","iyr","eyr","hgt","hcl","ecl","pid"))
    return passport.keys() >= required_keys

def validate(passport: Dict[str, str]) -> bool:
    validators = {
        "byr": lambda x: len(x)==4 and (1920<=int(x)<=2002),
        "iyr": lambda x: len(x)==4 and (2010<=int(x)<=2020),
        "eyr": lambda x: len(x)==4 and (2020<=int(x)<=2030),
        "hgt": lambda x: (x.endswith('cm') and (150<=int(x[:-2])<=193)) or \
                        (x.endswith('in') and ( 59<=int(x[:-2])<=76 )),
        "hcl": lambda x: len(x)==7 and x.startswith('#') and \
                        all(c in string.hexdigits for c in x[1:]),
        "ecl": lambda x: x in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),
        "pid": lambda x: len(x)==9 and all(c in string.digits for c in x),
        "cid": lambda x: True
    }
    return check_keys(passport) and \
           all(validators.get(k)(v) for (k, v) in passport.items())

def count_valid(passports: [[(str, str)]], validator) -> int:
    return sum(1 for passport in passports if validator(passport))

if __name__ == "__main__":
    passports = load_input("inputs/day4")
    print("Part 1:", count_valid(passports, check_keys))
    print("Part 2:", count_valid(passports, validate))
