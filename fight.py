from Zombies import Zombie
from hero import Hero
import random

y=("yes","yeah","y","Y","YES","Yes")
n=("no","nah","n","N","NO","No")


fstart= print("You encounter a Zombie. FIGHT START.")
moveset=print("1)Charged attack.[2x your normal damage, 1/2 recoil],2)normal attack[normal damage, no recoil], 3)damage potion[+5 damage], 4)health potion[+40 health]")

def fight():
    fstart
    zombie_health=200
    hero_health=200
    while zombie_health> 0:
        print ("The Zombie attacked you. Loose 10 hp.") 
        hero_health-10
    if hero_health==0:
        print("You have died.")
    elif hero_health>0 and zombie_health==0:
        return fight
    
