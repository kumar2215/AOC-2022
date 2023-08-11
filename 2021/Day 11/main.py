
with open('input.txt', 'r') as f:
    grid = {(i, j): int(value) for j, line in enumerate(f.read().split('\n')) for i, value in enumerate(line)}

flashes = 0
counter = 0
def perform_step():
    global flashes, counter
    flashed_octopuses = []
    for octopus_pos in grid:
        grid[octopus_pos] += 1
    while not all(val <= 9 for val in grid.values()):
        for octopus_pos in grid.copy():
            if grid[octopus_pos] > 9:
                flashed_octopuses.append(octopus_pos)
                grid[octopus_pos] = 0
                if counter < 100: flashes += 1
                x, y = octopus_pos
                points = [(x + i, y + j) for i in range(-1, 2) for j in range(-1, 2) if (x + i, y + j) != octopus_pos and (x + i, y + j) in grid]
                for point in points:
                    grid[point] += 1
    for octopus_pos in flashed_octopuses:
        grid[octopus_pos] = 0
    counter += 1

while not all(val == 0 for val in grid.values()):
    perform_step()

print(f"Part 1: {flashes}")
print(f"Part 2: {counter}")
