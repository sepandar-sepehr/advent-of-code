from math import prod

all_wires = []
with open('d25_input', 'r') as f:
    for line in f:
        line = line.strip()
        from_comp = line.split(':')[0]
        to_comp = line.split(':')[1].split()
        for comp in to_comp:
            all_wires.append((from_comp, comp))
print(all_wires)


def get_groups(wires):
    groups = []
    for wire in wires:
        found = False
        for group in groups:
            if wire[0] in group or wire[1] in group:
                group.add(wire[0])
                group.add(wire[1])
                found = True
                break
        if not found:
            groups.append({wire[0], wire[1]})

    for i in range(len(groups)):
        j = i+1
        while j < len(groups):
            if groups[i].intersection(groups[j]):
                groups[i] = groups[i].union(groups[j])
                groups[j] = set()
                j = i+1 # restart checking since groups[i] might now intersect with other groups
            else:
                j += 1
    groups = [g for g in groups if g]
    return groups

for i, wire1 in enumerate(all_wires):
    for j, wire2 in enumerate(all_wires[i+1:]):
        for wire3 in all_wires[i+j+2:]:
            tmp_wires = all_wires.copy()
            # print(wire1, wire2, wire3)
            # print(tmp_wires)
            tmp_wires.remove(wire1)
            tmp_wires.remove(wire2)
            tmp_wires.remove(wire3)
            # print(tmp_wires)
            groups = get_groups(tmp_wires)
            if len(groups) == 2:
                print('wires cut', wire1, wire2, wire3)
                print('groups', groups)
                print('Part 1: ', prod(len(g) for g in groups))
                exit()

