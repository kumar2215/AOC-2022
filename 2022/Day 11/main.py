from scanf import scanf

class Monkey:

    def __init__(self, index: int, starting_items: list[int], operation, divisor: int, test: dict):
        self.index = index
        self.starting_items = starting_items
        self.operation = operation
        self.divisor = divisor
        self.test = [lambda x: x % divisor == 0, test]
        self.inspection_count = 0

monkeys1 = []
monkeys2 = []
M = 1

with open('input.txt') as f:
    lines = f.read().splitlines()
    for n, line in enumerate(lines, start=1):
        if n % 7 == 1:
            ID = scanf('Monkey %d:', line)[0]
        elif n % 7 == 2:
            starting_items = [int(x) for x in line.removeprefix('  Starting items: ').split(', ')]
        elif n % 7 == 3:
            operation = 'lambda x: (x op)'.replace('op', line.removeprefix('  Operation: new = old ').replace('old', 'x'))
        elif n % 7 == 4:
            divisor = scanf('  Test: divisible by %d', line)[0]
            M *= divisor
        elif n % 7 == 5:
            true = scanf('    If true: throw to monkey %d', line)[0]
        elif n % 7 == 6:
            false = scanf('    If false: throw to monkey %d', line)[0]
            monkey1 = Monkey(ID, starting_items.copy(), eval(operation + ' // 3'), divisor, {True: true, False: false})
            monkeys1.append(monkey1)
            monkey2 = Monkey(ID, starting_items.copy(), eval(operation), divisor, {True: true, False: false})
            monkeys2.append(monkey2)

def perform_round(monkeys):
    for monkey in monkeys:
        for x in monkey.starting_items.copy():
            monkey.starting_items.pop(0)
            x = monkey.operation(x) % M
            monkey.inspection_count += 1
            new_index = monkey.test[1][monkey.test[0](x)]
            for new_monkey in monkeys:
                if new_monkey.index == new_index:
                    new_monkey.starting_items.append(x)
                    break

for i in range(20):
    perform_round(monkeys1)
monkey_inspection_count_1 = sorted([monkey.inspection_count for monkey in monkeys1], reverse=True)

for i in range(1, 10001):
    perform_round(monkeys2)
monkey_inspection_count_2 = sorted([monkey.inspection_count for monkey in monkeys2], reverse=True)

print(f"Part 1: {monkey_inspection_count_1[0] * monkey_inspection_count_1[1]}")
print(f"Part 2: {monkey_inspection_count_2[0] * monkey_inspection_count_2[1]}")
