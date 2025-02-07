from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✔"

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

state = Label(text="Timer",bg=YELLOW,fg=GREEN,font=(FONT_NAME,35,"bold"))
state.grid(column=1,row=0)

canvas = Canvas(height=250,width=200,bg=YELLOW,highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image = tomato)
canvas.create_text(103,130,text="00:00",fill="white",font=(FONT_NAME,30,"bold"))
canvas.grid(column=1,row=1)

start = Button(text="Start")
start.grid(column=0,row=2)

reset = Button(text="Reset")
reset.grid(column=2,row=2)

checkmark = Label(text=CHECKMARK,fg=GREEN,bg=YELLOW,font=(25))
checkmark.grid(column=1,row=3)


window.mainloop()