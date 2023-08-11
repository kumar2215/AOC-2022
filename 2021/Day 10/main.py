
with open('input.txt', 'r') as f:
    lines = [x for x in f.read().split('\n')]

L = ['(', '[', '{', '<']
complements = {')': '(', ']': '[', '}': '{', '>': '<'}
corrupted_lines = {}
syntax_checker_points_table = {')': 3, ']': 57, '}': 1197, '>': 25137}
syntax_checker_points = 0

for line in lines:
    lefts = []
    for char in line:
        if char in L:
            lefts.append(char)
        else:
            if complements[char] == lefts[-1]:
                lefts.pop()
                continue
            else:
                corrupted_lines[line] = char
                syntax_checker_points += syntax_checker_points_table[char]
                break

incomplete_lines = [line for line in lines if line not in corrupted_lines]
autocomplete_points_table = {'(': 1, '[': 2, '{': 3, '<': 4}
autocomplete_points = []

for line in incomplete_lines:
    lefts = []
    for char in line:
        if char in L:
            lefts.append(char)
        else:
            if complements[char] == lefts[-1]:
                lefts.pop()
                continue
    autocomplete_point = 0
    for char in reversed(lefts):
        autocomplete_point *= 5
        autocomplete_point += autocomplete_points_table[char]
    autocomplete_points.append(autocomplete_point)

print(f"Part 1: {syntax_checker_points}")
print(f"Part 2: {sorted(autocomplete_points)[int(len(autocomplete_points)/2)]}")
