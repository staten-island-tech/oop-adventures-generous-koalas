import random
from hero import Hero
class Potion:
    def _init_ (self, name, effect):
        self.name = name
        self.effect = effect
class Merchant:
    def _init_(self,available_items):
        self.available_items=available_items
    def buy(self, Hero):
        item = random.choice(items)
        items = ["Health Potion", "Damage Potion"]

        if item == "Health Potion":
            Potion = random.choice(self.available_items)
            print(f"Merchant: Welcome adventurer! I have some items for sale: {item}")

        if response == 'Yes':
            if item == "Health Potion":
                Hero.items = items
            else: 


