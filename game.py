import random
"""A number-guessing game."""
# Put your code here

print("Welcome to our game!")
name = input("What's your name? ")
number = random.randrange(1,100)
#guess = int(input("What's your guess? "))


count = 1
def get_guess():
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
        print("too low")
        guess = int(input("What's your guess? "))
    elif guess  > number:
        print("too high")
        guess = int(input("What's your guess? "))

print("you got it")
print(f"{name}, it took you {count} tries.")
