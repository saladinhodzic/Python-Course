from turtle import Turtle,Screen

ninja = Turtle()
screen = Screen()
def move():
    ninja.forward(10)
screen.listen()
screen.onkey(key="space", fun = move)
screen.exitonclick()