
with open('input.txt', 'r') as f:
    lines = f.read().split('\n')

games = {}
for line in lines:
    ID, subsets = line.split(':')
    ID = int(ID.removeprefix('Game '))
    games[ID] = [s.split(',') for s in subsets.split(';')]

for game in games:
    lst = []
    for subset in games[game]:
        dct = {}
        for cubes in subset:
            cubes = cubes.strip()
            num, color = cubes.split(' ')
            dct[color] = int(num)
        lst.append(dct)
    games[game] = lst

max_red, max_green, max_blue = 12, 13, 14
possible_games = []
powers = []

for game in games:
    possible = True
    for subset in games[game]:
        if subset.get('red', 0) > max_red or subset.get('green', 0) > max_green or subset.get('blue', 0) > max_blue:
            possible = False
            break
    if possible:
        possible_games.append(game)
    R = max([subset.get('red', 0) for subset in games[game]])
    G = max([subset.get('green', 0) for subset in games[game]])
    B = max([subset.get('blue', 0) for subset in games[game]])
    powers.append(R * G * B)

print(f"Part 1: {sum(possible_games)}")
print(f"Part 2: {sum(powers)}")
