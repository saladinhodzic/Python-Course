from Question import Question
from data import question_data

data=[]
for object in question_data:
    new_question=Question(object["text"],object["answer"])
    data.append(new_question)
    
print(data[0].text)