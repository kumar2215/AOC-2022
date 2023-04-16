with open('input.txt') as f:
    centres = [tuple(int(x) for x in cube.split(',')) for cube in f.read().split('\n')]

class Cube:

    def __init__(self, centre: tuple):
        self.centre = centre
        x, y, z = centre
        self.vertices = []
        self.sides = {}
        for i in range(-1, 2):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    if all(d != 0 for d in (i, j, k)):
                        self.vertices.append((x + i / 2, y + j / 2, z + k / 2))
                    if abs(i) + abs(j) + abs(k) == 1:
                        self.sides[(i, j, k)] = []
        for vertice in self.vertices:
            X, Y, Z = vertice
            dct = {0: (X - x) * 2, 1: (Y - y) * 2, 2: (Z - z) * 2}
            for index in dct:
                tup = [0, 0, 0]
                tup[index] = dct[index]
                self.sides[tuple(tup)].append(vertice) # NOQA

cubes = [Cube(centre) for centre in centres]

X = [c[0] for c in centres]
Y = [c[1] for c in centres]
Z = [c[2] for c in centres]
empty_spaces = [(x, y, z) for x in range(min(X), max(X) + 1) for y in range(min(Y), max(Y) + 1) for z in range(min(Z), max(Z) + 1)
                if (x, y, z) not in centres]
outer_empty_spaces = [s for s in empty_spaces if s[0] in (min(X), max(X)) or s[1] in (min(Y), max(Y)) or s[2] in (min(Z), max(Z))]

lengths = [len(empty_spaces)]
removable = []

def adjust():
    for s1 in outer_empty_spaces + removable.copy():
        for s2 in empty_spaces.copy():
            if sum([abs(s2[x] - s1[x]) for x in range(0, 3)]) == 1:
                empty_spaces.remove(s2)
                removable.append(s2)

adjust()
lengths.append(len(empty_spaces))
while lengths[-2] != lengths[-1]:
    adjust()
    lengths.append(len(empty_spaces))

empty_spaces = [Cube(space) for space in empty_spaces]

def find_surface_area(spaces: list[Cube]):
    count = 0
    for c1 in spaces:
        for c2 in spaces:
            if c2 is not c1 and sum([abs(c2.centre[x] - c1.centre[x]) for x in range(0, 3)]) == 1:
                for n in c2.sides:
                    N = tuple(-c for c in n)
                    if c2.sides[n] == c1.sides[N]:
                        count += 1
    return len(spaces) * 6 - count

print(f'Part 1: {find_surface_area(cubes)}')
print(f'Part 2: {find_surface_area(cubes) - find_surface_area(empty_spaces)}')
