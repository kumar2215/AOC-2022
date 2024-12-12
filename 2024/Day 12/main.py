from collections import defaultdict
with open("input.txt") as f:
    grid = [list(line) for line in f.read().split("\n")]

ROWS, COLS = len(grid), len(grid[0])
REIGONS = defaultdict(list)
for i in range(ROWS):
    for j in range(COLS):
        plant = grid[i][j]
        REIGONS[plant].append((i, j))

class UnionFind:
    def __init__(self, lst, pred):
        n = len(lst)
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.n = n
        for i in range(n):
            for j in range(i + 1, n):
                if pred(lst[i], lst[j]):
                    self.union(i, j)
        self.groups = defaultdict(list)
        for i in range(n):
            self.groups[self.find(i)].append(lst[i])

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

def is_adjacent(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2) == 1

def is_adjacent2(s1, s2):
    if s1[0] != s2[0]: return False
    return is_adjacent(s1[1:], s2[1:])   

REIGONS = {plant: UnionFind(REIGONS[plant], is_adjacent).groups for plant in REIGONS}

def get_parameter_and_sides(plant, reigon, points):
    count, sides = 0, set()
    for pt in points:
        X, Y = pt
        closest = [(X + 1, Y), (X - 1, Y), (X, Y + 1), (X, Y - 1)]
        for point in closest:
            x, y = point
            if (not 0 <= x < ROWS) or (not 0 <= y < COLS) or (not point in REIGONS[plant][reigon]):
                count += 1
                if point == (X+1, Y): sides.add(('v', X, Y))
                elif point == (X-1, Y): sides.add(('^', X, Y))
                elif point == (X, Y+1): sides.add(('>', X, Y))
                elif point == (X, Y-1): sides.add(('<', X, Y))
    return count, UnionFind(list(sides), is_adjacent2).n

total_price, total_price2 = 0, 0
for plant in REIGONS:
    for group in REIGONS[plant]:
        parameter, sides = get_parameter_and_sides(plant, group, REIGONS[plant][group])
        N = len(REIGONS[plant][group])
        total_price += N * parameter
        total_price2 += N * sides
        
print(f"Part 1: {total_price}")
print(f"Part 2: {total_price2}")