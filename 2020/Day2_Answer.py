from collections import Counter 

class Solution:
	def __init__(self):
		self.input = list()

		with open('Day2_input', 'r') as file:
			self.input = file.readlines()

	def run_part1(self):
		valid_pass_no = 0

		for line in self.input:
			line = line.strip()
			parts = line.split(' ')
			counter = Counter(parts[2])
			min_count = int(parts[0].split('-')[0])
			max_count = int(parts[0].split('-')[1])
			char_count = counter[parts[1][0]]
			if char_count >= min_count and char_count <= max_count:
				valid_pass_no += 1

		return valid_pass_no

			
	def run_part2(self):
		valid_pass_no = 0

		for line in self.input:
			line = line.strip()
			parts = line.split(' ')
			index1 = int(parts[0].split('-')[0])
			index2 = int(parts[0].split('-')[1])
			password = parts[2]
			char1 = password[index1-1]
			char2 = password[index2-1]
			test_char = parts[1][0]	
		
			if (char1 == test_char) != (char2 == test_char):
				valid_pass_no += 1

		return valid_pass_no

s = Solution()
print(s.run_part1())
print(s.run_part2())