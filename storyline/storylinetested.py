def start():
    a = input("Welcome to *Game Title*!! Lets begin. Press Enter to Continue") 
    b = input("Hello! You are a student in Staten Island Technical High School and you are attempting to survive the zombie apocalypse.")
    c = input ("The goal is to get to Staten Island Techincal high School's roof, where the rescue point is. You will start in Level 1, in the basement. Be careful!") 
    start = input("Your chemistry teacher's alarm rings, indicating that tutoring sess is over! You begin to get up. Do you want to go to the Comp Sci room or SO Store")
    BeginningA = ["So store", "school store", "School Store", "Snack Store"]
    BeginningB = ["Computer Sci Room", "Comp Sci room", "Comp Sci", "comp sci", "Mr whalen's room"]
    if start in BeginningB:
        print ("you are now in the computer science room, what would you like to do?")
        import CompSCi.py
    if start in BeginningC:
        print ("you are now in the band room") 
        import Bandroom.py
    elif:
        print ("you are going to the so store")
        import sostore.py
# make a class that represents the so store, and the choices they can make. 
