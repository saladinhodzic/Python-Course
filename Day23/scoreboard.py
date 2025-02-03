from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('black')
        self.goto(-260,260)
        self.score=0
        self.level()
    def level(self):
        self.clear()
        self.write(f"Level: {self.score+1}",font=FONT)
    def update_score(self):
        self.score+=1
        self.level()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align='center',font=FONT)