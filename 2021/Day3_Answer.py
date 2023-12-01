import math
lines = list()
with open('d3_input', 'r') as file:
	for line in file:
		size = len(line)
		lines.append(line)

mc_digits = [0] * size
for line in lines:
	i = 0
	for digit in line:
		if digit == '0':
			mc_digits[i]-=1
		if digit == '1':
			mc_digits[i]+=1
		i +=1

binary_gamma = [0] * size
binary_epsilon = [0] * size
gamma = 0
epsilon = 0
i = 0
for mc_digit in mc_digits:
	if mc_digit > 0:
		binary_gamma[i] = 1
		binary_epsilon[i] = 0
		gamma += math.pow(2, size-i-1)
	else:
		binary_gamma[i] = 0
		binary_epsilon[i] = 1
		epsilon += math.pow(2, size-i-1)
	i+=1


print(gamma * epsilon)

##### part 2


oxygen = lines.copy()
for i in range(size):
	i_mc = 0
	temp_lines = list()
	for line in oxygen:
		if line[i] == '0':
			i_mc -= 1
		else: 
			i_mc += 1

	if i_mc >= 0: 
		i_mc = '1'
	else:
		i_mc = '0'

	for line in oxygen:
		if line[i] == i_mc:
			temp_lines.append(line)
	oxygen = temp_lines
	if len(oxygen) == 1:
		break

co2 = lines.copy()
for i in range(size):
	i_lc = 0
	temp_lines = list()
	for line in co2:
		if line[i] == '0':
			i_lc -= 1
		else: 
			i_lc += 1

	if i_lc >= 0: 
		i_lc = '0'
	else:
		i_lc = '1'

	for line in co2:
		if line[i] == i_lc:
			temp_lines.append(line)

	co2 = temp_lines
	if len(co2)==1:
		break

oxygen_val = 0
co2_val = 0
for i in range(size):
	oxygen_val += int(oxygen[0][i]) * math.pow(2, size-1-i)
	co2_val += int(co2[0][i]) * math.pow(2, size-1-i)
print(oxygen)
print(co2)
print(oxygen_val * co2_val)

