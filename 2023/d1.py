input_lines = list()
with open('d1_input', 'r') as file:
    for line in file:
        input_lines.append(line)


# ** Part 1 **

# total = 0
# for line in input_lines:
# 	first_num = None
# 	last_num = None
# 	for char in line:
# 		if char.isdigit():
# 			if first_num is None:
# 				first_num = char
# 			else:
# 				last_num = char
# 	if last_num is None:
# 		last_num = first_num
# 	total += int(first_num + last_num)
#
# print(total)

# ** Part 2 **
def get_string_num_starting(line, i):
    if line[i:i + 3] == 'one':
        return '1'
    if line[i:i + 3] == 'two':
        return '2'
    if line[i:i + 5] == 'three':
        return '3'
    if line[i:i + 4] == 'four':
        return '4'
    if line[i:i + 4] == 'five':
        return '5'
    if line[i:i + 3] == 'six':
        return '6'
    if line[i:i + 5] == 'seven':
        return '7'
    if line[i:i + 5] == 'eight':
        return '8'
    if line[i:i + 4] == 'nine':
        return '9'
    return None


total = 0
for line in input_lines:
    first_num = None
    last_num = None
    for i in range(len(line)):
        maybeNum = get_string_num_starting(line, i)
        char = line[i]
        if maybeNum is not None:
            if first_num is None:
                first_num = maybeNum
            else:
                last_num = maybeNum

        if char.isdigit():
            if first_num is None:
                first_num = char
            else:
                last_num = char
        if last_num is None:
            last_num = first_num
    total += int(first_num + last_num)
print(total)
