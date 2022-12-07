f = open('input.txt')
lst = f.read().split('\n')
sum_array = []
temp = []

for x in lst:
    if x != '' and x.isnumeric():
        temp.append(int(x))
    elif x == '' or x == lst[len(lst) - 1]:
        sum_array.append(sum(temp.copy()))
        temp.clear()
print(max(sum_array))  # Part 1

sum_array.sort(reverse=True)
print(sum(sum_array[0:3]))  # Part 2
