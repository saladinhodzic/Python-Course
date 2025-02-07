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
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_countdown():
    window.after_cancel(timer)
    canvas.itemconfig(canvas_text,text="00:00")
    checkmark.config(text="")
    state.config(text="Timer",fg=GREEN)
    global reps
    reps = 0
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps+=1
    countdown_seconds = WORK_MIN * 60
    short_break =SHORT_BREAK_MIN * 60
    long_break =LONG_BREAK_MIN * 60
    if reps == 8:
        countdown(round(long_break))
        state["text"] = "Long Break"
        state["fg"] = RED
        checkmark["text"] += CHECKMARK
        
    if reps % 2 != 0:
        countdown(round(countdown_seconds))
        state["text"] = "Work"
    else:
        countdown(round(short_break))
        state["text"] = "Break"
        checkmark["text"] += CHECKMARK
        state["fg"] = PINK
        
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):
    minutes = count // 60
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(canvas_text,text = f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000,countdown,count-1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

state = Label(text="Timer",bg=YELLOW,fg=GREEN,font=(FONT_NAME,35,"bold"))
state.grid(column=1,row=0)

canvas = Canvas(height=250,width=200,bg=YELLOW,highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image = tomato)
canvas_text =canvas.create_text(103,130,text="00:00",fill="white",font=(FONT_NAME,30,"bold"))
canvas.grid(column=1,row=1)

start = Button(text="Start",command=start_timer)
start.grid(column=0,row=2)

reset = Button(text="Reset",command=reset_countdown)
reset.grid(column=2,row=2)

checkmark = Label(text="",fg=GREEN,bg=YELLOW,font=(25))
checkmark.grid(column=1,row=3)


window.mainloop()