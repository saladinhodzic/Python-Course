from turtle import Turtle
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.squares = []
        self.x = -380
        self.y = 0
    def create_paddle(self):
        for _ in range(3):
            square = Turtle("square")
            square.color("white")
            square.penup()
            square.goto(self.x,self.y)
            self.y-=20
            square.setheading(90)
            self.squares.append(square)
    def move_up(self):
        for i in range(len(self.squares)-1,0,-1):
            self.squares[i].goto(self.squares[i-1].pos())
        self.squares[0].forward(20)
    def move_down(self):
        for i in range(len(self.squares)-1):
            self.squares[i].goto(self.squares[i+1].pos())
        self.squares[-1].back(20)