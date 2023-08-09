
with open('input.txt', 'r') as f:
    dct = {tuple(x.split(' | ')[0].split()): x.split(' | ')[1].split() for x in f.read().split('\n')}

nums = {2: 1, 3: 7, 4: 4, 7: 8}

count = 0
for line in dct.values():
    output_value = ''
    for output in line:
        if len(output) in nums:
            count += 1

def get_decoder(code):
    decoder = {nums[len(num)]: set(num) for num in code if len(num) in nums}
    decoder[9] = [set(num) for num in code if set(num).issuperset(decoder[4].union(decoder[7])) and len(num) == 6][0]
    BL = tuple(decoder[8].difference(decoder[9]))[0]
    decoder[0] = [set(num) for num in code if not set(num).issuperset(decoder[4].difference(decoder[1])) and len(num) == 6][0]
    decoder[5] = [set(num) for num in code if set(num).issuperset(decoder[4].difference(decoder[1])) and len(num) == 5][0]
    decoder[6] = decoder[5].union(set(BL))
    decoder[2] = [set(num) for num in code if BL in set(num) and len(num) == 5][0]
    decoder[3] = [set(num) for num in code if set(num) not in decoder.values()][0]
    return decoder

total = 0
for code, line in dct.items():
    decoder = get_decoder(code)
    output_value = ''
    for output in line:
        num = [n for n in decoder if set(output) == decoder[n]][0]
        output_value += str(num)
    total += int(output_value)

print(f"Part 1: {count}")
print(f"Part 2: {total}")
