
with open('input.txt') as f:
    times, distances = f.read().split('\n')
    times, distances = times.removeprefix('Time:').strip().split(), distances.removeprefix('Distance:').strip().split()
    race_2 = {int(''.join(t for t in times)): int(''.join(d for d in distances))}
    times, distances = [int(x) for x in times], [int(x) for x in distances]
    race = {t: d for t, d in zip(times, distances)}

def solve_quadratic(a, b, c):
    return (-b + (b**2 - 4*a*c) ** 0.5) / (2*a), (-b - (b**2 - 4*a*c) ** 0.5) / (2*a)

def get_ways(Race):
    ways = 1
    for time in Race:
        s, e = solve_quadratic(-1, time, -Race[time])
        ways *= int(e) - int(s)
    return ways

print(f"Part 1: {get_ways(race)}")
print(f"Part 2: {get_ways(race_2)}")
