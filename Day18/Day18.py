from turtle import Turtle, Screen
import random
our_turtle=Turtle()
our_turtle.shape("turtle")
colors=['red','green','blue']

directions=[0,90,180,270]

while(True):
    our_turtle.color(random.choice(colors))
    our_turtle.forward(20)
    our_turtle.setheading(random.choice(directions))
    






















screen=Screen()
screen.exitonclick()