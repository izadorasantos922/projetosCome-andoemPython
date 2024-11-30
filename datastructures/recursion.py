def fibonacci(number):
    if number == 0:
        return 0;
    elif number == 1:
        return 1;
    else:
        return fibonacci(number - 2) + fibonacci(number - 1)


def fatorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * fatorial(x - 1)

for i in range(0, 10):
    print(fibonacci(i), end=" ")

