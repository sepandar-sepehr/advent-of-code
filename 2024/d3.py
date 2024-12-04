import re

input_lines = []
with open('d3_input', 'r') as file:
    for line in file:
        # input_lines.append([int(i) for i in line.strip().split()])
        input_lines.append(line)

print(input_lines)
input_str = ''.join(input_lines)
sum = 0
res = re.findall(r'mul\((\d+),(\d+)\)', input_str)
print(res)
for mul in res:
    sum += int(mul[0]) * int(mul[1])

print('part 1: ', sum)

# with open('sample2_d3_input', 'r') as file:
#     input_str = file.readlines()[0]

def add_muls(input_str):
    sum = 0
    res = re.findall(r'mul\((\d+),(\d+)\)', input_str)
    for mul in res:
        sum += int(mul[0]) * int(mul[1])
    return sum

def add_muls_rec(input_str):
    sum = 0
    dont_i = input_str.find("don't()")
    str1 = input_str[:dont_i]
    sum += add_muls(str1)

    str2 = input_str[dont_i:]
    if str2.find('do()') != -1:
        sum += add_muls_rec(str2[str2.find('do()'):])

    return sum

print('part2: ', add_muls_rec(input_str))