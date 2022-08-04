class Allergies:
    list_of_allergies = {'eggs':1, 'peanuts': 2, 'shellfish': 4, 'strawberries': 8, 'tomatoes': 16, 'chocolate': 32, 'pollen': 64, 'cats': 128}

    
    def __init__(self, score):
        self.score = score

        
    def allergic_to(self, item):
        return self.score & Allergies.list_of_allergies[item] != 0

      
    @property
    def lst(self):
        return [allergy for allergy in Allergies.list_of_allergies if self.allergic_to(allergy)]
      
