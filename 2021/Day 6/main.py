with open('input.txt', 'r') as f:
    lst = [int(x) for x in f.read().split(',')]
    Dct = {x: lst.count(x) if x in lst else 0 for x in range(9)}

def iterate(n, dct):
    for _ in range(n):
        counter = dct.copy()
        counter[0] = dct[1]
        counter[1] = dct[2]
        counter[2] = dct[3]
        counter[3] = dct[4]
        counter[4] = dct[5]
        counter[5] = dct[6]
        counter[6] = dct[0] + dct[7]
        counter[7] = dct[8]
        counter[8] = dct[0]
        dct = counter
    return sum(dct.values())

print(f"Part 1: {iterate(80, Dct.copy())}")
print(f"Part 2: {iterate(256, Dct.copy())}")
