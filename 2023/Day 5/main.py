
from tqdm import tqdm
class Function:

    def __init__(self, ranges: dict[range]):
        self.ranges = ranges

    def __call__(self, x):
        for r in self.ranges:
            if x in r:
                return x + self.ranges[r]
        else:
            return x

    def inv(self, y):
        for r in self.ranges:
            c = self.ranges[r]
            if y - c in r:
                return y - c
        else:
            return y

with open('input.txt') as f:
    lines = f.read().split('\n') + ['']
    seeds = [int(x) for x in lines[0].removeprefix('seeds: ').split()]
    mappings = {}
    curr = ()
    for n in range(2, len(lines)):
        line = lines[n]
        if '-' in line:
            curr = tuple(line.removesuffix(' map:').split('-to-'))
            mappings[curr] = {}
        elif line:
            DR, SR, RL = [int(x) for x in line.split()]
            mappings[curr][range(SR, SR + RL)] = DR - SR
        else:
            mappings[curr] = Function(mappings[curr])

mappings2 = {mapping[::-1]: mappings[mapping] for mapping in mappings}
def inverse(x):
    curr = 'location'
    while curr != 'seed':
        curr, f = [(mapping, mappings2[mapping]) for mapping in mappings2 if mapping[0] == curr][0]
        x = f.inv(x)
        curr = curr[1]
    return x

m = 0
def generator(seeds):
    global m
    while not any(inverse(m) in r for r in seeds):
        m += 1
        yield m

def get_min_location(seeds):
    if type(seeds[0]) is int:
        locations = seeds.copy()
        curr = 'seed'
        while curr != 'location':
            curr, f = [(mapping, mappings[mapping]) for mapping in mappings if mapping[0] == curr][0]
            locations = [f(x) for x in locations]
            curr = curr[1]
        return min(locations)
    else:
        for _ in tqdm(generator(seeds)): continue
        return m

print(f"Part 1: {get_min_location(seeds)}")
seeds_2 = [range(s, s + l) for s, l in zip([x for i, x in enumerate(seeds) if i % 2 == 0], [x for i, x in enumerate(seeds) if i % 2 == 1])]
print(f"Part 2: {get_min_location(seeds_2)}")
