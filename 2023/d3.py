import math

matrix = list()
with open('d3_input', 'r') as file:
    for line in file:
        matrix.append([c for c in line.strip()])


def adjacents(position):
    return [(position[0] - 1, position[1]), (position[0], position[1] - 1), (position[0] + 1, position[1]),
            (position[0], position[1] + 1),
            (position[0] - 1, position[1] - 1), (position[0] - 1, position[1] + 1), (position[0] + 1, position[1] + 1),
            (position[0] + 1, position[1] - 1)]


def is_symbol(position):
    if 0 <= position[0] < len(matrix) and 0 <= position[1] < len(matrix[0]):
        if not matrix[position[0]][position[1]].isnumeric() and matrix[position[0]][position[1]] != '.':
            return True
    return False

def numbers_have_symbol_adjacent(number_positions):
    for number_position in number_positions:
        if any(is_symbol(position) for position in adjacents(number_position)):
            return True
    return False


matching_nums = []
for i, row in enumerate(matrix):
    buffer = []
    for j, c in enumerate(row):
        if c.isnumeric():
            buffer.append((i, j))
        else:
            if numbers_have_symbol_adjacent(buffer):
                number = int(''.join([matrix[num[0]][num[1]] for num in buffer]))
                matching_nums.append(number)
            buffer = []
    if len(buffer) != 0:
        if numbers_have_symbol_adjacent(buffer):
            number = int(''.join([matrix[num[0]][num[1]] for num in buffer]))
            matching_nums.append(number)

print(matching_nums)
print(sum(matching_nums))


def number_with_position(position):
    y = position[0]
    x = position[1]
    buffer = [matrix[y][x]]
    included_positions = [(y,x)]
    i = x-1
    still_num = True
    while i>=0 and still_num:
        if matrix[y][i].isnumeric():
            buffer.append(matrix[y][i])
            included_positions.append((y,i))
        else:
            still_num = False
        i-=1
    buffer.reverse()
    i = x + 1
    still_num = True
    while i < len(matrix[0]) and still_num:
        if matrix[y][i].isnumeric():
            buffer.append(matrix[y][i])
            included_positions.append((y,i))
        else:
            still_num = False
        i+=1
    if len(buffer) != 0:
        return (int(''.join(buffer)), included_positions)
    return (0, [])

# Part 2
total = 0
for i, row in enumerate(matrix):
    for j, c in enumerate(row):
        if c == '*':
            included_numbers = []
            for adjacent in adjacents((i, j)):
                if matrix[adjacent[0]][adjacent[1]].isnumeric():
                    (number, included_positions) = number_with_position(adjacent)
                    if number not in included_numbers and number != 0:
                        included_numbers.append(number)
            print(included_numbers)
            if len(included_numbers) == 2:
                total += math.prod(included_numbers)

print(total)