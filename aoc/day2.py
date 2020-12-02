#!/usr/bin/env python3
"""
Day 2: Password Philosophy

https://adventofcode.com/2020/day/2
"""

from dataclasses import dataclass

@dataclass
class Password:
    policy: (int, int)
    letter: str
    word: str

    def is_valid(self):
        """ Part 1 password validator """
        return self.policy[0] <= self.word.count(self.letter) <= self.policy[1]

    def is_valid2(self):
        """ Part 2 password validator """
        pos1, pos2 = map(lambda x: x-1, self.policy)
        return (self.word[pos1] == self.letter) ^ (self.word[pos2] == self.letter)


def load_input(filename: str) -> [Password]:
    def parse_line(line: str) -> Password:
        pol, letter, word = line.strip().split()
        policy = (*map(int, pol.split('-')),)
        return Password(policy, letter[0], word)

    with open(filename) as f:
        return [ parse_line(line) for line in f]

def count_valid(passwords: [Password], validator=Password.is_valid) -> int:
    return len(list(filter(validator, passwords)))

if __name__ == "__main__":
    values = load_input("inputs/day2")
    print("Part 1:", count_valid(values))
    print("Part 2:", count_valid(values, Password.is_valid2))
