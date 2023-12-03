
with open('input.txt') as f:
    db = [line.split(': ') for line in f.read().split('\n')]

count = 0
count2 = 0
for entry in db:
    policy, password = entry
    R, char = policy.split(' ')
    start, end = [int(x) for x in R.split('-')]
    if list(password).count(char) in range(start, end + 1):
        count += 1
    if (password[start - 1] is char) ^ (password[end - 1] is char):
        count2 += 1

print(f"Part 1: {count}")
print(f"Part 2: {count2}")
