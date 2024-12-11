"""
Advent Of Code 2024
Code written by Milo
--- Day 6: Guard Gallivant ---
"""
import re
from ordered_set import OrderedSet

# Deal with input.
with open("day_6/input.txt", "r") as file:
    input = file.read().splitlines()

# Parse start position.
start_row_pattern = re.compile(r"^[.#]*\^[.#]*$")
start_row = next(filter(start_row_pattern.match, input))

# Initial setup
x, y = input.index(start_row), start_row.index("^")
input = list(map(list, input))

def in_bounds(grid, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

def loops(grid, x, y):
    dx, dy = -1, 0
    seen = OrderedSet()

    while True:
        seen.add((x, y, dx, dy))
        if not in_bounds(grid, x+dx, y+dy): return OrderedSet(map(lambda x: (x[0],x[1]), seen))
        if grid[x+dx][y+dy] == "#":
            dy, dx = -dx, dy
        else:
            x, y = x+dx, y+dy
        if (x, y, dx, dy) in seen: return True

def find_loops(grid):
    loop_count = 0

    for row, col in loops(input, x, y):
        if grid[row][col] != ".": continue
        grid[row][col] = "#"
        loop_count += loops(grid, x, y) == True
        grid[row][col] = "."
    return loop_count


def part1():
    """
    PART1

    Answer for part1: 5177
    """
    return len(loops(input, x, y))

def part2():
    """
    PART2

    Answer for part2: 1686
    """
    return find_loops(input)

def main():
    print(f"Part1: {part1()}\nPart2: {part2()}")

if __name__ == "__main__":
    main()