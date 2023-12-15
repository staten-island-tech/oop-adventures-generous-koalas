import random

class Potion:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

class HealthPotion(Potion):
    def __init__(self, name, healing, cost):
        super().__init__(name, cost)
        self.healing = healing

class DamagePotion(Potion):
    def __init__(self, name, damagee, cost):
        super().__init__(name, cost)
        self.damage = damagee

class Hero:
    def __init__(self, name, health, coins, damage):
        self.name = name
        self.health = health
        self.coins = coins
        self.damage = damage
        self.inventory = {
            "health_potions": [],
            "damage_potions": []
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
            self.damagee += potion.damagee
            print(f"{self.name} used {potion.name}. Damage boosted by {potion.damagee}.")
        else:
            print("No damage potions in inventory.")



def earn_currency(self, amount):
        self.currency += amount
        print(f"{self.name} earned {amount} coins!")






class Merchant:
    def __init__(self, available_items):
        self.available_items = available_items

    def offer_item(self):
        print("Merchant: Welcome, adventurer! Take a look at my wares:")
        for idx, item in enumerate(self.available_items, start=1):
            if isinstance(item, HealthPotion):
                print(f"{idx}. {item.name} - Healing: {item.healing} - Cost: {item.cost} coins")
            elif isinstance(item, DamagePotion):
                print(f"{idx}. {item.name} - Damage Boost: {item.damagee} - Cost: {item.cost} coins")
            else:
                print(f"{idx}. {item}")

        choice = input("Enter the number of the item you want to purchase (or '0' to exit): ")
        try:
            choice = int(choice)
            if 0 < choice <= len(self.available_items):
                selected_item = self.available_items[choice - 1]

                if isinstance(selected_item, Potion) and hero.coins >= selected_item.cost:
                    hero.inventory[selected_item.name.lower() + "s"].append(selected_item)
                    print(f"{hero.name} purchased {selected_item.name} for {selected_item.cost} coins. Added to inventory!")
                    hero.currency -= selected_item.cost
                elif isinstance(selected_item, Potion):
                    print(f"{hero.name} doesn't have enough coins to buy {selected_item.name}.")
                else:
                    print("Merchant: Sorry, I don't sell that item.")
            elif choice != 0:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        return None  
    print("Inventory:")
    print(f"Health Potions: {len(Hero.inventory['health_potions'])}")
    print(f"Damage Potions: {len(Hero.inventory['damage_potions'])}")



hero = Hero(name="John", health=200, coins=50, damage=15)
merchant = Merchant(available_items=[
    HealthPotion(name="Health Potion", healing=5, cost=25),
    DamagePotion(name="Damage Potion", damagee=30, cost=25),
])
