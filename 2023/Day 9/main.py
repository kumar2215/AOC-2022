
with open("input.txt") as f:
    historys = [[[int(x) for x in line.split()]] for line in f.read().split('\n')]
    
pred = []
pred_2 = []

for history in historys:
    temp = history[0].copy()
    while any(temp):
        temp = [temp[i+1] - temp[i] for i in range(len(temp) - 1)]
        history.append(temp)
    pred.append(sum([s[-1] for s in history]))
    first = 0
    for seq in history[::-1]:
      first = seq[0] - first
    pred_2.append(first)
    
print(f"Part 1: {sum(pred)}")
print(f"Part 2: {sum(pred_2)}")
