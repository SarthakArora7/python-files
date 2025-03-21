from art import logo
from os import system

print(logo)
print()

bid_dictionary = {}

def inp():
    name = input("What's your name : ")
    bid = int(input("What's your bid : $"))
    bid_dictionary[name] = bid

def calculate(bid_dictionary):
    max_bid = 0
    for name in bid_dictionary:
        bid_amount = bid_dictionary[name]
        if max_bid < bid_amount:
            max_bid = bid_amount
            winner = name
    print(f"The winner is {winner} with a bid of ${max_bid}")

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