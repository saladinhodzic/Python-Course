from turtle import Turtle
POSITIONS = [(-380,0),(-380,-20),(-380,-40)]
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.squares = []
        self.create_paddle()
    def create_paddle(self):
        for i in range(3):
            square = Turtle("square")
            square.color("white")
            square.penup()
            square.goto(POSITIONS[i])
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