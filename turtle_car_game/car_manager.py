COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random


class CarManager:

    def __init__(self):
        self.all_cars = []

    def make_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1.5, stretch_len=2.5)
            new_car.color(random.choice(COLORS))
            y = random.randint(-240, 250)
            new_car.goto(300, y)
            self.all_cars.append(new_car)

    def keep_moving(self, level):
        for car in self.all_cars:
            if level == 1 :
                car.back(STARTING_MOVE_DISTANCE)
            else:
                car.back(MOVE_INCREMENT)




