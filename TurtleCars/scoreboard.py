from turtle import Turtle

FONT=("Courier",15,"bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=0
        self.update_score()
    def update_score(self):
        self.penup()
        self.level+=1
        self.clear()
        self.hideturtle()
        self.speed("fastest")
        self.goto(-230,220)
        self.write(arg=f"Level: {self.level}",align="left",font=FONT)
        self.high_score()
    def high_score(self):
        with open("DAY23\highscore.txt","r+") as file:
            self.max_score=file.read()
            if self.level>int(self.max_score):
                self.max_score=self.level
            self.goto(230,220)
            self.write(arg=f"Max Level: {self.max_score}",align="right",font=FONT)
            file.seek(0)
            file.write(str(self.max_score))
    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER!",align="center",font=FONT)
            