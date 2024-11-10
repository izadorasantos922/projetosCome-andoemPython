print("Welcome");
bill = input("How much is your bill? \n")
waiter_percent = input("How much would you like to tip (in percentage)? \n")

def Calculate(bill, waiter_percent):
    bill = int(bill);
    waiter_percent = int(waiter_percent)

    total = (bill * (waiter_percent / 100)) + bill
    return total

print(f"The total is {Calculate(bill, waiter_percent)}")