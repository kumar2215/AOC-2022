
with open("input.txt") as f:
    seq = f.read().split(",")

def my_hash(string: str):
    current = 0
    for s in string:
        current = (current + ord(s)) * 17 % 256
    return current

lst = []
boxes = [{} for n in range(256)]
for lens in seq:
    lst.append(my_hash(lens))
    if '=' in lens:
        label, f = lens.split('=')
        boxes[my_hash(label)][label] = int(f)
    elif '-' in lens:
        label = lens.split('-')[0]
        box = boxes[my_hash(label)]
        if label in box:
            box.pop(label)

power = 0
for ID, box in enumerate(boxes, start=1):
    for slot, label in enumerate(box, start=1):
        power += ID * slot * box[label]

print(f"Part 1: {sum(lst)}")
print(f"Part 2: {power}")
