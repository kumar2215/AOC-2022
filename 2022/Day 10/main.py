f = open('input.txt')
commands = f.read().split('\n')

cycle = 0
x = 1
signal_strength = []
sprite_pos = [0, 1, 2]
CRT_row = ''

for command in commands:
    if command.startswith('addx'):
        num = int(command.split()[1])
        for _ in range(2):
            if (cycle % 40) in sprite_pos:
                CRT_row += '#'
            elif (cycle % 40) not in sprite_pos:
                CRT_row += '.'
            cycle += 1
            if (cycle + 20) % 40 == 0:
                signal_strength.append(cycle * x)
        x += num
        sprite_pos = [pos+num for pos in sprite_pos]
    elif command == 'noop':
        if (cycle % 40) in sprite_pos:
            CRT_row += '#'
        elif (cycle % 40) not in sprite_pos:
            CRT_row += '.'
        cycle += 1
        if (cycle + 20) % 40 == 0:
            signal_strength.append(cycle * x)

print(sum(signal_strength))

for i in range(6):
    print(CRT_row[40*i:40*(i+1)])
