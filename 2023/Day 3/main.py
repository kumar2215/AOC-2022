
with open('input.txt') as f:
    grid = {(i, j): char for j, line in enumerate(f.read().split('\n')) for i, char in enumerate(line)}

nums = {}
visited = []

for pt in grid:
    if grid[pt].isnumeric() and pt not in visited:
        lst = [pt]
        s = grid[pt]
        visited.append(pt)
        while True:
            next_pt = (pt[0] + 1, pt[1])
            if next_pt in grid and grid[next_pt].isnumeric():
                lst.append(next_pt)
                s += grid[next_pt]
                visited.append(next_pt)
                pt = next_pt
            else:
                nums[tuple(lst)] = s
                break

grid = {pt: grid[pt] for pt in grid if not grid[pt].isnumeric()}
part_numbers = []
gears = {}

for points in nums:
    surrounding = []
    num = int(nums[points])
    for point in points:
        x, y = point
        poss_surrounding = [(x + i, y + j) for i in (-1, 0, 1) for j in (-1, 0, 1) if i != j or i != 0]
        for pt in poss_surrounding:
            if pt in grid and pt not in points:
                surrounding.append(pt)
    if any(grid[pt] != '.' for pt in surrounding):
        part_numbers.append(num)
    for pt in surrounding:
        if grid[pt] == '*':
            if pt in gears:
                gears[pt].append(num)
            else:
                gears[pt] = [num]

gears = {pt: list(set(gears[pt])) for pt in gears}
gears = {pt: gears[pt][0] * gears[pt][1] for pt in gears if len(gears[pt]) == 2}

print(f"Part 1: {sum(part_numbers)}")
print(f"Part 2: {sum(gears.values())}")
