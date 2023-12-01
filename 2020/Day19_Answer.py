from collections import defaultdict
import copy

class Solution:
	def __init__(self):
		self.rules = dict()
		self.messages = list()
		with open('Day19_input', 'r') as file:
			line = file.readline()
			while line != '\n':
				rule = self._parse_rule(line.strip())
				self.rules[rule[0]] = rule[1]
				line = file.readline()

			line = file.readline()
			while line:
				self.messages.append(line.strip())
				line = file.readline()
		print(self.rules)
		print(self.messages)
		self.calculated = defaultdict(list)

	def _parse_rule(self, line):
		parts = line.split(':')
		rules = parts[1].strip().replace('"', '').split('|')
		parsed_rules = list()
		for rule in rules:
			parsed_rules.append(rule.strip().split(' '))
		return (parts[0], parsed_rules)
	
	# def _match_1rule(self, messagee, rule):
	# 	i = 0
	# 	for node in rule:
	# 		if self.rules[node][0][0] <= 'z' and self.rules[node][0][0] >= 'a':
	# 			if message[i] != self.rules[node][0][0]:
	# 				return False
	# 			i+=1
	# 		else:
	# 			return self._match_rules(message[i+1:], node)

	# def _match_rules(self, message, start):
	# 	rule0 = self.rules[start]
	# 	for rule in rule0:
	# 		if self._match_1rule(message, rule):
	# 			return True
	# 	return False

	# def part1(self):
	# 	count = 0
	# 	for message in self.messages:
	# 		if self._match_rules(message, '0'):
	# 			count += 1
	# 	return count

	def _open_node(self, node, opened_nodes):
		# dict_key = ""
		# if len(opened_nodes) != 0:
		# 	dict_key = (node, opened_nodes[0])
		# 	if dict_key in self.calculated:
		# 		return self.calculated[dict_key]

		if node == '8' and len(opened_nodes)>0 and len(opened_nodes[0])>25:
			return opened_nodes
		if node == '11' and len(opened_nodes)>0 and len(opened_nodes[0])>43:
			return opened_nodes

		if self.rules[node][0][0] <= 'z' and self.rules[node][0][0] >= 'a':
			new_char = self.rules[node][0][0]
			if len(opened_nodes) == 0:
				return [new_char]
			result = list()
			for opened_node in opened_nodes:
				result.append(opened_node + new_char)
			# self.calculated[dict_key] = result
			return result

		# print(node)
		# print(opened_nodes)
		copied = list()
		for so_far in opened_nodes:
			copied.append(so_far[:])

		rule1 = self.rules[node][0]
		for _node in rule1:
			opened_nodes = self._open_node(_node, opened_nodes)
		# print('opened')
		# print(opened_nodes)
		if len(self.rules[node]) == 1:
			# self.calculated[dict_key] = opened_nodes
			return opened_nodes
		rule2 = self.rules[node][1]
		for _node in rule2:
			copied = self._open_node(_node, copied)
		# print('copy')
		# print(copied)
		# self.calculated[dict_key] = opened_nodes + copied
		return opened_nodes + copied
			

	# def _flatten_nodes(self, nodes):
	# 	result = list()
		
	# 	while not all(isinstance(node, str) for node in nodes):

	# 			if isinstance(node[0][0])
	# 				result += self._flatten_nodes(node)
	# 			else:

	# 		else:
	# 			result.append(node)

	# 	return result

	def part1(self):
		rule0 = self.rules['0'][0]

		opened_nodes = list()
		for node in rule0:
			opened_nodes = self._open_node(node, opened_nodes)
	
		count = 0
		for message in self.messages:
			if message in opened_nodes:
				count+=1
		return count
		# valid_strings = self._flatten_nodes(opened_nodes)
		# print(valid_strings)

	def _open_node2(self, node, opened_nodes):
		# dict_key = ""
		# if len(opened_nodes) != 0:
		# 	dict_key = (node, opened_nodes[0])
		# 	if dict_key in self.calculated:
		# 		return self.calculated[dict_key]

		# if node == '8' and len(opened_nodes)>0 and len(opened_nodes[0])>25:
		# 	return opened_nodes
		# if node == '11' and len(opened_nodes)>0 and len(opened_nodes[0])>43:
		# 	return opened_nodes

		if self.rules[node][0][0] <= 'z' and self.rules[node][0][0] >= 'a':
			new_char = self.rules[node][0][0]
			if len(opened_nodes) == 0:
				return [new_char]
			result = list()
			for opened_node in opened_nodes:
				result.append(opened_node + new_char)
			# self.calculated[dict_key] = result
			return result

		# print("opened: {}".format(opened_nodes))
		# print("rules: {}".format(self.rules[node]))
		copies = [-1] * (len(self.rules[node])-1)
		for i in range(len(copies)):
			copies[i] = copy.deepcopy(opened_nodes)

		# print("empty copies: {}".format(copies))	

		rule1 = self.rules[node][0]
		for _node in rule1:
			opened_nodes = self._open_node2(_node, opened_nodes)

		if len(self.rules[node]) == 1:
			return opened_nodes

		for i in range(1, len(self.rules[node])):
			ruleN = self.rules[node][i]
			for _node in ruleN:
				copies[i-1] = self._open_node2(_node, copies[i-1])
		# print("updated copies {}".format(copies))
		# print("opened_nodes {}".format(opened_nodes))
		result = opened_nodes
		for new_copy in copies:
			result += new_copy
		# print("result: {}".format(result))
		return result
			

	def part2(self):
		# rule0 = self.rules['0'][0]
	
		# count = 0
		# for message in self.messages:
		# 	opened_nodes = list()
		# 	for node in rule0:
		# 		opened_nodes = self._open_node2(node, opened_nodes)
		# 	if len(opened_nodes) != 0 and message in opened_nodes:
		# 		count+=1
		# return count
		rule0 = self.rules['0'][0]

		opened_nodes = list()
		for node in rule0:
			opened_nodes = self._open_node2(node, opened_nodes)
		setO = set(opened_nodes)
		
		# print(opened_nodes)
		count = 0
		for message in self.messages:
			if message in opened_nodes:
				count+=1
		return count		
s = Solution()
# print('part 1 answer: {}'.format(s.part1()))
print('part 2 answer: {}'.format(s.part2()))
