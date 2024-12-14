from scanf import scanf
from sympy.matrices import Matrix

with open("input.txt") as f:
    claw_machines = [macjine.split("\n") for macjine in f.read().split("\n\n")]
    
class ClawMachine:
    
    def __init__(self, machine):
        buttonA, buttonB, prize = machine
        buttonA = scanf("Button A: X+%d, Y+%d", buttonA)
        buttonB = scanf("Button B: X+%d, Y+%d", buttonB)
        prize = scanf("Prize: X=%d, Y=%d", prize)
        
        self.buttons = Matrix([buttonA, buttonB]).transpose()
        self.prize = Matrix(prize)
        self.prize2 = Matrix([10000000000000 + prize[0], 10000000000000 + prize[1]])
        
    def solve(self):
        a, b = self.buttons.inv() * self.prize
        if int(a) == a and int(b) == b and a <= 100 and b <= 100: return 3*a + b
        else: return 0
        
    def solve2(self):
        a, b = self.buttons.inv() * self.prize2
        if int(a) == a and int(b) == b: return 3*a + b
        else: return 0
        
total, total2 = 0, 0
for machine in claw_machines:
    total += ClawMachine(machine).solve()
    total2 += ClawMachine(machine).solve2()
    
print(f"Part 1: {total}")
print(f"Part 2: {total2}")