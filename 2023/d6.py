import math


def ways_to_win(time, dist):
    ways = 0
    for i in range(time):
        if (time - i) * i > dist:
            ways += 1
    return ways

def ways_to_win_2(time, dist):
    min_time = math.inf
    max_time = 0
    for i in range(time):
        if (time - i) * i > dist:
            min_time = i
            break

    for i in range(time):
        j = time - i
        if (time - j) * j > dist:
            max_time = j
            break
    return max_time - min_time + 1
# Test
time_to_dist = {
    7: 9,
    15: 40,
    30: 200
}

res = 1
for time, dist in time_to_dist.items():
    res *= ways_to_win(time, dist)
print("part 1 test passed: {}".format(res == 288))

# part 2
time = 71530
dist = 940200
res = ways_to_win_2(time, dist)
print("part 2, test passed: {}".format(71503 == res))

# My data
time_to_dist = {
    48: 296,
    93: 1928,
    85: 1236,
    95: 1391
}

res = 1
for time, dist in time_to_dist.items():
    res *= ways_to_win(time, dist)
print('Part 1, mine:', res)

# Part 2
time = 48938595
dist = 296192812361391
res = ways_to_win_2(time, dist)
print('part 2, mine:', res)
