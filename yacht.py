# Score categories.
# Change the values as you see fit.
YACHT = 50
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = "FULL_HOUSE"
FOUR_OF_A_KIND = "OUR_OF_A_KIND"
LITTLE_STRAIGHT = "LITTLE_STRAIGHT"
BIG_STRAIGHT = "BIG_STRAIGHT"
CHOICE = "CHOICE"


def score(dice, category):
    combination = set(dice)
    element = max(dice, key=dice.count)
    occurrence = dice.count(element)
    
    if category in (ONES, TWOS, THREES, FOURS, FIVES, SIXES):
        return dice.count(category) * category
    elif category == FULL_HOUSE and occurrence == 3:
        return sum(dice)
    elif category == FOUR_OF_A_KIND and occurrence >= 4:
        return element * 4
    elif category == LITTLE_STRAIGHT and combination == {1, 2, 3, 4, 5}:
        return 30
    elif category == BIG_STRAIGHT and combination == {2, 3, 4, 5, 6}:
        return 30
    elif category == FULL_HOUSE and occurrence == 3: 
        return sum(dice)
    elif category == CHOICE:
        return sum(dice)
    elif category == YACHT and occurrence == 5:
        return 50
    else:
        return 0
    
    
