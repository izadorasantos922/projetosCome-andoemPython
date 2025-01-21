from turtle import Turtle
import random 
import time

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(["red", "blue", "green", "yellow", "purple", "brown", "orange", "pink"]))
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.penup()
        self.start_position()

    def start_position(self):
        random_y = random.randint(-200, 200)
        self.goto(300, random_y)

    def move(self):
        self.setx(self.xcor() - 5 )

