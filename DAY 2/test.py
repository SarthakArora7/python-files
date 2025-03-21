# # 🚨 Don't change the code below 👇
# two_digit_number = input("Type a two digit number: ")
# # 🚨 Don't change the code above 👆

# ####################################
# #Write your code below this line 👇

# first_digit = two_digit_number[0]
# second_digit = two_digit_number[1]

# result = int(first_digit) + int(second_digit)

# print (result)

age = input("Enter your current age : ")

lifetime = 90
years_left = 90 - int(age)
weeks_left = years_left * 52
days_left = years_left * 365

print(f"You have {years_left} years, {weeks_left} weeks and {days_left} days left.")