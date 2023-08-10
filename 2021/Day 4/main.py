with open('input.txt', 'r') as f:
    lst = f.read().split('\n')
    numbers_to_be_drawn = [int(i) for i in lst.pop(0).split(',')]
    lst.pop(0); lst.append('')

Grids = {}
temp = []
for x in lst:
    if x != '':
        temp.append(tuple(int(i) for i in x.split()))
    if x == '':
        Grids[tuple(temp.copy())] = [[0 for _ in range(5)] for _ in range(5)]
        temp.clear()

Grids_to_be_removed = []
for num in numbers_to_be_drawn:
    for grid in Grids:
        for i in range(5):
            if num in grid[i]:
                index = grid[i].index(num)
                Grids[grid][i][index] = 1
    for grid in Grids:
        for i in range(5):
            if all(Grids[grid][i]) or all([Grids[grid][j][i] for j in range(5)]):
                if not Grids_to_be_removed:
                    first_Grids = Grids.copy()
                    the_first_grid = grid
                    Num1 = num
                Grids_to_be_removed.append(grid)
                break
    for grid in Grids_to_be_removed:
        if grid in Grids:
            Grids.pop(grid)
        if len(Grids) == 1:
            final_Grids = Grids.copy()
    if len(Grids) == 0:
        the_last_grid = Grids_to_be_removed[-1]
        Num2 = num
        break

def main(grids, grid, num):
    unmarked_nums = []
    for i in range(5):
        for j in range(5):
            if grids[grid][i][j] == 0:
                unmarked_nums.append(grid[i][j])
    return sum(unmarked_nums) * num

print(f"Part 1: {main(first_Grids, the_first_grid, Num1)}")
print(f"Part 2: {main(final_Grids, the_last_grid, Num2)}")
