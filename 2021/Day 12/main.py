
with open('input.txt', 'r') as f:
    connections = [x.split('-') for x in f.read().split('\n')]
    cave_system = {}
    for connection in connections:
        start, end = connection
        cave_system[start].append(end) if cave_system.get(start) else cave_system.setdefault(start, [end])
        cave_system[end].append(start) if cave_system.get(end) else cave_system.setdefault(end, [start])

routes = [['start']]
while not all(route[-1] == 'end' for route in routes):
    for route in routes.copy():
        if route[-1] != 'end':
            for next_cave in cave_system[route[-1]]:
                if next_cave != 'start' and (next_cave.isupper() or (next_cave.islower() and route.count(next_cave) == 0)):
                    routes.append(route + [next_cave])
            routes.remove(route)
print(f"Part 1: {len(routes)}")

routes2 = [['start']]
while not all(route[-1] == 'end' for route in routes2):
    for route in routes2.copy():
        if route[-1] != 'end':
            for next_cave in cave_system[route[-1]]:
                if next_cave != 'start' and (next_cave.isupper()
                    or (next_cave.islower() and all(route.count(cave) == 1 for cave in route if cave.islower()) and next_cave in route)
                    or (next_cave.islower() and route.count(next_cave) == 0)):
                    routes2.append(route + [next_cave])
            routes2.remove(route)
print(f"Part 2: {len(routes2)}")
