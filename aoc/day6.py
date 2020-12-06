#!/usr/bin/env python3
"""
Day 6: Custom Customs

https://adventofcode.com/2020/day/6
"""

from itertools import chain

def load_input(filename: str):
    with open(filename) as f:
        return list(map(str.split, f.read().split("\n\n")))

def answers_union(answers:[str]):
    return len(set(chain.from_iterable(answers)))

def answers_intersection(answers:[str]):
    return len(set.intersection(*map(set, answers)))


if __name__ == "__main__":
    group_answers = load_input("inputs/day6")
    print("Part 1:", sum(map(answers_union, group_answers)))
    print("Part 2:", sum(map(answers_intersection, group_answers)))
