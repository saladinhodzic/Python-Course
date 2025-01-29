from turtle import Turtle,Screen

nindza = Turtle()
nindza.shape("turtle")
nindza.color("red")

for i in range(4,10):
    for j in range(i):
        nindza.forward(50)
        nindza.right(360/i)
    


screen = Screen()
screen.exitonclick()