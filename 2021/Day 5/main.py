from collections import Counter
with open('input.txt', 'r') as f:
    lst = [x.split(' -> ') for x in f.read().split('\n')]

def main(part):
    count = 0
    coordinates = []
    for x in lst:
        x1, y1 = [int(i) for i in x[0].split(',')]
        x2, y2 = [int(i) for i in x[1].split(',')]
        if part == 1:
            if x1 > x2:
                x1, x2 = x2, x1
            if y1 > y2:
                y1, y2 = y2, y1
            if x1 == x2:
                coordinates.extend([(x1, i) for i in range(y1, y2+1)])
            elif y1 == y2:
                coordinates.extend([(i, y1) for i in range(x1, x2+1)])
        else:
            if x1 > x2:
                x1, y1, x2, y2 = x2, y2, x1, y1
            if x1 == x2 and y1 > y2:
                y1, y2 = y2, y1
            if x1 == x2:
                coordinates.extend([(x1, i) for i in range(y1, y2 + 1)])
            elif y1 == y2:
                coordinates.extend([(i, y1) for i in range(x1, x2 + 1)])
            elif abs(x2 - x1) == abs(y2 - y1):
                if int((y2 - y1) / (x2 - x1)) == 1:
                    coordinates.extend([(x1 + i, y1 + i) for i in range(0, (x2 - x1) + 1)])
                elif int((y2 - y1) / (x2 - x1)) == -1:
                    coordinates.extend([(x1 + i, y1 - i) for i in range(0, (x2 - x1) + 1)])
    for coordinate, num in dict(Counter(coordinates)).items():
        if num > 1:
            count += 1
    return count

print(f"Part 1: {main(1)}")
print(f"Part 2: {main(2)}")
