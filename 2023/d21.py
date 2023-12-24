with open('d21_input', 'r') as file:
    input_map = [[c for c in line.strip()] for line in file.readlines()]


start = (0, 0)
for y, line in enumerate(input_map):
    for x, c in enumerate(line):
        if c == 'S':
            start = (x, y)
            break

reached = {start}
input_map[start[1]][start[0]] = '.'

def find_new_reached():
    new_reached = set([])
    for x, y in reached:
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= x + dx < len(input_map[0]) and 0 <= y + dy < len(input_map):
                if input_map[y + dy][x + dx] == '.':
                    new_reached.add((x + dx, y + dy))
    return new_reached


def clear_reached():
    for i in range(len(input_map)):
        for j in range(len(input_map[0])):
            if input_map[i][j] == 'O':
                input_map[i][j] = '.'

for i in range(64):
    new_reached = find_new_reached()
    clear_reached()
    for x, y in new_reached:
        input_map[y][x] = 'O'
    reached = new_reached

def count_plots():
    return sum([sum([1 if c == 'O' else 0 for c in line]) for line in input_map])

print(count_plots())
