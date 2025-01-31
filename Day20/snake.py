from turtle import Turtle,Screen
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
x=0
for _ in range(3):
    new_turtle = Turtle()
    new_turtle.shape("square")
    new_turtle.color("white")
    new_turtle.setx(x)
    x-=20




screen.exitonclick()