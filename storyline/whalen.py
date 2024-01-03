class Game():
    def movement(moveset):
        if moveset== "1":
                n = random.randint(1, 2)
                if n == 1:
                    print ("Good job! The zombie's hp dropped by 30, that hit hurt...-15 hp")
                    F.health = F.health-dmg
                    D.health=D.health-(dmg*2)
                    print("Your health is..",F.health)
                    v
                    print("The zombie's health is",D.health)
                elif n == 2:
                    print("You missed and the zombie attacked twice!!-20hp")
                    F.health = F.health-(zdmg*2)
                    print("Your health is..",F.health)
                    v
                    print("The zombie's health is",D.health)
                    v

            elif moveset=="2":
                print (random.choice(op2))
                if random.choice(op2) == ("Nice!The zombie's hp dropped by 15!"):
                    D.health=D.health-dmg
                    v
                    print("The zombie's health is",D.health)
                    v
                elif random.choice(op2) == ("You missed... the zombie bit you! -10hp"):
                    F.health=F.health-zdmg
                    v
                    print("Your health is....",F.health)
                    v  

            elif moveset=="3":
                if random.choice(op3) == ("You used your damage potion! The zombie's hp dropped by 30!"):
                    print("Nice!The zombie's hp dropped by 30!")
                    D.health=D.health-pdmg
                    v
                    print("The zombie's health is",D.health)
                    v
                elif random.choice(op3) == ("Your damage potion fell out of your hands atleast you managed to dodge the zombie's attack...."):
                    print("Your damage potion fell out of your hands atleast you managed to dodge the zombie's attack....")
                    D.health=D.health
                    F.health=F.health
                    v
                    print("Your health is....",F.health)
                    v  
                    print("The zombie's health is",D.health)
                    v

            elif moveset=="4":
                if random.choice(op4) == ("You used your healing potion! +40 hp"):
                    print("You used your healing potion! +40p!")
                    F.health=F.health+40
                    v
                    print("Your health is..",F.health)
                    v
                elif random.choice(op4) == ("Your potion fell out of your hands atleast you managed to dodge the zombie's attack...."):
                    print("Your potion fell out of your hands atleast you managed to dodge the zombie's attack....")
                    F.health=F.health
                    D.health=D.health
                    v
                    print("Your health is....",F.health)
                    v  
                    print("The zombie's health is",D.health)

Game.movement(2)