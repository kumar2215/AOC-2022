f = open('input.txt')
lst = [x.split(',') for x in f.read().split('\n')]

count1 = 0
count2 = 0
for x in lst:
    a1, a2 = [int(i) for i in x[0].split('-')]
    b1, b2 = [int(i) for i in x[1].split('-')]
    a = set(range(a1, a2 + 1))
    b = set(range(b1, b2 + 1))
    
    # Part 1
    if a.union(b) == a or a.union(b) == b:
        count1 += 1
    
    # Part 2
    if a.intersection(b):
        count2 += 1

print(count1, count2)
