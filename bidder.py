print(r"""
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\
""")

print("Welcome to the secret auction program \n")

def winner(dict):
    maxBid = 0;
    winner = ""
    for person in dict:
        if dict[person] > maxBid:
            maxBid = dict[person];
            winner = person
    print(f"The winner is {person} with ${maxBid}")

bidders = {}
end_game = False

while not end_game:
    print("\n")
    name = input("What's your name? ")
    bid = int(input("What's your bid? "))
    bidders[name] = bid
    restart = input("Are there any more bidders? (yes) or (no) ")
    if restart == "no":
        end_game = True
        print("\n")
        winner(bidders)
        exit()

