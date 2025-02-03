from turtle import Turtle
class Track(Turtle):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 260
        self.create_track()
    def create_track(self):
        while self.y != -280:
            track = Turtle("square")
            track.color("gray")
            track.shapesize(0.3,0.1)
            track.penup()
            track.goto(self.x,self.y)
            self.y-=20