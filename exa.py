class Weapon():
    weapons = {
        'bow': {
           'damage': 5,
           'accuracy': 100
        },
        'axe': {
           'damage': 10,
           'accuracy': 50
        }
    }

    def __init__(self, weapon):
        # clean up the param a bit
        weapon = weapon.lower().strip()
        if weapon in self.weapons:
            self.name = self.weapons[weapon]
            self.damage = self.name['damage']
            self.accuracy = self.name['accuracy']
