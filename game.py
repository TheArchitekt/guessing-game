import random
"""A number-guessing game."""
# Put your code here

print("Welcome to our game!")
name = input("What's your name? ")
number = random.randrange(1,100)
guess = int(input("What's your guess? "))
