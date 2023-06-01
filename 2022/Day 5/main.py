from copy import deepcopy

with open('input.txt', 'r') as f:
    lst = f.read().split('\n')

Break = lst.index('')
stacks = {int(i): [] for i in lst[Break - 1] if i.isnumeric()}
indexes = {num: lst[Break-1].index(str(num)) for num in stacks}

for i, x in enumerate(lst):
    if i < Break-1:
        while len(x) < len(lst[Break-1]):
            x += ' '
        for stack, index in indexes.items():
            if x[index] != ' ':
                stacks[stack].append(x[index])
    if i == Break:
        stacks1 = deepcopy(stacks)
        stacks2 = deepcopy(stacks)
    elif i > Break:
        value, start, end = [int(j) for j in x.split(' ') if j.isnumeric()]

        # Part 1
        for _ in range(value):
            char = stacks1[start][0]
            stacks1[start].pop(0)
            stacks1[end].insert(0, char)

        # Part 2
        char = []
        for _ in range(value):
            char.append(stacks2[start][0])
            stacks2[start].pop(0)
        stacks2[end] = (stacks2[end][::-1] + char[::-1])[::-1]

msg1 = ''
for stack in stacks1:
    msg1 += stacks1[stack][0]

msg2 = ''
for stack in stacks2:
    msg2 += stacks2[stack][0]

print(f'Part 1: {msg1}')
print(f'Part 1: {msg2}')
