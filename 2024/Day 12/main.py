from collections import defaultdict
with open("input.txt") as f:
    grid = [list(line) for line in f.read().split("\n")]

ROWS = len(grid)
COLS = len(grid[0])
REIGONS = defaultdict(list)
for i in range(ROWS):
    for j in range(COLS):
        plant = grid[i][j]
        REIGONS[plant].append((i, j))

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.n = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.size[px] < self.size[py]:
                px, py = py, px
            self.parent[py] = px
            self.size[px] += self.size[py]
            self.n -= 1

for plant in REIGONS:
    points = REIGONS[plant]
    reigon = UnionFind(len(points))
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
           dx, dy = abs(points[i][0] - points[j][0]), abs(points[i][1] - points[j][1])
           if 0 <= dx <= 1 and 0 <= dy <= 1 and 0 < dx + dy <= 2:
               reigon.union(i, j)
    REIGONS[plant] = defaultdict(set)
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            if reigon.find(i) == reigon.find(j):
                REIGONS[plant][reigon.find(i)].add(points[j])
        REIGONS[plant][reigon.find(i)].add(points[i])

def get_parameter(plant, reigon):
    def check(pt):
        X, Y = pt
        count = 0
        closest = [(X + 1, Y), (X - 1, Y), (X, Y + 1), (X, Y - 1)]
        for point in closest:
            x, y = point
            if (not 0 <= x < ROWS) or (not 0 <= y < COLS) or (not point in REIGONS[plant][reigon]):
                count += 1
        return count
    return check

AREAS = {plant: {group: len(REIGONS[plant][group]) for group in REIGONS[plant]} for plant in REIGONS}
PERIMETERS = {plant: {group: sum(map(get_parameter(plant, group), REIGONS[plant][group])) for group in REIGONS[plant]} for plant in REIGONS}

total_price = 0
for plant in REIGONS:
    for group in REIGONS[plant]:
        total_price += AREAS[plant][group] * PERIMETERS[plant][group]
print(f"Part 1: {total_price}")
