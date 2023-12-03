
with open('input.txt') as f:
    MEMORY = [int(x) for x in f.read().split(',')]

def run(noun, verb):
    memory = MEMORY.copy()
    memory[1] = noun
    memory[2] = verb
    pointer = 0
    while memory[pointer] != 99:
        num1 = memory[memory[pointer + 1]]
        num2 = memory[memory[pointer + 2]]
        idx = memory[pointer + 3]
        if memory[pointer] == 1:
            memory[idx] = num1 + num2
        elif memory[pointer] == 2:
            memory[idx] = num1 * num2
        pointer += 4
    return memory[0]

MAGIC_NUMBER = 19690720
inputs = (0, 0)
for n in range(100):
    for v in range(100):
        if run(n, v) == MAGIC_NUMBER:
            inputs = (n, v)
            break

print(f"Part 1: {run(12, 2)}")
print(f"Part 2: {100 * inputs[0] + inputs[1]}")
