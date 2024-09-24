import random
test_case = [['9H', '8H', '7H', '6H', '5H'],
            ['AH', 'AS', 'AD', 'AC', '7D'],
            ['KH', 'KS', 'KD', '7S', '7C'],
            ['2D', '7D', '9D', 'JD', 'QD'],
            ['5C', '6H', '7S', '8D', '9H'],
            ['JC', 'JH', 'JS', '2D', '6H'],
            ['8C', '8D', '5S', '5H', 'KC'],
            ['9H', '9D', '3S', '7C', '5H'],
            ['KH', '9S', '6D', '4C', '2H']]

rank_names = ["high card", "pair", "two pair", "three of a kind", "straight", "flush", "full house", "four of a kind", "straight flush"]

#numeric value of a card
def value(card):
    if card[0] == "A":
        return 14
    if card[0] == "K":
        return 13
    if card[0] == "Q":
        return 12
    if card[0] == "J":
        return 11
    return int(card[0:-1])

#symbol of a card
def suit(card):
    return card[-1]

#checking flush
def is_flush(cards):
    return all([suit(card) == suit(cards[0]) for card in cards[1:]])

#checking if the flush checker works
# print([is_flush(hand) for hand in test_case])

#arranging the cards sequentially and seeing their frequency in each hand
def hand_dist(cards):
    dist = {i:0 for i in range(2,15)}
    for card in cards:
        dist[value(card)] += 1
    return dist

#ensuring hand_dist function
# for case in test_case:
#     print(hand_dist(case))

#straight with high card
def straight_high_card(cards):
    dist = hand_dist(cards)
    for val in range(2,11):
        if all([dist[val + i] == 1 for i in range(5)]):
            return val + 4
    return None

#ensuring straight_high_card function
# for case in test_case:
#     print(straight_high_card(case))

#counting cards for one pair or 3/4 of a kind
def card_count(cards, num, but = None):
    dist = hand_dist(cards)
    for i in range(2,15):
        if i == but:
            continue
        if dist[i] == num:
            return i
    return None

#ensuring card_count_function
# for case in test_case:
#     print(card_count(case, 3))

#hands ranking
def hands_ranking(cards):
    if straight_high_card(cards) is not None and is_flush(cards):
        return 8
    if card_count(cards, 4) is not None:
        return 7
    if card_count(cards, 3) is not None and card_count(cards, 2) is not None:
        return 6
    if is_flush(cards):
        return 5
    if straight_high_card(cards) is not None:
        return 4
    if card_count(cards, 3):
        return 3
    one_pair = card_count(cards, 2)
    if one_pair is not None:
        if card_count(cards, 2, one_pair) is not None:
            return 2
        return 1
    return 0

# for case in test_case:
#     print(hands_ranking(case))

#comparing two hands
def compare_hands(hand1, hand2):
    r1 = hands_ranking(hand1)
    r2 = hands_ranking(hand2)
    if r1 < r2:
        return -1
    if r1 > r2:
        return 1
    return 0

def make_deck():
    top_four = ("J","Q","K","A")
    deck = []
    for symbol in ("D","C","H","S"):
        for val in range(2, 15):
            if val < 11:
                val_string = str(val)
            else:
                val_string = top_four[val - 11]
            deck.append(val_string + symbol)
    return deck

#shuffler
def shuffle():
    deck = make_deck()
    random.shuffle(deck)
    return deck

#dealing cards
def deal(deck, n):
    hand = deck[0:n]
    del deck[0:n]
    return hand

def show_compared_hands(hand1, hand2):
    sgn = compare_hands(hand1, hand2)
    result = ("loses to", "ties", "beats")[sgn + 1]
    r1 = hands_ranking(hand1)
    r2 = hands_ranking(hand2)
    print(f"{rank_names[r1]} {result} {rank_names[r2]}")

# deck = shuffle()
# hand1 = deal(deck, 5)
# hand2 = deal(deck, 5)
# print(hand1, hand2)
#
# show_compared_hands(hand1, hand2)

def test_random_hands(n=20):
    for i in range(20):
        deck = shuffle()
        hand1 = deal(deck, 5)
        hand2 = deal(deck, 5)
        print(hand1, hand2)
        show_compared_hands(hand1, hand2)

test_random_hands()

