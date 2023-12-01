def read_file():
	with open('Day17_input', 'r') as file:
		input = [[list(line.strip()) for line in file.readlines()]]	
	return input

IDXS = [
	(0,0,0,-1), (0,0,0,1), 
	(0,0,1,-1), (0,0,1,1), (0,0,1,0),
	(0,0,-1,-1), (0,0,-1,1), (0,0,-1,0), 

	(0,1,0,-1), (0,1,0,1), (0,1,0,0),
	(0,1,1,-1), (0,1,1,1), (0,1,1,0),
	(0,1,-1,-1), (0,1,-1,1), (0,1,-1,0),

	(0,-1,0,-1), (0,-1,0,1), (0,-1,0,0),
	(0,-1,1,-1), (0,-1,1,1), (0,-1,1,0),
	(0,-1,-1,-1), (0,-1,-1,1), (0,-1,-1,0),

	(1,0,0,-1), (1,0,0,1), (1,0,0,0),
	(1,0,1,-1), (1,0,1,1), (1,0,1,0),
	(1,0,-1,-1), (1,0,-1,1), (1,0,-1,0), 

	(1,1,0,-1), (1,1,0,1), (1,1,0,0),
	(1,1,1,-1), (1,1,1,1), (1,1,1,0),
	(1,1,-1,-1), (1,1,-1,1), (1,1,-1,0),

	(1,-1,0,-1), (1,-1,0,1), (1,-1,0,0),
	(1,-1,1,-1), (1,-1,1,1), (1,-1,1,0),
	(1,-1,-1,-1), (1,-1,-1,1), (1,-1,-1,0),

	(-1,0,0,-1), (-1,0,0,1), (-1,0,0,0),
	(-1,0,1,-1), (-1,0,1,1), (-1,0,1,0),
	(-1,0,-1,-1), (-1,0,-1,1), (-1,0,-1,0), 

	(-1,1,0,-1), (-1,1,0,1), (-1,1,0,0),
	(-1,1,1,-1), (-1,1,1,1), (-1,1,1,0),
	(-1,1,-1,-1), (-1,1,-1,1), (-1,1,-1,0),

	(-1,-1,0,-1), (-1,-1,0,1), (-1,-1,0,0),
	(-1,-1,1,-1), (-1,-1,1,1), (-1,-1,1,0),
	(-1,-1,-1,-1), (-1,-1,-1,1), (-1,-1,-1,0)
]

def get_neighbour_idx(i, j, k, w):
	neighbours = [None] * 80
	for i2, idx in enumerate(IDXS):
		neighbours[i2] = (i+idx[0], j+idx[1], k+idx[2], w+idx[3])
	return neighbours

def get_neighbours(hcube, ijkw):
	i = ijkw[0]
	j = ijkw[1]
	k = ijkw[2]
	w = ijkw[3]
	neighbours = [None] * 80
	for i2, idx in enumerate(IDXS):
		new_i = i+idx[0]
		new_j = j+idx[1]
		new_k = k+idx[2]
		new_w = w+idx[3]
		if new_i >= 0 and new_j >= 0 and new_k >= 0 and new_w >= 0 and new_w < len(hcube[0][0][0]) and new_k < len(hcube[0][0]) and new_j < len(hcube[0]) and new_i < len(hcube):
			neighbours[i2] = hcube[new_i][new_j][new_k][new_w]
		else:
			neighbours[i2] = '.'
	return neighbours

def count_actives(neighbours):
	count = 0
	for n in neighbours:
		if n == '#':
			count+=1 
	return count

def live(hcube):
	new_hcube = list()
	for i in range(len(hcube)+2):
		cube = list()
		for j in range(len(hcube[0])+2):
			plane = list()
			for k in range(len(hcube[0][0])+2):
				plane.append([None]*(len(hcube[0][0][0])+2))
			cube.append(plane)
		new_hcube.append(cube)

	for i, cube in enumerate(hcube):
		for j, plane in enumerate(cube):
			for k, row in enumerate(plane):
				for w, cell in enumerate(row):
					if cell == '#':
						neighbours = get_neighbours(hcube, (i, j, k, w))
						active_count = count_actives(neighbours)
						if active_count == 2 or active_count == 3:
							new_hcube[i+1][j+1][k+1][w+1] = '#'
					
					indices = get_neighbour_idx(i, j, k, w)
					for n_idx in indices:
						if new_hcube[n_idx[0]+1][n_idx[1]+1][n_idx[2]+1][n_idx[3]+1] == None:
							neighbours = get_neighbours(hcube, n_idx)
							active_count = count_actives(neighbours)
							if active_count == 3:
								new_hcube[n_idx[0]+1][n_idx[1]+1][n_idx[2]+1][n_idx[3]+1] = '#'
							else:
								new_hcube[n_idx[0]+1][n_idx[1]+1][n_idx[2]+1][n_idx[3]+1] = '.'

	return new_hcube

def count_active(hypercube):
	count = 0
	for cube in hypercube:
		for plane in cube:
			for row in plane:
				for cell in row:
					if cell == '#':
						count+=1
	return count

def part2():
	input = read_file()

	hcube = [input]
	for i in range(6):
		hcube = live(hcube)
		print('live{}'.format(i))

	return count_active(hcube)

print('part 2 answer: {}'.format(part2()))
