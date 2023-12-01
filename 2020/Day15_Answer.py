from collections import defaultdict

class Solution:
	def __init__(self):
		self.input = list()
		with open('Day15_input', 'r') as file:
			line = file.readlines()[0]
			self.input = line.split(',')
		print(self.input)


	def part1(self):
		seen_nums = [int(x) for x in self.input]
		
		i = len(seen_nums)
		while i != 2020:
			last = seen_nums[-1]
			occurances = [j for j,num in enumerate(seen_nums) if num == last]
			if len(occurances) == 1:
				seen_nums.append(0)
			else:
				seen_nums.append(occurances[-1]-occurances[-2])
			i+=1

		return seen_nums[-1]

	def part2(self):
		seen_nums = defaultdict(list)
		for i, x in enumerate(self.input):
			seen_nums[int(x)].append(i)

		last = int(self.input[-1])

		i = len(self.input)
		while i != 30000000:
			occurances = seen_nums[last]
			# print(occurances)
			# print(last)
			if len(occurances) == 1:
				seen_nums[0].append(i)
				last = 0
			else:
				new_val = occurances[-1]-occurances[-2]
				seen_nums[new_val].append(i)
				last = new_val
			i+=1

		return last


s = Solution()
print('part 1 answer: {}'.format(s.part1()))
print('part 2 answer: {}'.format(s.part2()))
