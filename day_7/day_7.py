"""
Advent Of Code 2024
Code written by Milo
--- Day 7: Bridge Repair ---
"""
from functools import reduce
# Deal with input.
with open("day_7/input.txt", "r") as file:
    input = file.read().splitlines()
    equations = {int(key): list(map(int, values.split())) for key, values in map(lambda x: x.split(": "), input)}

def all_combinations(key, digits):
    return key in reduce(
        lambda acc, x: [a + x for a in acc] + [a * x for a in acc], digits[1:], [digits[0]]
    )

def all_combinations2(key, digits):
    return key in reduce(
        lambda acc, x: [a + x for a in acc] + [a * x for a in acc] + [int(str(a) + str(x)) for a in acc], digits[1:], [digits[0]]
    )

def part1():
    """
    PART1

    Answer for part1: 1985268524462
    """
    return sum(key for key, values in equations.items() if all_combinations(key, values))

def part2():
    """
    PART2

    Answer for part2: 150077710195188
    """
    return sum(key for key, values in equations.items() if all_combinations2(key, values))

def main():
    print(f"Part1: {part1()}\nPart2: {part2()}")

if __name__ == "__main__":
    main()