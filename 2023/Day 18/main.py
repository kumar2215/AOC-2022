
from itertools import pairwise
with open("input.txt") as f:
    lines = [line.split() for line in f.read().split('\n')]
    instructions_1 = [(line[0], int(line[1])) for line in lines]
    dct = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}
    instructions_2 = [(dct[line[2][-2]], int(line[2][1:-2].replace('#', '0x'), 16)) for line in lines]

def get_area(instructions):
    curr = (1, 1)
    grid = [curr]
    for direction, steps in instructions:
        if direction == 'R':
            for _ in range(steps):
                x, y = curr
                curr = (x + 1, y)
                grid.append(curr)
        elif direction == 'L':
            for _ in range(steps):
                x, y = curr
                curr = (x - 1, y)
                grid.append(curr)
        elif direction == 'D':
            for _ in range(steps):
                x, y = curr
                curr = (x, y + 1)
                grid.append(curr)
        elif direction == 'U':
            for _ in range(steps):
                x, y = curr
                curr = (x, y - 1)
                grid.append(curr)
    grid.append((1, 1))
    n = len(grid)
    new_grid = (pt for pt in grid)
    del grid
    A = 0
    for p1, p2 in pairwise(new_grid):
        x1, y1 = p1
        x2, y2 = p2
        A += x1 * y2 - y1 * x2
    return (abs(A) + n + 1) // 2

print(f"Part 1: {get_area(instructions_1)}")
print(f"Part 2: {get_area(instructions_2)}")
