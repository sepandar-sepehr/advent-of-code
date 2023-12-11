import math

with open('d11_input', 'r') as file:
    lines = [[c for c in line.strip()] for line in file]

def no_galaxy_columns():
    cols = []
    for i in range(len(lines[0])):
        if all(c == '.' for c in [lines[j][i] for j in range(len(lines))]):
            cols.append(i)
    return cols

def no_galaxy_rows():
    rows = []
    for i in range(len(lines)):
        if all(c == '.' for c in [lines[i][j] for j in range(len(lines[0]))]):
            rows.append(i)
    return rows

new_map = []
rows_to_dup = no_galaxy_rows()
for i in range(len(lines)):
    new_map.append(lines[i])
    if i in rows_to_dup:
        new_map.append(lines[i])
# print(new_map)

cols_to_dup = no_galaxy_columns()
expanded_map = [[] for _ in range(len(new_map))]
# print(expanded_map)
for j in range(len(new_map[0])):
    for i in range(len(new_map)):
        c = new_map[i][j]
        expanded_map[i].append(c)
    if j in cols_to_dup:
        for i in range(len(new_map)):
            c = new_map[i][j]
            expanded_map[i].append(c)

# print(expanded_map)

def find_galaxies(space):
    galaxies = []
    for i, row in enumerate(space):
        for j, c in enumerate(row):
            if c =='#':
                galaxies.append((i,j))
    return galaxies

galaxies = find_galaxies(expanded_map)
sum_paths = 0
for i, galaxy_1 in enumerate(galaxies):
    for j, galaxy_2 in enumerate(galaxies):
        if i != j:
            dist = 0
            row_diff = math.fabs(galaxy_1[0] - galaxy_2[0])
            col_diff = math.fabs(galaxy_1[1] - galaxy_2[1])
            dist += row_diff + col_diff
            sum_paths += dist
            # print(galaxy_1, galaxy_2, dist)

print(sum_paths/2)


# part 2

def count_exp_cols_in_bw(g1, g2):
    first = min(g1[1], g2[1])
    second = max(g1[1], g2[1])
    count = 0
    for i in range(first+1, second):
        if i in cols_to_dup:
            count += 1
    return count

def count_exp_rows_in_bw(g1, g2):
    first = min(g1[0], g2[0])
    second = max(g1[0], g2[0])
    count = 0
    for i in range(first+1, second):
        if i in rows_to_dup:
            count += 1
    return count

galaxies = find_galaxies(lines)
sum_paths = 0
for i, galaxy_1 in enumerate(galaxies):
    for j, galaxy_2 in enumerate(galaxies):
        if i != j:
            dist = 0
            row_diff = math.fabs(galaxy_1[0] - galaxy_2[0])
            col_diff = math.fabs(galaxy_1[1] - galaxy_2[1])
            exp_rows = count_exp_rows_in_bw(galaxy_1, galaxy_2)
            if exp_rows != 0:
                dist += exp_rows * 1000000
                dist -= exp_rows
            exp_cols = count_exp_cols_in_bw(galaxy_1, galaxy_2)
            if exp_cols != 0:
                dist += exp_cols * 1000000
                dist -= exp_cols
            dist += row_diff + col_diff
            sum_paths += dist

print(sum_paths/2)