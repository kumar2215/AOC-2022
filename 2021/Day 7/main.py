with open('input.txt', 'r') as f:
    lst = [int(i) for i in f.read().split(',')]

total_fuel1 = {pos: sum([abs(x-pos) for x in lst]) for pos in lst}  # Part 1
total_fuel2 = {pos: sum([int(abs(x-pos)*(abs(x-pos)+1)/2) for x in lst]) for pos in lst}  # Part 2

print(f"Part 1: {min(total_fuel1.values())}")
print(f"Part 2: {min(total_fuel2.values())}")
