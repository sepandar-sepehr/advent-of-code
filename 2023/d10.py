import math

matrix = []
with open('d10_input', 'r') as file:
    matrix = [[c for c in line.strip()] for line in file]


# for each, see if it's a loop
# count distance
def find_s():
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'S':
                return (i, j)

s_pos = find_s()
print('S pos:', s_pos)
neighbours_dir = [(0, -1), (-1, 0), (1, 0), (0, 1)]


def is_north(pos, rel_pos):
    if pos[0]-1 == rel_pos[0] and pos[1] == rel_pos[1]:
        return True
    return False


def is_south(pos, rel_pos):
    if pos[0]+1 == rel_pos[0] and pos[1] == rel_pos[1]:
        return True
    return False

def is_east(pos, rel_pos):
    if pos[0] == rel_pos[0] and pos[1]+1 == rel_pos[1]:
        return True
    return False

def is_west(pos, rel_pos):
    if pos[0] == rel_pos[0] and pos[1]-1 == rel_pos[1]:
        return True
    return False

def find_valid_options():
    valid_options = []

    maybe_neighbours = [(s_pos[0]+dir[0], s_pos[1]+dir[1]) for dir in neighbours_dir]
    non_empty_neighbours = [pos for pos in maybe_neighbours if matrix[pos[0]][pos[1]] != '.' and pos[0] >= 0 and pos[1] >= 0]
    print('non_empty_neighbours', non_empty_neighbours)
    for i in range(len(non_empty_neighbours)):
        for j in range(i+1, len(non_empty_neighbours)):
            n1 = non_empty_neighbours[i]
            n2 = non_empty_neighbours[j]
            if (is_north(s_pos, n1) and is_south(s_pos, n2)) or (is_north(s_pos, n2) and is_south(s_pos, n1)):
                valid_options.append('|')
            elif (is_north(s_pos, n1) and is_east(s_pos, n2)) or (is_north(s_pos, n2) and is_east(s_pos, n1)):
                valid_options.append('L')
            elif (is_north(s_pos, n1) and is_west(s_pos, n2)) or (is_north(s_pos, n2) and is_west(s_pos, n1)):
                valid_options.append('J')
            elif (is_east(s_pos, n1) and is_west(s_pos, n2)) or (is_east(s_pos, n2) and is_west(s_pos, n1)):
                valid_options.append('-')
            elif (is_east(s_pos, n1) and is_south(s_pos, n2)) or (is_east(s_pos, n2) and is_south(s_pos, n1)):
                valid_options.append('F')
            elif (is_west(s_pos, n1) and is_south(s_pos, n2)) or (is_west(s_pos, n2) and is_south(s_pos, n1)):
                valid_options.append('7')
            else:
                print("WTF!", n1, n2, s_pos)
                raise Exception('Invalid combo')

    return valid_options


valid_options = find_valid_options()
print(valid_options)

valid_east = ['7', 'J', '-']
valid_west = ['L', 'F', '-']
valid_north = ['7', 'F', '|']
valid_south = ['L', 'J', '|']
def next_curs(pos):
    if matrix[pos[0]][pos[1]] == '|':
        if matrix[pos[0]-1][pos[1]] not in valid_north:
            return None
        if matrix[pos[0]+1][pos[1]] not in valid_south:
            return None
        return (pos[0]-1, pos[1]), (pos[0]+1, pos[1])
    elif matrix[pos[0]][pos[1]] == '-':
        if matrix[pos[0]][pos[1]-1] not in valid_west:
            return None
        if matrix[pos[0]][pos[1]+1] not in valid_east:
            return None
        return (pos[0], pos[1]-1), (pos[0], pos[1]+1)
    elif matrix[pos[0]][pos[1]] == 'L':
        if matrix[pos[0]-1][pos[1]] not in valid_north:
            return None
        if matrix[pos[0]][pos[1]+1] not in valid_east:
            return None
        return (pos[0]-1, pos[1]), (pos[0], pos[1]+1)
    elif matrix[pos[0]][pos[1]] == 'J':
        if matrix[pos[0] - 1][pos[1]] not in valid_north:
            return None
        if matrix[pos[0]][pos[1]-1] not in valid_west:
            return None
        return (pos[0]-1, pos[1]), (pos[0], pos[1]-1)
    elif matrix[pos[0]][pos[1]] == '7':
        if matrix[pos[0] + 1][pos[1]] not in valid_south:
            return None
        if matrix[pos[0]][pos[1] - 1] not in valid_west:
            return None
        return (pos[0]+1, pos[1]), (pos[0], pos[1]-1)
    elif matrix[pos[0]][pos[1]] == 'F':
        if matrix[pos[0] + 1][pos[1]] not in valid_south:
            return None
        if matrix[pos[0]][pos[1] + 1] not in valid_east:
            return None
        return (pos[0]+1, pos[1]), (pos[0], pos[1]+1)
    else:
        print("WTF!", pos)
        raise Exception('Invalid combo')

def is_invalid_pos(pos):
    if pos[0] >= 0 and pos[1] >= 0 and pos[0] < len(matrix) and pos[1] < len(matrix[0]):
        return False
    return True

def is_diff_pos(pos1, pos2):
    return pos1[0] != pos2[0] or pos1[1] != pos2[1]

def count_loop():
    visited = [s_pos]
    count = 1
    prev_cur1 = s_pos
    prev_cur2 = s_pos
    curs = next_curs(s_pos)
    if not curs:
        return math.inf, []
    (cur1, cur2) = curs
    visited.append(cur2)
    visited.append(cur1)
    while is_diff_pos(cur1, cur2):
        if is_invalid_pos(cur1) or is_invalid_pos(cur2):
            return math.inf, []

        curs = next_curs(cur1)
        if not curs:
            return math.inf, []
        next_cur1_1, next_cur1_2 = curs
        if is_diff_pos(next_cur1_1, prev_cur1):
            prev_cur1 = cur1
            cur1 = next_cur1_1
        else:
            prev_cur1 = cur1
            cur1 = next_cur1_2

        curs = next_curs(cur2)
        if not curs:
            return math.inf, []
        next_cur2_1, next_cur2_2 = curs
        if is_diff_pos(next_cur2_1, prev_cur2):
            prev_cur2 = cur2
            cur2 = next_cur2_1
        else:
            prev_cur2 = cur2
            cur2 = next_cur2_2

        visited.append(cur2)
        visited.append(cur1)

        count += 1
    return count, visited

def clear_junk(visited):
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if (i,j) not in visited:
                matrix[i][j] = '.'

def find_loop_len():
    for valid_option in valid_options:
        matrix[s_pos[0]][s_pos[1]] = valid_option
        loop_len, visited = count_loop()
        if loop_len != math.inf:
            return(loop_len, visited)


loop_len_res = find_loop_len()

print('part 1: ', loop_len_res[0])
clear_junk(loop_len_res[1])

count_I = 0
for i in range(len(matrix)):
    col_border_count = 0
    for j in range(len(matrix[0])):
        if matrix[i][j] in ['F', '7', '|']:
            col_border_count += 1
        elif matrix[i][j] == '.':
            if col_border_count%2 == 0:
                matrix[i][j] = '0'
            else:
                matrix[i][j] = 'I'
                count_I += 1
print(matrix)
print('Part 2: ', count_I)

