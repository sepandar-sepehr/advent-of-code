from collections import defaultdict

mirror_map = []
with open('d16_input', 'r') as file:
    for line in file:
        mirror_map.append([c for c in line.strip()])


def get_new_beams(pos, direction):
    x, y = pos
    new_beams = []
    if mirror_map[y][x] == '/':
        if direction == 'r':
            new_beams.append((pos, 'u'))
        elif direction == 'l':
            new_beams.append((pos, 'd'))
        elif direction == 'u':
            new_beams.append((pos, 'r'))
        elif direction == 'd':
            new_beams.append((pos, 'l'))
    elif mirror_map[y][x] == '\\':
        if direction == 'r':
            new_beams.append((pos, 'd'))
        elif direction == 'l':
            new_beams.append((pos, 'u'))
        elif direction == 'u':
            new_beams.append((pos, 'l'))
        elif direction == 'd':
            new_beams.append((pos, 'r'))
    elif mirror_map[y][x] == '|':
        if direction == 'r':
            new_beams.append((pos, 'u'))
            new_beams.append((pos, 'd'))
        elif direction == 'l':
            new_beams.append((pos, 'u'))
            new_beams.append((pos, 'd'))
        elif direction == 'u':
            new_beams.append((pos, 'u'))
        elif direction == 'd':
            new_beams.append((pos, 'd'))
    elif mirror_map[y][x] == '-':
        if direction == 'r':
            new_beams.append((pos, 'r'))
        elif direction == 'l':
            new_beams.append((pos, 'l'))
        elif direction == 'u':
            new_beams.append((pos, 'l'))
            new_beams.append((pos, 'r'))
        elif direction == 'd':
            new_beams.append((pos, 'l'))
            new_beams.append((pos, 'r'))
    elif mirror_map[y][x] == '.':
        new_beams.append((pos, direction))
    else:
        raise Exception('Unknown mirror')
    return [new_beam for new_beam in new_beams if new_beam is not None]


def count_visited():
    count = 0
    for y in range(len(visited_matrix)):
        for x in range(len(visited_matrix[0])):
            if visited_matrix[y][x]:
                count += visited_matrix[y][x]
    return count



max_count = 0
for i in range(len(mirror_map[0])):
    visited_matrix = [[False for _ in range(len(mirror_map[0]))] for _ in range(len(mirror_map))]
    visited_directions = defaultdict(list)
    beams = [((i, -1), 'd')]

    while len(beams) > 0:
        new_beams = []
        for beam in beams:
            x, y = beam[0]
            direction = beam[1]
            if direction == 'r':
                x += 1
            elif direction == 'l':
                x -= 1
            elif direction == 'u':
                y -= 1
            elif direction == 'd':
                y += 1

            if x < 0 or y < 0 or x >= len(mirror_map[0]) or y >= len(mirror_map):
                continue

            new_beams_of_beam = get_new_beams((x, y), direction)
            for new_beam in new_beams_of_beam:
                if new_beam[0] in visited_directions and new_beam[1] in visited_directions[new_beam[0]]:
                    continue
                else:
                    visited_directions[new_beam[0]].append(new_beam[1])
                    visited_matrix[new_beam[0][1]][new_beam[0][0]] = True
                    new_beams.append(new_beam)

        beams = new_beams

    if count_visited() > max_count:
        max_count = count_visited()

for i in range(len(mirror_map[0])):
    visited_matrix = [[False for _ in range(len(mirror_map[0]))] for _ in range(len(mirror_map))]
    visited_directions = defaultdict(list)
    beams = [((i, len(mirror_map)), 'u')]

    while len(beams) > 0:
        new_beams = []
        for beam in beams:
            x, y = beam[0]
            direction = beam[1]
            if direction == 'r':
                x += 1
            elif direction == 'l':
                x -= 1
            elif direction == 'u':
                y -= 1
            elif direction == 'd':
                y += 1

            if x < 0 or y < 0 or x >= len(mirror_map[0]) or y >= len(mirror_map):
                continue

            new_beams_of_beam = get_new_beams((x, y), direction)
            for new_beam in new_beams_of_beam:
                if new_beam[0] in visited_directions and new_beam[1] in visited_directions[new_beam[0]]:
                    continue
                else:
                    visited_directions[new_beam[0]].append(new_beam[1])
                    visited_matrix[new_beam[0][1]][new_beam[0][0]] = True
                    new_beams.append(new_beam)

        beams = new_beams

    if count_visited() > max_count:
        max_count = count_visited()

for i in range(len(mirror_map)):
    visited_matrix = [[False for _ in range(len(mirror_map[0]))] for _ in range(len(mirror_map))]
    visited_directions = defaultdict(list)
    beams = [((-1, i), 'r')]

    while len(beams) > 0:
        new_beams = []
        for beam in beams:
            x, y = beam[0]
            direction = beam[1]
            if direction == 'r':
                x += 1
            elif direction == 'l':
                x -= 1
            elif direction == 'u':
                y -= 1
            elif direction == 'd':
                y += 1

            if x < 0 or y < 0 or x >= len(mirror_map[0]) or y >= len(mirror_map):
                continue

            new_beams_of_beam = get_new_beams((x, y), direction)
            for new_beam in new_beams_of_beam:
                if new_beam[0] in visited_directions and new_beam[1] in visited_directions[new_beam[0]]:
                    continue
                else:
                    visited_directions[new_beam[0]].append(new_beam[1])
                    visited_matrix[new_beam[0][1]][new_beam[0][0]] = True
                    new_beams.append(new_beam)

        beams = new_beams

    if count_visited() > max_count:
        max_count = count_visited()

for i in range(len(mirror_map)):
    visited_matrix = [[False for _ in range(len(mirror_map[0]))] for _ in range(len(mirror_map))]
    visited_directions = defaultdict(list)
    beams = [((len(mirror_map[0]), i), 'l')]

    while len(beams) > 0:
        new_beams = []
        for beam in beams:
            x, y = beam[0]
            direction = beam[1]
            if direction == 'r':
                x += 1
            elif direction == 'l':
                x -= 1
            elif direction == 'u':
                y -= 1
            elif direction == 'd':
                y += 1

            if x < 0 or y < 0 or x >= len(mirror_map[0]) or y >= len(mirror_map):
                continue

            new_beams_of_beam = get_new_beams((x, y), direction)
            for new_beam in new_beams_of_beam:
                if new_beam[0] in visited_directions and new_beam[1] in visited_directions[new_beam[0]]:
                    continue
                else:
                    visited_directions[new_beam[0]].append(new_beam[1])
                    visited_matrix[new_beam[0][1]][new_beam[0][0]] = True
                    new_beams.append(new_beam)

        beams = new_beams

    if count_visited() > max_count:
        max_count = count_visited()

print('part2', max_count)

# 8673 too low