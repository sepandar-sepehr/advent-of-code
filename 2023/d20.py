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

def press_button():
    pulses_sent = {
        LOW: 1,
        HIGH: 0
    }
    queue = []
    for receiver in broadcaster_receivers:
        queue.append((receiver, LOW, 'button'))
        pulses_sent[LOW] += 1
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
                    pulses_sent[pulse_to_send] += 1
                    # print(cur_id, receiver, pulse_to_send, pulses_sent[pulse_to_send])

        elif cur_id in conjunctions:
            conjunction_states[cur_id][sender] = cur_pulse
            if all([state == HIGH for state in conjunction_states[cur_id].values()]):
                pulse_to_send = LOW
            else:
                pulse_to_send = HIGH

            for receiver in conjunctions[cur_id]:
                queue.append((receiver, pulse_to_send, cur_id))
                pulses_sent[pulse_to_send] += 1
                # print(cur_id, receiver, pulse_to_send, pulses_sent[pulse_to_send])

        else:
            # print('Unknown id: ', cur_id)
            continue

    return pulses_sent[LOW], pulses_sent[HIGH]


sum_low_pulses_sent, sum_high_pulses_sent = 0, 0
for i in range(1000):
    (low_pulses_sent, high_pulses_sent) = press_button()
    sum_low_pulses_sent += low_pulses_sent
    sum_high_pulses_sent += high_pulses_sent
res = sum_low_pulses_sent * sum_high_pulses_sent
print(sum_low_pulses_sent, sum_high_pulses_sent)
print('Part 1: ', res)
