import random 


friends = [];

number = int(input("How many friends in total? "))
i = 0
while(i < number):
    friend = input("Insert a name of a friend ");
    if friend:
        friends.append(friend)
    i += 1

chosen_friend = random.randint(0, number - 1);

print(f"The friend who will pay the bill is {friends[chosen_friend]}")