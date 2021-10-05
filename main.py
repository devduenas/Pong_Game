from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Practise Pong Game")
screen.tracer(0)

l_paddle = Paddle((-388, 0))
r_paddle = Paddle((380, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.slide_up, "Up")
screen.onkey(r_paddle.slide_down, "Down")
screen.onkey(l_paddle.slide_up, "w")
screen.onkey(l_paddle.slide_down, "s")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    # Bounce wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()
    # Bounce paddle
    if ball.distance(r_paddle) < 60 and ball.xcor() > 368 or ball.distance(l_paddle) < 60 and ball.xcor() < -368:
        ball.bounce_paddle()
    # Scoring
    if ball.xcor() > 400:
        scoreboard.r_points()
        ball.reset_game()

    if ball.xcor() < -410:
        scoreboard.l_points()
        ball.reset_game()


screen.exitonclick()
