class Solution:
	def __init__(self):
		self.input = list()
		self.map = list(list())
		with open('Day3_input', 'r') as file:
			self.input = file.readlines()

		for line in self.input:
			line = line.strip()
			self.width = len(line)
			self.map.append(self.split(line))

	def split(self, word): 
	    return [char for char in word]  

	def run_part1(self):
		x_i = 3
		tree_count = 0
		for i in range(1, len(self.map)):
			if self.map[i][x_i%self.width] == '#':
				tree_count += 1
			x_i += 3
		return tree_count

	def part2_a(self):
		x_i = 1
		tree_count = 0
		for i in range(1, len(self.map)):
			if self.map[i][x_i%self.width] == '#':
				tree_count += 1
			x_i += 1
		return tree_count

	def part2_b(self):
		x_i = 5
		tree_count = 0
		for i in range(1, len(self.map)):
			if self.map[i][x_i%self.width] == '#':
				tree_count += 1
			x_i += 5
		return tree_count

	def part2_c(self):
		x_i = 7
		tree_count = 0
		for i in range(1, len(self.map)):
			if self.map[i][x_i%self.width] == '#':
				tree_count += 1
			x_i += 7
		return tree_count

	def part2_d(self):
		x_i = 1
		tree_count = 0
		y_i = 2
		for i in range(1, len(self.map)):
			if self.map[y_i][x_i%self.width] == '#':
				tree_count += 1
			x_i += 1
			y_i += 2
			if y_i > len(self.map):
				print(tree_count)
				return tree_count
		return tree_count

	def run_part2(self):
		return self.run_part1() * self.part2_a() * self.part2_b() * self.part2_c() * self.part2_d()

s = Solution()
print(s.run_part1())
print(s.run_part2())