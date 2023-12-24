# this is inspired by https://aoc-puzzle-solver.streamlit.app
# Instead of modifying the code to solve infinite copies of the map, I just modified the input map to have 3 copies since that's all I needed
import numpy as np


with open('d21_input', 'r') as file:
    input_map = [[c for c in line.strip()] for line in file.readlines()]


start = (0, 0)
for y, line in enumerate(input_map):
    for x, c in enumerate(line):
        if c == 'S':
            start = (x, y)
            break

reached = {start}
input_map[start[1]][start[0]] = '.'


def find_new_reached():
    new_reached = set([])
    for x, y in reached:
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= x + dx < len(input_map[0]) and 0 <= y + dy < len(input_map):
                if input_map[y + dy][x + dx] == '.':
                    new_reached.add((x + dx, y + dy))
    return new_reached


def clear_reached():
    for i in range(len(input_map)):
        for j in range(len(input_map[0])):
            if input_map[i][j] == 'O':
                input_map[i][j] = '.'


def plot_map():
    for i in range(len(input_map)):
        print(''.join(input_map[i]))
    print('')


def count_plots():
    return sum([sum([1 if c == 'O' else 0 for c in line]) for line in input_map])


n = 65+131*2
plotted_counts = []
crossing_counts = []
for i in range(n):
    new_reached = find_new_reached()
    clear_reached()
    for x, y in new_reached:
        input_map[y][x] = 'O'
    reached = new_reached
    plotted = count_plots()
    plotted_counts.append(plotted)
    if (i+1) % 131 == 65:
        crossing_counts.append(plotted)
    # print('{},{}'.format(i+1, plotted))
    # plot_map()
    # print(i+1)

print(crossing_counts)
x_data = [0, 1, 2]
p = np.polyfit(x=x_data, y=crossing_counts, deg=2)
f = np.poly1d(p)

x_new = 26501365 // 131
y_predicted = f(x_new)
print(f"Predicted value at x = {x_new} is y = {y_predicted.round()}")
