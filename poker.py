from collections import defaultdict


value_card = dict(zip(['2','3','4','5','6','7','8','9','10','J','Q','K','A'], range(2,15)))

def best_hands(hands):
    if len(hands) == 1:
        return hands

    hand_dict = defaultdict()
    for hand in hands:
        parse_hand = [(card[:-1], card[-1]) for card in hand.split()]
        hand_ranks = [value_card[num] for num, suit in parse_hand]
        if sorted(hand_ranks) == [2,3,4,5,14]:
            hand_ranks = [5,4,3,2,1]
        hand_grouped = sorted([(hand_ranks.count(i),i) for i in set(hand_ranks)], reverse=True)
        counts, number = zip(*hand_grouped)

        straight = (len(counts) == 5 and max(number) - min(number) == 4)
        flush = len(set([suit for num, suit in parse_hand])) == 1
        if straight and flush:
            hand_dict[hand] = (8, number)
        elif counts == (4,1):
            hand_dict[hand] = (7, number)
        elif counts == (3,2):
            hand_dict[hand] = (6, number)
        elif flush:
            hand_dict[hand] = (5, number)
        elif straight:
            hand_dict[hand] = (4, number)
        elif counts == (3, 1, 1):
            hand_dict[hand] = (3, number)
        elif counts == (2, 2, 1):
            hand_dict[hand] = (2, number)
        elif counts == (2, 1, 1, 1):
            hand_dict[hand] = (1, number)
        else:
            hand_dict[hand] = (0, number)

    currmax = max(hand_dict.values())
    return [hand_s for hand_s, val in hand_dict.items() if val == currmax]
