with open('input.txt', 'r') as f:
    lst = [i for i in f.read()]

def find_marker(length):
    for i in range(len(lst)):
        if len(set(lst[i: i + length])) == length:
            return i + length

print(f"Part 1: {find_marker(4)}")
print(f"Part 2: {find_marker(14)}")
