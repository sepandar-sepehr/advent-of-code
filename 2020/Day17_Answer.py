def read_file():
	with open('Day17_input', 'r') as file:
		input = [list(line.strip()) for line in file.readlines()]
	return input

IDXS = [
	(0,0,-1), (0,0,1), 
	(0,-1,-1), (0,-1,+1), (0,-1,0), 
	(0,1,-1), (0,+1,+1), (0,+1,0),

	(-1,0,-1), (-1,0,+1), (-1,0,0),
	(1,0,-1), (1,0,1), (1,0,0),
	(-1,-1,-1), (-1,-1,1), (-1,-1,0),

	(1,1,-1), (1,1,1), (1,1,0),
	(-1,1,-1), (-1,1,1), (-1,1,0),
	(1,-1,-1), (1,-1,1), (1,-1,0)
]

def get_neighbour_idx(i, j, k):
	neighbours = [None] * 26
	for i2, idx in enumerate(IDXS):
		neighbours[i2] = (i+idx[0], j+idx[1], k+idx[2])
	return neighbours

def get_neighbours(cube, ijk):
	i = ijk[0]
	j = ijk[1]
	k = ijk[2]
	neighbours = [None] * 26
	for i2, idx in enumerate(IDXS):
		new_i = i+idx[0]
		new_j = j+idx[1]
		new_k = k+idx[2]
		if new_i >= 0 and new_j >= 0 and new_k >= 0 and new_k < len(cube[0][0]) and new_j < len(cube[0]) and new_i < len(cube):
			neighbours[i2] = cube[new_i][new_j][new_k]
		else:
			neighbours[i2] = '.'
	return neighbours

def count_actives(neighbours):
	count = 0
	for n in neighbours:
		if n == '#':
			count+=1 
	return count

def live(cube):
	new_cube = list()
	for i in range(len(cube)+2):
		plane = list()
		for j in range(len(cube[0])+2):
			plane.append([None]*(len(cube[0][0])+2))
		new_cube.append(plane)

	for i, plane in enumerate(cube):
		for j, row in enumerate(plane):
			for k, cell in enumerate(row):
				if cell == '#':
					neighbours = get_neighbours(cube, (i, j, k))
					active_count = count_actives(neighbours)
					if active_count == 2 or active_count == 3:
						new_cube[i+1][j+1][k+1] = '#'
				
				indices = get_neighbour_idx(i, j, k)
				for n_idx in indices:
					if new_cube[n_idx[0]+1][n_idx[1]+1][n_idx[2]+1] == None:
						neighbours = get_neighbours(cube, n_idx)
						active_count = count_actives(neighbours)
						if active_count == 3:
							new_cube[n_idx[0]+1][n_idx[1]+1][n_idx[2]+1] = '#'
						else:
							new_cube[n_idx[0]+1][n_idx[1]+1][n_idx[2]+1] = '.'

	return new_cube

def count_active(cube):
	count = 0
	for plane in cube:
		for row in plane:
			for cell in row:
				if cell == '#':
					count+=1
	return count

def part1():
	input = read_file()

	cube = [input]
	print(cube)
	for i in range(6):
		cube = live(cube)
		print('live{}'.format(i))
		print(cube)

	return count_active(cube)

def part2():
	return

print('part 1 answer: {}'.format(part1()))
print('part 2 answer: {}'.format(part2()))
