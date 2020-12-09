""" Solution validation unit tests.

Those unit tests ensure that the code still provide the correct results, as
validated by the Advent of Code website. The goal is to ensure non-regression
after a refactoring, for instance.
"""

from aoc import day1, day2, day3, day4, day5, day6, day7, day8, day9

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

def test_day_7():
    """ Validate solutions for day 7 puzzle """
    specs = day7.load_input("inputs/day7")
    assert len(day7.search_containers(specs, "shiny gold")) == 115
    assert day7.count_bags_inside(specs, "shiny gold")-1 == 1250

def test_day_8():
    """ Validate solutions for day 8 puzzle """
    program = day8.load_input("inputs/day8")
    assert day8.run(program)[1].acc == 1814
    assert day8.repair_and_run(program).acc == 1056

def test_day_9():
    """ Validate solutions for day 9 puzzle """
    numbers = day9.load_input("inputs/day9")
    day9.find_invalid_number(numbers, 25) == 25918798
    day9.find_weakness(numbers, 25) == 3340942
