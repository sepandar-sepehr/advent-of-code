from collections import defaultdict

workflows = {}
ratings = []
with open('d19_input', 'r') as file:
    for line in file:
        if line.strip() == '':
            break
        id = line.strip().split('{')[0]
        workflows[id] = line.strip().split('{')[1][:-1].split(',')

    for line in file:
        rating_row = {}
        ratings_str = line.strip()[1:-1].split(',')
        for rating_str in ratings_str:
            [id, rating] = rating_str.split('=')
            rating_row[id] = int(rating)

        ratings.append(rating_row)

print(workflows)
print(ratings)


def check_workflow(rating, workflow):
    for rule in workflow:
        if len(rule.split(':')) == 1:
            return rule

        [condition, target] = rule.split(':')
        id = condition[0]
        if condition[1] == '<':
            if rating[id] < int(condition[2:]):
                return target
        elif condition[1] == '>':
            if rating[id] > int(condition[2:]):
                return target
        else:
            raise Exception('Unknown condition')


def is_accepted(rating):
    cur_id = 'in'
    while cur_id not in ['A', 'R']:
        cur_id = check_workflow(rating, workflows[cur_id])
    return cur_id == 'A'


def rating_sum(rating):
    res = 0
    for k, v in rating.items():
        res += v

    return res


res = 0
for rating in ratings:
    if is_accepted(rating):
        res += rating_sum(rating)

print('Part1:', res)

# BF solution is too slow
# p2_res = 0
# for i in range(1, 4001):
#     for j in range(1, 4001):
#         for k in range(1, 4001):
#             for l in range(1, 4001):
#                 rating = {'x': i, 'm': j, 'a': k, 's': l}
#                 if is_accepted(rating):
#                     p2_res += 1


def negate_workflow_rule(rule):
    condition = rule.split(':')[0]
    return condition[0] + ('>' if condition[1] == '<' else '<') + (str(int(condition[2:])-1) if  condition[1] == '<' else str(int(condition[2:])+1))


queue = [([], workflows['in'])]
accepted_conditions = []
while len(queue) > 0:
    print(queue)
    (conditions_so_far, workflow) = queue.pop()
    for rule in workflow:
        if len(rule.split(':')) == 1:
            if rule == 'A':
                accepted_conditions.append(conditions_so_far)
                continue
            elif rule == 'R':
                continue
            else:
                queue.append((conditions_so_far, workflows[rule]))
        else:
            [condition, target] = rule.split(':')
            if target == 'A':
                accepted_conditions.append(conditions_so_far+[condition])
            elif target == 'R':
                pass
            else:
                queue.append((conditions_so_far + [condition], workflows[target]))
            conditions_so_far.append(negate_workflow_rule(rule))

print('accepted_conditions', accepted_conditions)


def calc_acceptable(conditions):
    res = 1
    conditions_by_key = defaultdict(list)
    for condition in conditions:
        id = condition[0]
        conditions_by_key[id].append(condition)

    for id, key_conditions in conditions_by_key.items():
        min = 0
        max = 4001
        for condition in key_conditions:
            if condition[1] == '<':
                if int(condition[2:]) < max:
                    max = int(condition[2:])
            else:
                if int(condition[2:]) > min:
                    min = int(condition[2:])
        if min >= max:
            return 0
        res *= (max - min - 1)

    res *= 4000**(4 - len(conditions_by_key))
    print(res, conditions)
    return res


p2_res = 0
for accepted_condition in accepted_conditions:
    p2_res += calc_acceptable(accepted_condition)


print('Part2:', p2_res)
