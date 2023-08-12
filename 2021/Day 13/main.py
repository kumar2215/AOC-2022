
with open('input.txt', 'r') as f:
    transparent_paper = f.read().split('\n')
    spacing = transparent_paper.index('')
    dots = [tuple(int(c) for c in coordinate.split(',')) for coordinate in transparent_paper[:spacing]]
    max_X = max(x for (x, y) in dots)
    max_Y = max(y for (x, y) in dots)
    coordinates = {(i, j): '#' if (i, j) in dots else ' ' for j in range(max_Y + 1) for i in range(max_X + 1)}
    instructions = [instruction.removeprefix('fold along ').split('=') for instruction in transparent_paper[spacing + 1:]]

def fold(instruction: list):
    axis, val = instruction
    val = int(val)
    assert all({'x': x != val, 'y': y != val}[axis] for (x, y) in dots), ValueError
    if axis == 'x':
        for pos in coordinates.copy():
            x, y = pos
            if x > val and coordinates[pos] == '#':
                coordinates[(2 * val - x, y)] = '#'
                coordinates.pop(pos)
            elif x >= val:
                coordinates.pop(pos)
    else:
        for pos in coordinates.copy():
            x, y = pos
            if y > val and coordinates[pos] == '#':
                coordinates[(x, 2 * val - y)] = '#'
                coordinates.pop(pos)
            elif y >= val:
                coordinates.pop(pos)

first_instruction = instructions.pop(0)
fold(first_instruction)
print(f"Part 1: {len([c for c in coordinates if coordinates[c] == '#'])}")

for instruction in instructions:
    fold(instruction)

code = ''
Y = 0
for pt in sorted(coordinates, key=lambda pos: pos[1]):
    if pt[1] > Y:
        code += '\n'
        code += coordinates[pt]
        Y = pt[1]
    else:
        code += coordinates[pt]

print(f"Part 2: \n{code}")
