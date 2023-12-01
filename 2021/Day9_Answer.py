matrix = []
with open('d9_input', 'r') as file:
	for line in file:
		matrix.append([int(c) for c in line.strip()])


def is_low(i, j, matrix):
	cur_val = matrix[i][j]
	if i - 1 >= 0:
		if matrix[i-1][j] <= cur_val:
			return False
	if i + 1 < len(matrix):
		if matrix[i+1][j] <= cur_val:
			return False
	if j - 1 >= 0:
		if matrix[i][j-1] <= cur_val:
			return False
	if j + 1 < len(matrix[0]):
		if matrix[i][j+1] <= cur_val:
			return False

	return True

total_risk = 0
low_points = []
for i, row in enumerate(matrix):
	for j, num in enumerate(row):
		if is_low(i, j, matrix):
			low_points.append((i,j))
			total_risk += matrix[i][j] + 1

print('part 1:', total_risk)

i_max = len(matrix)
j_max = len(matrix[0])

def get_neighbours(i,j, visited):
	neighbours = []
	if i>0 and (i-1, j) not in visited and matrix[i-1][j] != 9:
		neighbours.append((i-1, j))
	if j>0 and (i, j-1) not in visited and matrix[i][j-1] != 9:
		neighbours.append((i, j-1))
	if i + 1 < i_max and (i+1, j) not in visited and matrix[i+1][j] != 9:
		neighbours.append((i+1, j))
	if j + 1 < j_max and (i, j+1) not in visited and matrix[i][j+1] != 9:
		neighbours.append((i, j+1))
	return neighbours

def basin_size(i, j, matrix):
	visited = [(i,j)]
	cur_i = i
	cur_j = j
	neighbours = get_neighbours(cur_i,cur_j, visited)
	while len(neighbours) > 0:
		new_neighbours = []
		for neighbour in neighbours:
			visited.append(neighbour)
			new_neighbours.extend(get_neighbours(neighbour[0], neighbour[1], visited))

		neighbours = list(set(new_neighbours))

	return len(visited)
	

basin_sizes = []
for low_point in low_points:
	basin_sizes.append(basin_size(low_point[0], low_point[1], matrix))
basin_sizes.sort()
print('part 2:', basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3])
