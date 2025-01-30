from turtle import Turtle,Screen

ninja = Turtle()
screen = Screen()
def forward():
    ninja.forward(20)
def backward():
    ninja.back(20)
def clockwise():
    current = ninja.heading()
    ninja.setheading(current+10)
def counter_clockwise():
    current = ninja.heading()
    ninja.setheading(current - 10)
def clear():
    ninja.setheading(0)
    ninja.goto(0,0)
    ninja.clear()
screen.listen()
screen.onkey(key="w", fun = forward)
screen.onkey(key="s", fun = backward)
screen.onkey(key="d", fun = clockwise)
screen.onkey(key="a", fun = counter_clockwise)
screen.onkey(key="c", fun = clear)
screen.exitonclick()