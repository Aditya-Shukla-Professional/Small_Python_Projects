from turtle import Turtle 

FONT=("Courier",40,"normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=[0,0]
        self.hideturtle()
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.display_score()
    def display_score(self):
        self.clear()
        self.goto(0,240)
        self.write(arg=f"{self.score[0]}:{self.score[1]}",align="center",font=FONT)
    def update_score_l(self):
        self.score[0]+=1
    def update_score_r(self):
        self.score[1]+=1
    def game_over(self):
        self.goto(0,0)
        self.write(arg="Game Over!",align="center",font=FONT)
    
