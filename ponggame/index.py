from turtle import Turtle, Screen
from paddle import Paddle
import time
from scoreboard import Scoreboard
from ball import Ball

screen = Screen()
screen.bgcolor("pink")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.goup, "Up")
screen.onkey(r_paddle.godown, "Down")
screen.onkey(l_paddle.goup, "w")
screen.onkey(l_paddle.godown, "s")

gameison = True
 
while gameison:
    time.sleep(ball.movespeed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor()> 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 380: 
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
