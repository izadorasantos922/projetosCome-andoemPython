from turtle import Turtle

class TurtleG(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.reset_position()

    def goup(self):
        if self.ycor() < 250:  
            self.new_y = self.ycor() + 20
            self.goto(self.xcor(), self.new_y)
    def godown(self):
        if self.ycor() > -250:
            self.new_y = self.ycor() - 20
            self.goto(self.xcor(), self.new_y)
    def reset_position(self):
        self.goto(0,-250)
        self.setheading(90)


