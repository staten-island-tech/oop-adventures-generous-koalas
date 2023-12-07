class Weapons:
    def __init__(self,name,damage,weaporange,inventory):
        self.name = name 
        self.damage = damage
        self.range = weaporange
        self.inventory = inventory
    def gain (self, item): 
        self.inventory.append(item)
        print (self.inventory)