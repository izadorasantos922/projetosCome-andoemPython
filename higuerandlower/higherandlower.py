from data import data
from src.art import logo
from src.art import vs
import random

print(logo)

def game():
    end_game = False
    userscore = 0;
    random_celebrity1 = None;
    while not end_game:
        if(not random_celebrity1):
            random_celebrity1 = random.choice(data)
            continue
        random_celebrity2 = random.choice(data)
        print(f"Compare A: {random_celebrity1['name']}, {random_celebrity1['description']}, from {random_celebrity1['country']}")
        print(vs)
        print(f"Compare B: {random_celebrity2['name']}, {random_celebrity2['description']}, from {random_celebrity2['country']}")
        userChoice = input("Who has more followers? Type 'A' or 'B': ").lower();
        if(userChoice == "a"):
            if(random_celebrity1['follower_count'] > random_celebrity2['follower_count']):
                userscore += 1
                print(f"You are right! Current score {userscore}")
                continue;
            else:
                print("You lose!")
                break
        elif(userChoice == "b"):
            if(random_celebrity2['follower_count'] > random_celebrity1['follower_count']):
                userscore += 1
                print(f"You are right! Current score {userscore}")
            else:
                print(f"You lose! you final score is {userscore}")
                break
        else:
            print("Invalid")
            break
        
game();