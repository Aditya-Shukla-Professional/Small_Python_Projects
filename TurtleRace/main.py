from turtle import Turtle,Screen
import random
screen=Screen()
screen.setup(width=500,height=400)
is_race_on=False
user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ").lower()
turtle_color=["red","blue","green","yellow","orange","purple"]
y_pos=[-70,-40,-10,20,50,80]
lst_turtle=[]
for i in range(0,6):
    turtle=Turtle(shape="turtle")
    turtle.color(turtle_color[i])
    turtle.penup()
    turtle.goto(x=-230,y=y_pos[i])
    lst_turtle.append(turtle)
if user_bet:
    is_race_on=True
while is_race_on:
    for turtle in lst_turtle:
        random_dis=random.randint(0,10)
        turtle.forward(random_dis)
        if turtle.xcor()>230:
            is_race_on=False
            print("You won!") if user_bet==turtle.color() else print(f"You lost. The {turtle.pencolor()} turtle won.")
            screen.bye()
            break
screen.mainloop()
