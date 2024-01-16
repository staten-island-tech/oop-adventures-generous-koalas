##from anthony's file, apparently it doesn't work, look at it later 

class Inventory:
    def __init__(self):
        self.items = []


    def add_item(self, item):
        self.items.append(item)


    def remove_item(self, item):
        self.items.remove(item)


    def display_inventory(self):
        print("Inventory:")
        for idx, item in enumerate(self.items, start=1):
            print(f"{idx}. {item['name']}")


class Hero:
    def __init__(self, name, health, damage, coins):
        self.name = name
        self.health = health
        self.damage = damage
        self.coins = coins
        self.inventory = Inventory()
 

    def earn_coins(self, amount):
        self.coins += amount
        print(f"{self.name} earned {amount} coins!")


    def acquire_item(self, item):
        self.inventory.add_item(item)
        print(f"{self.name} received a {item['name']}!")


    def use_health_potion(self):
        for item in self.inventory.items:
            if item['name'] == "Health Potion":
                self.health += item['effect']
                print(f"{self.name} used a Health Potion and gained {item['effect']} health. Current health: {self.health}")
                self.inventory.remove_item(item)
                return True
        print(f"{self.name} doesn't have any Health Potions.")
        return False


    def use_damage_potion(self):
        for item in self.inventory.items:
            if item['name'] == "Damage Potion":
                print(f"{self.name} used a Damage Potion and dealt 40 damage to the zombie!")
                self.inventory.remove_item(item)
                return True
        print(f"{self.name} doesn't have any Damage Potions.")
        return False


    def display_inventory(self):
        self.inventory.display_inventory()


class Merchant:
    def __init__(self, items):
        self.items = items


    def display_items(self):
        print("Merchant: Welcome, adventurer! Take a look at my wares:")
        for idx, item in enumerate(self.items, start=1):
            print(f"{idx}. {item['name']} - Cost: {item['cost']} coins")


    def sell_item(self, hero):
        while True:
            self.display_items()
            choice = input("Enter the number of the item you want to purchase (or '0' to exit): ")


            try:
                choice = int(choice)
                if 0 < choice <= len(self.items):
                    selected_item = self.items[choice - 1]


                    if hero.coins >= selected_item['cost']:
                        hero.coins -= selected_item['cost']
                        hero.acquire_item(selected_item)
                        print(f"{hero.name} bought {selected_item['name']}!")
                    else:
                        print(f"{hero.name} doesn't have enough coins to buy {selected_item['name']}.")


                elif choice == 0:
                    return None 
                else:
                    print("Invalid choice. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

class ZombieGame:
    def __init__(self):
        self.hero = Hero(name="Cornelius", health=100, damage=15, coins=25)
        self.merchant_items = [
            {"name": "Health Potion", "cost": 25, "effect": 40},
            {"name": "Damage Potion", "cost": 25, "effect": 0},  
        ]
        self.merchant = Merchant(items=self.merchant_items)


    def play(self):
        item = self.merchant.sell_item(self.hero)
        if item:
            print(f"Remaining coins: {self.hero.coins}")
            self.hero.display_inventory()



        self.hero.display_inventory()


game = ZombieGame()
game.play()


import random
from hero import Hero

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


class Potion:
    def _init_(self, name, cost):
        self.name = name
        self.cost = cost

class HealthPotion(Potion):
    def _init_(self, name, healing, cost):
        super()._init_(name,cost)
        self.healing = healing

class DamagePotion(Potion):
    def _init_(self,name, damage, cost):
        super()._init_(name,cost)
        self.damage = damage


class Merchant:
    def _init(self,items):
        self.items = items
    
    def offer_item(self):
        item = random.choice(self.items)
        if isinstance(item, HealthPotion):
            print(f"Merchant: Welcome, {Hero.name}! I have an item on sale for you: {item.name} - Healing: {item.healing} - Cost: {item.cost}.")
        elif isinstance(item, DamagePotion):
            print(f"Merchant: Welcome, {Hero.name}! I have an item on sale for you: {item.name} - Damage Boost: {item.damage_boost} - Cost: {item.cost}")

Hero = Hero(name="Cameron", health = 200, coins= 100, damage = 15 )
merchant = Merchant(items = [
    HealthPotion(name="Health Potion", healing=40, cost = 25)
    DamagePotion(name="Damage Potion", damage_boost=5, cost= 25)
])
