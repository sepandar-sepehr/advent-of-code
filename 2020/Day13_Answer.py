import math

class Solution:
	def __init__(self):
		self.input = list()
		with open('Day13_input', 'r') as file:
			self.input = [line.strip() for line in file.readlines()]
		print(self.input)
		print(len(self.input[1].split(',')))

	def part1(self):
		dep_ts = int(self.input[0])
		input_buses = self.input[1].split(',')

		running_buses = list()
		for bus in input_buses:
			if bus != 'x':
				running_buses.append(int(bus))

		ts = dep_ts
		while True:
			for bus in running_buses:
				if ts % bus == 0:
					return bus * (ts - dep_ts)
			ts += 1

	def is_subs(self, ts, nums_ts, nums, use_nums):
		ts_inc = ts
		for i, num in enumerate(nums):
			if i == use_nums:
				return True

			if ts_inc % num != 0:
				return False

			if i == len(nums_ts)-1:
				return True
			else:
				ts_inc = ts + nums_ts[i+1]

		return True

	def part2(self):
		dep_ts = int(self.input[0])
		input_buses = self.input[1].split(',')

		nums = list()
		nums_ts = list()
		for ts, bus in enumerate(input_buses):
			if bus != 'x':
				nums.append(int(bus))
				nums_ts.append(ts)
		print("nums")
		print(nums)	
		print(nums_ts)

		prod = nums[0]
		used_nums = list()
		used_nums.append(nums[0])
		t = 0
		mul = 1
		i = 1
		while len(used_nums) < len(nums)+1:
			ts = t + prod * mul
			# print("t: {}".format(ts))
			mul += 1
			if self.is_subs(ts, nums_ts, nums, i+1):
				print("prod {}".format(prod))
				print("ts {}".format(ts))
				print("mul {}".format(mul))
				if i == len(nums):
					return t
				t = ts
				mul = 1
				used_nums.append(nums[i])
				prod = prod * nums[i]
				i+=1

		return t


s = Solution()
print('part 1 answer: {}'.format(s.part1()))
print('part 2 answer: {}'.format(s.part2()))
