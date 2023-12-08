
from math import lcm
with open('input.txt', 'r') as f:
    lines = f.read().split('\n')
    directions = list(lines[0])
    nodes = {}
    for line in lines[2:]:
        node, next_nodes = line.split(' = ')
        nodes[node] = next_nodes[1:-1].split(', ')

dir_pointer = 0
pos_pointer = 'AAA'
n = len(directions)
steps = 0
while pos_pointer != 'ZZZ':
    direction = {'L': 0, 'R': 1}[directions[dir_pointer % n]]
    next_node = nodes[pos_pointer][direction]
    pos_pointer = next_node
    dir_pointer += 1
    steps += 1
print(f"Part 1: {steps}")

dir_pointer = 0
pos_pointers = [node for node in nodes if node[-1] == 'A']
steps_2 = []
for p in pos_pointers:
    temp_steps = 0
    while p[-1] != 'Z':
        direction = {'L': 0, 'R': 1}[directions[dir_pointer % n]]
        next_node = nodes[p][direction]
        p = next_node
        dir_pointer += 1
        temp_steps += 1
    steps_2.append(temp_steps)
print(f"Part 2: {lcm(*steps_2)}")
