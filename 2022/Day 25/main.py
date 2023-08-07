from math import log, ceil

with open('input.txt', 'r') as f:
    Input = [[{'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}[sym] for sym in list(x)] for x in f.read().split('\n')]
    numbers = [sum([num * 5 ** idx for idx, num in enumerate(reversed(x))]) for x in Input]
    total = sum(numbers)
    total += int(''.join(('2' for i in range(ceil(log(total, 5))))), base=5)
    SNAFU = ''
    idx = int(log(total, 5))
    while total > 0:
        val = total // (5 ** idx)
        SNAFU += {2: '2', 1: '1', 0: '0', -1: '-', -2: '='}[val - 2]
        total -= val * (5 ** idx)
        idx -= 1
    print(SNAFU)
