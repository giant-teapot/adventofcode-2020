#!/usr/bin/env python3
"""
Day 5: Binary Boarding

https://adventofcode.com/2020/day/5
"""

from typing import Set

def load_input(filename: str):
    with open(filename) as f:
        return map(str.strip, f.readlines())

def row_number(seat: str) -> int:
    binary = ''.join(('0' if c=='F' else '1' for c in seat[:7]))
    return int(binary, 2)

def column_number(seat: str) -> int:
    binary = ''.join(('0' if c=='L' else '1' for c in seat[-3:]))
    return int(binary, 2)

def seat_id(seat: str) -> int:
    return row_number(seat)*8 + column_number(seat)

def missing_seats(seat_ids: [int]) -> Set[int]:
    min_seat, max_seat = min(seat_ids), max(seat_ids)
    return set((x for x in range(min_seat, max_seat))) - set(seat_ids)


if __name__ == "__main__":
    seats = load_input("inputs/day5")
    seat_ids = list(map(seat_id, seats))
    print("Part 1:", max(seat_ids))
    print("Part 2:", missing_seats(seat_ids).pop())
