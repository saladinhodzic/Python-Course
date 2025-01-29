import turtle 
import random
turtle.colormode(255)
nindza = turtle.Turtle()
nindza.shape("turtle")
nindza.color("red")
nindza.pensize(10)
nindza.speed(5)
angles = [90,180,270,0]
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)
for _ in range(100):
    nindza.right(random.choice(angles))
    nindza.forward(30)
    nindza.pencolor(random_color())

screen = turtle.Screen()
screen.exitonclick()