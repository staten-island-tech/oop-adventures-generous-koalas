class compsci1():
    def checkcode(): 
        print("You find your computer and sit down, turning your compuer on. But it is not turning on.")
        print("you stand up, checking the motherboard. Press any key to check.")
        b = input("as you tilt your head, you realize the cord is not only unplugged but it seems like it was ...chewed off?? Press any key to continue")
        gr = input("then the door slightlty opens, and you hear a small growl. Type YES to check, type NO to stay put") 
        if gr == "YES": 
            print("once you are near the door. You see a slimy substance on the floor. As you bend down to check what it is, you feel a sharp pain in your neck. as you turn around you see a small,green,horrible zombie, ready to fight.")
            import fight1
        if gr == "NO":
            print("you decided to hide, going under the desk. looking in front of you, you see a dark green, skeleton like figure. It bends down and finds you, growling at your face, looking hungrier than ever. ")
            import fight1
    checkcode()
    