
from scanf import scanf
from itertools import combinations
from sympy import solve, symbols, Eq
with open("input.txt") as f:
    hailstones = [scanf("%d, %d, %d @ %d, %d, %d", line) for line in f.read().split('\n')]

LB, UB = 200000000000000, 400000000000000
count = 0
for h1, h2 in combinations(hailstones, 2):
    x1, y1, z1, dx1, dy1, dz1 = h1
    x2, y2, z2, dx2, dy2, dz2 = h2
    t2 = (dx1 * dy1 / (dy2 * dx1 - dx2 * dy1)) * ((x2 - x1) / dx1 - (y2 - y1) / dy1) if (dy2 * dx1 - dx2 * dy1) else None
    if t2 is None:
        continue
    t1 = (y2 - y1) / dy1 + (dy2 / dy1) * t2
    X1, Y1 = x1 + dx1 * t1, y1 + dy1 * t1
    if t1 > 0 and t2 > 0:
        if LB <= X1 <= UB and LB <= Y1 <= UB:
            count += 1
print(f"Part 1: {count}")

a, b, c, a0, b0, c0 = symbols('a,b,c,a0,b0,c0')
sol, eqns = {}, []
for hailstone in hailstones:
    x, y, z, dx, dy, dz = hailstone
    n1, d1 = x - a0, a - dx
    n2, d2 = y - b0, b - dy
    n3, d3 = z - c0, c - dz
    eqns.extend([
        Eq(n1 * d2, n2 * d1),
        Eq(n1 * d3, n3 * d1),
        Eq(n2 * d3, n3 * d2)
    ])
    try:
        sol = solve(eqns)
    except NotImplementedError:
        continue
    sol = sol if type(sol) is dict else sol[0]
    try:
        sol = {s: int(val) for s, val in sol.items()}
        break
    except TypeError:
        continue
print(f"Part 2: {sum([sol[a0], sol[b0], sol[c0]])}")
