
from itertools import combinations
with open("input.txt") as f:
    rows = [list(x) for x in f.read().split('\n')]
    rows_with_no_galaxies = [j for j, row in enumerate(rows, start=1) if all(c == '.' for c in row)]
    columns = [[row[c] for row in rows] for c in range(len(rows[0]))]
    columns_with_no_galaxies = [i for i, column in enumerate(columns, start=1) if all(r == '.' for r in column)]
    galaxies = [(i, j) for j, row in enumerate(rows, start=1) for i, char in enumerate(row, start=1) if char == '#']

total, m = 0, 2
total_2, m2 = 0, 1_000_000
for pair in combinations(galaxies, 2):
    (x1, y1), (x2, y2) = pair
    x1, x2, y1, y2 = min(x1, x2), max(x1, x2), min(y1, y2), max(y1, y2)
    extra_rows, extra_cols = [r for r in rows_with_no_galaxies if y1 < r < y2], [c for c in columns_with_no_galaxies if x1 < c < x2]
    total += abs(x2 - x1) + abs(y2 - y1) + (len(extra_rows) + len(extra_cols)) * (m - 1)
    total_2 += abs(x2 - x1) + abs(y2 - y1) + (len(extra_rows) + len(extra_cols)) * (m2 - 1)

print(f"Part 1: {total}")
print(f"Part 2: {total_2}")
