from random import randint


def modifier(constitution):
    return (constitution - 10) // 2


class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

        
    def ability(self):
        roll_dice = ([randint(1, 6) for x in range(0, 4)])
        roll_dice.remove(min(roll_dice))
        return sum(roll_dice)
      
