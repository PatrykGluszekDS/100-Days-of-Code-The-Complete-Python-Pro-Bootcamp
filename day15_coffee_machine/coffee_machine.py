MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def report(stock):
    print(f"water: {stock['water']}ml ")
    print(f"milk: {stock['milk']}ml")
    print(f"coffee: {stock['coffee']}g")
    print(f"money: ${stock['money']}")


def check_resources(coffe):
    for resource, amount in MENU[coffe]["ingredients"].items():
        if resources[resource] < amount:
            print(f"It is not enough {resource}!")
            return False
    return True


def input_money():
    print("Please insert coins.")
    quarters = int(input("How many quarters ($0.25)?: "))
    dimes = int(input("How many dimes ($0.10)?: "))
    nickles = int(input("How many nickles ($0.05)?: "))
    pennies = int(input("How many pennies ($0.01)?: "))
    return quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01


def using_stuff(coffee):
    needed_water = MENU[coffee]['ingredients']['water']
    needed_coffee = MENU[coffee]['ingredients']['coffee']
    resources['water'] -= needed_water
    resources['coffee'] -= needed_coffee
    if coffee == 'latte' or coffee == 'cappuccino':
        needed_milk = MENU[coffee]['ingredients']['milk']
        resources['milk'] -= needed_milk


while True:
    user_wish = input("What would you like? (espresso/latte/cappuccino): ")

    if user_wish == 'off':
        break
    elif user_wish == 'report':
        report(resources)
    elif user_wish == 'espresso' or user_wish == 'latte' or user_wish == 'cappuccino':
        is_ok = check_resources(user_wish)
        if is_ok:  # checking resources
            monetary_value = input_money()
            if monetary_value < MENU[user_wish]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
                continue
            else:
                resources['money'] += MENU[user_wish]["cost"]

                if monetary_value > MENU[user_wish]["cost"]:
                    rest = monetary_value - MENU[user_wish]["cost"]
                    print(f"Here is ${rest} dollars in change")

                using_stuff(user_wish)
                print(f"Here is your {user_wish}. Enjoy!")
