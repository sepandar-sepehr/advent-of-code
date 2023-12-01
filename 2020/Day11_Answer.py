class Solution:
	def __init__(self):
		self.input = list()
		with open('Day11_input', 'r') as file:
			self.input = [self.split(line.strip()) for line in file.readlines()]
		print(self.input)

	def split(self, word):
		return [char for char in word]

	def count_adjacent_occ(self, input, i, j):
		count = 0
		if i > 0:
			if input[i-1][j] == '#':
				count += 1

			if j > 0: 
				if input[i-1][j-1] == '#':
					count += 1

			if j < len(input[0])-1:
				if input[i-1][j+1] == '#':
					count += 1

		if i < len(input)-1:
			if input[i+1][j] == '#':
				count += 1

			if j > 0:
				if input[i+1][j-1] == '#':
					count += 1

			if j < len(input[0])-1:
				if input[i+1][j+1] == '#':
					count += 1

		if j > 0:
			if input[i][j-1] == '#':
				count += 1

		if j< len(input[0])-1:
			if input[i][j+1] == '#':
				count += 1

		return count

	def count_diag_occ(self, input, i, j):
		count = 0
		if i > 0:
			see_1 = False
			for k in range(1, i+1):
				if not see_1:
					if input[i-k][j] == '#':
						see_1 = True
						count += 1
					if input[i-k][j] == 'L':
						see_1 = True

			see_1 = False
			for k in range(1, i+1):
				if j-k >= 0: 
					if not see_1:
						if input[i-k][j-k] == '#':
							see_1 = True
							count += 1
						if input[i-k][j-k] == 'L':
							see_1 = True

			see_1 = False
			for k in range(1, i+1):
				if j+k < len(input[0]):
					if not see_1:
						if input[i-k][j+k] == '#':
							see_1 = True
							count += 1
						if input[i-k][j+k] == 'L':
							see_1 = True


		if i < len(input)-1:
			see_1 = False
			for k in range(1, len(input)-i):
				if not see_1:
					if input[i+k][j] == '#':
						see_1 = True
						count += 1
					if input[i+k][j] == 'L':
						see_1 = True


			see_1 = False
			for k in range(1, len(input)-i):
				if not see_1:
					if j-k >= 0:
						if input[i+k][j-k] == '#':
							see_1 = True
							count += 1
						if input[i+k][j-k] == 'L':
							see_1 = True

			see_1 = False
			for k in range(1, len(input)-i):
				if j+k < len(input[0]):
					if not see_1:
						if input[i+k][j+k] == '#':
							see_1 = True
							count += 1
						if input[i+k][j+k] == 'L':
							see_1 = True

		if j > 0:
			see_1 = False
			for k in range(1, j+1):
				if not see_1:
					if input[i][j-k] == '#':
						see_1 = True
						count += 1
					if input[i][j-k] == 'L':
						see_1 = True

		if j < len(input[0])-1:
			see_1 = False
			for k in range(1, len(input[0])-j):
				if not see_1:
					if input[i][j+k] == '#':
						see_1 = True
						count += 1
					if input[i][j+k] == 'L':
						see_1 = True

		return count

	def shuffle(self, input):
		new_map = list()
		for i, line in enumerate(input):
			new_list = list()
			new_map.append(new_list)
			for j, char in enumerate(line): 
				if char == 'L':
					if self.count_adjacent_occ(input, i, j) == 0:
						new_map[i].append('#')
					else:
						new_map[i].append('L')
				elif char == '#':
					if self.count_adjacent_occ(input, i, j) >= 4:
						new_map[i].append('L')
					else:
						new_map[i].append('#')
				elif char == '.':
					new_map[i].append('.')
				else:
					print("WTF!!!")

		return new_map

	def shuffle_2(self, input):
		new_map = list()
		for i, line in enumerate(input):
			new_list = list()
			new_map.append(new_list)
			for j, char in enumerate(line): 
				if char == 'L':
					if self.count_diag_occ(input, i, j) == 0:
						new_map[i].append('#')
					else:
						new_map[i].append('L')
				elif char == '#':
					if self.count_diag_occ(input, i, j) >= 5:
						new_map[i].append('L')
					else:
						new_map[i].append('#')
				elif char == '.':
					new_map[i].append('.')
				else:
					print("WTF!!!")

		return new_map

	def match(self, prev_map, new_map):
		for i, line in enumerate(prev_map):
			for j, char in enumerate(line):
				if char != new_map[i][j]:
					return False

		return True

	def copy_matrix(self, old_matrix):
		new_matrix = list()
		for i, line in enumerate(old_matrix):
			new_matrix.append(list())
			for j, char in enumerate(line):
				new_matrix[i].append(char)

		return new_matrix

	def count_occ(self, matrix):
		count = 0
		for i, line in enumerate(matrix):
			for j, char in enumerate(line):
				if char == '#':
					count += 1

		return count

	def part1(self):
		prev_map = self.input
		while True:
			new_map = self.shuffle(prev_map)
			if self.match(prev_map, new_map):
				return self.count_occ(new_map)

			prev_map = self.copy_matrix(new_map)


	def part2(self):
		prev_map = self.input
		while True:
			new_map = self.shuffle_2(prev_map)
			if self.match(prev_map, new_map):
				return self.count_occ(new_map)
			prev_map = self.copy_matrix(new_map)


s = Solution()
# print('part 1 answer: {}'.format(s.part1()))
print('part 2 answer: {}'.format(s.part2()))
