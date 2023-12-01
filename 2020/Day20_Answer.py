from collections import defaultdict
import numpy as np
import math

class Solution:
	def __init__(self):
		self.pics = {}
		self.side_to_ids_map = defaultdict(list)
		self.side_counts = defaultdict(int)
		self.pieces_count = 0

		with open('Day20_input', 'r') as file:
			line = file.readline()
			while line:
				title_id = int(line.split(' ')[1].strip()[:-1])
				matrix = list()
				line = file.readline()
				while line and line != '\n':
					line_chars = [char for char in line.strip()]
					matrix.append(line_chars)
					line = file.readline()
				self.pieces_count += 1

				self.pics[title_id] = matrix
				for side in self.get_sides(matrix):
					side_str = ''.join(side)
					if side_str[::-1] in self.side_to_ids_map:
						side_str = side_str[::-1]
					self.side_to_ids_map[side_str].append(title_id)
					self.side_counts[side_str] += 1
				
				line = file.readline()
		# for t_id, pic in self.pics.items():
		# 	print(t_id, pic)
		print(self.side_to_ids_map)
		print(self.side_counts)

	def get_sides(self, matrix):
		n = len(matrix)
		sides = [list(matrix[0]), list(matrix[n-1])]
		m = len(matrix[0])
		side3 = list()
		side4 = list()
		for row in matrix:
			side3.append(row[0])
			side4.append(row[m-1])

		sides.append(side3)
		sides.append(side4)

		return sides

	def rot_flip(self, matrix, n):
		if n // 4 == 1 or n//4 == 2:
			matrix = np.flip(matrix, n//4 - 1)
		if n // 4 == 3:
			print("4")
			matrix = np.flip(np.flip(matrix, 0), 1)
		n = n % 4
		return np.rot90(matrix, k=n+1)

	def part1(self):
		count_ones = defaultdict(int)
		for side, count in self.side_counts.items():
			if count == 1:
				count_ones[self.side_to_ids_map[side][0]] += 1
		
		result = 1
		for title_id, count in count_ones.items():
			if count == 2:
				result *= title_id

		return result

	def find_piece(self, full_pic_ids, used_pieces, i, j):
		comparing_pieces = list()
		dim = int(math.sqrt(self.pieces_count))
		if i != 0 and j != dim-1:
			comparing_pieces.append(full_pic_ids[i-1][j])
		if j != 0 and j != dim-1:
			comparing_pieces.append(full_pic_ids[i][j-1])

		comparing_neighbours = defaultdict(int)
		for (comparing_title_id, comparing_rot_i) in comparing_pieces:
			comparing_pic = self.rot_flip(self.pics[comparing_title_id], comparing_rot_i)
			for side in self.get_sides(comparing_pic):
				side_str = ''.join(side)
				if side_str[::-1] in self.side_to_ids_map:
					side_str = side_str[::-1]				
				
				for title_id in self.side_to_ids_map[side_str]:
					if title_id not in used_pieces:
						comparing_neighbours[title_id] += 1

		for k,v in comparing_neighbours.items():
			if v == 2:
				return k

	def remove_edges(self, matrix):
		result = [None] * (len(matrix)-2)
		for i in range(1, len(matrix)-1):
			row = [None] * (len(matrix[0])-2)
			for j in range(1, len(matrix[0])-1):
				row[j-1] = matrix[i][j]
			result[i-1] = row
		return result

	def build_picture(self, full_pic_ids):
		dim = int(math.sqrt(self.pieces_count))
		full_pic = [None] * dim
		for i in range(dim):
			full_pic[i] = [None] * dim

		for i in range(dim):
			for j in range(dim):
				no_edge_matrix = self.remove_edges(self.rot_flip(self.pics[full_pic_ids[i][j][0]],full_pic_ids[i][j][1]))
				# no_edge_matrix = (self.rot_flip(self.pics[full_pic_ids[i][j][0]], full_pic_ids[i][j][1]))
				full_pic[i][j] = no_edge_matrix

		return full_pic

	def find_edge(self, full_pic_ids, remaining_edges, i, j):
		comparing_pic_id = full_pic_ids[i][j][0]
		comparin_pic_rot_i = full_pic_ids[i][j][1]
		comparing_pic = self.rot_flip(self.pics[comparing_pic_id], comparin_pic_rot_i)
		for side in self.get_sides(comparing_pic):
			side_str = ''.join(side)
			if side_str[::-1] in self.side_to_ids_map:
				side_str = side_str[::-1]				
			for title_id in self.side_to_ids_map[side_str]:
				if title_id in remaining_edges:
					return (title_id, ''.join(side))

	def find_center_node(self, full_pic_ids, remaining_edges, i, j):
		left_id = full_pic_ids[i][j-1][0]
		left_rot_i = full_pic_ids[i][j-1][1]
		left_pic = self.rot_flip(self.pics[left_id], left_rot_i)
		left_side = self.get_sides(left_pic)[3]
		print(left_side)

		top_id = full_pic_ids[i-1][j][0]
		top_rot_i = full_pic_ids[i-1][j][1]
		top_pic = self.rot_flip(self.pics[top_id], top_rot_i)
		top_side = self.get_sides(top_pic)[1]
		print(top_side)

		side_str = ''.join(left_side)
		if side_str[::-1] in self.side_to_ids_map:
			side_str = side_str[::-1]				
		for title_id in self.side_to_ids_map[side_str]:
			print(title_id)
			if title_id in remaining_edges:
				print(title_id)
				matrix = self.pics[title_id]
				print(matrix)
				for i in range(12):
					rot_matrix = self.rot_flip(matrix, i)
					# print(rot_matrix)
					print('newe left {}'.format(self.get_sides(rot_matrix)[2]))
					print('newe top {}'.format(self.get_sides(rot_matrix)[0]))
					if self.get_sides(rot_matrix)[0] == top_side and self.get_sides(rot_matrix)[2] == left_side:
						rotate_i = i
				return (title_id, rotate_i)

	def find_rotate_for_top_edge(self, piece_id, left_side_str):
		matrix = self.pics[piece_id]
		# sides = self.get_sides(matrix)
		# for side in sides:
		# 	side_str = ''.join(side)
		# 	if side_str[::-1] in self.side_counts:
		# 		side_str = side_str[::-1]
		# 	if self.side_counts[side_str] == 1:
		# 		top_side = side

		for i in range(12):
			rot_matrix = self.rot_flip(matrix, i)
			new_sides = self.get_sides(rot_matrix)
			# if list(new_sides[0]) == top_side or list(new_sides[0]) == top_side.reverse():
			maybe_left_str = ''.join(list(new_sides[2]))
			if maybe_left_str == left_side_str :
				return i

	def find_rotate_for_left_edge(self, piece_id, top_side_str):
		matrix = self.pics[piece_id]
		# sides = self.get_sides(matrix)
		# for side in sides:
		# 	side_str = ''.join(side)
		# 	if side_str[::-1] in self.side_counts:
		# 		side_str = side_str[::-1]
		# 	if self.side_counts[side_str] == 1:
		# 		left_side = side

		for i in range(12):
			rot_matrix = self.rot_flip(matrix, i)
			new_sides = self.get_sides(rot_matrix)
			# if list(new_sides[2]) == left_side or list(new_sides[2]) == left_side.reverse():
			maybe_top_str = ''.join(list(new_sides[0]))
			if maybe_top_str == top_side_str: # or maybe_top_str[::-1] == top_side_str:
				return i

	def find_rotate_for_corner(self, piece_id):
		matrix = self.pics[piece_id]
		sides = self.get_sides(matrix)
		edge_sides = list()
		for side in sides:
			side_str = ''.join(side)
			if side_str[::-1] in self.side_counts:
				side_str = side_str[::-1]
			if self.side_counts[side_str] == 1:
				edge_sides.append(side_str)
		
		print('corner edges {}'.format(edge_sides))
		for i in range(12):
			rot_matrix = self.rot_flip(matrix, i)
			new_sides = self.get_sides(rot_matrix)
			# check top and left are in edges
			new_left_str = ''.join(new_sides[2])
			if new_left_str in edge_sides or new_left_str[::-1] in edge_sides:
				new_top_str = ''.join(new_sides[0])
				if new_top_str in edge_sides or new_top_str[::-1] in edge_sides:
					return i

	def find_rotate_for_right_edge(self, piece_id, top_side_str):
		matrix = self.pics[piece_id]
		# sides = self.get_sides(matrix)
		# for side in sides:
		# 	side_str = ''.join(side)
		# 	if side_str[::-1] in self.side_counts:
		# 		side_str = side_str[::-1]
		# 	if self.side_counts[side_str] == 1:
		# 		right_side = side
		
		for i in range(12):
			rot_matrix = self.rot_flip(matrix, i)
			new_sides = self.get_sides(rot_matrix)
			# if list(new_sides[3]) == right_side or list(new_sides[3]) == right_side.reverse():
			maybe_top_str = ''.join(list(new_sides[0]))
			if maybe_top_str == top_side_str: # or maybe_top_str[::-1] == top_side_str:
				return i

	def find_rotate_for_bottom_edge(self, piece_id, left_side_str):
		matrix = self.pics[piece_id]
		# sides = self.get_sides(matrix)
		# for side in sides:
		# 	side_str = ''.join(side)
		# 	if side_str[::-1] in self.side_counts:
		# 		side_str = side_str[::-1]
		# 	if self.side_counts[side_str] == 1:
		# 		bottom_side = side
		
		for i in range(12):
			rot_matrix = self.rot_flip(matrix, i)
			new_sides = self.get_sides(rot_matrix)
			# if list(new_sides[1]) == bottom_side or list(new_sides[1]) == bottom_side.reverse():
			maybe_left_str = ''.join(list(new_sides[2]))
			if maybe_left_str == left_side_str: # or maybe_left_str[::-1] == left_side_str:
				return i

	def part2(self):
		count_ones = defaultdict(int)
		for side, count in self.side_counts.items():
			if count == 1:
				count_ones[self.side_to_ids_map[side][0]] += 1

		corners = list()
		remaining_edges = list()
		for title_id, count in count_ones.items():
			if count == 2:
				corners.append(title_id)
			remaining_edges.append(title_id)
		remaining_inner_pieces_ids = self.pics.keys() - remaining_edges

		dim = int(math.sqrt(self.pieces_count))
		full_pic_ids = [-1] * dim
		for i in range(dim):
			full_pic_ids[i] = [-1] * dim
		full_pic_ids[0][0] = (corners[0], self.find_rotate_for_corner(corners[0])) # random rotation for now
		used_pieces = [corners[0]]
		remaining_edges = [id for id in remaining_edges if id != corners[0]]

		# build left side
		for i in range(1, dim):
			(piece_id, side_str) = self.find_edge(full_pic_ids, remaining_edges, i-1, 0)
			remaining_edges = [id for id in remaining_edges if id != piece_id]
			used_pieces.append(piece_id)
			rotate_i = self.find_rotate_for_left_edge(piece_id, side_str)
			full_pic_ids[i][0] = (piece_id, rotate_i)

		# build top side
		for i in range(1, dim):
			(piece_id, side_str) = self.find_edge(full_pic_ids, remaining_edges, 0, i-1)

			remaining_edges = [id for id in remaining_edges if id != piece_id]
			used_pieces.append(piece_id)
			rotate_i = self.find_rotate_for_top_edge(piece_id, side_str)
			full_pic_ids[0][i] = (piece_id, rotate_i)

		# second_piece_id = full_pic_ids[0][1][0]
		# rotate_second_piece = self.rot_flip(self.pics[second_piece_id], full_pic_ids[0][1][1])
		# rotate_i = self.find_rotate_for_corner(corners[0], self.get_sides(rotate_second_piece)[2])
		# print("corner rotate {}".format(rotate_i))
		
		# build right side
		for i in range(1, dim):
			(piece_id, side_str) = self.find_edge(full_pic_ids, remaining_edges, i-1, dim-1)

			remaining_edges = [id for id in remaining_edges if id != piece_id]
			used_pieces.append(piece_id)
			rotate_i = self.find_rotate_for_right_edge(piece_id, side_str)
			full_pic_ids[i][dim-1] = (piece_id, rotate_i)

		# build bottom side (ignore last)
		for i in range(1, dim-1):
			(piece_id, side_str) = self.find_edge(full_pic_ids, remaining_edges, dim-1, i-1)
			remaining_edges = [id for id in remaining_edges if id != piece_id]
			used_pieces.append(piece_id)
			rotate_i = self.find_rotate_for_bottom_edge(piece_id, side_str)
			full_pic_ids[dim-1][i] = (piece_id, rotate_i)

		print('remaining piece {}'.format(remaining_edges))

		# fill inside
		for i in range(1, dim-1):
			for j in range(1, dim-1):
				# (piece_id, side_str) = self.find_piece(full_pic_ids, used_pieces, i, j)
				(piece_id, rotate_i) = self.find_center_node(full_pic_ids, remaining_inner_pieces_ids, i, j)
				remaining_inner_pieces_ids = [id for id in remaining_inner_pieces_ids if id != piece_id]
				full_pic_ids[i][j] = (piece_id, rotate_i)
		print('full_pic_ids {}'.format(full_pic_ids))

		full_pic = self.build_picture(full_pic_ids)
		# for pic_row in full_pic:
		# 	for i in range(len(pic_row[0][0])):
		# 		new_row = ''
		# 		for j in range(len(pic_row)):
		# 			new_row += ''.join(pic_row[j][i])
		# 		print(new_row)
		# 	print("newRow")

		flattened_pic = self.rot_flip(self.flatten_pic(full_pic),10)

		monster_count = 0
		hash_count = 0
		for i in range(len(flattened_pic)):
			hash_count += sum(char=='#' for char in flattened_pic[i])
			for j in range(len(flattened_pic[0])):
				if self.monster_starts(flattened_pic, i, j):
					monster_count+=1

		print(hash_count)
		return hash_count - monster_count * 15

	def flatten_pic(self, full_pic):
		result = list()
		for pic_row in full_pic:
			for i in range(len(pic_row[0][0])):
				new_row = list()
				for j in range(len(pic_row)):
					new_row += pic_row[j][i]
				result.append(new_row)
				print(''.join(new_row))

		return result

	def monster_starts(self, full_pic, i, j):
		n = len(full_pic)
		if j > n-20:
			return False
		if i > n-3:
			return False
		if full_pic[i][j+18] != "#":
			return False
		if any(char != "#" for char in [full_pic[i+1][j], full_pic[i+1][j+5], full_pic[i+1][j+6], full_pic[i+1][j+11], full_pic[i+1][j+12], full_pic[i+1][j+17], full_pic[i+1][j+18], full_pic[i+1][j+19]]):
			return False
		if any(char != "#" for char in [full_pic[i+2][j+1], full_pic[i+2][j+4], full_pic[i+2][j+7], full_pic[i+2][j+10], full_pic[i+2][j+13], full_pic[i+2][j+16]]):
			return False
		return True

s = Solution()
print('part 1 answer: {}'.format(s.part1()))
print('part 2 answer: {}'.format(s.part2()))
