def start():
    a = input("Welcome to *Game Title*!! Lets begin. Press Enter to Continue") 
    b = input("Hello! You are a student in Staten Island Technical High School and you are attempting to survive the zombie apocalypse.")
    c = input ("The goal is to get to Staten Island Techincal high School's roof, where the rescue point is. You will start in Level 1, in the basement. Be careful!") 
    start = input("Your chemistry teacher's alarm rings, indicating that tutoring sess is over! You begin to get up. Do you want to go to the Comp Sci room or SO Store")
    BeginningA = ["So store", "school store", "School Store", "Snack Store"]
    BeginningB = ["Computer Sci Room", "Comp Sci room", "Comp Sci", "comp sci", "Mr whalen's room"]
    if start in BeginningA:
         print ("What do you do in the SO Store?")
    elif start in BeginningB:
         print("You walk in and realize that no one is in the room")
start()
