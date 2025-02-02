# Pong Game
import time
from turtle import Screen
from paddle import Paddle

# creating screen
screen = Screen()
screen.setup(800,600)
# screen.tracer(0)
screen.bgcolor("black")

# creating paddle
first_player = Paddle()
# moving the first paddle
screen.listen()
screen.onkeypress(first_player.move_up,"Up")
screen.onkeypress(first_player.move_down,"Down")
# controlling the animation
# screen.update()

# exiting the program
screen.exitonclick()
