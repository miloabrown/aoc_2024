"""
Advent Of Code 2024
Code written by Milo
--- Day 4: Ceres Search ---
"""

# Deal with input.
with open("day_4/input.txt", "r") as file:
    input = file.read().splitlines()

right_border = len(input[0])
bottom_border = len(input)

def in_bounds(x,y):
    return 0 <= x < bottom_border and 0 <= y < right_border

# Function for part1
def count_all_directions(x, y):
    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1), # Vertical and horizontal
        (-1, -1), (1, 1), (-1, 1), (1, -1) # Diagonals
    ]
    return sum(
        1 for dx, dy in directions
        if in_bounds(x + 3 * dx, y + 3 * dy) and
        "".join(input[x + i * dx][y + i * dy] for i in range(4)) == "XMAS"
    )

# Function for part2
def is_x_mas(x,y):
    found = 0
    opposites = {
        (-1, 1): (1, -1),
        (1, 1): (-1, -1)
    }
    for diagonal_1, diagonal_2 in opposites.items():
        if in_bounds(x+diagonal_1[0], y+diagonal_1[1]) and in_bounds(x+diagonal_2[0], y+diagonal_2[1]):
            if input[x+diagonal_1[0]][y+diagonal_1[1]]+input[x+diagonal_2[0]][y+diagonal_2[1]] in ["SM", "MS"]:
                found += 1

    return found == 2

def part1():
    """
    PART1

    Answer for part1: 2358
    """
    return sum([count_all_directions(x,y) for x in range(bottom_border) for y in range(right_border) if input[x][y] == "X"])


def part2():
    """
    PART2

    Answer for part2: 1737
    """
    return sum([is_x_mas(x,y) for x in range(bottom_border) for y in range(right_border) if input[x][y] == "A"])


def main():
    print(f"Part1: {part1()}\nPart2: {part2()}")

if __name__ == "__main__":
    main()