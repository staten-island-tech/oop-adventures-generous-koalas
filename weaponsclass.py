class Weapons(): 
    def create (self):
        name = self.name 
        damage = self.damage 
        accuracy = self.accuracy
        weaponrange = self.weaponrange 

        weaponry = {"name": name, "damage rate": damage, "accuracy": accuracy, "range": weaponrange}
        return (weaponry) 
    

x = Weapons() 
x1 = x.create()






