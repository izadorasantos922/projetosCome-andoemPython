from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("White")
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
         self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def gameover(self):
        self.goto(0, 0)
        self.write(f"GAMER OVER", align="center", font=("Arial", 24, "normal"))


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
       




