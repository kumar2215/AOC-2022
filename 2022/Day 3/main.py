f = open('input.txt')
lst = f.read().split('\n')

lower = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
         'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
upper = {'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38,
         'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52}
overall = lower | upper

# Part 1
total1 = 0
for x in lst:
    l = len(x)
    first_part = set(x[0:int(l / 2)])
    second_part = set(x[int(l / 2):l])
    total1 += overall[list(first_part.intersection(second_part))[0]]

# Part 2
total2 = 0
for i in range(len(lst)):
    if i % 3 == 0:
        temp = lst[i:i + 3]
        first = set(temp[0])
        second = set(temp[1])
        third = set(temp[2])
        s = first.intersection(second)
        s = third.intersection(s)
        total2 += overall[list(s)[0]]

print(total1)
print(total2)
