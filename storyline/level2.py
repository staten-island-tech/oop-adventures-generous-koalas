class level2 
def Secondfloor(): 
  print("You are now on the second floor! Now the whole second and first floor are now opened to you!") 
  start = input("As you walk down the hallway, swiftly and quietly, you noticed Ms. Ravitz' room was cracked open.\n You peaked in, noticing all the papers stashed on her desk. Press ENTER to continue")
  begin = input("You sit down in her chair, begin searching the papers, trying to find a way to get out of this hellhole. \n Then you see a paper in cardstock saying 'ESCAPE = ROOF'. \n You need to go to the roof! Lucily, staircase I, takes you DIRECTLY to the roof!/n But...how to get there...with no harm? Press ENTER to continue")
  print("as you walk out, you hear a LOUD growling sound. Uh oh! You begin running quietly across the halls, making your way to the staircase, hoping nothing or no ONE is behind you!") 
  print("Once you reached halfway there, you see a figure. A large, stick-like figure. Oh no! \n The figure abrutly stops and looks over to you. And then starts running!") 
  weapon = input("But wait! You can choose a weapon if you'd like! You can choose a Dull pencil, Sharp pencil, Heavy backpack, Troika Book, Opened Paper Clip, and Safety Scissors. \n type 'D' for dull pencil \n type 'S' for sharp pencil,\n type 'B' for heavy backpack,\n type 'T' for the troika book, type 'O' for the opened paper clip \n type 'SS' for the safety scissors. \n If you'd like to fight with your fist, type none") 
  if weapon == "none": 
    import normalzombie.py
  if weapon == "D":
    import dullpencil.py
  if weapon == "S":
    import normalzombiesharpened.py
  if weapon == "B":
    import heavybackpack.py
  if weapon == "O":
    import openedpaperclip2.py
  if weapon == "SS" : 
    import  safetyscissors2.py
    
  
