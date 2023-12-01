class Solution:
	def __init__(self):
		self.input = list()
		with open('Day6_input', 'r') as file:
			self.input = file.readlines()

	def part1(self):
		counts = list()
		ans_count = set()
		for line in self.input:
			ans = line.strip()
			for char in ans:
				ans_count.add(char)
			# print (ans)
			# print(ans_count)
			if line == "\n":
				counts.append(len(ans_count))
				# print(len(ans_count))
				ans_count = set()

		counts.append(len(ans_count))
		# print(len(ans_count))
		tot = 0
		for count in counts:
			tot += count
		return tot

	def count_chars(self, char_map, n):
		answers = 0
		print(char_map)
		print(n)
		for k in char_map:
			if char_map[k] == n:
				answers += 1
		print(answers)
		return answers

	def part2(self):
		counts = list()
		ans_count = {}
		line_no = 0
		for line in self.input:
			ans = line.strip()
			for char in ans:
				if char not in ans_count:
					ans_count[char] = 1
				else:
					ans_count[char] += 1
			print(ans)
			print(ans_count)
			line_no += 1
			if line == "\n":
				counts.append(self.count_chars(ans_count, line_no-1))
				# print(counts)
				ans_count = {}
				line_no = 0

		counts.append(self.count_chars(ans_count, line_no))
		print(counts)
		tot = 0
		for count in counts:
			tot += count
		return tot


s = Solution()
print(s.part1())
print(s.part2())