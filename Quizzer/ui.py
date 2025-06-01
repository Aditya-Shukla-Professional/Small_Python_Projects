from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.score=0
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.label=Label(text="Score: 0",font=("Arial","20","italic"),bg=THEME_COLOR,fg="white")
        self.label.grid(row=0,column=1)

        self.canvas=Canvas(width=300,height=250,bg="white",highlightthickness=0)
        self.question=self.canvas.create_text(150,125,text="Some Question Text",font=("Arial","20","italic"),fill=THEME_COLOR,width=280)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        self.true_img=PhotoImage(file=r"DAY34\images\true.png")
        self.right_btn=Button(image=self.true_img, highlightthickness=0,command=self.true_pressed)
        self.right_btn.grid(row=2,column=0)

        self.false_img=PhotoImage(file=r"DAY34\images\false.png")
        self.wrong_btn=Button(image=self.false_img, highlightthickness=0,command=self.false_pressed)
        self.wrong_btn.grid(row=2,column=1)

        self.get_next_question()
        
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question,text=q_text)
        else:
            self.label.config(text=f"You've reached the end of the quiz your score: {self.score}/10")
            self.right_btn.config(state="disabled")
            self.wrong_btn.config(state="disabled")
        self.canvas.config(bg="white")


    def true_pressed(self):
        is_right=self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right=self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.score+=1
            self.canvas.config(bg="green")
            self.label.config(text=f"Score: {self.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,lambda:self.get_next_question())

