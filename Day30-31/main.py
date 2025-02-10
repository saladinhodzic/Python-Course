from tkinter import *
import pandas
import random
FONT_LANG = ("Ariel",35,"italic")
FONT_WORD = ("Ariel",60,"bold")
BACKGROUND = "#F2EFE7"

# showing random words

def generate_word():
    data = pandas.read_csv("words.csv")
    data_dict = data.to_dict(orient="records")
    random_word = random.choice(data_dict)
    canvas.itemconfig(word,text=random_word["German"])
# making the UI

window = Tk()

window.title("Flashy Card")
window.minsize(width=800,height=550)
window.config(padx=50,pady=50)

front_card = PhotoImage(file = "images/card_front.png")
canvas = Canvas(width=800,height=526,bg=BACKGROUND)
canvas.create_image(400,270,image = front_card)
canvas.grid(column=0,row=0,columnspan=2)
lang = canvas.create_text(400,150,text="German",font=FONT_LANG)
word = canvas.create_text(400,263,text="Ich",font=FONT_WORD)

wrong = PhotoImage(file="images/wrong.png")
right = PhotoImage(file="images/right.png")

wrong_button = Button(image=wrong,highlightthickness=0)
wrong_button.grid(column=0,row=1)
right_button = Button(image = right,highlightthickness=0,command=generate_word)
right_button.grid(column=1,row=1)


window.mainloop()