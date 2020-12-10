#!/usr/bin/env python3
"""
Day 10: Adapter Array

https://adventofcode.com/2020/day/10
"""

from collections import Counter

def load_input(filename: str) -> [int]:
    with open(filename) as f:
        return [int(line.strip()) for line in f]

def get_jotlage_diff_distribution(joltage: [int]) -> [(int, int)]:
    device_joltage = max(joltage)+3
    joltage = sorted(joltage + [0, device_joltage])

    joltages_to_diff = zip(joltage[:-1], joltage[1:])
    diffs = map(lambda pair: pair[1]-pair[0], joltages_to_diff)

    return Counter(diffs)

def adapter_combinations(joltage) -> int:
    device_joltage = max(joltage)+3
    joltage = sorted(joltage + [device_joltage])

    # The number of combination can be accumulated from "left to right" by
    # computing the number of combination for 1 adapter, then 2, and 3...
    #
    # The combination for any "joltage" is the sum of the number of combinations
    # of the 3 joltages directly below.

    combinations = [1] + [0]*device_joltage
    for j in joltage:
        combinations[j] = combinations[j-1] \
                        + combinations[j-2] \
                        + combinations[j-3]

    return combinations[device_joltage]


if __name__ == "__main__":
    joltage = load_input("inputs/day10")
    distributions = get_jotlage_diff_distribution(joltage)
    print("Part 1:", distributions[1]*distributions[3])
    print("Part 2:", adapter_combinations(joltage))
