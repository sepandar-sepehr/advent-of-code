from collections import defaultdict

LOW = 'Low'
HIGH = 'High'

flip_flops = {}
flip_flop_states = {}
conjunctions = {}
conjunction_states = defaultdict(dict)
with open('d20_input', 'r') as file:
    # Have to make sure it's the first line
    broadcaster_receivers = file.readline().strip().split(' -> ')[1].split(', ')
    for line in file:
        if line[0] == '%':
            flip_flop = line.split(' -> ')[0][1:]
            receivers = line.strip().split(' -> ')[1].split(', ')
            flip_flops[flip_flop] = receivers
            flip_flop_states[flip_flop] = False
        else:
            conjunction = line.split(' -> ')[0][1:]
            receivers = line.strip().split(' -> ')[1].split(', ')
            conjunctions[conjunction] = receivers

for flip_flop, receivers in flip_flops.items():
    for receiver in receivers:
        if receiver in conjunctions:
            conjunction_states[receiver][flip_flop] = LOW
for conjunction, receivers in conjunctions.items():
    for receiver in receivers:
        if receiver in conjunctions:
            conjunction_states[receiver][conjunction] = LOW

def press_button(i):
    queue = []
    for receiver in broadcaster_receivers:
        queue.append((receiver, LOW, 'button'))
    while queue:
        (cur_id, cur_pulse, sender) = queue.pop(0)
        if cur_id in flip_flops:
            if cur_pulse == HIGH:
                continue
            else:
                if flip_flop_states[cur_id]:
                    pulse_to_send = LOW
                    flip_flop_states[cur_id] = False
                else:
                    pulse_to_send = HIGH
                    flip_flop_states[cur_id] = True

                for receiver in flip_flops[cur_id]:
                    queue.append((receiver, pulse_to_send, cur_id))

        elif cur_id in conjunctions:
            conjunction_states[cur_id][sender] = cur_pulse
            if all([state == HIGH for state in conjunction_states[cur_id].values()]):
                pulse_to_send = LOW
            else:
                pulse_to_send = HIGH

            for receiver in conjunctions[cur_id]:
                queue.append((receiver, pulse_to_send, cur_id))
                if receiver == 'lg' and pulse_to_send == HIGH:
                    return True

        else:
            continue

    return False


for i in range(1, 10000):
    if press_button(i):
        print(i)
        break

# Manually grouped them into separate sets leading to `lg`, then run for each:
# sj set: 3881
# nk set: 3931
# sr set: 3851
# tp set: 3943
#  LCM of these:
# 231657829136023