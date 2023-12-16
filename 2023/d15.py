from collections import defaultdict

with open('d15_input', 'r') as file:
    line = file.readline()
    lines = [val.strip() for val in line.strip().split(',')]


def hash(input_str):
    val = 0
    for c in input_str:
        val += ord(c)
        val *= 17
        val %= 256
    return val


res = 0
for code in lines:
    res += hash(code)
print('part1', res)

boxes = defaultdict(list)


def box_has_foc(box, foc):
    for (f, v) in boxes[box]:
        if f == foc:
            return True
    return False


def replace_foc(box, foc, val):
    for i, (f, v) in enumerate(boxes[box]):
        if f == foc:
            boxes[box][i] = (f, val)
            return


def remove_foc(box, foc):
    for i, (f, v) in enumerate(boxes[box]):
        if f == foc:
            boxes[box].pop(i)
            return


for code in lines:
    if len(code.split('=')) > 1:
        foc = code.split('=')[0].strip()
        val = int(code.split('=')[1].strip())
        box = hash(foc)
        if box_has_foc(box, foc):
            replace_foc(box, foc, val)
        else:
            boxes[box].append((foc, val))
    else:
        foc = code.split('-')[0].strip()
        box = hash(foc)
        if box_has_foc(box, foc):
            remove_foc(box, foc)

res_2 = 0
for box in boxes:
    for i, (f, v) in enumerate(boxes[box]):
        res_2 += (box + 1) * (i + 1) * v

print('part2', res_2)
