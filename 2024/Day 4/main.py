
with open("input.txt") as f:
    data = [list(line) for line in f.read().split("\n")]

grid = {}
ROWS = len(data)
COLS = len(data[0])
for y, row in enumerate(data):
    for x, cell in enumerate(row):
        grid[(x, y)] = cell

MAGIC_WORD = "XMAS"

def get_possible_words(pt):
    x, y = pt
    words = []
    
    # Horizontal
    if x + 4 <= COLS:
        words.append("".join(grid[(x+i, y)] for i in range(4)))
    if x - 3 >= 0:
        words.append("".join(grid[(x-i, y)] for i in range(4)))
    
    # Vertical
    if y + 4 <= ROWS:
        words.append("".join(grid[(x, y+i)] for i in range(4)))
    if y - 3 >= 0:
        words.append("".join(grid[(x, y-i)] for i in range(4)))
    
    # Diagonal
    if x + 4 <= COLS and y + 4 <= ROWS:
        words.append("".join(grid[(x+i, y+i)] for i in range(4)))
    if x - 3 >= 0 and y - 3 >= 0:
        words.append("".join(grid[(x-i, y-i)] for i in range(4)))
    
    # Reverse Diagonal
    if x + 4 <= COLS and y - 3 >= 0:
        words.append("".join(grid[(x+i, y-i)] for i in range(4)))
    if x - 3 >= 0 and y + 4 <= ROWS:
        words.append("".join(grid[(x-i, y+i)] for i in range(4)))
    
    return words

def is_X_MAX(pt):
    x, y = pt
    if grid[pt] != "A": return 0
    
    TOP_LEFT = grid.get((x - 1, y - 1), "")
    TOP_RIGHT = grid.get((x + 1, y - 1), "")
    BOTTOM_LEFT = grid.get((x - 1, y + 1), "")
    BOTTOM_RIGHT = grid.get((x + 1, y + 1), "")
    
    D1 = set([TOP_LEFT, BOTTOM_RIGHT])
    D2 = set([TOP_RIGHT, BOTTOM_LEFT])
    S = {"M", "S"}
    
    return D1 == S and D2 == S

count, count2 = 0, 0
for pt in grid:
    count += get_possible_words(pt).count(MAGIC_WORD)
    count2 += is_X_MAX(pt)

print(f"Part 1: {count}")
print(f"Part 2: {count2}")