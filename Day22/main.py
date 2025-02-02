# Pong Game
import time
from turtle import Screen
from paddle import Paddle

# creating screen
screen = Screen()
screen.setup(800,600)
screen.tracer(0)
screen.bgcolor("black")

# creating paddle
first_player = Paddle()
first_player.create_paddle()
second_player = Paddle()
second_player.x = 380
second_player.create_paddle()
# moving the first paddle
screen.listen()
screen.onkeypress(first_player.move_up,"Up")
screen.onkeypress(first_player.move_down,"Down")
screen.onkeypress(second_player.move_up,"w")
screen.onkeypress(second_player.move_down,"s")
# controlling the animation
screen.update()

# exiting the program
screen.exitonclick()
