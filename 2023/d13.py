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
print(patterns)

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


res = 0
for idx, pattern in enumerate(patterns):
    for i in range(0, len(pattern)):
        if is_mirror_at_row(pattern, i):
            res += 100 * (i + 1)
            print('row', idx, i)

    for i in range(0, len(pattern[0])):
        if is_mirror_at_col(pattern, i):
            res += i + 1
            print('col', idx, i)


print('part1', res)

# 25747 too low