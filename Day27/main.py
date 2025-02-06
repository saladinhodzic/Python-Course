from tkinter import *

window = Tk()
window.title("GUI Program")
window.minsize(width=500,height=500)

# making label
label = Label(text="Hello")
label.pack()

# making button
def button_click():
    label["text"] = "Button was clicked"
button = Button(text="Click me", command=button_click)
button.pack()
window.mainloop()