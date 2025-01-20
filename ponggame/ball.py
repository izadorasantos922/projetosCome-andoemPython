from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("purple")
        self.goto(0,0)
        self.y_move = 10
        self.x_move = 10
        self.movespeed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.movespeed *= 0.9
    def bounce_x(self):
        self.x_move *= -1
        self.movespeed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.movespeed = 0.1
        self.bounce_x()
         


