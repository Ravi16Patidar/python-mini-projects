# Steps of the Project

# 1. Generate a random number within a specified range.
# 2. Ask the user to guess a number within that range.
# 3. Compare the user's guess with the random number.
# 4. If both numbers match, display:
#    "Congratulations! You guessed the correct number."
# 5. Otherwise, display:
#    "Wrong guess. Try again."
# 6. Repeat until the user guesses the correct number.

import random

randNumber = random.randint(1, 10)

guessingNumber = None

def userInput():
    global guessingNumber

    while True:
        try:
            guessingNumber = int(input("Guess a number between 1 to 10: "))

            if 1 <= guessingNumber and guessingNumber <= 10:
                break
            else:
                print("Please enter a number between 1 and 10.")

        except ValueError:
            print("Please enter a valid number.")

userInput()

while True:
    if randNumber == guessingNumber:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        print("You guessed wrong, try again.")
        userInput()