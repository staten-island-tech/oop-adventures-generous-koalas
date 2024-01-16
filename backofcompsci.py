class compsci2():
     def backroom(): 
          print("You walk around the back and realized everything is destroyed and on the floor, scattered. What happened here? ")
          print("You bend down and move one of the papers to get a white board, but you realize there is a green slimy substance on it")
          a = input("as you drop it, you realize you hear a small growl coming from under the table. press enter to continue") 
          b= input("you stoop down to the table")
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
           backroom()
