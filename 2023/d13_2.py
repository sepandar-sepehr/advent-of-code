patterns = []
mNo = 1
with open('d13_input', 'r') as file:
    pattern_buff = []
    for line in file:
        if line.strip() != '' and mNo == 1:
            pattern_buff.append([c for c in line.strip()])
        if line.strip() == '':
            patterns.append(pattern_buff)
            pattern_buff = []
    patterns.append(pattern_buff)

def is_mirror_at_row(pattern, idx):
    if idx == len(pattern)-1:
        return False
    for i in range(0, idx+1):
        if ((idx-i) >= 0 and (idx+i+1) < len(pattern)
                and pattern[idx+i+1] != pattern[idx-i]):
            return False
    return True

def col_match(pattern, idx1, idx2):
    for i in range(len(pattern)):
        if pattern[i][idx1] != pattern[i][idx2]:
            return False
    return True

def is_mirror_at_col(pattern, idx):
    if  idx == len(pattern[0])-1:
        return False
    for i in range(0, idx+1):
        if ((idx-i) >= 0 and idx+i+1 < len(pattern[0]) and
                not col_match(pattern, idx+i+1, idx-i)):
            return False
    return True


ref_lines = {}
for idx, pattern in enumerate(patterns):
    for i in range(0, len(pattern)):
        if is_mirror_at_row(pattern, i):
            ref_lines[idx] = ('row', i+1)

    for i in range(0, len(pattern[0])):
        if is_mirror_at_col(pattern, i):
            ref_lines[idx] = ('col', i+1)


def find_all_lines(pattern):
    res = []
    for i in range(0, len(pattern[0])):
        if is_mirror_at_col(pattern, i):
            res.append(('col', i + 1))

    for i in range(0, len(pattern)):
        if is_mirror_at_row(pattern, i):
            res.append(('row', i + 1))

    return res


def update_pattern_and_calculate(pattern, i, j, idx, res):
    original_value = pattern[i][j]
    pattern[i][j] = '#' if original_value == '.' else '.'

    new_ref_lines = find_all_lines(pattern)
    for new_ref_line in new_ref_lines:
        if new_ref_line[1] != ref_lines[idx][1] or new_ref_line[0] != ref_lines[idx][0]:
            res += new_ref_line[1] if new_ref_line[0] == 'col' else new_ref_line[1] * 100
            return res, True

    pattern[i][j] = original_value
    return res, False

res = 0
for idx, pattern in enumerate(patterns):
    found = False
    for i in range(len(pattern)):
        for j in range(len(pattern[0])):
            if not found:
                res, found = update_pattern_and_calculate(pattern, i, j, idx, res)
                if found:
                    break



print('part2', res)
