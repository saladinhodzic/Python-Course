from tkinter import *
import pandas
import random
FONT_LANG = ("Arial",35,"italic")
FONT_WORD = ("Arial",60,"bold")
BACKGROUND = "#F2EFE7"
timer = None
random_word = None
# showing random words
try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("words.csv")
else:
    data_dict = data.to_dict(orient="records")
def generate_word():
    global timer,random_word
    if timer:
        window.after_cancel(timer)
    random_word = random.choice(data_dict)
    canvas.itemconfig(word,text=random_word["German"],fill='black')
    canvas.itemconfig(lang,text="German",fill='black')
    canvas.itemconfig(background_image,image=front_card)
    timer = window.after(3000,flip)
    
def update_csv():
    data_dict.remove(random_word)
    updated_data = pandas.DataFrame(data_dict)
    updated_data.to_csv('words_to_learn.csv',index=False)
    generate_word()
def flip():
    canvas.itemconfig(background_image,image = back_card)
    canvas.itemconfig(lang,text = "English",fill = "white")
    canvas.itemconfig(word,text = random_word["English"],fill = "white")
# making the UI

window = Tk()
window.title("Flashy Card")
window.minsize(width=800,height=550)
window.config(padx=50,pady=50)

back_card = PhotoImage(file="images/card_back.png")
front_card = PhotoImage(file = "images/card_front.png")
canvas = Canvas(width=800,height=526,bg=BACKGROUND)
background_image = canvas.create_image(400,270)
canvas.grid(column=0,row=0,columnspan=2)
lang = canvas.create_text(400,150,font=FONT_LANG)
word = canvas.create_text(400,263,font=FONT_WORD)

wrong = PhotoImage(file="images/wrong.png")
right = PhotoImage(file="images/right.png")

wrong_button = Button(image=wrong,highlightthickness=0,command=generate_word)
wrong_button.grid(column=0,row=1)
right_button = Button(image = right,highlightthickness=0,command=update_csv)
right_button.grid(column=1,row=1)

generate_word()
window.mainloop()