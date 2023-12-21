# This worked with sample but has an issue with my input

instructions = []
with open('d18_input', 'r') as file:
    for line in file:
        data = line.strip().split()
        code = data[2][-2]
        if code == '0':
            dir = 'R'
        elif code == '1':
            dir = 'D'
        elif code == '2':
            dir = 'L'
        elif code == '3':
            dir = 'U'
        else:
            raise Exception('Invalid code')

        depth = int(data[2][2:-2], 16)
        instructions.append((dir, depth))

print(instructions)

stack = []

VALID_REC_SEQUENCES = [['R', 'D', 'L'], ['D', 'L', 'U'], ['L', 'U', 'R'], ['U', 'R', 'D']]


def has_potential_rec(stack):
    if len(stack) < 3:
        return False
    last3_directions = [i[0] for i in stack[-3:]]
    if last3_directions in VALID_REC_SEQUENCES:
        return True

def merge_last2(stack):
    if len(stack) < 2:
        return 0

    last2 = stack[-2:]
    directions = set([inst[0] for inst in last2])
    if len(directions) == 1:
        stack.pop()
        stack.pop()
        stack.append((last2[0][0], last2[0][1] + last2[1][1]))
        return 0
    elif directions in [{'R', 'L'}, {'U', 'D'}]:
        stack.pop()
        stack.pop()
        if last2[0][1] < last2[1][1]:
            stack.append((last2[1][0], last2[1][1] - last2[0][1]))
        else:
            stack.append((last2[0][0], last2[0][1] - last2[1][1]))
        return abs(last2[0][1] - last2[1][1])
    return 0

def extract_area(stack):
    last3 = [stack.pop() for _ in range(3)]
    last3.reverse()
    directions = [inst[0] for inst in last3]

    if directions == VALID_REC_SEQUENCES[0]:
        right_len = last3[0][1]
        left_len = last3[2][1]
        if right_len < left_len:
            stack.append(last3[1])
            merge_last2(stack)  # in case now two of same direction are on top of each other
            stack.append(('L', left_len-right_len))
        else:
            stack.append(('R', right_len-left_len))
            stack.append(last3[1])
    elif directions == VALID_REC_SEQUENCES[1]:
        down_len = last3[0][1]
        up_len = last3[2][1]
        if down_len < up_len:
            stack.append(last3[1])
            merge_last2(stack)
            stack.append(('U', up_len-down_len))
        else:
            stack.append(('D', down_len-up_len))
            stack.append(last3[1])
    elif directions == VALID_REC_SEQUENCES[2]:
        left_len = last3[0][1]
        right_len = last3[2][1]
        if left_len < right_len:
            stack.append(last3[1])
            merge_last2(stack)
            stack.append(('R', right_len-left_len))
        else:
            stack.append(('L', left_len-right_len))
            stack.append(last3[1])
    elif directions == VALID_REC_SEQUENCES[3]:
        up_len = last3[0][1]
        down_len = last3[2][1]
        if up_len < down_len:
            stack.append(last3[1])
            merge_last2(stack)
            stack.append(('D', down_len-up_len))
        else:
            stack.append(('U', up_len-down_len))
            stack.append(last3[1])
    else:
        raise Exception('Invalid directions')

    return min(last3[0][1], last3[2][1]) * last3[1][1]

area = 1
for instruction in instructions:
    stack.append(instruction)
    area+=instruction[1]/2
    print(stack)
    merge_last2(stack)
    print('stack after merge', stack)
    while has_potential_rec(stack):
        area += extract_area(stack)
        print('extracted', stack)
        print(area)


print('part2: ', area)

# 38605030150591 too low
# 38605101747529 too low