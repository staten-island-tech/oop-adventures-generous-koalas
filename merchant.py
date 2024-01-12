
class Merchant:
    def __init__(self,name,coins,inventory): 
        self.name = name 
        self.coins= coins
        self.inventory = inventory
    def sell(self,item): 
        self.items.remove(item)
        print (f'you have purchased {item}') 
        print (self.items) 

import json 

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
Hero
