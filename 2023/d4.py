import math
total = 0
cards_dict = {}
with open('d4_input', 'r') as file:
    line_no = 1
    for line in file:
        winning_nums = line.strip().split(':')[1].strip().split('|')[0].strip().split()
        nums = line.strip().split(':')[1].strip().split('|')[1].strip().split()
        cards_dict[line_no] = (winning_nums, (nums, 1))

        win = -1
        for num in nums:
            if num in winning_nums:
                win+=1
        if win>=0:
            total += math.pow(2, win)
        line_no += 1
print(total)


# Part 2
for (i, card_dict_tuple) in cards_dict.items():
    winning_nums = card_dict_tuple[0]
    nums_and_count = card_dict_tuple[1]
    nums = nums_and_count[0]
    wins = 0
    for num in nums:
        if num in winning_nums:
            wins += 1
    for n in range(1, wins+1):
        cards_dict[i + n] = (cards_dict[i + n][0], (cards_dict[i + n][1][0], cards_dict[i + n][1][1] + nums_and_count[1]))


total = 0
for card_dict_tuple in cards_dict.values():
    total += card_dict_tuple[1][1]
print(total)

