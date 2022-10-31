import random
"""A number-guessing game."""
# Put your code here

print("Welcome to our game!")
name = input("What's your name? ")
number = random.randrange(1,100)
guess = int(input("What's your guess? "))

while guess != number:
    if guess < number:
        print("too low")
        guess = int(input("What's your guess? "))
    elif guess  > number:
        print("too high")
        guess = int(input("What's your guess? "))

print("you got it")
