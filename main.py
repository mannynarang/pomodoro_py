import tkinter
import time
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

reps = 0
timer = None

def reset():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    timer_label.config(text="Timer", font=(FONT_NAME, 50, "bold"))
    checkmark.config(text="✔")
    reps = 0


def secs(s):
    global timer
    count_mins = math.floor(s / 60)
    count_sec = s % 60

    timer = window.after(1000, secs, s - 1)
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if s >= 0:
        canvas.itemconfig(timer_text, text=f"{count_mins}:{count_sec}")
    else:
        window.after_cancel(timer)
        start_timer()



def start_timer():
    global reps


    reps += 1
    # do work
    print(reps)
    if reps % 8 == 0:
        # break time LONG_BREAK_MIN = 10
        timer_label.config(text="Long Break", fg=RED)
        secs(LONG_BREAK_MIN*60)
    elif reps % 2 == 0:
        timer_label.config(text="Short Break", fg=PINK)
        # break time SHORT_BREAK_MIN = 5
        checkmark.config(text=checkmark['text']+"✔")
        secs(SHORT_BREAK_MIN*60)
    else:
        timer_label.config(text="Working", fg=GREEN)
        secs(WORK_MIN*60)


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.minsize(width=200, height=200)
window.config(padx=100, pady=50, bg=YELLOW)
window.title("Pomodoro")

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo_image = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo_image)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)
timer_label = tkinter.Label(text="Timer", font=(FONT_NAME, 50, "bold"))
timer_label.config(bg=YELLOW, fg="GREEN")
timer_label.grid(row=0, column=1)

start_button = tkinter.Button(text="Start", bg=YELLOW)
start_button.grid(row=2, column=0)
start_button.config(command=start_timer)
checkmark = tkinter.Label(text="✔")
checkmark.config(fg=GREEN, bg=YELLOW)
checkmark.grid(row=3, column=1)
reset_button = tkinter.Button(text="Reset", bg=YELLOW)
reset_button.grid(row=2, column=2)
reset_button.config(command=reset)


# secs()
window.mainloop()
