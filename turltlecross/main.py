import random
from turtleG import TurtleG
from turtle import Screen
from car import Car
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Cross")
screen.tracer(0)

cars = []
turtle = TurtleG()
scoreboard = Scoreboard()

def createcar():
    car = Car()
    cars.append(car)

running = True
while running:
    if random.randint(1, 20) == 1:
        createcar()

    for car in cars:
        car.move()
        if car.xcor() < -300:
            car.start_position()

        if turtle.distance(car) < 20:
            running = False
            scoreboard.gameover()

    if turtle.ycor() > 200:
        scoreboard.levelup()
        turtle.reset_position()

    screen.listen()
    screen.onkey(turtle.goup, "Up")
    screen.onkey(turtle.godown, "Down")

    screen.update()
    time.sleep(scoreboard.movespeed)

screen.exitonclick()
