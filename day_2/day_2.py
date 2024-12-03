"""
Advent Of Code 2024
Code written by Milo
"""

# Deal with input.
with open("day_2/input.txt", "r") as file:
    input = list(map(lambda row: list(map(int,row.split())),file.read().splitlines()))

# Function for part1
def level_safe(level):
    level_angle = -1 if level[0] == max(level) else 1
    return (list(map(lambda x: x in range(level_angle, level_angle*4, level_angle), map(lambda x: x[1] - x[0], zip(level, level[1:])))))


# Functions for part2
def safe_when_fixed(level):
    return all(level_safe(level)) or any(all(level_safe(level[:i] + level[i+1:])) for i in range(len(level)))


# Main functions
def part1():
    """
    PART1

    Answer for part1: 306
    """
    return sum(map(lambda x: 1 if all(level_safe(x)) else 0,input))


def part2():
    """
    PART2

    Answer for part2: 366
    """
    return sum(map(lambda x: 1 if safe_when_fixed(x) else 0, input))

def main():
    print(f"Part1: {part1()}\nPart2: {part2()}")

if __name__ == "__main__":
    main()