
with open('input.txt', 'r') as f:
    lst = f.read().split('\n')

count = 0
for i in range(1, len(lst)):
    if int(lst[i]) > int(lst[i-1]):
        count += 1

count2 = 0
for i in range(1, len(lst)-2):
    arr1 = [int(k) for k in lst[i-1:i+2]]
    arr2 = [int(k) for k in lst[i:i+3]]
    if sum(arr2) > sum(arr1):
        count2 += 1

print(f"Part 1: {count}")
print(f"Part 2: {count2}")
