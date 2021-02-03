from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.colormode(255)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=r_paddle.move_up)
screen.onkey(key="Down", fun=r_paddle.move_down)
screen.onkey(key="a", fun=l_paddle.move_up)
screen.onkey(key="z", fun=l_paddle.move_down)

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if abs(ball.ycor()) > 290:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x()

    # Detect Right Paddle Miss
    if ball.xcor() > 380:
        score.l_point()
        ball.reset_position()

    #Detect Left Paddle Miss
    if ball.xcor() < -380:
        score.r_point()
        ball.reset_position()

screen.exitonclick()