import random

class Hero():
    def __init__(self,health,damage,x,y,coins,weapon=None):
        self.health=health
        self.damage=damage
        self.x=x
        self.y=y
        self.coins=coins
        self.weapon=weapon
    def attack(self):
        if self.weapon:
            return random.randidnt(1,self.weapon.damage)
        else:
            return 1

