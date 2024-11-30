from data.menu import Menu
from coffeMaker import CoffeMaker
from moneyMachine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? latte, cappuciono or espresso ")
    if(choice == "off"):
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffe(drink)
