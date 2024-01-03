def start():
    a = input("Welcome to *Game Title*!! Lets begin. Press Enter to Continue") 
    b = input("Hello! You are a student in Staten Island Technical High School and you are attempting to survive the zombie apocalypse.")
    c = input ("The goal is to get to Staten Island Techincal high School's roof, where the rescue point is. You will start in Level 1, in the basement. Be careful!") 
    start = input("Your chemistry teacher's alarm rings, indicating that tutoring sess is over! You begin to get up, and go to the basement. Type Band if you'd like to go to Band, or type Comp Sci to go to Mr Whalen's room")
    if start in BeginningA:
        print("You are going to the computer science room")
        import compsci
    if start in BeginningB:
        print("You are going to the band room")
        import bandroom
        



BeginningA = ["band", "Band", "band room"]
BeginningB = ["CompSci", "comp sci", "Comp Sci", "Comp sci"]