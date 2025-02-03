# Pong Game
import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
from track import Track
# creating screen
screen = Screen()
screen.setup(800,600)
screen.tracer(0)
screen.bgcolor("black")

# creating track for better UI
track = Track()

# creating paddle
first_player = Paddle()
first_player.create_paddle()
second_player = Paddle()
second_player.x = 380
second_player.create_paddle()

# moving the paddles
screen.listen()
screen.onkeypress(first_player.move_up,"Up")
screen.onkeypress(first_player.move_down,"Down")
screen.onkeypress(second_player.move_up,"w")
screen.onkeypress(second_player.move_down,"s")

# making the ball
ball = Ball()

# making the scoreboard
score = Score()

# starting the game
game_on = True
while game_on:
    screen.update() 
    time.sleep(0.05)
    ball.move()
    if ball.xcor()>390 or ball.xcor()<-390:
        score.update_score(ball)
        ball.restart()
        time.sleep(0.3)
        ball.move()
    if ball.ycor()< -290 or ball.ycor() > 290:
        ball.bounce()
    for i in range(len(first_player.squares)):
        if first_player.squares[i].distance(ball) <25 or second_player.squares[i].distance(ball)<25:
            ball.paddle_hit()

# exiting the program
screen.exitonclick()
