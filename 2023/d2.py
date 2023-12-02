input_lines = list()

def flatten(l):
    return [item for sublist in l for item in sublist]

total = 0
with open('d2_input', 'r') as file:
    for line in file:
        game_num = int(line.strip().split(':')[0].split(' ')[1])
        sets = line.strip().split(':')[1].strip().split(';')
        possible = True
        for set in sets:
            cubes = set.split(',')
            reds = 0
            blues = 0
            greens = 0
            for cube in cubes:
                color = cube.strip().split(' ')[1]
                count = int(cube.strip().split(' ')[0])
                if color == 'blue':
                    blues += count
                elif color == 'red':
                    reds += count
                else:
                    greens += count
            if reds > 12 or blues > 14 or greens > 13:
                possible = False
        if possible:
            total += game_num

print(total)

total = 0
with open('d2_input', 'r') as file:
    for line in file:
        game_num = int(line.strip().split(':')[0].split(' ')[1])
        sets = line.strip().split(':')[1].strip().split(';')
        min_red = 0
        min_green = 0
        min_blue = 0
        for set in sets:
            cubes = set.split(',')
            for cube in cubes:
                color = cube.strip().split(' ')[1]
                count = int(cube.strip().split(' ')[0])
                if color == 'blue':
                    if count > min_blue:
                        min_blue = count
                elif color == 'red':
                    if count > min_red:
                        min_red = count
                else:
                    if count > min_green:
                        min_green = count
        print(min_red , min_green , min_blue)
        total += (min_red * min_green * min_blue)
print(total)