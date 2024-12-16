
class QuizBrain():
    def __init__(self,list):
        self.question_number=0
        self.question_list=list
        self.score=0

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number+=1
        guess=input(f"Q:{self.question_number}{question.text}(true/false): ")
        self.check_answer(guess,question.answer)
    def still_has_questions(self):
        return self.question_number< len(self.question_list)
           
    def check_answer(self,guess,answer):
        if guess == answer:
            self.score+=1
            print(f"You got it right, answer is {answer}!")
        print(f"Your score is {self.score}/{self.question_number}")