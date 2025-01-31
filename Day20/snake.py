import turtle
class Snake():
    def __init__(self):
        self.tails= []
        self.x = 0
        for _ in range(3):
            new_turtle = turtle.Turtle()
            new_turtle.shape("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.setx(self.x)
            self.x-=20
            self.tails.append(new_turtle)
    def move(self):
        for turtle in range(len(self.tails)-1,0,-1):
            new_x = self.tails[turtle-1].xcor()
            new_y = self.tails[turtle-1].ycor()
            self.tails[turtle].goto(new_x,new_y)
        self.tails[0].forward(20)
    def up(self):
        if self.tails[0].heading() != 270:
            self.tails[0].setheading(90)
    def down(self):
        if self.tails[0].heading() != 90:
            self.tails[0].setheading(270)
    def right(self):
        if self.tails[0].heading() != 180:
            self.tails[0].setheading(0)
    def left(self):
        if self.tails[0].heading() != 0:    
            self.tails[0].setheading(180)