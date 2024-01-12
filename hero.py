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

    def use_health_potion(self):
        for item in self.inventory:
            if item['name'] == "Health Potion":
                self.health += item['effect']
                print(f"{self.name} used a Health Potion and gained {item['effect']} health. Current health: {self.health}")
                self.inventory.remove(item)
                return True
        print(f"{self.name} doesn't have any Health Potions.")
        return False

    def use_damage_potion(self):
        for item in self.inventory:
            if item['name'] == "Damage Potion":
                self.damage += item['effect']
                print(f"{self.name} used a Damage Potion and increased damage by {item['effect']}. Current damage: {self.damage}")
                self.inventory.remove(item)
                return True
        print(f"{self.name} doesn't have any Damage Potions.")
        return False

    def display_inventory(self):
        print(f"{self.name}'s Inventory: {self.inventory}")
        
