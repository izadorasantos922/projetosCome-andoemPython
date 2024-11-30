from turtle import Turtle, Screen
import random

screen = Screen()
screen.screensize(400, 300)
screen.listen()

numberOfTurtles = screen.textinput(title="Let's begin", prompt="How many turtles do you want? ")
numberOfGamers = screen.textinput(title=" ", prompt="How many players? ")

if numberOfTurtles.isdigit():
    numberOfTurtles = int(numberOfTurtles)
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown"]
    turtles = []  
    x = -250
    y = -200
    for i  in range(numberOfTurtles):
        new_turtle = Turtle()
        new_turtle.shape("turtle")
        new_turtle.color(colors[i % len(colors)])
        new_turtle.penup()  
        new_turtle.goto(x, y + i * 60)
        turtles.append(new_turtle)
       
bets = []
if(numberOfGamers.isdigit()):
    numberOfGamers = int(numberOfGamers)
    for i in range(numberOfGamers):
        bet = screen.textinput(title="Let's bet", prompt=f"which color do you choose? player{i + 1}")
        bets.append(bet)

if len(bets) > 0:
    race = True

while race:
    for turtle in turtles: 
        if turtle.xcor() > 250:
            race = False
            colorwinner = turtle.pencolor()
            for i,bet in enumerate(bets):
                if colorwinner == bet:
                    print(f"Congratulations Player {i + 1}! You chose the right turtle!")                
                    break
                else:
                    print(f"Sorry Player {i + 1} you lose! You chose the wrong turtle!")                


        distance = random.randint(5, 20)  
        turtle.forward(distance)            
screen.exitonclick()
