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

area = 1
cur_x = 0
cur_y = 0
for i, instruction in enumerate(instructions):
    x1, y1 = cur_x, cur_y

    dir = instruction[0]
    if dir == 'R':
        cur_x += instruction[1]
    elif dir == 'U':
        cur_y += instruction[1]
    elif dir == 'D':
        cur_y -= instruction[1]
    else:
        cur_x -= instruction[1]

    x2, y2 = cur_x, cur_y

    area += (x2 * y1 - x1 * y2)/2
    area += (instruction[1]/2)

x2, y2 = 0, 0
x1, y2 = cur_x, cur_y
area += (x2 * y1 - x1 * y2)/2


print('part2: ', area)

# 38605030150591 too low
# 38605101747529 too low