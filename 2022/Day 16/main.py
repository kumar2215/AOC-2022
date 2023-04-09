from itertools import permutations
with open('input.txt') as f:
    valves = {}
    valve_connections = {}
    for line in f.read().splitlines():
        first, second = line.split('; ')
        name, rate = [part for part in first.split() if part.isupper() or '=' in part]
        valves[name] = int(rate.removeprefix('rate='))
        valve_connections[name] = [part.removesuffix(',') for part in second.split() if part.isupper()]

useful_valves = sorted([valve for valve in valves if valves[valve]], key=lambda valve: -valves[valve])
grouped_perms = list(permutations(useful_valves, len(useful_valves) // 3))

def get_travel_time(target, start='AA', count=0):
    if target == start: return 0
    if target in valve_connections[start]: return count + 1
    else:
        traversed = set()
        while target not in traversed:
            count += 1
            traversed = traversed.union(valve_connections[start])
            for valve in traversed.copy():
                traversed = traversed.union(set(v for v in valve_connections[valve] if v is not start))
        return count + 1

travel_times = {valve: {v: get_travel_time(v, start=valve) for v in useful_valves if v != valve} for valve in ['AA'] + useful_valves}

def create(limit=30):
    perms = {}
    for perm in grouped_perms:
        time_remaining = limit
        temp = []
        for valve in perm:
            time_remaining -= travel_times[temp[-1] if temp else 'AA'][valve] + 1
            if time_remaining >= 0:
                temp.append(valve)
            else:
                perms[tuple(temp)] = time_remaining + travel_times[temp[-1] if temp else 'AA'][valve] + 1
                break
        else:
            perms[tuple(temp)] = time_remaining
    return perms

perms1 = create()
lengths = [len(perms1)]

def adjust(perms=perms1):
    removable = []
    for perm in perms.copy():
        next_valves = [valve for valve in travel_times[perm[-1]] if travel_times[perm[-1]][valve] + 1 <= perms[perm] and valve not in perm]
        for valve in next_valves:
            temp = list(perm)
            temp.append(valve)
            if tuple(temp) not in perms:
                perms[tuple(temp)] = perms[perm] - travel_times[perm[-1]][valve] - 1
            removable.append(perm)
    [perms.pop(perm) for perm in removable if perm in perms]

adjust()
lengths.append(len(perms1))

while lengths[-2] != lengths[-1]:
    adjust()
    lengths.append(len(perms1))

def perform_round(permutation, limit=30):
    valves_opened = []
    time = 0
    pressure_released = 0
    total_pressure = 0
    for i in range(len(permutation)):
        valve = permutation[i]
        valves_opened.append(valve)
        time += travel_times[permutation[i - 1] if time else 'AA'][valve] + 1
        if time <= limit:
            total_pressure += valves[valve]
            pressure_released += valves[valve] * (limit - time)
        else:
            valves_opened.remove(valve)
    return pressure_released

Perms = {}
for perm in perms1:
    Perms[perform_round(perm)] = tuple(perm)

perms2 = create(limit=26)
lengths2 = [len(perms2)]
adjust(perms=perms2)
lengths2.append(len(perms2))

while lengths2[-2] != lengths2[-1]:
    adjust(perms=perms2)
    lengths2.append(len(perms2))

permlengths = {len(perm): {} for perm in perms2 if len(perm) > len(useful_valves) // 3}

for perm in perms2:
    if len(perm) > len(useful_valves) // 3:
        permlengths[len(perm)][perm] = perform_round(perm, limit=26)

pairs = {}
for l1 in permlengths:
    for l2 in permlengths:
        if (l1, l2) not in pairs and (l2, l1) not in pairs:
            pairs[(l1, l2)] = {}
            for p1 in permlengths[l1]:
                for p2 in permlengths[l2]:
                    if p1 != p2:
                        pair1 = (p1, tuple(v for v in p2 if v not in p1))
                        pair2 = (tuple(v for v in p1 if v not in p2), p2)
                        pairs[(l1, l2)][perform_round(pair1[0], limit=26) + perform_round(pair1[1], limit=26)] = pair1
                        pairs[(l1, l2)][perform_round(pair2[0], limit=26) + perform_round(pair2[1], limit=26)] = pair2

print(f'Part 1: {max(Perms)}')
print(f'Part 2: {max({max(pairs[pair]): pair for pair in pairs})}')
