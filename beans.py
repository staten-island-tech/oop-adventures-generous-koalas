import random
import time

class Hero():
    def __init__(self,name, health,damage,coins):
        self.name=name
        self.health=health
        self.damage=damage
        self.coins=coins

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

fstart= print("You encounter a Zombie. FIGHT START.")
movedesc=print("1)Charged attack.[2x your normal damage, 1/2 recoil],2)normal attack[normal damage, no recoil], 3)damage potion[+30 damage], 4)health potion[+40 health]")
op1=("Good job! The zombie's hp dropped by 30, that hit hurt... -15 hp","You missed and the zombie attacked twice!!-20hp")
op2=("Nice!The zombie's hp dropped by 15!","You missed... the zombie bit you! -10hp")
op3=("You used your damage potion! The zombie's hp dropped by 30!","Your damage potion fell out of your hands atleast you managed to dodge the zombie's attack....")
op4=("You used your healing potion! +40 hp","Your potion fell out of your hands atleast you managed to dodge the zombie's attack....")
op5=("Fight","fight","f","F","FIGHT")

def peepee():
    Maroon=Hero(name="Maroon",health=200, damage=15,coins=20)
    zombies= Enemy(name="Zombie",health=200,damage=10)

class Poopoo():
    def fight():
        fstart
        movedesc
        dmg=Hero.damage
        zdmg=Enemy.damage
        pdmg=30
        v=time.sleep(1.5)
        Enemy.health=Enemy.health
        Hero.health=Hero.health
        while Hero.health>0:
            moveset=input ("-------\n1) Charged Attack, \n2) Normal Attack, \n3) Damage Potion,\n4)Healing Potion\n Enter the corresponding number:  ")
            if moveset== "1":
                n = random.randint(1, 2)
                if n == 1:
                    print ("Good job! The zombie's hp dropped by 30, that hit hurt...-15 hp")
                    Hero.health = Hero.health-dmg
                    Enemy.health=Enemy.health-(dmg*2)
                    print("Your health is..",Hero.health)
                    v
                    print("The zombie's health is",Enemy.health)
                elif n == 2:
                    print("You missed and the zombie attacked twice!!-20hp")
                    Hero.health = Hero.health-(zdmg*2)
                    print("Your health is..",Hero.health)
                    v
                    print("The zombie's health is",Enemy.health)
                    v

            elif moveset=="2":
                print (random.choice(op2))
                if random.choice(op2) == ("Nice!The zombie's hp dropped by 15!"):
                    Enemy.health=Enemy.health-dmg
                    v
                    print("The zombie's health is",Enemy.health)
                    v
                elif random.choice(op2) == ("You missed... the zombie bit you! -10hp"):
                    Hero.health=Hero.health-zdmg
                    v
                    print("Your health is....",Hero.health)
                    v  

            elif moveset=="3":
                if random.choice(op3) == ("You used your damage potion! The zombie's hp dropp…"):
                    print("Nice!The zombie's hp dropped by 30!")
                    Enemy.health=Enemy.health-pdmg
                    time.sleep(1.5)
                    print("The zombie's health is",Enemy.health)
                    time.sleep(1.5)
                elif random.choice(op3) == ("Your damage potion fell out of your hands atleast …"):
                    print("Your damage potion fell out of your hands atleast you managed to dodge the zombie's attack....")
                    Enemy.health=Enemy.health
                    Hero.health=Hero.health
                    time.sleep(1.5)
                    print("Your health is....",Hero.health)
                    time.sleep(1.5)   
                    print("The zombie's health is",Enemy.health)
                    v

            elif moveset=="4":
                if random.choice(op4) == ("You used your healing potion! +40 hp"):
                    print("You used your healing potion! +40p!")
                    Hero.health=Hero.health+40
                    time.sleep(1.5)
                    print("Your health is..",Hero.health)
                    time.sleep(1.5)
                elif random.choice(op4) == ("Your potion fell out of your hands atleast you man…"):
                    print("Your potion fell out of your hands atleast you managed to dodge the zombie's attack....")
                    time.sleep(1.5)
                    print("Your health is....",Hero.health)
                    time.sleep(1.5)   
                    print("The zombie's health is",Enemy.health)

            if Enemy.health==0:
                print("The Zombie died...")
                break

            if Enemy.health<0:
                print("HERO WINS.")
                time.sleep(1.5)
                print (f"You got 25 coins from defeating this zombie!")
                Hero.coins+25
                print (Hero.coins)

            
            if Hero.health==0:
                print("You've died...")
                break
                
            if Hero.health<0:
                print("ZOMBIE WINS.")
                time.sleep(1.5)
                fight_again= input("-------\nWould you like to battle again or go to the shop?\n'Fight' to try again.)")
                if fight_again in op5:
                    return (Poopoo())
            
        else:
            print ("Invalid option... Enter again: ")
            still_continue =input("What attack do you want to use?")
            moveset=still_continue
        print


