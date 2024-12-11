from collections import Counter
from multiprocessing import Process, Value
with open("input.txt") as f:
    org_stones = [int(x) for x in f.read().split(" ")]

PART1, BLINKS = 24, 75
total = Value('l', 0)  
total2 = Value('l', 0)

def handle_stone(num, blinks):
    global total, total2
    stones = Counter([num])
    for i in range(blinks):
        new_stones = Counter()
        for stone in stones:
            if stone == 0: new_stones[1] += stones[stone] 
            elif len(str(stone)) % 2 == 0:
                mid = len(str(stone)) // 2
                part1 = int(str(stone)[:mid])
                part2 = int(str(stone)[mid:])
                new_stones[part1] += stones[stone]
                new_stones[part2] += stones[stone]
            else:
                new_stones[stone * 2024] += stones[stone]
        stones = new_stones
        if i == PART1: 
            total.value += sum(stones.values())
    total2.value += sum(stones.values())
        
processes = []
for num in org_stones:
    p = Process(target=handle_stone, args=(num, BLINKS))
    p.start()
    processes.append(p)

for p in processes:
    p.join()

print(f"Part 1: {total.value}")
print(f"Part 2: {total2.value}")