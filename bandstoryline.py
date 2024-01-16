class bandstoryline:
def Band():
print ("you entered the band room, getting your instrument")
lalala = input("Now you have your instrument (remember; this can be used later on!) Once you start playing, you realize the door to Mr. Rams room is cracked open. Would you like to check? Type 'yes' if you'd like to look, 'no' if not.")
if lalala == 'yes':
print("you decided to check it out. \n You open the door, wider and notice a green slimy liquid on the floor.\n. You've seen this before...\n You decided to walk down the hallway, checking if any danger is near. \n the lights start flickering continuously as you get nearer to the furthest door ")

start = input("Then, the door bursts down, and a zombie, much bigger and taller from the last one appears. \n he seems very angry, and starts walking unsteadily towards you \n then he starts RUNNING. what should you do?? Type 'run' to run back to the band room, type 'fight' to charge him. ")
if start == 'run':
print ("You have decided to run to the room. \n lets go!")
import BANDrunawayoption
if start == 'fight':
print("you have decided to charge him. If you use this, you must have 1 or 'Charged Attack' as your first fighting choice! Good luck!!")
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

Band() 
