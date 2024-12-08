from collections import defaultdict
with open("input.txt") as f:
    data = [list(line) for line in f.read().split("\n")]
    
ROWS = len(data)
COLS = len(data[0])
ANTENNAS = defaultdict(list)
for y, row in enumerate(data):
    for x, cell in enumerate(row):
        if cell == '.': continue
        ANTENNAS[cell].append((x, y))
        
def is_in_grid(pt):
    x, y = pt
    return 0 <= x < COLS and 0 <= y < ROWS
        
ANTINODES = {}
ANTINODES2 = {}
for type, antennas in ANTENNAS.items():
    antinodes = set()
    antinodes2 = set()
    for a in antennas:
        for b in antennas:
            if a == b: continue
            dx = b[0] - a[0]
            dy = b[1] - a[1]
            antinode_1 = (b[0] + dx, b[1] + dy)
            antinode_2 = (a[0] - dx, a[1] - dy)
            antinodes2.add(a)
            antinodes2.add(b)
            if is_in_grid(antinode_1): 
                antinodes.add(antinode_1)
                while is_in_grid(antinode_1):
                    antinodes2.add(antinode_1)
                    antinode_1 = (antinode_1[0] + dx, antinode_1[1] + dy)
            if is_in_grid(antinode_2): 
                antinodes.add(antinode_2)
                while is_in_grid(antinode_2):
                    antinodes2.add(antinode_2)
                    antinode_2 = (antinode_2[0] - dx, antinode_2[1] - dy)
    ANTINODES[type] = antinodes
    ANTINODES2[type] = antinodes2
    
print(f"Part 1: {len({a for antinodes in ANTINODES.values() for a in antinodes})}")
print(f"Part 2: {len({a for antinodes in ANTINODES2.values() for a in antinodes})}")