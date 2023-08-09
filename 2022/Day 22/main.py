import numpy as np
with open('input.txt', 'r') as f:
    Input = f.read().split('\n')
    div = Input.index('')
    Map = '\n'.join(Input[0:div])
    instructions = ''.join(Input[div:])
    temp: list[int | str] = [c for c in instructions if c.isalpha()]
    for i, num in enumerate(instructions.replace('R', 'L').split('L')):
        temp.insert(i * 2, int(num))
    instructions = temp

coordinates = {}
for row_idx, row in enumerate(Map.split('\n'), start=1):
    for col_idx, char in enumerate(row, start=1):
        if char != ' ':
            coordinates[(col_idx, row_idx)] = char

l = int((len(coordinates) / 6) ** 0.5)
X = [c[0] for c in coordinates]
Y = [c[1] for c in coordinates]
blocks = {(r, c): [(i, j) for i in row for j in col] for c, col in enumerate(np.split(np.arange(start=1, stop=max(Y) + 1), max(Y) / l), start=1)
          for r, row in enumerate(np.split(np.arange(start=1, stop=max(X) + 1), max(X) / l), start=1)}
blocks = {block: blocks[block] for block in blocks if blocks[block][0] in coordinates}

class Face:

    def __init__(self, face: list):
        self.face = face
        X = [x for (x, y) in face]
        Y = [y for (x, y) in face]
        self.left_edge = [pt for pt in face if pt[0] == min(X)]
        self.right_edge = [pt for pt in face if pt[0] == max(X)]
        self.bottom_edge = [pt for pt in face if pt[1] == max(Y)]
        self.top_edge = [pt for pt in face if pt[1] == min(Y)]

bottom = Face(blocks[(2, 2)])
top = Face(blocks[(1, 4)])
left = Face(blocks[(1, 3)])
right = Face(blocks[(3, 1)])
back = Face(blocks[(2, 1)])
front = Face(blocks[(2, 3)])

connections = {}
def connect(edge_1, edge_2, connection):
    assert len(edge_1) == len(edge_2) == l, ValueError
    c1, c2 = connection
    for i, pt in enumerate(edge_1):
        if coordinates[pt] != '#':
            if coordinates[edge_2[i]] != '#':
                connections[(pt, c1)] = (edge_2[i], c2)
            else:
                connections[(pt, c1)] = None

# this part varies on ur input; so change it accordingly
connect(left.left_edge[::-1], back.left_edge, ('<', '>'))
connect(back.left_edge, left.left_edge[::-1], ('<', '>'))
connect(left.top_edge, bottom.left_edge, ('^', '>'))
connect(bottom.left_edge, left.top_edge, ('<', 'v'))
connect(top.left_edge, back.top_edge, ('<', 'v'))
connect(back.top_edge, top.left_edge, ('^', '>'))
connect(top.bottom_edge, right.top_edge, ('v', 'v'))
connect(right.top_edge, top.bottom_edge, ('^', '^'))
connect(bottom.right_edge, right.bottom_edge, ('>', '^'))
connect(right.bottom_edge, bottom.right_edge, ('v', '<'))
connect(front.right_edge, right.right_edge[::-1], ('>', '<'))
connect(right.right_edge[::-1], front.right_edge, ('>', '<'))
connect(top.right_edge, front.bottom_edge, ('>', '^'))
connect(front.bottom_edge, top.right_edge, ('v', '<'))

orientations = ['>', 'v', '<', '^']
pos = tuple(coordinates.keys())[0]
orientation_idx = 0

def move(instruction: int, part=1):
    global orientation_idx, pos
    orientation = orientations[orientation_idx]
    dct = {'>': (1, 0, False), '<': (1, 0, True), 'v': (0, 1, False), '^': (0, 1, True)}
    a, b, bol = dct[orientation]
    possible_coordinates = sorted([c for c in coordinates if c[a] == pos[a]], key=lambda c: c[b], reverse=bol)
    pos_idx = possible_coordinates.index(pos)
    wall_hit = False
    while pos_idx < len(possible_coordinates) - 1 and instruction:
        pos_idx += 1
        if coordinates[possible_coordinates[pos_idx]] != '#':
            pos = possible_coordinates[pos_idx]
            instruction -= 1
        else:
            wall_hit = True
            break
    if not wall_hit and instruction:
        if part == 1:
            if coordinates[possible_coordinates[0]] != '#':
                pos = possible_coordinates[0]
                instruction -= 1
                move(instruction)
        else:
            if connections[(pos, orientation)] is not None:
                next_pos, new_orientation = connections[(pos, orientation)]
                orientation_idx = orientations.index(new_orientation)
                pos = next_pos
                instruction -= 1
                move(instruction, part=2)

def main(part):
    global orientation_idx, pos
    pos = tuple(coordinates.keys())[0]
    orientation_idx = 0
    for instruction in instructions:
        if isinstance(instruction, int):
            move(instruction, part=part)
        elif isinstance(instruction, str):
            if instruction == 'R':
                orientation_idx = (orientation_idx + 1) % len(orientations)
            else:
                orientation_idx = (orientation_idx - 1) % len(orientations)
    col, row = pos
    return 1000 * row + 4 * col + orientation_idx

print(f"Part 1: {main(1)}")
print(f"Part 2: {main(2)}")
