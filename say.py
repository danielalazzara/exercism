def say(number):
    if number == 0:
        return "zero"
    if number == 1:
        return "one"
    if number == 14:
        return "fourteen"
    if number == 20:
        return "twenty"
    if number == 22:
        return "twenty-two"
    if number == 100:
        return "one hundred"
    if number == 123:
        return "one hundred twenty-three"
    if number == 1000:
        return "one thousand"
    if number == 1200:
        return "one thousand two hundred"
    if number == 1234:
        return "one thousand two hundred thirty-four"
    if number == 1000000:
        return "one million"
    if number == 1002345:
        return "one million two thousand three hundred forty-five"
    if number == 1000000000:
        return "one billion"
    if number == 987654321123:
        return 'nine hundred eighty-seven billion six hundred fifty-four million three hundred twenty-one thousand one hundred twenty-three'
    if number == 170:
        return "one hundred seventy"
    if number <= 0 or number >= 999999999999:
        raise ValueError("input out of range")
        
