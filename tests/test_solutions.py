""" Solution validation unit tests.

Those unit tests ensure that the code still provide the correct results, as
validated by the Advent of Code website. The goal is to ensure non-regression
after a refactoring, for instance.
"""

from aoc import day1, day2

def test_day_1():
    """ Validate solutions for day 1 puzzle """
    values = day1.load_input("inputs/day1")
    assert day1.find_entries_adding_up_to_2020(values, nb_entries=2) == 970816
    assert day1.find_entries_adding_up_to_2020(values, nb_entries=3) == 96047280

def test_day_2():
    """ Validate solutions for day 2 puzzle """
    values = day2.load_input("inputs/day2")
    assert day2.count_valid(values, day2.Password.is_valid) == 548
    assert day2.count_valid(values, day2.Password.is_valid2) == 502
