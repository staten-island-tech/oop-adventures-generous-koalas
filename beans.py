import random
import time
from attacks import Hero
from attacks import Merchant

inventory= []

class Enemy():
    def __init__(self, name, health,damage,):
        self.name=name
        self.health=health
        self.damage=damage
    

y=("yes","yeah","y","Y","YES","Yes")
n=("no","nah","n","N","NO","No")
#Get classes in here,
#figure out how to determine whether the user has potions to use during the moves which will also determine how many the times they can use the move (for potions)
#need a certain multiplier for each attack and certain damages per weapons

fstart= ("You encounter a Zombie. FIGHT START.")
movedesc=("1)Charged attack.[2x your normal damage, 1/2 recoil],2)normal attack[normal damage, no recoil], 3)damage potion[+30 damage], 4)health potion[+40 health]")
op1=("Good job! The zombie's hp dropped by 30, that hit hurt... -15 hp","You missed and the zombie attacked twice!!-20hp")
op2=("Nice!The zombie's hp dropped by 15!","You missed... the zombie bit you! -10hp")
op3=("You used your damage potion! The zombie's hp dropped by 30!","Your damage potion fell out of your hands atleast you managed to dodge the zombie's attack....")
op4=("You used your healing potion! +40 hp","Your potion fell out of your hands atleast you managed to dodge the zombie's attack....")
op5=("Fight","fight","f","F","FIGHT")



class p1():
    def fight():
        print (fstart)
        print (movedesc)
        F=Hero("Blastoise",200,15,20)
        D=Enemy("Zombie",200,10)
        print (F.name)
        print ("Fight commence.")
        dmg=F.damage
        zdmg=D.damage
        pdmg=30
        v=time.sleep(1.5)
        while F.health>0:
            moveset=input ("-------\n1) Charged Attack, \n2) Normal Attack, \n3) Damage Potion,\n4)Healing Potion\n Enter the corresponding number:  ")
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

            if D.health==0:
                print("The Zombie died...")
                break

            if D.health<0:
                print("HERO WINS.")
                v
                print ("You got 25 coins from defeating this zombie!")
                F.coins+25
                print (F.coins)

            if F.health==0:
                print("You've died...")
                break
                    
            if F.health<0:
                print("ZOMBIE WINS.")
                v
                fight_again= input("-------\nWould you like to battle again or go to the shop?\n'Fight' to try again.)")
                if fight_again in op5:
                    return

p1.fight()

class p2():
    def fight2():
        print (fstart)
        print (movedesc)
        F=Hero("Blastoise",200,15,20)
        D=Enemy("Baby Zombie",100,5)
        print (F.name)
        print ("Fight commence.")
        dmg=F.damage
        zdmg=D.damage
        pdmg=30
        v=time.sleep(1.5)
        while F.health>0:
            moveset=input ("-------\n1) Charged Attack, \n2) Normal Attack, \n3) Damage Potion,\n4)Healing Potion\n Enter the corresponding number:  ")
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

            if D.health==0:
                print("The Zombie died...")
                break

            if D.health<0:
                print("HERO WINS.")
                v
                print ("You got 15 coins from defeating this zombie!")
                F.coins+15
                print (F.coins)

            if F.health==0:
                print("You've died...")
                break
                    
            if F.health<0:
                print("ZOMBIE WINS.")
                v
                fight_again= input("-------\nWould you like to battle again or go to the shop?\n'Fight' to try again.)")
                if fight_again in op5:
                    return

p2.fight2()

class p3():
    def fight3():
        print (fstart)
        print (movedesc)
        F=Hero("Blastoise",200,15,20)
        D=Enemy("Mama Zombie",250,20)
        print (F.name)
        print ("Fight commence.")
        dmg=F.damage
        zdmg=D.damage
        pdmg=30
        v=time.sleep(1.5)
        while F.health>0:
            moveset=input ("-------\n1) Charged Attack, \n2) Normal Attack, \n3) Damage Potion,\n4)Healing Potion\n Enter the corresponding number:  ")
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

            if D.health==0:
                print("The Zombie died...")
                break

            if D.health<0:
                print("HERO WINS.")
                v
                print ("You got 50 coins from defeating this zombie!")
                print ("You've made it onto the roof. ")
                F.coins+50
                print (F.coins)

            if F.health==0:
                print("You've died...")
                break
                    
            if F.health<0:
                print("ZOMBIE WINS.")
                v
                fight_again= input("-------\nWould you like to battle again or go to the shop?\n'Fight' to try again.)")
                if fight_again in op5:
                    return

p3.fight3() 

if ("Damage Potion") in inventory:
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
elif ("Damage Potion") not in inventory:
    print ("You have no damage potion....")

if ("Health Potion") in inventory:
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
elif ("Health Potion") not in inventory:
    print ("You have no healing potion....")