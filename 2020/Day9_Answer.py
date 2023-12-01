class Solution:
	def __init__(self):
		self.input = list()
		with open('Day9_input', 'r') as file:
			self.input = [int(line.strip()) for line in file.readlines()]

	def is_in_last25(self, nums, val):
		i = len(nums) - 25
		while i < len(nums):
			j = len(nums) - 25
			while j < len(nums):
				if i != j:
					if nums[i] + nums[j] == val:
						return True
				j += 1

			i += 1

		return False

	def part1(self):
		nums = list()
		for i in range(0, 25):
			nums.append(self.input[i])

		i = 25
		while i < len(self.input):
			val = self.input[i]
			if not self.is_in_last25(nums, val):
				return val

			nums.append(val)
			i += 1

	def sub_matches(self, i, val):
		sum = 0
		for j in range(i, len(self.input)):
			sum += self.input[j]
			if sum > val:
				return False
			if sum == val:
				return j

	def part2(self):
		for i in range(0, len(self.input)):
			sub_match = self.sub_matches(i, 393911906) 
			if sub_match != False:
				new_list = list()
				for j in range(i, sub_match):
					new_list.append(self.input[j])

				return min(new_list) + max(new_list)
			
		return

s = Solution()
print('part 1 answer: {}'.format(s.part1()))
print('part 2 answer: {}'.format(s.part2()))
