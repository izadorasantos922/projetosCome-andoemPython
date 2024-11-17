smallpizzaprice = 15;
mediumpizzaprice = 20;
largepizzaprice = 25;
pepperonismallpizza = 2;
pepperonimediumorlargepizza = 3;
cheeseprice = 1;
total = 0;

typeofpizza = input("What size of pizza do you want S M or L? ").lower()
if(typeofpizza == "s"):
    total += smallpizzaprice;
elif(typeofpizza == "m"):
    total += mediumpizzaprice;
elif(typeofpizza == "l"):
    total += largepizzaprice;
else:
    print("Invalid");
    exit();
pepperoni = input("Do you want pepperoni on your pizza Y or N? ").lower()
if(pepperoni == "y" and total == smallpizzaprice):
    total += pepperonismallpizza;
elif(pepperoni == "y" and (total == mediumpizzaprice or total == largepizzaprice)):
    total += pepperonimediumorlargepizza;
if( pepperoni != "y" and pepperoni != "n"):
    print("Invalid");
    exit();

cheese = input("Do you want cheese on your pizza Y or N? ").lower()

if(cheese == "y"):
    total += cheeseprice;
if(cheese != "y" and cheese != "n"):
    print("Invalid");
    exit();

print(f"The total is: ${total}")


