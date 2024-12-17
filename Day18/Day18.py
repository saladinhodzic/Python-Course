from turtle import Turtle, Screen

our_turtle=Turtle()

degrees=360
sides=4
while (True):
    for _ in range(sides):
        our_turtle.forward(20)
        our_turtle.right(degrees/sides)
    sides+=1






















screen=Screen()
screen.exitonclick()