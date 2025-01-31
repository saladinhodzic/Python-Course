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