import random
"""A number-guessing game."""
# Put your code here

print("Welcome to our game!")
name = input("What's your name? ")
number = random.randrange(1,100)
count = 1

def get_guess():
    """A function used to ensure the guess is an integer"""

    guess = None

    while guess == None:
        try:
            guess = int(input("What's your guess? "))
        except ValueError:
            print("Nice try, not a valid number.")
    return guess

guess = get_guess()

while guess != number:
    count += 1

    if guess < number:
        print("Too low")
        guess = int(input("What's your guess? "))
    elif guess  > number:
        print("Too high")
        guess = int(input("What's your guess? "))

print("You got it!")
print(f"{name}, it took you {count} tries.")
