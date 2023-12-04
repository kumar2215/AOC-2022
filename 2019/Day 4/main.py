
with open('input.txt') as f:
    start, end = [int(x) for x in f.read().split('-')]

possible_nums = []
for num in range(start, end + 1):
    lst = list(str(num))
    if any(int(lst[i]) == int(lst[i + 1]) for i in range(len(lst) - 1)) and all(int(lst[i]) <= int(lst[i + 1]) for i in range(len(lst) - 1)):
        possible_nums.append(num)

possible_nums_2 = list(filter(lambda x: any(2 * s in str(x) and 3 * s not in str(x) for s in str(x)), possible_nums))

print(f"Part 1: {len(possible_nums)}")
print(f"Part 2: {len(possible_nums_2)}")
