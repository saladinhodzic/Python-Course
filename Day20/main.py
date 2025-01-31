from turtle import Screen
from snake import Snake
import time
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
game_is_on = True
screen.listen()
while game_is_on:
    screen.update()
    time.sleep(0.1)
    screen.onkey(key='Up',fun=snake.up)
    screen.onkey(key='Down',fun=snake.down)
    screen.onkey(key='Left',fun=snake.left)
    screen.onkey(key='Right',fun=snake.right)
    snake.move()
screen.exitonclick()