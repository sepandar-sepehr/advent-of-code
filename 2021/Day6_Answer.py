from collections import defaultdict

# cur_state = [3,4,3,1,2]
cur_state = [5,1,1,5,4,2,1,2,1,2,2,1,1,1,4,2,2,4,1,1,1,1,1,4,1,1,1,1,1,5,3,1,4,1,1,1,1,1,4,1,5,1,1,1,4,1,2,2,3,1,5,1,1,5,1,1,5,4,1,1,1,4,3,1,1,1,3,1,5,5,1,1,1,1,5,3,2,1,2,3,1,5,1,1,4,1,1,2,1,5,1,1,1,1,5,4,5,1,3,1,3,3,5,5,1,3,1,5,3,1,1,4,2,3,3,1,2,4,1,1,1,1,1,1,1,2,1,1,4,1,3,2,5,2,1,1,1,4,2,1,1,1,4,2,4,1,1,1,1,4,1,3,5,5,1,2,1,3,1,1,4,1,1,1,1,2,1,1,4,2,3,1,1,1,1,1,1,1,4,5,1,1,3,1,1,2,1,1,1,5,1,1,1,1,1,3,2,1,2,4,5,1,5,4,1,1,3,1,1,5,5,1,3,1,1,1,1,4,4,2,1,2,1,1,5,1,1,4,5,1,1,1,1,1,1,1,1,1,1,3,1,1,1,1,1,4,2,1,1,1,2,5,1,4,1,1,1,4,1,1,5,4,4,3,1,1,4,5,1,1,3,5,3,1,2,5,3,4,1,3,5,4,1,3,1,5,1,4,1,1,4,2,1,1,1,3,2,1,1,4]

def iterate_fish(cur_state, n):
	for i in range(n):
		new_timers = 0
		for j, timer in enumerate(cur_state):
			if timer == 0:
				new_timers += 1
				cur_state[j] = 6
			else:
				cur_state[j] -= 1
		cur_state += [8 for j in range(new_timers)]
	return len(cur_state)

print(iterate_fish(cur_state.copy(), 80))


def iterate_fish_fast(init_state, n):
	timer_to_count_map = defaultdict(int)
	for init_timer in init_state:
		timer_to_count_map[init_timer] += 1
	
	for i in range(n):
		new_timer_to_count_map = defaultdict(int)
		new_timer_to_count_map[6] = timer_to_count_map[0]
		new_timer_to_count_map[8] = timer_to_count_map[0]
		for i in range(1, 9):
			new_timer_to_count_map[i-1] += timer_to_count_map[i]
		timer_to_count_map = new_timer_to_count_map

	total = 0
	for i in range(9):
		total += timer_to_count_map[i]
	return total

	# state_with_1_start = [0]
	# for i in range(n):
	# 	new_timers = 0
	# 	for j, timer in enumerate(state_with_1_start):
	# 		if timer == 0:
	# 			new_timers += 1
	# 			state_with_1_start[j] = 6
	# 		else:
	# 			state_with_1_start[j] -= 1
	# 	for j in range(new_timers):
	# 		state_with_1_start.append(8)
	# 	# state_with_1_start += [8 for j in range(new_timers)]
	# 	if i > n-8:
	# 		day_to_count_map[i] = len(state_with_1_start)
	# 	print(i, len(state_with_1_start))

	# total = 0	
	# for init_timer in init_state:
	# 	total += day_to_count_map[n-init_timer-1]
	# return total


print(iterate_fish_fast(cur_state.copy(), 256))
