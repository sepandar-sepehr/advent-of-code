class Solution:
	def __init__(self):
		self.input = list()
		with open('Day12_input', 'r') as file:
			self.input = [self.split(line.strip()) for line in file.readlines()]
		print(self.input)
		self.direction = 0
		self.x = 0
		self.y = 0
		self.way_x = 10
		self.way_y = -1

	def split(self, line):
		return (line[:1], int(line[1:]))


	def run_instruction(self, instruction):
		if instruction[0] == 'L':
			self.direction = (self.direction - instruction[1])%360
		elif instruction[0] == 'R':
			self.direction = (self.direction + instruction[1])%360
		elif instruction[0] == 'N':
			self.x -= instruction[1]
		elif instruction[0] == 'S':
			self.y += instruction[1]
		elif instruction[0] == 'E':
			self.x += instruction[1]
		elif instruction[0] == 'W':
			self.y -= instruction[1]
		elif instruction[0] == 'F':
			if self.direction == 0:
				self.x += instruction[1]
			elif self.direction == 90:
				self.y += instruction[1]
			elif self.direction == 180:
				self.x -= instruction[1]
			elif self.direction == 270:
				self.y -= instruction[1]
			else:
				print("WTF!!")
		else:
			print("WTF!")

	def part1(self):
		for instruction in self.input:
			self.run_instruction(instruction)
		
		return abs(self.x) + abs(self.y)

	def run_instruction2(self, instruction):
		if instruction[0] == 'L':
			if instruction[1] == 90:
				temp = self.way_x
				self.way_x = self.way_y
				self.way_y = -temp
			elif instruction[1] == 180:
				self.way_x = (-self.way_x)
				self.way_y = (-self.way_y)
			elif instruction[1] == 270:
				temp = self.way_y
				self.way_y = self.way_x
				self.way_x = -temp
			else:
				print("WTF!!!")
		elif instruction[0] == 'R':
			if instruction[1] == 90:
				temp = self.way_y
				self.way_y = self.way_x
				self.way_x = -temp
			elif instruction[1] == 180:
				self.way_x = (-self.way_x)
				self.way_y = (-self.way_y)
			elif instruction[1] == 270:
				temp = self.way_x
				self.way_x = self.way_y
				self.way_y = -temp
			else:
				print("WTF!!!")

		elif instruction[0] == 'N':
			self.way_y -= instruction[1]
		elif instruction[0] == 'S':
			self.way_y += instruction[1]
		elif instruction[0] == 'E':
			self.way_x += instruction[1]
		elif instruction[0] == 'W':
			self.way_x -= instruction[1]
		elif instruction[0] == 'F':
			print(self.way_x, self.way_y)
			self.x += instruction[1] * self.way_x
			self.y += instruction[1] * self.way_y	
			print(self.x, self.y)			
		else:
			print("WTF!")

	def part2(self):
		self.direction = 0
		self.x = 0
		self.y = 0
		for instruction in self.input:
			self.run_instruction2(instruction)
		
		return abs(self.x) + abs(self.y)


s = Solution()
print('part 1 answer: {}'.format(s.part1()))
print('part 2 answer: {}'.format(s.part2()))
