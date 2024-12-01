left = list()
right = list()
with open('d1_input', 'r') as file:
    for line in file:
        x = ([int(i) for i in line.split()])
        left.append(x[0])
        right.append(x[1])

left.sort()
right.sort()
sum = 0
for i in range(len(left)):
    sum += abs(right[i] - left[i])
print('part 1: ', sum)


sum = 0
for num in left:
    sum += num * len([n for n in right if n == num])
print('part 2: ', sum)