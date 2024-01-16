class compsci1():
    def checkcode(): 
        print("You find your computer and sit down, turning your compuer on. But it is not turning on.")
        print("you stand up, checking the motherboard. Press any key to check.")
        b = input("as you tilt your head, you realize the cord is not only unplugged but it seems like it was ...chewed off?? Press any key to continue")
        gr = input("then the door slightlty opens, and you hear a small growl. Type YES to check, type NO to stay put") 
        if gr == "YES": 
            print("once you are near the door. You see a slimy substance on the floor. As you bend down to check what it is, you feel a sharp pain in your neck. as you turn around you see a small,green,horrible zombie, ready to fight.")
            weapon = input("But wait! You can choose a weapon if you'd like! You can choose a Dull pencil, Sharp pencil, Heavy backpack, Troika Book, Opened Paper Clip, and Safety Scissors. \n type 'D' for dull pencil \n type 'S' for sharp pencil,\n type 'B' for heavy backpack,\n type 'T' for the troika book, type 'O' for the opened paper clip \n type 'SS' for the safety scissors. \n If you'd like to fight with your fist, type none") 
                  if weapon == "none": 
                        import babyzombie.py
                  if weapon == "D":
                        import babydullpencil.py
                  if weapon == "S":
                        import babyzombiesharpened.py
                  if weapon == "B":
                        import heavybackpack.py
                  if weapon == "O":
                        import openedpaperclip.py
                  if weapon == "SS" :
                        import safetyscissors.py
                  after = input ("If you won, great!! Now you are on level 2! Lets go!")       
          if gr == "NO":
            print("you decided to hide, going under the desk. looking in front of you, you see a dark green, skeleton like figure. It bends down and finds you, growling at your face, looking hungrier than ever. ")
            weapon = input("But wait! You can choose a weapon if you'd like! You can choose a Dull pencil, Sharp pencil, Heavy backpack, Troika Book, Opened Paper Clip, and Safety Scissors. \n type 'D' for dull pencil \n type 'S' for sharp pencil,\n type 'B' for heavy backpack,\n type 'T' for the troika book, type 'O' for the opened paper clip \n type 'SS' for the safety scissors. \n If you'd like to fight with your fist, type none") 
                  if weapon == "none": 
                        import babyzombie.py
                  if weapon == "D":
                        import babydullpencil.py
                  if weapon == "S":
                        import babyzombiesharpened.py
                  if weapon == "B":
                        import heavybackpack.py
                  if weapon == "O":
                        import openedpaperclip.py
                  if weapon == "SS" :
                        import safetyscissors.py
                  after = input ("If you won, great!! Now you are on level 2! Lets go!")     checkcode()
    
