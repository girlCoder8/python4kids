# Goal: 
#### Create a game where the computer randomly selects a number between 1 and 10, and the player has to guess it.

### Code
import random

### Generate a random number between 1 and 10
number_to_guess = random.randint(1, 10)

### Ask the player for their guess
guess = int(input("Guess a number between 1 and 10: "))

### Check if the guess is correct
if guess == number_to_guess:
    print("You guessed it!")
else:
    print(f"Sorry, the number was {number_to_guess}.")
