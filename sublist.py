"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3


def sublist(list_a, list_b):
    if list_a == list_b:
        return EQUAL
    for i in range(len(list_b) - len(list_a) + 1):
        if list_a == list_b[i:i + len(list_a)]:
           return SUBLIST 
    for i in range(len(list_a) - len(list_b) + 1):
        if list_b == list_a[i:i + len(list_b)]:
           return SUPERLIST 
    return UNEQUAL
    
    
    
   
