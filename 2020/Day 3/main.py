
from functools import reduce
with open("input.txt") as f:
    rows = [list(x) for x in f.read().split('\n')]
    forest = {(i, j): char for j, row in enumerate(rows) for i, char in enumerate(row)}

R, C = len(rows), len(rows[0])
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
def get_trees(slope):
    dx, dy = slope
    curr = (0, 0)
    trees = 0
    while curr[1] < R:
        if forest[(curr[0] % C, curr[1])] == '#':
            trees += 1
        curr = (curr[0] + dx, curr[1] + dy)
    return trees

print(f"Part 1: {get_trees((3, 1))}")
print(f"Part 2: {reduce(lambda a, b: a * b, [get_trees(s) for s in slopes])}")
