val_to_node_map = {}

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def listprint(self):
        printval = self.head
        while printval is not None:
            print (printval.data, end=' ')
            printval = printval.next
        print()

def get_rot_sub(start_node):
	pick1 = start_node.next
	pick2 = pick1.next
	pick3 = pick2.next

	start_node.next = pick3.next

	return [pick1, pick2, pick3]

def find_with_val_and_not_in(cur_cup, val, exclude_list, max_val):
	if val == 0:
		val = max_val

	while val == exclude_list[0].data or val == exclude_list[1].data or val == exclude_list[2].data:
		val -=1
		if val == 0:
			val = max_val

	next_cup = cur_cup.next
	return val_to_node_map[val]

def insert_cups(dest_cup, pickups):
	next_cup = dest_cup.next
	dest_cup.next = pickups[0]
	pickups[2].next = next_cup


def part2(cup_label):
	cups = LinkedList()

	max_val = 1000000
	tail_cup = None
	for char in cup_label[::-1]:
		val = int(char)
		cup = Node(val)
		val_to_node_map[val] = cup
		if not tail_cup:
			tail_cup = cup
		cup.next = cups.head
		cups.head = cup
	
	last_val = 10
	while last_val <= max_val:
		cup = Node(last_val)
		val_to_node_map[last_val] = cup
		tail_cup.next = cup
		tail_cup = tail_cup.next
		last_val+=1

	tail_cup.next = cups.head
	# cups.listprint()

	cur_cup = cups.head
	length = 10
	for i in range(10000000):
		# if i% 1000 == 0:
		# 	print("itr " + str(i))

		pick_up = get_rot_sub(cur_cup)

		dest_cup = find_with_val_and_not_in(cur_cup, cur_cup.data-1, pick_up, max_val)

		insert_cups(dest_cup, pick_up)
		
		cur_cup = cur_cup.next

	while True:
		if cur_cup.data == 1:
			return cur_cup.next.data * cur_cup.next.next.data
		cur_cup = cur_cup.next

print('part 2 answer: {}'.format(part2('872495136')))
