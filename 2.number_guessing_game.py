# Number Guessing Game
# User keeps guessing until correct

import random

randomno = random.randrange(1, 101)
attempts = 0

while True:
    try:
        guess = int(input("Enter your guess (1-100): "))
        attempts += 1
    except ValueError:
        print("Please enter a valid number!")
        continue

    if guess < randomno:
        print("Too low! Try again.")
    elif guess > randomno:
        print("Too high! Try again.")
    else:
        print("You got it in", attempts, "attempts.")
        break

print("The random number was:", randomno)