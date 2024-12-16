"""
Advent Of Code 2024
Code written by Milo
--- Day 8: Resonant Collinearity ---
"""
import pandas as pd
from ordered_set import OrderedSet
from itertools import combinations

# Deal with input.
with open("day_8/input.txt", "r") as file:
    grid = [list(line) for line in file.read().splitlines()]

df = pd.DataFrame(grid)

def in_bounds(r, c):
    return 0 <= r < len(df) and 0 <= c < len(df.columns)

def get_pairs(r, c):
    freq = df.iloc[r, c]
    return OrderedSet((row, col) for row, col in df[df == freq].stack().index)

def find_antinodes(antennas: OrderedSet):
    antinodes = set()
    for (r1, c1), (r2, c2) in combinations(antennas, 2):
        dr, dc = r2 - r1, c2 - c1
        antinodes.update({(r2 + dr, c2 + dc), (r1 - dr, c1 - dc)})
    return {a for a in antinodes if in_bounds(*a)}

def find_antinodes2(antennas: OrderedSet):
    antinodes = set()
    for (r1, c1), (r2, c2) in combinations(antennas, 2):
        antinodes.update([(r1, c1), (r2, c2)])
        dr, dc = r2 - r1, c2 - c1
        # Forward direction
        a = (r2 + dr, c2 + dc)
        while in_bounds(*a):
            antinodes.add(a)
            a = (a[0] + dr, a[1] + dc)
        # Backward direction
        a = (r1 - dr, c1 - dc)
        while in_bounds(*a):
            antinodes.add(a)
            a = (a[0] - dr, a[1] - dc)
    return antinodes

def solve(func=find_antinodes):
    antinodes = set()
    for row, col in df.stack().index:
        if df.iloc[row, col] != ".":
            antinodes.update(func(get_pairs(row, col)))
    return len(antinodes)


def part1():
    """
    PART1

    Answer for part1:
    """
    return solve()

def part2():
    """
    PART2

    Answer for part2:
    """
    return solve(find_antinodes2)

def main():
    print(f"Part1: {part1()}\nPart2: {part2()}")

if __name__ == "__main__":
    main()