f = open('input.txt')
lst = [i for i in f.read() if i.isalpha()]

#Part 1
for i in range(len(lst)):
    if len(set(lst[i: 4])) == 4:
        num = i + 4
        print(num)
        break
        
# Part 2        
for i in range(len(lst)):
    if len(set(lst[i: 14])) == 14:
        num = i + 14
        print(num)
        break
