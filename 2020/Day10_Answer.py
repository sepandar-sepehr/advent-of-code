class Solution:
	def __init__(self):
		self.input = list()
		with open('Day10_input', 'r') as file:
			self.input = [int(line.strip()) for line in file.readlines()]

	def part1(self):
		max_volt = max(self.input)
		print(max_volt)
		next = 0
		one_count = 0
		three_count = 0
		while next != (max_volt):
			if (next + 1) in self.input:
				one_count += 1
				next += 1
			elif (next + 2) in self.input:
				next += 2
				print("WTF?")
			elif (next + 3) in self.input:
				next += 3
				three_count += 1
			else:
				print("failed")

		return (one_count) * (three_count + 1)

	def count_comb(self, n):
		if n == max(self.input):
			return 1
		tot = 0
		if n+1 in self.input:
			if n+1 in self.calculated:
				tot += self.calculated[n+1]
			else:
				val = self.count_comb(n+1)
				tot += val 
				self.calculated[n+1] = val
		if n+2 in self.input:
			if n+2 in self.calculated:
				tot += self.calculated[n+2]
			else:
				val = self.count_comb(n+2)
				tot += val 
				self.calculated[n+2] = val
		if  n+3 in self.input:
			if n+3 in self.calculated:
				tot += self.calculated[n+3]
			else:
				val = self.count_comb(n+3)
				tot += val 
				self.calculated[n+3] = val

		return tot

	def part2(self):
		self.calculated = {}
		return self.count_comb(0)


s = Solution()
print('part 1 answer: {}'.format(s.part1()))
print('part 2 answer: {}'.format(s.part2()))
