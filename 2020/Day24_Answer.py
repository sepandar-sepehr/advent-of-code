from collections import defaultdict

def read_line(line):
	result = list()
	buf = ''
	for char in line:
		if buf != '':
			result.append(buf+char)
			buf = ''
		elif char == 's' or char == 'n':
			buf = char
		else:
			result.append(char)
			buf = ''
	return result

def part1():
	with open('Day24_input', 'r') as file:
		input = [read_line(line.strip()) for line in file.readlines()]

	tiles = get_tiles(input)

	tile_map = defaultdict(bool)
	for tile in tiles:
		if tile_map[tile] == False:
			tile_map[tile] = True
		elif tile_map[tile] == True:
			tile_map[tile] = False

	count = 0
	print(tile_map.keys())
	print(len(tile_map.keys()))
	for tile, val in tile_map.items():
		if val == True:
			count += 1

	return count

def get_tiles(input):
	tiles = list()
	for insts in input:
		tile_loc = (0,0)
		for inst in insts:
			if inst == 'sw':
				tile_loc = (tile_loc[0]-1, tile_loc[1]-1)
			elif inst == 'se':
				tile_loc = (tile_loc[0]+1, tile_loc[1]-1)
			elif inst == 'e':
				tile_loc = (tile_loc[0]+2, tile_loc[1])
			elif inst == 'ne':
				tile_loc = (tile_loc[0]+1, tile_loc[1]+1)
			elif inst == 'nw':
				tile_loc = (tile_loc[0]-1, tile_loc[1]+1)
			elif inst == 'w':
				tile_loc = (tile_loc[0]-2, tile_loc[1])
			else:
				print(inst)
				panic()
		tiles.append(tile_loc)

	return tiles


def get_blacks(tiles):
	tile_map = defaultdict(bool)
	for tile in tiles:
		if tile_map[tile] == False:
			tile_map[tile] = True
		elif tile_map[tile] == True:
			tile_map[tile] = False

	blacks = list()
	for tile, val in tile_map.items():
		if val == True:
			blacks.append(tile)
	return blacks

def get_neighbours(tile):
	return [
		(tile[0]-1, tile[1]-1),
		(tile[0]+1, tile[1]-1),
		(tile[0]+2, tile[1]),
		(tile[0]+1, tile[1]+1),
		(tile[0]-1, tile[1]+1),
		(tile[0]-2, tile[1]),
	]

def part2():
	with open('Day24_input', 'r') as file:
		input = [read_line(line.strip()) for line in file.readlines()]
	
	tiles = get_tiles(input)
	blacks = set(get_blacks(tiles))

	for i in range(100):
		new_blacks = set()
		for black in blacks:
			neighbours = get_neighbours(black)
			black_neighbours = [n for n in neighbours if n in blacks]
			if len(black_neighbours) == 1 or len(black_neighbours) == 2:
				new_blacks.add(black)

			for nei in neighbours:
				if nei not in blacks:
					new_neis = get_neighbours(nei)
					black_neighbours = [n for n in new_neis if n in blacks]
					if len(black_neighbours) == 2:
						new_blacks.add(nei)					
					# check while rule, track checked

		blacks = new_blacks

	return len(new_blacks)


print('part 1 answer: {}'.format(part1()))
print('part 2 answer: {}'.format(part2()))
