from turtle import Turtle,Screen
import random
nindza = Turtle()
nindza.shape("turtle")
nindza.color("red")
nindza.pensize(10)
nindza.speed(5)
angles = [90,180,270,360]
colors = ["red","blue","yellow"]
for _ in range(100):
    nindza.right(random.choice(angles))
    nindza.forward(30)
    nindza.pencolor(random.choice(colors))

screen = Screen()
screen.exitonclick()