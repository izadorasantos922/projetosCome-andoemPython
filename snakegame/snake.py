from turtle import Turtle
STARTING_POSITIONS = [(0,0),(-20,0), (-40,0)]
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        for position in STARTING_POSITIONS :
            self.add_part(position)
    def add_part(self, position):
        new_part = Turtle("square")
        new_part.color("white")
        new_part.penup()
        new_part.goto(position)
        self.segments.append(new_part)

    def extend(self):
        self.add_part(self.segments[-1].position()) 


    def move(self):
        for seg in range(len(self.segments) - 1,0,-1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(MOVE)
    def up(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(UP)
    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)
    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)
