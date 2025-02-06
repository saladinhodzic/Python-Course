from tkinter import *

window = Tk()
window.title("GUI Program")
window.minsize(width=500,height=500)

# making label
label = Label(text="Hello")
label.pack()

# entry

input = Entry(width=10)
input.pack()
def button_click():
    label["text"] = input.get()
# making button
button = Button(text="Click me", command=button_click)
button.pack()
window.mainloop()