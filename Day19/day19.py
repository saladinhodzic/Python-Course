from turtle import Turtle,Screen

screen = Screen()
screen.setup(500,500)
user_bet = screen.textinput(title="Enter your bet:",prompt="Enter color: ")
colors = ['red','green','purple','yellow','orange','blue']
y = -150
for turtle in colors:
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.shape('turtle')
    new_turtle.color(turtle)
    new_turtle.goto(-230,y)
    y+=50
screen.exitonclick()