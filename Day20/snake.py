from turtle import Turtle,Screen
import time
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
segments= []
x=0
for _ in range(3):
    new_turtle = Turtle()
    new_turtle.shape("square")
    new_turtle.color("white")
    new_turtle.penup()
    new_turtle.setx(x)
    x-=20
    segments.append(new_turtle)
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for turtle in range(len(segments)-1,0,-1):
        new_x = segments[turtle-1].xcor()
        new_y = segments[turtle-1].ycor()
        segments[turtle].goto(new_x,new_y)
    segments[0].forward(20)
screen.exitonclick()