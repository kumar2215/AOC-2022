
with open('input.txt') as f:
    data = [[part for part in line.split() if '=' in part] for line in f.read().splitlines()]
    step_count = {}
    for n, line in enumerate(data):
        for index, statement in enumerate(line):
            statement = statement.removeprefix('x=')
            statement = statement.removeprefix('y=')
            statement = statement.replace(',', '')
            statement = statement.replace(':', '')
            line[index] = int(statement)
        x1, y1, x2, y2 = line
        step_count[(x1, y1)] = abs(x2 - x1) + abs(y2 - y1)
        data[n] = [(x1, y1), (x2, y2)]

sensors = [line[0] for line in data]
beacons = [line[1] for line in data]

Y, points = 2_000_000, set() # Part 1
limit, distress_beacon = 4_000_000, [] # Part 2

def checker(pt, sensor):
    lst = sensors.copy()
    lst.remove(sensor)
    return all((abs(pt[0] - sensor[0]) + abs(pt[1] - sensor[1]) > step_count[sensor]) for sensor in lst)

for line in data:
    sensor, beacon = line
    steps = step_count[sensor]

    # Part 1
    x, y = sensor
    dy = abs(Y - y)
    dx = steps - dy
    if dx >= 0:
        for step in range(-dx, dx + 1):
            if (x + step, Y) not in beacons + sensors:
                points.add((x + step, Y))

    # Part 2
    step = steps + 1
    for i in range(-step, step + 1):
        if i < 0:
            pt = (sensor[0] + i, sensor[1] + i + step)
            distress_beacon.append(pt) if all(0 <= r <= limit for r in pt) and checker(pt, sensor) else None
            pt = (sensor[0] + i, sensor[1] - i - step)
            distress_beacon.append(pt) if all(0 <= r <= limit for r in pt) and checker(pt, sensor) else None
        else:
            pt = (sensor[0] + i, sensor[1] + i - step)
            distress_beacon.append(pt) if all(0 <= r <= limit for r in pt) and checker(pt, sensor) else None
            pt = (sensor[0] + i, sensor[1] - i + step)
            distress_beacon.append(pt) if all(0 <= r <= limit for r in pt) and checker(pt, sensor) else None

print(f'Part 1: {len(points)}')
print(f'Part 2: {distress_beacon[0][0] * 4_000_000 + distress_beacon[0][1]}')
