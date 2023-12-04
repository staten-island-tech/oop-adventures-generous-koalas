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




