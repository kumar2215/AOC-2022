
with open('input.txt') as f:
    lines = f.read().split('\n')
    hands = {}
    for line in lines:
        hand, bid = line.split()
        hands[hand] = int(bid)

cards, cards_2 = list('AKQJT98765432'), list('AKQT98765432J')

class Hand:

    def __init__(self, hand: str, bid: int, part=1):
        self.hand = hand
        self.bid = bid
        self.type = 0
        self.part = part
        if part == 1:
            lst = list(hand)
            sorted_hand = sorted([lst.count(c) for c in set(hand)], reverse=True)
        else:
            temp = ''.join([c for c in hand if c != 'J'])
            temp = self.hand.replace('J', max(temp, key=lambda x: temp.count(x))) if temp else 'A' * 5
            lst = list(temp)
            sorted_hand = sorted([lst.count(c) for c in set(temp)], reverse=True)
        match sorted_hand:
            case [5]:
                self.type = 7
            case [4, 1]:
                self.type = 6
            case [3, 2]:
                self.type = 5
            case [3, 1, 1]:
                self.type = 4
            case [2, 2, 1]:
                self.type = 3
            case [2, 1, 1, 1]:
                self.type = 2
            case [1, 1, 1, 1, 1]:
                self.type = 1

    def __gt__(self, other):
        c = cards if self.part == 1 else cards_2
        if self.type != other.type:
            return self.type > other.type
        else:
            h1, h2 = self.hand, other.hand
            for i in range(5):
                if c.index(h1[i]) != c.index(h2[i]):
                    return c.index(h1[i]) < c.index(h2[i])


Hands = [Hand(hand, bid) for hand, bid in hands.items()]
Hands = sorted(Hands)
print(f"Part 1: {sum(i * hand.bid for i, hand in enumerate(Hands, start=1))}")

Hands_2 = [Hand(hand, bid, part=2) for hand, bid in hands.items()]
Hands_2 = sorted(Hands_2)
print(f"Part 2: {sum(i * hand.bid for i, hand in enumerate(Hands_2, start=1))}")
