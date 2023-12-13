import random
import time
from hero import Hero

Maroon=Hero(200,15,20,"Maroon",{"health_potions": [1], "damage_potions":[1]})


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


class Fight():
    def fight():
        fstart
        movedesc
        coins=random.randint(23,31)
        dmg="damage"
        zdmg="zdamage"
        pdmg="pdmg"
        v=time.sleep(1.5)
        zombie_health=200
        Maroon.health
        while Maroon.health>0:
            moveset=input ("-------\n1) Charged Attack, \n2) Normal Attack, \n3) Damage Potion,\n4)Healing Potion\n Enter the corresponding number:  ")
            if moveset== "1":
                n = random.randint(1, 2)
                if n == 1:
                    print ("Good job! The zombie's hp dropped by 30, that hit hurt...-15 hp")
                    Maroon.health = Maroon.health-dmg
                    zombie_health=zombie_health-(dmg*2)
                    print("Your health is..",Maroon.health)
                    v
                    print("The zombie's health is",zombie_health)
                elif n == 2:
                    print("You missed and the zombie attacked twice!!-20hp")
                    Maroon.health = Maroon.health-(zdmg*2)
                    print("Your health is..",Maroon.health)
                    v
                    print("The zombie's health is",zombie_health)
                    v

            if moveset=="2":
                print (random.choice(op2))
                if random.choice(op2) == ("Nice!The zombie's hp dropped by 15!"):
                    zombie_health=zombie_health-dmg
                    v
                    print("The zombie's health is",zombie_health)
                    v
                elif random.choice(op2) == ("You missed... the zombie bit you! -10hp"):
                    Maroon.health=Maroon.health-zdmg
                    v
                    print("Your health is....",Maroon.health)
                    v  

            if moveset=="3":
                if random.choice(op3) == ("You used your damage potion! The zombie's hp dropp…"):
                    print("Nice!The zombie's hp dropped by 30!")
                    zombie_health=zombie_health-pdmg
                    time.sleep(1.5)
                    print("The zombie's health is",zombie_health)
                    time.sleep(1.5)
                elif random.choice(op3) == ("Your damage potion fell out of your hands atleast …"):
                    print("Your damage potion fell out of your hands atleast you managed to dodge the zombie's attack....")
                    zombie_health=zombie_health
                    Maroon.health=Maroon.health
                    time.sleep(1.5)
                    print("Your health is....",Maroon.health)
                    time.sleep(1.5)   
                    print("The zombie's health is",zombie_health)
                    v

            if moveset=="4":
                if random.choice(op4) == ("You used your healing potion! +40 hp"):
                    print("You used your healing potion! +40p!")
                    Maroon.health=Maroon.health+40
                    time.sleep(1.5)
                    print("Your health is..",Maroon.health)
                    time.sleep(1.5)
                elif random.choice(op4) == ("Your potion fell out of your hands atleast you man…"):
                    print("Your potion fell out of your hands atleast you managed to dodge the zombie's attack....")
                    time.sleep(1.5)
                    print("Your health is....",Maroon.health)
                    time.sleep(1.5)   
                    print("The zombie's health is",zombie_health)

            if zombie_health==0:
                print("The Zombie died...")
                break

            if zombie_health<0:
                print("HERO WINS.")
                time.sleep(1.5)
                print (f"You got {coins} from defeating this zombie!")
                Maroon.coin+{coins}
                print (Maroon.coin)

            
            if Maroon.health==0:
                print("You've died...")
                break
                
            if Maroon.health<0:
                print("ZOMBIE WINS.")
                time.sleep(1.5)
                fight_again= input("-------\nWould you like to battle again or go to the shop?\n'Fight' to try again.)")
                if fight_again in op5:
                    return
            
        else:
            print ("You didn't choose an option... Enter again: ")
            still_continue =input("What attack do you want to use?")
            moveset=still_continue
    print (fight())
