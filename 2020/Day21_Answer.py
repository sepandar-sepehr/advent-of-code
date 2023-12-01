from collections import defaultdict
import copy

class Solution:
	def __init__(self):
		self.ingredients = set()
		self.alergens = set()
		self.ing_tuples = list()
		self.al_to_ing_map = defaultdict(list)
		with open('Day21_input', 'r') as file:
			line = file.readline()
			while line:
				[ings, alrgn] = line.split('(')
				alergens = alrgn.strip()[8:-1].strip().split(', ')
				self.alergens.update(set(alergens))
				ingredients = ings[:-1].split(' ')
				self.ingredients.update(set(ingredients))

				self.ing_tuples.append((set(ingredients), set(alergens)))
				for al in alergens:
					self.al_to_ing_map[al].append(set(ingredients))
				

				line = file.readline()

		print("al to ing map")
		for k,v in self.al_to_ing_map.items():
			print(k, v)
		
	

	def part1(self):
		contains_al = set()
		for al in self.alergens:
			print(al)
			print(set.intersection(*self.al_to_ing_map[al]))
			contains_al.update(set.intersection(*self.al_to_ing_map[al]))
			print('contains alergens: {}'.format(contains_al))

		count = 0
		for (ingredients, als) in self.ing_tuples:
			for ing in ingredients:
				if ing not in contains_al:
					count +=1
		return count

	def part2(self):
		bad_list = {}
		bad_list['dairy'] = 'rhvbn'
		bad_list['nuts'] = 'fvk'
		bad_list['wheat'] = 'zrb'
		bad_list['eggs'] = 'mmcpg'
		bad_list['shellfish'] = 'jgtb'
		bad_list['sesame'] = 'lbmt'
		bad_list['soy'] = 'hcbdb'
		bad_list['fish'] = 'kjf'
		bad_ings = list(bad_list.keys())
		bad_ings.sort()
		result = ''
		for bad_ing in bad_ings:
			result += ','
			result += bad_list[bad_ing]
		return result[1:]

s = Solution()
print('part 1 answer: {}'.format(s.part1()))
print('part 2 answer: {}'.format(s.part2()))
