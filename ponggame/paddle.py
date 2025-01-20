from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("Black")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position)

    def goup(self):
        if self.ycor() < 250:  
            self.new_y = self.ycor() + 20
            self.goto(self.xcor(), self.new_y)

    def godown(self):
        if self.ycor() > -250:
            self.new_y = self.ycor() - 20
            self.goto(self.xcor(), self.new_y)

