from turtle import Turtle
FONT = ("Arial",20,"normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.first_player = 0
        self.second_player = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0,260)
        self.update_text()
    def update_text(self):
        self.clear()
        self.write(f"{self.first_player} | {self.second_player}",align='center',font =FONT )
    def update_score(self,ball):
        if ball.xcor()>390:
            self.first_player+=1
        else:
            self.second_player+=1
        self.update_text()