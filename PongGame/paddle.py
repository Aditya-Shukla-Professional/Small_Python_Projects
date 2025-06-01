from turtle import Turtle

STARTING_POSITION=[(-360,0),(360,0)]
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.pongs=[]
        self.create_paddle()
    def create_paddle(self):
        for pos in STARTING_POSITION:
            pong=Turtle(shape="square")
            pong.shapesize(stretch_len=1,stretch_wid=5)
            pong.speed("fastest")
            pong.penup()
            pong.color("white")
            pong.goto(pos)
            self.pongs.append(pong)
    def r_paddle_up(self):
        self.pongs[1].goto(self.pongs[1].xcor(),self.pongs[1].ycor()+20)
    def r_paddle_down(self):
        self.pongs[1].goto(self.pongs[1].xcor(),self.pongs[1].ycor()-20)
    def l_paddle_up(self):
        self.pongs[0].goto(self.pongs[0].xcor(),self.pongs[0].ycor()+20)
    def l_paddle_down(self):
        self.pongs[0].goto(self.pongs[0].xcor(),self.pongs[0].ycor()-20)

        
