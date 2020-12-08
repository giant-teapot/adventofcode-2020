#!/usr/bin/env python3
"""
Day 7: Handy Haversacks

https://adventofcode.com/2020/day/7
"""

import operator
from typing import Set

def parse_bag_content(content:str) -> (int, str):
    n, c = content.split(maxsplit=1)
    n, c = int(n), c.strip(".\n")
    if n == 1:
        return n, c[:-len(' bag')]
    else:
        return n, c[:-len(' bags')]

def parse_bag_spec(spec_line: str) -> (str, [(int, str)]):
    """ Container -> [Contained] """
    color, bag_content = spec_line.split(" bags contain ")
    if bag_content == 'no other bags.\n':
        return (color, [])

    return (color, list(map(parse_bag_content, bag_content.split(', '))))

def load_input(filename: str):
    with open(filename) as f:
        return {
            color: inner_bags
            for color, inner_bags in map(parse_bag_spec, f.readlines())
        }

def search_containers(bag_specs, color: str) -> Set[str]:
    container_lookup = {} # Containee -> container lookup
    for container, containees in bag_specs.items():
        colors = map(operator.itemgetter(1), containees)
        for c in colors:
            if c not in container_lookup:
                container_lookup[c] = [container]
            else:
                container_lookup[c].append(container)

    container_bags = container_lookup.get(color, [])
    containers = set()
    while len(container_bags) > 0:
        bag = container_bags.pop()
        possible_containers = container_lookup.get(bag, [])
        container_bags.extend(possible_containers)
        containers.add(bag)

    return containers

def count_bags_inside(bag_specs, color: str) -> int:
    content = bag_specs.get(color)
    return 1+sum((n*count_bags_inside(bag_specs, c) for n, c in content))

if __name__ == "__main__":
    specs = load_input("inputs/day7")
    print("Part 1:", len(search_containers(specs, "shiny gold")))
    print("Part 2:", count_bags_inside(specs, "shiny gold")-1)
