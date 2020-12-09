#!/usr/bin/env python3
"""
Day 9: Encoding Error

https://adventofcode.com/2020/day/9
"""

from itertools import combinations

def load_input(filename: str) -> [int]:
    with open(filename) as f:
        return [int(line.strip()) for line in f]

def validate_next(preamble: [int], number: int) -> bool:
    return number in map(sum, combinations(preamble, 2))

def find_invalid_number(numbers: [int], preamble_size: int) -> int:
    for i in range(preamble_size, len(numbers)):
        preamble = numbers[i-preamble_size:i]
        if not validate_next(preamble, numbers[i]):
            return numbers[i]

    return 0

def find_weakness(numbers: [int], preamble_size: int) -> int:
    invalid_nb = find_invalid_number(numbers, preamble_size)

    for w_size in range(2, len(numbers)):
        for pos in range(0, len(numbers)-w_size+1):
            window = numbers[pos:pos+w_size]
            if sum(window) == invalid_nb:
                return min(window)+max(window)

    return 0

if __name__ == "__main__":
    numbers = load_input("inputs/day9")
    print("Part 1:", find_invalid_number(numbers, 25))
    print("Part 2:", find_weakness(numbers, 25))
