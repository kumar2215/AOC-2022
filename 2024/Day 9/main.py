
with open("input.txt") as f:
    data = list(f.read())
    
block = []
IDs = {}
LAST_ID = 0
for i, x in enumerate(data):
    if i % 2 == 0:
        block.extend([str(i//2)] * int(x)) 
        IDs[i//2] = int(x)
        LAST_ID = i//2
    else:
        block.extend(['.'] * int(x))

block2 = block.copy()
block_without_dots = [c for c in block if c != '.']
last = len(block)
for i, c in enumerate(block):
    if c == '.':
        block[i] = block_without_dots.pop()
        last -= 1
block = block[:last]

i = 0
spaces = {}
while i < len(block2):
    if block2[i] == '.':
        j = i
        while j + 1 < len(block2) and block2[j+1] == '.': 
            j += 1
        L = j - i + 1
        spaces[i] = L
        i = j
    i += 1
    
while LAST_ID > 0:
    L = IDs[LAST_ID]
    if dct := {k: v for k, v in spaces.items() if v >= L}:
        i = min(dct)
        idx = block2.index(str(LAST_ID))
        if i < idx:
            block2[i:i+L] = [str(LAST_ID)] * L
            block2[idx:idx+L] = ['.'] * L
            if L < spaces[i]:
                spaces[i+L] = spaces[i] - L
            del spaces[i]    
    LAST_ID -= 1

def checksum(block):
    return sum(int(c) * i for i, c in enumerate(block) if c != '.')


print(f"Part 1: {checksum(block)}")
print(f"Part 2: {checksum(block2)}")