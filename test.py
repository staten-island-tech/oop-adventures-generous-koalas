def storyline():
    a = input("Welcome to *Game Title*!! Lets begin. Press Enter to Continue") 
    b = input("Hello! You are a student in Staten Island Technical High School and you are attempting to survive the zombie apocalypse.")
    c = input ("The goal is to get to Staten Island Techincal high School's roof, where the rescue point is. You will start in Level 1, Brooklyn, NY. Try to get to Staten Island the best way possible. Be careful!")
    start = input("You wake up from your bed in Brooklyn after hearing a blood chilling shriek! You can either check out the sound, or stay in your room. What do you pick?")
    BeginningA = ["Check out the sound"]
    BeginningB = ["Stay in your room, and hide"]
    if start in BeginningA:
         print ("You mama")
    elif start in BeginningB:
         print("your papa")


storyline() 