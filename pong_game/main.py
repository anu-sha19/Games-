from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score_board import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Arcade")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
score = Scoreboard()

#middle dot
dot = Turtle()
x = 0
y=300
dot.hideturtle()
dot.penup()
dot.color("white")
dot.goto(x, y)
dot.pendown()
dot.setheading(270)
while dot.ycor() >= -y:
    dot.forward(10)
    dot.penup()
    dot.forward(10)
    dot.pendown()

game_on = True
# Create a paddle towards the right

screen.listen()
screen.onkey(fun=r_paddle.move_up, key="Up")
screen.onkey(fun=r_paddle.move_down, key="Down")
screen.onkey(fun=l_paddle.move_up, key="w")
screen.onkey(fun=l_paddle.move_down, key="s")

t = 0.05
while game_on:
    time.sleep(t)
    screen.update()
    ball.move()

    #detect wall collision
    if ball.ycor() >= 250 or ball.ycor() <= -250 :
        #bounce the ball
        ball.bounce_y()

    #collision with paddle
    if ball.distance(r_paddle)<50 and ball.xcor()> 340 or ball.distance(l_paddle)<50 and ball.xcor()< -340:
        ball.bounce_x()
        if t >= 0.02:
            t -= 0.005

    #detect when ball misses the right paddle
    if ball.xcor()> 360:
        score.update_score('l')
        ball.reset()
    # check which side scores 10 first
    if score.l_score > 9 :
        score.winner()
        game_on = False


    # detect when ball misses the left paddle
    if ball.xcor()< -380:
        score.update_score('r')
        ball.reset()
    #check which side scores 10 first
    if score.r_score > 9 :
        score.winner()
        game_on = False


screen.exitonclick()
