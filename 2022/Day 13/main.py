from copy import deepcopy
from ast import literal_eval

with open('input.txt', 'r') as f:
    lst = f.read().split()
    pairs = [(literal_eval(lst[2*i]), literal_eval(lst[2*i + 1])) for i in range(len(lst)//2)]  # Part 1
    packets = [literal_eval(packet) for packet in lst] + [[[2]], [[6]]]  # Part 2

def compare(left, right):
    if type(left) == list: left = deepcopy(left)
    if type(right) == list: right = deepcopy(right)
    if (type(left), type(right)) == (int, int):
        if left < right:
            return True, True
        elif left == right:
            return True, False
        elif left > right:
            return False, True
    elif (type(left), type(right)) == (int, list):
        return compare([left], right)
    elif (type(left), type(right)) == (list, int):
        return compare(left, [right])
    elif (type(left), type(right)) == (list, list):
        while left:
            try:
                l = left.pop(0)
            except IndexError:
                return True, True
            try:
                r = right.pop(0)
            except IndexError:
                return False, True
            res = compare(l, r)
            if res[1]:
                return res[0], True
        if len(left) < len(right):
            return True, True
        else:
            return False, False

indexes = []
for n, pair in enumerate(pairs, start=1):
    Left, Right = deepcopy(pair)
    result = compare(Left, Right)
    if result[0]:
        indexes.append(n)

ordered_packets = []
for packet in packets + [packets[0]]:
    if ordered_packets:
        i = 0
        while not compare(packet, ordered_packets[i])[0] and i < len(ordered_packets) - 1:
            i += 1
        ordered_packets.insert(i, packet)
    else:
        ordered_packets.append(packet)
ordered_packets.pop()

print(f'Part 1: {sum(indexes)}')
print(f'Part 2: {(ordered_packets.index([[2]]) + 1) * (ordered_packets.index([[6]]) + 1)}')
