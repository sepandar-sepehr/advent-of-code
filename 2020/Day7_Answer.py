class Solution:
	def __init__(self):
		self.input = list()
		with open('Day7_input', 'r') as file:
			self.input = file.readlines()
		
		self.bag_map = {}
		self.bag_count_map = {}

		for line in self.input:
			l_split = line.split(' contain ')
			container = l_split[0][:-5]
			if 'no other bags' not in l_split[1]:
				bag_colors = l_split[1][:-1].split(',')
				for bag_color in bag_colors:
					bag_color = bag_color.strip()
					bc_parts = bag_color.split(' ')

					# part 2
					if container not in self.bag_count_map:
						self.bag_count_map[container] = list()
					self.bag_count_map[container].append((int(bc_parts[0]), bc_parts[1] + ' ' + bc_parts[2]))

					new_color = (bc_parts[1] + ' ' + bc_parts[2])
					if new_color not in self.bag_map:
						self.bag_map[new_color] = set()
					self.bag_map[new_color].add(container)
		print(self.bag_map)
		print(self.bag_count_map)

	def get_next_layer(self, colors, seen_bags):
		new_set = set()
		for color in colors:
			if color not in seen_bags:
				if color in self.bag_map:
					for new_color in self.bag_map[color]:
						new_set.add(new_color)
		return new_set

	def part1(self):
		outer_bags = set()

		next_layer = self.bag_map['shiny gold'].copy()
		while len(next_layer) > 0:
			prev_layer = next_layer.copy()
			next_layer = self.get_next_layer(next_layer, outer_bags)
			for color in prev_layer:
				outer_bags.add(color)

		return len(outer_bags)

	def rec_count(self, color):
		if color not in self.bag_count_map:
			return 0

		total = 0
		for new_color in self.bag_count_map[color]:
			total = total + new_color[0] + new_color[0] * self.rec_count(new_color[1])

		return total

	def part2(self):		
		return self.rec_count('shiny gold')

s = Solution()
print(s.part1())
print(s.part2())