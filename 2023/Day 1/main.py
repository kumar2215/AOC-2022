
with open('input.txt', 'r') as f:
    lines = f.read().split('\n')

lines1 = [''.join(char for char in line if char.isnumeric()) for line in lines]
nums1 = [int(s[0] + s[-1]) for s in lines1 if s]

dct = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}

lines2 = {line: ({}, {}) for line in lines}
for word in dct:
    for line in lines2:
        if line.find(word) != -1:
            lines2[line][0][line.find(word)] = word
            lines2[line][1][line[::-1].find(word[::-1])] = word

nums2 = []
for line in lines2:
    indexes_0, indexes_1 = lines2[line]
    first = dct[indexes_0[min(indexes_0)]]
    last = dct[indexes_1[min(indexes_1)]]
    nums2.append(int(first + last))

print(f"Part 1: {sum(nums1)}")
print(f"Part 2: {sum(nums2)}")
