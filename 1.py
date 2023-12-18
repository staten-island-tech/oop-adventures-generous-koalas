from hero import Hero

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
                    print(f"{hero.name} purchased {selected_item['name']} for {selected_item['cost']} coins.")
                    hero.inventory.append(selected_item)
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
    print(f"{hero.name} received a {item['name']}!")
    print(f"Remaining coins: {hero.coins}")
    hero.display_inventory()


hero.use_health_potion()
hero.use_damage_potion()
