f = open('input.txt')
instructions = [line.split() for line in f.read().split('\n')]

def obtain_head_pos(head_pos: list[tuple]):
    for instruction in instructions:
        direction, steps = instruction[0], int(instruction[1])
        for i in range(steps):
            curr_head_pos = list(head_pos[0])
            if direction == 'R':
                curr_head_pos[0] += 1
            elif direction == 'L':
                curr_head_pos[0] -= 1
            elif direction == 'U':
                curr_head_pos[1] += 1
            elif direction == 'D':
                curr_head_pos[1] -= 1
            head_pos.insert(0, tuple(curr_head_pos))
    head_pos.reverse()
    return head_pos

def obtain_tail_pos(head_pos: list[tuple]):
    tail_pos = [(0, 0)]
    for curr_head_pos in head_pos:
        curr_tail_pos = list(tail_pos[0])
        dx = curr_head_pos[0] - curr_tail_pos[0]
        dy = curr_head_pos[1] - curr_tail_pos[1]
        if abs(dx) == 2 and dy == 0:
            if dx == 2:
                curr_tail_pos[0] += 1
            elif dx == -2:
                curr_tail_pos[0] -= 1
        elif abs(dy) == 2 and dx == 0:
            if dy == 2:
                curr_tail_pos[1] += 1
            elif dy == -2:
                curr_tail_pos[1] -= 1
        elif (dx == 1 and dy == 2) or (dy == 1 and dx == 2) or (dx == 2 and dy == 2):
            curr_tail_pos = [curr_tail_pos[0] + 1, curr_tail_pos[1] + 1]
        elif (dx == 1 and dy == -2) or (dy == -1 and dx == 2) or (dx == 2 and dy == -2):
            curr_tail_pos = [curr_tail_pos[0] + 1, curr_tail_pos[1] - 1]
        elif (dx == -1 and dy == 2) or (dy == 1 and dx == -2) or (dx == -2 and dy == 2):
            curr_tail_pos = [curr_tail_pos[0] - 1, curr_tail_pos[1] + 1]
        elif (dx == -1 and dy == -2) or (dy == -1 and dx == -2) or (dx == -2 and dy == -2):
            curr_tail_pos = [curr_tail_pos[0] - 1, curr_tail_pos[1] - 1]
        if tuple(curr_tail_pos) != tail_pos[0]:
            tail_pos.insert(0, tuple(curr_tail_pos))
    tail_pos.reverse()
    return tail_pos

# Part 1
head_pos = obtain_head_pos([(0, 0)])
for i in range(1):
    head_pos = obtain_tail_pos(head_pos)
print(len(set(head_pos)))

# Part 2
head_pos = obtain_head_pos([(0, 0)])
for i in range(9):
    head_pos = obtain_tail_pos(head_pos)
print(len(set(head_pos)))
