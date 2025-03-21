import random
from art import logo
from os import system

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def players_turn(players_card, computers_card):
  global players_current_score
  players_current_score = sum(players_card)
  selected_card = random.choice(cards)
  if selected_card == 11:
    if players_current_score < 11:
      players_card.append(11)
    else:
      players_card.append(1)
  else:
    players_card.append(selected_card)
  players_current_score = sum(players_card)
  print(f"Your cards: {players_card}, current score: {players_current_score}")
  print(f"Computer's first card: {computers_card}")
  if players_current_score > 21:
    return players_current_score
  another_card = input("Type 'y' to get another card, type 'n' to pass: ")
  if another_card == "y":
    players_turn(players_card, computers_card)
  else:
    return players_current_score

def computers_turn(computers_card):
  global current_score
  current_score = sum(computers_card)
  while current_score < 17:
    selected_card = random.choice(cards)
    if selected_card == 11:
      if current_score < 11:
        computers_card.append(11)
      else:
        computers_card.append(1)
    else:
      computers_card.append(selected_card)
    current_score = sum(computers_card)
  return current_score

def compare(players_score, computers_score):
  if players_score > 21:
    print("You went over. You lose 😭")
  elif players_score < 22 and computers_score < 22:
    if players_score < computers_score:
      print("You lose 😤")
    elif players_score > computers_score:
      print("You win 😀")
    elif players_score == computers_score:
      print("Draw 🙃")
  elif players_score <= 21 and computers_score > 21:
    print("You win 😀")

def game():
  print(logo)
  players_card = []
  computers_card = []
  players_card.append(random.choice(cards))
  computers_card.append(random.choice(cards))
  players_turn(players_card, computers_card)
  print(f"Your final hand: {players_card}, final score: {players_current_score}")
  computers_score = computers_turn(computers_card)
  print(f"Computer's final hand: {computers_card}, final score: {computers_score}")
  compare(players_current_score, computers_score)
  start_condition()

def start_condition():
  want_to_start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  if want_to_start == "y":
    system('cls')
    game()
  else:
    return

start_condition()
