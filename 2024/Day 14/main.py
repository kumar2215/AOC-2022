from scanf import scanf
with open("input.txt") as f:
    robots = [scanf("p=%d,%d v=%d,%d", line) for line in f.read().split("\n")]

ROWS, COLS = None, None
class Robot:
    
    def __init__(self, px, py, vx, vy):
        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy
    
    def simulate(self):
        self.px = (self.px + self.vx) % COLS
        self.py = (self.py + self.vy) % ROWS
        
        
robots = [Robot(*robot) for robot in robots]
ROWS = max(robot.py for robot in robots) + 1
COLS = max(robot.px for robot in robots) + 1

def print_grid():
    for y in range(ROWS):
        for x in range(COLS):
            v = sum(robot.py == y and robot.px == x for robot in robots)
            print(v if v > 0 else ".", end="")
        print()

def simulate(n):
    for _ in range(n):
        for robot in robots:
            robot.simulate()

def get_safety_factor():
    MIDDLE_ROW = ROWS // 2
    MIDDLE_COL = COLS // 2
    dct = {1: 0, 2: 0, 3: 0, 4: 0}
    for robot in robots:
        if robot.py < MIDDLE_ROW and robot.px < MIDDLE_COL:
            dct[1] += 1
        elif robot.py < MIDDLE_ROW and robot.px > MIDDLE_COL:
            dct[2] += 1
        elif robot.py > MIDDLE_ROW and robot.px < MIDDLE_COL:
            dct[3] += 1
        elif robot.py > MIDDLE_ROW and robot.px > MIDDLE_COL:
            dct[4] += 1
    return dct[1] * dct[2] * dct[3] * dct[4]

def is_chrismas_tree():
    grid = [["." for _ in range(COLS)] for _ in range(ROWS)]
    MIDDLE_COL = COLS // 2
    for y in range(ROWS):
        for x in range(COLS):
            v = sum(robot.py == y and robot.px == x for robot in robots)
            if v > 1: return False
    return True

i = 0
while not is_chrismas_tree():
    simulate(1)
    i += 1
    if i == 100: print(f"Part 1: {get_safety_factor()}")
    
print(f"Part 2: {i}")