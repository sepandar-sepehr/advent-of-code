lines = []
res = 0
with open('d9_input', 'r') as file:
    for line in file:
        lines.append([int(i) for i in line.strip().split()])

next_vals = []


def get_next_val(line):
    proc_lines = [line]
    next_line = line

    while any(i != 0 for i in next_line):
        next_line = []
        for i, num in enumerate(line):
            if i == len(line)-1:
                continue
            next_line.append(line[i+1] - num)
        proc_lines.append(next_line)
        line = next_line

    for i in range(len(proc_lines)-1, 0, -1):
        new_val = proc_lines[i-1][-1] + proc_lines[i][-1]
        proc_lines[i-1].append(new_val)

    return proc_lines[0][-1]


for line in lines:
    next_vals.append(get_next_val(line))


print(sum(next_vals))

# part 2

def get_prev_val(line):
    proc_lines = [line]
    next_line = line

    while any(i != 0 for i in next_line):
        next_line = []
        for i, num in enumerate(line):
            if i == len(line)-1:
                continue
            next_line.append(line[i+1] - num)
        proc_lines.append(next_line)
        line = next_line

    for i in range(len(proc_lines)-1, 0, -1):
        prev_line = proc_lines[i - 1]
        new_val = prev_line[0] - proc_lines[i][0]
        prev_line.reverse()
        prev_line.append(new_val)
        prev_line.reverse()

    return proc_lines[0][0]


next_vals=[]
for line in lines:
    next_vals.append(get_prev_val(line))


print(sum(next_vals))
