input_lines = []
with open('dn_input', 'r') as file:
    for line in file:
        # game_num = int(line.strip().split(':')[0].split(' ')[1])
        # sets = line.strip().split(':')[1].strip().split(';')
        # input_lines.append([int(i) for i in line.strip().split()])
        # seeds = [int(x) for x in file.readline().split(':')[1].strip().split()]
        input_lines.append(line)

print(input_lines)

sum = 0
print('part 1: ', sum)

print('part2: ', sum)