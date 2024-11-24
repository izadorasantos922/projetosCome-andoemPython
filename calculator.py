def add(n1, n2):
    return n1 + n2;

def subtract(n1, n2):
    return n1 - n2;

def multiply(n1, n2):
    return n1 * n2;

def divide(n1, n2):
    if n2 == 0:
        print("Cannot divide by zero!")
        return None;
    return n1 / n2
    
    
print("""
 _____________________
|  _________________  |
| |              0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
""")
    
continueWithResult = False
result = None

while True:
    if not continueWithResult:
        numberOne = float(input("What's your first number? "))
    else:
        numberOne = result
    symbol = input("Pick a operation (+, -, *, /): ")
    nextNumber = float(input("What's your next number? "))
    if(symbol == "+"):
        result = add(numberOne, nextNumber)
    elif(symbol == "-"):
        result = subtract(numberOne, nextNumber)
    elif(symbol == "*"):
        result =  multiply(numberOne, nextNumber)
    elif(symbol == "/"):
        result =  divide(numberOne, nextNumber)
        if result == None:
            continue
    else:
        print("Invalid!")
        continue
    print(f"Result: {result}");
     
    choice = input(f"Type 'y' to continue with {result}, or 'n' to start a new calculation, or 'exit' to quit: ").lower()
    if choice == "y":
        continueWithResult = True
    elif choice == "n":
        continueWithResult = False
    elif choice == "exit":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, restarting...")
        continueWithResult = False
