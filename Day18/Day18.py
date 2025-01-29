from turtle import Turtle,Screen

nindza = Turtle()
nindza.shape("turtle")
nindza.color("red")

for _ in range(5):
    nindza.forward(10)
    nindza.penup()
    nindza.forward(10)
    nindza.pendown()



screen = Screen()
screen.exitonclick()