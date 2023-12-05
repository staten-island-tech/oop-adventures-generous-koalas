class Merchant:
    def __init__(self,name,coins,inventory): 
        self.name = name 
        self.coins= coins
        self.inventory = inventory
    def sell(self,item): 
        self.items.remove(item)
        print (f'you have purchased {item}') 
        print (self.items) 
