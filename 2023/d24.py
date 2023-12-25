import numpy as np
from sympy import symbols, solve

pos_velocities = []
with open('d24_input', 'r') as file:
    for line in file:
        position1 = [int(val.strip()) for val in line.strip().split('@')[0].split(',')]
        velocities = [int(val.strip()) for val in line.strip().split('@')[1].split(',')]
        pos_velocities.append((position1, velocities))


def linear_equation_from_motion(x0, y0, speed_x, speed_y):
    a = speed_y / speed_x
    c = y0 - a * x0
    return a, c


def solve_system_of_linear_equations(a1, b1, c1, a2, b2, c2):
    A = np.array([[a1, b1], [a2, b2]])
    B = np.array([c1, c2])
    solution = np.linalg.solve(A, B)
    return solution


#     x0 + speed_x * t = solution_x
#     t = (solution_x - x0) / speed_x
def has_past(solution, positions, velocities):
    solution_x = solution[0]
    x0 = positions[0]
    speed_x = velocities[0]
    t = (solution_x - x0) / speed_x
    if t < 0:
        return True


min_xy = 200000000000000
max_xy = 400000000000000
valid_crosses = 0

for i, (position1, velocities) in enumerate(pos_velocities):
    for j, (positions, velocities2) in enumerate(pos_velocities):
        if i != j:
            a1, c1 = linear_equation_from_motion(position1[0], position1[1], velocities[0], velocities[1])
            a2, c2 = linear_equation_from_motion(positions[0], positions[1], velocities2[0], velocities2[1])
            if a1 == a2:
                continue
            solution = solve_system_of_linear_equations(a1, -1, -c1, a2, -1, -c2)
            print(f"The solution for {position1} and {positions} is x = {solution[0]}, y = {solution[1]}")
            if solution[0] >= min_xy and solution[0] <= max_xy and solution[1] >= min_xy and solution[1] <= max_xy:
                if has_past(solution, position1, velocities) or has_past(solution, positions, velocities2):
                    continue
                valid_crosses += 1

print('Part1:', valid_crosses // 2)


# Part 2 (inspired by https://www.youtube.com/watch?v=guOyA7Ijqgk&t=509s)
# Optimization possible but not necessary (see video)

rock_x, rock_y, rock_z, rock_vx, rock_vy, rock_vz = symbols('rock_x, rock_y, rock_z, rock_vx, rock_vy, rock_vz')
equations = []
for (position, velocities) in pos_velocities:
    hail_x, hail_y, hail_z = position
    hail_vx, hail_vy, hail_vz = velocities
    equations.append((rock_x - hail_x) * (hail_vy - rock_vy) - (rock_y - hail_y) * (hail_vx - rock_vx))
    equations.append((rock_y - hail_y) * (hail_vz - rock_vz) - (rock_z - hail_z) * (hail_vy - rock_vy))


solution = solve(equations)
print("Solution for part 2: rock_vx = {}, rock_vy = {}, rock_vz = {}, rock_x = {}, rock_y = {}, rock_z = {}".format(*solution[0].values()))
print('Part2:', solution[0][rock_x] + solution[0][rock_y] + solution[0][rock_z])
