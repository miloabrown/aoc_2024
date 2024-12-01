"""
Advent Of Code 2024
Code written by Milo
Day1: Historian Hysteria
"""
from collections import Counter
# Deal with input.
with open("day_1/input.txt", "r") as file:
    input = list(map(lambda row: list(map(int, row.split())), file.read().splitlines()))

def part1():
    """
    PART1
    Answer for part1: 1530215
    """
    return sum(map(lambda pair: abs(pair[0]-pair[1]),zip(*list(map(lambda column: sorted(column), zip(*input))))))

def part2():
    """
    PART2
    Answer for part2: 26800609
    """
    left, right = zip(*input)
    return sum(map(lambda number: number*Counter(right)[number],left))

def main():
    print(f"Part1: {part1()}\nPart2: {part2()}")

if __name__ == "__main__":
    main()
