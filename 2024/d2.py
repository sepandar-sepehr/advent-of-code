input_lines = []
with open('d2_input', 'r') as file:
    for line in file:
        input_lines.append([int(i) for i in line.split()])

print(input_lines)

def is_safe(line):
    is_safe = True
    all_increasing = True
    all_decreasing = True
    for i in range(len(line)):
        if i == len(line)-1:
            continue
        if abs(line[i] - line[i+1]) == 0 or abs(line[i] - line[i+1]) >= 4:
            is_safe = False
        if line[i] > line[i+1]:
            all_increasing = False
        if line[i] < line[i+1]:
            all_decreasing = False

    if is_safe and (all_increasing or all_decreasing):
        return True

safe = 0
for line in input_lines:
    if is_safe(line):
        safe += 1

print('part 1: ', safe)

safe = 0
for line in input_lines:
    for i in range(len(line)):
        new_line = line.copy()
        new_line.pop(i)
        if is_safe(new_line):
            safe += 1
            break

print('part 2: ', safe)