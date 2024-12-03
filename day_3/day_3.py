"""
Advent Of Code 2024
Code written by Milo
--- Day 3: Mull it Over ---
"""
import re
from itertools import chain

# Deal with input.
with open("day_3/input.txt", "r") as file:
    input = file.read().strip()

def part1():
    """
    PART1

    Answer for part1: 179834255
    """
    data = re.findall(r"mul\((\d+),(\d+)\)", input)
    return sum(map(lambda x: int(x[0]) * int(x[1]), data))

def part2():
    """
    PART2

    Answer for part2: 80570939
    """

    data = list(chain.from_iterable(map(lambda x: re.findall(r"mul\((\d+),(\d+)\)", x.split("don't")[0]), re.split(r"do(?!n\'t)", input))))
    return sum(map(lambda x: int(x[0]) * int(x[1]), data))

def main():
    print(f"Part1: {part1()}\nPart2: {part2()}")

if __name__ == "__main__":
    main()