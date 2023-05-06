with open('input.txt') as f:
    centres = [tuple(int(x) for x in cube.split(',')) for cube in f.read().split('\n') if cube]

X = [c[0] for c in centres]
Y = [c[1] for c in centres]
Z = [c[2] for c in centres]

empty_spaces = [(x, y, z) for x in range(min(X), max(X) + 1) for y in range(min(Y), max(Y) + 1) for z in range(min(Z), max(Z) + 1) if (x, y, z) not in centres]
outer_empty_spaces = [s for s in empty_spaces if s[0] in (min(X), max(X)) or s[1] in (min(Y), max(Y)) or s[2] in (min(Z), max(Z))]
removable = []

def adjust():
    for s1 in outer_empty_spaces + removable.copy():
        for s2 in empty_spaces.copy():
            if sum([abs(s2[x] - s1[x]) for x in range(0, 3)]) == 1:
                empty_spaces.remove(s2)
                removable.append(s2)

lengths = [len(empty_spaces)]
adjust()
lengths.append(len(empty_spaces))
while lengths[-2] != lengths[-1]:
    adjust()
    lengths.append(len(empty_spaces))

def find_surface_area(spaces: list[tuple[int, ...]]):
    count = 0
    for c1 in spaces:
        for c2 in spaces:
            if c2 != c1 and sum([abs(c2[x] - c1[x]) for x in range(0, 3)]) == 1:
                count += 1
    return len(spaces) * 6 - count

print(f'Part 1: {find_surface_area(centres)}')
print(f'Part 2: {find_surface_area(centres) - find_surface_area(empty_spaces)}')
