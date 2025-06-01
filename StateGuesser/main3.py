from turtle import Turtle, Screen, textinput
import pandas as pd

FONT=("Arial",10,"normal")
screen=Screen()
screen.bgpic(r"DAY25\blank_states_img.gif")
turtle=Turtle()
turtle.penup()
turtle.hideturtle()

game_is_on=True
correct=0
data=pd.read_csv(r"DAY25\50_states.csv")
while game_is_on:
    ask=textinput(f"{correct}/50 States Correct","What's another state name?").lower()
    for state in data.state:
        if ask==state.lower():
            correct+=1
            loc=data[data.state==state]
            turtle.goto(loc.iloc[0, 1],loc.iloc[0, 2])
            turtle.write(arg=state,align="center",font=FONT)
            read=pd.read_csv(r"DAY25\forgot.csv")
            for i in read.state:
                if i==state:
                    index=read[read["state"]==state].index
                    read.drop(index[0],inplace=True)
            read.to_csv(r"DAY25\forgot.csv", index=False)
        elif ask=="exit":
            game_is_on=False
            screen.bye()

screen.mainloop()