from copy import deepcopy

with open('input.txt', 'r') as f:
    monkeys = [monkey.split(': ') for monkey in f.read().split('\n')]
    equations = [' = '.join(monkey) for monkey in monkeys if not monkey[1].isnumeric()]
    monkeys = {monkey[0]: monkey[1] for monkey in monkeys}
    operations = {}
    for monkey in monkeys:
        if monkeys[monkey].isnumeric():
            monkeys[monkey] = int(monkeys[monkey])
        else:
            operations[monkey] = monkeys[monkey][5]
            monkeys[monkey] = monkeys[monkey].split(monkeys[monkey][4:7])
    org_monkeys = deepcopy(monkeys)
    pointer = 'humn'
    pointers = [pointer]
    while pointer not in monkeys['root']:
        for monkey in monkeys:
            if type(monkeys[monkey]) == list and pointer in monkeys[monkey]:
                pointer = monkey
                pointers.append(pointer)
    determined_value = monkeys['root'][not monkeys['root'].index(pointer)]

def stop():
    bol = True
    for monkey in monkeys:
        if type(monkeys[monkey]) in (int, float):
            continue
        elif type(monkeys[monkey]) == list and all(type(m) in (int, float) for m in monkeys[monkey]):
            first, second = monkeys[monkey]
            monkeys[monkey] = eval(f"{first} {operations[monkey]} {second}")
        else:
            bol = False
    return bol

while not stop():
    for monkey in monkeys:
        if type(monkeys[monkey]) == list:
            for monkey2 in monkeys[monkey]:
                if type(monkey2) == str and type(monkeys[monkey2]) in (int, float):
                    monkeys[monkey][monkeys[monkey].index(monkey2)] = monkeys[monkey2]

monkeys2 = monkeys.copy()
monkeys2['root'] = True
determined_value = monkeys2[determined_value]

def get_value(equation: str, variable: str):
    operation = equation[12]
    result, var1, var2 = equation[0:4], equation[7:11], equation[14:18]
    assert variable in (var1, var2), ValueError
    if operation == '+':
        if variable == var1:
            return monkeys2[result] - monkeys2[var2]
        else:
            return monkeys2[result] - monkeys2[var1]
    elif operation == '-':
        if variable == var1:
            return monkeys2[result] + monkeys2[var2]
        else:
            return monkeys2[var1] - monkeys2[result]
    elif operation == '*':
        if variable == var1:
            return monkeys2[result] / monkeys2[var2]
        else:
            return monkeys2[result] / monkeys2[var1]
    elif operation == '/':
        if variable == var1:
            return monkeys2[result] * monkeys2[var2]
        else:
            return monkeys2[var1] / monkeys2[result]

while pointer != 'humn':
    if pointer != pointers[-1]:
        equation = [eq for eq in equations if eq.startswith(pointer)][0]
        determined_value = get_value(equation, pointers[-1])
    monkeys2[pointers[-1]] = determined_value
    pointer = pointers.pop()

print(f"Part 1: {int(monkeys['root'])}")
print(f"Part 2: {int(monkeys2['humn'])}")
