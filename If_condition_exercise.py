# EXERCISE , NUMBER GUESSING GAME
# Make a variable, like winning_number and assign any number to it.
# Ask user to guess a number . 
# if user guessed correctly then print "YOU WIN !!!!"
# if user didn't guessed correctly then :
    # if user guessed lower than actual number then print "too low"
    # if user guessed higher than actual number then print "too high"

# bonus 
# google "how to generate random number in python " to generate random 
# winning number

#--------------------------------------------

# import the random module
import random
winning_number = (random.randint(0,9))
# print(ran_num)
# winning_number = int(27)
guessed_number = input("Enter number between 0 - 9 to win a game : ")
guessed_number = int(guessed_number)

if winning_number==guessed_number:
    print("Congrats, You won the game...!")
else:
    if guessed_number < winning_number:
        print("Sorry, Your number is too low")
    else:
        print("Sorry, Your number is too high")
