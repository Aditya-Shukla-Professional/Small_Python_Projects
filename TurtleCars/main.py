from turtle import Screen
from cars import CarManager
from walker import Tut
from time import sleep
from scoreboard import Scoreboard
import random

screen=Screen()
car_manager=CarManager()
tut=Tut()
screen.tracer(0)
scoreboard=Scoreboard()
screen.setup(width=500,height=500)
screen.listen()

game_is_on=True
while game_is_on:
    sleep(0.1)
    screen.update()
    create=random.randint(0,5)
    car_manager.move()
    if create==0:
        car_manager.car_creator()
    if tut.ycor()>230:
        scoreboard.update_score()
        tut.start_line()
    for car in car_manager.all_cars:
        if car.distance(tut)<20:
            game_is_on=False
            scoreboard.game_over()
    screen.onkeypress(tut.forward,"w")


screen.mainloop()