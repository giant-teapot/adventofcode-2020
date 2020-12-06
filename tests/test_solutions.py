""" Solution validation unit tests.

Those unit tests ensure that the code still provide the correct results, as
validated by the Advent of Code website. The goal is to ensure non-regression
after a refactoring, for instance.
"""

from aoc import day1, day2, day3, day4, day5, day6

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

def test_day_3():
    """ Validate solutions for day 3 puzzle """
    from functools import partial
    from math import prod

    forest_map = day3.load_input("inputs/day3")
    assert day3.count_trees(forest_map, 3, 1) == 268

    count = partial(day3.count_trees, forest_map)
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    assert prod(map(lambda x: count(*x), slopes)) == 3093068400

def test_day_4():
    """ Validate solutions for day 4 puzzle """
    passports = day4.load_input("inputs/day4")
    assert day4.count_valid(passports, day4.check_keys) == 264
    assert day4.count_valid(passports, day4.validate) == 224

def test_day_5():
    """ Validate solutions for day 5 puzzle """
    seats = day5.load_input("inputs/day5")
    seat_ids = list(map(day5.seat_id, seats))
    assert max(seat_ids) == 991
    missing_seats = day5.missing_seats(seat_ids)
    assert (len(missing_seats) == 1) and (534 in missing_seats)

def test_day_6():
    """ Validate solutions for day 6 puzzle """
    group_answers = day6.load_input("inputs/day6")
    assert sum(map(day6.answers_union, group_answers)) == 6583
    assert sum(map(day6.answers_intersection, group_answers)) == 3290
