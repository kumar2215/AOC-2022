
with open('input.txt') as f:
    nums = [int(num) for num in f.read().split('\n')]

p1 = 0
p2 = 0
MAGIC_NUMBER = 2020

for num1 in nums:
    for num2 in nums:
        if num1 != num2 and num1 + num2 == MAGIC_NUMBER:
            p1 = num1 * num2
        for num3 in nums:
            if len({num1, num2, num3}) == 3 and sum([num1, num2, num3]) == MAGIC_NUMBER:
                p2 = num1 * num2 * num3

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
