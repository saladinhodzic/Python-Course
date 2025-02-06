import tkinter

window = tkinter.Tk()
window.title("GUI Program")
window.minsize(width=500,height=500)

label = tkinter.Label(text="Hello")
label.pack()

window.mainloop()