from tkinter import *
import math

reps = 0
timer = None

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text= "00:00")
    title_label.config(text="Timer", font=("TImes New Roma", 50, "bold"))
    checkmarks.config(text="")
    global reps
    reps = 0

def start_timer():
    global reps 
    reps += 1
    work_sec = 25 * 60
    short_break_sec = 5 * 60

    if reps % 8 == 0:
        title_label.config(text="Break")
        count_down(short_break_sec)
    elif reps %  2 == 0:
        title_label.config(text="Break")
        count_down(short_break_sec)
    else: 
        title_label.config(text="Work")
        count_down(work_sec)

def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}: {count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔"
        checkmarks.config(text=marks)

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=100)
canvas = Canvas(width=200, height=224)
title_label = Label(text="Timer", fg="#006400", font=("Time New Roma", 50, "bold"))
title_label.grid(column=1, row=0)
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)
tomato_image = PhotoImage(file="assets/tomato.png")
canvas.create_image(103,112, image=tomato_image)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=("Time New Roma", 35, "bold"))
canvas.grid(column=1, row=1)
checkmarks = Label(fg="#006400", font=("Time New Roma", 20, "bold"))
checkmarks.grid(column=1, row=3)
window.mainloop()