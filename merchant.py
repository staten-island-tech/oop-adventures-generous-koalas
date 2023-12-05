import random
from hero import Hero
class Merchant:
    def _init_(self,x,y,available_weapons):
        self.x=x
        self.y=y
        self.available_weapons=available_weapons
    def buy(self,hero):
        items = ["Health Potion", "Damage Potion"]
        item = random.choice(items)

        if item == "Health Potion":
            health = random.choice(self.available_weapons)
            print(f"Merchant: Welcome! I have a health potion for sale!")
        r = input("Do you want to buy it? (Yes/No):")

        if r == 'Yes':
            if item == "Health Potion":
                hero.health = health
            else:
                hero.currency == 25
                print ("Merchant:Thank you for your purchase")
            return True
        else:
            print("Merchant:Maybe some other time! Thank you")

    