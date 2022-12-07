f = open('input.txt')
lst = f.read().split('\n')

opp_enc = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors'}
my_enc = {'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}
shape = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
outcome = {'lose': 0, 'draw': 3, 'win': 6}

# Part 1
total1 = 0
for x in lst:
    opp_choice = opp_enc[x[0]]
    my_choice = my_enc[x[2]]
    shape_score = shape[my_choice]
    tup = (my_choice, opp_choice)
    if tup in [('Rock', 'Scissors'), ('Scissors', 'Paper'), ('Paper', 'Rock')]:
        outcome_score = outcome['win']
    elif tup in [('Rock', 'Paper'), ('Scissors', 'Rock'), ('Paper', 'Scissors')]:
        outcome_score = outcome['lose']
    elif my_choice == opp_choice:
        outcome_score = outcome['draw']
    score = shape_score + outcome_score
    total1 += score

# Part 2
my_enc = {
    'lose': {'Rock': 'Scissors', 'Scissors': 'Paper', 'Paper': 'Rock'},
    'draw': {'Rock': 'Rock', 'Scissors': 'Scissors', 'Paper': 'Paper'},
    'win': {'Rock': 'Paper', 'Scissors': 'Rock', 'Paper': 'Scissors'},
}
outcome_enc = {'X': 'lose', 'Y': 'draw', 'Z': 'win'}

total2 = 0
for x in lst:
    opp_choice = opp_enc[x[0]]
    desired_outcome = outcome_enc[x[2]]
    outcome_score = outcome[desired_outcome]
    my_choice = my_enc[desired_outcome][opp_choice]
    shape_score = shape[my_choice]
    score = shape_score + outcome_score
    total2 += score

print(total1)
print(total2)
