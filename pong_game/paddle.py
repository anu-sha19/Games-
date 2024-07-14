from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(x, y)

    def move_up(self):
        y = self.ycor()
        self.goto(self.xcor(), y + 20)

    def move_down(self):
        y = self.ycor()
        self.goto(self.xcor(), y - 20)
