
from sympy import Interval
with open('input.txt') as f:
    times, distances = f.read().split('\n')
    times, distances = times.removeprefix('Time:').strip().split(), distances.removeprefix('Distance:').strip().split()
    race_2 = {int(''.join(t for t in times)): int(''.join(d for d in distances))}
    race = {t: d for t, d in zip([int(x) for x in times], [int(x) for x in distances])}

def solve_quadratic(a, b, c):
    return (-b + (b**2 - 4*a*c) ** 0.5) / (2*a), (-b - (b**2 - 4*a*c) ** 0.5) / (2*a)

def get_ways(Race):
    ways = 1
    for time in Race:
        s, e = solve_quadratic(-1, time, -Race[time])
        I = Interval(s, e, left_open=True, right_open=True)
        LB, UB = 0, 0
        for x in range(int(s), int(e) + 1):
            if x in I:
                LB = x
                break
        for x in range(int(s), int(e) + 1)[::-1]:
            if x in I:
                UB = x
                break
        ways *= UB - LB + 1
    return ways

print(f"Part 1: {get_ways(race)}")
print(f"Part 2: {get_ways(race_2)}")
