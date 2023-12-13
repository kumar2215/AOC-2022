
with open("input.txt") as f:
    grids = f.read().split('\n\n')

class Grid:

    def __init__(self, grid: str):
        self.grid = grid
        self.rows = grid.split('\n')
        self.columns = [[r[i] for r in self.rows] for i in range(len(self.rows[0]))]
        self.vertical_reflections = []
        self.horizontal_reflections = []
        for c, col in enumerate(self.columns):
            lhs = self.columns[:c+1][::-1]
            rhs = self.columns[c+1:]
            if lhs and rhs and all(l == r for l, r in zip(lhs, rhs)):
                self.vertical_reflections.append(c+1)
        for r, row in enumerate(self.rows):
            top = self.rows[:r+1][::-1]
            bottom = self.rows[r+1:]
            if top and bottom and all(t == b for t, b in zip(top, bottom)):
                self.horizontal_reflections.append(r+1)
        self.alternate_vr = []
        self.alternate_hr = []

    def alternate(self):
        dct = {'.': '#', '#': '.'}
        for r, row in enumerate(self.rows):
            for i, char in enumerate(row):
                temp = list(row)
                temp[i] = dct[char]
                temp = [''.join(temp)]
                new_grid = '\n'.join(self.rows[:r] + temp + self.rows[r + 1:])
                new_grid = Grid(new_grid)
                hr = [r for r in new_grid.horizontal_reflections if r not in self.horizontal_reflections]
                vr = [r for r in new_grid.vertical_reflections if r not in self.vertical_reflections]
                if hr:
                    self.alternate_hr = hr
                elif vr:
                    self.alternate_vr = vr
                if bool(self.alternate_hr) ^ bool(self.alternate_vr):
                    break

grids = [Grid(grid) for grid in grids]
row_sum, col_sum = 0, 0
row_sum2, col_sum2 = 0, 0
for grid in grids:
    row_sum += sum(grid.horizontal_reflections)
    col_sum += sum(grid.vertical_reflections)
    grid.alternate()
    row_sum2 += sum(grid.alternate_hr)
    col_sum2 += sum(grid.alternate_vr)

print(f"Part 1: {100 * row_sum + col_sum}")
print(f"Part 2: {100 * row_sum2 + col_sum2}")
