import turtle 
import random
turtle.colormode(255)
nindza = turtle.Turtle()
nindza.shape("arrow")
nindza.color("red")
nindza.pensize(2)
nindza.speed(0)
angles = [90,180,270,0]
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)
heading = 0
while heading <= 360:
    nindza.circle(100)
    nindza.setheading(heading)
    nindza.pencolor(random_color())
    heading+=5

screen = turtle.Screen()
screen.exitonclick()