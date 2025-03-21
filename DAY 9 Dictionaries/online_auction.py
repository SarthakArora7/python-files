from art import logo
from os import system

print(logo)
print()

bid_dictionary = {}


def inp():
    name = input("What's your name : ")
    bid = input("What's your bid : $")
    bid_dictionary[name] = bid

def calculate(bid_dictionary):
    values = []
    for name in bid_dictionary:
        values.append(bid_dictionary[name])
    print(values)

    bid_of_winner = max(values)
    print(bid_of_winner)

    for key in bid_dictionary:
        if bid_dictionary[key] == bid_of_winner:
            winner = key
    
    print(f"The winner is {winner} with a bid of ${bid_dictionary[winner]}")

def condition():
    choice = input("Anyone else to bid ? 'y' for yes and 'n' for no \n")
    if choice == "y":
        system('cls')
        inp()
        condition()
    elif choice == "n":
        calculate(bid_dictionary)

inp()
condition()