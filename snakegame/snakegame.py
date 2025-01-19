from turtle import Screen
from snake import Snake
import time 
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen() 
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

gameison = True
while gameison:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280:
        gameison = False
        scoreboard.gameover()
    
    for part in snake.segments:
        if part == snake.head:
            pass
        elif snake.head.distance(part) < 18:
            gameison = False
            scoreboard.gameover()
    



screen.exitonclick()