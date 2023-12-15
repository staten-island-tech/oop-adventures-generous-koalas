class Hero: 
    def __init__(self,name,money,inventory):
        self.name = name 
        self.money = money
        self.inventory = inventory
    def buy(self,item):
        self.inventory.append(item)
        print (self.inventory)
    @staticmethod 
    def attack(): 
        print("I attack for 10 damage") 
Black_Sword = Hero("Black Sword", 50, 300)
print(f"you have earned the {Black_Sword.name}")
