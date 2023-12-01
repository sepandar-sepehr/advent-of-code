class Solution:
	def __init__(self):
		self.input_nums = list()
		self.input_dict = dict()
		with open('Day1_input', 'r') as file:
			for line in file:
				self.input_nums.append(int(line))
				self.input_dict[int(line)] = True

	def run_part1(self):
		for num in self.input_dict.keys():
			if (2020-num) in self.input_dict:
				return num * (2020-num)

	def run_part2(self):
		for num in self.input_nums:
			for num2 in self.input_nums:
				if (2020-num-num2) in self.input_dict:
					return num * num2 * (2020-num-num2)

s = Solution()
print(s.run_part2())