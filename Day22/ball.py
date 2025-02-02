from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(0.75)
    def random_heading(self):
        heading = random.randint(0,270)
        self.setheading(heading)
    