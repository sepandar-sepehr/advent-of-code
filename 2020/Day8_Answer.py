class Solution:
	def __init__(self):
		self.input = list()
		with open('Day8_input', 'r') as file:
			self.input = file.readlines()

		self.instructions = list()
		for line in self.input:
			ins_line = line.strip().split(' ')
			self.instructions.append((ins_line[0], ins_line[1]))
		print(self.instructions)

	def run_instruction(self, instruction, current_line):
		if instruction[0] == 'nop':
			return current_line + 1
		elif instruction[0] == 'jmp':
			if instruction[1][:1] == '+':
				return current_line + int(instruction[1][1:])
			else:
				return current_line - int(instruction[1][1:])
		else:
			if instruction[1][:1] == '+':
				self.global_val += int(instruction[1][1:])
			else:
				self.global_val -= int(instruction[1][1:])
			return current_line + 1


	def part1(self):
		visited_lines = list()
		self.global_val = 0
		next_line = 0
		while next_line not in visited_lines:
			instruction = self.instructions[next_line]
			visited_lines.append(next_line)
			next_line = self.run_instruction(instruction, next_line)

		return self.global_val

	def is_looped(self):
		visited_lines = list()
		next_line = 0
		while (next_line not in visited_lines) and (next_line < len(self.input)):
			instruction = self.instructions[next_line]
			visited_lines.append(next_line)
			next_line = self.run_instruction(instruction, next_line)
		
		print(next_line)
		if next_line != len(self.input):
			return True

		return False

	def part2(self):
		next_line = 0
		not_found = True
		while not_found:
			instruction = self.instructions[next_line]
			if instruction[0] == 'nop':
				self.instructions[next_line] = ('jmp', instruction[1])
			
				if self.is_looped():
					self.instructions[next_line] = ('nop', instruction[1])
				else:
					not_found = False

			if instruction[0] == 'jmp':
				self.instructions[next_line] = ('nop', instruction[1])

				if self.is_looped():
					self.instructions[next_line] = ('jmp', instruction[1])
				else:
					not_found = False

			if not_found:
				next_line = self.run_instruction(instruction, next_line)

		next_line = 0
		self.global_val = 0
		while next_line < len(self.input):
			instruction = self.instructions[next_line]

			next_line = self.run_instruction(instruction, next_line)


		return self.global_val

s = Solution()
print(s.part1())
print(s.part2())