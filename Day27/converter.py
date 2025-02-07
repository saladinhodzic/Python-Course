# mile to km GUI Program
import tkinter

window = tkinter.Tk()
window.title("Mile To KM")
window.minsize(width=500,height=500)

input = tkinter.Entry()
input.grid(row=0,column=1)

miles = tkinter.Label(text="Miles")
miles.grid(row=0,column=2)

is_equal_to = tkinter.Label(text="is equal to")
is_equal_to.grid(row=1,column=0)

km_num = tkinter.Label(text="0")
km_num.grid(row=1,column=1)

km = tkinter.Label(text="KM")
km.grid(row=1,column=2)

def convert():
    km_num["text"] = round(int(input.get()) * 1.6,2)

button = tkinter.Button(text="Convert",command=convert)
button.grid(row=2,column=1)










window.mainloop()