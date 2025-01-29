from turtle import Turtle,Screen

nindza = Turtle()
nindza.shape("turtle")
nindza.color("red")

for _ in range(4):
    nindza.forward(100)
    nindza.right(90)



screen = Screen()
screen.exitonclick()