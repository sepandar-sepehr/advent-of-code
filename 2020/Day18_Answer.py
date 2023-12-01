import operator

class Expression:
	def __init__(self, nums, ops):
		self.nums = nums
		self.ops = ops

	def get_nums(self):
		return self.nums

	def get_ops(self):
		return self.ops

	def print_exp(self):
		for num in self.nums:
			if isinstance(num, Expression):
				print("exp")
				num.print_exp()
			else:
				print(num)
		print(self.ops)

class Solution:
	def __init__(self):
		with open('Day18_input', 'r') as file:
			self.expressions = [self.parse(line.strip()) for line in file.readlines()]
		# for exp in self.expressions:
		# 	exp.print_exp()

	def parse(self, x):
		operators = set('+-*/')
		op_out = list()
		num_out = list()
		buff = list()
		i = 0
		while i < len(x):
			c = x[i]
			if c in operators:  
				num_out.append(''.join(buff))
				buff = list()
				op_out.append(c)
				i+=1
			elif c == '(':
				par_num = 1
				matched_par = 0
				new_buff = list()
				while matched_par != par_num:
					i+=1
					c = x[i]
					new_buff.append(c)
					if c == ')':
						matched_par +=1
					if c == '(':
						par_num += 1
				inner_exp = self.parse(new_buff)
				num_out.append(inner_exp)
			elif c == ')':
				i+=1
			elif c == ' ':
				i+=1
			else:
				buff.append(c)
				i+=1
		num_out.append(''.join(buff))
		result = list()
		for num in num_out:
			if num != '':
				result.append(num)
		return Expression(result,op_out)

	def eval(self, exp):
		nums = exp.get_nums()
		ops = exp.get_ops()
		op_dict = {'*':operator.mul,
					'/':operator.truediv,
					'+':operator.add,
					'-':operator.sub}

		while len(nums) > 1:
			oo = ops.pop(0)
			value1 = nums[0]
			value2 = nums[1]
			if isinstance(nums[0], Expression):
				value1 = self.eval(value1)
			if isinstance(nums[1], Expression):
				value2 = self.eval(value2)
			value = op_dict[oo](int(value1), int(value2))
			nums[0:2] = [value]

		return nums[0]


	def eval2(self, exp):
		nums = exp.get_nums()
		ops = exp.get_ops()
		operator_order = ('+-', '*/')
		op_dict = {'*':operator.mul,
					'/':operator.truediv,
					'+':operator.add,
					'-':operator.sub}

		for op in operator_order:
			while any(o in ops for o in op):
				idx,oo = next((i,o) for i,o in enumerate(ops) if o in op)
				value1 = nums[idx]
				value2 = nums[idx+1]
				if isinstance(nums[idx], Expression):
					value1 = self.eval2(value1)
				if isinstance(nums[idx+1], Expression):
					value2 = self.eval2(value2)
				value = op_dict[oo](int(value1), int(value2))
				ops.pop(idx)
				nums[idx:idx+2] = [value]

		return nums[0]

	def part1(self):
		value = 0
		for exp in self.expressions:
			value += self.eval(exp)
		return value

	def part2(self):
		value = 0
		for exp in self.expressions:
			value += self.eval2(exp)
		return value

s = Solution()
# print('part 1 answer: {}'.format(s.part1()))
print('part 2 answer: {}'.format(s.part2()))
