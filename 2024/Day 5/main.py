with open("input.txt") as f:
    rules, updates = f.read().split("\n\n")
    rules = [rule.split("|") for rule in rules.split("\n")]
    updates = [tuple(int(x) for x in update.split(",")) for update in updates.split("\n")]
    RULES = {}
    for rule in rules:
        F, S = rule
        if int(F) not in RULES:
            RULES[int(F)] = []
        RULES[int(F)].append(int(S))

def is_correct(update):
    n = len(update)
    try:
        for i in range(n):
            right = update[i+1:]
            for j, x in enumerate(right):
                if x not in RULES[update[i]]:
                    new_update = list(update)
                    new_update[i], new_update[i+j+1] = new_update[i+j+1], new_update[i]
                    return False, tuple(new_update)
        return True, update
    except KeyError:
        invalid_key = update[i]
        values = [x for x in RULES if invalid_key in RULES[x]]
        indexes = [i for i, x in enumerate(update) if x in values]
        M = max(indexes)
        new_update = list(update)
        del new_update[i]
        new_update.insert(M, invalid_key)
        return False, tuple(new_update)

total, total2 = 0, 0
for update in updates:
    n = len(update)
    correct, update = is_correct(update)
    if correct:
        total += update[n//2]
    else:
        while not correct:
            correct, update = is_correct(update)
        total2 += update[n//2]

print(f"Part 1: {total}")
print(f"Part 2: {total2}")