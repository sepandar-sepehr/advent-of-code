class Coordinate(object):
	def __init__(self, x, y):
		super(Coordinate, self).__init__()
		self.x = x
		self.y = y

	def __str__(self):
		return '({}x, {}y)'.format(self.x, self.y)

	def __repr__(self):
	    return str(self)

class Line(object):
	def __init__(self, from_xy, to_xy):
		super(Line, self).__init__()
		self.from_xy = from_xy
		self.to_xy = to_xy

	def __str__(self):
		return '(from{}, to{})'.format(self.from_xy, self.to_xy)

	def __repr__(self):
	    return str(self)

	def same_row(self):
		return self.from_xy.x == self.to_xy.x

	def same_col(self):
		return self.from_xy.y == self.to_xy.y

	def diagonal(self):
		return abs(self.from_xy.x - self.to_xy.x) == abs(self.from_xy.y - self.to_xy.y)

		
lines = []

with open('d5_input', 'r') as file:
	for line in file:
		from_xy_split = line.split(' ')[0].split(',')
		from_xy = Coordinate(int(from_xy_split[0]), int(from_xy_split[1]))
		
		to_xy_split = line.split(' ')[2].split(',')
		to_xy = Coordinate(int(to_xy_split[0]), int(to_xy_split[1]))

		lines.append(Line(from_xy, to_xy))

print(lines)

def add_row(line_diagram, line):
	step = -1 if line.from_xy.y > line.to_xy.y else 1
	for i in range(line.from_xy.y, line.to_xy.y + step, step):
		line_diagram[line.from_xy.x][i] += 1
	return line_diagram

def add_col(line_diagram, line):
	step = -1 if line.from_xy.x > line.to_xy.x else 1
	for i in range(line.from_xy.x, line.to_xy.x + step, step):
		line_diagram[i][line.from_xy.y] += 1
	return line_diagram

dimension=990

# part 1
line_diagram = [[0 for i in range(dimension+1)] for i in range(dimension+1)]

for line in lines:
	if line.same_row():
		line_diagram = add_row(line_diagram, line)
	if line.same_col():
		line_diagram = add_col(line_diagram, line)

overlaps = 0
for line in line_diagram:
	for i in line:
		if i > 1:
			overlaps+=1
print(overlaps)


# part 2
def add_diag(line_diagram, line):
	size = abs(line.from_xy.x - line.to_xy.x) + 1
	for i in range(size):
		if line.from_xy.x > line.to_xy.x and line.from_xy.y > line.to_xy.y:
			line_diagram[line.to_xy.x+i][line.to_xy.y+i] += 1
		elif line.from_xy.x > line.to_xy.x and line.from_xy.y < line.to_xy.y:
			line_diagram[line.to_xy.x+i][line.to_xy.y-i] += 1
		elif line.from_xy.x < line.to_xy.x and line.from_xy.y > line.to_xy.y:
			line_diagram[line.from_xy.x+i][line.from_xy.y-i] += 1
		else:
			line_diagram[line.from_xy.x+i][line.from_xy.y+i] += 1
	return line_diagram

line_diagram = [[0 for i in range(dimension+1)] for i in range(dimension+1)]

for line in lines:
	if line.same_row():
		line_diagram = add_row(line_diagram, line)
	elif line.same_col():
		line_diagram = add_col(line_diagram, line)
	elif line.diagonal():
		line_diagram = add_diag(line_diagram, line)

overlaps = 0
for line in line_diagram:
	for i in line:
		if i > 1:
			overlaps+=1
print(overlaps)
