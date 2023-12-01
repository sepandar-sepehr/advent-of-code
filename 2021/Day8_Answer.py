from collections import defaultdict

signal_input = []
with open('d8_input', 'r') as file:
	for line in file:
		signal_patterns = line.split(' | ')[0].split()
		output_values = line.split(' | ')[1].split()
		signal_input.append((signal_patterns, output_values))


total = 0
for signal in signal_input:
	for output in signal[1]:
		out_len = len(output)
		if out_len in [2, 3, 4, 7]:
			total += 1
print(total)

### part 2
def has_str(main_str, sub_str):
	return all((c in main_str) for c in sub_str)

def decode(signal_patterns):
	digits_map = defaultdict(str)
	digits_map_rev = defaultdict(int)

	for pattern in signal_patterns:
		if len(pattern) == 7:
			digits_map[pattern] = 8
			digits_map_rev[8] = pattern
		elif len(pattern) == 4:
			digits_map[pattern] = 4
			digits_map_rev[4] = pattern
		elif len(pattern) == 3:
			digits_map[pattern] = 7
			digits_map_rev[7] = pattern
		elif len(pattern) == 2:
			digits_map[pattern] = 1
			digits_map_rev[1] = pattern
	
	# find 0,6,9 (size 6)
	for pattern in signal_patterns:
		if len(pattern) == 6:
			digit_4_pattern = digits_map_rev[4]
			is_9 = has_str(pattern, digit_4_pattern)
			
			if is_9:
				digits_map[pattern] = 9
				digits_map_rev[9] = pattern
			
			else:				
				digit_1_pattern = digits_map_rev[1]
				is_0 = has_str(pattern, digit_1_pattern)

				if is_0:
					digits_map[pattern] = 0
					digits_map_rev[0] = pattern
				else:
					digits_map[pattern] = 6
					digits_map_rev[6] = pattern

	# 2, 5, 3 (size 5)
	for pattern in signal_patterns:
		if len(pattern) == 5:
			digit_6_pattern = digits_map_rev[6]
			is_5 = has_str(digit_6_pattern, pattern)
			if is_5:
				digits_map[pattern] = 5
			else:
				digit_9_pattern = digits_map_rev[9]
				is_3 = has_str(digit_9_pattern, pattern)
				if is_3:
					digits_map[pattern] = 3
				else:
					digits_map[pattern] = 2

	return digits_map


def match_pattern(str1, str2):
	return all((c in str1) for c in str2) and all((c in str2) for c in str1)

total = 0
for signal in signal_input:
	digits_map = decode(signal[0])
	print(digits_map)
	output_str = ""
	for output in signal[1]:
		for pattern in digits_map.keys():
			if match_pattern(pattern, output):
				output_str += str(digits_map[pattern])
	print(output_str)
	total += int(output_str)

print(total)
