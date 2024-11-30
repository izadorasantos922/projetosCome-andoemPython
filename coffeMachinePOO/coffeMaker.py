class CoffeMaker:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }

    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        if drink is None:
            print("Invalid drink. Cannot proceed with making coffee.")
            return False
        can_make = True 
        for item in drink.ingredientes:
            if drink.ingredientes[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}")
                can_make = False
        return can_make

    def make_coffe(self, order):
        for item in order.ingredientes:
            self.resources[item] -= order.ingredientes[item]
        print(f"Here is your {order.name}. Enjoy!")
