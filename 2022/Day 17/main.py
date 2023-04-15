from copy import copy
with open('input.txt') as f:
    jets = list(f.read())

highest_point = 0
index = 1
chamber = [(i, 0) for i in range(1, 8)]

class Rock:

    def __init__(self, shape: list):
        self.shape = shape
        self.foot = [point for point in shape if point[0] == 0]
        self.position = {point: [point[0] + 3, point[1] + 4 + highest_point] for point in shape}

    def fall(self, idx):
        global highest_point
        self.position = {point: [point[0] + 3, point[1] + 4 + highest_point] for point in self.shape}
        while True:
            jet = jets[(idx - 1) % len(jets)]
            shift = [-1, 1][jet == '>']
            if all(1 <= self.position[point][0] + shift <= 7 for point in self.position)\
                and all((self.position[point][0] + shift, self.position[point][1]) not in chamber for point in self.position):
                for point in self.position:
                    self.position[point][0] += shift
            if all((self.position[point][0], self.position[point][1] - 1) not in chamber for point in self.position):
                for point in self.position:
                    self.position[point][1] -= 1
                idx += 1
            elif any((self.position[point][0], self.position[point][1] - 1) in chamber for point in self.position):
                idx += 1
                chamber.extend([tuple(self.position[point]) for point in self.position])
                highest_point = max(point[1] for point in chamber)
                break
        return idx

rock1 = Rock([(0, 0), (1, 0), (2, 0), (3, 0)])
rock2 = Rock([(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)])
rock3 = Rock([(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)])
rock4 = Rock([(0, 0), (0, 1), (0, 2), (0, 3)])
rock5 = Rock([(0, 0), (1, 0), (0, 1), (1, 1)])

rocks = [rock1, rock2, rock3, rock4, rock5]

H = []
for i in range(1, 8001):
    rock = copy(rocks[(i - 1) % 5])
    index = rock.fall(index)
    H.append(highest_point)

heights = [H[5 * i] - H[5 * i - 5] for i in range(1, len(H) // 5)]
period = 3

while True:
    interval1, interval2, interval3 = [], [], []
    start = 3
    while start + period < len(heights):
        interval1 = heights[start:start + period * 1]
        interval2 = heights[start + period * 1:start + period * 2]
        interval3 = heights[start + period * 2:start + period * 3]
        if interval1 == interval2 == interval3:
            break
        else:
            start += 1
    if interval1 == interval2 == interval3:
        break
    else:
        period += 1

diff = [H[i] - H[i - 1] for i in range(1, len(H))]

def calculate_height(n):
    N = n - start * 5
    initial = diff[0: start * 5]
    actual_period = period * 5
    interval = diff[start * 5: (start + period) * 5]
    remainder = N % actual_period
    if n <= start * 5: return sum(initial[0: n])
    else: return sum(initial) + (N // actual_period) * sum(interval) + sum(interval[0: remainder])

print(f'Part 1: {calculate_height(2022) - 1}')
print(f'Part 2: {calculate_height(10 ** 12)}')
