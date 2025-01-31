from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
score = Score()
game_is_on = True
screen.listen()
screen.onkey(key='Up',fun=snake.up)
screen.onkey(key='Down',fun=snake.down)
screen.onkey(key='Left',fun=snake.left)
screen.onkey(key='Right',fun=snake.right)
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.tails[0].distance(food)<15:
        food.refresh()
        score.update_score()
    if snake.tails[0].xcor() > 290 or snake.tails[0].xcor() < -290 or snake.tails[0].ycor()>290 or snake.tails[0].ycor()< -290:
        game_is_on = False
        score.game_over()
screen.exitonclick()