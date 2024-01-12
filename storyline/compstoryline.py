class specific_storyline:
      def CompSci():
            print("You walk into the room and realize nobody is inside") 
thisorthat = input("Great! Now you can either turn on a computer and continue your code or go to the back of the room. type 'Computer' for the first option, type 'Back' for the second.   ")   
if thisorthat == ("Computer"):
      import af
      wonorlose = input("Did you win?? Did you lose?? Type 'W' for win, type 'L' for lose")
      if wonorlose == 'W':
            print ("You have now opened access to the 2nd and 3rd floor!")
      if wonorlose == 'L':
            x = input("you know you can redo the fight? \n type Yes if you'd like to redo it. Type No is not.")
            if x == 'Yes': 
                  import fight1
if thisorthat == ("Back"):
     import af2
else:
      print("Im sorry but you are leaving the room...let's go to the store!")
      import schoolstore
specific_storyline() 
