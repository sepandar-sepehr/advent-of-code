from collections import defaultdict

class Solution:
	def __init__(self):
		self.input = list()
		with open('Day14_input', 'r') as file:
			self.input = [line.strip() for line in file.readlines()]
		print(self.input)
		self.mem_val = defaultdict(int)
		self.mem_map = defaultdict(set)

	def assign_val(self, mask, mem, val):
		binary = "{0:b}".format(val)
		binary64 = '0'*(36-len(binary)) + binary
		masked_val = ""
		for i in range(36):
			if mask[i] == 'X':
				masked_val += binary64[i]
			else:
				masked_val += mask[i]

		self.mem_val[mem] = masked_val

	def calc_vals(self):
		sum = 0
		for k,v in self.mem_val.items():
			sum += int(v, 2)

		return sum

	def part1(self):
		for line in self.input:
			parts = line.split(' = ')
			if parts[0] == 'mask':
				mask = parts[1]
			else: 
				mem = parts[0][4:-1]
				val = parts[1]
				self.assign_val(mask, mem, int(val))
		return self.calc_vals()

	def get_mem_adrss(self, mask, mem):
		binary = "{0:b}".format(mem)
		binary64 = '0'*(36-len(binary)) + binary
		masked_val = ""
		for i in range(36):
			if mask[i] == '0':
				masked_val += binary64[i]
			elif mask[i] == '1':
				masked_val += '1'
			else:
				masked_val += 'X'

		print(masked_val)
		return self.unmask_mem(masked_val)

	def unmask_mem(self, masked_val):
		# print(masked_val)
		if 'X' not in masked_val:
			return [masked_val]

		if masked_val in self.mem_map:
			return self.mem_map[masked_val]
			
		result = list()
		for i in range(len(masked_val)):
			if masked_val[i] == 'X':
				copy_val = masked_val[:]
				result += self.unmask_mem(masked_val[:i] + '1' + masked_val[i+1:])
				result += self.unmask_mem(masked_val[:i] + '0' + masked_val[i+1:])

		self.mem_map[masked_val] = set(result)
		return set(result)

	def calc_vals2(self):
		sum = 0
		for k,v in self.mem_val.items():
			sum += v

		return sum

	def part2(self):
		self.mem_val = defaultdict(int)

		for line in self.input:
			parts = line.split(' = ')
			if parts[0] == 'mask':
				mask = parts[1]
			else: 
				mem = parts[0][4:-1]
				val = parts[1]
				# print("hey")
				# print(mem)
				for mem_adrs in self.get_mem_adrss(mask, int(mem)):
					print("mem val: {}, {}".format(mem_adrs, val))
					self.mem_val[mem_adrs] = int(val)

		return self.calc_vals2()


s = Solution()
print('part 1 answer: {}'.format(s.part1()))
print('part 2 answer: {}'.format(s.part2()))
