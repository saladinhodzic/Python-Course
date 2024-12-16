from Question import Question
from data import question_data
from quiz_brain import QuizBrain
data=[]
for object in question_data:
    new_question=Question(object["text"],object["answer"])
    data.append(new_question)
    
quiz=QuizBrain(data)

while quiz.still_has_questions():
    quiz.next_question()
    print("\n")

print("You have completed quiz!")
print(f"Your final score is {quiz.score}/{quiz.question_number}")