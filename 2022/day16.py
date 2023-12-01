import re

v_to_v = {}
v_rates = {}
all_valves = set()
with open('input', 'r') as file_input:
	for line in file_input:
		num = int(re.findall(r'=(-?\d+)', line.strip())[0])
		v1 = re.findall(r'Valve (\w+) has flow rate=-?\d+; tunnels? leads? to valves?', line.strip())[0]
		v2s = list(map(lambda s: s.strip(), re.findall(r'Valve \w+ has flow rate=-?\d+; tunnels? leads? to valves? (.*)', line.strip())[0].split(',')))
		if num != 0:
			all_valves.add(v1)
		v_to_v[v1] = v2s
		v_rates[v1] = num

print(all_valves)
print(v_to_v)
print(v_rates)

total_pressure = 0

hashed = {}

def max_new_pressure(cur, remaining_time, open_valves):
	hash_key = cur + str(remaining_time) + '-'.join(open_valves)
	if hash_key in hashed:
		return hashed[hash_key]
	# print(cur, remaining_time, open_valves)

	if remaining_time <= 1:
		return 0

	if open_valves == all_valves:
		return 0

	max_pressure = 0
	# first next ones
	for nex_v in v_to_v[cur]:
		pressure_candidate = max_new_pressure(nex_v, remaining_time-1, open_valves.copy())
		if pressure_candidate > max_pressure:
			max_pressure = pressure_candidate

	# now opening
	if cur not in open_valves and v_rates[cur] != 0:
		pressure_from_opening = v_rates[cur] * (remaining_time-1)
		new_open_valves = open_valves.copy()
		new_open_valves.add(cur)
		# print('x')
		# print(open_valves)
		# print(new_open_valves)

		pressure_if_opened = pressure_from_opening+max_new_pressure(cur, remaining_time-1, new_open_valves)
		# print(cur, remaining_time, pressure_from_opening, pressure_if_opened)
		if pressure_if_opened > max_pressure:
			max_pressure = pressure_if_opened

	# print(cur, remaining_time, open_valves, max_pressure)
	hashed[hash_key] = max_pressure
	return max_pressure

# print('part1: ', max_new_pressure('AA', 30, set()))

hashed = {}
def max_parallel_pressure(curA, curB, remaining_time, open_valves):
	curs = [curA, curB]
	curs.sort()
	hash_key = '-'.join(curs) + str(remaining_time) + '-'.join(open_valves)
	if hash_key in hashed:
		return hashed[hash_key]
	# print(cur, remaining_time, open_valves)

	if remaining_time <= 1:
		return 0

	if open_valves == all_valves:
		return 0

	max_pressure = 0
	# first moving both
	for next_vA in v_to_v[curA]:
		for next_vB in v_to_v[curB]:
			if next_vB != next_vA:
				pressure_candidate = max_parallel_pressure(next_vA, next_vB, remaining_time-1, open_valves.copy())
				if pressure_candidate > max_pressure:
					max_pressure = pressure_candidate

	# now opening A and moving B
	if curA not in open_valves and v_rates[curA] != 0:
		pressure_from_opening = v_rates[curA] * (remaining_time-1)
		new_open_valves = open_valves.copy()
		new_open_valves.add(curA)

		for next_vB in v_to_v[curB]:
			if next_vB != curA:
				pressure_if_A_opened = pressure_from_opening+max_parallel_pressure(curA, next_vB, remaining_time-1, new_open_valves)
				if pressure_if_A_opened > max_pressure:
					max_pressure = pressure_if_A_opened

	# now opening B
	if curA != curB and curB not in open_valves and v_rates[curB] != 0:
		pressure_from_opening_B = v_rates[curB] * (remaining_time-1)
		new_open_valves = open_valves.copy()
		new_open_valves.add(curB)

		#moving A
		for next_vA in v_to_v[curA]:
			if next_vA != curA:
				pressure_if_B_opened = pressure_from_opening_B+max_parallel_pressure(next_vA, curB, remaining_time-1, new_open_valves)
				if pressure_if_B_opened > max_pressure:
					max_pressure = pressure_if_B_opened

		# both opening
		if curA not in open_valves and v_rates[curA] != 0:
			pressure_from_opening_both = pressure_from_opening_B + v_rates[curA] * (remaining_time-1)
			open_valves_with_both = new_open_valves.copy()
			open_valves_with_both.add(curA)
			pressure_if_both_opened = pressure_from_opening_both +max_parallel_pressure(curA, curB, remaining_time-1, open_valves_with_both)
			if pressure_if_both_opened > max_pressure:
				max_pressure = pressure_if_both_opened


	# print(curA,curB, remaining_time, open_valves, max_pressure)
	hashed[hash_key] = max_pressure
	return max_pressure

print('part2: ', max_parallel_pressure('AA', 'AA', 26, set()))
