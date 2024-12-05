"""
Advent Of Code 2024
Code written by Milo
--- Day 5: Pint Queue ---
"""
from functools import reduce

# Deal with input.
with open("day_5/input.txt", "r") as file:
    rules, updates = map(lambda x: x.split("\n"), file.read().strip().split("\n\n"))
    rules = list(map(lambda row: tuple(map(int, row.split("|"))), rules))
    updates = list(map(lambda row: list(map(int, row.split(","))), updates))

# Part 1 main solution
def in_order(update):
    for rule in rules:
        if not _rule_applies(rule, update):
            return False
    return True

# Part 2 main solution
def fix_order(update):
    prev, curr = None, update
    while prev != curr:
        prev, curr = curr, _apply_rules(curr[:])
    return curr

# Helper functions
def _rule_applies(rule, update):
    if rule[0] in update and rule[1] in update:
        return update.index(rule[0]) < update.index(rule[1])
    return True

def _apply_rules(update):
    return reduce(lambda acc, rule: acc if _rule_applies(rule, acc) else _swap(acc, *rule), rules, update)

def _swap(update, a, b):
    a_idx, b_idx = update.index(a), update.index(b)
    update[a_idx], update[b_idx] = update[b_idx], update[a_idx]
    return update

# Main functions
def part1():
    """
    PART1

    Answer for part1: 7365
    """
    return sum(map(lambda update: update[len(update)//2] if in_order(update) else 0, updates))

def part2():
    """
    PART2

    Answer for part2:
    """
    return sum(map(lambda update: fix_order(update)[len(update)//2], filter(lambda update: not in_order(update),updates)))

def main():
    print(f"Part1: {part1()}\nPart2: {part2()}")

if __name__ == "__main__":
    main()