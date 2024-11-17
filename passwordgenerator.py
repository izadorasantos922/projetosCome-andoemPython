import random

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '+', '{', '}', '[', ']', ';', ':', '"', "'", '<', '>', ',', '.', '/', '?', '~']
password = []

nr_letters = int(input("How many letters do you want? "))
for i in range(nr_letters):
    password.append(letters[random.randint(0, len(letters) - 1)])

nr_symbols = int(input("How many symbols do you want? "))
for i in range(nr_symbols):
    password.append(symbols[random.randint(0, len(symbols) - 1)])

nr_numbers = int(input("How many numbers do you want? "))
for i in range(nr_numbers):
    password.append(numbers[random.randint(0, len(numbers) - 1)])

random.shuffle(password)

password_str = ''.join(password)

print(f"Your password is: {password_str}")
