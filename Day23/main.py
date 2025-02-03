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

# making cars
cars = CarManager()
game_is_on = True
spawn_cars=0
cars.spawn()
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.move()
    if spawn_cars == 6:
        cars.spawn()
        spawn_cars=0 
    if player.ycor()>280:
        player.finish()
    spawn_cars+=1