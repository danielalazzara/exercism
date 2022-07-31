class Luhn:
    def __init__(self, card_num):
       self.card_num = card_num

    
    def valid(self):
        transformer = {'0':'0', '1':'2', '2':'4', '3':'6', '4':'8', '5':'1', '6':'3', '7':'5', '8':'7', '9':'9'}

        for i in self.card_num:
            if i.isalpha() or i in "-,_#$:%*":
                return False
        card = self.card_num.replace(" ", "")
        if len(card) <= 1:
            return False
        _card = list(card)
        for n, item in enumerate(card[::-1]):
            if n%2:
                print(_card[-(n+1)])
                _card[-(n+1)] = transformer[item] 
        card = _card
        card_sum = sum(int(i) for i in card)
        if card_sum % 10:
            return False
        else:
            return True
        
