THEME_COLOR = "#375362"
from quiz_brain import QuizBrain
from tkinter import *
class UserInterface():
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20,width=400,height=600)
        # creating label for score
        self.label = Label(text="Score : 0",bg=THEME_COLOR,fg="white",font=("Arial",16))
        self.label.grid(column=1,row=0)
        # creating canvas
        self.canvas = Canvas(width=300,height=250)
        self.canvas.grid(pady=50,column=0,row=1,columnspan=2)
        self.question_text = self.canvas.create_text(150,125,text="Quote",font=("Arial",20,"italic"),width=280)
        # creating buttons
        self.true = PhotoImage(file="images/true.png")
        self.false = PhotoImage(file="images/false.png")
        self.button1 = Button(image=self.true,highlightthickness=0,command=self.check_true)
        self.button2 = Button(image=self.false,highlightthickness=0,command=self.check_false)
        self.button1.grid(column=0,row=2)
        self.button2.grid(column=1,row=2)
        # get questions
        self.get_next_question()
        self.window.mainloop()
    def get_next_question(self):
        question = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text,text = question)
    def check_true(self):
        answer = self.quiz.check_answer("True")
        if answer:
            print("You got it right")
        self.get_next_question()
    def check_false(self):
        answer = self.quiz.check_answer("False")
        if answer:
            print("You got it wrong")
        self.get_next_question()