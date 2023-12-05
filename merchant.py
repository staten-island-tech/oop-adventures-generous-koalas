class merchant:
    def __init__(self,name,coins,inventory):
        self.name=name
        self.coins=coins
        self.inventory=inventory
    def buy(self,item):
        self.inventory.append(item)
        print (self.inventory)

