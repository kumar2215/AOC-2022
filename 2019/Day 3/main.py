
with open('input.txt') as f:
    instructions_1, instructions_2 = f.read().split('\n')
    instructions_1, instructions_2 = instructions_1.split(','), instructions_2.split(',')

def get_path(instructions):
    current = (0, 0)
    path = [current]
    for instruction in instructions:
        direction, steps = instruction[0], int(instruction[1:])
        x, y = current
        if direction == 'R':
            path.extend([(x + i, y) for i in range(1, steps + 1)])
            current = (x + steps, y)
        elif direction == 'L':
            path.extend([(x - i, y) for i in range(1, steps + 1)])
            current = (x - steps, y)
        elif direction == 'U':
            path.extend([(x, y + i) for i in range(1, steps + 1)])
            current = (x, y + steps)
        elif direction == 'D':
            path.extend([(x, y - i) for i in range(1, steps + 1)])
            current = (x, y - steps)
    return path

path_1 = get_path(instructions_1)
path_2 = get_path(instructions_2)
intersections = set(path_1).intersection(set(path_2))
intersections.remove((0, 0))
intersections = sorted(intersections, key=lambda pt: abs(pt[0]) + abs(pt[1]))

steps_to_get_there = [path_1.index(i) + path_2.index(i) for i in intersections]

print(f"Part 1: {abs(intersections[0][0]) + abs(intersections[0][1])}")
print(f"Part 2: {min(steps_to_get_there)}")
