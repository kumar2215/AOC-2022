
from multiprocessing import Process, Value
with open("input.txt") as f:
    data = [list(line) for line in f.read().split("\n")]

grid, guard_pos = {}, None
obstacles, possible_spots = [], []
for y, row in enumerate(data):
    for x, cell in enumerate(row):
        grid[(x, y)] = cell
        if cell in ("^", "v", "<", ">"): guard_pos = ((x, y), cell)
        elif cell == "#": obstacles.append((x, y))
        else: possible_spots.append((x, y))

def get_next_pos(pt, direction):
    x, y = pt
    if direction == "^": return (x, y - 1)
    if direction == "v": return (x, y + 1)
    if direction == "<": return (x - 1, y)
    if direction == ">": return (x + 1, y)

def get_new_direction(direction):
    if direction == "^": return ">"
    if direction == "v": return "<"
    if direction == "<": return "^"
    if direction == ">": return "v"

def simulate(guard_pos, obstacles):
    path = {guard_pos[0]}
    duplicates = 0
    while (next_pos := get_next_pos(*guard_pos)) in grid and duplicates < len(path):
        if next_pos in obstacles:
            new_direction = get_new_direction(guard_pos[1])
            next_pos = get_next_pos(guard_pos[0], new_direction)
            while next_pos in obstacles:
                new_direction = get_new_direction(new_direction)
                next_pos = get_next_pos(guard_pos[0], new_direction)
            guard_pos = (next_pos, new_direction)
        else:
            guard_pos = (next_pos, guard_pos[1])
        if guard_pos[0] in path: duplicates += 1
        else: 
            path.add(guard_pos[0])
            duplicates -= 1
    if duplicates >= len(path): return -1
    return len(path)

print(f"Part 1: {simulate(guard_pos, obstacles)}")

N = len(possible_spots)
N_per_process = N // 15
lsts = [possible_spots[i:i + N_per_process] for i in range(0, N, N_per_process)]
count = Value('i', 0)

def worker(lst, obstacles):
    for spot in lst:
        obstacles_copy = obstacles.copy()
        obstacles_copy.append(spot)
        if simulate(guard_pos, obstacles_copy) == -1: count.value += 1

processes = []
for i, lst in enumerate(lsts, 1):
    p = Process(target=worker, args=(lst, obstacles))
    p.start()
    processes.append(p)
    
for p in processes:
    p.join()
    
print(f"Part 2: {count.value}")