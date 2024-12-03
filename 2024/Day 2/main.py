with open('input.txt') as f:
    grid = [[int(x) for x in line.split()] for line in f.read().split('\n')]

def is_safe(row):
    increasing = (row[-1] - row[0]) > 0
    decreasing = (row[-1] - row[0]) < 0
    if not increasing and not decreasing: return False
    if increasing:
        for i in range(len(row) - 1):
            if row[i] >= row[i + 1] or not (1 <= row[i+1] - row[i] <= 3):
                return False
    elif decreasing:
        for i in range(len(row) - 1):
            if row[i] <= row[i + 1] or not (1 <= row[i] - row[i+1] <= 3):
                return False
    return True

def is_safe2(row):
    poss = [row.copy() for _ in range(len(row))]
    for i in range(len(row)):
        del poss[i][i]
    return any(is_safe(p) for p in poss)
            
print(f"Part 1: {len(list(filter(is_safe, grid)))}")
print(f"Part 2: {len(list(filter(is_safe2, grid)))}")