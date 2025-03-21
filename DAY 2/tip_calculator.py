print("Welcome to the tip calculator")
bill = float(input("What was the total bill ? $"))
percent = int(input("What percentage would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill ?"))
tip = bill*(1+(percent/100))/people
tip_round = "{:.2f}".format(tip)  # to format the tip to 2 decimal places !
print(f"Each person should pay ${tip_round}")