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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def paid_money():
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pannies = int(input("how many pennies?: "))
    total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pannies * 0.01
    return total

def check_resources(resource, choise):
    for i in resource:
        if resource[i] > resources[i]:
            print(f"Sorry there is not enough {i}.")
            return False
        return True

remain_on = True

while remain_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        remain_on = False

    elif choice == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: ${profit}")

    else:
        choice_ingredient = MENU[choice]

        if check_resources(choice_ingredient['ingredients'], choice):
            money = paid_money()
            if money < choice_ingredient["cost"]:
                print("Sorry that's not enough money. Money refunded.")
                remain_on = False

            else:
                for i in choice_ingredient['ingredients']:
                    resources[i] -= choice_ingredient['ingredients'][i]
                print(f"Here is your {choice}. Enjoy!")
                change = round(money - choice_ingredient["cost"], 2)
                print(f"Here is ${change} in change.")
                profit += choice_ingredient["cost"]

        else:
            remain_on = False


