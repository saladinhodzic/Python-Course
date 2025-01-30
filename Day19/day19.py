from turtle import Turtle,Screen
import random
screen = Screen()
screen.setup(500,500)
user_bet = screen.textinput(title="Enter your bet:",prompt="Enter color: ")
colors = ['red','green','purple','yellow','orange','blue']
turtles=[]
y = -150
for turtle in colors:
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.shape('turtle')
    new_turtle.color(turtle)
    new_turtle.goto(-230,y)
    y+=50
    turtles.append(new_turtle)

race_end = False
while not race_end:
    for turtle in turtles:
        if turtle.xcor()>230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You won!")
            else:
                print("You lost!")
            race_end = True
        turtle.forward(random.randint(5,15))
screen.exitonclick()