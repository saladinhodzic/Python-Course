from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=20,pady=20)
logo = PhotoImage(file="logo.png")
canvas = Canvas(height=200,width=200)
canvas.create_image(100,100,image = logo)
canvas.grid(column=1,row=0)

label_1= Label(text="Website: ")
label_1.grid(column=0,row=1)
input_1 = Entry(width=50)
input_1.grid(column=1,row=1,columnspan=2)

label_2 = Label(text="Email/Username: ")
label_2.grid(column=0,row=2)
input_2 = Entry(width=50)
input_2.grid(column=1,row=2,columnspan=2)

label_3 = Label(text="Password: ")
label_3.grid(column=0,row=3)
input_3 = Entry(width=25)
input_3.grid(column=1,row=3)
button_1 = Button(text="Generate Password")
button_1.grid(column=2,row=3)

button_2 = Button(text="Add",width=43)
button_2.grid(column=1,row=4,columnspan=2)







window.mainloop()