import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game = [rock, paper, scissor]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor.\n"))
# if choice == 0 :
#     print(rock)
# elif choice == 1 :
#     print(paper)
# elif choice == 2 :
#     print(scissor)
print(game[choice])

print("Computer Choose : ")

comp_choice = random.randint(0,2)
# if comp_choice == 0 :
#     print(rock)
# elif comp_choice == 1 :
#     print(paper)
# elif comp_choice == 2 :
#     print(scissor)

print(game[comp_choice])

if choice == comp_choice :
    print("Its a Draw!")

elif choice == 0 and comp_choice == 1 :
    print("You Lose!")
elif choice == 0 and comp_choice == 2 :
    print("You Win!")

elif choice == 1 and comp_choice == 0 :
    print("You Win!")
elif choice == 1 and comp_choice == 2 :
    print("You Lose!")

elif choice == 2 and comp_choice == 0 :
    print("You Lose!")
elif choice == 2 and comp_choice == 1 :
    print("You Win!")