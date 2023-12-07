import random
from hero import Hero
class Merchant:
    def _init_(self,gold):
        self.gold = gold

    def buy_health_potion(self):
        if self.gold >= 25:
            self.gold -= 25
            return 50
        else:
            print("Not enough gold")
            return 0 
    def buy_damage_potion(self):
        if self.gold>= 25:
            self.gold -= 25
            return 5
        else: 
            print("Not enough gold")
            return 0 

starting_gold = 20

Merchant = Merchant(starting_gold)


