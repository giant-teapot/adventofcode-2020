#!/usr/bin/env python3
"""
Day 1: Report Repair

https://adventofcode.com/2020/day/1
"""

import math

from itertools import product
from typing import Optional

def load_input(filename: str) -> [int]:
    with open(filename) as f:
        return [int(line.strip()) for line in f]

def find_entries_adding_up_to_2020(entries: [int], nb_entries: int) -> Optional[int]:
    for xs in product(entries, repeat=nb_entries):
        if sum(xs) == 2020:
            return math.prod(xs)

    return None

if __name__ == "__main__":
    values = load_input("inputs/day1")
    print("Part 1:", find_entries_adding_up_to_2020(values, nb_entries=2))
    print("Part 2:", find_entries_adding_up_to_2020(values, nb_entries=3))
