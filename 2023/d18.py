instructions = []
with open('d18_input', 'r') as file:
    for line in file:
        data = line.strip().split()
        instructions.append((data[0], int(data[1])))

print(instructions)

plane = [['.' for i in range(500)] for j in range(500)]
cur = (250, 0) # (y, x)
for instruction in instructions:
    if instruction[0] == 'R':
        for i in range(instruction[1]):
            plane[cur[0]][cur[1] + i] = '#'
        cur = (cur[0], cur[1] + instruction[1])
    elif instruction[0] == 'D':
        for i in range(instruction[1]):
            plane[cur[0] + i][cur[1]] = '#'
        cur = (cur[0] + instruction[1], cur[1])
    elif instruction[0] == 'L':
        for i in range(instruction[1]):
            plane[cur[0]][cur[1] - i] = '#'
        cur = (cur[0], cur[1] - instruction[1])
    elif instruction[0] == 'U':
        for i in range(instruction[1]):
            plane[cur[0] - i][cur[1]] = '#'
        cur = (cur[0] - instruction[1], cur[1])
    else:
        print("ERROR")

def print_plane(plane):
    for i in range(len(plane)):
        print(''.join(plane[i]))

print_plane(plane)

visited = [[False for _ in range(len(plane[0]))] for _ in range(len(plane))]

# hit max recursion, not useful
def flood_fill_dfs(plane, y, x):
    if y < 0 or y >= len(plane)-1 or x < 0 or x >= len(plane[y])-1 or visited[x][y] or plane[y][x] == '#':
        return

    visited[x][y] = True

    plane[y][x] = '#'
    flood_fill_dfs(plane, y, x + 1)
    flood_fill_dfs(plane, y, x - 1)
    flood_fill_dfs(plane, y + 1, x)
    flood_fill_dfs(plane, y - 1, x)

    return

def flood_fill_iterative(plane, y, x):
    stack = [(y, x)]
    while stack:
        y, x = stack.pop()
        if y < 0 or y >= len(plane)-1 or x < 0 or x >= len(plane[y])-1 or plane[y][x] == '#':
            continue

        plane[y][x] = '#'
        stack.append((y, x + 1))
        stack.append((y, x - 1))
        stack.append((y + 1, x))
        stack.append((y - 1, x))

# arbitrary number based on my input
flood_fill_iterative(plane, 251, 20)

print_plane(plane)


res = 0
for i in range(len(plane)):
    for j in range(len(plane[i])):
        if plane[i][j] == '#':
            res += 1

print('part1: ', res)
