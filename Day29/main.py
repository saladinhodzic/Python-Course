from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
import json
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    nr_letters = random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)
    password=[random.choice(letters) for _ in range(nr_letters)]
    password+=[random.choice(symbols) for _ in range(nr_symbols)]
    password+=[random.choice(numbers) for _ in range(nr_numbers)]
    random.shuffle(password)

    new_pass = ''.join(password)
    input_3.insert(0,new_pass)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_password():
    website = input_1.get()
    email = input_2.get()
    password = input_3.get()
    data_dict = {website:{"email":email, "password": password}}
    if len(website) == 0 or len(email) ==0 or len(password)==0:
        messagebox.showerror(title="ERROR",message="Please dont leave inputs empty.")
        return
    is_ok = messagebox.askokcancel(title=website,message=f"Your email {email}\nYour password {password}\nIs it okay to proceed?")
    if is_ok:
        with open("data.json") as data_file:
            data = json.load(data_file)
            data.update(data_dict)
        with open("data.json",'w') as data_file:
            json.dump(data,data_file,indent=4)
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
button_1 = Button(text="Generate Password",command=generate)
button_1.grid(column=2,row=3)

button_2 = Button(text="Add",width=35,command=add_password)
button_2.grid(column=1,row=4,columnspan=2)







window.mainloop()