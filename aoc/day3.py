#!/usr/bin/env python3
"""
Day 3: Toboggan Trajectory

https://adventofcode.com/2020/day/3
"""

import math

def load_input(filename: str) -> [[bool]]:
    with open(filename) as map_file:
        return [
            [ c=='#' for c in line.strip()]
            for line in map_file
        ]

def toboggan_slope(forest: [[bool]], x_slope: int, y_slope: int):
    forest_width, forest_height = len(forest[0]), len(forest)
    x, y = x_slope, y_slope
    while y < forest_height:
        yield forest[y][x%forest_width]
        x = x+x_slope
        y = y+y_slope

def count_trees(forest, x_slope, y_slope):
    return sum(1 for tree in toboggan_slope(forest, x_slope, y_slope) if tree)

if __name__ == "__main__":
    forest_map = load_input("inputs/day3")
    print("Part 1:", count_trees(forest_map, 3, 1))
    print("Part 2:", math.prod([
        count_trees(forest_map, 1, 1),
        count_trees(forest_map, 3, 1),
        count_trees(forest_map, 5, 1),
        count_trees(forest_map, 7, 1),
        count_trees(forest_map, 1, 2)
    ]))
