with open('input.txt') as f:
    grid = [list(x) for x in f.read().split()]

start = [grid[0].index('.'), 0]
end = [grid[len(grid)-1].index('.'), len(grid)-1]

blizzard_positions = {'<': [], '>': [], '^': [], 'v': []}
rest_points = []
blizzards = {}
for row_idx, row in enumerate(grid):
    for column_idx, value in enumerate(row):
        if value in ('<', '>', '^', 'v'):
            blizzard_positions[value].append((column_idx, row_idx))
            if value == '>':
                blizzards[(value, (column_idx, row_idx))] = [(i, row_idx) for i in range(1, len(grid[0]) - 1)]
            elif value == '<':
                blizzards[(value, (column_idx, row_idx))] = [(i, row_idx) for i in range(1, len(grid[0]) - 1)][::-1]
            elif value == 'v':
                blizzards[(value, (column_idx, row_idx))] = [(column_idx, i) for i in range(1, len(grid) - 1)]
            elif value == '^':
                blizzards[(value, (column_idx, row_idx))] = [(column_idx, i) for i in range(1, len(grid) - 1)][::-1]

for blizzard in blizzards:
    while blizzards[blizzard][0] != blizzard[1]:
        blizzards[blizzard].insert(0, blizzards[blizzard][len(blizzards[blizzard]) - 1])
        blizzards[blizzard].pop()

initial_blizzard_pos = blizzards.copy()
curr_blizzard_pos = {}
count = 0

def update_rest_points():
    rest_points.clear()
    positions = list(curr_blizzard_pos.keys())
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            if (j, i) not in positions:
                rest_points.append((j, i))

def perform_round(poss_pointers):
    global count, curr_blizzard_pos
    curr_blizzard_pos.clear()
    count += 1
    for key in initial_blizzard_pos.keys():
        if (val := initial_blizzard_pos[key][count % len(initial_blizzard_pos[key])]) not in curr_blizzard_pos:
            curr_blizzard_pos[val] = []
        curr_blizzard_pos[val].append(key[0])
    update_rest_points()
    for index, point in enumerate(poss_pointers.copy()):
        x, y = point
        poss_next_pos = [pos for pos in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)] if 1 <= pos[0] < len(grid[0]) - 1 and 1 <= pos[1] < len(grid) - 1]
        poss_next_pos = [pos for pos in poss_next_pos if pos in rest_points]
        poss_pointers = poss_pointers.union(set(poss_next_pos))
    [poss_pointers.remove(point) for point in poss_pointers.copy() if point in curr_blizzard_pos]
    return poss_pointers

def get_count(last_pointer, poss_pointers):
    internal_count = 0
    while last_pointer not in poss_pointers:
        poss_pointers = perform_round(poss_pointers)
        internal_count += 1
    return internal_count

first_trip_to_goal = get_count((end[0], end[1] - 1), {tuple(start)}) + 1  # Part 1
trip_back_to_start = get_count((start[0], start[1] + 1), {tuple(end)})  # Part 2
trip_back_to_goal = get_count((end[0], end[1] - 1), {tuple(start)})  # Part 2

print(f'Part 1: {first_trip_to_goal}')
print(f'Part 2: {first_trip_to_goal + trip_back_to_start + trip_back_to_goal}')
