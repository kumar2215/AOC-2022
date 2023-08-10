
with open('input.txt', 'r') as f:
    grid = [[int(x) for x in line] for line in f.read().split('\n')]

positions = {}
for row_idx, row in enumerate(grid):
    for col_idx, height in enumerate(row):
        positions[(col_idx, row_idx)] = height

def get_adjacent_points(point):
    x, y = point
    return [pt for pt in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)] if pt in positions]

low_points = {}
for pos in positions:
    if all(positions[pos] < positions[pt] for pt in get_adjacent_points(pos)):
        low_points[pos] = positions[pos]

basins = []
for low_point in low_points:
    basin = {low_point}
    while not all(positions[pt] == 9 for pos in basin for pt in get_adjacent_points(pos) if pt not in basin):
        for pos in basin:
            basin = basin.union(set(pt for pt in get_adjacent_points(pos) if positions[pt] < 9))
    basins.append(len(basin))
basins.sort(reverse=True)

print(f"Part 1: {sum(low_points.values()) + len(low_points)}")
print(f"Part 2: {basins[0] * basins[1] * basins[2]}")
