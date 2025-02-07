from tkinter import *

window = Tk()
window.title("GUI Program")
window.minsize(width=500,height=500)

# making label
label = Label(text="Hello")
label.grid(column=0,row=0)

def button_click():
    label["text"] = input.get()

button = Button(text="Click me", command=button_click)
button.grid(column=1,row=1)

new_button = Button(text="Click me", command=button_click)
new_button.grid(column=3,row=0)
# entry

input = Entry(width=10)
input.grid(column=3,row=2)







window.mainloop()