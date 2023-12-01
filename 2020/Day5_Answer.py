class Solution:
	def __init__(self):
		self.input = list()
		self.map = list()
		with open('Day5_input', 'r') as file:
			self.input = file.readlines()

		for line in self.input:
			line = line.strip()
			self.map.append((line[:-3], line[-3:]))

	def part1(self):
		highest_id = 0
		for seat in self.map:
			r = range(0, 127)
			row = -1
			for char in seat[0]:
				cur_low = r[0]
				cur_high = r[-1] + 1
				rem_len = cur_high - cur_low
				if char == 'B':
					new_low = cur_low + (rem_len // 2) + 1
					r = range(new_low, cur_high)
					if new_low == cur_high:
						row = new_low
				elif char == 'F':
					new_high = cur_high - (rem_len // 2) - 1
					r = range(cur_low, new_high)
					if new_high == cur_low:
						row = cur_low

			print(row)

			col = -1
			r = range(0, 7)
			for char in seat[1]:
				cur_low = r[0]
				cur_high = r[-1] + 1
				rem_len = cur_high - cur_low
				if char == 'R':
					new_low = cur_low + (rem_len // 2) + 1
					r = range(new_low, cur_high)
					if new_low == cur_high:
						col = new_low
				elif char == 'L':
					new_high = cur_high - (rem_len // 2) - 1
					r = range(cur_low, new_high)
					if new_high == cur_low:
						col = cur_low

			print(col)
			s_id = row * 8 + col
			if highest_id < s_id:
				highest_id = s_id

		return highest_id

	def part2(self):
		seat_ids = list()
		for seat in self.map:
			r = range(0, 127)
			row = -1
			for char in seat[0]:
				cur_low = r[0]
				cur_high = r[-1] + 1
				rem_len = cur_high - cur_low
				if char == 'B':
					new_low = cur_low + (rem_len // 2) + 1
					r = range(new_low, cur_high)
					if new_low == cur_high:
						row = new_low
				elif char == 'F':
					new_high = cur_high - (rem_len // 2) - 1
					r = range(cur_low, new_high)
					if new_high == cur_low:
						row = cur_low


			col = -1
			r = range(0, 7)
			for char in seat[1]:
				cur_low = r[0]
				cur_high = r[-1] + 1
				rem_len = cur_high - cur_low
				if char == 'R':
					new_low = cur_low + (rem_len // 2) + 1
					r = range(new_low, cur_high)
					if new_low == cur_high:
						col = new_low
				elif char == 'L':
					new_high = cur_high - (rem_len // 2) - 1
					r = range(cur_low, new_high)
					if new_high == cur_low:
						col = cur_low

			s_id = row * 8 + col
			seat_ids.append(s_id)

		for i in range(59, 905):
			if i not in seat_ids:
				print(i)
		seat_ids.sort()
		print(seat_ids)
		return len(seat_ids)

s = Solution()
print(s.part2())