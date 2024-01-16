class specific_storyline:
      def CompSci():
            print("You walk into the room and realize nobody is inside") 
thisorthat = input("Great! Now you can either turn on a computer and continue your code or go to the back of the room. type 'Computer' for the first option, type 'Back' for the second.   ")   
if thisorthat == ("Computer"):
      import af
      wonorlose = input("Did you win?? Did you lose?? Type 'W' for win, type 'L' for lose")
      if wonorlose == 'W':
            print ("You have now opened access to the 2nd and 3rd floor!")
      if wonorlose == 'L':
            x = input("you know you can redo the fight? \n type Yes if you'd like to redo it. Type No is not.")
            if x == 'Yes': 
                  weapon = input("But wait! You can choose a weapon if you'd like! You can choose a Dull pencil, Sharp pencil, Heavy backpack, Troika Book, Opened Paper Clip, and Safety Scissors. \n type 'D' for dull pencil \n type 'S' for sharp pencil,\n type 'B' for heavy backpack,\n type 'T' for the troika book, type 'O' for the opened paper clip \n type 'SS' for the safety scissors. \n If you'd like to fight with your fist, type none") 
                  if weapon == "none": 
                        import babyzombie
                  if weapon == "D":
                        import babydullpencil
                  if weapon == "S":
                        import babyzombiesharpened
                  if weapon == "B":
                        import heavybackpack
                  if weapon == "O":
                        import openedpaperclip 
                  if weapon == "SS" : 
                        import safetyscissors 
                  after = input ("If you won, great!! Now you are on level 2! Lets go!") 
if thisorthat == ("Back"):
           weapon = input("But wait! You can choose a weapon if you'd like! You can choose a Dull pencil, Sharp pencil, Heavy backpack, Troika Book, Opened Paper Clip, and Safety Scissors. \n type 'D' for dull pencil \n type 'S' for sharp pencil,\n type 'B' for heavy backpack,\n type 'T' for the troika book, type 'O' for the opened paper clip \n type 'SS' for the safety scissors. \n If you'd like to fight with your fist, type none") 
                  if weapon == "none": 
                        import babyzombie
                  if weapon == "D":
                        import babydullpencil
                  if weapon == "S":
                        import babyzombiesharpened
                  if weapon == "B":
                        import heavybackpack
                  if weapon == "O":
                        import openedpaperclip 
                  if weapon == "SS" : 
                        import safetyscissors 

else: 
print("Im sorry but you are leaving the room...let's go to the store!")
      import schoolstore
specific_storyline() 
