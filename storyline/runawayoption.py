
class runaway: 
  def RunOption(): 
  print("You returned back to the band room, hiding in Mr. Rams’ room, pondering on what to do next. \n  Well first you’d obviously would need a good hiding place and a weapon. \n luckily for you, the school store is right outside! \n To get more weapons you must go outside… \n Stay Safe! In the mean time, you are rewarded with a retired flute \n in danger, humans would do anything to save themselves. what would you do?”) 
  print(" You found out two hiding spots! The flute cabinet, which is completely empty right now or the back of the room, behind the bass drum!") 
  start1 = input(" (”Now you must go to the school store to get weapons, potions, etc \n You have a 30$ worth weapon! Hopefully it will make some damages! Press Enter to continue") 
  hallway = input(”you open the further down band room door, trying not to make any sound. There’s no sign of a zombie in the hallway. \n Once you silently slip out, you begin fastly tiptoeing to the school store. \n Once you are in the room, you lock the door behind you. Luckily, there is an owner that’s alive but fearful. \n He’s immortal so he cannot die no matter what.”)
  ## import schoolstore() / inventory () wtv they come up with 

 ##this is after their purchase!
schoolstoreleave = print (”great! Now you have all the weapons and potions you need! Let’s go back to the band room!!”) 
hallway2 = input(”As you start walking towards the band room’s door you realized that it is cracked open. press Enter to continue.”) 
introtofight = print(”you crept in, and see a zombie, probably the same one from earlier, rummaging around the room, groaning. \n you have two hiding places. Where would you like to hide? Type “1” for the flute cabinet, Type “2” for the behind the bass drum”) 
if introtofight == “1”: 
print(”You quickly tip toe to the flute cabinet, crouch and bring your knees close to your chest \n The zombie begins sniffing around, noticing that a new scent (human) has entered the room. \n he then gets closer to the flute cabinet \n Holding your breath, you hope they he doesn’t know you are in here, and hoping he does not open the door.”) 
a = input(”You heart is beginning to race and you are clutching on to your newly brought weapon/potion. He then looks at the cabinet…would you like to know what happens next? Press ENTER to continue.”) 
b = input(”The zombie then groans, and starts walking out the room…He didn’t realize you were in there! Thank god you chose to hide in the flute cabinet!!”) 
if introtofight == “2":
 print("You run behind the bass drum but as you crouch down, \n Your knee accidentally hits the bass drum, making a loud sound! \n The zombie stands up straight and begins to run towards the bass drum! \n Looks like you need to fight!")
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
