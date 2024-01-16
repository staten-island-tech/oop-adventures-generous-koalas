class specific_storyline:
      def CompSci():
            print("You walk into the room and realize nobody is inside") 
thisorthat = input("Great! Now you can either turn on a computer and continue your code or go to the back of the room. type 'Computer' for the first option, type 'Back' for the second.   ")   
if thisorthat == ("Computer"):
      import computercompsci
if thisorthat == ("Back"):
      import backofcompsci
else: 
print("Im sorry but you are leaving the room...let's go to the store!")
      import schoolstore
specific_storyline()
