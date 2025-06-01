from turtle import Turtle

STARTING_POSITION=[(0,0),(-20,0),(-40,0)]
MOVE_FORWARD=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)
    def add_segment(self,position):
        turtle=Turtle(shape="square")
        turtle.penup()
        turtle.color("white")
        turtle.goto(position)
        self.segments.append(turtle)
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_FORWARD)
    def up(self):
        self.head.setheading(UP) if self.head.heading()!=DOWN else None
    def down(self):
        self.head.setheading(DOWN) if self.head.heading()!=UP else None
    def left(self):
        self.head.setheading(LEFT) if self.head.heading()!=RIGHT else None
    def right(self):
        self.head.setheading(RIGHT) if self.head.heading()!=LEFT else None

    