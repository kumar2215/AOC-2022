with open('input.txt') as f:
    grid = [list(x) for x in f.read().split()]

elf_positions = []
for row_idx, row in enumerate(grid):
    for column_idx, value in enumerate(row):
        if value == '#':
            elf_positions.append((column_idx, row_idx))

directions = ['N', 'S', 'W', 'E']
valid_direction = {elf: () for elf in elf_positions}

def perform_round():
    global valid_direction
    valid_direction = {elf: () for elf in elf_positions}
    for elf in elf_positions:
        x, y = elf
        surrounding = {
            'N': (x, y - 1),
            'S': (x, y + 1),
            'E': (x + 1, y),
            'W': (x - 1, y),
            'NE': (x + 1, y - 1),
            'NW': (x - 1, y - 1),
            'SE': (x + 1, y + 1),
            'SW': (x - 1, y + 1)
        }
        if any(pos in elf_positions for pos in surrounding.values()):
            for direction in directions:
                if not any(pos in elf_positions for (dir, pos) in surrounding.items() if direction in dir):
                    valid_direction[elf] = surrounding[direction]
                    break

    for index, elf in enumerate(elf_positions):
        if valid_direction[elf] != () and list(valid_direction.values()).count(valid_direction[elf]) == 1:
            elf_positions[index] = valid_direction[elf]

    directions.append(directions[0])
    directions.pop(0)

count = 0
while len([val for val in valid_direction.values() if val]) > 0 or count == 0:  # Part 2
    perform_round()
    count += 1
    if count == 10:  # Part 1
        w = max([x for (x, y) in elf_positions]) - min([x for (x, y) in elf_positions]) + 1
        h = max([y for (x, y) in elf_positions]) - min([y for (x, y) in elf_positions]) + 1
        print(w * h - len(elf_positions))

print(count)
