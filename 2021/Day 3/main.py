with open('input.txt', 'r') as f:
    lst = f.read().split('\n')
    Lst = [[x[i] for x in lst] for i in range(len(lst[0]))]

gamma = ''
epsilon = ''
for line in Lst:
    if line.count('1') > line.count('0'):
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

oxygen_generator_rating = lst.copy()
for index in range(len(Lst)):
    l = Lst[index]
    if l.count('1') >= l.count('0'):
        oxygen_generator_rating = list(filter(lambda x: x[index] == '1', oxygen_generator_rating))
    else:
        oxygen_generator_rating = list(filter(lambda x: x[index] == '0', oxygen_generator_rating))
    if len(oxygen_generator_rating) == 1:
        oxygen_generator_rating = oxygen_generator_rating[0]
        break
    Lst = [[x[i] for x in oxygen_generator_rating] for i in range(len(oxygen_generator_rating[0]))]

CO2_scrubbing_rating = lst.copy()
for index in range(len(Lst)):
    l = Lst[index]
    if l.count('1') >= l.count('0'):
        CO2_scrubbing_rating = list(filter(lambda x: x[index] == '0', CO2_scrubbing_rating))
    else:
        CO2_scrubbing_rating = list(filter(lambda x: x[index] == '1', CO2_scrubbing_rating))
    if len(CO2_scrubbing_rating) == 1:
        CO2_scrubbing_rating = CO2_scrubbing_rating[0]
        break
    Lst = [[x[i] for x in CO2_scrubbing_rating] for i in range(len(CO2_scrubbing_rating[0]))]

gamma = int(gamma, base=2)
epsilon = int(epsilon, base=2)
print(f"Part 1: {gamma * epsilon}")

oxygen_generator_rating = int(''.join(oxygen_generator_rating), base=2)
CO2_scrubbing_rating = int(''.join(CO2_scrubbing_rating), base=2)
print(f"Part 2: {oxygen_generator_rating * CO2_scrubbing_rating}")
