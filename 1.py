
import random

class Hero:
    def __init__(self, name, health, damage, coins):
        self.name = name
        self.health = health
        self.damage = damage
        self.coins = coins

    def attack(self):
        return self.damage

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def earn_coins(self, amount):
        self.coins += amount
        print(f"{self.name} earned {amount} coins!")

class Enemy:
    def __init__(self, name, health, damage, reward):
        self.name = name
        self.health = health
        self.damage = damage
        self.reward = reward

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

                if selected_item['name'] == "Health Potion" or "Damage Potion" and hero.coins >= selected_item['cost']:
                    hero.coins -= selected_item['cost']
                    print(f"{hero.name} purchased {selected_item['name']} for {selected_item['cost']} coins.")
                    return selected_item
                else:
                    print(f"{hero.name} doesn't have enough coins to buy {selected_item['name']}.")
            elif choice != 0:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

        return None

def print_status(hero, zombies):
    print(f"{hero.name}'s Health: {hero.health} | Coins: {hero.coins}")
    print("Zombies:")
    for zombie in zombies:
        print(f"{zombie.name} - Health: {zombie.health} | Damage: {zombie.damage}")

def hero_turn(hero, zombies, merchant):
    print("\nHero's Turn:")
    print_status(hero, zombies)

    print("1. Continue")
    print("2. Visit Merchant")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        print("You move on")

    elif choice == '2':
        item = merchant.sell_item(hero)
        if item:
            print(f"{hero.name} received a {item['name']}!")

def zombies_turn(hero, zombies):
    print("\nZombies' Turn:")
    for zombie in zombies:
        damage_taken = zombie.damage
        hero.take_damage(damage_taken)
        print(f"{zombie.name} attacks {hero.name} and deals {damage_taken} damage!")

def main():
    hero = Hero(name="Cornelius", health=200, damage=15, coins=50)
    zombies = [Enemy(name="Zombie1", health=100, damage=10, reward=20)]
    merchant_items = [
        {"name": "Health Potion", "cost": 25},
        {"name": "Damage Potion", "cost": 25},
    ]
    merchant = Merchant(items=merchant_items)

    while hero.health > 0 and zombies:
        hero_turn(hero, zombies, merchant)
        zombies_turn(hero, zombies)

    if hero.health <= 0:
        print(f"{hero.name} has been defeated. Game over!")
    else:
        print(f"{hero.name} defeated all the zombies! You win!")

if __name__ == "__main__":
    main()
