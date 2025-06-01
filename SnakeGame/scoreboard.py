from turtle import Turtle
FONT=("Courier",20,"normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.goto(-270,260)
        self.write(arg=f"Score: {self.score}",align="left",font=FONT)
        self.score+=1
        self.high_score()
    def game_over(self):
        self.goto(0,0)
        self.write(arg="Game Over!",align="center",font=FONT)
    def high_score(self):
        with open(r"DAY20\score.txt","r+") as file:
            self.max_score=file.read()
            if self.score>int(self.max_score):
                file.seek(0)
                file.write(str(self.score))
            self.goto(270,260)
            self.write(arg=f"HighScore: {self.max_score}",align="right",font=FONT)

