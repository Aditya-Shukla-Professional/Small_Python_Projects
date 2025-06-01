from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move=10
        self.y_move=10
        self.move_speed=1
    def move(self):
        x_cor=self.xcor()+self.x_move+self.move_speed
        y_cor=self.ycor()+self.y_move+self.move_speed
        self.goto(x_cor,y_cor)
    def bounce_y(self):
            self.y_move*=-1
    def bounce_x(self):
            self.x_move*=-1
            self.move_speed*=1.5
        