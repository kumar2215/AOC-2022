import re

with open("input.txt", "r") as f:
    data = f.read()
    
expressions = re.findall(r"mul\(\d+,\d+\)", data)
result = [expression[4:-1].split(",") for expression in expressions]
result = sum(int(a) * int(b) for a, b in result)

dos = []
data_copy = data
L = 0
while (idx := data_copy.find("do()")) != -1:
    dos.append(idx+L)
    data_copy = data_copy[idx+4:]
    L = dos[-1] + 4
    
donts = []
data_copy = data
L = 0
while (idx := data_copy.find("don't()")) != -1:
    donts.append(idx+L)
    data_copy = data_copy[idx+7:]
    L = donts[-1] + 7

def enable_mul(n):
    dos_tmp = [do for do in dos if do < n]
    donts_tmp = [dont for dont in donts if dont < n]
    if dos_tmp and donts_tmp:
        return dos_tmp[-1] > donts_tmp[-1]
    elif not donts_tmp:
        return True
    return False

expressions2 = [expr for expr in expressions if enable_mul(data.find(expr))]
result2 = [expression[4:-1].split(",") for expression in expressions2]
result2 = sum(int(a) * int(b) for a, b in result2)

print(f"Part 1: {result}")
print(f"Part 2: {result2}")