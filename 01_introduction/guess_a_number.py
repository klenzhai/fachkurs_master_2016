#Guess a Number!

from random import randint


number = randint(0,100)
guess = int(input("Welcome to guess a number, what is your guess?\n"))
while guess < 0 or guess > 100:
    print("Please stay in the boundaries of 0 to 100.")
    guess = int(input("Enter your number.\n"))
i = 1

def Game(guess, number, i):
    while guess != number:
        if guess < number:
            print("No, too low!")
            i = i+1
        if guess > number:
            print("No, too high!")
            i = i+1
        guess = int(input("Another Guess?\n"))
        while guess < 0 or guess > 100:
            print("Please stay in the boundaries of 0 to 100.")
            guess = int(input("Enter your number.\n"))
    else:
        print("You're right! And you only needed " + str(i) + " Guesses.")
        i = 1
        again = input("Want to play again? (y/n)")
        if again == "y":
            number = randint(0,100)
            Game(guess, number, i)
        else:
            print("Good Bye!")
            

Game(guess, number, i)


