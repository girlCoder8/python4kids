# Lesson 2
## Exercise - if/else statements

age = 12
if age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")

# Exercise - Loops
for i in range(1, 6):
    print(f"Counting: {i}")


# Exercises
def square(number):
    return number * number


print(square(4))

### Project 1: Guess the Number
# Code
import random

number_to_guess = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))
if guess == number_to_guess:
    print("You guessed it!")
else:
    print(f"Sorry, the number was {number_to_guess}.")
