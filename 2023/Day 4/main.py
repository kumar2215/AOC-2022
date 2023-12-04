
with open('input.txt') as f:
    lines = f.read().split('\n')
    cards = {}
    num_cards = {}
    for line in lines:
        ID, rest = line.split(': ')
        ID = int([c for c in ID.split(' ') if c][1])
        winning, have = rest.split(' | ')
        winning, have = [int(x) for x in winning.split(' ') if x], [int(x) for x in have.split(' ') if x]
        cards[ID] = (winning, have)
        num_cards[ID] = 1

total = 0
for card in cards:
    winning, have = cards[card]
    won = [x for x in have if x in winning]
    total += 2 ** (len(won) - 1) if won else 0

    for new_card in range(card + 1, card + len(won) + 1):
        num_cards[new_card] += num_cards[card]

print(f"Part 1: {total}")
print(f"Part 2: {sum(num_cards.values())}")
