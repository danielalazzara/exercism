import re


class PhoneNumber:
    def __init__(self, number):

        just_digits = self._strip(number)
        self._check_letters(number)
        self._check_punctuations(number)

        if len(just_digits) <= 9:
            raise ValueError("incorrect number of digits")
        if len(just_digits) > 11:
            raise ValueError("more than 11 digits")
        if len(just_digits) == 11 and just_digits[0] == "1":
            just_digits = just_digits[1:]
        if len(just_digits) == 11 and just_digits[0] != "1":
            raise ValueError("11 digits must start with 1")
        if just_digits[0] == "0":
            raise ValueError("area code cannot start with zero")
        if just_digits[0] == "1":
            raise ValueError("area code cannot start with one")
        if just_digits[3] == "0":
            raise ValueError("exchange code cannot start with zero")
        if just_digits[3] == "1":
            raise ValueError("exchange code cannot start with one")
        
        self.number = just_digits
        self.area_code = just_digits[0:3]
        

    def _strip(self, some_string):
        result = []
        for element in some_string:
            if element.isdigit():
                result.append(element)
        return "".join(result)


    def _check_letters(self, number):
        for i in number:
            if i.isalpha():
                raise ValueError("letters not permitted")

    def _check_punctuations(self, number):
        for i in number:
            if i in ['@', '!', ':']:
                raise ValueError("punctuations not permitted")


    def pretty(self):
        area_code, exchange_code, number = self.number[0:3], self.number[3:6], self.number[6:10]  
        return f"({area_code})-{exchange_code}-{number}"
