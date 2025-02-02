from turtle import Turtle
ALIGNMENT = "center"
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
        self.score+=1
        self.clear()
        self.rewrite()
    def rewrite(self):
        self.write(f"Your Score: {self.score} ",align=ALIGNMENT,font=(12))
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over!",align=ALIGNMENT,font=(16))
