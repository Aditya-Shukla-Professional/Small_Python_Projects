from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard

screen=Screen()
paddle=Paddle()
ball=Ball()
scoreboard=Scoreboard()

screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong Game")
screen.listen()
screen.onkeypress(paddle.l_paddle_up,"w")
screen.onkeypress(paddle.l_paddle_down,"s")
screen.onkeypress(paddle.r_paddle_up,"Up")
screen.onkeypress(paddle.r_paddle_down,"Down")

game_is_on=True
while game_is_on:
    sleep(0.1)
    screen.update()
    ball.move()
    if (ball.distance(paddle.pongs[1])<50 and ball.xcor()>340):
        ball.bounce_x()
        scoreboard.update_score_r()
    if (ball.distance(paddle.pongs[0])<50 and ball.xcor()<-340):
        ball.bounce_x()
        scoreboard.update_score_l()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    if ball.xcor()>390 or ball.xcor()<-390:
        game_is_on=False
    scoreboard.display_score()
scoreboard.game_over()
screen.mainloop()