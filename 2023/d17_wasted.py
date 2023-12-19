import math
import sys

sys.setrecursionlimit(20000)
print(sys.getrecursionlimit())

with open('d17_input', 'r') as file:
    pool = [[int(c) for c in line.strip()] for line in file]

calculated = {}


def calc_min(cur_pos, dir, so_far, visited, heat_loss):
    x, y = cur_pos
    hash_key = "{}-{}-{}-{}".format(x, y, dir, so_far)

    if hash_key in calculated:
        return calculated[hash_key]

    if hash_key in visited:
        return math.inf

    if x < 0 or y < 0 or x == len(pool[0]) or y == len(pool):
        return math.inf
    # print(visited)
    new_visited = visited.copy()
    # new_visited.append(hash_key)
    new_visited.append(hash_key)
    # print(cur_pos, dir, so_far)
    cur_w = pool[y][x]

    # End
    if y == len(pool) - 1 and x == len(pool[0]) - 1:
        return cur_w

    # Hit walls
    if x == len(pool[0])-1:
        if dir == 'r':
            down_pos = (x, y + 1)
            new_val = cur_w + calc_min(down_pos, 'd', 1, new_visited, cur_w + heat_loss)
            calculated[hash_key] = new_val
            return new_val
        if so_far == 3:
            left_pos = (x - 1, y)
            new_val = cur_w + calc_min(left_pos, 'l', 1, new_visited, cur_w + heat_loss)
            calculated[hash_key] = new_val
            return new_val
    if y == len(pool)-1:
        if dir == 'd':
            right_pos = (x + 1, y)
            new_val = cur_w + calc_min(right_pos, 'r', 1, new_visited, cur_w + heat_loss)
            calculated[hash_key] = new_val
            return new_val
        if so_far == 3:
            up_pos = (x, y - 1)
            new_val = cur_w + calc_min(up_pos, 'u', 1, new_visited, cur_w + heat_loss)
            calculated[hash_key] = new_val
            return new_val
    if x == 0:
        if dir == 'l':
            down_pos = (x, y + 1)
            new_val = cur_w + calc_min(down_pos, 'd', 1, new_visited, cur_w + heat_loss)
            calculated[hash_key] = new_val
            return new_val
        if so_far == 3:
            right_pos = (x + 1, y)
            new_val = cur_w + calc_min(right_pos, 'r', 1, new_visited, cur_w + heat_loss)
            calculated[hash_key] = new_val
            return new_val
    if y == 0:
        if dir == 'u':
            right_pos = (x + 1, y)
            new_val = cur_w + calc_min(right_pos, 'r', 1, new_visited, cur_w + heat_loss)
            calculated[hash_key] = new_val
            return new_val
        if so_far == 3:
            down_pos = (x, y + 1)
            new_val = cur_w + calc_min(down_pos, 'd', 1, new_visited, cur_w + heat_loss)
            calculated[hash_key] = new_val
            return new_val

    # turn
    if so_far == 3:
        if dir in ['d', 'u']:
            right_pos = (x + 1, y)
            left_pos = (x - 1, y)
            new_val = cur_w + min(calc_min(right_pos, 'r', 1, new_visited, cur_w + heat_loss), calc_min(left_pos, 'l', 1, new_visited, cur_w + heat_loss))
            calculated[hash_key] = new_val
            return new_val
        elif dir in ['r', 'l']:
            up_pos = (x, y - 1)
            down_pos = (x, y + 1)
            new_val = cur_w + min(calc_min(up_pos, 'u', 1, new_visited, cur_w + heat_loss), calc_min(down_pos, 'd', 1, new_visited, cur_w + heat_loss))
            calculated[hash_key] = new_val
            return new_val
        else:
            raise Exception('Unknown dir')

    else:
        if dir == 'd':
            right_pos = (x + 1, y)
            left_pos = (x - 1, y)
            down_pos = (x, y + 1)
            new_val = cur_w + min(calc_min(right_pos, 'r', 1, new_visited, cur_w + heat_loss),
                                  calc_min(left_pos, 'l', 1, new_visited, cur_w + heat_loss),
                                  calc_min(down_pos, 'd', so_far + 1, new_visited, cur_w + heat_loss))
            calculated[hash_key] = new_val
            return new_val
        if dir == 'u':
            right_pos = (x + 1, y)
            left_pos = (x - 1, y)
            up_pos = (x, y - 1)
            new_val = cur_w + min(calc_min(right_pos, 'r', 1, new_visited, cur_w + heat_loss),
                                  calc_min(left_pos, 'l', 1, new_visited, cur_w + heat_loss),
                                  calc_min(up_pos, 'u', so_far + 1, new_visited, cur_w + heat_loss))
            calculated[hash_key] = new_val
            return new_val
        elif dir == 'r':
            up_pos = (x, y - 1)
            down_pos = (x, y + 1)
            right_pos = (x + 1, y)
            new_val = cur_w + min(calc_min(up_pos, 'u', 1, new_visited, cur_w + heat_loss),
                                  calc_min(down_pos, 'd', 1, new_visited, cur_w + heat_loss),
                                  calc_min(right_pos, 'r', so_far + 1, new_visited, cur_w + heat_loss))
            calculated[hash_key] = new_val
            return new_val
        elif dir == 'l':
            up_pos = (x, y - 1)
            down_pos = (x, y + 1)
            left_pos = (x - 1, y)
            new_val = cur_w + min(calc_min(up_pos, 'u', 1, new_visited, cur_w + heat_loss),
                                  calc_min(down_pos, 'd', 1, new_visited, cur_w + heat_loss),
                                  calc_min(left_pos, 'l', so_far + 1, new_visited, cur_w + heat_loss))
            calculated[hash_key] = new_val
            return new_val
        else:
            raise Exception('Unknown dir')


min_heat_loss = min(calc_min((1, 0), 'r', 1, [(0, 0)], 0),
                    calc_min((0, 1), 'd', 1, [(0, 0)], 0))
print(calculated)
print('part1', min_heat_loss)
# 1159 too high
# 1082 too high