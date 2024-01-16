class level3():
  def lvl3():
    print("Congrats! You are now on the last level! You now need to get to the roof! But be careful, there's one BIG and DANGEROUS zombie still out there!") 
    a = input("you are now running up staircase I, but you realized the doors are locked! Oh shoot! You need to go to the 1st floor, main office to get the key! \n Let's not waste anytime, lets go! Press Enter to continue") 
    b = print("you went back to the hallway, and now walking toward the next staircase, H.") 
    print("As you hurridly run down the stairs, you hear a loud groan. Uh oh! \n You continue running, and then you reach the 1st floor.\n You swiftly slide through the door and then start walking towards the office.") 
    fight3start = input("As you turn at room 129, you see a HUGE at least 6' tall Green and Brown, Hulk-sized zombie! Uh oh! Hopefully he didn't see you!! Press ENTER to continue.") 
    lightshower = input("Sorry bud...but he did. He turned around, slowly and starts walking to you! \n You back up to the wall and then start running down the hallway!\n He chases you, running at an incredible speed. He then gets the fire extinguisher and throws it at you, hitting your back! \n I'm sorry...I think you need to fight this dude! \n") 
    weapons = input("Choose a weapon ! \n You can choose a Dull pencil, Sharp pencil, Heavy backpack, Troika Book, Opened Paper Clip, and Safety Scissors. \n type 'D' for dull pencil \n type 'S' for sharp pencil,\n type 'B' for heavy backpack,\n type 'T' for the troika book, type 'O' for the opened paper clip \n type 'SS' for the safety scissors. \n If you'd like to fight with your fist, type none") 
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
lvl3()

class ending():
  def end():
    print("You now have the key! LETS GO!") 
    a = input("You open the doors to staircase I and run up the stairs. Once you are at the 3rd floor, you get the key and open the door! Press ENTER to continue!") 
    goodending = input("You are met with two policemen and a helicopter, ready to take you to safety! Press ENTER to continue!") 
    final = input("GREAT JOB! YOU SUCCESSFULLY LIVED THROUGH THE APOCALYPSE! I GET TO SLEEP AND YOU GET TO BE SAFE! WOOHOO!!") 

break 

