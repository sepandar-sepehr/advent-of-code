input_nums = list()
with open('d1_input', 'r') as file:
	for line in file:
		input_nums.append(int(line))

def part1():
	count = 0
	prev = input_nums[0]
	for i in input_nums:
		if i > prev:
			count += 1
		prev = i

	print(count)

def part2():
	count = 0
	prev = input_nums[0]
	for i in range(1, len(input_nums)-2):
		if input_nums[i+2] > prev:
			count += 1
		prev = input_nums[i]
	print(count)

part1()
part2()