import os
import random

chanceHard = 5
chanceEasy = 10
chances = 0;

def difficult():
    attempts = input("type (e) for Easy or (h) hard ").lower()
    if(attempts == 'e'):
        return chanceEasy
    elif(attempts == 'h'):
        return chanceHard
    else:
        print("Invalid")
        exit()

def choseANumber():
    try:
        chosenNumber = int(input("Guess a number fom 1 to 100 "))
        return chosenNumber
    except ValueError:
        print("Write a number ")
        exit()
    
def guessTheNumber():
    number = random.randint(1, 100)
    win = False
    chances = difficult();
    while not win:
        print("\n")
        print(f"You have {chances} chances")
        chosenNumber = choseANumber()
        if(chances > 0):
            if(chosenNumber == number):
                print(f"You win the number is {number}");
                win = True
            elif(chosenNumber < number):
                print("The number is higher");
                chances -= 1
                continue;
            elif(chosenNumber > number):
                print("The number is low");
                chances -= 1
                continue;
        else:
            print(f"You lose the number is {number}")
            exit()

guessTheNumber()

