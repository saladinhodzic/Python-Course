import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
# making screen
screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)

# making player
player = Player()
screen.onkey(player.move,'space')

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    if player.ycor()>280:
        player.finish()