from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

items = menu.get_items()

while True:
    user_wish = input(f"What would you like? {items}: ").lower()

    if user_wish == 'off':
        break
    elif user_wish == 'report':
        coffee_maker.report()
        money_machine.report()
    elif user_wish == 'cappuccino' or user_wish == 'latte' or user_wish == 'espresso':
        coffee = menu.find_drink(user_wish)

        if coffee_maker.is_resource_sufficient(coffee):
            print("Sufficient resources")
            if money_machine.make_payment(coffee.cost):
                coffee_maker.make_coffee(coffee)
        else:
            print("Insufficient resources")
