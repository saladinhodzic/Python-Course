from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(0,270)
        self.rewrite()
    def update_score(self):
        self.clear()
        self.score+=1
        self.rewrite()
    def rewrite(self):
        self.write(f"Your Score: {self.score} ",align='center',font=(12))
    