
from tqdm import tqdm
with open('input.txt') as f:
    lines = f.read().split('\n')
    springs = []
    for line in lines:
        spring, perm = line.split(' ')
        springs.append((spring, tuple(int(x) for x in perm.split(','))))

def solve(s: str, perm: tuple):
    pointers = tuple(0 for _ in perm)
    poss = {n: [] for n in range(len(perm))}
    for i, pointer in enumerate(pointers):
        last = len(s) - (sum(perm[i:]) + len(perm[i+1:])) if i < len(perm) - 1 else len(s) - perm[i]
        while pointer <= last:
            if set(s[pointer:pointer+perm[i]]).issubset({'?', '#'}):
                if (((i == 0 and '#' not in s[0:pointer]) or (0 < i < len(perm) - 1)) and ((pointer == 0) or (pointer > 0 and s[pointer - 1] != '#')) and s[pointer + perm[i]] != '#') or (i == len(perm) - 1 and (pointer+perm[i] == len(s) + 1 or '#' not in s[pointer+perm[i]:])):
                    poss[i].append(pointer)
            pointer += 1
    perms = {x: 1 for x in poss[0]}
    for n in range(len(poss) - 1):
        new_perms = {}
        for ele in perms:
            for x in poss[n + 1]:
                if x > ele + perm[n] and '#' not in s[ele + perm[n]: x]:
                    if x in new_perms:
                        new_perms[x] += perms[ele]
                    else:
                        new_perms[x] = perms[ele]
        perms = new_perms
    count = sum(perms.values())
    del perms
    return count

total, total_2 = 0, 0
for spring, perm in tqdm(springs):
    total += solve(spring, perm)
    total_2 += solve('?'.join([spring] * 5), perm * 5)
print(f"Part 1: {total}")
print(f"Part 2: {total_2}")
