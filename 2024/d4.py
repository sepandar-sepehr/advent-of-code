input_lines = []
with open('d4_input', 'r') as file:
    for line in file:
        input_lines.append(line.strip())

print(input_lines)

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

def is_xmas(pos, dir):
    pos = (pos[0] + dir[0], pos[1] + dir[1])
    if 0 <= pos[0] < len(input_lines) and 0 <= pos[1] < len(input_lines[0]):
        if input_lines[pos[0]][pos[1]] != 'M':
            return False
    else:
        return False

    pos = (pos[0] + dir[0], pos[1] + dir[1])
    if 0 <= pos[0] < len(input_lines) and 0 <= pos[1] < len(input_lines[0]):
        if input_lines[pos[0]][pos[1]] != 'A':
            return False
    else:
        return False

    pos = (pos[0] + dir[0], pos[1] + dir[1])
    if 0 <= pos[0] < len(input_lines) and 0 <= pos[1] < len(input_lines[0]):
        if input_lines[pos[0]][pos[1]] != 'S':
            return False
    else:
        return False

    return True

sum = 0
for i in range(len(input_lines)):
    for j in range(len(input_lines[0])):
        if input_lines[i][j] == 'X':
            for dir in DIRECTIONS:
                if is_xmas((i, j), dir):
                    sum += 1

print('part 1: ', sum)

#### part 2 ####

def is_x_mas_2_pos(pos1, pos2):
    if 0 <= pos1[0] < len(input_lines) and 0 <= pos1[1] < len(input_lines[0]):
        if 0 <= pos2[0] < len(input_lines) and 0 <= pos2[1] < len(input_lines[0]):
            if ((input_lines[pos1[0]][pos1[1]] != 'M' or input_lines[pos2[0]][pos2[1]] != 'S') and
                    (input_lines[pos1[0]][pos1[1]] != 'S' or input_lines[pos2[0]][pos2[1]] != 'M')):
                return False
        else:
            return False
    else:
        return False
    return True

def is_x_mas(pos):
    pos1_a = (pos[0] + 1, pos[1] + 1)
    pos2_a = (pos[0] - 1, pos[1] - 1)
    pos1_b = (pos[0] + 1, pos[1] - 1)
    pos2_b = (pos[0] - 1, pos[1] + 1)
    if is_x_mas_2_pos(pos1_a, pos2_a) and is_x_mas_2_pos(pos1_b, pos2_b):
        return True

    return False

sum = 0
for i in range(len(input_lines)):
    for j in range(len(input_lines[0])):
        if input_lines[i][j] == 'A':
            if is_x_mas((i, j)):
                sum += 1

print('part 2: ', sum)