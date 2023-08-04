
with open('input.txt') as f:
    grid = [list(x) for x in f.read().split()]
    temp_grid = [[x[i] for x in grid] for i in range(len(grid[0]))]

Start: tuple[int, int] = (0, 0)
End: tuple[int, int] = (0, 0)
Positions = {}
A = []
for row_idx, row in enumerate(grid):
    for column_idx, value in enumerate(row):
        if value == 'S':
            Start = (column_idx + 1, row_idx + 1)
        elif value == 'E':
            End = (column_idx + 1, row_idx + 1)
        if value == 'a':
            A.append((column_idx + 1, row_idx + 1))
        Positions[(column_idx + 1, row_idx + 1)] = value

values = ['S'] + sorted(set(v for v in Positions.values() if v.islower())) + ['E']

def get_adjacent_points(pt, val=''):
    x, y = pt
    adjacent_points = [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]
    adjacent_points = [point for point in adjacent_points if point in Positions]
    return [point for point in adjacent_points if Positions[point] == val] if val else adjacent_points

def contained(lst, val):
    return all(all(pt in lst or Positions[pt] != val for pt in get_adjacent_points(point)) for point in lst)

def get_group(pt):
    result = {pt}
    val = Positions[pt]
    while not contained(list(result), val):
        for point in result:
            result = result.union(set(get_adjacent_points(point, val)))
    return result

groups = {}
for pos in Positions:
    value = Positions[pos]
    if value not in groups:
        groups[value] = [sorted(get_group(pos))]
    else:
        if any(pos in group for group in groups[value]):
            continue
        else:
            groups[value].append(sorted(get_group(pos)))

for value in groups:
    for group in groups[value]:
        edges = [pt for pt in group if len(get_adjacent_points(pt)) > len(get_adjacent_points(pt, value))]
        surroundings = [pt for edge in edges for pt in get_adjacent_points(edge) if pt not in group]
        if value not in ('z', 'E') and not any(values.index(Positions[pt]) <= values.index(value) + 1 for pt in surroundings):
            [Positions.pop(pt) for pt in group]

def next_possible_points(point, start=Start):
    lst = []
    for pt in get_adjacent_points(point):
        if pt != start and values.index(Positions[pt]) - values.index(Positions[point]) <= 1:
            lst.append(pt)
    return lst

def find_shortest_path(start=Start):
    depth = 1
    possible_routes = [[start]]
    traversed = []
    while not any(route[-1] == End for route in possible_routes):
        for route in possible_routes.copy():
            for pos in next_possible_points(route[-1], start=start):
                if pos not in route and pos not in traversed:
                    possible_routes.append(route + [pos])
                    traversed.append(pos)
            possible_routes.remove(route)
        depth += 1
    return depth - 1

A = [find_shortest_path(start=a) for a in A if a in Positions]
print(f"Part 1: {find_shortest_path()}")
print(f"Part 2: {min(A)}")
