def Path1 (): 
    print (" Once you look at their information, you take you and your weapon (sword) into battle. To win this battle you must answer the following question:")

    riddle = input("I'm full of keys, but I cannot open a door, what am i? ")
    if riddle == "A piano":
        print ("You are right! You won the battle against the baby zombie! Lets keep going!")
    elif riddle == "a piano":
        print ("You are right! You won the battle against the baby zombie! Lets keep going")
    elif riddle == "Piano":
        print (" You are right ! You won against the baby zombie. Lets continue!!")
    else:
        print ("You  are wrong! The baby zombie attacked you! Game over :(")
Path1() 