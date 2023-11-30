import time 

Path1 = ["Left","left","l"]

Path2 = ["Right","right","r"]

print ("You are walking in the woods trying to find a specific plant. You come across two paths going in opposite directions") 
def Woods_Start(): 
    request = input("Which way do you want to go? Left or Right?") 
    if request in Path1: 
        print("As you continue walking down the road, you hear a weird sound. Is that...a snarl? A growl? Maybe it's a bear, or a raccoon but something hops out of the bushes. Something much worse than you expected. What do you do now??")
    if request in Path2: 
        print("You found your way home. Game over...or is it?")
Woods_Start()



Ans =  ["Piano", "a piano"]
def Path1 (): 

    print (" Once you look at their information, you take you and your weapon (sword) into battle. To win this battle you must answer the following question:")

    riddle = input("I'm full of keys, but I cannot open a door, what am i? ")
    if riddle in Ans:
        print ("You are right! You won the battle against the baby zombie! Lets keep going!")
    if riddle is not Ans: 
        print ("Oh no! You died! D:")
