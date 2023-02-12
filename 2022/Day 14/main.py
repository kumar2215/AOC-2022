with open('input.txt') as f:
    structures = [structure.split(' -> ') for structure in f.read().splitlines()]
    for index, structure in enumerate(structures):
        structures[index] = [tuple(int(num) for num in point.split(',')) for point in structure]

max_depth = max([point[1] for structure in structures for point in structure])

floor = [(x, max_depth + 2) for x in range(500 - 2 * max_depth, 500 + 2 * max_depth)]
structures.append(floor)
occupied_coordinates = {}

def set_up():
    occupied_coordinates.clear()
    for structure in structures:
        for i in range(len(structure) - 1):
            start, end = structure[i], structure[i+1]
            if start[0] == end[0]:
                S, E = min(start[1], end[1]), max(start[1], end[1])
                for y in range(S, E + 1):
                    occupied_coordinates[(start[0], y)] = '#'
            elif start[1] == end[1]:
                S, E = min(start[0], end[0]), max(start[0], end[0])
                for x in range(S, E + 1):
                    occupied_coordinates[(x, start[1])] = '#'

def det_placer(bead: tuple):
    bottom = (bead[0], bead[1] + 1)
    while bottom not in occupied_coordinates and bead[1] <= max_depth:
        bead = bottom
        bottom = (bead[0], bead[1] + 1)
    if bead[1] > max_depth:
        return False
    bottom_left = (bead[0] - 1, bead[1] + 1)
    bottom_right = (bead[0] + 1, bead[1] + 1)
    if bottom_left not in occupied_coordinates:
        return det_placer(bottom_left)
    elif bottom_right not in occupied_coordinates:
        return det_placer(bottom_right)
    else:
        occupied_coordinates[bead] = 'o'
        return True

def main(part):
    global max_depth
    set_up()
    bp, max_depth = [(1, max_depth), (0, max_depth + 2)][part - 1]
    stop = False
    while not stop:
        bead = (500, 0)
        while bead not in occupied_coordinates:
            bead = (bead[0], bead[1] + 1)
            if bead[1] > max_depth:
                stop = True
        bead = (bead[0], bead[1] - 1)
        if bead[1] < bp or not det_placer(bead):
            break
    return len([coord for coord in occupied_coordinates if occupied_coordinates[coord] == 'o'])

print(f'Part 1: {main(1)}')
print(f'Part 2: {main(2)}')
