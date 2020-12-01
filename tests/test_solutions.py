from aoc import day1

def test_day_1():
    values = day1.load_input("inputs/day1")
    assert(day1.find_entries_adding_up_to_2020(values, nb_entries=2) == 970816)
    assert(day1.find_entries_adding_up_to_2020(values, nb_entries=3) == 96047280)
