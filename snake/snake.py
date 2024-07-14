from turtle import Turtle, Screen

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    # Make a square snake of 3 squares
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in STARTING_POS:
            self.add_segment(position)

    def add_segment(self, position):
            snake = Turtle()
            snake.shape("circle")
            snake.color("white")
            snake.penup()
            snake.goto(position)
            self.snake_body.append(snake)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def move(self):
        for seg in range(len(self.snake_body) - 1, 0, -1):
            x = self.snake_body[seg - 1].xcor()
            y = self.snake_body[seg - 1].ycor()
            self.snake_body[seg].goto(x, y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() == DOWN:
            return
        else:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
