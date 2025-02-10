from tkinter import *

BACKGROUND = "#F2EFE7"
# making the UI

window = Tk()
window.title("Flashy Card")
window.minsize(width=800,height=550)
window.config(padx=50,pady=50)

front_card = PhotoImage(file = "images/card_front.png")
canvas = Canvas(width=800,height=526,bg=BACKGROUND)
canvas.create_image(400,270,image = front_card)
canvas.grid(column=0,row=0,columnspan=2)

wrong = PhotoImage(file="images/wrong.png")
right = PhotoImage(file="images/right.png")

wrong_button = Button(image=wrong,highlightthickness=0)
wrong_button.grid(column=0,row=1)
right_button = Button(image = right,highlightthickness=0)
right_button.grid(column=1,row=1)


window.mainloop()