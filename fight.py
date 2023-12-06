import random
import time

y=("yes","yeah","y","Y","YES","Yes")
n=("no","nah","n","N","NO","No")


fstart= print("You encounter a Zombie. FIGHT START.")
movedesc=print("1)Charged attack.[2x your normal damage, 1/2 recoil],2)normal attack[normal damage, no recoil], 3)damage potion[+30 damage], 4)health potion[+40 health]")
op1=("Good job! The zombie's hp dropped by 30, that hit hurt... -15 hp","You missed and the zombie attacked twice!!-20hp")
op2=("Nice!The zombie's hp dropped by 15!","You missed... the zombie bit you! -10hp")
op3=("You used your damage potion! The zombie's hp dropped by 30!","Your damage potion fell out of your hands atleast you managed to dodge the zombie's attack....")
op4=("You used your healing potion! +40 hp","Your potion fell out of your hands atleast you managed to dodge the zombie's attack....")
op5=("Fight","fight","f","F","FIGHT")




def fight():
    time.sleep(1.5)
    fstart
    time.sleep(1.5)
    movedesc
    time.sleep(1.5)
    zombie_health=200
    hero_health=200
    while hero_health>0:
        moveset=input ("-------\n1) Charged Attack, \n2) Normal Attack, \n3) Damage Potion,\n4)Healing Potion\n Enter the corresponding number:  ")
        if moveset== "1":
            print(random.choice(op1))
            if random.choice(op1) == ("Good job! The zombie's hp dropped by 30, that hit …"):
                print ("Good job! The zombie's hp dropped by 30, that hit hurt...-15 hp")
                hero_health = hero_health-15
                zombie_health=zombie_health-30
                print("Your health is..",hero_health)
                time.sleep(1.5)
                print("The zombie's health is",zombie_health)
            if random.choice(op1) == ("You missed and the zombie attacked twice!!-20hp"):
                print ("You missed and the zombie attacked twice!!-20hp")
                hero_health = hero_health-20
                print("Your health is..",hero_health)
                time.sleep(1.5)
                print("The zombie's health is",zombie_health)
                time.sleep(1.5)

        if moveset=="2":
            print (random.choice(op2))
            if random.choice(op2) == ("Nice!The zombie's hp dropped by 15!"):
                print("Nice!The zombie's hp dropped by 15!")
                zombie_health=zombie_health-15
                time.sleep(1.5)
                print("The zombie's health is",zombie_health)
                time.sleep(1.5)
            if random.choice(op2) == ("You missed... the zombie bit you! -10hp"):
                print("You missed... the zombie you!-10hp")
                hero_health=hero_health-10
                time.sleep(1.5)
                print("Your health is....",hero_health)
                time.sleep(1.5)   

        if moveset=="3":
            print (random.choice(op3))
            if random.choice(op3) == ("You used your damage potion! The zombie's hp dropp…"):
                print("Nice!The zombie's hp dropped by 30!")
                zombie_health=zombie_health-30
                time.sleep(1.5)
                print("The zombie's health is",zombie_health)
                time.sleep(1.5)
            if random.choice(op3) == ("Your damage potion fell out of your hands atleast …"):
                print("Your damage potion fell out of your hands atleast you managed to dodge the zombie's attack....")
                time.sleep(1.5)
                print("Your health is....",hero_health)
                time.sleep(1.5)   
                print("The zombie's health is",zombie_health)
                time.sleep(1.5)

        if moveset=="4":
            if random.choice(op4) == ("You used your damage potion! The zombie's hp dropp…"):
                print("Nice!The zombie's hp dropped by 15!")
                zombie_health=zombie_health-30
                time.sleep(1.5)
                print("The zombie's health is",zombie_health)
                time.sleep(1.5)
            if random.choice(op4) == ("Your damage potion fell out of your hands atleast …"):
                print("Your damage potion fell out of your hands atleast you managed to dodge the zombie's attack....")
                time.sleep(1.5)
                print("Your health is....",hero_health)
                time.sleep(1.5)   
                print("The zombie's health is",zombie_health)
                time.sleep(1.5)