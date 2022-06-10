conversion = [('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90), ('L', 50), ('XL', 40), ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)]

def roman(number):
    roman_number = ''
    for k, v in conversion:
        while v <= number:
            roman_number += k
            number -= v
    return roman_number
    
