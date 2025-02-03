from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(0.75)
        self.y = 10
        self.x = 10
    def move(self):
        y = self.ycor() + self.y
        x = self.xcor() + self.x
        self.goto(x,y)
    def bounce(self):
        self.y *= -1 
    def paddle_hit(self):
        self.x *= -1