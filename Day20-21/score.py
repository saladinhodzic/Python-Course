from turtle import Turtle
ALIGNMENT = "center"
class Score(Turtle):
    def __init__(self):
        super().__init__()
        with open("highscore.txt") as high_score:
            data = high_score.read()
            self.high_score = int(data)
        self.score = 0
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(0,270)
        self.rewrite()
    def update_score(self):
        self.score+=1
        self.rewrite()
    def rewrite(self):
        self.clear()
        self.write(f"Your Score: {self.score} High score: {self.high_score}",align=ALIGNMENT,font=(12))
    def reset(self):
        if self.score > self.high_score:
            with open("highscore.txt",'w') as data:
                data.write(str(self.score))
            self.high_score = self.score
        self.score = 0
        self.rewrite()
