from functools import cmp_to_key

card_bids = []
with open('d7_input', 'r') as file:
    for line in file:
        card_bids.append((line.split()[0], int(line.split()[1])))
print(card_bids)


def is_5(card):
    return card.count(card[0]) == 5


def is_4(card):
    return card.count(card[0]) == 4 or card.count(card[1]) == 4


def is_full(card):
    return len(set(card)) == 2 and not is_4(card)


def is_3(card):
    if is_full(card):
        return False
    return card.count(card[0]) == 3 or card.count(card[1]) == 3 or card.count(card[2]) == 3


def is_2_pair(card):
    return len(set(card)) == 3 and not is_3(card)


def is_pair(card):
    return len(set(card)) == 4


def is_high_card(card):
    return len(set(card)) == 5


card_order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
def second_order(card1, card2):
    for i in range(5):
        if card_order.index(card1[i]) < card_order.index(card2[i]):
            return 1
        if card_order.index(card1[i]) > card_order.index(card2[i]):
            return -1

    print('WHAAAAT?')


def compare_cards(card_bid1, card_bid2):
    card1 = card_bid1[0]
    card2 = card_bid2[0]

    if is_5(card1) and is_5(card2) or \
            is_4(card1) and is_4(card2) or \
            is_full(card1) and is_full(card2) or \
            is_3(card1) and is_3(card2) or \
            is_2_pair(card1) and is_2_pair(card2) or \
            is_pair(card1) and is_pair(card2) or \
            is_high_card(card1) and is_high_card(card2):
        return second_order(card1, card2)

    if is_5(card1):
        return 1
    if is_5(card2):
        return -1

    if is_4(card1):
        return 1
    if is_4(card2):
        return -1

    if is_full(card1):
        return 1
    if is_full(card2):
        return -1

    if is_3(card1):
        return 1
    if is_3(card2):
        return -1

    if is_2_pair(card1):
        return 1
    if is_2_pair(card2):
        return -1

    if is_pair(card1):
        return 1
    if is_pair(card2):
        return -1

    print("whaat whaat")


sorted_card_bids = sorted(card_bids, key=cmp_to_key(compare_cards))
print(sorted_card_bids)

res = 0
for i, card_bid in enumerate(sorted_card_bids):
    res += card_bid[1] * (i+1)
print(res)

