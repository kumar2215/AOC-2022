
with open("input.txt") as f:
    seq = f.read().split(",")

def my_hash(string: str):
    current = 0
    for s in string:
        current += ord(s)
        current *= 17
        current %= 256
    return current

lst = []
class Box:

    def __init__(self, ID):
        self.ID = ID
        self.labels = {}

boxes = [Box(n) for n in range(256)]

for lens in seq:
    lst.append(my_hash(lens))
    if '=' in lens:
        label, f = lens.split('=')
        boxes[my_hash(label)].labels[label] = int(f)
    elif '-' in lens:
        label = lens.split('-')[0]
        box = boxes[my_hash(label)]
        if label in box.labels:
            box.labels.pop(label)

power = 0
for ID, box in enumerate(boxes, start=1):
    for slot, label in enumerate(box.labels, start=1):
        f = box.labels[label]
        power += ID * slot * f

print(f"Part 1: {sum(lst)}")
print(f"Part 2: {power}")
