import re

with open('input', 'r') as file_input:
	wind_directions = file_input.readlines()[0]
print(wind_directions)

field = [
]

rocks = {
	0: [
		['.','.','@','@','@','@', '.']
	],
	1: [
		['.','.','.','@','.','.', '.'],
		['.','.','@','@','@','.', '.'],
		['.','.','.','@','.','.', '.']
	],
	2: [
		['.','.','@','@','@','.','.'],
		['.','.','.','.','@','.','.'],
		['.','.','.','.','@','.','.'],
	],
	3: [
		['.','.','@','.','.','.','.'],
		['.','.','@','.','.','.','.'],
		['.','.','@','.','.','.','.'],
		['.','.','@','.','.','.','.']
	],
	4:[
		['.','.','@','@','.','.','.'],
		['.','.','@','@','.','.','.']
	]
}


def move_right(moving_top):
	can_move = True
	for i in range(1,5):
		idx = moving_top-i
		if idx <0:
			continue

		rightest = ''.join(field[idx]).rfind('@')
		if rightest == 6:
			can_move = False
		elif rightest != -1 and field[idx][rightest+1] != '.':
			can_move = False

	if can_move:
		for i in range(1,5):
			idx = moving_top-i
			if idx <0:
				continue
			rightest = ''.join(field[idx]).rfind('@')
			if rightest != -1:
				field[idx][rightest+1] = '@'
				leftest = ''.join(field[idx]).find('@')
				field[idx][leftest] = '.'

def move_left(moving_top):
	can_move = True
	for i in range(1,5):
		idx = moving_top-i
		if idx <0:
			continue
		leftest = ''.join(field[idx]).find('@')
		if leftest == 0:
			can_move = False
		elif leftest != -1 and field[idx][leftest-1] != '.':
			can_move = False

	if can_move:
		for i in range(1,5):
			idx = moving_top-i
			if idx <0:
				continue
			leftest = ''.join(field[idx]).find('@')
			if leftest != -1:
				field[idx][leftest-1] = '@'
				rightest = ''.join(field[idx]).rfind('@')
				field[idx][rightest] = '.'

def make_stationary(moving_top):
	for i in range(5):
		idx = moving_top-i
		if idx <0 or idx >= len(field):
			continue
		field[idx] = list(map(lambda char: char.replace('@', '#'), field[idx]))

def move_down(moving_top):
	# print('moving')
	# for j in range(len(field)):
	# 	print(field[len(field)-j-1])

	# check can move
	for i in range(4):
		idx = moving_top-4+i
		if idx <0:
			continue

		for match in re.finditer('@', ''.join(field[idx])):
			if idx == 0:
				return False

			if field[idx-1][match.start()] not in ['.','@']:
				return False


	for i in range(4):
		idx = moving_top-4+i
		if idx <0:
			continue
		for match in re.finditer('@', ''.join(field[idx])):
			field[idx][match.start()] = '.'
			field[idx-1][match.start()] = '@'

	if field[-1] ==	['.']*7:
		field.pop()

	return True

seen = {}
heights = {}
def is_repeated(direction_i, cur_i):
	heights[cur_i] = len(field)
	rock_i = cur_i%5
	if len(field) < 100:
		return False
	top = ''
	for i in range(100):
		top += ','.join(field[-i])
	if (direction_i, rock_i, top) in seen.keys():
		return seen[(direction_i, rock_i, top)]
	else:
		seen[(direction_i, rock_i, top)] = cur_i
		return False

w_i = 0
max_i = 1000000000000
for i in range(max_i):
	landed = False
	rock = rocks[i%5]
	field += [
		['.']*7,
		['.']*7,
		['.']*7
	]
	field += [row[:] for row in rock]

	moving_top = len(field)
	# print('fieldA:')
	# for j in range(len(field)):
	# 	print(field[len(field)-j-1])

	while not landed:
		direction = wind_directions[w_i%len(wind_directions)]

		w_i += 1
		if direction == '>':
			move_right(moving_top)
		else:
			move_left(moving_top)

		if not move_down(moving_top):
			landed = True
		else:
			moving_top -= 1
	
	make_stationary(moving_top)

	repeated = is_repeated(w_i%len(wind_directions), i)
	if repeated:
		cycle_length = i-repeated
		leftover_rocks = (max_i-repeated)%(cycle_length)
		repeated_h = heights[repeated]
		leftover_height = heights[leftover_rocks + repeated-1] - repeated_h
		height_change = len(field)-repeated_h
		cycles = (max_i-repeated)//cycle_length
		print("reached height:", cycles * height_change + repeated_h + leftover_height)
		exit() 

# print('field:')
# for j in range(len(field)):
# 	print(field[len(field)-j-1])


print('part1: ', len(field))
