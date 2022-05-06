import random
import string

class Robot:
    def __init__(self):
        self.name = self.name_re()

    def reset(self):
        self.name = self.name_re()
        
    def name_re(self):
        random.seed()
        letters = random.choices(string.ascii_uppercase, k=2)
        numbers = random.choices(string.digits, k=3)
        return ''.join(letters + numbers)
        
