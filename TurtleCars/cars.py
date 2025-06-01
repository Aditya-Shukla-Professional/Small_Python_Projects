from turtle import Turtle
import random

car_color=["red","green","yellow","blue","purple","violet","indigo","orange"]
STARTING_MOVE_DISTANCE=10
MOVE_INCREMENT=5

class CarManager():
    def __init__(self):
        self.all_cars=[]
        self.car_creator()
    def car_creator(self):
        x_car=200
        y_car=random.randint(-150,160)
        new_car=Turtle("square")
        new_car.penup()
        new_car.speed("fastest")
        new_car.shapesize(stretch_len=2,stretch_wid=1)
        new_car.color(random.choice(car_color))
        new_car.goto(x_car,y_car)
        self.all_cars.append(new_car)
    def move(self):
        for car in self.all_cars:
            car.goto(car.xcor()-STARTING_MOVE_DISTANCE,car.ycor())