def get_rounds(number):
    """

     :param number: int - current round number.
     :return: list - current round and the two that follow.
    """

    round_list = [number]
    round_list.append(number + 1)
    round_list.append(number + 2)
    return round_list

def concatenate_rounds(round_1, rounds_2):
    """

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    
    return round_1 + rounds_2    

def list_contains_round(rounds, number):
    """

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    """

    if number in rounds:
        return True
    return False
   
def card_average(hand):
    """

    :param hand: list - cards in hand.
    :return:  float - average value of the cards in the hand.
    """

    return sum(hand) / len(hand)

def approx_average_is_average(hand):
    """

    :param hand: list - cards in hand.
    :return: bool - if approximate average equals to the `true average`.
    """

    first_hand = sum(hand) / len(hand)
    second_hand = (hand[0] + hand[-1]) / 2
    third_hand = hand[round(len(hand)/2)]
    return first_hand in (second_hand, third_hand)

def average_even_is_average_odd(hand):
    """

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    even = []
    odd = []

    for card in hand:
        if card % 2 == 0:
            even.append(card)
        else:
            odd.append(card)
    return card_average(even) == card_average(odd)

def maybe_double_last(hand):
    """

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if hand[-1] == 11:
        hand[-1] = 22
    return hand    
    
