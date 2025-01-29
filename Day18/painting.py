import colorgram
import turtle
import random
turtle.colormode(255)
colors = colorgram.extract("hirst-painting.jpg",12)
new_colors = [tuple(color.rgb) for color in colors]

ninja = turtle.Turtle()
ninja.hideturtle()
ninja.penup()
ninja.speed(0)
go_y=0
for i in range(10):
    for j in range(10):
        ninja.dot(15,random.choice(new_colors))
        ninja.forward(50)
    go_y+=50
    ninja.goto(0,go_y)







screen = turtle.Screen()
screen.exitonclick()