f = open('input.txt')
grid = [[int(i) for i in line if i.isnumeric()] for line in f.read().split('\n')]
row_len = len(grid)
column_len = len(grid[0])

visible = 0
scenic_scores = []
for row_idx, row in enumerate(grid):
    for column_idx, tree in enumerate(row):
        if row_idx == 0 or row_idx == row_len-1:
            visible += 1
        elif column_idx == 0 or column_idx == column_len-1:
            visible += 1
        else:
            # Part 1
            left = grid[row_idx][0:column_idx][::-1]
            right = grid[row_idx][column_idx + 1:column_len]
            top = [grid[j][column_idx] for j in range(0, row_idx)][::-1]
            bottom = [grid[j][column_idx] for j in range(row_idx + 1, row_len)]

            left_bol = all(tree > i for i in left)
            right_bol = all(tree > i for i in right)
            top_bol = all(tree > i for i in top)
            bottom_bol = all(tree > i for i in bottom)

            if any([left_bol, right_bol, top_bol, bottom_bol]):
                visible += 1

            # Part 2
            left_count, right_count, top_count, bottom_count = 0, 0, 0, 0
            for i in left:
                if tree > i:
                    left_count += 1
                else:
                    left_count += 1
                    break
            for i in right:
                if tree > i:
                    right_count += 1
                else:
                    right_count += 1
                    break
            for i in top:
                if tree > i:
                    top_count += 1
                else:
                    top_count += 1
                    break
            for i in bottom:
                if tree > i:
                    bottom_count += 1
                else:
                    bottom_count += 1
                    break
            scenic_score = left_count * right_count * bottom_count * top_count
            scenic_scores.append(scenic_score)

print(visible)
print(max(scenic_scores))
