from copy import copy, deepcopy

lines = list()
with open('d4_input', 'r') as file:
	sequence = [int(i) for i in file.readline().split(',')]
	file.readline()
	boards = []
	board = []
	for line in file:
		if line == '\n':
			boards.append(board)
			board = []
		else:
			row = [int(i) for i in line.strip().split()]
			board.append(row)


def markX(boards, num):
	for i, board in enumerate(boards):
		for j, row in enumerate(board):
			for k, row_num in enumerate(row):
				if row_num == num:
					boards[i][j][k] = 'X'
	return boards

def whoBingo(boards):
	winners = set()
	for i, board in enumerate(boards):
		for j, row in enumerate(board):
			all_X_row = True
			for row_num in row:
				if row_num != 'X':
					all_X_row = False
			if all_X_row:
				winners.add(i)

		for j in range(5):
			all_X_col = True
			for k in range(5):
				if boards[i][k][j] != 'X':
					all_X_col = False
			if all_X_col:
				winners.add(i)

	return winners


def sum_remaining(board):
	sum = 0
	for row in board:
		for num in row:
			if num != 'X':
				sum += num
	return sum

def bingo(boards):
	backup_boards = deepcopy(boards)
	for num in sequence:
		backup_boards = markX(backup_boards, num)
		winners = whoBingo(backup_boards)
		if len(winners) != 0:
			return(sum_remaining(backup_boards[winners.pop()] * num))

print(bingo(boards))

# Part 2
def last_bingo(boards):
	already_won = []
	for num in sequence:
		boards = markX(boards, num)
		winners = whoBingo(boards)
		if len(winners) != 0:
			already_won += winners
			if len(boards) == 1:
				return(sum_remaining(boards[winners.pop()] * num))
			winners_reverse = list(winners)
			winners_reverse.reverse()
			for winner_i in winners_reverse:
				del(boards[winner_i])

print(last_bingo(boards))



