from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

order = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

should_continue = True
while should_continue:
    name_of_drink = input(f"What would you like? ({order.get_items()}): ")
    ordered_drink = order.find_drink(name_of_drink)
    if name_of_drink == "off":
        should_continue = False
    elif name_of_drink == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        if coffee_machine.is_resource_sufficient(ordered_drink):
            if money_machine.make_payment(ordered_drink.cost):
                coffee_machine.make_coffee(ordered_drink)






