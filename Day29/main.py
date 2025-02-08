from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_password():
    website = input_1.get()
    email = input_2.get()
    password = input_3.get()
    if len(website) == 0 or len(email) ==0 or len(password)==0:
        messagebox.showerror(title="ERROR",message="Please dont leave inputs empty.")
        return
    is_ok = messagebox.askokcancel(title=website,message=f"Your email {email}\nYour password {password}\nIs it okay to proceed?")
    if is_ok:
        with open("data.txt",'a') as data:
            data.write(f"{website} | {email} | {password}\n")
            input_1.delete(0,END)
            input_3.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=50,pady=50)
logo = PhotoImage(file="logo.png")
canvas = Canvas(height=200,width=200)
canvas.create_image(100,100,image = logo)
canvas.grid(column=1,row=0)

label_1= Label(text="Website: ")
label_1.grid(column=0,row=1)
input_1 = Entry(width=35)
input_1.focus()
input_1.grid(column=1,row=1,columnspan=2)

label_2 = Label(text="Email/Username: ")
label_2.grid(column=0,row=2)
input_2 = Entry(width=35)
input_2.insert(0,"hsaladin06@gmail.com")
input_2.grid(column=1,row=2,columnspan=2)

label_3 = Label(text="Password: ")
label_3.grid(column=0,row=3)
input_3 = Entry(width=21)
input_3.grid(column=1,row=3)
button_1 = Button(text="Generate Password")
button_1.grid(column=2,row=3)

button_2 = Button(text="Add",width=35,command=add_password)
button_2.grid(column=1,row=4,columnspan=2)







window.mainloop()