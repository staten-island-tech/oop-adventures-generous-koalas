
from hero import Hero

class Hero:
    def __init__(self, name, health, damage, coins):
        self.name = name
        self.health = health
        self.damage = damage
        self.coins = coins
        self.inventory = []

    def earn_coins(self, amount):
        self.coins += amount
        print(f"{self.name} earned {amount} coins!")

    def acquire_item(self, item):
        self.inventory.append(item)
        print(f"{self.name} received a {item['name']}!")
        
    def use_health_potion(self):
        for item in self.inventory:
            if item['name'] == "Health Potion":
                self.health += item['effect']
                print(f"{self.name} used a Health Potion and gained {item['effect']} health. Current health: {self.health}")
                return True
        print(f"{self.name} doesn't have any Health Potions.")
        return False

    def use_damage_potion(self):
        for item in self.inventory:
            if item['name'] == "Damage Potion":
                self.damage += item['effect']
                print(f"{self.name} used a Damage Potion and increased damage by {item['effect']}. Current damage: {self.damage}")
                return True
        print(f"{self.name} doesn't have any Damage Potions.")
        return False

    def display_inventory(self):
        print(f"{self.name}'s Inventory: {self.inventory}")

class Merchant:
    def __init__(self, items):
        self.items = items

    def display_items(self):
        print("Merchant: Welcome, adventurer! Take a look at my wares:")
        for idx, item in enumerate(self.items, start=1):
            print(f"{idx}. {item['name']} - Cost: {item['cost']} coins")

    def sell_item(self, hero):
        self.display_items()
        choice = input("Enter the number of the item you want to purchase (or '0' to exit): ")

        try:
            choice = int(choice)
            if 0 < choice <= len(self.items):
                selected_item = self.items[choice - 1]

                if hero.coins >= selected_item['cost']:
                    hero.coins -= selected_item['cost']
                    hero.acquire_item(selected_item)
                    return selected_item
                else:
                    print(f"{hero.name} doesn't have enough coins to buy {selected_item['name']}.")
            elif choice != 0:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

        return None

hero = Hero(name="Cornelius", health=200, damage=15, coins=50)

merchant_items = [
    {"name": "Health Potion", "cost": 25, "effect": 40},
    {"name": "Damage Potion", "cost": 25, "effect": 5},
]

merchant = Merchant(items=merchant_items)
item = merchant.sell_item(hero)

if item:
    print(f"Remaining coins: {hero.coins}")
    hero.display_inventory()

use = input("Do you want to use a Health Potion? (yes/no): ").lower()
if use == "yes":
    hero.use_health_potion()

use = input("Do you want to use a Damage Potion? (yes/no): ").lower()
if use == "yes":
    hero.use_damage_potion()