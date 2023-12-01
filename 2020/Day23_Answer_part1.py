from collections import defaultdict
import copy


def get_rot_sub(input_list, start_i, end_i):
	if end_i - start_i > len(input_list):
		print("WTF!!!")
		panic()

	if start_i < end_i and end_i < len(input_list):
		return (input_list[start_i:end_i], (start_i, end_i))

	new_end = end_i%len(input_list)
	new_start = start_i%len(input_list)

	if new_start < new_end :
		return (input_list[new_start:new_end], (new_start, new_end))
	new_list = input_list[new_start:]
	new_list += input_list[:new_end]

	return (new_list,(new_start, new_end))

def find_with_val_and_not_in(cups, val, exclude_list):
	max_val = max(cups)
	if val == 0:
		val = max_val

	while val in exclude_list:
		val -=1
		if val == 0:
			val = max_val

	for i, cup in enumerate(cups):
		if val == cup:
			return i

def not_in_range(i, start, end):
	if start<end:
		if i >= start and i <= end:
			return False
		return True

	if i < start or i > end:
		return False
	return True

def get_new_indexes(start, length):
	result = [-1] * length
	result_i = 0
	for i in range(start, length):
		result[result_i] = i
		result_i+=1

	for i in range(length-result_i):
		resut[result_i] = i
		result_i+=1
	return result

def rotate_cups(cups, cur_idx, dest_cup_i, pickup_start):
	# get_new_indexes(cur_idx, len(cups))


	length = len(cups)
	result = [-1] * length
	result_i = 0
	not_seen_dest = True
	for i in range(length):
		new_i = (cur_idx+i)%length
		if not_in_range(new_i, pickup_start, (pickup_start+2)%length) and not_seen_dest:
			result[result_i] = cups[(cur_idx+i)%length]
			result_i+=1
		if new_i == dest_cup_i:
			not_seen_dest = False

	if result_i == 0:
		result[0] = cups[dest_cup_i]
		result_i+=1

	result[result_i] = cups[pickup_start]
	result_i+=1
	result[result_i] = cups[(pickup_start+1)%len(cups)]
	result_i+=1
	result[result_i] = cups[(pickup_start+2)%len(cups)]
	result_i+=1

	if result_i < len(cups):
		for cup in cups[dest_cup_i:]:
			if cup not in result:
				result[result_i] = cup
				result_i+=1
		for cup in cups[:dest_cup_i]:
			if cup not in result:
				result[result_i] = cup
				result_i+=1

	# print("new list before rotate pass {}".format(result))

	for i, cup in enumerate(result):
		if cup == cups[cur_idx]:
			rotate_by = cur_idx-i
	result =  result[-rotate_by:] + result[:-rotate_by]
	return result

def part1(cup_label):
	cups = list()
	for char in cup_label:
		cup = int(char)
		cups.append(cup)

	length = len(cups)
	
	for i in range(100):
		print("pass " + str(i+1))
		print(cups)
		cur_idx = i % length
		cur_cup = cups[cur_idx]

		pick_up, pick_up_range = get_rot_sub(cups, cur_idx+1, cur_idx+4)

		dest_cup_i = find_with_val_and_not_in(cups, cur_cup-1, pick_up)

		cups = rotate_cups(cups, cur_idx, dest_cup_i, pick_up_range[0])
		cur_idx+=1

	print(cups)

print('part 1 answer: {}'.format(part1('872495136')))
