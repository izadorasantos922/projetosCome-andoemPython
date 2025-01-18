# Draw a dashed line
# from turtle import Turtle, Screen

# screen = Screen()
# screen.screensize(400, 300)
# screen.listen()

# turtle = Turtle()
# turtle.shape("turtle")
# turtle.color("orange")
# turtle.penup()
# turtle.goto(-250, -200)
# turtle.pencolor("blue")
# turtle.pendown()
# for i in range(10): 
#     turtle.forward(25)
#     turtle.penup()
#     turtle.forward(25)
#     turtle.pendown()

# screen.exitonclick()

# from turtle import Turtle, Screen

# screen = Screen()
# screen.screensize(400, 300)
# screen.listen()

# turtle = Turtle()
# turtle.shape("turtle")
# turtle.color("orange")
# turtle.penup()
# turtle.goto(-100, 200)
# turtle.pencolor("blue")
# turtle.pendown()
# number = 5

# def draw(numberofsides):
#     angle = 360 / numberofsides
#     for i in range(numberofsides): 
#         turtle.forward(100)
#         turtle.right(angle)

# for i in range(3, 11):
#     draw(i)


# screen.exitonclick()
# import random
# from turtle import Turtle, Screen

# screen = Screen()
# screen.screensize(400, 300)
# screen.listen()

# turtle = Turtle()
# turtle.shape("turtle")
# turtle.color("orange")
# turtle.penup()
# turtle.goto(-100, -100)
# turtle.pencolor("blue")
# turtle.pendown()
# number = 5
# colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown"]
# def walk(numberofsteps):

#     for i in range(numberofsteps): 
#         turtle.forward(random.randint(25, 100))
#         turtle.right((72))
# walk(100)


# screen.exitonclick()

import random
from turtle import Turtle, Screen

screen = Screen()
screen.screensize(400, 300)
screen.listen()

turtle = Turtle()
turtle.shape("turtle")
turtle.color("orange")
turtle.penup()
turtle.goto(0,0)
turtle.pencolor("blue")
turtle.pendown()
turtle.speed("fastest")

for i in range(40):
    turtle.circle(120, 360)  
    turtle.setheading(turtle.heading() + 10)



screen.exitonclick()
