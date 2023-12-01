from collections import defaultdict
import copy

class Solution:
	def __init__(self):
		self.player1_cards = list()
		self.player2_cards = list()
		with open('Day22_input', 'r') as file:
			line = file.readline()
			line = file.readline()
			while line != '\n':
				self.player1_cards.append(int(line.strip()))
				line = file.readline()

			line = file.readline()
			line = file.readline()
			while line:
				self.player2_cards.append(int(line.strip()))
				line = file.readline()

		print(self.player1_cards)
		print(self.player2_cards)

	def part1(self):
		player1_cards = self.player1_cards[:]
		player2_cards = self.player2_cards[:]
		while len(player1_cards) > 0 and len(player2_cards) > 0:
			card1 = player1_cards[0]
			card2 = player2_cards[0]
			player1_cards = player1_cards[1:]
			player2_cards = player2_cards[1:]
			if card1 > card2:
				player1_cards.append(card1)
				player1_cards.append(card2)
			if card2 > card1:
				player2_cards.append(card2)
				player2_cards.append(card1)

		sum = 0
		for i, card in enumerate(player1_cards[::-1]):
			sum += (i+1) * card
		return sum

	def is_repeated_round(self, prev_rounds, player1_cards, player2_cards):
		for prev_round in prev_rounds:
			if prev_round[0] == player1_cards and prev_round[1] == player2_cards:
				return True
		return False

	def play_sub_game(self, player1_cards, player2_cards):
		rounds = list()
		while len(player1_cards) > 0 and len(player2_cards) > 0:
			if self.is_repeated_round(rounds, player1_cards, player2_cards):
				# print("it's repeated")
				return 1, player1_cards
			rounds.append((player1_cards, player2_cards))

			card1 = player1_cards[0]
			card2 = player2_cards[0]
			player1_cards = player1_cards[1:]
			player2_cards = player2_cards[1:]

			if card1 <= len(player1_cards) and card2 <= len(player2_cards):
				# print("subgame: {}, {}".format(player1_cards[:card1], player2_cards[:card2]))

				if self.play_sub_game(player1_cards[:card1], player2_cards[:card2])[0] == 1:
					player1_cards.append(card1)
					player1_cards.append(card2)
				else: 
					player2_cards.append(card2)
					player2_cards.append(card1)
			else:
				if card1 > card2:
					player1_cards.append(card1)
					player1_cards.append(card2)
				if card2 > card1:
					player2_cards.append(card2)
					player2_cards.append(card1)

		if len(player1_cards) == 0:
			return 2, player2_cards
		else:
			return 1, player1_cards

	def part2(self):
		self.last_p_1 = list()
		self.last_p_2 = list() 

		player1_cards = self.player1_cards[:]
		player2_cards = self.player2_cards[:]
		winner, winner_cards = self.play_sub_game(player1_cards, player2_cards)

		print("winner is {} with cards {}".format(winner, winner_cards))
		sum = 0
		for i, card in enumerate(winner_cards[::-1]):
			sum += (i+1) * card
		return sum
s = Solution()
print('part 1 answer: {}'.format(s.part1()))
print('part 2 answer: {}'.format(s.part2()))
