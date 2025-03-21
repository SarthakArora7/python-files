import art
from game_data import data
import random
from os import system

# print logo
def logo():
    print(art.logo)

# a function to collect random data from data folder
def assign_data():
    """Assign data to the variable"""
    assigned_data = random.choice(data)
    data.remove(assigned_data)
    return assigned_data
    
# a function to print data
def to_print(first_data, second_data):
    """Print the data"""
    print(f"Compare A: {first_data['name']}, a {first_data['description']}, from {first_data['country']}")
    print()
    print(art.vs)
    print()
    print(f"Against B: {second_data['name']}, a {second_data['description']}, from {second_data['country']}")

# a compare function which compares their follower counts and returns the data of the higher follower count
def compare(first_input, second_input):
    """Compares who has more followers"""
    if first_input['follower_count'] > second_input['follower_count']:
        return first_input['follower_count']
    else:
        return second_input['follower_count']

def game():
    score = 0
    condition = True
    a = assign_data()
    b = assign_data()
    logo()
    while condition:
        to_print(a, b)
        computer_answer = compare(a, b)
        # taking an answer from the user
        user_choice = (input("Who has more followers? Type 'A' or 'B': ")).lower()
        system('cls')
        if user_choice == 'a':
            if computer_answer == a['follower_count']:
                    score = score + 1
                    logo()
                    print(f"You're right! Current score: {score}")
                    # send new data as the input B to the compare and make A equals to the previous data of B 
                    a = b
                    b = assign_data()
                    condition = True
            else:
                    # when the user gets a wrong answer clear the screen and print a statement and show its score
                    system('cls')
                    print(f"Sorry, that's wrong. Final score: {score}")
                    # do all of these until the user gets a wrong answer
                    condition = False
        elif user_choice == 'b':
            if computer_answer == b['follower_count']:
                    score = score + 1
                    logo()
                    print(f"You're right! Current score: {score}")
                    # send new data as the input B to the compare and make A equals to the previous data of B 
                    a = b
                    b = assign_data()
                    condition = True
            else:
                    # when the user gets a wrong answer clear the screen and print a statement and show its score
                    print(f"Sorry, that's wrong. Final score: {score}")
                    # do all of these until the user gets a wrong answer
                    condition = False
    
game()
