import re

class Solution:
	def __init__(self):
		self.valid_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
		self.hair_color_regex = re.compile('^#[0-9a-f]{6}$')
		self.pass_id_regex = re.compile('^[\d]{9}$')
		self.input = list()
		self.passports = list()

		with open('Day4_input', 'r') as file:
			self.input = file.readlines()

		cache = ""
		for line in self.input:
			if line == "\n":
				cache = cache.strip()
				self.passports.append(cache)
				cache = ""

			cache += line.replace("\n", " ")

		cache = cache.strip()
		self.passports.append(cache)


	def part1(self):
		invalid_count = 0
		for passport in self.passports:
			kvs = passport.split(' ')
			pass_keys = list()
			for kv in kvs:
				pass_keys.append(kv.split(':')[0])
			
			invalid_pass = False
			for expected_key in self.valid_fields:
				if expected_key not in pass_keys:
					invalid_pass = True

			if invalid_pass == True:
				invalid_count += 1
		
		return len(self.passports) - invalid_count

	def part2(self):
		invalid_count = 0
		for passport in self.passports:
			kvs_raw = passport.split(' ')
			kvs = {}
			for kv_raw in kvs_raw:
				kvs[kv_raw.split(':')[0]] = kv_raw.split(':')[1]
			
			invalid_pass = False
			for expected_key in self.valid_fields:
				if not self.check_rule(expected_key, kvs):
					invalid_pass = True

			if invalid_pass == True:
				invalid_count += 1
			else:
				print(passport)
		
		return len(self.passports) - invalid_count

	def is_valid_height(self, h):
		if len(h) < 4:
			return False

		dim = h[-2:]
		height = int(h[:-2])
		if dim == "cm":
			return 150 <= height and height <= 193
		elif dim == "in":
			return 59 <= height and height <= 76
		else:
			return False

	def check_rule(self, expected_key, kvs):
		def validator(k, v):
			return{
				"byr": lambda v: 1920 <= int(v) and int(v) <= 2002,
				"iyr": lambda v: 2010 <= int(v) and int(v) <= 2020,
				"eyr": lambda v: 2020 <= int(v) and int(v) <= 2030,
				"hgt": lambda v: self.is_valid_height(v),
				"hcl": lambda v: self.hair_color_regex.match(v) is not None,
				"ecl": lambda v: v in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
				"pid": lambda v: self.pass_id_regex.match(v) is not None,
			}[k](v)

		if expected_key not in kvs.keys():
			return False

		return validator(expected_key, kvs[expected_key])

s = Solution()
print(s.part1())
print(s.part2())

