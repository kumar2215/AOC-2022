with open("input.txt") as f:
    grid = [[int(x) for x in list(line)] for line in f.read().split("\n")]

ROWS, COLS = len(grid), len(grid[0])
trail_heads = {(x, y) for y, row in enumerate(grid) for x, cell in enumerate(row) if cell == 0}

def can_be_next(X, Y):
    def can(next_pt):
        x, y = next_pt
        return 0 <= x < COLS and 0 <= y < ROWS and grid[y][x] - grid[Y][X] == 1
    return can

def get_next_possible_pos(x, y):
    return filter(can_be_next(x, y), [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)])
    
def get_trailhead_score(pt):
    frontier, seen= [pt], set()
    score, paths = 0, {(pt,)}
    while frontier:
        new_frontier = []
        for point in frontier:
            if point in seen: continue
            seen.add(point)
            x, y = point
            if grid[y][x] == 9: 
                score += 1
                continue
            else:
                next_poss = list(get_next_possible_pos(x, y))
                new_frontier.extend(next_poss)
                for path in filter(lambda p: p[-1] == point, paths.copy()):
                    paths.remove(path)
                    for new_pt in next_poss:
                        paths.add(path + (new_pt,))
        frontier = new_frontier
    return score, len(paths)

total_score, total_rating = 0, 0
for point in trail_heads:
    score, rating = get_trailhead_score(point)
    total_score += score
    total_rating += rating
    
print(f"Part 1: {total_score}")
print(f"Part 2: {total_rating}")