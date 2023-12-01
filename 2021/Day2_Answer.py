commands = list()
with open('d2_input', 'r') as file:
	for line in file:
		line_split = line.split(' ')
		commands.append((line_split[0], int(line_split[1])))

pos = (0,0)
for command in commands:
	if command[0] == 'forward':
		pos = (pos[0], pos[1] + command[1])
	elif command[0] == 'down':
		pos = (pos[0] + command[1], pos[1])
	elif command[0] == 'up':
		pos = (pos[0] - command[1], pos[1])
	else:
		print("WTF!")

print(pos[0] * pos[1])


pos = (0,0)
aim = 0
for command in commands:
	if command[0] == 'forward':
		pos = (pos[0] + aim * command[1], pos[1] + command[1])
	elif command[0] == 'down':
		aim += command[1]
	elif command[0] == 'up':
		aim -= command[1]
	else:
		print("WTF!")

print(pos[0] * pos[1])
