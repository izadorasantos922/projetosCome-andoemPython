from turtle import Turtle
import time

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.movespeed = 0.1
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(0,250)
        self.write(f"Level: {self.level}", align="center", font=("Courier", 20, "normal"))

    def levelup(self):
        self.level += 1
        self.movespeed *= 0.9
        self.update_scoreboard()
    def gameover(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=("Courier", 80, "normal"))
        


    

