from art import logo
import random

print(logo)
num = random.randrange(1,100)

def compare(users_guess, attempts):
    if users_guess == num:
        print(f"You got it! The answer was {users_guess}.")
        return False
    elif users_guess < num:
        if attempts == 1:
            print("Too low.")
        else:
            print("Too low.")
            print("Guess again.")
        return True
    elif users_guess > num:
        if attempts == 1:
            print("Too high.")
        else:
            print("Too high.")
            print("Guess again.")
        return True

def level(attempts):
    game_condition = True
    while attempts > 0 and game_condition == True:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        game_condition = compare(guess, attempts)
        attempts = attempts - 1
        if attempts == 0:
            print("You've run out of guesses, you lose.")

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"Pssst, the correct answer is {num}")
choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
if choice == "easy":
    level(10) 
else:
    level(5)