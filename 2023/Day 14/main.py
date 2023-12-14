
with open("input.txt") as f:
    rows = f.read().split("\n")
    rounded_rocks = []
    grid = {}
    n = len(rows)
    for j, row in enumerate(rows, start=1):
        for i, char in enumerate(row, start=1):
            if char == 'O':
                rounded_rocks.append((i, n - j + 1))
            grid[(i, n - j + 1)] = char

directions = {
    'N': lambda pt: (pt[0], pt[1] + 1),
    'W': lambda pt: (pt[0] - 1, pt[1]),
    'S': lambda pt: (pt[0], pt[1] - 1),
    'E': lambda pt: (pt[0] + 1, pt[1])
}
pattern = []
pointer = 0
lst = list(directions.keys())

def tilt():
    global rounded_rocks, grid, pointer
    new_grid = grid
    direction = lst[pointer % 4]
    next_ = directions[direction]
    if direction in ('S', 'E'):
        rounded_rocks.reverse()
    for rock in rounded_rocks:
        new_pos = next_(rock)
        while new_pos in new_grid and new_grid[new_pos] == '.':
            new_grid[rock] = '.'
            new_grid[new_pos] = 'O'
            rock = new_pos
            new_pos = next_(new_pos)
    rounded_rocks = [pos for pos in new_grid if new_grid[pos] == 'O']
    grid = new_grid
    pointer += 1
    count = sum([pos[1] for pos in rounded_rocks])
    return count

print(f"Part 1: {tilt()}")

def pattern_exists():
    period = 1
    while period < len(pattern) // 3:
        interval1, interval2, interval3 = [], [], []
        start = 0
        while start + period < len(pattern) // 3:
            interval1 = pattern[start:start + period * 1]
            interval2 = pattern[start + period * 1:start + period * 2]
            interval3 = pattern[start + period * 2:start + period * 3]
            if interval1 and interval1 == interval2 == interval3 and period > 1:
                return start, period, interval1
            else:
                start += 1
        if interval1 and interval1 == interval2 == interval3 and period > 1:
            return start, period, interval1
        else:
            period += 1
    return False

def one_cycle():
    count = 0
    for _ in range(4):
        count = tilt()
    pattern.append(count)

pointer -= 1
while not (result := pattern_exists()):
    one_cycle()

start, period, interval = result
print(f"Part 2: {interval[(1_000_000_000 - start) % period - 1]}")
