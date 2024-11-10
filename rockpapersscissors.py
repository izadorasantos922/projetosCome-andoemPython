import random
print("Welcome to the game Rock, Paper and Scissors")

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

array = [rock, paper, scissors];

userchoice = input("Choose rock, paper or scissors\n").lower()

match userchoice:
    case "rock":
        userchoice = array[0];
    case "paper":
        userchoice = array[1];
    case "scissors":
        userchoice = array[2];
    case _:
        print("Invalid selection")
        exit()

computerchoice = array[random.randint(0, 2)]

print(f"\nYour choice:\n{userchoice}")
print(f"Computer's choice:\n{computerchoice}")

if userchoice == rock and computerchoice == scissors:
    print("You win!")
elif userchoice == paper and computerchoice == rock:
    print("You win!")
elif userchoice == scissors and computerchoice == paper:
    print("You win!")
elif userchoice == computerchoice:
    print("It's a tie!")
else:
    print("You lose!")
