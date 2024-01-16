def start():
    a = input("Welcome to *Game Title*!! Lets begin. Press Enter to Continue") 
    b = input("Hello! You are a student in Staten Island Technical High School and you are attempting to survive the zombie apocalypse.")
    c = input ("The goal is to get to Staten Island Techincal high School's roof, where the rescue point is. You will start in Level 1, in the basement. Be careful!") 
    start = input("Your chemistry teacher's alarm rings, indicating that tutoring sess is over! You begin to get up, and go to the basement. Type Band if you'd like to go to Band, or type CompSci to go to Mr Whalen's room or to buy things, type in School Store") 
    if start == ("CompSci"):
        print("You are going to the computer science room")
        import compstoryline
    if start == ("Band"):
        print("You are going to the band room")
        import band
    if start == ("School Store"):
        print("you are now going to the school store!")
        import schoolstore
    else:
        ("since you didn't type anything else, you get to go to the school store")
        import schoolstore
start()

def level2():
    win = input("Did you win? Please be honest! Type 'Yes' if you did, Type 'No' if not.") 
if win == 'Yes':
    import level2.py 
if win == 'No':
    print("You can restart the fight! If not then...game over :( ") 
