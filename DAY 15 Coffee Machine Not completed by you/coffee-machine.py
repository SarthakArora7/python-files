from coffee_menu import MENU, resources


# TODO 3. make a function to check if the resources are sufficient for the coffee
def check_resources(drink, remaining_ingredients):
    condition = True
    if drink == "espresso":
        for item in MENU['espresso']['ingredients'] and remaining_ingredients:
            if MENU['espresso']['ingredients'][item] > remaining_ingredients[item]:
                condition = False
                print(f"Sorry there is not enough {item}")
                break
    else:
        for item in MENU[drink]['ingredients'] and remaining_ingredients:
            if MENU[drink]['ingredients'][item] > remaining_ingredients[item]:
                condition = False
                print(f"Sorry there is not enough {item}")
                break
    return condition


# TODO 2.   make a function to print report
def print_report(report, money_stored):
    print(f"Water: {report['water']}ml")
    print(f"Milk: {report['milk']}ml")
    print(f"Coffee: {report['coffee']}gm")
    print(f"Money: ${money_stored}")


# TODO 4. make a function to process coins and return the amount of coins
def process_coins(quarter, dimes, nickles, pennies):
    amount = quarter * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return amount


def calculate_ingredients(drink, count):
    if count == 0:
        if drink == "latte" or drink == "cappuccino":
            dictionary = resources
        else:
            dictionary = {'water': resources['water'],
                          'coffee': resources['coffee']}
    else:
        remaining_water = resources['water'] - MENU[drink]['ingredients']['water']
        remaining_coffee = resources['coffee'] - MENU[drink]['ingredients']['coffee']
        if drink == "latte" or drink == "cappuccino":
            remaining_milk = resources['milk'] - MENU[drink]['ingredients']['milk']
            return {'water': remaining_water,
                    'milk': remaining_milk,
                    'coffee': remaining_coffee, }
        else:
            return {'water': remaining_water,
                    'coffee': remaining_coffee, }


should_continue = True
remaining_ingredients = resources
report = resources
money_stored = 0
count = 0
# TODO 1.   ask user what would he like ?if he writes off then program should stop, if report then prints report
while should_continue:
    drink = input("  What would you like? (espresso/latte/cappuccino): ")
    if drink == "off":
        should_continue = False
    elif drink == "report":
        print_report(report, money_stored)
    elif drink == "espresso" or drink == "latte" or drink == "cappuccino":
        remaining_ingredients = calculate_ingredients(drink, count)
        if check_resources(drink, remaining_ingredients):
            print("Please insert coins.")
            quarter = int(input("how many quarters ?:"))
            dimes = int(input("how many dimes ?:"))
            nickles = int(input("how many nickles ?:"))
            pennies = int(input("how many pennies ?:"))
            amount_in_dollars = process_coins(quarter, dimes, nickles, pennies)
            cost_of_drink = MENU[drink]['cost']
            if amount_in_dollars >= cost_of_drink:
                print(f"Here is ${round(amount_in_dollars - cost_of_drink, 2)} in change.")
                print(f"Here is your {drink} ☕. Enjoy!")
                money_stored = cost_of_drink
                count = count + 1
                report = calculate_ingredients

            else:
                print("Sorry that's not enough money. Money refunded.")

#  TODO 7. make a function to enter the details of the chosen drink


# TODO 5. check if the money is sufficient for the required drink and return the remaining amount

# TODO 6. make a function to update report
