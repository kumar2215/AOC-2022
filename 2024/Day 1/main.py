with open("input.txt") as f:
    lines = f.readlines()
    L, R = [], []
    for line in lines:
        l, r = line.split()
        L.append(int(l))
        R.append(int(r))
    
L.sort()
R.sort()
total_distance = sum(abs(L[i] - R[i]) for i in range(len(L)))
similarity_score = sum(x * R.count(x) for x in L)

print(f"Part 1: {total_distance}")
print(f"Part 2: {similarity_score}")