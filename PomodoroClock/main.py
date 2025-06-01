from tkinter import *
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
IMAGE=r"DAY28\tomato.png"
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps=0
    label.config(text="Timer",fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")
    window.after_cancel(timer)
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    # work_sec=3
    # short_break_sec=2
    # long_break_sec=3
    if reps%2!=0:
        count_down(work_sec-1)
        label.config(text="Work",fg=GREEN)
    elif reps%2==0 and reps%8!=0:
        count_down(short_break_sec-1)
        label.config(text="Short Break",fg=PINK)
    else:
        count_down(long_break_sec-1)
        label.config(text="Long Break",fg=RED)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    canvas.itemconfig(timer_text, text=f"{count//60 if (count//60)>0 else "00"}:{count%60 if (count%60)>9 else f"0{count%60}"}")
    if count>0:
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        num=math.floor(reps/2)
        mark=num*"✔️"
        check_marks.config(text=mark)
        if (reps/2)>4:
            reset_timer()
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

label=Label(text="Timer",bg=YELLOW,font=(FONT_NAME,"40","bold"),fg=GREEN)
label.grid(row=0,column=1)

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file=IMAGE)
canvas.create_image(100,112,image=tomato_img)
timer_text=canvas.create_text(100,130,text="00:00",font=(FONT_NAME,"35","bold"),fill="white")
canvas.grid(row=1,column=1)

start_btn=Button(text="Start",padx=10,highlightthickness=0,command=start_timer)
start_btn.grid(row=2,column=0)

reset_btn=Button(text="Reset",padx=10,highlightthickness=0,comman=reset_timer)
reset_btn.grid(row=2,column=2)

check_marks=Label(bg=YELLOW,fg=GREEN,font=(FONT_NAME,"12","bold"))
check_marks.grid(row=3,column=1)

window.mainloop()