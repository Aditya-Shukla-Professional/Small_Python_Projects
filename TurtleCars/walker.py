from turtle import Turtle

MOVE_INCREMENT=10

class Tut(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.speed("fastest")
        self.setheading(90)
        self.start_line()
    def forward(self):
        x_cor=self.xcor()
        y_cor=self.ycor()
        self.goto(x_cor,y_cor+MOVE_INCREMENT)
    def start_line(self):
        self.goto(0,-200)