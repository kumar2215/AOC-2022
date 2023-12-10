
from itertools import pairwise
with open("input.txt") as f:
    lines = f.read().split('\n')
    grid = {}
    dct = {
        '|': {'^': '^', 'v': 'v'},
        '-': {'>': '>', '<': '<'},
        'L': {'v': '>', '<': '^'},
        'J': {'v': '<', '>': '^'},
        '7': {'>': 'v', '^': '<'},
        'F': {'^': '>', '<': 'v'},
        '.': '.',
        'S': 'S'
    }
    start = ()
    for j, line in enumerate(lines, start=1):
        for i, char in enumerate(line, start=1):
            if char == 'S':
                start = (i, j)
            grid[(i, j)] = dct[char]

x, y = start
num_count = {}
counter = 0
pointers = {
    (x + 1, y): '>',
    (x - 1, y): '<',
    (x, y + 1): 'v',
    (x, y - 1): '^'
}
pointers = {p: pointers[p] for p in pointers if p in grid}

while any(pointer not in num_count for pointer in pointers):
    counter += 1
    for pointer in pointers.copy():
        direction = pointers[pointer]
        pointers.pop(pointer)
        if direction in grid[pointer]:
            nx, ny = pointer
            next_direction = grid[pointer][direction]
            if pointer not in num_count:
                num_count[pointer] = counter
            if next_direction == '>' and (new_pt := (nx + 1, ny)) in grid:
                pointers[new_pt] = next_direction
            elif next_direction == '<' and (new_pt := (nx - 1, ny)) in grid:
                pointers[new_pt] = next_direction
            elif next_direction == '^' and (new_pt := (nx, ny - 1)) in grid:
                pointers[new_pt] = next_direction
            elif next_direction == 'v' and (new_pt := (nx, ny + 1)) in grid:
                pointers[new_pt] = next_direction

path = [start] + [pt for i, pt in enumerate(list(num_count.keys())) if i % 2 == 0] + [pt for i, pt in enumerate(list(num_count.keys())) if i % 2 == 1][::-1] + [start]
area = 0
for pair in pairwise(path):
    (x1, y1), (x2, y2) = pair
    area += x1 * y2 - y1 * x2

print(f"Part 1: {counter}")
print(f"Part 2: {(abs(area) - len(num_count) + 1) // 2}")
