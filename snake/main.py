import time
from snake import Snake
from food import Food
from score_board import Score
from turtle import Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  #Animation off so that snake doesn't walk like caterpiller. Nothing heppens until you update()

snake = Snake()
food = Food()
score =0
score_keeper = Score()

#Keyboard controls to move the snake in the desired direction
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

#move the snake
game_on = True
while game_on:
    snake.move()
    screen.update()
    time.sleep(0.2)

    #detect collision with food
    if snake.head.distance(food) < 15:
        snake.extend() #extend the tail after eating
        food.refresh()
        score_keeper.increase_score()

    #detect collision with wall
    if snake.head.xcor() >= 290 or snake.head.xcor() <= -290 or snake.head.ycor() >= 290 or snake.head.ycor() <= -290:
        score_keeper.game_over()
        game_on = False

    #detect collision with tail
    for segment in snake.snake_body[1:]:
           if snake.head.distance(segment) < 10:
               score_keeper.game_over()
               game_on = False







screen.exitonclick()
