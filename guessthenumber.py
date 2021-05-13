guessTheNumber=int(input("Guess a number between 1 and 9. Enter your guess-"))
if(guessTheNumber>5):
    print("Your guess was too high")
elif(guessTheNumber<5):
    print("Your guess was too low")
else:
    print("You won!")