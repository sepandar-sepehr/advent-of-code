import math

nodes = {}
with open('d8_input', 'r') as file:
    instructions = file.readline().strip()
    file.readline()
    for line in file:
        cur = line.strip().split('=')[0].strip()
        lr = line.strip().split('=')[1].strip().replace('(', '').replace(')', '').split(',')
        left = lr[0].strip()
        right = lr[1].strip()
        nodes[cur] = (left, right)

print(instructions)
print(nodes)

# Part 1
cur_node = 'AAA'
count = 0
instruction_i = 0
while cur_node != 'ZZZ':
    next_instruction = instructions[instruction_i % len(instructions)]
    if next_instruction == 'R':
        cur_node = nodes[cur_node][1]
    else:
        cur_node = nodes[cur_node][0]
    instruction_i +=1
    count += 1
print('part 1:', count)

# Part 2
curs = []
for node in nodes.keys():
    if node[-1] == 'A':
        curs.append(node)
print(curs)

#  following is too slow:
#
# def have_reached(nodes):
#     for node in nodes:
#         if node[-1] != 'Z':
#             return False
#     return True

# instruction_i = 0
# count = 0
# while not have_reached(curs):
#     next_instruction = instructions[instruction_i % len(instructions)]
#     for i in range(len(curs)):
#         cur_node = curs[i]
#         if next_instruction == 'R':
#             cur_node = nodes[cur_node][1]
#         else:
#             cur_node = nodes[cur_node][0]
#         curs[i] = cur_node
#     instruction_i += 1
#     count += 1

loop_counts = [0] * len(curs)
for i in range(len(curs)):
    cur_node = curs[i]
    instruction_i = 0
    count = 0
    while cur_node[-1] != 'Z':
        next_instruction = instructions[instruction_i % len(instructions)]
        if next_instruction == 'R':
            cur_node = nodes[cur_node][1]
        else:
            cur_node = nodes[cur_node][0]
        instruction_i +=1
        count += 1
    loop_counts[i] = count


print('part 2:', math.lcm(*loop_counts))