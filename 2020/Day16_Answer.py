from collections import defaultdict
import re

class Solution:
	def __init__(self):
		self.input = list()
		with open('Day16_input', 'r') as file:
			self.input = [line.strip().split(',') for line in file.readlines()]
		print(self.input)
		self.rules = list()
		with open('Day16_rules', 'r') as file:
			for line in file.readlines():
				parts1 = line.strip().split(': ')
				parts2 = parts1[1].split(' or ')
				self.rules.append((parts1[0], parts2))
		print(self.rules)


	def get_invalid_values(self, ticket):
		result = list()
		for value in ticket:
			num = int(value)
			matched = False
			for rule in self.rules:
				rule_range = rule[1][0].split('-')
				if (num in range(int(rule_range[0]), int(rule_range[1])+1)):
					matched = True
				rule_range = rule[1][1].split('-')
				if (num in range(int(rule_range[0]), int(rule_range[1])+1)):
					matched = True

			if not matched:
				result.append(num)

		return result

	def part1(self):
		tot = 0
		for ticket in self.input:
			invalid_values = self.get_invalid_values(ticket)
			for value in invalid_values:
				tot += value
		return tot

	def find_matching_index(self, rule, valid_tickets):
		rule_range = rule[0].split('-')
		range1 = range(int(rule_range[0]), int(rule_range[1])+1)
		rule_range = rule[1].split('-')
		range2 = range(int(rule_range[0]), int(rule_range[1])+1)

		matched_indexes = list()
		for i in range(len(self.rules)):
			all_matched = True
			for ticket in valid_tickets:
				num = int(ticket[i])
				if num not in range1 and num not in range2:
					all_matched = False

			if all_matched:
				matched_indexes.append(i)

		return matched_indexes

	def part2(self):
		my_ticket = [71,127,181,179,113,109,79,151,97,107,53,193,73,83,191,101,89,149,103,197]
		valid_tickets = list()
		for ticket in self.input:
			invalid_values = self.get_invalid_values(ticket)
			if len(invalid_values) == 0:
				valid_tickets.append(ticket)

		print(valid_tickets)
		mul = 1
		for rule in self.rules:
			# if 'departure' in rule[0]:
			print(rule[0])
			print(self.find_matching_index(rule[1], valid_tickets))

		return my_ticket[10]*my_ticket[13]*my_ticket[8]*my_ticket[18]*my_ticket[5]*my_ticket[16]


s = Solution()
print('part 1 answer: {}'.format(s.part1()))
print('part 2 answer: {}'.format(s.part2()))
