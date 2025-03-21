# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1_lower = name1.lower()
name2_lower = name2.lower()

total_true = 0
total_love = 0

total_true += name1_lower.count("t") + name2_lower.count("t")
total_true += name1_lower.count("r") + name2_lower.count("r")
total_true += name1_lower.count("u") + name2_lower.count("u")
total_true += name1_lower.count("e") + name2_lower.count("e")

total_love += name1_lower.count("l") + name2_lower.count("l")
total_love += name1_lower.count("o") + name2_lower.count("o")
total_love += name1_lower.count("v") + name2_lower.count("v")
total_love += name1_lower.count("e") + name2_lower.count("e")

total_str = str(total_true) + str(total_love)

total_int = int(total_str)

if total_int < 10 or total_int > 90:
    print(f"Your score is {total_int}, you go together like coke and mentos.")
elif total_int > 40 and total_int < 50:
    print(f"Your score is {total_int}, you are alright together.")
else:
    print(f"Your score is {total_int}")
