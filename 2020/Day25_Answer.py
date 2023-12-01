with open('Day25_input', 'r') as file:
	input = [line.strip() for line in file.readlines()]

def get_loop(pk):
	x = 1
	i = 0
	while True:
		x = x * 7
		x = x % 20201227
		i+=1
		if x == pk:
			return i
	
def answer(card_pk, door_pk):
	card_loop = get_loop(card_pk)
	door_loop = get_loop(door_pk)

	print(card_loop)
	print(door_loop)
	x = 1
	for i in range(door_loop):
		x = x * card_pk
		x = x % 20201227
	return x


print('part 1 answer: {}'.format(answer(8252394, 6269621)))
