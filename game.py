


"""A number-guessing game."""

# Put your code here
first_name = input("Howdy, what's your name?")
#Select random number
import random
number = random.randint(1,100)
print(first_name, "I'm thinking of a number between 1 and 100.")
print("Try to guess my number.")
#while loop when number and guess are not the same
tries = 1
guess = int(input("Your guess?"))

while True:
#Ask if the number is higher than 50
    if guess < number:
        print("Your guess is too low, try again.")
        tries = tries + 1
        guess = input("Your guess?")
        guess = int(guess)
    elif guess > number:
        print("Your guess is too high, try again.")
        tries = tries + 1
        guess = input("Your guess?")
        guess = int(guess)
    else:
        print("Well done,", first_name, "! You found my number in", tries, "tries!")
        break