def CompSci():
    print("You walk into the room and realize nobody is inside") 
thisorthat = input("Great! Now you can either turn on a computer and continue your code or go to the back of the room. (CAPS SENSITIVE)   ")
this = ["turn on computer", "finish code", "turn on a computer and continue your code",  "continue code"]
that = ["go to the back", "back of the room","emma watson room","go to back","go to the back of the room"]    
if thisorthat in this:
        print ("You sit down and turn on the computer. Bur, it's not clicking on. You get up and try to figure out what's wrong, looking at the motherboard. You notice the circuit is disconnected. Who could've done this?")
elif thisorthat in this: 
      print("You...")
else:
      print("Dude, you're going to the school store")
      import schoolstore
