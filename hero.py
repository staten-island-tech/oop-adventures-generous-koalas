import random
## Create  Class for creating new dictionaries here
class Hero():
    def _init_(self,health, name, coins, damage):
        self.health=health
        self.damage=damage
        self.coins=coins
        self.name=name
        self.inventory = {
            "health_potions": [],
            "damage_potions": [],
        }
    def use_health_potion(self):
        if self.inventory['health_potions']:
            potion = self.inventory['health_potions'].pop()
            self.health += potion.healing
            print(f"{self.name} used {potion.name}. Health restored by {potion.healing}.")
        else:
            print("No health potions in inventory.")

    def use_damage_potion(self):
        if self.inventory['damage_potions']:
            potion = self.inventory['damage_potions'].pop()
            self.damage += potion.damage_boost
            print(f"{self.name} used {potion.name}. Damage boosted by {potion.damage_boost}.")
        else:
            print("No damage potions in inventory.")

        
