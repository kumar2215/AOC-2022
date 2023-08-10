
with open('input.txt', 'r') as f:
    lst = [x.split() for x in f.read().split('\n')]

def main(part):
    depth = 0
    x_pos = 0
    aim = 0
    for x in lst:
        instruction = x[0]
        value = int(x[1])
        if part == 1:
            if instruction == 'forward':
                x_pos += value
            elif instruction == 'down':
                depth += value
            elif instruction == 'up':
                depth -= value
        else:
            if instruction == 'forward':
                x_pos += value
                depth += aim * value
            elif instruction == 'down':
                aim += value
            elif instruction == 'up':
                aim -= value
    return x_pos * depth

print(f"Part 1: {main(1)}")
print(f"Part 2: {main(2)}")
