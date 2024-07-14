import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkey(fun=player.move_up, key="Up")

car = CarManager()
game_is_on = True

level = 1
score = Scoreboard(level)
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.make_cars()
    car.keep_moving(level)

    for cars in car.all_cars:
        if cars.distance(player) < 33:
            game_is_on = False
            score.game_over()

    if player.ycor() > 280:
        level += 1
        player.winner()
        score.clear()
        score = Scoreboard(level)

screen.exitonclick()
