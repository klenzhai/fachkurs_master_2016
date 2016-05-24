#Guess a Number!

from random import randint


number = randint(0,100)
print("Welcome to guess a number!\n")


def Game(number, i):
    guess = Guess() 
    
    while guess != number:
        if guess < number:
            print("No, too low!")
            i = i+1
        if guess > number:
            print("No, too high!")
            i = i+1
        guess = Guess()
    
    else:
        print("You're right! And you only needed " + str(i) + " Guesses.")
        again = input("Want to play again? (y/n)")
        if again == "y":
            number = randint(0,100)
            Game(number, 1)
        else:
            print("Good Bye!")
            
def Guess():
    guess = Guess_type()
    while guess < 0 or guess > 100:
        print("Please stay in the boundaries of 0 to 100.")
        guess = Guess_type()
    return guess

def Guess_type():
    error = False
    while error == False:
        try:
            guess = input("What is your Guess?\n")
            guess = int(guess)
            error = True
        except:
            print("Try again")
    return guess


def Demo(number, i):
    number1 = number
    number2 = randint(0,100)
    max = 100
    min = 0
    while number2 != number1:
        if number2 < number1:
            min = number2+1
            number2 = randint(min, max)
            i = i+1
        if number2 > number1:
            max = number2-1
            number2 = randint(min, max)
            i = i+1 
        print("The number the computer should guess is " + str(number1) + "\n The number the computer guessed is " + str(number2))
    else:
        print("The computer took " + str(i) + " tries.")


which = input("What do you want to play, the demo version (enter 'd'), or the normal game (enter 'n')?\n")
if which == "d":
    Demo(number, 1)
elif which == "n":
    Game(number, 1)

