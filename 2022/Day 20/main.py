class Int:
    decryption_key = 811589153
    
    def __init__(self, value: str, part=1):
        self.value = [int(value), int(value) * self.decryption_key][part - 1]

with open('input.txt', 'r') as f:
    contents = f.read()
    lst = [Int(x, part=1) for x in contents.split('\n')]
    lst2 = [Int(x, part=2) for x in contents.split('\n')]

def mixing(ls: list, times):
    org_ls = ls.copy()
    for _ in range(times):
        for num in org_ls:
            if num.value == 0 or num.value % (len(ls) - 1) == 0:
                continue
            dct = {num: i for i, num in enumerate(ls)}
            idx = dct[num]
            new_idx = num.value + idx
            ls.pop(idx)
            if new_idx not in (0, len(ls)):
                ls.insert(new_idx % len(ls), num)
            elif new_idx == 0:
                ls.append(num)
            else:
                ls.insert(0, num)
    idx_0 = [i for i, num in enumerate(ls) if num.value == 0][0]
    result = ls[(1000 + idx_0) % len(ls)].value + ls[(2000 + idx_0) % len(ls)].value + ls[(3000 + idx_0) % len(ls)].value
    return result

print(f"Part 1: {mixing(lst, 1)}")
print(f"Part 2: {mixing(lst2, 10)}")
