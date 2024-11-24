from data.menu import MENU
from data.resources import resources

def print_resources():
    print(f"Water {resources['water']} ml")
    print(f"Milk {resources['milk']} ml")
    print(f"Coffe {resources['coffee'] } g")
    print(f"Money ${resources['money']}")

def check_resources(coffe_type):
    if resources['water'] < coffe_type['water']:
        print("There's not enough water for your coffe's type")
        return False
    elif resources['milk'] < coffe_type['milk']:
        print("There's not enough milk for your coffe's type")
        return False
    elif resources['coffee'] < coffe_type['coffee']:
        return False
        print("There's not enough coffe for your coffe's type")
    else:
        return True

def process_coins():
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))

    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return total

def makecoffe(coffe_type):
    coffe = MENU[coffe_type]
    if check_resources(coffe):
        total_money = process_coins()
        if total_money >= coffe['cost']:
            resources['water'] -= coffe['water']
            resources['milk'] -= coffe['milk']
            resources['coffee'] -= coffe['coffee']
            change = round(total_money - coffe['cost'], 2)
            if change > 0:
                print(f"Here is ${change} in change.")
            print(f"Here is your {coffe_type}. Enjoy!")
        else:
            print("Sorry, that's not enough money. Money refunded.")

    else:
        print("Cannot make coffee due to insufficient resources.")


def coffe_machine():
    on = True
    while on:
        coffe_type = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()
        if coffe_type == 'off':
            print("Turning off the coffee machine. Goodbye!")
            on = False
            break
        elif(coffe_type == 'report'):
            print_resources()
        elif coffe_type == 'espresso' or coffe_type == 'latte' or coffe_type == 'cappuccino' :
            makecoffe(coffe_type)
        else:
            print("Invalid choice, please select a valid coffee type or type 'off' to turn off the machine.")
            continue

coffe_machine()