import heapq
import math
import sys

sys.setrecursionlimit(20000)
print(sys.getrecursionlimit())

with open('d17_input', 'r') as file:
    pool = [[int(c) for c in line.strip()] for line in file]


class PoolNode:
    def __init__(self, x, y, direction, cur_steps):
        self.x = x
        self.y = y
        self.direction = direction
        self.cur_steps = cur_steps

    def __hash__(self):
        return hash((self.x, self.y, self.direction, self.cur_steps))

    def __eq__(self, other):
        return (self.x, self.y, self.direction, self.cur_steps) == (other.x, other.y, other.direction, other.cur_steps)

    def __str__(self):
        return "{}-{}-{}-{}".format(self.x, self.y, self.direction, self.cur_steps)

    def __lt__(self, other):
        return self.get_cur_steps() < other.get_cur_steps()

    def get_cur_steps(self):
        return self.cur_steps

    def get_direction(self):
        return self.direction

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


def get_neighbours(pool_node: PoolNode):
    x, y, cur_steps, cur_direction = pool_node.get_x(), pool_node.get_y(), pool_node.get_cur_steps(), pool_node.get_direction()
    neighbours = []
    if x < len(pool[0]) - 1:
        if cur_direction != 'r' and cur_direction != 'l':
            neighbours.append(PoolNode(x + 1, y, 'r', 1))
        elif cur_direction == 'r' and cur_steps < 3:
            neighbours.append(PoolNode(x + 1, y, 'r', cur_steps + 1))
    if y < len(pool) - 1:
        if cur_direction != 'd' and cur_direction != 'u':
            neighbours.append(PoolNode(x, y + 1, 'd', 1))
        elif cur_direction == 'd' and cur_steps < 3:
            neighbours.append(PoolNode(x, y + 1, 'd', cur_steps + 1))
    if x > 0:
        if cur_direction != 'l' and cur_direction != 'r':
            neighbours.append(PoolNode(x - 1, y, 'l', 1))
        elif cur_direction == 'l' and cur_steps < 3:
            neighbours.append(PoolNode(x - 1, y, 'l', cur_steps + 1))
    if y > 0:
        if cur_direction != 'u' and cur_direction != 'd':
            neighbours.append(PoolNode(x, y - 1, 'u', 1))
        elif cur_direction == 'u' and cur_steps < 3:
            neighbours.append(PoolNode(x, y - 1, 'u', cur_steps + 1))
    return neighbours


distances = {}
for i in range(len(pool)):
    for j in range(len(pool[0])):
        distances[(j, i)] = math.inf

visited = set()
def calc_min_heat_loss():
    distances[(0, 0)] = 0
    to_visit = [(0, PoolNode(0, 0, 'r', 0))]

    while to_visit:
        dist_so_far, cur_node = heapq.heappop(to_visit)

        if cur_node in visited:
            continue

        visited.add(cur_node)

        neighbours = get_neighbours(cur_node)
        for neighbour in neighbours:
            x, y = neighbour.get_x(), neighbour.get_y()
            new_dist = dist_so_far + pool[y][x]
            if new_dist < distances[(x, y)]:
                distances[(x, y)] = new_dist
            heapq.heappush(to_visit, (new_dist, neighbour))


calc_min_heat_loss()
print(distances)
print('part1', distances[(len(pool[0]) - 1, len(pool) - 1)])
